"""Exact small-world counter-guess lifts; no hash-hardness/source campaign."""
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
L = 2

def canonical(r, m, bottom):
    if bottom and m == 2 and r == 1:
        return None
    return r ^ (m & 1)

def coordinates(p, r, m, c, kind, bottom=False, count=17):
    expected = canonical(r, m, bottom)
    matched = expected is not None and c == expected
    route = p[1] if matched else 1 - p[1]
    if m == 0:
        leaves = [0] * 17
    elif m in (1, 2):
        leaves = [1] * 17
    else:
        leaves = [0] * 17 if kind == 'one' else [0] * 8 + [1] * 9
    out = {(p, route, j, leaf) for j, leaf in enumerate(leaves)}
    if count == 18:
        # A virtual filter tuple; never an actual private secret/tree exposure.
        out.add((p, route, 17, 0 if matched else 1))
    return out

def source(q, s, f, nonce_tape, kind, bottom):
    p = (s, s ^ f)
    seen, records, replies = {}, [], [('prekey', 0), ('pk', p)]
    for call in range(q):
        if call == 0:
            m = 0
        elif call == 1:
            m = 1 + (seen[0] ^ p[1])  # Legitimate adaptation to prior nonce/root.
        else:
            m = 0  # Restore/repeated message reuses its original nonce.
        fresh = m not in seen
        if fresh:
            seen[m] = nonce_tape[len(seen)]
        r = seen[m]
        c = canonical(r, m, bottom)
        if fresh:
            records.append((len(seen), m, r, c))
        if c is None:
            replies.append(('natural_bottom', m))
            return tuple(replies), records, None, False
        replies.append(('completed', m, r, c, f))
    star = (0, 3, 1)  # R*, freshM*, acceptedc*: canonical(0,3)=1.
    target = coordinates(p, *star, kind, bottom)
    exposure = set()
    for _, m, r, c in records:
        assert c is not None
        exposure |= coordinates(p, r, m, c, kind, bottom)
    covered = target <= exposure
    replies.append(('final', star, covered))
    return tuple(replies), records, star, covered

rows = []
total_worlds = 0
nonwitness_wrong_guess_win = False
for q, kind, bottom in [(1, 'one', False), (2, 'one', False), (2, 'two', False), (3, 'two', True)]:
    k = min(17, q)
    Q = 1 << (q-1).bit_length()
    nonce_slots = min(q, 2)
    source_weight = Fraction(1, 4 * (1 << nonce_slots))
    guess_weight = Fraction(1, L ** nonce_slots)
    selector_weight = Fraction(1, Q ** k)
    p_source = p_all = p_sparse = Fraction(0)
    p_all18 = p_sparse18 = Fraction(0)
    view_by_guesses = Counter()
    for s, f, nonce_tape in product(range(2), range(2), product(range(2), repeat=nonce_slots)):
        view, records, star, covered = source(q, s, f, nonce_tape, kind, bottom)
        p = (s, s ^ f)
        p_source += source_weight * covered
        firsts = {ordinal: (m, r, c0) for ordinal, m, r, c0 in records}
        for guesses in product(range(L), repeat=nonce_slots):
            # ALL-label route ignores mapped guessed targets in its source view.
            repeated_view, repeated_records, repeated_star, repeated_covered = source(q, s, f, nonce_tape, kind, bottom)
            assert (view, records, star, covered) == (repeated_view, repeated_records, repeated_star, repeated_covered)
            view_by_guesses[(guesses, view)] += source_weight
            registered = set()
            registered18 = set()
            for ordinal, (m, r, c0) in firsts.items():
                g = guesses[ordinal-1]
                registered |= coordinates(p, r, m, g, kind, bottom)
                registered18 |= coordinates(p, r, m, g, kind, bottom, 18)
            all_win = bool(covered and coordinates(p, *star, kind, bottom) <= registered)
            all_win18 = bool(covered and coordinates(p, *star, kind, bottom, 18) <= registered18)
            assert all_win == all_win18
            p_all += source_weight * guess_weight * all_win
            p_all18 += source_weight * guess_weight * all_win18
            if kind == 'one' and q == 2 and all_win:
                _, _, second_c = firsts[2]
                nonwitness_wrong_guess_win |= guesses[1] != second_c
            for selectors in product(range(1, Q+1), repeat=k):
                selected = set(selectors) & set(firsts)
                # SPARSE route artificially aborts if any queried guess is wrong.
                matches = all(firsts[o][2] is not None and guesses[o-1] == firsts[o][2] for o in selected)
                sparse_reg = set()
                sparse_reg18 = set()
                for o in selected:
                    m, r, _ = firsts[o]
                    sparse_reg |= coordinates(p, r, m, guesses[o-1], kind, bottom)
                    sparse_reg18 |= coordinates(p, r, m, guesses[o-1], kind, bottom, 18)
                sparse_win = bool(covered and matches and coordinates(p, *star, kind, bottom) <= sparse_reg)
                sparse_win18 = bool(covered and matches and coordinates(p, *star, kind, bottom, 18) <= sparse_reg18)
                assert sparse_win == sparse_win18
                p_sparse += source_weight * guess_weight * selector_weight * sparse_win
                p_sparse18 += source_weight * guess_weight * selector_weight * sparse_win18
                assert len(selected) <= k
                total_worlds += 1
    # Every fixed guess vector gives exactly the same FULL toy source-view law.
    distributions = []
    for guesses in product(range(L), repeat=nonce_slots):
        distributions.append({view: weight for (g, view), weight in view_by_guesses.items() if g == guesses})
    assert all(d == distributions[0] for d in distributions)
    assert p_all >= p_source / L ** k
    assert p_sparse >= p_source / (Q * L) ** k
    assert p_all18 == p_all and p_sparse18 == p_sparse
    rows.append({'q_initiated': q, 'kind': kind, 'natural_bottom_model': bottom,
                 'source_C_probability': str(p_source), 'all_label_primary_success': str(p_all),
                 'sparse_primary_success': str(p_sparse), 'all_label_loss_envelope': L ** k,
                 'sparse_loss_envelope': (Q * L) ** k, 'Q_pad': Q, 'max_sparse_targets': k,
                 'source_view_guess_independent': True, 'virtual18_needs_no_extra_witness': True})
assert nonwitness_wrong_guess_win
assert rows[-1]['source_C_probability'] == '3/4'
result = {
    'status': 'PASS_EXACT_FINITE_ALL_LABEL_AND_SPARSE_PRIMARY_ITSR_LIFTS',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'enumerated_selector_nonce_guess_worlds': total_worlds,
    'rows': rows,
    'wrong_nonwitness_guess_can_still_win_all_label_route': nonwitness_wrong_guess_win,
    'source17_real_coordinates_only': True,
    'optional_virtual18_filter_not_a_secret_tree': True,
    'natural_bottom_mass_unnormalized': True,
    'scope': 'Exact toy metadata/coverage probabilities; no SHA hardness, source signature run, timing campaign, global kernel proof or numeric security certificate.',
}
out = HERE / 'PROBABILISTIC-LIFT-CONTROLS.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))

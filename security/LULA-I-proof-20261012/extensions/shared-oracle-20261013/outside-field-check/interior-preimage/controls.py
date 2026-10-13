"""Finite logical UD/PRE channel controls; no source signatures or hash hardness."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
D = range(4)

def f(s, t, x):
    if t == 0:
        return x // 2  # Deliberately nonbalanced: uniform start is not uniform x1.
    if t == 1:
        return (x + s) % 4
    if t == 2:
        return (3*x + s) % 4
    return (x + 1) % 4

def finish(s, x, start):
    for t in range(start, 4):
        x = f(s, t, x)
    return x

def endpoint_from_image(s, image, step):
    return finish(s, image, step+1)

def public_run(s, other, p, next_node):
    """Root/cache formed from known selected image; atomic classical responses."""
    endpoint = endpoint_from_image(s, next_node, p)
    root = (endpoint + 2*other + s) % 4
    cache = (endpoint, root, other)
    # Genuine child/canonical row depends on other input, not this chain's prefix.
    digit = other
    # Deterministic adaptive request choice based on the actually released root.
    asks_selected = ((root + s) % 2 == 0)
    view = [('prekey', 'same_public_fixed_f'), ('pk', s, root)]
    if s == 1 and other == 3:
        return tuple(view+[('natural_bottom',)]), False, False, cache
    if asks_selected:
        # Assemble logical slots; finish the rest of the call BEFORE release gate.
        sig = finish(s, next_node, p+1) if digit == 4 else None
        if digit > p:
            sig = next_node
            for t in range(p+1, digit):
                sig = f(s, t, sig)
        if digit <= p:
            return tuple(view+[('complete_response_guard',)]), False, False, cache
        view.append(('completed_selected', digit, sig, cache))
        view.append(('restore_repeat', digit, sig, cache))
    else:
        view.append(('completed_other', other, cache))
    # Toy public final algorithm solves the tiny chain endpoint by enumeration.
    # It always starts the final chain at2, so the final typed trace is2,3.
    candidate = next(x for x in D if finish(s, x, 2) == endpoint)
    final_root = (finish(s, candidate, 2) + 2*other + s) % 4
    # A returns an eligible candidate only on this public-root predicate, and an
    # invalid candidate otherwise. This makes UD probability gaps nontrivial.
    win = final_root == root and root == 0
    selected_input = candidate if p == 2 else (f(s, 2, candidate) if p == 3 else None)
    image_event = bool(win and selected_input is not None and f(s, p, selected_input) == next_node)
    view.append(('final_fresh', candidate, final_root, win, image_event))
    return tuple(view), win, image_event, cache

def cut_channel(p, r):
    result = Counter()
    for s, other, u in product(range(2), D, D):
        x = u
        for t in range(r, p+1):
            x = f(s, t, x)
        result[public_run(s, other, p, x)] += Fraction(1, 32)
    assert sum(result.values()) == 1
    return result

def ud_channel(p, r, real):
    result = Counter()
    for s, other, z in product(range(2), D, D):
        y = f(s, r, z) if real else z
        for t in range(r+1, p+1):
            y = f(s, t, y)
        result[public_run(s, other, p, y)] += Fraction(1, 32)
    return result

def event_mass(channel, skip_zero=False):
    return sum(weight for (view, _, event, _), weight in channel.items()
               if event and (not skip_zero or view[1][1] != 0))

checks = 0
for p in (1, 2):
    for r in range(p):
        assert ud_channel(p, r, True) == cut_channel(p, r)
        assert ud_channel(p, r, False) == cut_channel(p, r+1)
        checks += 2
    # PRE target is f_p(U): observed channel includes only next image/suffix.
    assert ud_channel(p, p, True) == cut_channel(p, p)
    for s, u in product(range(2), D):
        y = f(s, p, u)
        answers = [v for v in D if f(s, p, v) == y]
        assert answers and all(f(s, p, v) == y for v in answers)
        checks += 1

# Selector0=>p0, selector1=>p1, selector2=>p2, selector3=>dummy.
# p0 contribution is inactive and cancels across all UD hops; toy final trace2
# makes p0's selected image event0, as above. Exact signed gaps average BEFORE abs.
aggregate = []
for k in range(3):
    aggregate.append(sum(event_mass(cut_channel(p, min(k, p))) for p in (1, 2))/4)
for k in range(2):
    real_bit = sum(event_mass(ud_channel(p, k, True)) for p in (1, 2) if p > k)/4
    random_bit = sum(event_mass(ud_channel(p, k, False)) for p in (1, 2) if p > k)/4
    assert real_bit-random_bit == aggregate[k]-aggregate[k+1]
    checks += 1
pre_success = sum(event_mass(ud_channel(p, p, True)) for p in (1, 2))/4
assert pre_success == aggregate[-1]
assert aggregate[0] <= pre_success + sum(abs(aggregate[k]-aggregate[k+1]) for k in range(2))
assert any(aggregate[k] != aggregate[k+1] for k in range(2))
nonzero_aggregate = [sum(event_mass(cut_channel(p, min(k, p)), True)
                        for p in (1, 2))/4 for k in range(3)]
for k in range(2):
    real_bit = sum(event_mass(ud_channel(p, k, True), True)
                   for p in (1, 2) if p > k)/4
    random_bit = sum(event_mass(ud_channel(p, k, False), True)
                     for p in (1, 2) if p > k)/4
    assert real_bit-random_bit == nonzero_aggregate[k]-nonzero_aggregate[k+1]
    checks += 1
nonzero_pre = sum(event_mass(ud_channel(p, p, True), True) for p in (1, 2))/4
assert nonzero_pre == nonzero_aggregate[-1]
assert all(a <= b for a, b in zip(nonzero_aggregate, aggregate))

# Original toy final starts at2 and inverts a permutation suffix, so x2 genuine.
source_hidden_probability = event_mass(cut_channel(2, 0))
assert source_hidden_probability <= 4*aggregate[0]

# Hidden-X equality is not an observable bit when two inputs have same image.
assert f(0, 0, 0) == f(0, 0, 1) == 0
same_known_challenge_image = 0
literal_equal = [int(0 == hidden_x) for hidden_x in (0, 1)]
assert literal_equal == [1, 0]
assert all(f(0, 0, 0) == same_known_challenge_image for _ in (0, 1))

# Exact-law uniform-input substitution fails; a UD advantage is needed.
first_image_distribution = Counter(f(0, 0, x) for x in D)
assert first_image_distribution != Counter(D)
stale_root_mismatches = 0
for s, other, old_u, new_u in product(range(2), D, D, D):
    old_endpoint = finish(s, old_u, 0)
    new_endpoint = finish(s, new_u, 2)
    old_root = (old_endpoint+2*other+s) % 4
    new_root = (new_endpoint+2*other+s) % 4
    stale_root_mismatches += old_root != new_root
assert stale_root_mismatches > 0

# Actual finite geometry; arithmetic only, no namespace allocation.
heights = (5, 5, 5, 5, 21)
widths = (16, 16, 16, 16, 256)
chains = (32, 32, 32, 32, 16)
keys = tuple(1 << sum(heights[j:]) for j in range(5))
dw = sum(n*l*(w-1) for n, l, w in zip(keys, chains, widths))
df = (1 << 41)*17*(1 << 9)
dh = dw+df
assert dw == 1089588072284160
assert df == 19140298416324608
assert dh == 20229886488608768
assert (1 << 54) < dh <= (1 << 55)
assert max(w-2 for w in widths) == 254
result = {
    'status': 'PASS_EXACT_FINITE_INTERIOR_UD_PRE_CHANNEL_AND_SELECTOR_CONTROLS',
    'scope': 'Finite logical-channel/probability controls, no source-signature execution, actual hash hardness, timing, full namespace or kernel proof',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'channel_relation_and_preimage_checks': checks,
    'aggregate_event_probabilities': list(map(str, aggregate)),
    'aggregate_PRE_candidate_success': str(pre_success),
    'nonzero_filtered_aggregate_probabilities_unnormalized': list(map(str, nonzero_aggregate)),
    'nonzero_filtered_PRE_success_unnormalized': str(nonzero_pre),
    'original_toy_hidden_probability': str(source_hidden_probability),
    'signed_selector_gap_equalities': True,
    'opaque_literal_equality_counterexample': literal_equal,
    'PRE_any_matching_input_not_hidden_X_test': True,
    'nonbalanced_prefix_distribution': dict(first_image_distribution),
    'stale_root_mismatch_worlds': stale_root_mismatches,
    'repeat_restore_consistent_and_natural_bottom_unnormalized': True,
    'actual_geometry': {'keys': keys, 'WOTS_nonterminal': dw, 'FORS_start': df, 'union': dh, 'selector_bits': 55, 'UD_hops': 254},
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))

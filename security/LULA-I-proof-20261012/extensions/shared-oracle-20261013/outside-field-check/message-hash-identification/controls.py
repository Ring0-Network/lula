"""Exact finite ITSR-interface discriminators, not LULA/SHA security tests."""
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# One nonce, one route/tree-coordinate, two messages and two counters.
# All counters satisfy the toy filter; honest target policy is first counter.
def digest(message, counter):
    return message if counter == 0 else 0

primary_success = []
variant_success = []
for signed in (0, 1):
    covered = {digest(signed, 0)}
    # Singleton nonce means primary pair freshness is exactly message freshness.
    primary_success.extend(int(digest(candidate, 0) in covered)
                           for candidate in (0, 1) if candidate != signed)
    variant_success.extend(int(digest(candidate, counter) in covered)
                           for candidate, counter in product((0, 1), (0, 1))
                           if candidate != signed)
assert max(primary_success) == 0 and max(variant_success) == 1
assert digest(1, 1) == digest(0, 0) and digest(1, 0) != digest(0, 0)

# A second separation keeps all17 source-coordinate labels and two nonces.
# Artificial full256 words have all real leaves/filter zero and route2R+M
# canonically; accepted counter1 redirects the freshM1 candidate to route2R.
def full_toy_word(r, m, c):
    route = 2*r + (m if c == 0 else 0)
    return route << 53

def full_toy_set(r, m, c):
    d = full_toy_word(r, m, c)
    assert ((d >> 94) & 511) == 0
    route = (d >> 53) & ((1 << 41)-1)
    indices = [(d >> (256-9*(i+1))) & 511 for i in range(17)]
    return {(route, i, leaf) for i, leaf in enumerate(indices)}

for r, m in product((0, 1), repeat=2):
    target = full_toy_set(r, m, 0)
    assert len(target) == 17
    for star_r, star_m in product((0, 1), repeat=2):
        if (star_r, star_m) != (r, m):
            assert not full_toy_set(star_r, star_m, 0) <= target
    if m == 0:
        assert full_toy_set(r, 1, 1) <= target
assert Fraction(sum(full_toy_set(r, 1, 1) <= full_toy_set(r, 0, 0) for r in (0, 1)), 2) == 1

# Fresh nonce per repeated target request differs from a persistent J[M].
fresh_pairs = Counter(product((0, 1), repeat=2))
memo_pairs = Counter({(r, r): 1 for r in (0, 1)})
fresh_agree = Fraction(sum(n for (a, b), n in fresh_pairs.items() if a == b), 4)
memo_agree = Fraction(sum(n for (a, b), n in memo_pairs.items() if a == b), 2)
assert fresh_agree == Fraction(1, 2) and memo_agree == 1
# A reduction that queries once and repeats its saved reply exactly repairs it.
wrapper_pairs = Counter((r, r) for r in (0, 1))
assert wrapper_pairs == memo_pairs

# Genuine source joint state can have uniform public marginal while its
# signature-visible auxiliary relation is destroyed by a substituted root.
source_views = Counter((s, s ^ f, f) for s, f in product((0, 1), repeat=2))
independent_views = Counter(product((0, 1), repeat=3))
source_public = Counter()
independent_public = Counter()
for (s, z, f), count in source_views.items():
    source_public[(s, z)] += Fraction(count, 4)
for (s, z, f), count in independent_views.items():
    independent_public[(s, z)] += Fraction(count, 8)
assert source_public == independent_public
genuine_relation = sum(Fraction(n, 4) for (s, z, f), n in source_views.items() if z == s ^ f)
replacement_relation = sum(Fraction(n, 8) for (s, z, f), n in independent_views.items() if z == s ^ f)
assert genuine_relation == 1 and replacement_relation == Fraction(1, 2)

# A source setup/signer bottom does not imply a conditional successful-row law.
# Target registration followed by a later atomic signing failure need not have
# a separate commit API: a correctly absorbing reduction never wins afterward.
worlds = list(product((False, True), repeat=2))  # hash-search complete, rest-of-sign complete
winning_worlds = [w for w in worlds if all(w)]
assert len(winning_worlds) == 1 and Fraction(len(winning_worlds), len(worlds)) == Fraction(1, 4)
assert all(not (a and b) for a, b in worlds if not b)

# Real source byte frames and digest bit extraction, only public local hashes.
byte_rows = []
for value, message in product((0, 1), (b'', b'a')):
    r = bytes([value]) * 16
    s = bytes([1 - value]) * 16
    z = bytes([2]) * 16
    inner_word = r + s + z + message
    assert len(inner_word) == 48 + len(message)
    u = hashlib.sha256(inner_word).digest()
    assert len(u) == 32
    first = None
    for counter in range(8192):
        outer_word = u + counter.to_bytes(4, 'big') + s
        assert len(outer_word) == 52
        d = hashlib.sha256(outer_word).digest()
        raw = int.from_bytes(d, 'big')
        if ((raw >> 94) & 511) == 0:  # bits153..161 in MSB-first numbering
            first = counter
            indices = tuple((raw >> (256 - 9*(i+1))) & 511 for i in range(17))
            route = (raw >> 53) & ((1 << 41) - 1)
            assert len(indices) == 17
            assert all(0 <= x < 512 for x in indices)
            assert 0 <= route < 1 << 41
            assert ((route >> 5) << 5) | (route & 31) == route
            # The discarded eighteenth index is the filter, not a secret tree.
            assert ((raw >> (256 - 18*9)) & 511) == 0
            zero_lower = raw & (((1 << 128)-1) << 128)
            assert zero_lower >> 128 == raw >> 128
            assert ((zero_lower >> 53) & ((1 << 41)-1)) == 0
            assert ((zero_lower >> 94) & 511) == 0
            byte_rows.append({'R_byte': value, 'message_hex': message.hex(), 'first_counter_within_control_cap': first,
                              'indices': indices, 'route41': route})
            break
    assert first is not None, 'This finite control did not find a passing digest.'

result = {
    'status': 'PASS_EXACT_ITSR_INTERFACE_DISCRIMINATORS_NOT_SOURCE_SECURITY',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'canonical_map_primary_singleton_nonce_max_success': 0,
    'canonical_target_arbitrary_counter_variant_max_success': 1,
    'two_nonce_full17_tuple_counter_separation': True,
    'two_nonce_canonical_fresh_pair_max_success': 0,
    'two_nonce_arbitrary_counter_fresh_message_success': '1',
    'repeated_message_fresh_nonce_agreement': str(fresh_agree),
    'repeated_message_memoized_nonce_agreement': str(memo_agree),
    'one_query_memoizing_wrapper_matches_source_J': True,
    'root_public_marginals_equal_in_countermodel': True,
    'source_root_signature_auxiliary_relation': str(genuine_relation),
    'independent_root_signature_auxiliary_relation': str(replacement_relation),
    'atomic_bottom_unconditioned_success_mass': '1/4',
    'no_commit_interface_needed_on_absorbing_failure': True,
    'literal_full256_two_stage_hash_bit_rows': byte_rows,
    'prefix_projection_route_and_filter_zero_match_helper_statements': True,
    'scope': 'Counter/nonce/root toy logical separations and literal digest extraction only. No SHA hardness, uniformity, LULA forgery, global proof or RO transfer.',
}
out = HERE / 'CONTROL-RESULTS.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'counter_gap': [0, 1], 'actual_byte_rows': len(byte_rows)}, indent=2))

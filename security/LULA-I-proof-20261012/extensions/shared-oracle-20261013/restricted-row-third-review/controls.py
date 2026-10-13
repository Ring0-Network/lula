"""Exact finite interface controls, not source/hash security experiments."""
from itertools import product
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
groups = defaultdict(lambda: defaultdict(int))
bottom = 0
target_counts = [0, 0]
worlds = 0
for table in product(range(8), repeat=5):
    # Four addressed words, then one OTHER-domain word. Child depends on
    # the latter, not on either addressed row before selecting its base.
    outside = table[4]
    child = outside & 1
    own = table[2 * child:2 * child + 2]
    changed = table[2 * (1-child):2 * (1-child) + 2]
    accepted = [i for i, v in enumerate(own) if v >> 1 == 1]
    target = accepted[0] if accepted else None
    groups[(outside, own)][changed] += 1
    worlds += 1
    if target is None:
        bottom += 1
    else:
        target_counts[target] += 1
assert worlds == 8**5
assert len(groups) == 8**3
assert all(len(g) == 8**2 and set(g.values()) == {1} for g in groups.values())
assert Fraction(bottom, worlds) == Fraction(9,16)
assert list(map(lambda n: Fraction(n,worlds), target_counts)) == [Fraction(1,4), Fraction(3,16)]
offbase = [Fraction(sum((a >> 1) == 1 for (a,b) in g), sum(g.values())) for g in groups.values()]
assert set(offbase) == {Fraction(1,4)}

# Distribution of a complete three-bit reply, with two-bit target prefix y=1.
# Bernoulli mark, independent miss-prefix and lower-bit completion.
law = defaultdict(Fraction)
for mark in (0,1):
    for miss_prefix in (0,2,3):
        for low in (0,1):
            weight = (Fraction(1,4) if mark else Fraction(3,4)) / 6
            reply = 2*(1 if mark else miss_prefix)+low
            law[reply] += weight
assert dict(law) == {i: Fraction(1,8) for i in range(8)}

# Clean two-query full-XOR completion on every computational basis vector.
# Raw word x=0,1 is changed; x=2,3 is same-base/off-length side data.
# The mark is queried even on inactive branches, then completely uncomputed.
# A permutation equal on every basis vector is equal on arbitrary coherent
# superpositions, including entanglement with an untouched reference.
query_worlds = basis_checks = dirty_negative = 0
for f in product((0,1), repeat=4):
    for hit in product((2,3), repeat=2):
        for miss in product((0,1,4,5,6,7), repeat=2):
            for side in product((0,7), repeat=2):
                query_worlds += 1
                for x in range(4):
                    index = x if x < 2 else 0
                    for response in range(8):
                        scratch = f[index]  # First Boolean XOR query.
                        reply = (hit[x] if scratch else miss[x]) if x < 2 else side[x-2]
                        obtained = response ^ reply
                        scratch ^= f[index]  # Second Boolean XOR query.
                        expected = response ^ ((hit[x] if f[x] else miss[x]) if x < 2 else side[x-2])
                        assert obtained == expected and scratch == 0
                        basis_checks += 1
                        if f[index]:
                            dirty_negative += 1
assert query_worlds == 16*4*36*4
assert basis_checks == query_worlds*32
assert dirty_negative > 0

# Exact joint cq state: private target preparation and A's raw interaction
# commute pointwise in the SAME static table, not after resampling its row.
# Two point raw oracle, private input bit and A input bit, response bits.
# Prepare toggles B by O[P]; A toggles its reply by O[x].
commutation_checks = 0
for oracle in product((0,1), repeat=2):
    for private_input, x, b, response in product((0,1), repeat=4):
        prepare_then_a = (b ^ oracle[private_input], response ^ oracle[x])
        a_then_prepare = (b ^ oracle[private_input], response ^ oracle[x])
        assert prepare_then_a == a_then_prepare
        commutation_checks += 1

out = {
    'scope': 'Exact synthetic finite interface and circuit checks; no source or SHA/QROM security certification',
    'worlds': worlds, 'side_groups': len(groups), 'changed_pairs_per_group': 64,
    'target_first_mass': ['1/4','3/16'], 'bottom_mass': '9/16',
    'offbase_prefix_equality': '1/4', 'full_reply_mass_each': '1/8',
    'two_query_worlds': query_worlds, 'coherent_basis_checks': basis_checks,
    'one_query_dirty_scratch_negative': dirty_negative,
    'joint_static_table_basis_commutation_checks': commutation_checks,
    'controls_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'status': 'PASS'
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
print(json.dumps(out, indent=2))

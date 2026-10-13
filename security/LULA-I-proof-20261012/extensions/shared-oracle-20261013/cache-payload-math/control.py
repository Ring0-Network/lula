"""Exact finite observer/counter controls; no signature or operational payload code."""
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
N, C = 4, 2
T = {1, 2}

def first(row):
    return next((i for i, d in enumerate(row) if d in T), None)

def row_disintegration_weight(row):
    j = first(row)
    p = Fraction(len(T), N)
    if j is None:
        return (1-p)**C * Fraction(1, N-len(T))**C
    return ((1-p)**j * p * Fraction(1, len(T))
            * Fraction(1, N-len(T))**j * Fraction(1, N)**(C-j-1))

rows = list(itertools.product(range(N), repeat=C))
for row in rows:
    assert row_disintegration_weight(row) == Fraction(1, N**C)
assert sum(map(row_disintegration_weight, rows)) == 1

# The advice contains MORE than the payload: entire type7 function for two
# possible public-surface child roots, endpoints, compressed PK, and root.
# No hidden predecessor X or unused private master K is read by this advice.
groups = defaultdict(lambda: {"x": Counter(), "k": Counter(), "worlds": 0})
worlds = 0
for table in itertools.product(rows, repeat=2):
    for child, endpoint, leaf_pk, root in itertools.product(range(2), range(N), range(N), range(N)):
        ctr = first(table[child])
        complete = ctr is not None
        public_payload = (leaf_pk, root, ctr) if complete else None
        outside = (table, child, endpoint, leaf_pk, root)
        # A retained query/work-state descriptor may be any function of this
        # outside advice and payload. This finite descriptor is deliberately
        # dependent on both the counter and pre-disclosure outside table.
        memory = (sum(sum(r) for r in table)+child+endpoint+(ctr or 0)) % 7
        view = (outside, public_payload, complete, memory)
        for x, k in itertools.product(range(N), repeat=2):
            g = groups[view]
            g["x"][x] += 1
            g["k"][k] += 1
            g["worlds"] += 1
            worlds += 1
for view, group in groups.items():
    assert set(group["x"].values()) == {group["worlds"]//N}
    assert set(group["k"].values()) == {group["worlds"]//N}
    # Any normalized query-input distribution depending on the view has
    # averaged matching-coordinate mass 1/N, even with unequal amplitudes.
    weights = [1, 2, 3, 4]
    support = sum(Fraction(weights[v], sum(weights))*Fraction(group["x"][v], group["worlds"])
                  for v in range(N))
    assert support == Fraction(1, N)

# Negative control 1: counter metadata genuinely correlates with its child
# given the outside type7 table. Treating counters as child-independent is
# false. Such correlation is permitted because child is safe public surface.
distinguishing_table = ((0, 0), (1, 0))
assert first(distinguishing_table[0]) is None
assert first(distinguishing_table[1]) == 0
assert first((0, 1)) == 1 and (0 not in T)

# Negative control 2: adding the private master as a fixture field destroys
# the unused-key support invariant. A view-driven query can then nominate K
# with certainty rather than 1/N. Adding X likewise destroys hidden uniformity.
unsafe_seed_groups = defaultdict(Counter)
unsafe_hidden_groups = defaultdict(Counter)
for k, x in itertools.product(range(N), repeat=2):
    unsafe_seed_groups[("fixture_seed", k)][k] += 1
    unsafe_hidden_groups[("working_predecessor", x)][x] += 1
assert all(max(c.values()) == sum(c.values()) for c in unsafe_seed_groups.values())
assert all(max(c.values()) == sum(c.values()) for c in unsafe_hidden_groups.values())

result = {
    "status": "PASS_SCOPED_EXACT_FINITE_OBSERVER_CONTROLS",
    "model": {"node_alphabet": N, "counters_per_row": C, "accepted": sorted(T)},
    "iid_row_assignments": len(rows),
    "row_weight": str(Fraction(1, N**C)),
    "joint_worlds": worlds,
    "outside_payload_memory_groups": len(groups),
    "remaining_hidden_coordinate_guess_probability": str(Fraction(1, N)),
    "unused_master_guess_probability": str(Fraction(1, N)),
    "unequal_query_weight_support_mass": str(Fraction(1, N)),
    "negative_child_counter_independence_refuted": True,
    "negative_seed_fixture_support_mass": "1",
    "negative_hidden_working_value_guess_probability": "1",
    "scope": "Exact finite sampler/factorization identities only; no full source or quantum theorem mechanization.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE / "CONTROL-RESULTS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))

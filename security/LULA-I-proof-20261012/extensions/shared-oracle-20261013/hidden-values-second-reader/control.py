"""Independent bounded exact controls; no real signing or oracle timing."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = ROOT / "publications/LULA-I/release/code/lula1/src/lib.rs"
PIN = "ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210"
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN

# First arrangement: directly enumerate the ordinary function before keygen.
# Full toy images have two bits, while hidden inputs/prefixes have one bit.
original_leaf = Counter()
for x, f0, f1 in product(range(2), range(4), range(4)):
    f = (f0, f1)
    original_leaf[(x, f, f[x])] += 1

# Second arrangement: sample hidden input + designated full image first.
ghost_leaf = Counter()
for x, y, other_image in product(range(2), range(4), range(4)):
    f = [None, None]
    f[x] = y
    f[1 - x] = other_image
    ghost_leaf[(x, tuple(f), y)] += 1
assert original_leaf == ghost_leaf
assert sum(original_leaf.values()) == sum(ghost_leaf.values()) == 32

# Two position-separated chain restrictions. The endpoint is public advice;
# the intermediate image prefix is the next hidden coordinate, not safe advice.
original_chain = Counter()
for x0, f00, f01, f10, f11 in product(range(2), range(4), range(4), range(4), range(4)):
    f0, f1 = (f00, f01), (f10, f11)
    x1 = f0[x0] >> 1
    x2 = f1[x1] >> 1
    original_chain[(x0, x1, x2, f0, f1)] += 1
ghost_chain = Counter()
for x0, x1, x2, r0, r1, other0, other1 in product(
        range(2), range(2), range(2), range(2), range(2), range(4), range(4)):
    f0, f1 = [None, None], [None, None]
    f0[x0], f0[1-x0] = 2*x1+r0, other0
    f1[x1], f1[1-x1] = 2*x2+r1, other1
    ghost_chain[(x0, x1, x2, tuple(f0), tuple(f1))] += 1
assert original_chain == ghost_chain
assert sum(original_chain.values()) == sum(ghost_chain.values()) == 512

# Counterexample to unchanged conditional uniformity in the REAL no-hit view.
surviving_x = [x for x in range(2) if x != 0]
survival_second_hit = Fraction(sum(x == 1 for x in surviving_x), len(surviving_x))
assert survival_second_hit == 1
assert survival_second_hit > Fraction(1, 2)

# Continued comparison execution: the hit flag never affects the reply.
# One hidden successor is queried, then revealed together with its suffix.
# Install only fresh designated points; retain every previously answered point.
history_groups = defaultdict(list)
union_hits = []
good_installs = conflicts = preserved_old_replies = 0
for x0, x1, x2, coin, hi, lo, tail1 in product(range(2), repeat=7):
    candidate1 = x2 ^ coin
    table = {(1, candidate1): (hi, lo)}
    old_table = dict(table)
    hit1 = candidate1 == x1  # Analytical flag: never controls execution.
    designated_image = (x2, tail1)
    if (1, x1) not in table:
        table[(1, x1)] = designated_image
    for point, reply in old_table.items():
        assert table[point] == reply
    preserved_old_replies += 1
    known_reply = table[(1, x1)]
    if not hit1:
        assert known_reply == designated_image
        good_installs += 1
    elif known_reply != designated_image:
        conflicts += 1
    candidate2 = known_reply[0] ^ x1 ^ coin
    hit2 = candidate2 == x0
    history = (x1, x2, coin, hi, lo, tail1, known_reply)
    history_groups[history].append(hit2)
    union_hits.append(hit1 or hit2)
assert all(Fraction(sum(hits), len(hits)) == Fraction(1,2)
           for hits in history_groups.values())
assert Fraction(sum(union_hits), len(union_hits)) == Fraction(3,4)
assert good_installs == 64 and conflicts == 48

# An invalid silent reprogramming variant visibly changes a former reply.
silent_mismatches = []
for x, designated_image, prior_reply in product(range(2), range(4), range(4)):
    silent_mismatches.append(x == 0 and designated_image != prior_reply)
silent_mismatch_probability = Fraction(sum(silent_mismatches),len(silent_mismatches))
assert silent_mismatch_probability == Fraction(3,8)

# Counterexample to exposure chosen by an unrevealed coordinate. Both choices
# leave position 0 concealed syntactically, and the two digits sum to 3.
hidden_selected_guess = []
for x0, x1, x2, x3 in product(range(2), repeat=4):
    boundary = 1 if x0 == 0 else 2
    other_digit = 3 - boundary
    assert boundary + other_digit == 3
    assert boundary > 0
    guess = 0 if boundary == 1 else 1
    hidden_selected_guess.append(guess == x0)
assert Fraction(sum(hidden_selected_guess),len(hidden_selected_guess)) == 1

# Counterexample to omitting suffix closure. A known predecessor lets an
# ordinary public chain evaluation recover the successor without guessing.
bad_suffix_hits = []
for x0, f0, f1 in product(range(2), range(2), range(2)):
    f = (f0, f1)
    successor = f[x0]
    recovered = f[x0]
    bad_suffix_hits.append(recovered == successor)
assert Fraction(sum(bad_suffix_hits),len(bad_suffix_hits)) == 1

candidate_cap = 17 + 4 * (32*15-240) + (16*255-2040)
assert candidate_cap == 3017

# Independently validate the optional exact all-key statement. Sliding-window
# polynomial convolution avoids float approximations and huge RO allocations.
def coefficient(w, length, total):
    row = [1] + [0] * total
    for _ in range(length):
        window = 0
        following = []
        for s in range(total + 1):
            window += row[s]
            if s >= w:
                window -= row[s-w]
            following.append(window)
        row = following
    return row[total]

lower_slice = coefficient(16,32,240)
top_slice = coefficient(256,16,2040)
assert lower_slice == 5181241160064611531897369560287267312
assert top_slice == 454918678781617793203528879683071744
assert min(lower_slice,top_slice)*1024 >= 1 << 128
lower_keys = sum(1 << e for e in (41,36,31,26))
top_keys = 1 << 21
assert lower_keys == 2269957324800 and top_keys == 2097152
assert lower_keys+top_keys < 1 << 42
assert pow(1024,1024) > 2*pow(1023,1024)
assert 2**22-42 == 4194262 and 2**22-21 == 4194283

out = {
    "status": "PASS_SCOPED_CLASSICAL_HIDDEN_VALUE_LEMMA_WITH_NEGATIVE_CONTROLS",
    "source_sha256": PIN,
    "leaf_joint_distributions_equal": True,
    "leaf_worlds_each_arrangement": 32,
    "chain_joint_distributions_equal": True,
    "chain_worlds_each_arrangement": 512,
    "real_second_guess_hit_given_first_no_hit": str(survival_second_hit),
    "incorrect_real_survival_uniform_prediction": "1/2",
    "continued_ideal_disclosure_worlds": 128,
    "remaining_hidden_guess_probability_every_unflagged_history": "1/2",
    "adaptive_two_query_union_probability": "3/4",
    "two_query_union_bound": "1",
    "good_fresh_installs": good_installs,
    "already_charged_conflicts_retaining_old_reply": conflicts,
    "old_reply_preserved_worlds": preserved_old_replies,
    "incorrect_silent_reprogram_visible_mismatch_probability": str(silent_mismatch_probability),
    "hidden_selected_boundary_guess_probability": "1",
    "hidden_selected_boundary_preserves_two_digit_sum": 3,
    "omitting_suffix_closure_successor_hit_probability": "1",
    "final_verifier_candidate_call_cap": candidate_cap,
    "optional_global_counter_check": {
        "lower_slice_count": str(lower_slice),
        "top_slice_count": str(top_slice),
        "lower_key_count": lower_keys,
        "top_key_count": top_keys,
        "both_densities_at_least_1_over_1024": True,
        "all_key_absence_union_bound": "2^(-4194262)",
        "top_setup_absence_union_bound": "2^(-4194283)",
        "required_for_partial_hidden_value_lemma": False
    },
    "scope": "Classical joint F/J ideal game, fixed nonzero seed, predictable atomic disclosure; no full security claim."
}
(HERE / "CHECKS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))

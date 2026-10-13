"""Tiny exact interface controls, no source signing/forgery or timing code."""
from itertools import product
from fractions import Fraction
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent

def accepted(word):
    return (word >> 1) == 1

def canonical(row):
    for c, word in enumerate(row):
        if accepted(word):
            return c, word
    return None

worlds = comparisons = bottoms = c0 = c1 = wrong_policy = 0
for child_bits in product(range(2), repeat=2):
    for words in product(range(4), repeat=8):
        worlds += 1
        for hidden_seed in range(2):
            # Fixed global table indexed by seed, base, counter; complete 2-bit words.
            def raw(seed, base, counter):
                return words[seed * 4 + base * 2 + counter]
            def collection_child():
                return child_bits[hidden_seed]
            source_child = child_bits[hidden_seed]
            registered_child = collection_child()
            assert registered_child == source_child
            source_row = tuple(raw(hidden_seed, source_child, c) for c in range(2))
            target = canonical(source_row)
            # Parameter release does not redraw the row or the low output limb.
            if target is not None:
                ctr, full = target
                assert raw(hidden_seed, registered_child, ctr) == full
                assert not any(accepted(source_row[c]) for c in range(ctr))
                if ctr == 0:
                    c0 += 1
                else:
                    c1 += 1
                other_valid = [c for c in range(2) if accepted(source_row[c])]
                wrong_policy += (max(other_valid) != ctr)
            else:
                bottoms += 1
            comparisons += 1

assert worlds == 262144
assert comparisons == 524288
assert Fraction(c0, comparisons) == Fraction(1, 2)
assert Fraction(c1, comparisons) == Fraction(1, 4)
assert Fraction(bottoms, comparisons) == Fraction(1, 4)
assert Fraction(wrong_policy, comparisons) == Fraction(1, 4)

# Independent accepted-fullword resampling loses source fullword identity.
matches = samples = 0
for row in product(range(4), repeat=2):
    target = canonical(row)
    if target is None:
        continue
    for resampled in (2, 3):
        samples += 1
        matches += resampled == target[1]
assert Fraction(matches, samples) == Fraction(1, 2)

# Counter-policy implication separation: both policies satisfy the same Prop,
# but their optimal different-base target collision probabilities are1 and0.
def policy_hash(base, counter):
    return 0 if counter == 0 else base + 1
policy_success = {}
for target_counter in (0, 1):
    wins = 0
    for base in (0, 1):
        y = policy_hash(base, target_counter)
        wins += any(policy_hash(1 - base, c) == y for c in (0, 1))
    policy_success[str(target_counter)] = str(Fraction(wins, 2))
assert policy_success == {"0": "1", "1": "0"}

# Same THF prefix interface, different full raw lower-limb law.
prefix_only_same = all((prefix << 1 | side) >> 1 == prefix
                       for prefix, side in product(range(2), repeat=2))
assert prefix_only_same
raw_side_one_uniform = Fraction(sum(side == 1 for side in range(2)), 2)
raw_side_one_zero = Fraction(0)
assert raw_side_one_uniform == Fraction(1, 2)
assert raw_side_one_zero == 0

receipt = {
    "scope": "Exact tiny interface controls only; no actual source/security/timing result",
    "complete_global_worlds": worlds,
    "hidden_seed_collection_source_comparisons": comparisons,
    "exact_first_counter_0_mass": str(Fraction(c0, comparisons)),
    "exact_first_counter_1_mass": str(Fraction(c1, comparisons)),
    "exact_bottom_mass": str(Fraction(bottoms, comparisons)),
    "choose_last_policy_metadata_disagreement": str(Fraction(wrong_policy, comparisons)),
    "independent_accepted_target_fullword_identity": str(Fraction(matches, samples)),
    "valid_policy_optimal_collision_success": policy_success,
    "prefix_identical_raw_side_one_uniform": str(raw_side_one_uniform),
    "prefix_identical_raw_side_one_zero": str(raw_side_one_zero),
    "low_rows": sum(2**h for h in (41,36,31,26)),
    "top_rows": 2**21,
    "low_pad_bits":42,
    "top_selector_bits":21,
    "bottom_collection_calls":17*(512+511)+1,
    "upper_collection_calls":32*(32*15+1)+31,
    "bottom_private_labels":17*512,
    "upper_private_labels":32*32,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(OUT / "CONTROL-RESULTS.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))

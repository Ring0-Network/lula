"""Exact finite controls, not a source attack or kernel proof."""
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
conditions = defaultdict(Counter)
worlds = successful = 0
first = Counter()
for outside in range(2):
    C = outside  # side-derived child, never reads the selected row
    for table in itertools.product(range(8), repeat=4):
        worlds += 1
        same = (table[2*C], table[2*C+1])
        other = (table[2*(1-C)], table[2*(1-C)+1])
        conditions[(outside, C, same)][other] += 1
        accepted = [c for c, full in enumerate(same) if (full >> 1) != 0]
        if accepted:
            successful += 1
            first[accepted[0]] += 1
for side, distribution in conditions.items():
    assert len(distribution) == 64
    assert set(distribution.values()) == {1}
assert successful == worlds * Fraction(15, 16)

for y in range(4):
    full_distribution = Counter()
    for f in range(2):
        prob_f = Fraction(1, 4) if f else Fraction(3, 4)
        for G in set(range(4)) - {y}:
            for lower in range(2):
                output = ((y if f else G) << 1) | lower
                full_distribution[output] += prob_f * Fraction(1, 3) * Fraction(1, 2)
    assert set(full_distribution.values()) == {Fraction(1, 8)}

# Literal source framing check, including both nonzero parameters and all toy R.
alias_cases = 0
for Pbyte in (1, 255):
    P = bytes([Pbyte]) * 16
    A = bytearray(22)
    A[9] = 7
    selected = P + bytes(48) + bytes(A) + bytes(16) + bytes(4)
    assert len(selected) == 106
    # Any inner alias must contain P at16:32, but selected contains zero there.
    assert selected[16:32] != P
    assert len(bytes(32) + bytes(4) + P) == 52 != len(selected)
    for typ in range(5):
        other_A = bytearray(A)
        other_A[9] = typ
        addressed = P + bytes(48) + bytes(other_A) + bytes(20)
        assert addressed != selected
        alias_cases += 1

result = {
    "kind": "finite_controls_only",
    "exit_expectation": 0,
    "worlds": worlds,
    "successful_targets": successful,
    "first_counter_counts": dict(first),
    "complete_side_condition_groups": len(conditions),
    "off_base_words_per_group": 64,
    "off_base_fullword_uniform": True,
    "boolean_completion_fullword_probability": "1/8",
    "literal_type_alias_cases_checked": alias_cases,
    "Boolean_queries_per_fullRaw_query": 2,
    "conservative_E3_numerator": "8*(2*Q+3)^2",
    "pre_evaluation_stopping_E3_numerator": "8*(2*Q+1)^2",
    "not_source_execution_or_quantum_kernel_proof": True,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT / "CONTROL-RESULTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))

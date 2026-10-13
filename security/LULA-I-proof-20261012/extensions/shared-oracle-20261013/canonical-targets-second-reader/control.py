"""Exhaustive finite RO control; no implementation signing or benchmarking."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import json
from pathlib import Path

M, LOW, C = 4, 2, 3
A = {0, 1}
images = list(product(range(M), range(LOW)))
masses = Counter()
views = defaultdict(Counter)
target_law = defaultdict(Counter)
free_selection = [0, 0]
for rows in product(images, repeat=C + 2):
    c = next((j for j in range(C) if rows[j][0] in A), None)
    masses[c] += 1
    if c is None:
        assert all(rows[j][0] not in A for j in range(C))
        continue
    assert all(rows[j][0] not in A for j in range(c))
    y = rows[c][0]
    target_law[c][rows[c]] += 1
    view = (c, rows[c], rows[:c])
    fresh = rows[c + 1] if c + 1 < C else rows[C]
    views[view][fresh] += 1
    free_selection[1] += 1
    free_selection[0] += any(rows[j][0] == y for j in (C, C+1))

total = sum(masses.values())
expected = {0: Fraction(1,2), 1: Fraction(1,4), 2: Fraction(1,8), None: Fraction(1,8)}
assert all(Fraction(masses[c],total)==p for c,p in expected.items())
for c, law in target_law.items():
    assert set(law)==set(product(A, range(LOW)))
    assert len(set(law.values()))==1
for view, law in views.items():
    assert set(law)==set(images)
    assert len(set(law.values()))==1
    assert Fraction(sum(n for (p,_),n in law.items() if p==view[1][0]),sum(law.values()))==Fraction(1,M)
free = Fraction(*free_selection)
assert free==Fraction(7,16)>Fraction(1,M)
out = {
    "worlds": total,
    "conditional_views": len(views),
    "counter_masses": {str(c):str(Fraction(n,total)) for c,n in masses.items()},
    "fresh_residual_match_every_view": "1/4",
    "full_target_image_law_given_counter": "uniform over four accepted full images",
    "free_two_residual_answers_then_one_selected_query": str(free),
    "status": "PASS_FINITE_CONTROL_ONLY"
}
# Independently recompute the source top acceptance coefficient and conservative
# rational exponent; no decimal approximation is needed for this receipt.
top_count = sum((-1)**j * comb(16,j) * comb(2055-256*j,15)
                for j in range(8))
assert top_count == 454918678781617793203528879683071744
top_p = Fraction(top_count, 2**128)
coarse_exponent = (2**32 * top_count)//2**128 - 21
assert coarse_exponent == 5741859
out["top_accepted_count"] = str(top_count)
out["top_probability"] = str(top_p)
out["rigorous_top_noncompletion_upper_bound"] = "2^-5741859"
Path(__file__).with_name("CONTROL-RESULTS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))

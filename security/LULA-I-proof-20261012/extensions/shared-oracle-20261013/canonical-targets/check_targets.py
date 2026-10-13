"""Exact tiny row checks and actual top acceptance arithmetic; no signing runs."""
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json

M, T, C = 4, frozenset((1, 2)), 3
p = Fraction(len(T), M)
tables = list(product(range(M), repeat=C+1))
groups = defaultdict(list)
for table in tables:
    c = next((i for i in range(C) if table[i] in T), None)
    key = (c, table[c]) if c is not None else (None, None)
    groups[key].append(table)
    if c is None:
        weight = (1-p)**C / (M-len(T))**C / M
    else:
        weight = ((1-p)**c*p / len(T)
                  / (M-len(T))**c / M**(C-c-1) / M)
    assert weight == Fraction(1, M**(C+1))

checks = 0
for (c, y), group in groups.items():
    if c is None:
        assert len(group) == (M-len(T))**C*M
        continue
    for point in range(C+1):
        hit = Fraction(sum(table[point] == y for table in group), len(group))
        want = Fraction(1) if point == c else Fraction(0) if point < c else Fraction(1,M)
        assert hit == want
        checks += 1

# Two independently conditioned successful rows: disclose both canonical targets,
# adaptively choose a row using its target value, query that row's other-child point.
success_tables = [table for table in tables if any(v in T for v in table[:C])]
hits = total = 0
for a in success_tables:
    ca = next(i for i in range(C) if a[i] in T)
    for b in success_tables:
        cb = next(i for i in range(C) if b[i] in T)
        chosen = a if a[ca] >= b[cb] else b
        cc = ca if chosen is a else cb
        hits += chosen[C] == chosen[cc]
        total += 1
assert Fraction(hits,total) == Fraction(1,M)

# Invalid rule: accepted target is selected after inspecting residual point X.
# Y=X if accepted, otherwise Y=1. Residual X is not independent conditional on Y.
negative_hits = sum(x == (x if x in T else 1) for x in range(M))
negative_probability = Fraction(negative_hits,M)
conditional_two = [x for x in range(M) if (x if x in T else 1) == 2]
assert negative_probability == Fraction(1,2) > Fraction(1,M)
assert Fraction(sum(x == 2 for x in conditional_two),len(conditional_two)) == 1

# Full actual acceptance count, independently by inclusion-exclusion and DP.
n, radix, s = 16, 256, 2040
ie = sum((-1)**j*comb(n,j)*comb(s-radix*j+n-1,n-1)
         for j in range(s//radix+1))
dp = [1]
for _ in range(n):
    nxt = []
    window = 0
    for j in range(len(dp)+radix-1):
        if j < len(dp):
            window += dp[j]
        if j >= radix and j-radix < len(dp):
            window -= dp[j-radix]
        nxt.append(window)
    dp = nxt
assert ie == dp[s]
assert sum(dp) == radix**n
assert dp[s] == max(dp)
p_top = Fraction(ie,radix**n)
counter_space, rows = 2**32, 2**21
# (1-p)^C <= 2^(-Cp), so this integer is a rigorous conservative exponent.
simple_exp = (counter_space*ie)//(radix**n)
with localcontext() as ctx:
    ctx.prec = 65
    pd = Decimal(ie)/Decimal(radix**n)
    row_log2 = Decimal(counter_space)*(1-pd).ln()/Decimal(2).ln()
    union_log2 = Decimal(21)+row_log2
    approx = {"p_top":str(pd), "row_failure_log2":str(row_log2),
              "union_failure_log2":str(union_log2)}

result = {
    "status":"PASS_SMALL_EXACT_CONTROLS_AND_ARITHMETIC",
    "tiny_marginal_tables":len(tables), "tiny_conditional_point_checks":checks,
    "all_targets_exposed_adaptive_row_hit":str(Fraction(hits,total)),
    "wrong_residual_selected_target_hit":str(negative_probability),
    "wrong_rule_conditional_y_two_hit":"1",
    "top_count_inclusion_exclusion":str(ie), "top_count_dp":str(dp[s]),
    "top_probability":{"numerator":str(p_top.numerator),"denominator":str(p_top.denominator)},
    "top_rows":rows, "distinct_counters":counter_space,
    "tau_exact":"[1-(1-p_top)^(2^32)]^(2^21)",
    "rigorous_simple_completion_failure_bound":f"1-tau_top <= 2^-{simple_exp-21}",
    "approximate_logs_only":approx,
    "scope":"Classical ideal type7 row lemma controls; not a Rust/full-security proof",
}
Path(__file__).with_name("CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

"""Exact rational discriminator for expected-count versus pathwise padding.

Abstract FORS coverage-stream counterexample, not an executable signature attack.
Uses actual B,t,k and two latent exposures. No third-party dependencies.
"""
from fractions import Fraction
import json
import math
from pathlib import Path

B, t, k, Q = 2**41, 512, 17, 2**30
pi = Fraction(1, B)
mu = Fraction(2*t-1, t)**k / (B*t**(k+1))
nu = Fraction(4*t-3, t)**k / (B**2*t**(2*k+2))
p_fixed = (1-pi)*Fraction(2, B*t**(k+1)) + pi*mu
expected_count = Q*pi
lower = pi*(Q*mu - Fraction(Q*(Q-1), 2)*nu)
wrong = (expected_count+1)*p_fixed
pathwise_upper = (Q+1)*p_fixed
assert lower > 31*wrong
assert lower <= pathwise_upper

def exact(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}

result = {
    "scope": "Abstract raw-candidate coverage, not a real source forgery",
    "parameters": {"B": B, "t": t, "k": k, "q": 2, "Q_H": Q},
    "strategy": "Request Q candidates only when two exposure instance addresses coincide",
    "expected_candidate_count": exact(expected_count),
    "bonferroni_success_lower": exact(lower),
    "invalid_expected_plus_one_upper": exact(wrong),
    "valid_deterministic_plus_one_upper": exact(pathwise_upper),
    "lower_over_invalid_approx": float(lower/wrong),
    "log2_lower_approx": math.log2(lower.numerator)-math.log2(lower.denominator),
    "checks": {"lower_exceeds_31_times_invalid": True, "lower_below_deterministic_bound": True},
}
Path(__file__).with_name("EXPECTED_CAP_COUNTEREXAMPLE.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))

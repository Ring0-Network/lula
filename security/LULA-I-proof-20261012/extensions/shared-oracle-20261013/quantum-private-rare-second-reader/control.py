"""Small exact controls for classical-block stopping vs coherent postselection.

No source security or quantum forgery is certified by these finite controls.
"""
from fractions import Fraction as F
import json
from pathlib import Path

# The often-used coherent PSD claim is false, with an exact quadratic witness.
# rho=|+><+|; P projects to coordinate0; v=(1,-1).
rho = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
prhop = [[F(1, 2), F(0)], [F(0), F(0)]]
v = (F(1), F(-1))
def quad(matrix, vector):
    return sum(vector[i] * matrix[i][j] * vector[j]
               for i in range(2) for j in range(2))
assert quad(rho, v) == 0
assert quad(prhop, v) == F(1, 2)

# Two hidden key values, independent of the continued ideal operative history.
# Within either measured history the query remains coherent. No history dephases
# its query state, and no active mask is applied to the coherent query register.
histories = [(F(1, 3), (F(3, 5), F(4, 5))),
             (F(2, 3), (F(4, 5), F(-3, 5)))]
for prob, psi in histories:
    assert sum(a * a for a in psi) == 1
continued_mass = sum(F(1, 2) * prob * psi[key] ** 2
                     for key in range(2) for prob, psi in histories)
assert continued_mass == F(1, 2)
max_normalized = F(0)
for mask in range(16):
    active_mass = F(0)
    active_weight = F(0)
    for key in range(2):
        for h, (prob, psi) in enumerate(histories):
            keep = (mask >> (2 * key + h)) & 1
            if keep:
                active_mass += F(1, 2) * prob * psi[key] ** 2
                active_weight += F(1, 2) * prob
    assert active_mass <= continued_mass
    if active_weight:
        max_normalized = max(max_normalized, active_mass / active_weight)

# A still simpler selected block shows conditional mass1 despite continued1/N.
selected_weight = F(1, 2)  # keep only key0, fixed query|0>
selected_support = F(1, 2)
assert selected_support <= F(1, 2)
assert selected_support / selected_weight == 1

# An actual one-query marked-XOR/phase toy with16 hidden keys, a common
# diffusion, measured nominee and BEFORE-service alias stop. This is a finite
# abstract control, not source signing or a cryptographic forgery.
n = 16
ideal_amp = [F(1, 4)] * n
real_b = ideal_b = real_w = ideal_w = gap_sq = F(0)
active_q2_support = continued_q2_support = active_q2_weight = F(0)
for key in range(n):
    real_amp = [F(3, 16)] * n
    real_amp[key] = F(11, 16)
    assert sum(a*a for a in real_amp) == 1
    gap_sq += sum((r-i)**2 for r, i in zip(real_amp, ideal_amp))/n
    for guess in range(n):
        pr = real_amp[guess]**2/n
        pi = ideal_amp[guess]**2/n
        if guess == key:
            real_b += pr
            ideal_b += pi
        elif guess == (key-1) % n:
            real_w += pr
            ideal_w += pi
        # Continued key-blind IDEAL may make a second query at guess+1.
        # Stopped ACTIVE deletes guess=key histories. After normalization
        # private mass rises to1/15, but unnormalized support remains1/16.
        q2 = (guess+1) % n
        continued_q2_support += pi * (q2 == key)
        if guess != key:
            active_q2_weight += pi
            active_q2_support += pi * (q2 == key)
assert gap_sq == F(1, 4)  # d=2/sqrt16=1/2, including environment references
assert ideal_b == ideal_w == F(1, 16)
assert real_b == F(121, 256) and real_w == F(9, 256)
assert active_q2_support == continued_q2_support == F(1, 16)
assert active_q2_weight == F(15, 16)
assert active_q2_support/active_q2_weight == F(1, 15)
# Separate B/W bound=(1/2+1/4)^2=9/16 each. Shared bound is
# (1/2+sqrt(1/8))^2=3/8+sqrt(2)/4; verify exact radical comparison.
assert real_b <= F(9, 16) and real_w <= F(9, 16)
joint_real = real_b+real_w
assert joint_real == F(65, 128)
assert joint_real-F(3, 8) >= 0
assert (joint_real-F(3, 8))**2 <= F(1, 8)
# Shared bound <1, whereas capped sum of separate bounds is1.
assert (F(1)-F(3, 8))**2 > F(1, 8)

result = {
    "status": "PASS_EXACT_RATIONAL_CONTROLS",
    "coherent_psd_claim_refuted": True,
    "negative_witness_rho": str(quad(rho, v)),
    "negative_witness_projected": str(quad(prhop, v)),
    "classical_environment_history_masks": 16,
    "continued_private_support": str(continued_mass),
    "all_unnormalized_active_supports_dominated": True,
    "normalized_active_support_can_be_one": True,
    "marked_xor_phase_toy_hidden_keys": n,
    "toy_purified_gap_squared": str(gap_sq),
    "toy_real_first_alias_probability": str(real_b),
    "toy_real_no_alias_other_terminal_probability": str(real_w),
    "toy_joint_terminal_probability": str(joint_real),
    "toy_joint_bound": "3/8+sqrt(2)/4",
    "toy_second_slot_unnormalized_support": str(active_q2_support),
    "toy_second_slot_normalized_support": str(active_q2_support/active_q2_weight),
    "proof_scope": "Finite block/norm controls; not a source security proof",
}
Path(__file__).with_name("CHECKS.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))

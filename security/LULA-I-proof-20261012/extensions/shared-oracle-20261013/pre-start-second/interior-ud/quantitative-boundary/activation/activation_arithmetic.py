"""Exact source-geometry/hypothetical arithmetic, never a LULA execution."""
from fractions import Fraction
from math import isqrt
from decimal import Decimal, localcontext
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
M = 1 << 55
N = 1 << 128
K = sum(1 << e for e in (41, 36, 31, 26))
KTOP = 1 << 21
P_SUM = 3360 * K + 518160 * KTOP
SIGMA = Fraction(N - 1, N)
Q_EXPS = [24, 30, 38, 40, 41, 44, 50, 64]
SETUP = (1 << 21) * (19505 + (1 << 32)) - 1
HOT = 82090 + 5 * (1 << 32)
COLD = 8560574463 + 82090 + 6 * (1 << 32)
OVERHEAD = 3224 + 254
CU = Fraction(12 * M * 254, 1 << 64)
CA = Fraction(12 * P_SUM, 1 << 64)

def dec(x):
    with localcontext() as ctx:
        ctx.prec = 35
        return str(Decimal(x.numerator) / Decimal(x.denominator))

def ceil(x):
    return -((-x.numerator) // x.denominator)

def info(x):
    return {"fraction": str(x), "decimal_display": dec(x)}

activation = []
for r in range(254):
    active = 32 * K * max(14-r, 0) + 16 * KTOP * (254-r)
    a = Fraction(active, M)
    activation.append({"r": r, "active_labels": str(active),
                       "selector_activation": info(a),
                       "source_execution_activation_with_zero_skip": info(a*SIGMA)})
assert sum(int(a["active_labels"]) for a in activation) == P_SUM == 7628143271608320
assert Fraction(activation[-1]["selector_activation"]["fraction"]) == Fraction(1, 1 << 30)
assert CU == Fraction(381, 64)
assert CA == Fraction(682009155, 137438953472)

thresholds = {}
for name, coefficient in [("uniform254", CU), ("activation_weighted", CA)]:
    vals = {}
    for c in [Fraction(1,2), Fraction(1)]:
        t = c / coefficient
        qa_target_only = t - 1
        vals[str(c)] = {
            "effective_Q_crossing": info(t),
            "first_integer_effective_Q_at_or_above_crossing": str(ceil(t)),
            "target_only_Q_A_crossing_if_Q_target_equals_Q_A_plus_one": info(qa_target_only),
            "first_nonnegative_integer_target_only_Q_A_at_or_above_crossing": str(max(0,ceil(qa_target_only))),
            "nonnegative_global_Q_A_crossing_exists_with_reviewed_setup_cap": False,
        }
    thresholds[name] = vals

# Exact dyadic radical enclosures; no Decimal is used for certificates.
BITS = 192
DYADIC = 1 << BITS
def sqrt_interval(v):
    z = isqrt(v * DYADIC * DYADIC)
    lo, hi = Fraction(z, DYADIC), Fraction(z+1, DYADIC)
    assert lo*lo <= v < hi*hi
    return lo, hi

S2L,S2U = sqrt_interval(2)
SLL,SLU = sqrt_interval(3017)
direct_thresholds = {}
for c in [Fraction(1,2), Fraction(1)]:
    if c == Fraction(1,2):
        lo = (1 << 62)*S2L - SLU/2
        hi = (1 << 62)*S2U - SLL/2
        exact = "2^62 sqrt(2) - sqrt(3017)/2"
    else:
        lo = (1 << 63) - SLU/2
        hi = (1 << 63) - SLL/2
        exact = "2^63 - sqrt(3017)/2"
    assert lo.numerator//lo.denominator == hi.numerator//hi.denominator
    assert ceil(lo) == ceil(hi)
    direct_thresholds[str(c)] = {
        "exact_algebraic_crossing": exact,
        "certified_dyadic_lower": info(lo),
        "certified_dyadic_upper": info(hi),
        "nearest_integer_below": str(lo.numerator//lo.denominator),
        "nearest_integer_above": str(ceil(hi)),
        "bounds_width_fraction": str(hi-lo),
    }

rows = []
for qa_exp in [32,64]:
    qa = 1 << qa_exp
    direct_lo = min(Fraction(1), Fraction((2*qa+SLL)**2,N))
    direct_hi = min(Fraction(1), Fraction((2*qa+SLU)**2,N))
    for q_exp in Q_EXPS:
        q = 1 << q_exp
        for mode, sign_cap in [("hot",HOT),("absent_cache",COLD)]:
            qb = qa+SETUP+q*sign_cap+OVERHEAD
            eps = min(Fraction(1),Fraction(12*qb,1 << 64))
            rows.append({
                "Q_A_exponent":qa_exp,"q_exponent":q_exp,"mode":mode,
                "Q_A":str(qa),"q":str(q),"Q_B_global_complete_h_cap":str(qb),
                "conditional_fixed_label_generic_epsilon_cap":info(eps),
                "hypothetical_uniform_UD_cap_PRE_zero":str(min(Fraction(1),M*254*eps)),
                "hypothetical_activation_UD_cap_PRE_zero":str(min(Fraction(1),P_SUM*eps)),
                "direct_reviewed_HJ_RO_event_bound_lower":info(direct_lo),
                "direct_reviewed_HJ_RO_event_bound_upper":info(direct_hi),
                "hypothetical_target_only_activation_cap_PRE_zero":str(min(Fraction(1),CA*(qa+1))),
            })
assert len(rows)==32
assert all(r["hypothetical_activation_UD_cap_PRE_zero"]=="1" for r in rows)

out = {
    "classification":"COMPUTED_ACTIVATION_AND_CONDITIONAL_QUERY_ENVELOPES_NOT_SECURITY_BITS",
    "source_driver_sha256":"a18799fba64ec1a6370e18e0d5d4b21108109cf9022fc8d7195e55d860a08c4b",
    "source_library_sha256":"ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210",
    "lower_wots_key_sum":str(K),"top_wots_keys":str(KTOP),
    "selector_size":str(M),"summed_active_position_multiplicity":str(P_SUM),
    "sum_selector_activation":info(Fraction(P_SUM,M)),
    "activation_probabilities":activation,
    "uniform_conditional_linear_coefficient":info(CU),
    "activation_conditional_linear_coefficient":info(CA),
    "rational_envelope_crossings":thresholds,
    "direct_model_radical_crossings_with_exact_rational_enclosures":direct_thresholds,
    "sqrt_enclosure_bits":BITS,
    "rows":rows,
    "fixed_h_hardness_certified":False,
    "random_full_oracle_target_only_lift_proved":False,
    "terminal_PRE_advantage_evaluated":False,
    "old_core_or_certificate_changes":False,
    "new_source_game_declarations":0,"whole_goal_complete":False,
}
(BASE/"ACTIVATION-ARITHMETIC.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
md = ["# Activation-aware hypothetical table and native direct-event comparison","",
      "**COMPUTED — model-separated arithmetic.** Primitive columns assume the random-function generic formula applies at each fixed-label budget; that lift and actual fixed-h hardness are unproved. PRE=0 is only an optimistic diagnostic. Direct columns evaluate the reviewed native HJ random-oracle final-event bound, not fixed-h hardness. No cell is a security-bit or category claim.","",
      "| Q_A | q | global cap hot | global cap absent cache | target-only activation cap, if lifted | direct native HJ/RO H_final bound |",
      "|---|---|---:|---:|---:|---:|"]
for qa_exp in [32,64]:
    for q_exp in Q_EXPS:
        hot=next(r for r in rows if r["Q_A_exponent"]==qa_exp and r["q_exponent"]==q_exp and r["mode"]=="hot")
        cold=next(r for r in rows if r["Q_A_exponent"]==qa_exp and r["q_exponent"]==q_exp and r["mode"]=="absent_cache")
        with localcontext() as ctx:
            ctx.prec=12
            d = str(+Decimal(hot["direct_reviewed_HJ_RO_event_bound_upper"]["decimal_display"]))
        md.append(f"| 2^{qa_exp} | 2^{q_exp} | {hot['hypothetical_activation_UD_cap_PRE_zero']} | {cold['hypothetical_activation_UD_cap_PRE_zero']} | {hot['hypothetical_target_only_activation_cap_PRE_zero']} | {d} |")
md += ["","Exact global Q_B values and certified direct radical bounds are retained in ACTIVATION-ARITHMETIC.json.","",
       "| hypothetical effective-query envelope | c=1/2 exact crossing | first integer Q | c=1 exact crossing | first integer Q |",
       "|---|---|---:|---|---:|",
       "| uniform254 | 32/381 | 1 | 64/381 | 1 |",
       "| activation-weighted | 68719476736/682009155 | 101 | 137438953472/682009155 | 202 |","",
       "For Q_target=Q_A+1, activation first crosses c=1/2 at integer Q_A=100 and c=1 at integer Q_A=201. Global honest setup already passes both thresholds. These are crossings of hypothetical sufficient envelopes, not measured or optimal attack costs.","",
       "| native direct HJ/RO envelope | exact algebraic crossing | certified integer immediately below | certified integer immediately above |",
       "|---|---|---:|---:|",
       f"| c=1/2 | 2^62 sqrt(2)-sqrt(3017)/2 | {direct_thresholds['1/2']['nearest_integer_below']} | {direct_thresholds['1/2']['nearest_integer_above']} |",
       f"| c=1 | 2^63-sqrt(3017)/2 | {direct_thresholds['1']['nearest_integer_below']} | {direct_thresholds['1']['nearest_integer_above']} |","",
       "Direct crossings contain radicals; the JSON gives exact rational dyadic enclosures and validates their nearest integers with integer arithmetic. The native direct lemma counts Q_A coherent adversarial slots; its common honest-service and terminal-examiner argument explains why source-global primitive-simulator work is not added to that variable. This does not excuse omitting honest work from a primitive adversary's own budget.","",
       "Signed cancellation, image-event structure or a better aggregate proof may improve either generic diagnostic. Saturated upper envelopes are neither attacks nor impossibility results.",""]
(BASE/"COMPARISON-TABLE.md").write_text("\n".join(md),encoding="utf-8")
print(json.dumps({"classification":out["classification"],"activation_rows":len(activation),"budget_rows":len(rows),
                  "position_sum":str(P_SUM),"sum_activation":str(Fraction(P_SUM,M)),
                  "direct_nearest_integers":{c:(v["nearest_integer_below"],v["nearest_integer_above"]) for c,v in direct_thresholds.items()},
                  "exit_code":0}))

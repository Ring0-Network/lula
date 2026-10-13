"""Exact hypothetical arithmetic; not a fixed-h security bound or source run."""
from fractions import Fraction
from decimal import Decimal, localcontext
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
EXPONENTS = [24, 30, 38, 40, 41, 44, 50, 64]
SETUP = (1 << 21) * (19505 + (1 << 32)) - 1
HOT = 82090 + 5 * (1 << 32)
COLD = 8560574463 + 82090 + 6 * (1 << 32)
FINAL = 3224
EXTRA = 254
SELECTOR = 1 << 55
HOPS = 254
DENOM = 1 << 64

def decimal(fr):
    with localcontext() as ctx:
        ctx.prec = 30
        return str(Decimal(fr.numerator) / Decimal(fr.denominator))

rows = []
for qa_exp in [32, 64]:
    qa = 1 << qa_exp
    for q_exp in EXPONENTS:
        q = 1 << q_exp
        for mode, sign_cap in [("hot", HOT), ("absent_cache", COLD)]:
            qb = qa + SETUP + q * sign_cap + FINAL + EXTRA
            raw = Fraction(12 * qb, DENOM)
            delta_cap = min(Fraction(1), raw)
            ud_term = SELECTOR * HOPS * delta_cap
            rows.append({
                "classification": "HYPOTHETICAL_ARITHMETIC_NOT_FIXED_H_SECURITY",
                "Q_A_exponent": qa_exp,
                "q_exponent": q_exp,
                "mode": mode,
                "Q_A": str(qa),
                "q": str(q),
                "complete_h_Q_B_cap": str(qb),
                "assumed_per_hop_unclipped_fraction": str(raw),
                "assumed_per_hop_unclipped_decimal": decimal(raw),
                "assumed_per_hop_cap_fraction": str(delta_cap),
                "assumed_per_hop_cap_decimal": decimal(delta_cap),
                "amplified_UD_arithmetic_fraction": str(ud_term),
                "amplified_UD_arithmetic_decimal": decimal(ud_term),
                "capped_envelope_if_PRE_zero": str(min(Fraction(1), ud_term)),
            })

thresholds = {}
for qa_exp in [32, 64]:
    qa = 1 << qa_exp
    for mode, sign_cap in [("hot", HOT), ("absent_cache", COLD)]:
        # Largest integer q for which 12 Q_B <= 2^64.
        qmax = ((DENOM // 12) - qa - SETUP - FINAL - EXTRA) // sign_cap
        thresholds[f"Q_A_2^{qa_exp}_{mode}"] = {
            "largest_q_with_unclipped_per_hop_at_most_one": str(qmax) if qmax >= 0 else None,
            "nonnegative_q_exists": qmax >= 0,
        }

WKEYS = (1 << 41) + (1 << 36) + (1 << 31) + (1 << 26)
P_WEIGHT = 3360 * WKEYS + 518160 * (1 << 21)
out = {
    "classification": "COMPUTED_HYPOTHETICAL_ENVELOPE_NOT_SECURITY_BITS",
    "applies_to_actual_fixed_h": False,
    "same_global_raw_oracle_lifting_proved_here": False,
    "assumed_inequality_for_arithmetic_only": "delta_r <= min(1,12 Q_B / 2^64)",
    "terminal_PRE_advantage_evaluated": False,
    "terminal_PRE_zero_is_an_optimistic_diagnostic_only": True,
    "source_budgets": {
        "H_setup": str(SETUP), "H_hot": str(HOT), "H_absent_cache": str(COLD),
        "H_final": FINAL, "H_selected_extra": EXTRA,
    },
    "selector_bits": 55,
    "UD_hops": HOPS,
    "eight_q_exponents": EXPONENTS,
    "aggregate_unclipped_linear_coefficient": str(Fraction(SELECTOR * HOPS * 12, DENOM)),
    "aggregate_nontrivial_Q_B_threshold": str(Fraction(DENOM, SELECTOR * HOPS * 12)),
    "active_position_weight_for_optional_refinement": str(P_WEIGHT),
    "active_weight_linear_coefficient": str(Fraction(12 * P_WEIGHT, DENOM)),
    "active_weight_nontrivial_Q_threshold": str(Fraction(DENOM, 12 * P_WEIGHT)),
    "per_hop_thresholds": thresholds,
    "rows": rows,
    "new_source_game_declarations": 0,
    "whole_goal_complete": False,
}
assert SETUP == 9007240159690751
assert HOT == 21474918570
assert COLD == 34330460329
assert len(rows) == 32
assert all(r["capped_envelope_if_PRE_zero"] == "1" for r in rows)
assert Fraction(SELECTOR * HOPS * 12, DENOM) == Fraction(381, 64)
(BASE / "CONDITIONAL-ENVELOPE.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

md = [
    "# Hypothetical capped UD envelope", "",
    "**COMPUTED — arithmetic only.** Assume, solely for this diagnostic, each constructed UD adversary satisfies delta<=min(1,12 Q_B/2^64). Applicability to fixed h or its full same-h interface is unproved. PRE is optimistically set to zero only to test whether the UD term already saturates. Values are probabilities/envelopes, never security bits.", "",
    "Q_B=Q_A+H_setup+q H_mode+3224+254. Every table row's 2^55*254 amplified UD envelope caps at 1, already with PRE=0.", "",
]
for qa_exp in [32, 64]:
    md += [f"## Q_A=2^{qa_exp}", "",
        "| q | Q_B hot | per-hop hypothetical cap hot | Q_B absent cache | per-hop hypothetical cap absent cache | aggregate cap, PRE=0 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for q_exp in EXPONENTS:
        hot = next(r for r in rows if r["Q_A_exponent"] == qa_exp and r["q_exponent"] == q_exp and r["mode"] == "hot")
        cold = next(r for r in rows if r["Q_A_exponent"] == qa_exp and r["q_exponent"] == q_exp and r["mode"] == "absent_cache")
        with localcontext() as ctx:
            ctx.prec = 8
            dh = str(+Decimal(hot["assumed_per_hop_cap_decimal"]))
            dc = str(+Decimal(cold["assumed_per_hop_cap_decimal"]))
        md.append(f"| 2^{q_exp} | {hot['complete_h_Q_B_cap']} | {dh} | {cold['complete_h_Q_B_cap']} | {dc} | 1 |")
    md.append("")
md += [
    "**PROVED — analytic saturation of this hypothetical expression.** Before the per-hop cap, the aggregate coefficient is exactly 381/64 times Q_B. Its outer cap therefore reaches 1 for any integer Q_B>=1; the nontrivial threshold is Q_B<64/381. This says the proposed sufficient envelope is uninformative. It is neither an attack nor a conclusion about actual fixed-h hardness.", "",
    "Exact fractions, unclipped values and threshold computations are retained in CONDITIONAL-ENVELOPE.json.", "",
]
(BASE / "CONDITIONAL-TABLE.md").write_text("\n".join(md), encoding="utf-8")
print(json.dumps({"classification": out["classification"], "rows": len(rows), "all_aggregate_caps": "1", "coefficient": "381/64", "per_hop_thresholds": thresholds, "active_position_weight": str(P_WEIGHT)}))

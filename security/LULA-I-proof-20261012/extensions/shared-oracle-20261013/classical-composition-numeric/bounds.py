"""Independent interval evaluation of the reviewed conservative classical RO sum.

Run: python -I -B bounds.py
Requires the already installed mpmath 1.3.0; no source/paper/old-packet writes.
These are advantage-bound exponents, not work factors or category certificates.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math
import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PIN = "ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210"
assert hashlib.sha256((ROOT / "publications/LULA-I/release/code/lula1/src/lib.rs").read_bytes()).hexdigest() == PIN
mp.mp.dps = 280
mp.iv.dps = 230
IV = mp.iv.mpf
N = 1 << 128
B = 1 << 41
t = 512
C = 1 << 32
EXPONENTS = (24,30,38,40,41,44,50,64)
QUERY_EXPONENTS = (64,128)

def endpoints(v):
    return mp.mpf(v._mpi_[0]), mp.mpf(v._mpi_[1])

def serial(v):
    lo, hi = endpoints(v)
    assert lo >= 0 and hi >= lo
    return {
        "lower_decimal": mp.nstr(lo,90),
        "upper_decimal": mp.nstr(hi,90),
        "lower_dyadic_mpf_tuple": list(v._mpi_[0]),
        "upper_dyadic_mpf_tuple": list(v._mpi_[1]),
        "midpoint_decimal": mp.nstr((lo+hi)/2,70),
        "negative_log2_upper": float(-mp.log(hi,2)) if hi else None,
        "negative_log2_lower": float(-mp.log(lo,2)) if lo else None,
        "meaning": "outward interval evaluation of a positive advantage upper-bound expression"
    }

def cap(v):
    lo, hi = endpoints(v)
    if lo >= 1:
        return IV(1)
    if hi >= 1:
        return IV([lo,1])
    return v

def fors_interval(q):
    rho = IV(1)/B
    r = IV(511)/512
    total = IV(0)
    for j in range(18):
        total += ((-1)**j * math.comb(17,j)) * ((1-rho+rho*r**j)**q)
    out = total/512
    lo, hi = endpoints(out)
    # Outward cancellation arithmetic may straddle the exact saturation cap.
    # The positive expectation proves 0 < p_F <= 1/512, so intersect it.
    assert lo > 0 and lo <= mp.mpf(1)/512
    return IV([lo,min(hi,mp.mpf(1)/512)])

def positive_check(q, moment):
    """Independently arranged nonnegative recurrence + analytic tail control."""
    rho = IV(1)/B
    mu = IV(q)/B
    r = IV(511)/512
    mu_mid = mp.mpf(q)/B
    if mu_mid > 4096:
        deficit = mp.iv.exp(-mu/8)
        lower = (1-deficit)*(1-mp.iv.exp((mu/2)*mp.iv.log(r)))**17/512
        lower_lo = endpoints(lower)[0]
        moment_lo,moment_hi = endpoints(moment)
        assert moment_lo >= lower_lo and moment_hi <= mp.mpf(1)/512
        return {"method":"Chernoff saturation interval", "lower":mp.nstr(lower_lo,90),"upper":"0.001953125"}
    stop = min(q,max(320,math.ceil(mu_mid+20*mp.sqrt(mu_mid+1)+300)))
    weight = (1-rho)**q
    total = IV(0)
    for count in range(1,stop+1):
        weight *= IV(q-count+1)*rho/(count*(1-rho))
        total += weight*(1-r**count)**17
    lower = total/512
    L = stop+1
    tail = IV(0) if stop == q else mp.iv.exp(-mu+L*(1+mp.iv.log(mu/L)))/512
    lower_lo,lower_hi = endpoints(lower)
    upper_lo,upper_hi = endpoints(lower+tail)
    moment_lo,moment_hi = endpoints(moment)
    assert moment_hi >= lower_lo and moment_lo <= upper_hi
    return {
        "method":"positive binomial recurrence with Chernoff omitted-tail bound",
        "stop":stop,
        "lower":mp.nstr(lower_lo,90),"upper":mp.nstr(upper_hi,90),
        "omitted_weighted_tail_upper":mp.nstr(endpoints(tail)[1],90),
        "relative_interval_width":mp.nstr((upper_hi-lower_lo)/lower_lo,30)
    }

exhaust_unit = (IV(511)/512)**C
rows=[]
for qlog in EXPONENTS:
    q = 1 << qlog
    pF = fors_interval(q)
    crosscheck = positive_check(q,pF)
    for Qlog in QUERY_EXPONENTS:
        Q = 1 << Qlog
        # Exact rational recombination independently validates all constants.
        component_coefficients = [Q+2*q+2, 2*Q+q+1, Q+3017, Q+3217, Q+5, 1]
        scalar_coefficient = sum(component_coefficients)
        assert scalar_coefficient == 6*Q+3*q+6243
        pair_coefficient = q*Q + q*(q-1)//2 + q
        exact_scalar = sum(Fraction(c,N) for c in component_coefficients)
        assert exact_scalar == Fraction(6*Q+3*q+6243,N)
        terms = {
            "joint_private_fixed_nonzero_seed":IV(component_coefficients[0])/N,
            "fors_bridge_128_fixed_nonzero_seed":IV(component_coefficients[1])/N,
            "hidden_value":IV(component_coefficients[2])/N,
            "public_graph":IV(component_coefficients[3])/N,
            "canonical_type7":IV(component_coefficients[4])/N,
            "seed_zero_once":IV(1)/N,
            "fors_bridge_256":IV(pair_coefficient)/(N*N),
            "fors_exhaustion":q*exhaust_unit,
            "covered_candidate_union":(Q+1)*pF
        }
        direct_total = IV(scalar_coefficient)/N + IV(pair_coefficient)/(N*N) + q*exhaust_unit + (Q+1)*pF
        term_total = sum(terms.values(),IV(0))
        dl,du = endpoints(direct_total)
        tl,tu = endpoints(term_total)
        assert max(dl,tl) <= min(du,tu)
        rows.append({
            "log2_signing_query_cap":qlog,"signing_query_cap":str(q),
            "log2_adversarial_public_query_cap":Qlog,"adversarial_public_query_cap":str(Q),
            "scalar_128_numerator":str(scalar_coefficient),
            "scalar_128_denominator":str(N),
            "pair_256_numerator":str(pair_coefficient),
            "pair_256_denominator":str(N*N),
            "FORS_per_raw_candidate":serial(pF),
            "positive_crosscheck":crosscheck,
            "terms":{name:serial(value) for name,value in terms.items()},
            "uncapped_total":serial(direct_total),
            "capped_total":serial(cap(direct_total)),
            "outcome":"COMPUTED_INTERVAL_EVALUATION_OF_ACCEPTED_MANUAL_CLASSICAL_RO_BOUND",
            "classical_level_or_QROM_category_certification":"NOT_ESTABLISHED_BY_THIS_BOUND"
        })

out={
    "source_sha256":PIN,
    "reviewed_root_candidate_sha256":"21ee235fec883dc8e55c8b4f8759df3d76e722292cf5a2065cae2ab2ef1536dd",
    "mpmath_version":mp.__version__,"interval_decimal_precision":mp.iv.dps,
    "formula":"min(1,(6Q_H+3q+6243)/2^128 + (qQ_H+q(q-1)/2+q)/2^256 + q(511/512)^(2^32) + (Q_H+1)p_F(q))",
    "event_scope":"Unconditioned partial classical full-output random-oracle source game; initiated signing calls; one final verifier; one seed-zero charge.",
    "meaning_of_reported_bits":"Negative base-2 logarithm of a capped advantage upper bound, NOT a work factor or a per-candidate component exponent.",
    "scope_limits":["No fixed-SHA guarantee","No standard-model primitive reduction","No checked Rust refinement","No QROM signer theorem","No arbitrary cache-corruption/timing interface","No successful-setup normalization"],
    "optional_five_QH_sharpening_used":False,
    "rows":rows
}
(HERE/"OWN-BOUNDS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
table=["# Independent conservative classical RO evaluation", "", out["formula"], "", out["meaning_of_reported_bits"], "", "| q | Q_H | FORS per-candidate exponent | Total capped-bound exponent |", "|---:|---:|---:|---:|"]
for row in rows:
    table.append(f"| 2^{row['log2_signing_query_cap']} | 2^{row['log2_adversarial_public_query_cap']} | {row['FORS_per_raw_candidate']['negative_log2_upper']:.12f} | {row['capped_total']['negative_log2_upper']:.12f} |")
table += ["", "Every interval uses 230-digit outward arithmetic. A second positive occupancy calculation with tail control overlaps the finite-moment interval. Exact rational arithmetic recombines the additive constants. The full dyadic endpoints and each term are in OWN-BOUNDS.json. No root output was read to generate these values.", "", "Status: COMPUTED_ACCEPTED_MANUAL_CLASSICAL_RO_BOUND; WORK_FACTOR_AND_QROM_CATEGORY_NOT_ESTABLISHED."]
(HERE/"OWN-BOUNDS.md").write_text("\n".join(table)+"\n",encoding="utf-8")
print("\n".join(table))

"""Compare root rows only after the independent OWN-BOUNDS result exists."""
from pathlib import Path
import hashlib
import json
import mpmath as mp

HERE = Path(__file__).resolve().parent
X = HERE.parent
mp.mp.dps = 280
own_path = HERE/"OWN-BOUNDS.json"
own = json.loads(own_path.read_text(encoding="utf-8"))
assert own["optional_five_QH_sharpening_used"] is False
own_rows = {(r["log2_signing_query_cap"],r["log2_adversarial_public_query_cap"]):r for r in own["rows"]}

def mid(record):
    lo = mp.mpf(tuple(record["lower_dyadic_mpf_tuple"]))
    hi = mp.mpf(tuple(record["upper_dyadic_mpf_tuple"]))
    return (lo+hi)/2

def clipped(v):
    return min(mp.mpf(1),v)

def check_decimal(value, expected, relative_tolerance=mp.mpf("1e-43")):
    measured = mp.mpf(value)
    relative_error = abs(measured-expected)/expected if expected else abs(measured)
    assert relative_error < relative_tolerance, (value,mp.nstr(expected,70),mp.nstr(relative_error,40))
    return mp.nstr(relative_error,40)

checked=[]
identities={"own_bounds_sha256":hashlib.sha256(own_path.read_bytes()).hexdigest()}
root_script_hash = hashlib.sha256((X/"bounds.py").read_bytes()).hexdigest()
for query_log in (64,128):
    path = X/f"root-checks/bounds-QH{query_log}/bounds.json"
    document = json.loads(path.read_text(encoding="utf-8"))
    identities[str(path.relative_to(X))] = hashlib.sha256(path.read_bytes()).hexdigest()
    assert document["script_sha256"] == root_script_hash
    assert len(document["rows"]) == 8
    for row in document["rows"]:
        key = row["log2_q"],query_log
        expected = own_rows[key]
        q = int(expected["signing_query_cap"])
        Q = int(expected["adversarial_public_query_cap"])
        assert row["q"] == str(q) and row["QH"] == str(Q)
        assert row["classical_RO_linear_numerator"] == str(6*Q+3*q+6243)
        terms = {name:mid(rec) for name,rec in expected["terms"].items()}
        expected_fields={
            "FORS_binomial_per_raw_candidate":mid(expected["FORS_per_raw_candidate"]),
            "joint_nonzero_probability":clipped(terms["joint_private_fixed_nonzero_seed"]),
            "coverage_beta_nonzero_probability":clipped(terms["fors_bridge_128_fixed_nonzero_seed"]+terms["fors_bridge_256"]+terms["fors_exhaustion"]),
            "conditional_FORS_union_probability":clipped(terms["covered_candidate_union"]),
            "hidden_input_event_bound_nonzero":clipped(terms["hidden_value"]),
            "graph_target_event_bound_nonzero":clipped(terms["public_graph"]),
            "canonical_type7_event_bound_nonzero":clipped(terms["canonical_type7"]),
            "seed_zero_probability":terms["seed_zero_once"],
            "classical_RO_pair_term":terms["fors_bridge_256"],
            "total_probability":mid(expected["capped_total"])
        }
        errors={name:check_decimal(row[name],value) for name,value in expected_fields.items()}
        errors["FORS_exhaustion_term"] = check_decimal(row["FORS_exhaustion_term"],terms["fors_exhaustion"],mp.mpf("1e-28"))
        expected_bits = expected["capped_total"]["negative_log2_upper"]
        assert abs(row["total_bits"]-expected_bits) < 1e-11
        if query_log == 128 or row["log2_q"] in (50,64):
            assert row["total_probability"] == "1.0" and row["total_bits"] == 0.0
        assert row["classical_level1_status"] == "NOT_ESTABLISHED_NO_CERTIFIED_CAPACITY"
        assert row["quantum_total"] is None and row["quantum_status"] == "OPEN_NO_QROM_REDUCTION"
        assert row["WOTS_generic_primitive_reduction"] is None and row["tree_generic_primitive_embedding"] is None
        checked.append({
            "log2_q":row["log2_q"],"log2_Q_H":query_log,
            "total_bound_exponent":row["total_bits"],
            "exact_linear_coefficient_matches":True,
            "term_relative_errors":errors,
            "capped_one_verified":row["total_probability"] == "1.0",
            "level1_and_QROM_not_promoted":True
        })

identities["root_script_sha256"] = root_script_hash
receipt={
    "outcome":"PASS_ALL_16_ROOT_ROWS_AND_CLASSICAL_TERM_LEDGER",
    "comparison_order":"Independent OWN-BOUNDS.json was saved first; root result files were then read.",
    "root_rows_compared":len(checked),"scope":"Conservative6Q_H bound only; no optional sharpening.",
    "identities":identities,"rows":checked
}
(HERE/"ROOT-CROSSCHECK.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
lines=["# Root numerical cross-check", "", "Outcome: PASS_ALL_16_ROOT_ROWS_AND_CLASSICAL_TERM_LEDGER.", "", "`python -I -B crosscheck_root.py` returned exit 0. Independent interval results were saved before inspecting root output. All eight q values match at each of Q_H=2^64 and 2^128; each root per-term decimal matches the independent result within its serialization precision. Exact integer coefficients 6Q_H+3q+6243 match in all rows.", "", "At Q_H=2^64 the total caps at one for q=2^50 and 2^64. At Q_H=2^128 it caps at one for every tested q. The negative-log totals are upper-bound exponents, not work factors; root leaves classical level 1 uncertified and full QROM/efficient primitive reductions unresolved.", "", "Root identities and all relative-error checks appear in ROOT-CROSSCHECK.json. No root file was changed."]
(HERE/"ROOT-CROSSCHECK.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print(json.dumps({"outcome":receipt["outcome"],"rows":len(checked),"identities":identities},indent=2))

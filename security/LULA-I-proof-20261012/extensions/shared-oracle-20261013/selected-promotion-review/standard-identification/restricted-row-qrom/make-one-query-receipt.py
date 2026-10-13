import hashlib
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
X = HERE.parents[2]
ROOT = X / "root-keyed-review"
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(ROOT / "ONE-QUERY-COMPLETION.md") == "7def78f7f5e771e397373f7ad81c7977674669d2064a3b2ce1a31e13d31bf1f0"
assert sha(ROOT / "one_query_completion.py") == "89128e32d5a3eeb7da92c4fe22fbcbc5de725e5c235f0625480832f9981cd9c1"
assert (HERE / "one-query-rerun/ONE-QUERY-CONTROL.json").read_bytes() == (ROOT / "ONE-QUERY-CONTROL.json").read_bytes()
result = {
    "status": "ACCEPTED_MANUAL_ONE_QUERY_COMPLETION_AND_RESTRICTED_RO_CONSEQUENCE",
    "root_claimed_blindness": False,
    "root_subject_pins": {str((ROOT / n).relative_to(X)): sha(ROOT / n) for n in ("ONE-QUERY-COMPLETION.md", "one_query_completion.py", "ONE-QUERY-CONTROL.json")},
    "own_pins": {n: sha(HERE / n) for n in ("INDEPENDENT-FIRST.md", "PEER-REVIEW.md", "REVIEW-RECEIPT.json", "ONE-QUERY-REVIEW.md", "rerun-one-query.py", "one-query-rerun/ONE-QUERY-CONTROL.json")},
    "prior_peer_first_pin": sha(X / "keyed-target-reader/restricted-row-qrom/INDEPENDENT-FIRST.md"),
    "checks": {n: True for n in ("one_standard_unconditional_Boolean_XOR_query", "Fourier_response_exact_translation", "scratch_zero_no_extra_input_phase", "arbitrary_entangled_reference_linearity", "outside_Delta_zero_plus_identity", "independent_completion_tables", "canonical_bottom_same_function_preserved", "preserved_program_M_Qplus1", "new_stopped_extractor_M_Q_no_Win_recognition", "independent_rerun_exit0", "rerun_byte_identical", "negative_controls_discriminate_missing_phase_and_uncompute", "honest_runtime_still_charged")},
    "derived_bound": "min(1,8*(M+1)^2/2^128)",
    "preserved_program_bound": "min(1,8*(Q+2)^2/2^128)",
    "new_stopped_program_bound": "min(1,8*(Q+1)^2/2^128)",
    "new_checked_declarations": 0,
    "full_source_game_checked_declarations": 0,
    "category_capacity_fixed_SHA_claim": False,
    "efficient_coherent_implementation_claim": False,
    "whole_goal_complete": False,
}
(HERE / "ONE-QUERY-REVIEW.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(sha(HERE / "ONE-QUERY-REVIEW.json"))

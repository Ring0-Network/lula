import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parents[2]
PEER = X / "keyed-target-reader" / "restricted-row-qrom"
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(HERE / "INDEPENDENT-FIRST.md") == "74d25d6b3a7332d866ac8c11d3a0b75b37390837b02e7abc05d72332f84a31c1"
assert sha(PEER / "INDEPENDENT-FIRST.md") == "44dcb6acf797cf27875eece1a9f52f6e8faf2c365a8a391d4d5a14812b1c419b"
assert (HERE / "peer-rerun/CONTROL-RESULTS.json").read_bytes() == (PEER / "CONTROL-RESULTS.json").read_bytes()
receipt = {
    "status": "ACCEPTED_MANUAL_RESTRICTED_INITIAL_GLOBAL_RO_COMPONENT",
    "own_first_saved_before_new_peer_read": True,
    "files": {name: sha(HERE / name) for name in ("INDEPENDENT-FIRST.md", "OWN-RECEIPT.json", "PEER-REVIEW.md", "rerun-peer-controls.py", "peer-rerun/CONTROL-RESULTS.json")},
    "peer_subject_pins": {str((PEER / name).relative_to(X)): sha(PEER / name) for name in ("INDEPENDENT-FIRST.md", "controls.py", "CONTROL-RESULTS.json", "RECEIPT.json")},
    "checks": {
        "immutable_first_hashes": True,
        "fullword_boolean_product_law": True,
        "two_queries_per_Raw": True,
        "canonical_bottom_unnormalized": True,
        "static_controlled_joint_commutation": True,
        "nonzero_honest_alias_exclusions": True,
        "preserved_program_M_Qplus1": True,
        "new_stopped_extractor_M_Q": True,
        "stopped_output_requires_no_full_Win_recognition": True,
        "no_query_history_measurement": True,
        "independent_controls_rerun_exit0": True,
        "rerun_output_byte_identical": True,
        "root_one_query_proposal_not_read": True,
    },
    "new_checked_declarations": 0,
    "full_source_game_checked_declarations": 0,
    "category_or_fixed_SHA_claim": False,
    "efficient_coherent_implementation_claim": False,
    "whole_goal_complete": False,
}
(HERE / "REVIEW-RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(sha(HERE / "REVIEW-RECEIPT.json"))

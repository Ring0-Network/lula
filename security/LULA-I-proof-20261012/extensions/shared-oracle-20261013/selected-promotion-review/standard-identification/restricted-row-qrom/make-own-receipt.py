import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parents[2]
SRC = Path(r"C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs")
PDF = Path(r"C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\R2\R2B-joint-constraints\refs\sphincsplusc_2022_778\2022-778.pdf")
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

assert sha(HERE / "INDEPENDENT-FIRST.md") == "74d25d6b3a7332d866ac8c11d3a0b75b37390837b02e7abc05d72332f84a31c1"
assert sha(SRC) == "ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210"
assert sha(PDF) == "1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215"
receipt = {
    "status": "INDEPENDENT_FIRST_SAVED_AWAITING_PEER_REVIEW",
    "new_peer_proposals_read_before_first": False,
    "files": {name: sha(HERE / name) for name in ("INDEPENDENT-FIRST.md", "controls.py", "CONTROL-RESULTS.json")},
    "source": {str(SRC): sha(SRC)},
    "primary": {str(PDF): sha(PDF), str(PDF.with_suffix('.txt')): sha(PDF.with_suffix('.txt'))},
    "primary_anchor": "SPHINCS+C AppendixE TheoremE.3 printed35/PDFindex37",
    "manual_bound": "min(1,8*(2*M+1)^2/2^128)",
    "conservative_marked_calls": "M<=Q+1",
    "new_pre_evaluation_extractor_marked_calls": "M<=Q",
    "checks": {
        "canonical_fullword_row_retained": True,
        "condition_only_initial_side_data_not_A_transcript": True,
        "no_pretarget_Raw": True,
        "commutation_pointwise_static_readonly_O": True,
        "all_honest_hash_runtime_charged": True,
        "no_query_history_measurement": True,
        "no_nohit_postselection": True,
        "controls_exit_zero": True,
    },
    "zero_new_kernel_declarations": True,
    "fixed_SHA_hardness_claim": False,
    "all_HK_collection_conjecture_proved": False,
    "efficient_outside_implementation_proved": False,
    "whole_goal_complete": False,
}
(HERE / "OWN-RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(sha(HERE / "OWN-RECEIPT.json"))

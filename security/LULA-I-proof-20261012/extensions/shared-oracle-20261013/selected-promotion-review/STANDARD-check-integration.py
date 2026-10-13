import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name): return json.loads((X / name).read_text(encoding="utf-8"))
P = read("STANDARD-CANONICAL-PROMOTION.json")
OLD = read("outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json")
SUBJECT = read("outside-field-check/standard-component-review/SUBJECT-REVIEW.json")
SOURCE = Path(r"C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs")
assert sha(SOURCE) == SUBJECT["source_sha256"]
assert sha(X / "outside-field-check/standard-component-review/SUBJECT-REVIEW.json") == P["subject_review_sha256"]
assert OLD["documents"] == P["predecessor_documents"]
groups = {
    "documents": P["documents"],
    "promoted_artifacts": {**P["artifact"], "STANDARD-CANONICAL-PROMOTION.json": sha(X / "STANDARD-CANONICAL-PROMOTION.json")},
    "source_subjects": P["subject_pins"],
    "backup_pins": {f'{P["predecessor_backup"]}/{n}': h for n,h in P["predecessor_documents"].items()},
    "preserved_artifacts": P["preserved_core_artifacts"],
    "control_pins": P["kernel_pins"],
    "prior_review_receipts": {
        "outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json": sha(X / "outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json"),
        "outside-field-check/standard-component-review/SUBJECT-REVIEW.json": P["subject_review_sha256"],
        "selected-promotion-review/standard-identification/PROVENANCE.json": SUBJECT["author_provenance_sha256"],
    },
}
for group,pins in groups.items():
    for name,expected in pins.items():
        assert sha(X / name) == expected, (group,name)
for name,h in OLD.get("earlier_backup_pins",{}).items():
    assert sha(X / name) == h,name
for p in SUBJECT["primary_files"]:
    assert sha(Path(p["pdf"])) == p["pdf_sha256"]
    assert sha(Path(p["cached_text"])) == p["cached_text_sha256"]
assert P["new_supporting_checked_declarations"] == 4
assert P["cumulative_supporting_checked_declarations"] == 44
assert P["new_whole_source_game_checked_declarations"] == 0
kernel = read("root-keyed-review/COUNTER-POLICY-CHECK.json")
assert kernel["checked_declarations"] == 4 and kernel["exit_code"] == 0
assert kernel["custom_axioms"] == 0 and kernel["admissions"] == 0
assert kernel["source_security_checked_declarations"] == 0
assert SUBJECT["independent_kernel_reexecution"]["exit_code"] == 0
diff=[]
for name in P["documents"]:
    before = (X / P["predecessor_backup"] / name).read_text(encoding="utf-8")
    after = (X / name).read_text(encoding="utf-8")
    diff.extend(difflib.unified_diff(before.splitlines(),after.splitlines(),fromfile=f'before/{name}',tofile=f'current/{name}',lineterm=""))
(HERE / "STANDARD-MANUAL-DIFF.txt").write_text("\n".join(diff)+"\n",encoding="utf-8")
if (HERE / "STANDARD-INTEGRATION-REVIEW.md").exists():
    receipt = {
        "status": "ACCEPTED_SCOPED_STANDARD_CANONICAL_CURRENT_INDEX",
        **groups,
        "provenance_pins": {
            "selected-promotion-review/STANDARD-INTEGRATION-REVIEW.md": sha(HERE / "STANDARD-INTEGRATION-REVIEW.md"),
            "selected-promotion-review/STANDARD-MANUAL-DIFF.txt": sha(HERE / "STANDARD-MANUAL-DIFF.txt"),
            "selected-promotion-review/STANDARD-check-integration.py": sha(Path(__file__)),
        },
        "checks": {n: True for n in (
            "current_six_doc_pins", "previous_outside_doc_pins_match_immutable_before_standard",
            "previous_backup_chain_preserved", "primary_actual_pdf_text_pins", "manualdiff_read",
            "canonical_policy_legal_no_all_policies_equivalence", "r_is_construction_choice",
            "hidden_parameter_disjoint_types0_to4_child", "same_full_public_h_all_aliases",
            "fixed_predicate_lower42_top21", "unconditional_S_nonzero_no_double_seedzero",
            "bottom_unnormalized", "reduction_all_runtime_work_charged",
            "HK_collection_quantitative_conjecture_not_promoted", "synthetic_helpers_only",
            "prior_scalar_source_unchanged", "restricted_QROM_onequery_not_used_in_this_promotion")},
        "new_supporting_checked_declarations": 4,
        "cumulative_supporting_checked_declarations": 44,
        "new_whole_source_game_checked_declarations": 0,
        "source_path": str(SOURCE),
        "source_sha256": sha(SOURCE),
        "fixed_SHA_hardness_or_category_claim": False,
        "whole_goal_complete": False,
    }
    (HERE / "STANDARD-INTEGRATION-REVIEW.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print("ACCEPTED",sha(HERE / "STANDARD-INTEGRATION-REVIEW.json"))
else:
    print("PINS_CHECKED_MANUAL_REVIEW_PENDING",len(diff),"diff lines")

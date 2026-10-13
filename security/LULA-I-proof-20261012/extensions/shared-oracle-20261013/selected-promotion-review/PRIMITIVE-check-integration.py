import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name): return json.loads((X / name).read_text(encoding="utf-8"))
P = read("PRIMITIVE-SUCCESSORS-PROMOTION.json")
OLD = read("selected-promotion-review/STANDARD-INTEGRATION-REVIEW.json")
assert OLD["documents"] == P["predecessor_documents"]
assert len(P["accepted_evidence_absolute_pins"]) == 98
internal,external = {},{}
for name,h in P["accepted_evidence_absolute_pins"].items():
    path = Path(name)
    assert sha(path) == h,name
    if path.is_relative_to(X): internal[str(path.relative_to(X)).replace('\\','/')] = h
    else: external[name] = h
groups = {
    "documents": P["documents"],
    "promoted_artifacts": {**P["artifacts"],"PRIMITIVE-SUCCESSORS-PROMOTION.json":sha(X / "PRIMITIVE-SUCCESSORS-PROMOTION.json")},
    "source_subjects": internal,
    "prior_review_receipts": P["receipt_pins"],
    "backup_pins": {f'{P["predecessor_backup"]}/{n}':h for n,h in P["predecessor_documents"].items()},
    "preserved_artifacts": P["preserved_core_artifacts"],
}
for group,pins in groups.items():
    for name,h in pins.items(): assert sha(X / name)==h,(group,name)
for group in ("promoted_artifacts","source_subjects","backup_pins","preserved_artifacts","control_pins","prior_review_receipts","provenance_pins"):
    for name,h in OLD.get(group,{}).items(): assert sha(X / name)==h,(group,name)
assert P["source_scalar_manuscript_changes"] == 0
assert P["cumulative_supporting_checked_declarations"] == 44
assert P["new_source_game_checked_declarations"] == 0
assert P["whole_goal_complete"] is False
private = read("outside-field-check/public-h-private-review/FINAL-SUBJECT-REVIEW.json")
qrom = read("restricted-row-third-review/FINAL-SUBJECT-REVIEW.json")
assert private["final_artifact"] == {"PRIVATE-FIXED-H-REDUCTION.md":P["artifacts"]["PRIVATE-FIXED-H-REDUCTION.md"]}
assert qrom["pins"]["final_subject"]["sha256"] == P["artifacts"]["RESTRICTED-CANONICAL-QROM.md"]
assert qrom["new_extractor_M"] == "Q" and qrom["old_adapter_M"] == "Q+1"
assert private["whole_goal_complete"] is False
assert private["new_kernel_declarations"] == 0
diff=[]
for name in P["documents"]:
    before=(X/P["predecessor_backup"]/name).read_text(encoding="utf-8")
    after=(X/name).read_text(encoding="utf-8")
    diff.extend(difflib.unified_diff(before.splitlines(),after.splitlines(),fromfile=f'before/{name}',tofile=f'current/{name}',lineterm=""))
(HERE/"PRIMITIVE-MANUAL-DIFF.txt").write_text("\n".join(diff)+"\n",encoding="utf-8")
if (HERE/"PRIMITIVE-INTEGRATION-REVIEW.md").exists():
    receipt = {
        "status":"ACCEPTED_SCOPED_PRIVATE_FIXED_H_AND_RESTRICTED_QROM_CURRENT_INDEX",
        **groups,
        "accepted_evidence_absolute_pins":P["accepted_evidence_absolute_pins"],
        "external_absolute_pins":external,
        "accepted_evidence_items":98,
        "provenance_pins":{f'selected-promotion-review/{n}':sha(HERE/n) for n in ("PRIMITIVE-INTEGRATION-REVIEW.md","PRIMITIVE-MANUAL-DIFF.txt","PRIMITIVE-check-integration.py")},
        "checks":{n:True for n in (
            "current_six_documents_exact_pins","all98_accepted_items_exact_hashes",
            "standard_prior_documents_map_immutable_before_primitive_successors",
            "historical_standard_artifacts_backup_subject_receipt_pins_preserved",
            "manual_full_artifact_and_diff_read","private_f_g_frames_and_classical_private_quantum_public_interfaces",
            "private_signed_average_not_average_absolute","private_hops_no_new_seedzero_or_selector",
            "same_full_fixed_h_all_aliases_no_programmable_Raw",
            "absorbing_private_services_and_persistent_memo_caps",
            "fixed_h_public_lower_limb_Hmsg_graph_obligation_open",
            "restricted_global_O_model_distinct_from_fixed_h",
            "restricted_initial_side_condition_only_no_nohit",
            "one_query_full256_clean_isometry_entangled_reference",
            "old_final_eval_M_Qplus1_vs_NEW_predigest_M_Q",
            "tau_unnormalized_eta_once_unconditional_nonzero",
            "all_honest_runtime_work_charged","all_prior_scalar_source_theorems_unchanged",
            "supporting44_new_game_kernel0","no_category_capacity_or_goal_closure")},
        "cumulative_supporting_checked_declarations":44,
        "new_source_game_checked_declarations":0,
        "new_supporting_checked_declarations":0,
        "fixed_SHA_hardness_or_category_claim":False,
        "whole_goal_complete":False,
    }
    (HERE/"PRIMITIVE-INTEGRATION-REVIEW.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print("ACCEPTED",sha(HERE/"PRIMITIVE-INTEGRATION-REVIEW.json"))
else: print("PINS_CHECKED_MANUAL_REVIEW_PENDING",len(diff),"diff lines",len(internal),"internal",len(external),"external")

from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent;X=B.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subject=X/'CLASSICAL-JOINT-RO-THEOREM.md'
assert sha(subject)=='4fa7c3b63a268bd7535a753813d109a2f768f0089df44b54223a6e34cfaf35f0'
technical=B/'FINAL-TECHNICAL-CANDIDATE-REVIEW.json'
assert sha(technical)=='53f3facb555f3f41f22e0e95d323d208575e82ca64bda64da15980bc16fa44c2'
old=json.loads(technical.read_text(encoding='utf-8'))
for path,digest in old['preserved_artifacts'].items():
    p=Path(path) if Path(path).is_absolute() else X/path
    assert sha(p)==digest,path
for path,digest in {**old['source_subjects'],**old['provenance_pins']}.items():assert sha(X/path)==digest,path
numerics=json.loads((B/'JOINT-NUMERICS.json').read_text(encoding='utf-8'))
assert len(numerics['rows'])==16 and len(numerics['half_success_crossings'])==8
assert all(r['adjacent_certified'] for r in numerics['half_success_crossings'])
checks={k:True for k in ['exact_corrected_subject_rechecked','source_shared_full_raw_REAL_marginal_explicit',
 'same_safe_graph_row_private_coverage_world','full256_lower_limbs_retained',
 'no_complete_function_identity_claim','atomic_inflight_unsigned_J_scope_explicit',
 'knownpoint_install_firstbad_and_forward_exposure_verified','no_surplus_row_or_full_secret_advice',
 'deterministic_candidate_padding_only','fixed6241_uniform6242_once_seedzero',
 'honest_cache_only_transfer_zero_event_query_loss','eight_q_16_rows_and_8_adjacent_crossings_verified',
 'exact_rational_intervals_and_exhaustion_enclosed','historical_source_and_scalar_pins_unchanged',
 'manual_scope_not_source_kernel_or_category_certificate']}
pins={str((B/n).relative_to(X)).replace('\\','/'):sha(B/n) for n in [
 'FINAL-TECHNICAL-CANDIDATE-REVIEW.json','FINAL-SUBJECT-REVIEW.md',
 'joint_numerics.py','JOINT-NUMERICS.json','JOINT-NUMERICS.md','finalize_subject.py']}
out=dict(status='ACCEPTED_MANUAL_CLASSICAL_JOINT_RO_FINAL_SUBJECT',
 subject='CLASSICAL-JOINT-RO-THEOREM.md',subject_sha256=sha(subject),checks=checks,
 source_subjects=old['source_subjects'],provenance_pins={**old['provenance_pins'],**pins},
 preserved_artifacts=old['preserved_artifacts'],numerical_input_pins=numerics['input_pins'],
 initial_draft_sha256='c0b0a26e7a4024cbc86668b6470b1f6214f915cce9a47f30ea2b21448069c343',
 changes_requested='REAL marginal and atomic unsigned-J scope explicit; observable-prefix agreement replaces complete-function identity. Constants unchanged.',
 prior_supporting_declarations=47,new_checked_declarations=0,new_source_game_declarations=0,
 core_index_promotion_reviewed=False,security_level_or_category_established=False,whole_goal_complete=False)
(B/'FINAL-SUBJECT-REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],receipt_sha256=sha(B/'FINAL-SUBJECT-REVIEW.json'),checks=len(checks),whole_goal_complete=False)))

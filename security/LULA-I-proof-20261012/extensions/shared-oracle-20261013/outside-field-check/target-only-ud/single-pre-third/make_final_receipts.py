"""Exact subject/caller receipts; own-folder writes, all older packets immutable."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
ROOT=PARENT.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pins(base,names):return {n:sha(base/n) for n in names}
single=ROOT/'SINGLE-TARGET-PRE-RO.md'
combined=ROOT/'TARGET-ONLY-HIDDEN-BOUND.md'
assert sha(HERE/'INDEPENDENT-FIRST.md')=='995fea1ac5af0f0d7620e6db2f42699fa1acf70932728701fea8ad657266b0c7'
assert sha(single)=='16b5b6f7dd49ba1a1b263e60de59c4c3e4ce078294482578139f3aa719bbf85a'
assert sha(combined)=='b6b2e65a6c6cb1af262809216163916d79a1e6dfe19c085957b98a3f01d6547a'
assert sha(ROOT/'TARGET-ONLY-UD-RO.md')=='4e0aeeb0b0ed72eae3dd45e506fee8bf57db176e7ed3b6ddcd5cf2393b52e9df'
controls=json.loads((HERE/'CONTROL-RESULTS.json').read_text())
assert sha(HERE/'controls.py')==controls['script_sha256']
for n in ('quantitative.py','QUANTITATIVE-RESULTS.json'):
    assert sha(HERE/'root-quantitative-recheck'/n)==sha(ROOT/'root-target-only-ud'/n)
prior=json.loads((PARENT/'FINAL-SUBJECT-REVIEW.json').read_text())
assert sha(Path(prior['source']['path']))==prior['source']['sha256']
N=1<<128
DH=20229886488608768
AH=7628143271608320
mu=Fraction(2*N-1,N*N)
slope=Fraction(12*AH,1<<64)
def envelope(qa):
    r=qa+1
    return DH*min(Fraction(1),(2*r+1)**2*mu)+slope*r
assert envelope(99)<=Fraction(1,2)<envelope(100)
assert envelope(200)<=1<envelope(201)
single_receipt={
 'verdict':'ACCEPT_MANUAL_SINGLE_TARGET_PRE_QUERY_BOUND_AND_ACTUAL_CALLER',
 'subject_path':str(single),'subject_sha256':sha(single),
 'actual_caller_subject_sha256':sha(combined),
 'own_first_saved_before_new_single_PRE_peer_root_proofs_read':True,
 'own_pins':pins(HERE,['INDEPENDENT-FIRST.md','controls.py','CONTROL-RESULTS.json','FINAL-SUBJECT-REVIEW.md']),
 'peer_first_pins':{
  'selected-promotion-review/quantitative-goal-audit/single-pre/INDEPENDENT-FIRST.md':sha(ROOT/'selected-promotion-review'/'quantitative-goal-audit'/'single-pre'/'INDEPENDENT-FIRST.md'),
  'pre-start-second/interior-ud/quantitative-boundary/activation/single-pre/INDEPENDENT-FIRST.md':sha(ROOT/'pre-start-second'/'interior-ud'/'quantitative-boundary'/'activation'/'single-pre'/'INDEPENDENT-FIRST.md')},
 'source':prior['source'],
 'supporting_subject_pins':pins(ROOT,['FIXED-H-HIDDEN-PREDECESSORS.md','TARGET-ONLY-UD-RO.md','OUTSIDE-SIMULATOR-THEOREM.md']),
 'query_bound':'kappa_PRE(Q,n)<=min(1,(2Q+1)^2*(2/2^n-1/2^(2n)))',
 'checks':{
  'correlated_planted_field_exact_full_function_challenge_joint_law':True,
  'conditional_perpoint_mu_only_no_iid_assumption':True,
  'common_purification_includes_mark_field_equivalent_L2_average':True,
  'zero_prefixes_auxiliary_data_independent_marker':True,
  'one_Boolean_query_per_complete_H_query_clean_phase_scratch':True,
  'complete_lower_limb_offrow_invalid_extension_preserved':True,
  'terminal_any_preimage_not_original_X_only':True,
  'no_extra_challenger_output_test_query':True,
  'exact_Nminus1_miss_alphabet_not_modulo_biased':True,
  'miss_entropy_not_claimed_actual_bounded_faircoin_sampling_time':True,
  'explicit_expected_rejection_cost_charged_in_own_first':True,
  'no_efficient_nonbinary_simulator_claim':True,
  'actual_B1_selector_target_then_PY_zero_public_prequeries':True,
  'whole_source_A_prekey_rerun_after_primitive_challenge':True,
  'no_free_O_dependent_preprocessed_A_state':True,
  'opaque_X_in_selected_F_or_coin_never_materialized':True,
  'other_FJ_and_outside_coefficients_independent_marker':True,
  'source_root_counter_cache_only_Y_independent_data_or_counted_replies':True,
  'gated_completed_response_no_private_partial_buffer_exposure':True,
  'ghost_same_Y_service_code_not_claimed_literal_source':True,
  'honest_service_code_independent_marker_no_free_target_answers':True,
  'all_P_high_low_router_and_one_selected_final_call_QAplus1':True,
  'prefix_only_remote_access_fulloutput_embedding_same_query_count':True,
  'absorbing_partiality_and_nonzero_S_conjunction':True,
 },
 'expected_target_miss_sampling_cost':'n*N^2/(N-1) expected fair bits via reject largest integer; almost-sure termination, unbounded worst-case sampling time; n*N entry bits and charged lookup gates',
 'control_execution':{'exit_code':0,'marker_completion_relations':286,'fullword_phase_amplitudes':6144,'clean_scratch_checks':4,'query_envelope_cases':12,'scope':controls['scope']},
 'caller_premise_status':'CLOSED_MANUALLY_FOR_STATED_HJ_O_LOGICAL_INTERFACE',
 'new_source_game_declarations':0,'new_security_kernel_declarations':0,
 'fixed_SHA_full_security_category_capacity':'NOT_ESTABLISHED',
 'source_manuscript_old_numeric_bounds_prior_receipt_edits':0,
 'whole_goal_complete':False,
 'builder_sha256':sha(Path(__file__)),
}
(HERE/'FINAL-SUBJECT-REVIEW.json').write_text(json.dumps(single_receipt,indent=2)+'\n',encoding='utf8')
combined_receipt={
 'verdict':'ACCEPT_MANUAL_RANDOM_ORACLE_HIDDEN_COMPONENT_WITH_AUDITED_PRE_CALLER',
 'subject_path':str(combined),'subject_sha256':sha(combined),
 'review_md_sha256':sha(PARENT/'FINAL-HIDDEN-BOUND-REVIEW.md'),
 'single_PRE_subject_sha256':sha(single),
 'single_PRE_third_review':{'path':str(HERE/'FINAL-SUBJECT-REVIEW.json'),'sha256':sha(HERE/'FINAL-SUBJECT-REVIEW.json')},
 'prior_target_only_subject_and_receipt_pins':{'TARGET-ONLY-UD-RO.md':sha(ROOT/'TARGET-ONLY-UD-RO.md'),'outside-field-check/target-only-ud/FINAL-SUBJECT-REVIEW.json':sha(PARENT/'FINAL-SUBJECT-REVIEW.json')},
 'source':prior['source'],
 'model':'Ideal-private HJ[O], shared full256 random oracle, S!=0; no actual SHA assignment',
 'inequality':'Pr[Win AND H_final AND S!=0]<=min(1,D_H*min(1,(2R+1)^2*(2/N-1/N^2))+12*A_H*R/sqrt(N)), R=Q_A+1,N=2^128',
 'constants':{'N':str(N),'D_H':DH,'A_H':AH,'mu':str(mu),'UD_slope':str(slope)},
 'checks':{
  'no_primitive_prequeries_whole_source_prekey_counted_after_challenge':True,
  'caller_zero_state_marker_independent_not_assumed_from_name':True,
  'opaque_X_never_read_generated_root_cache_counter_Y_only':True,
  'all_unrelated_services_independent_or_target_query_counted':True,
  'actual_final_target_verification_reply_reused_in_QAplus1':True,
  'fullword_lower_allP_aliases_and_nonzero_branch_preserved':True,
  'exact_wholemark_PRE_constant_valid_for_caller_R':True,
  'valid_PRE_and_active_UD_selector_conditioning_correct':True,
  'outside_2Tall_field_table_time_storage_circuit_costs_retained':True,
  '32_quantitative_rows_reexecuted_byte_identical_all_caps1':True,
  'half_QA99_100_and_cap_QA200_201_exact_including_PRE':True,
  'sufficient_crossings_not_attacks_or_categories':True,
  'stronger_old_direct_hidden_theorem_preserved_no_replacement':True,
  'old_kappa_OPEN_receipt_immutable_separate_successor':True,
 },
 'root_quantitative_pins':pins(ROOT/'root-target-only-ud',['quantitative.py','QUANTITATIVE-RESULTS.json']),
 'independent_root_quantitative_reexecution':{'exit_code':0,'rows':32,'byte_identical_results':True,'pins':pins(HERE/'root-quantitative-recheck',['quantitative.py','QUANTITATIVE-RESULTS.json'])},
 'independent_endpoint_values':{str(qa):str(envelope(qa)) for qa in (99,100,200,201)},
 'preserved_old_direct_subject_pins':pins(ROOT,['DYNAMIC-QUANTUM-HIDDEN-THEOREM.md','QUANTUM-RO-THEOREM.md']),
 'old_direct_theorem_scope':'Inherited previously reviewed comparison; not newly recertified or numerically changed here',
 'material_correction_required':False,
 'new_source_game_declarations':0,'new_security_kernel_declarations':0,
 'source_manuscript_old_scalar_prior_receipt_edits':0,
 'full_fixed_SHA_security_category_capacity_parameter_repair':'NOT_ESTABLISHED',
 'whole_goal_complete':False,
 'builder_sha256':sha(Path(__file__)),
}
(PARENT/'FINAL-HIDDEN-BOUND-REVIEW.json').write_text(json.dumps(combined_receipt,indent=2)+'\n',encoding='utf8')
for base,names in [(HERE,['FINAL-SUBJECT-REVIEW.md','FINAL-SUBJECT-REVIEW.json','CONTROL-RESULTS.json']),(PARENT,['FINAL-HIDDEN-BOUND-REVIEW.md','FINAL-HIDDEN-BOUND-REVIEW.json'])]:
    for n in names:print(n,sha(base/n))

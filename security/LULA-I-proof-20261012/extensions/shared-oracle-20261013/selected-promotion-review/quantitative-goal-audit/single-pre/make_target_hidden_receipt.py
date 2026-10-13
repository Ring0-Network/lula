from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
X=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subjects={
 'TARGET-ONLY-HIDDEN-BOUND.md':'b6b2e65a6c6cb1af262809216163916d79a1e6dfe19c085957b98a3f01d6547a',
 'TARGET-ONLY-UD-RO.md':'4e0aeeb0b0ed72eae3dd45e506fee8bf57db176e7ed3b6ddcd5cf2393b52e9df',
 'SINGLE-TARGET-PRE-RO.md':'16b5b6f7dd49ba1a1b263e60de59c4c3e4ce078294482578139f3aa719bbf85a',
 'FIXED-H-HIDDEN-PREDECESSORS.md':'d47b8a5ecc72a3d1ff7f52d3b3a16be6220f4acf5d0c08416f902939320dbb13',
}
for n,h in subjects.items():assert sha(X/n)==h,n
receipt_names=(
 'outside-field-check/target-only-ud/FINAL-SUBJECT-REVIEW.json',
 'pre-start-second/interior-ud/quantitative-boundary/activation/single-pre/FINAL-SUBJECT-REVIEW.json',
 'selected-promotion-review/quantitative-goal-audit/single-pre/FINAL-SUBJECT-REVIEW.json')
for n in receipt_names:
 r=json.loads((X/n).read_text(encoding='utf-8'))
 assert r['subject_sha256'] in (subjects['TARGET-ONLY-UD-RO.md'],subjects['SINGLE-TARGET-PRE-RO.md'])
 assert r['whole_goal_complete'] is False
caller=json.loads((X/receipt_names[0]).read_text(encoding='utf-8'))
assert sha(X/receipt_names[0])=='36ef17cc915cb610a1aae908f79d8fbdecd702eb15cc2c2eb93e17c3de849d58'
assert caller['remote_cap'].startswith('Q_A+1')
numeric=json.loads((HERE/'TARGET-HIDDEN-NUMERIC-CHECK.json').read_text(encoding='utf-8'))
assert numeric['rows']==32 and numeric['root_copy_result_identical'] is True
prior=json.loads((X/'selected-promotion-review/HIDDEN-UD-PRE-INTEGRATION-REVIEW.json').read_text(encoding='utf-8'))
for n,h in prior['preserved_artifacts'].items():assert sha(X/n)==h,n
out={
 'verdict':'ACCEPT_EXACT_TARGET_ONLY_RANDOM_ORACLE_HIDDEN_COMPONENT_BOUND',
 'subject':'TARGET-ONLY-HIDDEN-BOUND.md','subject_sha256':subjects['TARGET-ONLY-HIDDEN-BOUND.md'],
 'subject_pins':subjects,'premise_receipt_pins':{n:sha(X/n) for n in receipt_names},
 'own_pins':{n:sha(HERE/n) for n in ('FINAL-TARGET-HIDDEN-SUBJECT-REVIEW.md','root_quantitative.py',
    'QUANTITATIVE-RESULTS.json','check_target_hidden.py','TARGET-HIDDEN-NUMERIC-CHECK.json','make_target_hidden_receipt.py')},
 'preserved_artifacts':prior['preserved_artifacts'],
 'checks':{n:True for n in ('exact_final_caller_and_PRE_subject_receipt_pins',
    'source_prekey_after_primitive_challenge_preserved_not_discarded',
    'opaque_input_Y_designated_edge_all_other_metadata_ghost_independent',
    'ghost_services_analytical_algorithm_not_false_source_law_claim',
    'atomic_response_gate_no_partial_secret_exposure','allP_fullword_literal_alias_router',
    'nonzero_inner_bytes_outer_length_other_tweak_honest_exclusions',
    'R_QAplus1_final_selected_reply_reused','outside_all_honest_storage_circuit_work_retained',
    'PRE_valid_selector_D_H_weight','UD_active_condition_before_abs_and_P',
    'primary_HK_Lemma3_12R_sqrtN_exact_random_family','single_PRE_stronger_kappa_used',
    'seedzero_unconditional_local_failure_no_recharge',
    'copied_root_script_only_executed_authorized_folder','root_result_byte_identical',
    'independent_exact32_rational_rows_and_resource_caps','adjacent99_100_half_crossing',
    'uncapped200_201_one_crossing_not_capped_probability_failure',
    'old_stronger_direct_hidden_bound_and_scalar_tables_preserved',
    'finite_RO_not_actual_fixed_h_hardness','no_efficient_nonbinary_table_or_category_claim')},
 'model':'Ideal-private HJ[O] complete shared random oracle, scoped atomic logical services',
 'bound':'min(1,D_H*kappa(Q_A+1)+12*sum_A_r*(Q_A+1)/2^64)',
 'all32_requested_component_caps':1,'half_crossing_QA':[99,100],'uncapped_one_crossing_QA':[200,201],
 'caller_premise_scope':'Exact reviewed manual target-only interface; inherited source/resource obligations, not new full-source kernel verification',
 'current_index_review':False,'new_source_game_checked_declarations':0,
 'new_source_game_declarations':0,'fixed_h_hardness_established':False,'whole_goal_complete':False,
}
p=HERE/'FINAL-TARGET-HIDDEN-SUBJECT-REVIEW.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(p))

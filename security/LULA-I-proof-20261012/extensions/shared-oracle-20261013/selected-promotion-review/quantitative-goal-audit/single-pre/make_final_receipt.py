from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
X=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(X/'SINGLE-TARGET-PRE-RO.md')=='16b5b6f7dd49ba1a1b263e60de59c4c3e4ce078294482578139f3aa719bbf85a'
assert sha(HERE/'INDEPENDENT-FIRST.md')=='1cf6aca94fc1c6db16f0444fe0eb56c5ec04f011c30484609927ea7e62cf6b1f'
peer=json.loads((HERE/'PEER-REVIEW.json').read_text(encoding='utf-8'))
for n,h in peer['peer_pins'].items():assert sha(X/n)==h,n
for n,h in peer['own_pins'].items():assert sha(HERE/n)==h,n
controls=json.loads((HERE/'WHOLE-MARKER-CONTROLS.json').read_text(encoding='utf-8'))
assert controls['status']=='PASS_CORRELATED_MARK_AND_FULLWORD_LAW'
out={
 'verdict':'ACCEPT_EXACT_FINAL_MANUAL_SINGLE_TARGET_PRE_RO_QUERY_THEOREM',
 'subject':'SINGLE-TARGET-PRE-RO.md','subject_sha256':sha(X/'SINGLE-TARGET-PRE-RO.md'),
 'own_pins':{n:sha(HERE/n) for n in ('INDEPENDENT-FIRST.md','PEER-REVIEW.md','PEER-REVIEW.json','FINAL-SUBJECT-REVIEW.md',
      'FINITE-TABLE-CLARIFICATION.md','WHOLE-MARKER-CONTROLS.json','whole_marker_controls.py',
      'peer_finite_controls.py','FINITE-CONTROLS.json','make_final_receipt.py')},
 'peer_pins':peer['peer_pins'],
 'bound':'min(1,(2Q+1)^2*(2/N-1/N^2))',
 'checks':{n:True for n in ('final_provenance_split_first_vs_stronger_review_accurate',
    'exact_single_exante_random_target_zero_public_prequeries',
    'initial_and_interquery_aux_independent_whole_field_conditional_Y_P',
    'correlated_marker_only_perpoint_mu_needed','latent_X_only_distribution_not_local_simulation',
    'purified_zero_oracle_mass_and_common_terminal_projector','adaptive_measurements_retained_memory_plus_padding',
    'whole_real_function_challenge_law_exact','fullword_independent_lower_limbs',
    'literal_aliases_selected_outside_delta_zero','one_ordinary_Boolean_fullword_call_clean_scratch',
    'no_unknown_controlled_oracle_or_unmarked_dummy_query','final_candidate_no_extra_digest_query',
    'Qzero_baseline_exact_upper_envelope_not_positiveQ_optimality',
    'older_split_and_primary_average_search_preserved','exact_Nminus1_table_no_biased_modulo',
    'huge_known_local_table_entropy_storage_circuit_costs_charged','no_efficient_sampler_claim',
    'peer_controls_reexecuted_exit0_identical','own_fullword_marker_controls_exit0',
    'caller_source_router_ghost_independence_remote_cap_separate_OPEN',
    'no_fixedSHA_numeric_category_capacity_sourcekernel_or_goal_closure')},
 'source_application_accepted':False,
 'efficient_reduction_claimed':False,'actual_fixed_h_hardness_established':False,
 'new_source_game_checked_declarations':0,'new_source_game_declarations':0,'whole_goal_complete':False,
}
p=HERE/'FINAL-SUBJECT-REVIEW.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(p))

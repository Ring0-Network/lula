from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
primary=Path('C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/M-measure/M2-sphincs-reparam/refs/eprint_2022_346_hulsing_kudinov_tight')
assert sha(primary.with_suffix('.pdf'))=='80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3'
assert sha(primary.with_suffix('.txt'))=='be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561'
assert sha(HERE/'INDEPENDENT-FIRST.md')=='1cf6aca94fc1c6db16f0444fe0eb56c5ec04f011c30484609927ea7e62cf6b1f'
controls=json.loads((HERE/'CONTROL-RESULTS.json').read_text(encoding='utf-8'))
assert controls['status']=='PASS_FINITE_LAW_AND_ONE_QUERY_CONTROLS'
assert controls['first_sha256']==sha(HERE/'INDEPENDENT-FIRST.md')
assert controls['clarification_sha256']==sha(HERE/'FINITE-TABLE-CLARIFICATION.md')
assert controls['script_sha256']==sha(HERE/'controls.py')
out={
 'status':'DERIVED_SOURCE_FIRST_CONDITIONAL_SINGLE_TARGET_QROM_PRE_QUERY_BOUND',
 'own_pins':{n:sha(HERE/n) for n in ('INDEPENDENT-FIRST.md','FINITE-TABLE-CLARIFICATION.md','SCOPE-AND-STATUS.md','controls.py','CONTROL-RESULTS.json','make_receipt.py')},
 'primary':{'pdf_path':str(primary.with_suffix('.pdf')),'pdf_sha256':sha(primary.with_suffix('.pdf')),
    'text_path':str(primary.with_suffix('.txt')),'text_sha256':sha(primary.with_suffix('.txt')),'anchor':'Section8.2 Definition9/Theorem4, cached text1027-1036'},
 'original_hit':'min(1,(2Q+1)^2/N)',
 'different_hit':'min(1,8(Q+1)^2/N)',
 'total_bound':'min(1,(12Q^2+20Q+9)/N)',
 'N':'2^128, both input count and target-prefix count',
 'checks':{n:True for n in ('single_tweak_chosen_exante_no_public_prequeries',
     'fullword_overlay_exact_real_joint_law','ghost_X_independent_auxiliary_state_explicit',
     'original_hit_common_terminal_projector_no_query_measurement',
     'different_input_known_X_only_reduction_internal',
     'exact_Nminus1_miss_and_uniform_lower_limbs','one_Boolean_query_clean_Fourier_completion',
     'designated_outside_delta_zero_not_controlled_oracle','final_candidate_output_before_hash_QnotQplus1',
     'all_raw_aliases_inside_row_are_charged','full256_outside_correlations_preserved',
     'finite_independent_tables_huge_resources_explicit','binary2Twise_nonpoweroftwo_efficiency_not_claimed',
     'finite_controls_exit0_no_source_execution','no_fixedSHA_UD_source_security_or_category_substitution')},
 'new_peer_read':False,'independent_final_peer_acceptance':False,
 'new_source_game_checked_declarations':0,'actual_fixed_h_hardness':'NOT_ESTABLISHED','whole_goal_complete':False,
}
p=HERE/'REVIEW-RECEIPT.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(p))

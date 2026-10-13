from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;X=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(HERE/'INDEPENDENT-FIRST.md')=='6eade370c61bfaf4b9c907b69d0cbabc692a82b446414c3d4dbd5ed977c50baa'
assert sha(X/'QUANTUM-UD-POLYNOMIAL-RO.md')=='55971b61f6fd7cba54fe589c100d61351e67f7373182515593cf2c63d83bb7d5'
assert (HERE/'root_controls.py').read_bytes()==(X/'root-ud-polynomial/controls.py').read_bytes()
assert (HERE/'CONTROLS.json').read_bytes()==(X/'root-ud-polynomial/CONTROLS.json').read_bytes()
prior=json.loads((X/'selected-promotion-review/TARGET-PRE-INTEGRATION-REVIEW.json').read_text(encoding='utf-8'))
for n,h in prior['preserved_artifacts'].items():assert sha(X/n)==h,n
check=json.loads((HERE/'INDEPENDENT-CONTROLS.json').read_text(encoding='utf-8'))
assert check['source_component_rows']==32
primary_names=('beals-quant-ph-9802049v3.pdf','beals-quant-ph-9802049v3.txt','beals-author-polynomials.pdf',
 'beals-author-polynomials.txt','beals-theorem-4-12.png','markov-mendeleev-translation.pdf','markov-mendeleev-translation.txt')
out={
 'verdict':'ACCEPT_EXACT_MANUAL_QUADRATIC_ONE_TARGET_UD_RO_AND_SCOPED_CALLER',
 'subject':'QUANTUM-UD-POLYNOMIAL-RO.md','subject_sha256':sha(X/'QUANTUM-UD-POLYNOMIAL-RO.md'),
 'own_pins':{n:sha(HERE/n) for n in ('INDEPENDENT-FIRST.md','FINAL-SUBJECT-REVIEW.md','root_controls.py','CONTROLS.json',
    'independent_controls.py','INDEPENDENT-CONTROLS.json','make_receipt.py')},
 'primary_pins':{n:sha(HERE/n) for n in primary_names},
 'primary_anchors':{'beals_v3':'Lemmas3.2,4.1,4.2','beals_author':'Lemma4.2/3.2 and Theorem4.12 printed12, visually inspected',
    'markov_original_translation':'ProblemNo.2 conclusion printed16,2d^2 L/(b-a)'},
 'peer_first_pins':{n:sha(X/n) for n in ('root-ud-polynomial/INDEPENDENT-FIRST.md','outside-field-check/ud-polynomial/INDEPENDENT-FIRST.md')},
 'premise_pins':{n:sha(X/n) for n in ('TARGET-ONLY-UD-RO.md','FIXED-H-HIDDEN-PREDECESSORS.md','SINGLE-TARGET-PRE-RO.md',
    'outside-field-check/target-only-ud/FINAL-SUBJECT-REVIEW.json')},
 'preserved_artifacts':prior['preserved_artifacts'],
 'bound':'min(1,(1-1/N)*4Q^2/(N-4Q^2)) if4Q^2<N, else1',
 'checks':{n:True for n in ('own_first_saved_before_new_peer_root_derivations','primary_Beals_degree_symmetrization_read',
    'primary_grid_theorem_formula_visually_verified','original_Markov_derivative_normalization_verified',
    'same_joint_conditional_aux_law_not_separate_independence_only','iid_ideal_planted_real_exact_laws_not_marginals_only',
    'one_ordinary_Boolean_fullword_completion','degree2Q_grid0_1_and_signed_binomial_difference',
    'centering_nearest_grid_Markov_denominator_retained','Qzero0_valid_branch_and_largeQ_cap1',
    'fullword_ALLP_literal_aliases_and_lower_limb_preserved','actual_opaque_Y_source_caller_same_code_and_coins',
    'completed_response_gates_partial_noncompletion_no_hiddenX_advice','source_prekey_chronology_no_unknown_prequest',
    'remote_QAplus1_final_reply_reuse_outside_honest_work_charged','active_condition_before_parameter_and_absolute',
    'one_source_seedzero_charge_not_component_recharge','root_controls_copy_reexec_exit0_identical',
    'independent66_binomial37_grid5_phase_and_negative_controls','exact32_rows_and_two_uncapped_adjacent_crossings',
    'old_stronger_directH_full_source_scalars_preserved','exactNminus1_resource_boundary_no_efficiency_or_cost_lower_claim',
    'privateK_separate_candidate_not_read_or_accepted','no_SHA_category_capacity_repair_or_whole_goal_closure')},
 'caller_scope':'Manual exact primitive/source-interface premises, not full source kernel refinement',
 'new_source_game_checked_declarations':0,'new_source_game_declarations':0,
 'actual_fixed_h_hardness_established':False,'whole_goal_complete':False,
}
p=HERE/'FINAL-SUBJECT-REVIEW.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(p))

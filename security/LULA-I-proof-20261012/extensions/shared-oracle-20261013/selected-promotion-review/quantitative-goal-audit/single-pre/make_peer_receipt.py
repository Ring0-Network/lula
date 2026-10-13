from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
X=HERE.parents[2]
PEER=X/'pre-start-second/interior-ud/quantitative-boundary/activation/single-pre'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(HERE/'INDEPENDENT-FIRST.md')=='1cf6aca94fc1c6db16f0444fe0eb56c5ec04f011c30484609927ea7e62cf6b1f'
assert sha(PEER/'INDEPENDENT-FIRST.md')=='618ea5b85ff695e76aa785a916e2dcee3abbd28edbc0f930cbd972b9fa14b3f2'
assert sha(PEER/'DERIVATION-RECEIPT.json')=='c0778ff5d29962a167f3f34a1c6a66a8be30953d84ceeb761305d0349dacb34f'
assert (HERE/'FINITE-CONTROLS.json').read_bytes()==(PEER/'FINITE-CONTROLS.json').read_bytes()
assert (HERE/'peer_finite_controls.py').read_bytes()==(PEER/'finite_controls.py').read_bytes()
out={
 'verdict':'ACCEPT_MANUAL_CORRELATED_WHOLE_MARKER_FINITE_SINGLE_PRE_DERIVATION',
 'peer_pins':{(PEER/n).relative_to(X).as_posix():sha(PEER/n) for n in ('INDEPENDENT-FIRST.md','DERIVATION-RECEIPT.json','finite_controls.py','FINITE-CONTROLS.json')},
 'own_pins':{n:sha(HERE/n) for n in ('INDEPENDENT-FIRST.md','REVIEW-RECEIPT.json','PEER-REVIEW.md','peer_finite_controls.py','FINITE-CONTROLS.json','whole_marker_controls.py','WHOLE-MARKER-CONTROLS.json','make_peer_receipt.py')},
 'whole_bound':'min(1,(2Q+1)^2*(2/N-1/N^2))',
 'own_first_bound_preserved':'min(1,(12Q^2+20Q+9)/N)',
 'checks':{n:True for n in ('own_first_saved_before_authorized_peer_read','exact_peer_first_receipt_pins',
    'latent_X_only_generates_whole_marker_not_simulator_localdata',
    'whole_field_independent_known_G_L_outside_tables_conditional_Y_P',
    'correlated_coordinates_only_perpoint_marginal_mu_needed',
    'zero_oracle_quantum_prefix_and_output_independent_entire_field',
    'common_terminal_projector_norm_gap_2Qsqrtmu',
    'one_Boolean_call_linear_or_Fourier_exact_with_clean_plus_masks',
    'Q_final_candidate_no_digest_extra_query','fullword_lower_limb_extension_distribution_exact',
    'literal_raw_aliases_cannot_be_free_outside','exact_Nminus1_sampling_not_binarymodulo',
    'huge_tables_circuits_charged_no_efficiency_claim','Qzero_baseline_exact_valid_node',
    'peer_controls_reexecution_exit0_byte_identical','own_correlated_fullword_negative_controls_exit0',
    'no_source_target_router_or_actual_hardness_certification')},
 'source_application':'SEPARATE_UNREVIEWED_CALLER_OBLIGATION',
 'new_source_game_checked_declarations':0,'whole_goal_complete':False,
}
p=HERE/'PEER-REVIEW.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',sha(p))

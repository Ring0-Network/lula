"""Finalize own-folder subject-only review, leaving all prior packets immutable."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
PEER=ROOT/'pre-start-second'/'interior-ud'/'quantitative-boundary'/'activation'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pins(base,names):return {n:sha(base/n) for n in names}
subject=ROOT/'TARGET-ONLY-UD-RO.md'
assert sha(subject)=='4e0aeeb0b0ed72eae3dd45e506fee8bf57db176e7ed3b6ddcd5cf2393b52e9df'
assert sha(HERE/'INDEPENDENT-FIRST.md')=='fca41de9835bd7b681fac94ecbd8a521f00361d7a2c007cb8410e1655c5650bd'
prior=json.loads((HERE/'SOURCE-FIRST-RECEIPT.json').read_text())
assert sha(Path(prior['source']['path']))==prior['source']['sha256']
assert sha(Path(prior['primary']['text']))==prior['primary']['text_sha256']
for n in ('router_controls.py','ROUTER-CONTROLS.json'):
    assert sha(HERE/'root-router-recheck'/n)==sha(ROOT/'root-target-only-ud'/n)
controls=json.loads((HERE/'CONTROL-RESULTS.json').read_text())
assert controls['script_sha256']==sha(HERE/'controls.py')
A=7628143271608320
slope=Fraction(12*A,1<<64)
assert slope==Fraction(682009155,137438953472)
out={
 'verdict':'ACCEPT_MANUAL_FULL_SHARED_RANDOM_ORACLE_TARGET_ONLY_ROUTER_AND_UD_COMPONENT',
 'scope':'Exact final root subject only; not current-index/promotion, fixed-SHA hardness or whole-source kernel receipt',
 'subject_path':str(subject),'subject_sha256':sha(subject),
 'review_md_sha256':sha(HERE/'FINAL-SUBJECT-REVIEW.md'),
 'own_first_saved_before_new_target_only_peer_root_artifact_read':True,
 'own_pins':pins(HERE,['INDEPENDENT-FIRST.md','SOURCE-FIRST-RECEIPT.json','controls.py','CONTROL-RESULTS.json']),
 'root_first_and_controls':pins(ROOT/'root-target-only-ud',['INDEPENDENT-FIRST.md','router_controls.py','ROUTER-CONTROLS.json']),
 'activation_peer_pins':pins(PEER,['INDEPENDENT-FIRST.md','ACTIVATION-RECEIPT.json','activation_arithmetic.py']),
 'supporting_subject_pins':pins(ROOT,['FIXED-H-HIDDEN-PREDECESSORS.md','OUTSIDE-SIMULATOR-THEOREM.md','CHANGED-CHILD-EXTRACTION.md']),
 'source':prior['source'],'primary':prior['primary'],
 'model':'Single complete shared256-bit random oracle O, ideal independent persistent F/J, finite ex-ante raw encoding/unitary extension and S!=0 conjunction; not fixed SHA',
 'remote_cap':'Q_A+1 ordinary H evaluations, including coherent pre-key + continuing A raw queries and at most one final selected typed call',
 'local_budget':'T_all=Q_A+H_setup+q*H_mode+3224+254;2T_all independent hidden polynomial G; ALL known local source/circuit/generation/storage work charged',
 'activation':{'selector_bits':55,'D_H':20229886488608768,'sum_A_r':A,'sum_a_r':str(Fraction(A,1<<55)),'UD_slope':str(slope),'effective_Q_half_crossing':str(Fraction(1,2)/slope),'effective_Q_cap_crossing':str(1/slope),'first_integer_effective_half_cap':[101,202]},
 'inequality':'Pr_HJ_O[Win AND H_final AND S!=0] <= min(1,D_H*kappa_PRE(Q_A+1,128)+12*sum_A_r*(Q_A+1)/2^64)',
 'checks':{
  'all_P102_byte_slice_injective_and_complete_lower_limb':True,
  'full_shared_O_joint_law_and_repeats_preserved':True,
  'one_ordinary_remote_and_one_known_outside_query_clean_entangled_router':True,
  'no_controlled_unknown_oracle_or_second_uncomputation_query':True,
  'nonzero_S_inner_byte_exclusion_outer_length_and_other_exact_ADRS':True,
  'actual_S0_alias_negative_control_all_P0_adversarial_queries_retained':True,
  'designated_selected_image_intercepted_and_gated_suffix_response':True,
  'final_selected_typed_call_at_most_once_reply_reused':True,
  'source_root_cache_quantum_continuation_completion_laws_preserved':True,
  'no_nohit_blocking_query_history_measurement_or_programming':True,
  'outside_G_H_F_J_independent_known_local_circuits':True,
  'ALL_honest_and_A_outside_calls_in_2T_budget':True,
  'outside_field_key_time_gates_memory_and_invalid_state_extension_charged':True,
  'published_HK_randomTh12QsqrtN_applicable_no_collection_conjecture':True,
  'active_selector_conditional_program_legal_before_P':True,
  'signed_average_before_absolute_inactive_and_dummy_cancellation':True,
  'valid_PRE_selector_weight_exact':True,
  'explicit_kappa_PRE_OPEN_not_Theta_or_zero':True,
  'thresholds_envelope_only_not_attack_or_category':True,
  'old_direct_bounds_and_scalar_tables_unchanged':True,
 },
 'own_control_execution':{'exit_code':0,'unitary_checks':4160,'joint_distribution_tables':256,'byte_checks':33,'scope':controls['scope']},
 'root_control_independent_reexecution':{'exit_code':0,'tables':1024,'response_amplitude_checks':65536,'byte_identical_output':True,'pins':pins(HERE/'root-router-recheck',['router_controls.py','ROUTER-CONTROLS.json'])},
 'explicit_finite_single_PRE_bound':'OPEN_AT_THIS_SUBJECT_NO_CONSTANT_INFERRED',
 'material_correction_required':False,
 'new_source_game_declarations':0,'new_security_kernel_declarations':0,
 'source_manuscript_old_numeric_bounds_prior_receipt_edits':0,
 'fixed_h_hardness_complete_security_category_capacity':'NOT_ESTABLISHED',
 'whole_goal_complete':False,
 'builder_sha256':sha(Path(__file__)),
}
(HERE/'FINAL-SUBJECT-REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
for n in ('FINAL-SUBJECT-REVIEW.md','FINAL-SUBJECT-REVIEW.json'):
    print(n,sha(HERE/n))

"""Pin final subject-only interior-predecessor review; writes in this folder only."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
SOURCE=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
DRIVER=SOURCE.parent/'bin'/'lula1_driver_original.rs'
HK=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\M-measure\M2-sphincs-reparam\refs\eprint_2022_346_hulsing_kudinov_tight.txt')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pins(base,names):return {n:digest(base/n) for n in names}
subject=ROOT/'FIXED-H-HIDDEN-PREDECESSORS.md'
assert digest(subject)=='d47b8a5ecc72a3d1ff7f52d3b3a16be6220f4acf5d0c08416f902939320dbb13'
assert digest(SOURCE)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert digest(HK)=='be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561'
assert digest(HERE/'INDEPENDENT-FIRST.md')=='11425f21cd72b464fc8b237f50d742be1e9c9e4e6b60dd92680b1fdd504f3059'
assert digest(HERE/'CLARIFICATION.md')=='1c8672afbcB84298e8a840925e7533516385faf1e765fdf6c86c0091c676e0e7'.lower()
for n in ('toy_channels.py','TOY-CONTROLS.json'):
    assert digest(HERE/'root-control-recheck'/n)==digest(ROOT/'root-interior-ud'/n)
own_controls=json.loads((HERE/'CONTROL-RESULTS.json').read_text())
assert own_controls['script_sha256']==digest(HERE/'controls.py')
receipt={
 'verdict':'ACCEPT_MANUAL_ORDINARY_UD_PRE_HIDDEN_PREDECESSOR_COMPONENT',
 'subject_path':str(subject),'subject_sha256':digest(subject),
 'review_md_sha256':digest(HERE/'FINAL-SUBJECT-REVIEW.md'),
 'own_first_saved_before_new_peer_root_interior_reads':True,
 'own_pins':pins(HERE,['INDEPENDENT-FIRST.md','CLARIFICATION.md','controls.py','CONTROL-RESULTS.json']),
 'peer_pins':pins(ROOT/'pre-start-second'/'interior-ud',['INDEPENDENT-FIRST.md','ROOT-REVIEW.md']),
 'root_candidate_and_controls':pins(ROOT/'root-interior-ud',['DERIVATION-CANDIDATE.md','toy_channels.py','TOY-CONTROLS.json']),
 'root_control_independent_rerun':{'exit_code':0,'byte_identical_result':True,'checks':3072,'pins':pins(HERE/'root-control-recheck',['toy_channels.py','TOY-CONTROLS.json'])},
 'source':{'path':str(SOURCE),'sha256':digest(SOURCE),'anchors':'121-151;239-267;291-307;479-584;601-667;679-729'},
 'geometry_driver':{'path':str(DRIVER),'sha256':digest(DRIVER),'anchors':'lines7-20 lula1 parameter choice, not persistence fixtures'},
 'primary':{'text_path':str(HK),'text_sha256':digest(HK),'pdf_sha256':digest(HK.with_suffix('.pdf')),'anchors':'HK22 Definitions3-4 text188-208/printed5; Definition7 text241-268/printed6; Claim2 text437-511'},
 'event_anchor':pins(ROOT,['CHANGED-CHILD-EXTRACTION.md']),
 'source_scope':'Ideal-private HJ[h] with independent memoized F/J, fixed public full h, uniform S, logical API including actual root/cache/signature results and absorbing atomic-service noncompletion. Original private h-derived starts require separate PRF hops.',
 'inequality':'Pr_HJ_h[Win AND H_final AND S!=0] <= min(1,2^55*(Succ_SM_PRE(B_PRE)+sum_(r=0)^253 Adv_SM_UD(B_UD_r)))',
 'geometry':own_controls['actual_geometry'],
 'checks':{
  'ordinary_fixed_target_before_P_then_source_setup_pk_release':True,
  'one_primary_target_zero_stage1_collection_calls':True,
  'acyclic_selected_endpoint_child_root_counter_routing_dependencies':True,
  'persistent_replacements_consistent_cache_restores':True,
  'completed_response_gate_no_internal_setup_exposure':True,
  'opaque_slots_not_streamed_all_remaining_rows_completed':True,
  'natural_failure_and_partiality_unnormalized':True,
  'observable_next_image_superset_no_hidden_equality_or_first_H_classifier':True,
  'original_H_source_event_inclusion_not_event_equality':True,
  'exact_real_random_selected_hybrid_marginal_laws':True,
  'quantum_channel_public_h_unchanged_no_history_measurement':True,
  'no_no_hit_restriction_or_programming':True,
  'terminal_PRE_any_matching_preimage':True,
  'signed_selector_gaps_averaged_before_absolute':True,
  'inactive_FORS_low_positions_dummy_contributions_cancel':True,
  '55bit_selector_geometry_254_hops_independently_checked':True,
  'nonzero_conjunction_same_in_all_programs_external_seed_mass_once':True,
  'actual_S0_aliases_no_independent_ro_or_namespace_tags':True,
  'one_extra_F_label_254_hashes_4096_nodebytes_plus_metadata':True,
  'all_source_challenger_circuit_storage_bytes_costs_charged':True,
  'source_call_caps_classified_inherited_not_fresh_full_source_audit':True,
  'private_cache_disclosure_arbitrary_secret_timing_not_claimed':True,
  'own_controls_exit0_and_root_rerun_byte_identical':True,
 },
 'own_control_checks':26,
 'own_control_aggregate_probabilities':own_controls['aggregate_event_probabilities'],
 'own_nonzero_filtered_probabilities_unnormalized':own_controls['nonzero_filtered_aggregate_probabilities_unnormalized'],
 'own_control_scope':own_controls['scope'],
 'material_correction_required':False,
 'new_source_game_declarations':0,
 'source_manuscript_numeric_scalar_prior_receipt_edits':0,
 'evaluated_hardness_quantitative_adequacy_full_security_category_capacity':'NOT_ESTABLISHED',
 'whole_goal_complete':False,
 'builder_sha256':digest(Path(__file__)),
}
(HERE/'FINAL-SUBJECT-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
for n in ('FINAL-SUBJECT-REVIEW.md','FINAL-SUBJECT-REVIEW.json','CONTROL-RESULTS.json'):
    print(n,digest(HERE/n))

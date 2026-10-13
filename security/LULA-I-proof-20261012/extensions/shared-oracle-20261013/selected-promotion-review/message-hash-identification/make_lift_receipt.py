import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
PEER=X/'outside-field-check/message-hash-identification'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(HERE/'COUNTER-GUESS-LIFT.md')=='9c1fadb8eedc8dbf19f20800a0950836433c00f0782297d9f315fca0328433ca'
assert sha(PEER/'PROBABILISTIC-LIFT-FIRST.md')=='c558399bc390589efddc4176bf45a90be0df04562e5e7395798108878d4c08c8'
own=('COUNTER-GUESS-LIFT.md','COUNTER-GUESS-INPUT-COMPLETION.md','COUNTER-GUESS-MAP-CLARIFICATION.md','COUNTER-GUESS-SOURCE-ROUTE.md','counter_guess_controls.py','COUNTER-GUESS-CONTROLS.json','compare_lift_controls.py','LIFT-COMPARISON-CONTROLS.json','PROBABILISTIC-LIFT-PEER-REVIEW.md','REVIEW-RECEIPT.json')
result={
 'status':'ACCEPTED_MANUAL_DISTINCT_FULL_REGISTER_AND_SPARSE_ORDINARY_ITSR_LIFTS',
 'own_lift_first_saved_before_new_peer_lift_read':True,
 'own_files':{n:sha(HERE/n) for n in own},
 'peer_lift_subject':{'outside-field-check/message-hash-identification/PROBABILISTIC-LIFT-FIRST.md':sha(PEER/'PROBABILISTIC-LIFT-FIRST.md')},
 'full_register_nonabort':{'target_queries':'q_distinct<=q','loss':'L^k, k=min(17,q); <=2^544','q0':'C_source impossible'},
 'peer_full_abort_baseline':{'target_queries':'q_distinct<=q','loss':'L^q','source_law':'faithful matched prefixes only'},
 'peer_sparse':{'target_queries':'<=k=min(17,q)','loss':'(Q*L)^k, Q=least power2>=q','dummy_duplicate_slots':'retained without normalization'},
 'checks':{n:True for n in (
  'ordinary_nonce_key_after_chosen_counter_interface','full_nonabort_source_view_guess_independent',
  'sparse_unflagged_comparator_and_scaled_matched_quantum_channels','witness_first_completion_distinct_labels_at_most17',
  'no_query_history_measurement_or_witness_leakage','canonical_Hcan_separator_does_not_refute_Hfree',
  'source_context_F_auxiliaries_and_actual_h_words','rank_domain_unique_total_with_maxbplus1',
  'chosencontext_route297_is_label_not_random_entropy','source_route41_no_pF297_numeric_transfer',
  'actual_bottom_vs_artificial_guess_abort_distinct','fresh_source_message_implies_primary_pair_fresh',
  'optional18_hash_coordinate_no_extra_secret_witness_or_guess','all_runtime_hash_bytes_circuits_charged',
  'exact_comparison_controls_exit0','no_existing_scalar_or_source_change')},
 'optional18_variant':'accepted bookkeeping implication only; not new source tree/exposure or entropy',
 'new_checked_source_game_declarations':0,
 'actual_primitive_hardness':'NOT_ESTABLISHED',
 'quantitative_adequacy_category_capacity':'NOT_ESTABLISHED',
 'whole_goal_complete':False,
}
(HERE/'PROBABILISTIC-LIFT-REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(sha(HERE/'PROBABILISTIC-LIFT-REVIEW.json'))

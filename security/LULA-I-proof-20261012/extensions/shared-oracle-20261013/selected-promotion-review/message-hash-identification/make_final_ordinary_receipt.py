import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
PEER=X/'outside-field-check/message-hash-identification'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subject='72a398e9a2d991b83de02c7982eae1ca6bdbb4c59d684b86094865ff03ef04cc'
assert sha(X/'MESSAGE-HASH-ORDINARY-LIFT.md')==subject
assert sha(X/'MESSAGE-HASH-PRIMITIVE-COMPONENT.md')=='1406428b0f8ab96e0b5aa923a372c0773067fbc4d79f0f6c2065fd17edfb0dff'
assert sha(PEER/'PROBABILISTIC-LIFT-REVIEW.json')=='7bed93dfadde9b5f9cd0b06e7f27bde91f27297d1ba2787b39cd1254c5771573'
prior=json.loads((HERE/'REVIEW-RECEIPT.json').read_text(encoding='utf-8'))
for p in prior['primary_versions']:
    assert sha(Path(p['pdf']))==p['pdf_sha256']
    assert sha(Path(p['text']))==p['text_sha256']
result={
 'status':'ACCEPTED_EXACT_FINAL_MANUAL_ORDINARY_ITSR_LOSS_AWARE_SUBJECT',
 'current_index_review':False,
 'subject_pins':{'MESSAGE-HASH-ORDINARY-LIFT.md':subject,'MESSAGE-HASH-PRIMITIVE-COMPONENT.md':sha(X/'MESSAGE-HASH-PRIMITIVE-COMPONENT.md')},
 'own_pins':{n:sha(HERE/n) for n in ('FINAL-ORDINARY-SUBJECT-REVIEW.md','COUNTER-GUESS-LIFT.md','COUNTER-GUESS-INPUT-COMPLETION.md','COUNTER-GUESS-MAP-CLARIFICATION.md','COUNTER-GUESS-SOURCE-ROUTE.md','PROBABILISTIC-LIFT-PEER-REVIEW.md','PROBABILISTIC-LIFT-REVIEW.json','REVIEW-RECEIPT.json','LIFT-COMPARISON-CONTROLS.json')},
 'peer_pins':{str((PEER/n).relative_to(X)).replace('\\','/'):sha(PEER/n) for n in ('PROBABILISTIC-LIFT-FIRST.md','PROBABILISTIC-LIFT-REVIEW.md','PROBABILISTIC-LIFT-REVIEW.json','FINAL-ORDINARY-SUBJECT-REVIEW.md','FINAL-ORDINARY-SUBJECT-REVIEW.json')},
 'primary_versions':prior['primary_versions'],
 'checks':{n:True for n in ('total_rank_family_fully_specified','source_exante_bound_all_executions','rank_extra_domain_bplus1_hardness_named','same_h_exact_words_tag_metadata_only','dense_exact_source_channel_guess_independent','at_most17_completed_distinct_witnesses','sparse_matching_prefix_quantum_channels_not_unconditional_abortlaw','dense_qtargets_Lk_vs_sparse_ktargets_BordLk','nonce_memoization_freshness_bottom','no_uniform297route_or_pF297_transfer','optional18_no_extra_source_tree_or_loss','all_source_and_challenger_costs_explicit','prior_direct_component_unchanged','actual_primary_pins_rechecked','no_old_scalar_or_category_upgrade')},
 'new_source_game_checked_declarations':0,
 'actual_family_hardness_or_numerical_adequacy':'NOT_ESTABLISHED',
 'whole_goal_complete':False,
}
(HERE/'FINAL-ORDINARY-SUBJECT-REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(sha(HERE/'FINAL-ORDINARY-SUBJECT-REVIEW.json'))

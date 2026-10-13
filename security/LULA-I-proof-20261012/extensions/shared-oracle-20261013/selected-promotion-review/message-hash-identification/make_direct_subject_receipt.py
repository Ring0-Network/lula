import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected='1406428b0f8ab96e0b5aa923a372c0773067fbc4d79f0f6c2065fd17edfb0dff'
assert sha(X/'MESSAGE-HASH-PRIMITIVE-COMPONENT.md')==expected
result={
 'status':'ACCEPTED_EXACT_DIRECT_NAMED_MESSAGE_HASH_COMPONENT_SUBJECT',
 'current_index_review':False,
 'subject_pins':{'MESSAGE-HASH-PRIMITIVE-COMPONENT.md':expected},
 'own_pins':{n:sha(HERE/n) for n in ('DIRECT-COMPONENT-SUBJECT-REVIEW.md','INDEPENDENT-FIRST.md','CONTEXT-LIFT-CLARIFICATION.md','REVIEW-RECEIPT.json','PROBABILISTIC-LIFT-REVIEW.json')},
 'event':'Win AND indexed17 C_cov from completed signatures',
 'checks':{n:True for n in ('exact_same_h_fullword_source_frames','actual_root_F_jointlaw_and_prekey','memoized_new_label_nonce_law','canonical_target_free_valid_finalcounter_explicit','bottom_unnormalized_absorbing','no_commit_or_false_source_exposure','no_new_seedzero_penalty_interface_only','logical_tags_not_source_hash_bytes','all_runtime_work_charged','primary_ITSR_numerical_hardness_unproved','ordinary_guess_candidates_separate_not_in_this_subject','old_scalar_source_manuscript_unchanged')},
 'new_source_game_checked_declarations':0,'whole_goal_complete':False,
}
(HERE/'DIRECT-COMPONENT-SUBJECT-REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(sha(HERE/'DIRECT-COMPONENT-SUBJECT-REVIEW.json'))

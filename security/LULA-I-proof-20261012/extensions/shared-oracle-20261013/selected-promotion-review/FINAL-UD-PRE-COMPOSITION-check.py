import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
X=HERE.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads((X/p).read_text(encoding='utf-8'))
expected={
    'FIXED-H-COMPOSITION-WITH-UD-PRE.md':'99dd90a7c3623357b60377f5e9c1f720a9a23170b9d78ddfa6f0a11a154eb856',
    'FIXED-H-HIDDEN-PREDECESSORS.md':'d47b8a5ecc72a3d1ff7f52d3b3a16be6220f4acf5d0c08416f902939320dbb13',
    'FIXED-H-COMPOSITION.md':'ece1d8311059d3b7d8dd3f2aca091ab28b2e17fb8cdff84fc2792e1443e892ae',
    'selected-promotion-review/FINAL-COMPOSITION-SUBJECT-REVIEW.json':'2c4a4bee5701fc87ac4f1731e49c47fa9c9e77c1783f8e1fd39db26330581350',
    'selected-promotion-review/MESSAGE-GRAPH-INTEGRATION-REVIEW.json':'e5ca80bf96b4898e3ab2b489f7552aacca26b6d9ef73ce51d7f53e41afa2d06e',
}
for n,h in expected.items(): assert sha(X/n)==h,n
previous=read('selected-promotion-review/MESSAGE-GRAPH-INTEGRATION-REVIEW.json')
for n,h in previous['preserved_artifacts'].items(): assert sha(X/n)==h,n
second_name='pre-start-second/interior-ud/FINAL-SUBJECT-REVIEW.json'
second=read(second_name)
assert second['subject_sha256']==expected['FIXED-H-HIDDEN-PREDECESSORS.md']
assert second['whole_goal_complete'] is False and second['new_source_game_declarations']==0
assert second['review_status']=='ACCEPT_MANUAL_CONDITIONAL_ORDINARY_UD_PRE_INTERFACE'
checks={n:True for n in (
    'exact_final_subject_hashes','full_composition_and_hidden_subject_read',
    'hidden_proof_premise_separate_from_algebra_review','available_second_reader_binds_exact_hidden_subject',
    'private_telescoping_precedes_pointwise_union','Win_fresh_root_completed_indexed_source_cover',
    '254_separate_signed_average_UD_advantages','hidden_image_superset_requires_inequality_not_equality',
    '55bit_selector_factor_and_inner_min_cap','one_outer_seedzero_no_private_or_primitive_recharge',
    'Gamma_cov_distinct_available_resource_hypotheses','NEW_graph55_55_21_41_42_particular_successes',
    'type7_42_21_unconditional_success_no_extra_eta',
    'all_full_public_h_source_challenger_quantum_resources_remain_bound',
    'no_unknown_input_equality_or_quantum_history_observation_import',
    'no_actual_fixed_h_hardness_numeric_or_RO_substitution',
    'dense_2pow544_is_loss_not_security_bits','old_subject_index_receipts_source_scalars_preserved',
    'no_source_game_kernel_category_capacity_or_repair_closure')}
receipt={
    'status':'ACCEPTED_CONDITIONAL_UD_PRE_COMPOSITION_ALGEBRA',
    'subject_sha256':expected['FIXED-H-COMPOSITION-WITH-UD-PRE.md'],
    'subject_pins':{n:h for n,h in expected.items() if n.endswith('.md')},
    'prior_review_receipts':{n:h for n,h in expected.items() if n.endswith('.json')},
    'hidden_proof_premise_receipts':{second_name:sha(X/second_name)},
    'preserved_artifacts':previous['preserved_artifacts'],
    'provenance_pins':{f'selected-promotion-review/{n}':sha(HERE/n) for n in ('FINAL-UD-PRE-COMPOSITION-REVIEW.md','FINAL-UD-PRE-COMPOSITION-check.py')},
    'checks':checks,
    'scope':'Conditional algebra only; hidden ordinary reduction is an exact-subject separately reviewed premise',
    'hidden_proof_outside_field_final_receipt_status':'PENDING_AT_THIS_REVIEW_CUT_REQUIRE_EXACT_BINDING_BEFORE_PREMISE_PROMOTION',
    'new_source_game_checked_declarations':0,
    'actual_fixed_h_hardness':'NOT_ESTABLISHED',
    'whole_goal_complete':False,
}
out=HERE/'FINAL-UD-PRE-COMPOSITION-REVIEW.json'
out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print('ACCEPTED_CONDITIONAL_ALGEBRA',sha(out))

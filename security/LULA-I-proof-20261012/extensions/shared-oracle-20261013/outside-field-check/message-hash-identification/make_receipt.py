import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parents[1]
SELECTED = X / 'selected-promotion-review/message-hash-identification'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
peer_receipt = load(SELECTED / 'REVIEW-RECEIPT.json')
assert sha(HERE / 'INDEPENDENT-FIRST.md') == 'b07700807df0f78be2272afd7a5372044603b92697b3760afaa8cdfac5a3a1df'
assert sha(HERE / 'CLARIFICATION.md') == '77b1c53d624b8980621f2366ec7ba41e9456955b58024e3cb227b85cfdb27891'
for name, expected in peer_receipt['files'].items():
    assert sha(SELECTED / name) == expected, name
for name, expected in peer_receipt['peer_subject_pins'].items():
    assert sha(X / name) == expected, name
for primary in peer_receipt['primary_versions']:
    assert sha(Path(primary['pdf'])) == primary['pdf_sha256']
    assert sha(Path(primary['text'])) == primary['text_sha256']
assert sha(Path(peer_receipt['source_path'])) == peer_receipt['source_sha256']
for name, expected in peer_receipt['event_anchor'].items():
    assert sha(X / name) == expected
for name in ('controls.py', 'CONTROL-RESULTS.json'):
    assert sha(HERE / 'selected-control-recheck' / name) == sha(SELECTED / name)
control = load(HERE / 'CONTROL-RESULTS.json')
assert sha(HERE / 'controls.py') == control['source_sha256']
assert control['two_nonce_full17_tuple_counter_separation']
kernel = load(X / 'root-message-hash/PROJECTION-CHECK.json')
assert kernel['exit_code'] == 0 and kernel['checked_declarations'] == 3
assert kernel['new_source_game_checked_declarations'] == 0
assert sha(X / 'root-message-hash/DigestProjection.lean') == kernel['source_sha256']
assert sha(X / 'root-message-hash/DigestProjection.log') == kernel['log_sha256']
assert all(set(a) == {'propext', 'Quot.sound'} for a in kernel['axiom_sets'])
assert (HERE / 'DigestProjection-recheck.log').read_text(encoding='utf-8') == (X / 'root-message-hash/DigestProjection.log').read_text(encoding='utf-8')
result = {
    'verdict': 'ACCEPT_MANUAL_CONDITIONAL_REGISTERED_CONTEXT_CTAC_COVERAGE_ADAPTER_PRIMARY_ITSR_TRANSFER_OPEN',
    'own_first_saved_before_new_peer_proposal': True,
    'own_subject_pins': {p: sha(HERE / p) for p in ['INDEPENDENT-FIRST.md', 'CLARIFICATION.md', 'EVENT-BINDING.md', 'PEER-REVIEW.md', 'controls.py', 'CONTROL-RESULTS.json']},
    'peer_subject_pins': { 'selected-promotion-review/message-hash-identification/' + p: h for p, h in peer_receipt['files'].items() },
    'peer_review_receipt_sha256': sha(SELECTED / 'REVIEW-RECEIPT.json'),
    'primary_versions': peer_receipt['primary_versions'],
    'source_sha256': peer_receipt['source_sha256'],
    'event_anchor': peer_receipt['event_anchor'],
    'event': 'Win AND indexed C_cov:17 real tuples at one final route, exposed by completed honest responses across restored branches',
    'conditional_inequality': 'Pr_SrcFJideal_h[Win AND C_cov] <= Succ_RC_CTAC_SR_h(B_cov)',
    'control_execution': {
        'own_controls_exit_code': 0,
        'peer_controls_reexecuted_exit_code': 0,
        'peer_reexecution_byte_identical_results': True,
        'own_control_results_sha256': sha(HERE / 'CONTROL-RESULTS.json'),
        'peer_copied_source_sha256': sha(HERE / 'selected-control-recheck/controls.py'),
        'peer_reexecution_results_sha256': sha(HERE / 'selected-control-recheck/CONTROL-RESULTS.json'),
    },
    'projection_helper_pins': {
        'root-message-hash/DigestProjection.lean': kernel['source_sha256'],
        'root-message-hash/DigestProjection.log': kernel['log_sha256'],
        'root-message-hash/PROJECTION-CHECK.json': sha(X / 'root-message-hash/PROJECTION-CHECK.json'),
        'outside-field-check/message-hash-identification/DigestProjection-recheck.log': sha(HERE / 'DigestProjection-recheck.log'),
    },
    'projection_helper_independent_reexecution': {
        'command': kernel['command'], 'exit_code': 0, 'checked_declarations': 3,
        'axiom_sets': kernel['axiom_sets'],
        'scope': 'Same-word prefix and bit slices only; no two-stage hash-prefix identity, SHA assumption, source/game/security refinement.',
    },
    'checks': {
        'primary_nonce_return_and_versions_explicit': True,
        'full256_same_h_two_stage_literal_frames': True,
        'real17_indices_filter153_to161_route162_to202': True,
        'memoized_classical_J_first_label_caching': True,
        'source_joint_S_root_F_retained_no_uniform_root_replacement': True,
        'retained_F_not_advice_or_extra_oracle_to_A': True,
        'logical_context_tags_decoded_away_from_source_hash_bytes': True,
        'lifted_route_parameters_not_source41_RO_numerics': True,
        'prekey_source_chronology_quantum_continuation': True,
        'canonical_target_arbitrary_valid_final_counter_gap': True,
        'Win_freshness_and_indexed_Ccov_from_completed_responses': True,
        'separate_H_G_public_graph_events_not_bounded_here': True,
        'no_commit_needed_under_absorbing_partiality': True,
        'finite_bottom_unnormalized_no_extra_seedzero_charge': True,
        'honest_local_and_challenger_hash_runtime_bytes_circuits_charged': True,
        'no_uniform_lowerbits_or_HJ_h_equals_HJ_O': True,
        'own_and_peer_finite_controls_passed': True,
        'three_projection_helpers_only_bit_function_facts': True,
    },
    'ordinary_primary_ITSR_quantitative_or_exact_transfer': 'OPEN',
    'named_CTAC_property_hardness': 'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
    'new_supporting_projection_declarations_reviewed': 3,
    'potential_cumulative_supporting_declarations_if_promoted': 47,
    'new_source_game_security_checked_declarations': 0,
    'fixed_h_full_security_category_capacity': 'not established',
    'root_source_manuscript_core_numeric_or_prior_receipt_edits': 0,
    'whole_goal_complete': False,
    'review_builder_sha256': sha(Path(__file__)),
}
out = HERE / 'REVIEW.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'verdict': result['verdict'], 'manual_sha256': sha(HERE / 'PEER-REVIEW.md'), 'receipt_sha256': sha(out)}, indent=2))

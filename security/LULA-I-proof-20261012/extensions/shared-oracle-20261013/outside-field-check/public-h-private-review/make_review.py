import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parents[1]
AUTHOR = X / 'chain-pre-adapter/public-h-private'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
provenance = load(AUTHOR / 'SUCCESSOR-PROVENANCE.json')
assert provenance['own_control_exit'] == 0 and provenance['original_pins_preserved']
for name, expected in provenance['files'].items():
    assert sha(AUTHOR / name) == expected, name
for name in ('control.py', 'control-successor.py', 'CONTROL-RESULTS.json', 'CONTROL-SUCCESSOR-RESULTS.json'):
    assert sha(HERE / 'peer-recheck' / name) == sha(AUTHOR / name), name
first = sha(HERE / 'INDEPENDENT-FIRST.md')
assert first == 'ce1595126df47f472fed0a7a1489840f1fabbc4e8490604e73baeaa397014cca'
source = X.parents[3] / 'publications/LULA-I/release/code/lula1/src/lib.rs'
assert sha(source) == 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
counts = X / 'PRIVATE-REDUCTION-PROGRAMS.md'
assert sha(counts) == 'feff3d899edcb0b675970eaf915c221d837a47ab7357828758f0f0a40c923f89'
literal = load(HERE / 'LITERAL-GAP-CONTROLS.json')
assert literal['source_sha256'] == sha(HERE / 'literal_and_gap_controls.py')
assert literal['zero_seed_zero_p_literal_f_g_aliases'] == 4
result = {
    'verdict': 'ACCEPT_EXACT_ORDINARY_PUBLIC_PARAMETER_PRIVATE_PRF_ADAPTER_IDENTITIES_WITH_CHARGED_SOURCE_RELATIVE_RESOURCES',
    'own_first_saved_before_peer_files_and_controls': True,
    'first_derivation_sha256': first,
    'source_sha256': sha(source),
    'inherited_counts_sha256': sha(counts),
    'subject_pins': {'chain-pre-adapter/public-h-private/' + n: h for n, h in provenance['files'].items()},
    'successor_provenance_sha256': sha(AUTHOR / 'SUCCESSOR-PROVENANCE.json'),
    'manual_review_sha256': sha(HERE / 'REVIEW.md'),
    'review_builder_sha256': sha(Path(__file__)),
    'own_control_pins': {
        'literal_and_gap_controls.py': sha(HERE / 'literal_and_gap_controls.py'),
        'LITERAL-GAP-CONTROLS.json': sha(HERE / 'LITERAL-GAP-CONTROLS.json'),
        'peer-recheck/control.py': sha(HERE / 'peer-recheck/control.py'),
        'peer-recheck/control-successor.py': sha(HERE / 'peer-recheck/control-successor.py'),
        'peer-recheck/CONTROL-RESULTS.json': sha(HERE / 'peer-recheck/CONTROL-RESULTS.json'),
        'peer-recheck/CONTROL-SUCCESSOR-RESULTS.json': sha(HERE / 'peer-recheck/CONTROL-SUCCESSOR-RESULTS.json'),
    },
    'control_exits': {'peer_original_reexecution': 0, 'peer_successor_reexecution': 0, 'own_literal_and_gap': 0},
    'checks': {
        'exact_128bit_private_f_g_with_same_full256_public_h': True,
        'ordinary_public_parameter_game_explicitly_named': True,
        'pointwise_S_signed_identity_and_correct_averaging': True,
        'particular_absolute_gap_equals_particular_advantage': True,
        'supremum_insecurity_upperbound_not_particular_equality': True,
        'total_triangle_inequality_not_equality': True,
        'prekey_quantum_continuation_and_S_withheld_from_A': True,
        'all_private_calls_intercepted_unknown_seed_unreachable': True,
        'classical_private_queries_quantum_public_computation': True,
        'literal_aliases_including_S0_retained': True,
        'no_new_zero_seed_charge_in_private_identity': True,
        'persistent_F_J_and_freshness_across_restoration': True,
        'source_parser_and_root_equality_final_verification': True,
        'matched_absorbing_partial_service_bottom': True,
        'actual_toy_bottom_successor_cases': True,
        'source_loop_private_label_caps_rederived': True,
        'public_call_ledger_inherited_not_reaudited_in_full': True,
        'honest_hash_bytes_time_storage_and_quantum_circuit_costs_charged': True,
        'private_challenger_execution_separately_charged_for_total_work': True,
        'no_external_raw_oracle_or_RO_numeric_transplant': True,
        'private_prefix_prfs_do_not_certify_full_H_msg_lower128_or_route_distribution': True,
        'prefix_preserving_lower128_zero_countermodel_checked': True,
    },
    'scope': 'Manual exact ordinary fixed-public-h private adapters, conditional on family insecurity. Finite controls are serialization/game-interface discriminators only.',
    'family_hardness': 'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
    'fixed_h_public_component_full_forgery_bound': 'OPEN',
    'fixed_h_full_H_msg_adaptive_coverage_public_graph_lemma': 'OPEN',
    'external_RO_or_QROM_numerical_transfer': False,
    'new_kernel_declarations': 0,
    'source_game_checked_declarations': 0,
    'category_capacity': 'not established',
    'whole_goal_complete': False,
    'source_manuscript_global_or_prior_receipt_edits': 0,
}
out = HERE / 'REVIEW.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'verdict': result['verdict'], 'review_sha256': result['manual_review_sha256'], 'receipt_sha256': sha(out)}, indent=2))

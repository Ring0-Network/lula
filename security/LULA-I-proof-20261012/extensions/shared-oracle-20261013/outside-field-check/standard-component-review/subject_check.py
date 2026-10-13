import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
author_path = X / 'selected-promotion-review/standard-identification/PROVENANCE.json'
author = load(author_path)
pins = {}
for name, expected in author['files'].items():
    path = X / 'selected-promotion-review/standard-identification' / name
    assert sha(path) == expected, name
    pins['selected-promotion-review/standard-identification/' + name] = expected
for name, expected in author['peer_review_pins'].items():
    assert sha(X / name) == expected, name
    pins[name] = expected
for entry in author['primary_files']:
    assert sha(Path(entry['pdf'])) == entry['pdf_sha256']
    assert sha(Path(entry['cached_text'])) == entry['cached_text_sha256']
for name, expected in author['preserved_core_artifacts'].items():
    assert sha(X / name) == expected, name
kernel_path = X / 'root-keyed-review/COUNTER-POLICY-CHECK.json'
kernel = load(kernel_path)
assert kernel['exit_code'] == 0 and kernel['checked_declarations'] == 4
assert kernel['custom_axioms'] == kernel['admissions'] == kernel['source_security_checked_declarations'] == 0
assert sha(X / 'root-keyed-review/CounterPolicy.lean') == kernel['source_sha256']
assert sha(X / 'root-keyed-review/CounterPolicy.log') == kernel['log_sha256']
expected_axioms = {
    'LulaCounterPolicy.both_policies_accepted': ['propext'],
    'LulaCounterPolicy.canonical_policy_collision': [],
    'LulaCounterPolicy.later_policy_no_changed_base_collision': ['propext'],
    'LulaCounterPolicy.no_finite_factor_from_zero_success': ['propext'],
}
assert kernel['axioms'] == expected_axioms
assert (HERE / 'CounterPolicy-recheck.log').read_text(encoding='utf-8') == (X / 'root-keyed-review/CounterPolicy.log').read_text(encoding='utf-8')
result = {
    'verdict': 'ACCEPT_MANUAL_CONDITIONAL_FIXED_PUBLIC_HASH_CANONICAL_COLLECTION_COMPONENT',
    'current_index_review': False,
    'subject_pins': pins,
    'author_provenance_sha256': sha(author_path),
    'source_sha256': author['source_sha256'],
    'primary_files': author['primary_files'],
    'inherited_preserved_core_artifacts': author['preserved_core_artifacts'],
    'prior_outside_integration_sha256': sha(X / 'outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json'),
    'manual_review_sha256': sha(HERE / 'SUBJECT-REVIEW.md'),
    'checker_sha256': sha(Path(__file__)),
    'kernel_pins': {
        'root-keyed-review/CounterPolicy.lean': kernel['source_sha256'],
        'root-keyed-review/CounterPolicy.log': kernel['log_sha256'],
        'root-keyed-review/COUNTER-POLICY-CHECK.json': sha(kernel_path),
        'outside-field-check/standard-component-review/CounterPolicy-recheck.log': sha(HERE / 'CounterPolicy-recheck.log'),
    },
    'independent_kernel_reexecution': {'exit_code': 0, 'toolchain': kernel['toolchain'], 'command': kernel['command'], 'axioms': expected_axioms},
    'checks': {
        'canonical_first_legal_specialization_no_forall_policy_gate': True,
        'r_security_parameter_construction_choice': True,
        'hidden_parameter_other_tweak_child_computation': True,
        'genuine_child_public_types0_to4_disjoint_type7': True,
        'fixed_public_hash_prekey_may_start_after_parameter_release_withheld_from_a': True,
        'lower42_top21_fixed_predicate_split': True,
        'unconditioned_nonzero_event_no_eta_denominator': True,
        'bottom_local_failure_not_global_normalization': True,
        'same_full_public_hash_lower_limb_computation': True,
        'external_global_raw_qrom_is_distinct_interface': True,
        'all_honest_work_and_primitive_preprocessing_charged': True,
        'hk_generic_collection_bounds_are_conjecture_not_proved': True,
        'four_helpers_only_synthetic_policy_countermodel': True,
        'new_restricted_qrom_candidates_not_reviewed_or_relied_upon': True,
    },
    'new_supporting_checked_declarations': 4,
    'potential_cumulative_supporting_checked_declarations': 44,
    'new_source_game_security_checked_declarations': 0,
    'quantitative_c1_bounds': 'OPEN',
    'HJ_fixed_hash_equals_HJ_random_oracle': 'not asserted',
    'fixed_sha_hardness': 'not established',
    'category_capacity': 'not established',
    'whole_goal_complete': False,
}
out = HERE / 'SUBJECT-REVIEW.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'verdict': result['verdict'], 'receipt_sha256': sha(out), 'manual_sha256': result['manual_review_sha256']}, indent=2))

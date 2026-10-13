import hashlib
import json
from pathlib import Path

here = Path(__file__).resolve().parent
base = here.parent
subjects = [
    'chain-pre-independent/outside-simulator/INDEPENDENT-DERIVATION.md',
    'chain-pre-independent/outside-simulator/CLARIFICATION.md',
    'chain-pre-independent/outside-simulator/ROUTES-CLARIFICATION.md',
    'chain-pre-adapter/outside-simulator/INDEPENDENT-DERIVATION.md',
]
premises = [
    'PRIVATE-REDUCTION-PROGRAMS.md',
    'selected-promotion-review/QPRE-FINAL-REVIEW.json',
    'selected-promotion-review/T7-REVIEW.json',
]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
result = {
    'verdict': 'ACCEPT_SCOPED_MANUAL_BOUNDED_QUERY_CONSTRUCTION_AND_B_ONLY_REPLACEMENT',
    'first_independent_derivation_saved_before_peer_reads': True,
    'first_independent_derivation_sha256': sha(here / 'first-independent-derivation.md'),
    'subject_pins': {p: sha(base / p) for p in subjects},
    'inherited_premise_pins': {p: sha(base / p) for p in premises},
    'source_binding_in_inherited_registry': 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210',
    'source_counts_independently_rederived_in_this_review': False,
    'review_sha256': sha(here / 'SECOND-READER.md'),
    'control_source_sha256': sha(here / 'toy_controls.py'),
    'control_results_sha256': sha(here / 'toy-results.json'),
    'control_exit_code': 0,
    'manual_acceptance': {
        'finite_injective_length_sensitive_encoding': True,
        'matched_invalid_state_extension_required': True,
        'deterministic_trace_one_tower_all_power_of_two_degrees': True,
        'four_recursive_products_quadratic_bit_gate_cost': True,
        'optional_conjugate_modulus_quartic_deterministic_bit_cost': True,
        'full_256_bit_uniform_projection': True,
        'clean_reversible_horner_evaluation': True,
        'all_honest_and_adversary_outside_calls_counted': True,
        'static_worst_case_domain_and_query_bounds_required': True,
        'coefficients_hidden_and_reused_for_every_eval': True,
        'b_only_success_equality_under_inherited_caps': True,
        'row_conditioning_on_independent_full_row_not_rf_derived_y': True,
        'no_nonsaturated_full_rf_law_claim': True,
        'explicit_gate_list_generation_charged_if_used': True,
    },
    'inherited_caps': {
        'H_setup': '2^21*(19505+2^32)-1',
        'H_hot': '82090+5*2^32',
        'H_cold': '8560574463+82090+6*2^32',
        'T_PRE': 'Q+H_setup+q*H_mode+3224+254',
        'T_ROW': 'Q+H_setup+q*H_mode+3224+17392',
        'row_preprocessing_external_challenge_not_outside_eval': 'at most 2^32 calls; separately charged',
    },
    'optional_comparator_scope': 'Conditionally valid compiled algorithm; terminal classifier source reachability/count completeness not independently audited here; unnecessary for B-only acceptance.',
    'toy_results': json.loads((here / 'toy-results.json').read_text(encoding='utf-8')),
    'limitations': [
        'No new whole-source or arbitrary-degree kernel checked declarations.',
        'No actual quantum runtime or production implementation benchmark.',
        'Conventional keyed PRE/PRF/TCR and fixed SHA identification remain open.',
        'Category and q_max certification do not follow.',
        'Physical termination and source implementation refinement remain separate.',
    ],
    'outside_authorized_folder_writes': False,
}
out = here / 'SECOND-READER.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'review_sha256': result['review_sha256'], 'receipt_sha256': sha(out), 'receipt': str(out)}, indent=2))

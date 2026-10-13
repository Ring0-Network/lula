"""Pin scoped manual reviews and check copied finite controls; own-folder writes only."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PEER = ROOT / 'selected-promotion-review' / 'message-hash-identification'
SOURCE = ROOT.parents[4] / 'publications' / 'LULA-I' / 'release' / 'code' / 'lula1' / 'src' / 'lib.rs'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def pins(base, names):
    return {name: digest(base / name) for name in names}

assert digest(HERE / 'PROBABILISTIC-LIFT-FIRST.md') == 'c558399bc390589efddc4176bf45a90be0df04562e5e7395798108878d4c08c8'
assert digest(PEER / 'COUNTER-GUESS-LIFT.md') == '9c1fadb8eedc8dbf19f20800a0950836433c00f0782297d9f315fca0328433ca'
assert digest(ROOT / 'MESSAGE-HASH-PRIMITIVE-COMPONENT.md') == '1406428b0f8ab96e0b5aa923a372c0773067fbc4d79f0f6c2065fd17edfb0dff'
source_path = Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert digest(source_path) == 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
prior = json.loads((HERE / 'REVIEW.json').read_text(encoding='utf-8'))
for version in prior['primary_versions']:
    assert digest(Path(version['pdf'])) == version['pdf_sha256']
    assert digest(Path(version['text'])) == version['text_sha256']
for name in ('counter_guess_controls.py', 'compare_lift_controls.py', 'COUNTER-GUESS-LIFT.md', 'COUNTER-GUESS-INPUT-COMPLETION.md', 'COUNTER-GUESS-CONTROLS.json', 'LIFT-COMPARISON-CONTROLS.json'):
    assert digest(HERE / 'counter-guess-peer-recheck' / name) == digest(PEER / name)
assert digest(PEER / 'PROBABILISTIC-LIFT-PEER-REVIEW.md') == 'c43480c9504cd91d603a65cc4098cb6143b0397178463261715e17727d959568'
assert digest(PEER / 'PROBABILISTIC-LIFT-REVIEW.json') == 'b3633fdc195e13bc39b914f31fb95e635900d2e963d0dddc15465c3f8d602b78'

review = {
    'verdict': 'ACCEPT_MANUAL_LAWFUL_ONE_SIDED_PRIMARY_FREE_COUNTER_ITSR_LIFT_HARDNESS_UNEVALUATED',
    'own_new_first_saved_before_any_new_selected_probabilistic_lift_proposal_read': True,
    'own_folder': str(HERE),
    'own_pins': pins(HERE, ['PROBABILISTIC-LIFT-FIRST.md', 'PROBABILISTIC-LIFT-REVIEW.md', 'probabilistic_lift_controls.py', 'PROBABILISTIC-LIFT-CONTROLS.json', 'INDEPENDENT-FIRST.md', 'CLARIFICATION.md', 'EVENT-BINDING.md', 'REVIEW.json']),
    'selected_pins': pins(PEER, ['COUNTER-GUESS-LIFT.md', 'COUNTER-GUESS-INPUT-COMPLETION.md', 'COUNTER-GUESS-MAP-CLARIFICATION.md', 'COUNTER-GUESS-SOURCE-ROUTE.md', 'counter_guess_controls.py', 'COUNTER-GUESS-CONTROLS.json', 'compare_lift_controls.py', 'LIFT-COMPARISON-CONTROLS.json', 'PROBABILISTIC-LIFT-PEER-REVIEW.md', 'PROBABILISTIC-LIFT-REVIEW.json']),
    'source': {'path': str(source_path), 'sha256': digest(source_path)},
    'primary_versions_rechecked': prior['primary_versions'],
    'event_anchor': pins(ROOT, ['CHANGED-CHILD-EXTRACTION.md']),
    'source_event': 'Win AND indexed C_cov:17 real tuple coordinates covered at one final route by completed honest responses, final message fresh among all initiated requests',
    'precise_family': 'Public SAME fixed h; total free-counter logical chosen-context H_free with key R128 sampled uniformly after chosen Enc(S,Z,M,c); virtual route297 includes chosen256 context bits plus actual41 route bits, followed by17*9 real indices; exact invalid-code completion part of family',
    'all_label_nonabort': {
        'target_queries': 'q_distinct<=q initiated classical source signing requests',
        'loss': 'L^k, L=2^32 and k=min(17,q); L^17=2^544',
        'inequality': 'Pr_SrcFJideal_h[Win AND C_cov] <= min(1,L^k Succ_primary_ITSR_Hfree(B_all))',
        'q0': 'Coverage event impossible; no need to invoke empty witness',
        'source_view': 'Exact full source channel independent of guesses; ignore primary guessed mapped data for ALL source-facing decisions and responses',
        'matching_event': 'Only deterministic completed coverage-witness messages (d<=k) need match, with conditional probability L^-d; wrong nonwitness targets enlarge ledger',
        'canonical_guess_abort': False,
    },
    'own_full_abort_alternative': {'loss': 'L^q', 'targets': 'q_distinct<=q', 'source_view': 'Faithful matched source prefixes only; artificial guess abort separate from natural source bottom'},
    'own_sparse_alternative': {'loss': '(Q*L)^k, Q=least power2>=q and k=min(17,q)', 'targets': '<=k', 'selectors': 'Duplicates and unrealized ordinal slots retained; padded deterministic witness vector has probability Q^-k, no rejection normalization'},
    'resource_scope': 'ALL actual setup/FORS/WOTS/canonical-search/final work, bytes, private F and nonce dictionaries, cache and quantum public-h circuits charged. Primary target: one inner and one outer hash plus total parsing/map; challenger costs separately charged. No finite polynomial/practical timing guarantee for native partial source claimed.',
    'checks': {
        'full256_inner_and_outer_same_literal_h': True,
        'primary_oracle_returns_uniform_R_and_G_after_chosen_input': True,
        'quantum_continuation_classical_target_signing_services': True,
        'memoized_R_on_repeats_and_all_source_branches': True,
        'actual_source_S_root_F_joint_distribution_retained': True,
        'consistent_private_F_retained_not_advice_to_A': True,
        'public_h_all_local_queries_including_prekey_chronology': True,
        'logical_tags_decoded_no_source_hash_byte_changes': True,
        'final_fresh_M_implies_fresh_primitive_input_even_nonce_collision': True,
        'natural_bottom_mass_unnormalized_no_resampling': True,
        'literal_S0_aliases_preserved_no_extra_seedzero_charge': True,
        'source17_exposure_Ccov_not_H_G_graph_events': True,
        'canonical_Hcan_countermodel_preserved_different_family': True,
        'no_false_uniform297_route_entropy': True,
        'no_old_RO_scalar_or_private_prefix_hardness_transfer': True,
        'no_HJ_h_equals_HJ_O_identity': True,
    },
    'own_control_execution': {'exit_code': 0, 'worlds': 4624, 'scope': 'Exact toy17-coordinate adaptive metadata/coverage probabilities, not source signature/SHA/quantum kernel/security run'},
    'peer_control_independent_reexecution': {
        'copied_sources_and_results': pins(HERE / 'counter-guess-peer-recheck', ['counter_guess_controls.py', 'COUNTER-GUESS-CONTROLS.json', 'compare_lift_controls.py', 'LIFT-COMPARISON-CONTROLS.json', 'COUNTER-GUESS-LIFT.md', 'COUNTER-GUESS-INPUT-COMPLETION.md']),
        'both_exit_codes': [0, 0],
        'results_byte_identical_to_peer': True,
        'algebra_cases': 60,
        'adaptive_history_witness_cases': 54,
        'completion_masses_unnormalized': ['3/4', '11/16', '43/64', '171/256'],
    },
    'optional18_variant': 'Accepted manual bookkeeping only: filter forces virtual coordinate18=0 for final candidate and matched witnesses at same I; nonempty<=17 witness collection already covers it, so no extra message/counter guess/query/secret exposure. Tagged width459 is a different precisely specified map; no extra entropy or hardness.',
    'actual_free_counter_family_hardness': 'NOT_ESTABLISHED; exact family/adversary resource insecurity remains an additional assumption',
    'quantitative_adequacy_fixed_h_full_security_category_capacity': 'NOT_ESTABLISHED',
    'new_source_game_security_kernel_declarations': 0,
    'source_manuscript_scalar_root_index_prior_receipt_edits': 0,
    'whole_goal_complete': False,
    'builder_sha256': digest(Path(__file__)),
}
(HERE / 'PROBABILISTIC-LIFT-REVIEW.json').write_text(json.dumps(review, indent=2) + '\n', encoding='utf-8')

component = {
    'verdict': 'ACCEPT_FAITHFUL_DIRECT_NAMED_MESSAGE_HASH_COVERAGE_COMPONENT',
    'scope': 'Actual root direct-property subject only; no current-index/promotion receipt',
    'subject': {'path': str(ROOT / 'MESSAGE-HASH-PRIMITIVE-COMPONENT.md'), 'sha256': digest(ROOT / 'MESSAGE-HASH-PRIMITIVE-COMPONENT.md')},
    'review_md_sha256': digest(HERE / 'FINAL-COMPONENT-REVIEW.md'),
    'accepted_direct_review_receipt': {'path': str(HERE / 'REVIEW.json'), 'sha256': digest(HERE / 'REVIEW.json')},
    'own_first_and_clarification_pins': pins(HERE, ['INDEPENDENT-FIRST.md', 'CLARIFICATION.md', 'EVENT-BINDING.md']),
    'peer_first_and_clarification_pins': pins(PEER, ['INDEPENDENT-FIRST.md', 'CONTEXT-LIFT-CLARIFICATION.md', 'REVIEW-CLARIFICATION.md', 'REVIEW-RECEIPT.json']),
    'source_sha256': digest(source_path),
    'event_anchor': pins(ROOT, ['CHANGED-CHILD-EXTRACTION.md']),
    'conditional_inequality': 'Pr_SrcFJideal_h[Win AND indexed C_cov] <= Succ_RC_CTAC_SR_h(B_cov)',
    'faithfulness_checks': {
        'full256_same_h_two_literal_stages_17_filter9_route41': True,
        'prekey_quantum_continuation_source_parameter_release': True,
        'consistent_F_actual_S_root_correlation_and_memoized_J': True,
        'logical_tags_no_source_h_word_change': True,
        'fresh_Win_event_and_completed_response_coordinate_exposure': True,
        'early_primitive_target_superset_no_Commit_required': True,
        'absorbing_bottom_no_normalization_and_all_S0_aliases': True,
        'all_source_challenger_local_bytes_circuit_storage_costs_charged': True,
        'canonical_primary_interface_separator_is_family_specific': True,
        'no_H_G_graph_event_or_lowerbit_uniformity_inference': True,
        'no_free_counter_ordinary_lossylift_claimed_in_this_prior_component': True,
        'no_fixed_h_numeric_security_or_RO_scalar_transfer': True,
    },
    'correction_required_for_stated_subject_scope': False,
    'projection_helpers': 'Three separately reviewed same-word-only bit identities; not source/game/security theorem',
    'later_lossy_primary_Hfree_route': 'Separate accepted manual successor program; not part of subject140642 and does not negate canonical Hcan separation',
    'new_source_game_security_kernel_declarations': 0,
    'source_manuscript_scalar_index_prior_receipt_edits': 0,
    'fixed_h_full_security_category_capacity': 'NOT_ESTABLISHED',
    'builder_sha256': digest(Path(__file__)),
}
(HERE / 'FINAL-COMPONENT-REVIEW.json').write_text(json.dumps(component, indent=2) + '\n', encoding='utf-8')
for name in ['PROBABILISTIC-LIFT-REVIEW.md', 'PROBABILISTIC-LIFT-REVIEW.json', 'PROBABILISTIC-LIFT-CONTROLS.json', 'FINAL-COMPONENT-REVIEW.md', 'FINAL-COMPONENT-REVIEW.json']:
    print(name, digest(HERE / name))

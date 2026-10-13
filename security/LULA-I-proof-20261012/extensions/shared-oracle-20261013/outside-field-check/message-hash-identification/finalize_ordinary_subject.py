"""Subject-only immutable pins for the final root ordinary-lift artifact."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PEER = ROOT / 'selected-promotion-review' / 'message-hash-identification'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def pins(base, names):
    return {name: digest(base / name) for name in names}

subject = ROOT / 'MESSAGE-HASH-ORDINARY-LIFT.md'
assert digest(subject) == '72a398e9a2d991b83de02c7982eae1ca6bdbb4c59d684b86094865ff03ef04cc'
assert digest(HERE / 'PROBABILISTIC-LIFT-REVIEW.json') == '7bed93dfadde9b5f9cd0b06e7f27bde91f27297d1ba2787b39cd1254c5771573'
assert digest(ROOT / 'MESSAGE-HASH-PRIMITIVE-COMPONENT.md') == '1406428b0f8ab96e0b5aa923a372c0773067fbc4d79f0f6c2065fd17edfb0dff'
prior = json.loads((HERE / 'PROBABILISTIC-LIFT-REVIEW.json').read_text(encoding='utf-8'))
assert digest(Path(prior['source']['path'])) == prior['source']['sha256']
for version in prior['primary_versions_rechecked']:
    assert digest(Path(version['pdf'])) == version['pdf_sha256']
    assert digest(Path(version['text'])) == version['text_sha256']
receipt = {
    'verdict': 'ACCEPT_FAITHFUL_MANUAL_ORDINARY_ITSR_LOSS_AWARE_COMPONENT',
    'scope': 'Actual final root ordinary-lift subject only; not a current-index/promotion/source-security receipt',
    'subject': {'path': str(subject), 'sha256': digest(subject)},
    'review_md_sha256': digest(HERE / 'FINAL-ORDINARY-SUBJECT-REVIEW.md'),
    'own_pins': pins(HERE, ['PROBABILISTIC-LIFT-FIRST.md', 'PROBABILISTIC-LIFT-REVIEW.md', 'PROBABILISTIC-LIFT-REVIEW.json', 'probabilistic_lift_controls.py', 'PROBABILISTIC-LIFT-CONTROLS.json', 'FINAL-COMPONENT-REVIEW.json', 'REVIEW.json']),
    'peer_pins': pins(PEER, ['COUNTER-GUESS-LIFT.md', 'COUNTER-GUESS-INPUT-COMPLETION.md', 'COUNTER-GUESS-MAP-CLARIFICATION.md', 'COUNTER-GUESS-SOURCE-ROUTE.md', 'PROBABILISTIC-LIFT-PEER-REVIEW.md', 'PROBABILISTIC-LIFT-REVIEW.json']),
    'unchanged_direct_root_component': pins(ROOT, ['MESSAGE-HASH-PRIMITIVE-COMPONENT.md']),
    'source': prior['source'],
    'primary_versions_rechecked': prior['primary_versions_rechecked'],
    'event_anchor': pins(ROOT, ['CHANGED-CHILD-EXTRACTION.md']),
    'total_instance': {
        'input_bits': '8b+289: S128||Z128||c32||rank_(8b+1)',
        'b': 'Ex-ante ceiling for every source message in every execution, including final candidates',
        'rank': 'E(M)=sum_(j<|M|)256^j+BE_integer(M)',
        'all_input_bitstrings_decode': True,
        'max_decoded_message_bytes': 'b+1',
        'source_encodings_exact': True,
        'whole_family_insecurity_including_extra_decoded_members': True,
        'new_actual_hardness': False,
        'output_bits': '450: chosen-context route297 followed by17 real9-bit indices',
    },
    'dense': {'event': 'Win AND indexed C_cov from completed source responses', 'loss': 'L^k with L=2^32, k=min(17,q)', 'primary_target_cap': 'q_distinct<=q', 'q0': 'source coverage impossible', 'source_channel': 'Exact guess-independent full source-facing quantum channel; no artificial guess abort', 'success_parameter': 'Particular B_dense success or applicable maximum at actual complete resources'},
    'sparse': {'loss': '(B_ord*L)^k', 'B_ord': '2^ceil(log2 max(1,q)), ordinal padding only', 'primary_target_cap': '<=k', 'source_channel': 'Faithful matched prefixes; artificial mismatch abort explicitly separate', 'success_parameter': 'Separate B_sparse success at its own complete resources'},
    'checks': {
        'nonce_uniform_ex_ante_distinct_from_fixed_tape_coupling': True,
        'guessed_target_G_never_used_for_source_feedback': True,
        'total_rank_definition_and_bplus1_costs_explicit': True,
        'full256_inner_and_outer_same_public_h_literal_words': True,
        'actual_source_F_root_setup_correlation_and_prekey_quantum_memory': True,
        'fresh_source_M_implies_primary_pair_fresh': True,
        'only17_real_indexed_completed_response_exposures': True,
        'source_bottom_unnormalized_all_S0_aliases_retained': True,
        'dense_kmin17q_and_q_targets_not_conflated': True,
        'sparse_Bord_not_raw_Q_query_budget': True,
        'virtual18_no_extra_witness_guess_secret_or_tree': True,
        'chosen_context297_label_no_random_entropy': True,
        'all_source_local_challenger_circuit_bytes_storage_costs_charged': True,
        'precise_family_hardness_not_inferred_from_SHA_name_or_RO': True,
        'old_Hcan_separation_and_direct_component_preserved': True,
        'no_generic_rejection_qL_bound': True,
    },
    'existing_control_evidence': {'own_worlds': 4624, 'peer_algebra_cases': 60, 'peer_adaptive_history_witness_cases': 54, 'both_peer_reexecution_exit_codes': [0, 0], 'peer_results_byte_identical': True, 'scope': 'Pinned in own7bed receipt; finite logical/probability controls only'},
    'projection_support': 'Three independently reexecuted same-word bit helpers pinned in own4d3ff receipt; not this source/game reduction',
    'correction_required_for_final_subject': False,
    'new_source_game_security_kernel_declarations': 0,
    'source_scalar_manuscript_root_index_prior_receipt_edits': 0,
    'actual_primitive_hardness_quantitative_adequacy_full_security_category_capacity': 'NOT_ESTABLISHED',
    'builder_sha256': digest(Path(__file__)),
}
(HERE / 'FINAL-ORDINARY-SUBJECT-REVIEW.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
for name in ('FINAL-ORDINARY-SUBJECT-REVIEW.md', 'FINAL-ORDINARY-SUBJECT-REVIEW.json'):
    print(name, digest(HERE / name))

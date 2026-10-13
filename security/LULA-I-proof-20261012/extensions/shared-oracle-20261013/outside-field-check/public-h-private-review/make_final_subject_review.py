import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
X = HERE.parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
review = load(HERE / 'REVIEW.json')
assert sha(HERE / 'REVIEW.json') == 'f38bf5e3d3650980fb34566a768779f27bb31e0d3aee245f5522c58c0077922f'
assert all(review['checks'].values())
for path, expected in review['subject_pins'].items():
    assert sha(X / path) == expected
for path, expected in review['own_control_pins'].items():
    assert sha(HERE / path) == expected
assert sha(HERE / 'INDEPENDENT-FIRST.md') == review['first_derivation_sha256']
assert sha(HERE / 'REVIEW.md') == review['manual_review_sha256']
artifact = X / 'PRIVATE-FIXED-H-REDUCTION.md'
assert sha(artifact) == 'a0bd91372f65af85521889c01d260f010ecb4af9d4da11392d21b3ebfc8b5e75'
text = artifact.read_text(encoding='utf-8')
for exact in [
    'D<=min(N_D,2181038080+q U_mode)',
    'The signed challenge gaps equal p0-p1 and p1-p2.',
    'not automatically E_S|p0(S)-p1(S)|',
    'no extra seed-zero term in these hops',
    'absorbing nonwinning output0',
    'Do not count the same private hash both as a local reduction call and a challenger call.',
    "h'(x)=prefix128 h(x)||zero128",
    'The earlier HJ[O] expressions cannot be silently used for HJ[h].',
]:
    assert exact in text, exact
result = {
    'verdict': 'ACCEPT_FAITHFUL_FINAL_FIXED_H_PRIVATE_PRF_ADAPTER_SUBJECT',
    'current_index_or_combined_promotion_review': False,
    'final_artifact': {'PRIVATE-FIXED-H-REDUCTION.md': sha(artifact)},
    'accepted_prior_review_sha256': sha(HERE / 'REVIEW.json'),
    'subject_pins': review['subject_pins'],
    'successor_provenance_sha256': review['successor_provenance_sha256'],
    'own_first_derivation_sha256': review['first_derivation_sha256'],
    'own_control_pins': review['own_control_pins'],
    'source_sha256': review['source_sha256'],
    'inherited_counts_sha256': review['inherited_counts_sha256'],
    'manual_final_review_sha256': sha(HERE / 'FINAL-SUBJECT-REVIEW.md'),
    'checker_sha256': sha(Path(__file__)),
    'checks': {
        'faithful_exact_f_g_same_full_public_h_128bit_private': True,
        'signed_absolute_particular_advantage_triangle_conventions_match': True,
        'public_S_signed_averaging_correct': True,
        'prekey_S_withheld_and_quantum_continuation_retained': True,
        'all_zero_seed_literal_aliases_no_new_zero_charge': True,
        'classical_private_quantum_public_interface': True,
        'matched_absorbing_partial_services_no_native_claim': True,
        'exact_D_cap_no_extra_plus1_needed': True,
        'source_private_loops_rederived_public_namespace_ledger_inherited': True,
        'private_challenger_vs_B_runtime_costs_separate': True,
        'prefix_lower_limb_countermodel_and_OPEN_full_H_msg_graph_lemma': True,
        'no_HJ_h_equals_HJ_O_or_RO_numeric_transplant': True,
        'no_hardness_category_or_capacity_certificate': True,
    },
    'new_kernel_declarations': 0,
    'new_checked_source_game_declarations': 0,
    'private_family_hardness': 'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
    'full_H_msg_adaptive_coverage_and_public_graph': 'OPEN',
    'fixed_h_full_forgery_bound': 'OPEN',
    'whole_goal_complete': False,
    'root_source_manuscript_index_or_prior_receipt_edits': 0,
}
out = HERE / 'FINAL-SUBJECT-REVIEW.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'verdict': result['verdict'], 'manual_sha256': result['manual_final_review_sha256'], 'receipt_sha256': sha(out)}, indent=2))

"""Pin-check the manually read selected-graph promotion and successor index."""
from pathlib import Path
import hashlib
import json

X = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
promotion = read(X / 'SELECTED-GRAPH-PROMOTION.json')
subject = read(OUT / 'SUBJECT-RECEIPT.json')
old = read(X / 'cache-payload-source/INTEGRATION-FINAL-REVIEW.json')

for group in ('subject_pins', 'current_documents', 'new_artifacts', 'preserved_scalar_artifacts'):
    for n, h in promotion[group].items():
        assert sha(X / n) == h, (group, n)
for n, h in subject['subject_pins'].items():
    assert sha(X / n) == h, n
for n, h in old['documents'].items():
    assert sha(X / 'root-docs-before-selected-graph' / n) == h, n
    assert promotion['prior_documents'][n] == h, n
for group in ('promoted_artifacts', 'prior_review_receipts'):
    for n, h in old[group].items():
        assert sha(X / n) == h, (group, n)
assert sha(X / 'PAYLOAD-PRIVATE-CURRENT-INDEX.json') == old['current_index_sha256']
assert sha(X / 'PAYLOAD-PRIVATE-PROMOTION.json') == old['preserved_promotion_sha256']
assert promotion['initial_promotion_subject_review_sha256'] == sha(OUT / 'SUBJECT-RECEIPT.json')
assert promotion['resource_review_receipt_sha256'] == sha(X / 'selected-graph-resources/REVIEW-RECEIPT.json')

g = (X / 'SELECTED-GRAPH-REDUCTION.md').read_text(encoding='utf8')
d7 = (X / 'CHANGED-CHILD-EXTRACTION.md').read_text(encoding='utf8')
for n in (X / 'selected-graph-challenge/LOCALIZED-FINAL-SUCCESSOR.md',):
    local = n.read_text(encoding='utf8')
    for before, after in promotion['localized_scope_repairs']:
        assert local.count(before) == 1, before
        local = local.replace(before, after)
    assert local.strip() in g, 'exact repaired localized subject inclusion'
correction = (X / 'selected-graph-challenge/LOCALIZED-SEED-SCOPE-CLARIFICATION.md').read_text(encoding='utf8')
assert correction.strip() in g
assert '`Pr[B_local wins] = 2^-56 * Pr[source Win AND G_final]`' not in g
assert '`Pr[B_cond wins] = 2^-56 * Pr[source Win AND G_final | S != 0]`' in g
assert '`Q_H + 2q + 4`' in g
assert 'their sum is2Q_q, not Q_q' in g
assert 'single1/N S=0 term is paid once' in g
assert 'honestly exposed WOTS address A with a successful canonical row' in d7
assert '`D7_base subset D7_full`' in d7
assert 'No standard S-TCR reduction or security-category claim' in d7

Ntop = 2**21
pc = Ntop * (16*255+1) + Ntop-2
pe = pc+1 + 4*(32*(32*15+1)+31) + 17*(512+511)+1
vc = Ntop*16
ve = vc + 4*32*32 + 17*512
assert (pc, pe, vc, ve, 2**56) == (8560574462,8560653547,33554432,33567232,72057594037927936)

receipt = {
    'verdict': 'ACCEPT_CORRECTED_SELECTED_GRAPH_AND_CHANGED_CHILD_CURRENT_INDEX',
    'review_scope': 'Manual source-model review and hash integration; not full source or quantum mechanization.',
    'documents': promotion['current_documents'],
    'promoted_artifacts': promotion['new_artifacts'],
    'subject_pins': promotion['subject_pins'],
    'initial_subject_review_sha256': sha(OUT / 'SUBJECT-RECEIPT.json'),
    'promotion_sha256': sha(X / 'SELECTED-GRAPH-PROMOTION.json'),
    'prior_review_receipts': {
        'cache-payload-source/INTEGRATION-FINAL-REVIEW.json': sha(X / 'cache-payload-source/INTEGRATION-FINAL-REVIEW.json'),
        'selected-graph-resources/REVIEW-RECEIPT.json': sha(X / 'selected-graph-resources/REVIEW-RECEIPT.json'),
    },
    'prior_doc_backups': {f'root-docs-before-selected-graph/{n}':h for n,h in old['documents'].items()},
    'preserved_scalar_artifacts': promotion['preserved_scalar_artifacts'],
    'checks': {
        'conditional_nonzero_seed_identity_controls_all_selected_claims': True,
        'exact_padded_selector_loss_2_pow_56': True,
        'selected_classical_handle_cap_QH_plus_2q_plus_4_nonzero_seed': True,
        'only_Win_and_final_classical_G_not_everraw_or_quantum_history': True,
        'quantum_two_handle_cost_and_no_history_extraction': True,
        'one_global_seed_zero_charge': True,
        'D7_base_requires_exposed_successful_row_and_base_inequality': True,
        'counter_insensitive_descent_preserves_pointwise_cover': True,
        'D7_base_subset_old_D7_full': True,
        'all_old_scalar_theorem_and_calculator_hashes_unchanged': True,
        'old_integration_document_pins_match_immutable_backup': True,
        'conventional_primitive_category_capacity_and_full_source_check_not_claimed_closed': True,
        'manual_results_do_not_add_checked_declarations': True,
        'uniform_nonzero_S_is_semantic_game_not_deterministic_coin_runtime_claim': True,
    },
    'manual_review_sha256': sha(OUT / 'SUBJECT-REVIEW.md'),
    'integration_manual_review_sha256': sha(OUT / 'INTEGRATION-REVIEW.md'),
    'checker_sha256': sha(Path(__file__)),
    'new_machine_checked_declarations': 0,
    'security_level_category': 'not established',
    'whole_goal_complete': False,
}
(OUT / 'INTEGRATION-REVIEW.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf8')
print(json.dumps({'verdict':receipt['verdict'],'documents':len(receipt['documents']),'checks':len(receipt['checks']),'receipt_sha256':sha(OUT / 'INTEGRATION-REVIEW.json')}))

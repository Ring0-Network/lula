"""Read-only checks of root promotion; writes only this reviewer's own JSON.

The --resources mode can run before promotion. The default refuses to emit
an integration receipt until the actual promoted artifact and backups exist.
"""
import ast
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
X = HERE.parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))


def resource_checks():
    root = load(X / 'root-outside-simulator/RESOURCE-CHECK.json')
    old = load(X / 'selected-promotion-review/T7-CONTROL-RESULTS.json')
    setup = (1 << 21) * (19505 + (1 << 32)) - 1
    hot = 82090 + 5 * (1 << 32)
    cold = 8560574463 + 82090 + 6 * (1 << 32)
    assert root['setup_public_cap'] == setup
    assert root['hot_public_per_sign'] == hot
    assert root['cold_public_per_sign'] == cold
    qs = {24, 30, 38, 40, 41, 44, 50, 64}
    assert len(old['q_resource_rows']) == 8
    assert {r['q_exponent'] for r in old['q_resource_rows']} == qs
    for row in old['q_resource_rows']:
        q = 1 << row['q_exponent']
        for mode, cap, private in [('hot', hot, 12816), ('cold', cold, 33567232)]:
            assert row[mode + '_honest_outside_plus_C'] == setup + q * cap + 3224 + 17392
            assert row[mode + '_F_cap'] == min(19212937084272640, 8704 + 2181038080 + q * private)
    seen = set()
    b = root['profile']['b']
    domain = sum(1 << (8*j) for j in range(b+1))
    degree = 1
    while degree < max(256, 8*b+1):
        degree *= 2
    for row in root['family_rows']:
        q = 1 << row['log2_q']
        adversary = 1 << row['log2_Q_adversarial']
        key = (row['log2_q'], row['log2_Q_adversarial'], row['mode'], row['adapter'])
        assert key not in seen
        seen.add(key)
        cap = {'hot': hot, 'cold': cold}[row['mode']]
        extra = {'PRE': 254, 'ROW': 17392}[row['adapter']]
        total = adversary + setup + q*cap + 3224 + extra
        coeffs = min(total*2, domain)
        assert row['T_all_outside_evaluations'] == total
        assert row['k'] == coeffs
        assert row['m'] == degree
        assert row['coefficient_bits'] == coeffs * degree
        assert row['coefficient_bytes'] * 8 == coeffs * degree
    expected = {(q, a, mode, adapter) for q in qs for a in (32, 64)
                for mode in ('hot', 'cold') for adapter in ('PRE', 'ROW')}
    assert seen == expected and len(seen) == 64
    assert root['inherited_type7_receipt_sha256'] == sha(X / 'selected-promotion-review/T7-INTEGRATION-REVIEW.json')
    assert sha(X / 'root-outside-simulator/field-recheck/toy_controls.py') == sha(HERE / 'toy_controls.py')
    assert sha(X / 'root-outside-simulator/field-recheck/toy-results.json') == sha(HERE / 'toy-results.json')
    result = {
        'status': 'PASS_INDEPENDENT_INTEGER_RESOURCE_RECHECK',
        'family_rows_checked': 64,
        'inherited_q_rows_checked': 8,
        'root_reexecution_source_and_results_match': True,
        'resource_check_sha256': sha(X / 'root-outside-simulator/RESOURCE-CHECK.json'),
        'root_resource_helper_sha256': sha(X / 'root-outside-simulator/check_resources.py'),
        'inherited_t7_control_results_sha256': sha(X / 'selected-promotion-review/T7-CONTROL-RESULTS.json'),
        'scope': 'Integer identities only; source caps are inherited; b=598 is an example; no security or performance category.',
    }
    (HERE / 'integration-resource-check.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return result


def main():
    resources = resource_checks()
    if '--resources' in sys.argv:
        print(json.dumps(resources, indent=2))
        return
    promotion_path = X / 'OUTSIDE-SIMULATOR-PROMOTION.json'
    assert promotion_path.exists(), 'Actual root promotion has not occurred.'
    promotion = load(promotion_path)
    predecessor = load(X / 'selected-promotion-review/T7-INTEGRATION-REVIEW.json')
    peer = load(HERE / 'SECOND-READER.json')
    docs = ['PROOF.md', 'OPEN.md', 'TERM-TABLE.md', 'REQUIREMENT-MAP.md', 'HANDOFF.md', 'SECURITY-CRITERION.md']
    assert set(promotion['documents']) == set(docs)
    assert promotion['prior_documents'] == predecessor['documents']
    assert promotion['prior_type7_receipt_sha256'] == sha(X / 'selected-promotion-review/T7-INTEGRATION-REVIEW.json')
    assert promotion['second_reader_sha256'] == sha(HERE / 'SECOND-READER.json')
    assert promotion['author_final_packet'].startswith('Still in progress; not relied upon.')
    assert promotion['root_resource_sha256'] == resources['resource_check_sha256']
    assert promotion['subject_pins'] == peer['subject_pins']
    for path, expected in peer['subject_pins'].items():
        assert sha(X / path) == expected
    for path, expected in peer['inherited_premise_pins'].items():
        assert sha(X / path) == expected
    assert peer['first_independent_derivation_saved_before_peer_reads']
    assert sha(HERE / 'first-independent-derivation.md') == peer['first_independent_derivation_sha256']
    for path, expected in predecessor['backup_pins'].items():
        assert sha(X / path) == expected
    old_qpre = load(X / 'selected-promotion-review/QPRE-INTEGRATION-REVIEW.json')
    for name, expected in old_qpre['documents'].items():
        assert sha(X / 'root-docs-before-type7' / name) == expected
    helper = X / 'root-promote-outside.py'
    parsed = ast.parse(helper.read_text(encoding='utf-8'))
    literals = {}
    for node in ast.walk(parsed):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    literals.setdefault(target.id, []).append(node.value.value)
    addition = literals['addition'][0]
    handoff = next(s for s in literals['text'] if 'latest continuation is PROGRESS' in s)
    backup_pins = {}
    for name in docs:
        backup = X / 'root-docs-before-outside' / name
        assert sha(backup) == predecessor['documents'][name]
        backup_pins['root-docs-before-outside/' + name] = sha(backup)
        suffix = ('\n## 14. Bounded-query efficient outside simulator\n' + addition if name == 'PROOF.md'
                  else handoff if name == 'HANDOFF.md' else addition)
        expected = backup.read_text(encoding='utf-8').rstrip() + '\n\n' + suffix.strip() + '\n'
        actual = (X / name).read_text(encoding='utf-8')
        assert actual == expected, name
        assert sha(X / name) == promotion['documents'][name]
    artifact_path = X / 'OUTSIDE-SIMULATOR-THEOREM.md'
    candidate = (X / 'chain-pre-adapter/outside-simulator/INDEPENDENT-DERIVATION.md').read_text(encoding='utf-8')
    replacements = [
        ('**PROVED — manual first candidate awaiting independent reading.**', '**PROVED — manual bounded-query B-only construction accepted by an independent mathematical reader.**'),
        ('**OPEN — independent reading and controls.**', '**PROVED / COMPUTED — review and controls supplied in the successor evidence below.**'),
        ('The direct tower irreducibility/multiplication construction, exact k-wise/whole-B route, malformed-state extension and complete budget need a different reader and discriminating finite controls before promotion. No new kernel declaration is claimed yet.',
         'The direct tower construction, whole-B route and matched invalid-state extension have received independent manual reading and discriminating finite controls. Complete numeric source caps are inherited from the already reviewed adapters and root arithmetic checks; this is not a new source-count audit. No new kernel declaration is claimed.'),
    ]
    for old, new in replacements:
        assert candidate.count(old) == 1
        candidate = candidate.replace(old, new, 1)
    expected_artifact = literals['header'][0] + candidate + '\n' + literals['footer'][0]
    assert artifact_path.read_text(encoding='utf-8') == expected_artifact
    assert promotion['new_artifact'] == {'OUTSIDE-SIMULATOR-THEOREM.md': sha(artifact_path)}
    protected = dict(predecessor['preserved_artifacts'])
    protected.update(predecessor['promoted_artifacts'])
    assert promotion['preserved_artifacts'] == protected
    for path, expected in protected.items():
        assert sha(X / path) == expected
    assert promotion['new_checked_declarations'] == 0
    assert promotion['supporting_checked_declarations_total'] == 40
    assert promotion['whole_source_game_checked_declarations'] == 0
    assert promotion['B_only_probability_preservation'] is True
    assert promotion['full_source_classifier_newly_certified'] is False
    assert promotion['level_category'] == 'not established'
    assert promotion['manuscript_edits'] == 0
    assert (HERE / 'OUTSIDE-INTEGRATION-REVIEW.md').exists(), 'Save manual current-artifact review first.'
    result = {
        'verdict': 'ACCEPT_SCOPED_B_ONLY_OUTSIDE_SIMULATOR_CURRENT_INDEX',
        'documents': promotion['documents'],
        'promoted_artifacts': promotion['new_artifact'],
        'prior_type7_receipt_sha256': sha(X / 'selected-promotion-review/T7-INTEGRATION-REVIEW.json'),
        'predecessor_backup_pins': backup_pins,
        'subject_pins': peer['subject_pins'],
        'author_final_packet': 'Not relied upon; accepted immutable first derivation is pinned by independent review.',
        'provenance_pins': {
            'OUTSIDE-SIMULATOR-PROMOTION.json': sha(promotion_path),
            'outside-field-check/SECOND-READER.json': sha(HERE / 'SECOND-READER.json'),
            'outside-field-check/first-independent-derivation.md': sha(HERE / 'first-independent-derivation.md'),
        },
        'helper_pins': {
            'root-promote-outside.py': sha(helper),
            'root-outside-simulator/check_resources.py': resources['root_resource_helper_sha256'],
            'outside-field-check/check_integration.py': sha(Path(__file__)),
        },
        'control_pins': {
            'outside-field-check/toy_controls.py': sha(HERE / 'toy_controls.py'),
            'outside-field-check/toy-results.json': sha(HERE / 'toy-results.json'),
            'root-outside-simulator/field-recheck/toy_controls.py': sha(X / 'root-outside-simulator/field-recheck/toy_controls.py'),
            'root-outside-simulator/field-recheck/toy-results.json': sha(X / 'root-outside-simulator/field-recheck/toy-results.json'),
            'root-outside-simulator/RESOURCE-CHECK.json': resources['resource_check_sha256'],
            'outside-field-check/integration-resource-check.json': sha(HERE / 'integration-resource-check.json'),
        },
        'inherited_premise_pins': peer['inherited_premise_pins'],
        'earlier_backup_pins': predecessor['backup_pins'],
        'prior_qpre_receipt_sha256': sha(X / 'selected-promotion-review/QPRE-INTEGRATION-REVIEW.json'),
        'preserved_artifacts': protected,
        'manual_review_sha256': sha(HERE / 'OUTSIDE-INTEGRATION-REVIEW.md'),
        'checks': {
            'actual_six_document_pins_and_exact_additions': True,
            'accepted_type7_predecessor_backups_preserved': True,
            'exact_immutable_author_body_and_three_status_edits': True,
            'unfinished_author_packet_not_relied_upon': True,
            'earlier_type7_qpre_backup_chain_unchanged': True,
            'source_probability_formulas_and_prior_scalar_artifacts_unchanged': True,
            'b_only_outside_success_equality_no_full_source_law': True,
            'independent_row_conditioning_not_rf_derived_target': True,
            'deterministic_bit_gate_resources_and_static_all_honest_t': True,
            'all64_resource_rows_and8_inherited_q_rows_rechecked': True,
            'root_reexecution_matches_independent_control': True,
            'no_new_kernel40_supporting0_whole_source': True,
            'conventional_category_capacity_still_open': True,
        },
        'supporting_checked_declarations_total': 40,
        'new_checked_declarations': 0,
        'whole_source_game_new_checked_declarations': 0,
        'source_counts_independently_rederived': False,
        'security_level_category': 'not established',
        'whole_goal_complete': False,
    }
    out = HERE / 'OUTSIDE-INTEGRATION-REVIEW.json'
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'verdict': result['verdict'], 'receipt_sha256': sha(out), 'manual_sha256': result['manual_review_sha256']}, indent=2))


if __name__ == '__main__':
    main()

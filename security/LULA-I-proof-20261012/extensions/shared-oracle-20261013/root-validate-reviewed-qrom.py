"""Validate the current reviewed finite-QROM cut without rerunning old proofs."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf8'))

p=subprocess.run([sys.executable,'-I','-B',str(X/'check_extension.py'),'preservation'],capture_output=True,text=True)
assert p.returncode==0,p.stderr
preservation=read(X/'PRESERVATION.json')
qc=read(X/'quantum-composition-numeric/ROOT-CROSSCHECK.json')
assert qc['status']=='PASS_ALL16_PINNED_QUANTUM_COMPONENT_TOTAL_AND_EXPONENT_CROSSCHECKS'
assert qc['master_script_sha256']==sha(X/'bounds.py')
assert qc['source_theorem_sha256']==sha(X/'QUANTUM-RO-THEOREM.md')
assert qc['complete_composition_review_sha256']==sha(X/'quantum-composition-second-reader/SECOND_READER.md')
assert qc['probability_checks']==176 and qc['exponent_checks']==112
assert all(qc['historical_manifest_checks'].values())
refined=read(X/'quantum-private-rare-numeric/ROOT-REFINED-CROSSCHECK.json')
assert refined['status']=='PASS_ALL16_ROOT_REFINED_ROWS_FIELDS_AND_EXPONENTS'
assert refined['numeric_field_count']==96 and refined['exponent_count']==64
for name,digest in refined['artifact_pins'].items():
    assert sha(X/name)==digest, name
assert refined['independent_candidate_sha256']==sha(X/'quantum-private-rare-numeric/CANDIDATE-BOUNDS.json')
cc=read(X/'root-current-classical-recheck/ROOT-CROSSCHECK.json')
assert cc['root_rows_compared']==16
assert cc['identities']['root_script_sha256']==sha(X/'bounds.py')
outputs={}
for name in ('bounds-QH64','bounds-QH128'):
    path=X/f'root-checks/{name}/bounds.json'
    assert qc['root_output_sha256'][name]==sha(path)
    data=read(path)
    assert data['script_sha256']==sha(X/'bounds.py')
    assert data['quantum_theorem_sha256']==sha(X/'QUANTUM-RO-THEOREM.md')
    assert len(data['rows'])==8
    for row in data['rows']:
        assert row['quantum_status']=='COMPUTED_FROM_REVIEWED_FINITE_QROM_SOURCE_GAME_UNION'
        assert row['quantum_total'] is not None
        assert row['quantum_category1_status']=='NOT_ESTABLISHED_NO_CERTIFIED_CAPACITY'
    outputs[name]={'sha256':sha(path),'rows':8,'Qq':data['rows'][0]['Qq']}
checks=[]
for source,receipt,count in (
 ('root-formal/SeedGuess.ec','root-formal/easycrypt-current.json',4),
 ('formal-tree/AddressedMerkle.lean','formal-tree/check.json',5),
 ('wots-certification/ChainEvidence.lean','wots-certification/check.json',8),
 ('root-formal/SPRSeparation.lean','root-formal/SPRSeparation-check.json',4),
 ('query-resource-formal/QueryThreshold.lean','query-resource-formal/CHECK.json',7),
 ('private-challenge-program/AdapterCounts.ec','private-challenge-program/EASYCRYPT-CHECK.json',5),
 ('selected-promotion-review/QPRE-Averaging.lean','selected-promotion-review/QPRE-Lean-Check.json',7)):
    record=read(X/receipt)
    assert record['exit_code']==0 and record['source_sha256']==sha(X/source)
    text=(X/source).read_text(encoding='utf8')
    assert not re.search(r'\b(sorry|admit|native_decide)\b',text)
    checks.append({'source':source,'sha256':sha(X/source),'successful_receipt':receipt,
      'receipt_sha256':sha(X/receipt),'checked_declarations':count,
      'scope':'Supporting algebra/list statements only; not complete Rust or quantum verification.'})
hidden=read(X/'root-dynamic-hidden-controls/CHECKS.json')
assert hidden['control_sha256']==sha(X/'root-dynamic-hidden-controls/control.py')
assert hidden['ordinary_marginal_exact'] and hidden['remaining_secret_conditional_states_identical']
assert sha(X/'QUANTUM-COVERAGE-DRAFT.md')=='990aeb1067f9ac12235ef3982bc9d3d132cffeab5e704a7d0865a69d77e0c0ce'
assert sha(X/'QUANTUM-COMPOSITION-DRAFT.md')=='71d3f23a3d161c7ade049dcf4f5d2a0467fe7a4a6a0bf97a899eb63bff708b89'
assert sha(X/'DYNAMIC-QUANTUM-HIDDEN-DRAFT.md')=='1b139a3cdd93621c4ebc05f98145807f1bbd23a19d7892440df9d42b3ed0560d'
docs=['PROOF.md','CLASSICAL-RO-THEOREM.md','QUANTUM-COVERAGE-THEOREM.md',
 'QUANTUM-RO-THEOREM.md','bounds.py','bounds-classical-reviewed.py','TERM-TABLE.md',
 'OPEN.md','REQUIREMENT-MAP.md','HANDOFF.md','SPR-ONLY-COUNTEREXAMPLE.md']
docs += ['QUANTUM-EVENT-SPECIFIC-THEOREM.md','bounds-event-specific.py']
resource=read(X/'query-resource-root/CHECK.json')
assert resource['status']=='PASS_ALL32_ADJACENT_RATIONAL_QUERY_BOUND_CROSSINGS'
assert resource['independent_certificate_sha256']==sha(X/'query-resource-independent/THRESHOLDS.json')
assert resource['independent_script_sha256']==sha(X/'query-resource-independent/thresholds.py')
assert resource['root_script_sha256']==sha(X/'query-resource-root/check.py')
assert len(resource['rows'])==32
resource_data=read(X/'query-resource-independent/THRESHOLDS.json')
for name,digest in resource_data['input_pins'].items(): assert sha(X/name)==digest,name
from fractions import Fraction
for row in resource_data['rows']:
    assert int(row['Q_fail'])==int(row['Q_pass'])+1
    assert Fraction(*map(int,row['pass_bound']['upper_rational']))<=Fraction(1,2)
    assert Fraction(*map(int,row['fail_bound']['lower_rational']))>Fraction(1,2)
resource_peer=read(X/'query-resource-formal/SECOND_READER_CHECK.json')
assert resource_peer['outcome']=='RECORDED_ENDPOINTS_AND_INPUT_PINS_PASS'
assert resource_peer['endpoint_pairs']==32 and resource_peer['endpoint_comparisons']==64
assert 'ACCEPTED_EXACT_OUTWARD_THRESHOLDS_WITHIN_REVIEWED_MODEL' in (X/'query-resource-formal/SECOND_READER.md').read_text(encoding='utf8')
for name,digest in resource_peer['artifacts'].items():
    assert sha(X/'query-resource-independent'/name)==digest,name
scope_review=read(X/'original-goal-audit-20261013/SUCCESSOR-CHECK.json')
assert scope_review['outcome']=='PASS_ORIGINAL_SCOPE_NO_CROSSING_AND_SUCCESSOR_INDEX'
assert all(scope_review['checks'].values())
for name,digest in scope_review['successor_pins'].items():
    prior=(X/'root-docs-before-payload-private'/name)
    assert sha(prior if prior.exists() else X/name)==digest,name
for name,digest in scope_review['accepted_artifacts_unchanged'].items(): assert sha(X/name)==digest,name
docs += ['SECURITY-CRITERION.md','DELEGATION-INCIDENT.md',
 'query-resource-independent/thresholds.py','query-resource-independent/THRESHOLDS.json',
 'query-resource-independent/INDEPENDENT_DERIVATION.md',
 'query-resource-formal/INDEPENDENT_DERIVATION.md','query-resource-formal/SECOND_READER.md',
 'query-resource-formal/SECOND_READER_CHECK.json',
 'query-resource-root/check.py','query-resource-root/CHECK.json',
 'original-goal-audit-20261013/AUDIT.md','original-goal-audit-20261013/AUDIT.json',
 'original-goal-audit-20261013/SUCCESSOR-CHECK.md','original-goal-audit-20261013/SUCCESSOR-CHECK.json']
payload_review=read(X/'cache-payload-source/REVIEW.json')
assert payload_review['verdict']=='ACCEPT_MANUAL_EXACT_PUBLIC_LOGICAL_PAYLOAD_EXTENSION_WITH_UNCHANGED_FINITE_MODEL_BOUNDS'
private_review=read(X/'cache-payload-source/PRIVATE-CHALLENGE-REVIEW.json')
assert private_review['verdict']=='ACCEPT_MANUAL_JOINT_ACCESS_ROM_ADAPTER_IDENTITIES_AND_RESOURCE_CAPS'
for review in (payload_review,private_review):
    for artifact in review['files'].values():
        assert sha(Path(artifact['path']))==artifact['sha256'],artifact['path']
payload_control=read(X/'cache-payload-math/CONTROL-RESULTS.json')
assert payload_control['status']=='PASS_SCOPED_EXACT_FINITE_OBSERVER_CONTROLS'
assert payload_control['script_sha256']==sha(X/'cache-payload-math/control.py')
assert payload_control['joint_worlds']==524288 and payload_control['outside_payload_memory_groups']==32768
assert payload_control['negative_seed_fixture_support_mass']=='1'
assert payload_control['remaining_hidden_coordinate_guess_probability']=='1/4'
counts=read(X/'private-challenge-program/COUNT-CHECKS.json')
assert counts['script_sha256']==sha(X/'private-challenge-program/check_counts.py')
assert counts['setup_private_distinct_and_invocations']==2181038080
assert counts['hot_private_distinct']==12816 and counts['cold_private_distinct']==33567232
assert counts['public_final_verifier_cap']==3224 and len(counts['q_columns'])==8
promotion=read(X/'PAYLOAD-PRIVATE-PROMOTION.json')
for name,digest in promotion['new_artifacts'].items(): assert sha(X/name)==digest,name
integration=read(X/'cache-payload-source/INTEGRATION-FINAL-REVIEW.json')
assert integration['verdict']=='ACCEPT_CORRECTED_PAYLOAD_PRIVATE_CURRENT_INDEX'
assert integration['all_five_status_repairs_and_two_precision_repairs_closed']
assert integration['same_sufficient_bounds_not_advantage_equality']
assert integration['payload_aware_internal_adapters_accepted']
assert integration['category_capacity_and_conventional_generic_obligations_still_open']
for group in ('documents','promoted_artifacts','prior_review_receipts'):
    for name,digest in integration[group].items():
        prior_doc=X/'root-docs-before-selected-graph'/name
        assert sha(prior_doc if group=='documents' else X/name)==digest,name
assert integration['current_index_sha256']==sha(X/'PAYLOAD-PRIVATE-CURRENT-INDEX.json')
assert integration['preserved_promotion_sha256']==sha(X/'PAYLOAD-PRIVATE-PROMOTION.json')

selected=read(X/'selected-promotion-review/INTEGRATION-REVIEW.json')
assert selected['verdict']=='ACCEPT_CORRECTED_SELECTED_GRAPH_AND_CHANGED_CHILD_CURRENT_INDEX'
assert all(selected['checks'].values()) and len(selected['checks'])==14
assert selected['new_machine_checked_declarations']==0
assert selected['security_level_category']=='not established' and not selected['whole_goal_complete']
for group in ('documents','promoted_artifacts','subject_pins','prior_review_receipts','prior_doc_backups','preserved_scalar_artifacts'):
    for name,digest in selected[group].items():
        prior_doc=X/'root-docs-before-chain-pre'/name
        assert sha(prior_doc if group=='documents' else X/name)==digest,name
assert selected['promotion_sha256']==sha(X/'SELECTED-GRAPH-PROMOTION.json')
assert selected['initial_subject_review_sha256']==sha(X/'selected-promotion-review/SUBJECT-RECEIPT.json')
assert selected['integration_manual_review_sha256']==sha(X/'selected-promotion-review/INTEGRATION-REVIEW.md')
assert selected['checker_sha256']==sha(X/'selected-promotion-review/check_integration.py')
graph_resource=read(X/'selected-graph-resources/REVIEW-RECEIPT.json')
assert graph_resource['outcome']=='ACCEPT_LOCALIZED_ADDRESSED_RO_ADAPTER_WITH_NONZERO_SEED_SCOPE'
for name,digest in graph_resource['subject_pins'].items():assert sha(X/name)==digest,name
for name,digest in graph_resource['own_pins'].items():assert sha(X/'selected-graph-resources'/name)==digest,name
assert graph_resource['numeric_receipts']['full_graph_nodes']==39339469515522047
assert graph_resource['numeric_receipts']['selected_dependency_rows']==372
assert graph_resource['numeric_receipts']['qrows']==8
assert graph_resource['numeric_receipts']['strict_predecessor_public_max']==8560574462
assert graph_resource['numeric_receipts']['final_route_public']==8560653547
assert graph_resource['numeric_receipts']['padded_selector_loss']==2**56
selected_control=read(X/'selected-graph-challenge/LOCALIZED-CONTROL-RESULTS.json')
assert selected_control
assert sha(X/'selected-graph-challenge/localized_control.py')=='a786fd70856573f344b212289b28c40991923960bd972c91237c7236aaea2e1e'
assert sha(X/'selected-graph-challenge/LOCALIZED-CONTROL-RESULTS.json')=='6767d3dc53b23769f698acdb8169b476b26d3f8c0007e8da379ca04f91180c25'

docs += ['SELECTED-GRAPH-REDUCTION.md','CHANGED-CHILD-EXTRACTION.md','SELECTED-GRAPH-PROMOTION.json',
 'selected-promotion-review/SUBJECT-RECEIPT.json','selected-promotion-review/INTEGRATION-REVIEW.json',
 'selected-promotion-review/INTEGRATION-REVIEW.md','selected-promotion-review/check_integration.py',
 'selected-graph-resources/REVIEW-RECEIPT.json','selected-graph-challenge/LOCALIZED-FINAL-SUCCESSOR.md',
 'selected-graph-challenge/LOCALIZED-SEED-SCOPE-CLARIFICATION.md',
 'selected-primitive-definitions/D7-BASE-EXTRACTION.md','selected-graph-challenge/D7-BASE-SECOND-READER.md',
 'selected-graph-challenge/localized_control.py','selected-graph-challenge/LOCALIZED-CONTROL-RESULTS.json']

pre=read(X/'selected-promotion-review/PRE-INTEGRATION-REVIEW.json')
assert pre['verdict']=='ACCEPT_CORRECTED_CLASSICAL_PRE_CURRENT_INDEX'
assert len(pre['checks'])==12 and all(pre['checks'].values())
assert pre['new_machine_checked_declarations']==0 and not pre['whole_goal_complete']
assert pre['security_level_category']=='not established'
for group in ('documents','promoted_artifacts','subject_pins','prior_review_receipts','prior_doc_backups','preserved_artifacts','controls'):
    for name,digest in pre[group].items():
        prior_doc=X/'root-docs-before-quantum-pre'/name
        assert sha(prior_doc if group=='documents' else X/name)==digest,name
assert pre['promotion_sha256']==sha(X/'CLASSICAL-PRE-PROMOTION.json')
assert pre['manual_review_sha256']==sha(X/'selected-promotion-review/PRE-INTEGRATION-REVIEW.md')
assert pre['checker_sha256']==sha(X/'selected-promotion-review/PRE-check-integration.py')
pre_subject=read(X/'chain-pre-independent/COMBINED-REVIEW.json')
assert pre_subject['status']=='ACCEPTED_SCOPED_CLASSICAL_RO_RELATIVE_MANUAL'
for name,digest in pre_subject['subjects'].items():assert sha(X/name)==digest,name
for group in ('independent_before_peer','review'):
    for name,digest in pre_subject[group].items():assert sha(X/'chain-pre-independent'/name)==digest,name
pre_author=read(X/'chain-pre-adapter/PROVENANCE.json')
assert pre_author['status']=='READY_FOR_ROOT_PROMOTION_SCOPED_CLASSICAL_RO_RELATIVE'
for name,digest in pre_author['files'].items():assert sha(X/'chain-pre-adapter'/name)==digest,name
assert pre_author['reader_receipt']['sha256']==sha(X/pre_author['reader_receipt']['path'])
assert pre_author['resources']['protected_combined']==20229886488608768
assert pre_author['resources']['combined_selector_bits']==55
assert pre_author['resources']['extra_public_hashes']==254
pre_resources=read(X/'selected-promotion-review/PRE-COMBINED-REVIEW.json')
assert pre_resources['verdict']=='ACCEPT_LOCALIZED_COMBINED_CLASSICAL_RO_RELATIVE_PRE_MANUAL'
assert all(pre_resources['checks'].values()) and pre_resources['q_resource_columns']==8
for name,digest in pre_resources['subject_pins'].items():assert sha(X/name)==digest,name
for name,digest in pre_resources['own_pins'].items():assert sha(X/'selected-promotion-review'/name)==digest,name
pre_control=read(X/'selected-promotion-review/PRE-CONTROL-RESULTS.json')
assert pre_control['status']=='PASS_SCOPED_ORDINARY_WORLD_STOPPED_PREFIX_AND_RESOURCE_CONTROLS'
assert pre_control['ordinary_worlds']==512 and len(pre_control['q_resource_rows'])==8
assert pre_control['script_sha256']==sha(X/'selected-promotion-review/PRE-positive-control.py')
for row in pre_control['prekey_atomic_disclosure_postkey_policies']:
    assert row['selected_success_sum']>=row['source_events']
    assert row['selected_first_hit_couplings']==row['source_events']
qs=[24,30,38,40,41,44,50,64]
L=2**32
hs=2**21*(19505+L)-1
hot=82090+5*L
cold=8560574463+82090+6*L
nd=19212937084272640
for exponent,row in zip(qs,pre_control['q_resource_rows'],strict=True):
    q=2**exponent
    assert row['q_exponent']==exponent
    assert row['hot_honest_public_plus_254']==hs+q*hot+3224+254
    assert row['cold_honest_public_plus_254']==hs+q*cold+3224+254
    assert row['hot_F_distinct_cap']==min(nd,1+2181038080+q*12816)
    assert row['cold_F_distinct_cap']==min(nd,1+2181038080+q*33567232)
assert 480*(2**41+2**36+2**31+2**26)+4080*2**21==1089588072284160
assert 2**41*17*512==19140298416324608
assert 2**54<20229886488608768<2**55
docs += ['CLASSICAL-PRE-REDUCTION.md','CLASSICAL-PRE-PROMOTION.json',
 'chain-pre-adapter/PROVENANCE.json','chain-pre-adapter/INDEPENDENT_DERIVATION.md',
 'chain-pre-adapter/FORS-LOCALIZED-SUCCESSOR.md','chain-pre-adapter/CONTROL-RESULTS.json',
 'chain-pre-adapter/control.py','chain-pre-independent/COMBINED-REVIEW.json',
 'chain-pre-independent/COMBINED-SECOND-READER.md','chain-pre-independent/FORS-LOCALIZED-SIBLING.md',
 'selected-promotion-review/PRE-INTEGRATION-REVIEW.json','selected-promotion-review/PRE-INTEGRATION-REVIEW.md',
 'selected-promotion-review/PRE-check-integration.py','selected-promotion-review/PRE-COMBINED-REVIEW.json',
 'selected-promotion-review/PRE-CONTROL-RESULTS.json','selected-promotion-review/PRE-positive-control.py']

qpre=read(X/'selected-promotion-review/QPRE-INTEGRATION-REVIEW.json')
assert qpre['verdict']=='ACCEPT_CORRECTED_FINITE_QPRE_CURRENT_INDEX'
assert len(qpre['checks'])==12 and all(qpre['checks'].values())
assert qpre['supporting_checked_declarations_total']==40
assert qpre['new_supporting_declarations']==7 and qpre['whole_source_game_new_checked_declarations']==0
assert qpre['security_level_category']=='not established' and not qpre['whole_goal_complete']
for group in ('documents','promoted_artifacts','source_subjects','provenance_pins','prior_review_receipts','backup_pins','preserved_artifacts','control_pins','helper_pins'):
    for name,digest in qpre[group].items():
        path=X/'root-docs-before-type7'/name if group=='documents' else X/name
        assert sha(path)==digest,name
assert qpre['manual_review_sha256']==sha(X/'selected-promotion-review/QPRE-INTEGRATION-REVIEW.md')
assert qpre['checker_sha256']==sha(X/'selected-promotion-review/QPRE-check-integration.py')
qpre_subject=read(X/'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json')
assert qpre_subject['status']=='ACCEPTED_SCOPED_FINITE_QROM_RELATIVE_MANUAL'
assert qpre_subject['all_outside_raw_calls_share_fixed_table'] and not qpre_subject['core_numeric_changes']
for name,digest in qpre_subject['subjects'].items():assert sha(X/'chain-pre-adapter'/name)==digest,name
qpre_author=read(X/'chain-pre-adapter/quantum-PROVENANCE.json')
assert qpre_author['status']=='READY_FOR_ROOT_PROMOTION_SCOPED_FINITE_QROM_RELATIVE_MANUAL'
assert not qpre_author['core_numeric_bounds_changed'] and not qpre_author['source_manuscript_parameters_changed']
for name,digest in qpre_author['files'].items():assert sha(X/'chain-pre-adapter'/name)==digest,name
assert qpre_author['reader_receipt']['sha256']==sha(X/qpre_author['reader_receipt']['path'])
qpre_resource=read(X/'selected-promotion-review/QPRE-FINAL-REVIEW.json')
assert qpre_resource['verdict']=='ACCEPT_CORRECTED_QPRE_ALGEBRA_AND_FINITE_RESOURCE_SCOPE'
for name,digest in qpre_resource['subject_pins'].items():assert sha(X/name)==digest,name
for name,digest in qpre_resource['own_pins'].items():assert sha(X/'selected-promotion-review'/name)==digest,name
for name,digest in qpre_resource['prior_classical_documents'].items():assert sha(X/'root-docs-before-quantum-pre'/name)==digest,name
for name,digest in qpre_resource['preserved_scalar_artifacts'].items():assert sha(X/name)==digest,name
assert qpre_resource['D_cut']==1016949404336128
assert qpre_resource['L']==2**55 and qpre_resource['new_supporting_checked_declarations']==7
assert qpre_resource['full_source_game_quantum_checked_declarations']==0
qpre_lean=read(X/'selected-promotion-review/QPRE-Lean-Check.json')
assert qpre_lean['checked_declarations']==7 and qpre_lean['exit_code']==0
assert qpre_lean['source_sha256']==sha(X/'selected-promotion-review/QPRE-Averaging.lean')
assert qpre_lean['log_sha256']==sha(X/'selected-promotion-review/QPRE-Lean.log')
assert qpre_lean['custom_axioms']==0 and qpre_lean['admissions']==0
axiom_log=(X/'selected-promotion-review/QPRE-Lean.log').read_text(encoding='utf8')
axiom_sets=re.findall(r'depends on axioms: \[([^\]]*)\]',axiom_log)
assert len(axiom_sets)==7
for items in axiom_sets:
    assert {x.strip() for x in items.split(',') if x.strip()} <= {'propext','Classical.choice','Quot.sound'}
qpre_control=read(X/'chain-pre-adapter/quantum-CONTROL-RESULTS.json')
assert qpre_control['status']=='COMPUTED_FINITE_CHANNEL_CONTROLS_NOT_SOURCE_QROM_PROOF'
assert len(qpre_control['checks'])==6 and qpre_control['final_first_event_checks']==3072
assert qpre_control['non_genuine_prefix_mergers']==1024
for row in qpre_control['checks']:
    assert row['worlds']==1024
    assert row['support_first']<=row['support_bound']+1e-12
    assert row['support_second']<=row['support_bound']+1e-12
    assert row['squared_total_diff']<=row['vector_triangle_bound']**2+1e-12
qpre_algebra=read(X/'selected-promotion-review/QPRE-Algebra-Control.json')
assert qpre_algebra['status']=='PASS_EXACT_SELECTOR_CROSS_TERM_COUNTEREXAMPLE_AND_SOURCE_RESOURCE_LEDGER'
assert qpre_algebra['script_sha256']==sha(X/'selected-promotion-review/QPRE-Algebra-Control.py')
bad_expansion=qpre_algebra['missing_sqrt_L_counterexample']
assert Fraction(bad_expansion['correct_envelope'])==Fraction(bad_expansion['actual_source_success'])==Fraction(1,4)
assert Fraction(bad_expansion['incorrect_cross_term_envelope'])==Fraction(3,16)<Fraction(1,4)
assert qpre_algebra['D_cut']==32*14*(2**41+2**36+2**31+2**26)+16*254*2**21==1016949404336128
for exponent,row in zip(qs,qpre_algebra['q_source_resource_rows'],strict=True):
    q=2**exponent
    assert row['q_exp']==exponent
    assert row['honest_hot_public_plus254']==hs+q*hot+3224+254
    assert row['honest_cold_public_plus254']==hs+q*cold+3224+254
    assert row['hot_private_distinct_cap']==min(nd,1+2181038080+q*12816)
    assert row['cold_private_distinct_cap']==min(nd,1+2181038080+q*33567232)
docs += ['QUANTUM-PRE-REDUCTION.md','QUANTUM-PRE-PROMOTION.json',
 'chain-pre-adapter/quantum-PROVENANCE.json','chain-pre-adapter/quantum-INDEPENDENT-DERIVATION.md',
 'chain-pre-adapter/quantum-CLARIFICATION.md','chain-pre-adapter/quantum-RESOURCE-CLARIFICATION.md',
 'chain-pre-adapter/quantum-control.py','chain-pre-adapter/quantum-CONTROL-RESULTS.json',
 'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json',
 'chain-pre-independent/quantum-prefix/CORRECTED-SUCCESSOR.md',
 'selected-promotion-review/QPRE-INTEGRATION-REVIEW.json','selected-promotion-review/QPRE-INTEGRATION-REVIEW.md',
 'selected-promotion-review/QPRE-check-integration.py','selected-promotion-review/QPRE-FINAL-REVIEW.json',
 'selected-promotion-review/QPRE-Averaging.lean','selected-promotion-review/QPRE-Lean-Check.json',
 'selected-promotion-review/QPRE-Lean.log','selected-promotion-review/QPRE-Algebra-Control.json']
docs += ['CACHE-PAYLOAD-THEOREM.md','PRIVATE-REDUCTION-PROGRAMS.md',
 'PAYLOAD-PRIVATE-PROMOTION.json','cache-payload-source/REVIEW.json',
 'cache-payload-source/PRIVATE-CHALLENGE-REVIEW.json',
 'cache-payload-math/CONTROL-RESULTS.json','cache-payload-math/control.py',
 'private-challenge-program/COUNT-CHECKS.json','private-challenge-program/check_counts.py',
 'private-challenge-program/FINAL-SUCCESSOR.md','private-challenge-program/FINAL-PROVENANCE.json',
 'PAYLOAD-PRIVATE-CURRENT-INDEX.json','cache-payload-source/INTEGRATION-FINAL-REVIEW.md',
 'cache-payload-source/INTEGRATION-FINAL-REVIEW.json']
t7=read(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.json')
assert t7['verdict']=='ACCEPT_CORRECTED_TYPE7_CURRENT_INDEX'
assert len(t7['checks'])==13 and all(t7['checks'].values())
assert t7['supporting_checked_declarations_total']==40 and t7['new_supporting_declarations']==0
assert t7['whole_source_game_new_checked_declarations']==0 and not t7['whole_goal_complete']
assert t7['security_level_category']=='not established'
for group in ('documents','promoted_artifacts','source_subjects','provenance_pins','prior_review_receipts','backup_pins','preserved_artifacts','control_pins'):
    for name,digest in t7[group].items():
        path=X/'root-docs-before-outside'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
assert t7['manual_review_sha256']==sha(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.md')
assert t7['checker_sha256']==sha(X/'selected-promotion-review/T7-check-integration.py')
t7_source=read(X/'chain-pre-adapter/type7/PROVENANCE.json')
assert t7_source['status']=='READY_FOR_ROOT_PROMOTION_SCOPED_CLASSICAL_QROM_ROW_INTERFACE_MANUAL'
for name,digest in t7_source['files'].items():assert sha(X/'chain-pre-adapter/type7'/name)==digest,name
for name in ('independent_reader_receipt','previous_reader_receipt','additional_resource_reader'):
    assert t7_source[name]['sha256']==sha(X/t7_source[name]['path'])
t7_resource=read(X/'selected-promotion-review/T7-REVIEW.json')
assert t7_resource['verdict']=='ACCEPT_SCOPED_FIRST_ACCEPTED_TYPE7_ROW_RESOURCES_AND_INTERFACE'
for name,digest in t7_resource['subject_pins'].items():assert sha(X/name)==digest,name
for name,digest in t7_resource['own_pins'].items():assert sha(X/'selected-promotion-review'/name)==digest,name
for name,digest in t7_resource['prior_documents'].items():assert sha(X/'root-docs-before-type7'/name)==digest,name
for name,digest in t7_resource['preserved_scalar_artifacts'].items():assert sha(X/name)==digest,name
assert t7_resource['rows']==sum(2**h for h in (41,36,31,26,21))==2269959421952
assert t7_resource['selector_pad']==2**42
assert t7_resource['C_public_max']==17392 and t7_resource['C_F_distinct_max']==8704
assert t7_resource['target_row_challenge_preprocessing_cap']==2**32
assert t7['source_sha256']==t7_resource['source_sha256']=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
docs += ['TYPE7-REDUCTION-PROGRAM.md','TYPE7-PROMOTION.json','TYPE7-PROMOTION-PRELIMINARY.json',
 'chain-pre-adapter/type7/PROVENANCE.json','selected-promotion-review/T7-INTEGRATION-REVIEW.json',
 'selected-promotion-review/T7-INTEGRATION-REVIEW.md','selected-promotion-review/T7-check-integration.py',
 'selected-promotion-review/T7-REVIEW.json','selected-promotion-review/T7-CONTROL-RESULTS.json']
outside=read(X/'outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json')
assert outside['verdict']=='ACCEPT_SCOPED_B_ONLY_OUTSIDE_SIMULATOR_CURRENT_INDEX'
assert len(outside['checks'])==13 and all(outside['checks'].values())
assert outside['supporting_checked_declarations_total']==40 and outside['new_checked_declarations']==0
assert outside['whole_source_game_new_checked_declarations']==0 and not outside['whole_goal_complete']
assert outside['security_level_category']=='not established'
for group in ('documents','promoted_artifacts','predecessor_backup_pins','subject_pins','provenance_pins','helper_pins','control_pins','inherited_premise_pins','earlier_backup_pins','preserved_artifacts'):
    for name,digest in outside[group].items():
        path=X/'root-docs-before-standard'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
assert outside['manual_review_sha256']==sha(X/'outside-field-check/OUTSIDE-INTEGRATION-REVIEW.md')
assert outside['prior_type7_receipt_sha256']==sha(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.json')
outside_peer=read(X/'outside-field-check/SECOND-READER.json')
assert outside_peer['verdict']=='ACCEPT_SCOPED_MANUAL_BOUNDED_QUERY_CONSTRUCTION_AND_B_ONLY_REPLACEMENT'
assert all(outside_peer['manual_acceptance'].values()) and outside_peer['control_exit_code']==0
assert outside_peer['first_independent_derivation_saved_before_peer_reads']
for group in ('subject_pins','inherited_premise_pins'):
    for name,digest in outside_peer[group].items():assert sha(X/name)==digest,name
assert sha(X/'outside-field-check/first-independent-derivation.md')==outside_peer['first_independent_derivation_sha256']
assert sha(X/'outside-field-check/SECOND-READER.md')==outside_peer['review_sha256']
assert sha(X/'root-outside-simulator/field-recheck/toy-results.json')==outside_peer['control_results_sha256']
outside_resources=read(X/'root-outside-simulator/RESOURCE-CHECK.json')
assert outside_resources['status']=='PASS_ROOT_INTEGER_RESOURCE_IDENTITIES_NOT_SECURITY_BOUNDS'
assert outside_resources['eight_inherited_q_rows_checked']==8 and len(outside_resources['family_rows'])==64
for row in outside_resources['family_rows']:
    assert row['log2_q'] in qs and row['log2_Q_adversarial'] in (32,64)
    hmode=hot if row['mode']=='hot' else cold
    extra=254 if row['adapter']=='PRE' else 17392
    total=2**row['log2_Q_adversarial']+hs+2**row['log2_q']*hmode+3224+extra
    assert row['T_all_outside_evaluations']==total and row['k']==2*total
    assert row['m']==8192 and row['coefficient_bits']==row['k']*8192
    assert row['coefficient_bytes']==row['coefficient_bits']//8
assert len({(r['log2_q'],r['log2_Q_adversarial'],r['mode'],r['adapter']) for r in outside_resources['family_rows']})==64
docs += ['OUTSIDE-SIMULATOR-THEOREM.md','OUTSIDE-SIMULATOR-PROMOTION.json','root-promote-outside.py',
 'outside-field-check/SECOND-READER.json','outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json',
 'outside-field-check/OUTSIDE-INTEGRATION-REVIEW.md','outside-field-check/check_integration.py',
 'root-outside-simulator/check_resources.py','root-outside-simulator/RESOURCE-CHECK.json']
standard=read(X/'STANDARD-CANONICAL-PROMOTION.json')
assert standard['status']=='REVIEWED_MANUAL_STANDARD_CANONICAL_COMPONENT_PROMOTED'
assert standard['cumulative_supporting_checked_declarations']==44
assert standard['new_supporting_checked_declarations']==4
assert standard['new_whole_source_game_checked_declarations']==0 and not standard['whole_goal_complete']
for group in ('documents','artifact','subject_pins','preserved_core_artifacts','kernel_pins'):
    for name,digest in standard[group].items():
        path=X/'root-docs-before-primitive-successors'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for name,digest in standard['predecessor_documents'].items():assert sha(X/'root-docs-before-standard'/name)==digest,name
assert standard['subject_review_sha256']==sha(X/'outside-field-check/standard-component-review/SUBJECT-REVIEW.json')
counter=read(X/'root-keyed-review/COUNTER-POLICY-CHECK.json')
assert counter['exit_code']==0 and counter['checked_declarations']==4
assert counter['source_sha256']==sha(X/'root-keyed-review/CounterPolicy.lean')
assert counter['log_sha256']==sha(X/'root-keyed-review/CounterPolicy.log')
assert counter['custom_axioms']==counter['admissions']==counter['source_security_checked_declarations']==0
assert all(set(items)<={'propext','Classical.choice','Quot.sound'} for items in counter['axioms'].values())
assert not re.search(r'\b(sorry|admit|native_decide)\b',(X/'root-keyed-review/CounterPolicy.lean').read_text())
checks.append({'source':'root-keyed-review/CounterPolicy.lean','sha256':counter['source_sha256'],
 'successful_receipt':'root-keyed-review/COUNTER-POLICY-CHECK.json',
 'receipt_sha256':sha(X/'root-keyed-review/COUNTER-POLICY-CHECK.json'),'checked_declarations':4,
 'scope':'Synthetic two-base counter-policy separation, not source cryptographic game.'})
docs += ['STANDARD-CANONICAL-COMPONENT.md','STANDARD-CANONICAL-PROMOTION.json','root-promote-standard.py',
 'outside-field-check/standard-component-review/SUBJECT-REVIEW.json',
 'root-keyed-review/CounterPolicy.lean','root-keyed-review/COUNTER-POLICY-CHECK.json']
standard_current=read(X/'selected-promotion-review/STANDARD-INTEGRATION-REVIEW.json')
assert standard_current['status']=='ACCEPTED_SCOPED_STANDARD_CANONICAL_CURRENT_INDEX'
assert all(standard_current['checks'].values())
for group in ('documents','promoted_artifacts','source_subjects','backup_pins','preserved_artifacts','control_pins','prior_review_receipts','provenance_pins'):
    for name,digest in standard_current[group].items():
        path=X/'root-docs-before-primitive-successors'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
primitive=read(X/'PRIMITIVE-SUCCESSORS-PROMOTION.json')
assert primitive['status']=='REVIEWED_PRIVATE_FIXED_H_AND_RESTRICTED_QROM_SUCCESSORS_PROMOTED'
assert primitive['cumulative_supporting_checked_declarations']==44
assert primitive['new_source_game_checked_declarations']==primitive['source_scalar_manuscript_changes']==0
assert not primitive['whole_goal_complete'] and primitive['original_level_category_statement']=='not established'
for group in ('documents','artifacts','receipt_pins','preserved_core_artifacts'):
    for name,digest in primitive[group].items():
        path=X/'root-docs-before-message-graph'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for name,digest in primitive['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
for name,digest in primitive['predecessor_documents'].items():assert sha(X/'root-docs-before-primitive-successors'/name)==digest,name
private_review=read(X/'outside-field-check/public-h-private-review/REVIEW.json')
assert all(private_review['checks'].values()) and all(v==0 for v in private_review['control_exits'].values())
assert private_review['source_game_checked_declarations']==0 and not private_review['external_RO_or_QROM_numerical_transfer']
row_review=read(X/'restricted-row-third-review/FINAL-SUBJECT-REVIEW.json')
assert row_review['status']=='ACCEPTED_FINAL_MANUAL_RESTRICTED_CANONICAL_QROM_COMPONENT'
assert row_review['new_extractor_M']=='Q' and row_review['old_adapter_M']=='Q+1'
assert row_review['new_game_kernel_declarations']==row_review['old_scalar_changes']==0
one_review=read(X/'restricted-row-third-review/ONE-QUERY-RECEIPT.json')
assert one_review['controls_exit_code']==0 and one_review['clean_basis_checks']==8192
assert one_review['mixed_region_checks']==256 and not one_review['terminated_optional_exhaustive']['completed_result']
root_one=read(X/'root-keyed-review/ONE-QUERY-CONTROL.json')
assert root_one['clean_basis_states_checked']==8192 and root_one['boolean_queries_per_raw_xor']==1
assert root_one['source_sha256']==sha(X/'root-keyed-review/one_query_completion.py')
assert root_one['proof_sha256']==sha(X/'root-keyed-review/ONE-QUERY-COMPLETION.md')
docs += ['PRIVATE-FIXED-H-REDUCTION.md','RESTRICTED-CANONICAL-QROM.md',
 'PRIMITIVE-SUCCESSORS-PROMOTION.json','root-promote-primitive-successors.py',
 'selected-promotion-review/STANDARD-INTEGRATION-REVIEW.json',
 'outside-field-check/public-h-private-review/REVIEW.json',
 'outside-field-check/public-h-private-review/FINAL-SUBJECT-REVIEW.json',
 'restricted-row-third-review/FINAL-SUBJECT-REVIEW.json','restricted-row-third-review/ONE-QUERY-RECEIPT.json',
 'root-keyed-review/ONE-QUERY-COMPLETION.md','root-keyed-review/ONE-QUERY-CONTROL.json']
primitive_current=read(X/'selected-promotion-review/PRIMITIVE-INTEGRATION-REVIEW.json')
assert primitive_current['status']=='ACCEPTED_SCOPED_PRIVATE_FIXED_H_AND_RESTRICTED_QROM_CURRENT_INDEX'
assert all(primitive_current['checks'].values()) and primitive_current['accepted_evidence_items']==98
assert primitive_current['cumulative_supporting_checked_declarations']==44
assert primitive_current['new_source_game_checked_declarations']==0 and not primitive_current['whole_goal_complete']
for group in ('documents','promoted_artifacts','source_subjects','prior_review_receipts','backup_pins','preserved_artifacts','provenance_pins'):
    for name,digest in primitive_current[group].items():
        path=X/'root-docs-before-message-graph'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for group in ('accepted_evidence_absolute_pins','external_absolute_pins'):
    for name,digest in primitive_current[group].items():assert sha(Path(name))==digest,name
docs += ['selected-promotion-review/PRIMITIVE-INTEGRATION-REVIEW.json']
message=read(X/'MESSAGE-GRAPH-PROMOTION.json')
assert message['status']=='REVIEWED_MESSAGE_GRAPH_FIXED_H_SYMBOLIC_SUCCESSORS_PROMOTED'
assert message['cumulative_supporting_checked_declarations']==47
assert message['new_source_game_checked_declarations']==message['source_scalar_manuscript_changes']==0
assert message['whole_goal_complete'] is False
assert message['original_level_category_statement']=='not established'
for group in ('documents','artifacts','receipt_pins'):
    for name,digest in message[group].items():
        path=X/'root-docs-before-hidden-ud-pre'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for name,digest in message['predecessor_documents'].items():
    assert sha(X/'root-docs-before-message-graph'/name)==digest,name
for name,digest in message['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
projection=read(X/'root-message-hash/PROJECTION-CHECK.json')
assert projection['exit_code']==0 and projection['checked_declarations']==3
assert projection['source_sha256']==sha(X/'root-message-hash/DigestProjection.lean')
assert projection['log_sha256']==sha(X/'root-message-hash/DigestProjection.log')
assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in projection['axiom_sets'])
assert not re.search(r'\b(sorry|admit|native_decide|axiom)\b',(X/'root-message-hash/DigestProjection.lean').read_text())
checks.append({'source':'root-message-hash/DigestProjection.lean',
 'sha256':projection['source_sha256'],'successful_receipt':'root-message-hash/PROJECTION-CHECK.json',
 'receipt_sha256':sha(X/'root-message-hash/PROJECTION-CHECK.json'),'checked_declarations':3,
 'scope':'Same-word bit projection only, not source H_msg preservation or SHA hardness.'})
ordinary=read(X/'selected-promotion-review/message-hash-identification/FINAL-ORDINARY-SUBJECT-REVIEW.json')
composition=read(X/'selected-promotion-review/FINAL-COMPOSITION-SUBJECT-REVIEW.json')
assert all(ordinary['checks'].values()) and all(composition['checks'].values())
assert composition['subject_sha256']==sha(X/'FIXED-H-COMPOSITION.md')
successor_counts=read(X/'root-message-hash/SUCCESSOR-COUNTS.json')
assert list(successor_counts['graph_selector_bits'].values())==[55,55,21,41,42]
assert [r['dense_loss_log2'] for r in successor_counts['rows']]==[544]*8
assert [r['sparse_loss_log2'] for r in successor_counts['rows']]==[952,1054,1190,1224,1241,1292,1394,1632]
message_current=read(X/'selected-promotion-review/MESSAGE-GRAPH-INTEGRATION-REVIEW.json')
assert message_current['status']=='ACCEPTED_SCOPED_MESSAGE_GRAPH_FIXED_H_SYMBOLIC_CURRENT_INDEX'
assert all(message_current['checks'].values()) and message_current['accepted_evidence_items']==145
assert message_current['cumulative_supporting_checked_declarations']==47
assert message_current['new_source_game_checked_declarations']==0 and not message_current['whole_goal_complete']
for group in ('documents','promoted_artifacts','source_subjects','prior_review_receipts','backup_pins','preserved_artifacts','provenance_pins'):
    for name,digest in message_current[group].items():
        path=X/'root-docs-before-hidden-ud-pre'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for group in ('accepted_evidence_absolute_pins','external_absolute_pins'):
    for name,digest in message_current[group].items():assert sha(Path(name))==digest,name
docs += ['MESSAGE-GRAPH-PROMOTION.json','MESSAGE-HASH-ORDINARY-LIFT.md',
 'MESSAGE-HASH-PRIMITIVE-COMPONENT.md','FIXED-H-GRAPH-COMPONENT.md','FIXED-H-COMPOSITION.md',
 'root-message-hash/DigestProjection.lean','root-message-hash/PROJECTION-CHECK.json',
 'root-message-hash/SUCCESSOR-COUNTS.json','selected-promotion-review/FINAL-COMPOSITION-SUBJECT-REVIEW.json',
 'selected-promotion-review/MESSAGE-GRAPH-INTEGRATION-REVIEW.json']
hidden_pre=read(X/'HIDDEN-UD-PRE-PROMOTION.json')
assert hidden_pre['status']=='REVIEWED_MANUAL_ORDINARY_HIDDEN_UD_PRE_AND_SYMBOLIC_COMPOSITION_PROMOTED'
assert hidden_pre['cumulative_supporting_checked_declarations']==47
assert hidden_pre['new_source_game_checked_declarations']==hidden_pre['source_scalar_manuscript_changes']==0
assert hidden_pre['whole_goal_complete'] is False
assert hidden_pre['original_level_category_statement']=='not established'
assert hidden_pre['conditional_algebra_second_final_premise_now_satisfied'] is True
for group in ('documents','artifacts','receipt_pins'):
    for name,digest in hidden_pre[group].items():
        path=X/'root-docs-before-target-only-pre'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for name,digest in hidden_pre['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
for name,digest in hidden_pre['predecessor_documents'].items():
    assert sha(X/'root-docs-before-hidden-ud-pre'/name)==digest,name
hidden_field=read(X/'outside-field-check/interior-preimage/FINAL-SUBJECT-REVIEW.json')
hidden_second=read(X/'pre-start-second/interior-ud/FINAL-SUBJECT-REVIEW.json')
assert all(hidden_field['checks'].values()) and not hidden_field['material_correction_required']
assert hidden_second['review_status']=='ACCEPT_MANUAL_CONDITIONAL_ORDINARY_UD_PRE_INTERFACE'
assert hidden_field['subject_sha256']==hidden_second['subject_sha256']==sha(X/'FIXED-H-HIDDEN-PREDECESSORS.md')
assert hidden_field['new_source_game_declarations']==hidden_second['new_source_game_declarations']==0
assert hidden_second['toy_exit_code']==0 and hidden_second['toy_checks']==3072
hidden_algebra=read(X/'selected-promotion-review/FINAL-UD-PRE-COMPOSITION-REVIEW.json')
assert all(hidden_algebra['checks'].values())
assert hidden_algebra['subject_sha256']==sha(X/'FIXED-H-COMPOSITION-WITH-UD-PRE.md')
hidden_current=read(X/'selected-promotion-review/HIDDEN-UD-PRE-INTEGRATION-REVIEW.json')
assert all(hidden_current['checks'].values()) and hidden_current['accepted_evidence_items']==175
assert hidden_current['cumulative_supporting_checked_declarations']==47
assert hidden_current['new_source_game_checked_declarations']==0 and not hidden_current['whole_goal_complete']
for group in ('documents','promoted_artifacts','source_subjects','prior_review_receipts','backup_pins','preserved_artifacts','provenance_pins'):
    for name,digest in hidden_current[group].items():
        path=X/'root-docs-before-target-only-pre'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for group in ('accepted_evidence_absolute_pins','external_absolute_pins'):
    for name,digest in hidden_current[group].items():assert sha(Path(name))==digest,name
docs += ['HIDDEN-UD-PRE-PROMOTION.json','FIXED-H-HIDDEN-PREDECESSORS.md',
 'FIXED-H-COMPOSITION-WITH-UD-PRE.md','outside-field-check/interior-preimage/FINAL-SUBJECT-REVIEW.json',
 'pre-start-second/interior-ud/FINAL-SUBJECT-REVIEW.json',
 'selected-promotion-review/FINAL-UD-PRE-COMPOSITION-REVIEW.json',
 'selected-promotion-review/HIDDEN-UD-PRE-INTEGRATION-REVIEW.json']
target_pre=read(X/'TARGET-PRE-PROMOTION.json')
assert target_pre['status']=='REVIEWED_RANDOM_ORACLE_TARGET_ONLY_PRE_QUANTITATIVE_SUCCESSORS_PROMOTED'
assert len(target_pre['accepted_evidence_absolute_pins'])==228
assert target_pre['cumulative_supporting_checked_declarations']==47
assert target_pre['new_source_game_checked_declarations']==target_pre['source_scalar_manuscript_changes']==0
assert not target_pre['whole_goal_complete'] and target_pre['random_oracle_model_only']
for group in ('documents','artifacts','receipt_pins'):
    for name,digest in target_pre[group].items():
        path=X/'root-docs-before-polynomial-ud'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for name,digest in target_pre['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
for name,digest in target_pre['predecessor_documents'].items():
    assert sha(X/'root-docs-before-target-only-pre'/name)==digest,name
target_current=read(X/'selected-promotion-review/TARGET-PRE-INTEGRATION-REVIEW.json')
assert target_current['status']=='ACCEPTED_SCOPED_RANDOM_ORACLE_TARGET_ONLY_PRE_CURRENT_INDEX'
assert all(target_current['checks'].values()) and target_current['accepted_evidence_items']==228
assert target_current['cumulative_supporting_checked_declarations']==47
assert target_current['new_source_game_checked_declarations']==0 and not target_current['whole_goal_complete']
for group in ('documents','promoted_artifacts','source_subjects','prior_review_receipts','backup_pins','preserved_artifacts','provenance_pins'):
    for name,digest in target_current[group].items():
        path=X/'root-docs-before-polynomial-ud'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for group in ('accepted_evidence_absolute_pins','external_absolute_pins'):
    for name,digest in target_current[group].items():assert sha(Path(name))==digest,name
target_numeric=read(X/'root-target-only-ud/QUANTITATIVE-RESULTS.json')
assert target_numeric['source_sha256']==sha(X/'root-target-only-ud/quantitative.py')
assert len(target_numeric['rows'])==32
N=2**128;AH=7628143271608320;DH=20229886488608768
mu=Fraction(2*N-1,N*N)
slope=Fraction(12*AH,2**64)
assert target_numeric['marker_mu']==str(mu) and target_numeric['UD_slope']==str(slope)
for row in target_numeric['rows']:
    qa=2**row['log2_QA'];R=qa+1
    pre_bound=min(Fraction(1),(2*R+1)**2*mu)
    assert Fraction(int(row['PRE_numerator']),int(row['PRE_denominator']))==pre_bound
    assert Fraction(int(row['UD_source_numerator']),int(row['UD_source_denominator']))==slope*R
    assert Fraction(row['hidden_component_cap'])==min(Fraction(1),DH*pre_bound+slope*R)==1
    q=2**row['log2_q'];hm=hot if row['mode']=='prepared' else cold
    assert int(row['outside_query_cap'])==qa+hs+q*hm+3224+254
for row in target_numeric['constant_probability_crossings']:
    target=Fraction(row['target']);lo=row['QA_pass'];hi=row['QA_fail']
    assert hi==lo+1
    expr=lambda qa: DH*min(Fraction(1),(2*(qa+1)+1)**2*mu)+slope*(qa+1)
    assert Fraction(row['pass_value'])==expr(lo)<=target<expr(hi)==Fraction(row['fail_value'])
assert [(r['QA_pass'],r['QA_fail']) for r in target_numeric['constant_probability_crossings']]==[(99,100),(200,201)]
docs += ['TARGET-PRE-PROMOTION.json','TARGET-ONLY-UD-RO.md','SINGLE-TARGET-PRE-RO.md',
 'TARGET-ONLY-HIDDEN-BOUND.md','root-target-only-ud/quantitative.py',
 'root-target-only-ud/QUANTITATIVE-RESULTS.json','selected-promotion-review/TARGET-PRE-INTEGRATION-REVIEW.json']
poly_ud=read(X/'POLYNOMIAL-UD-PROMOTION.json')
assert poly_ud['status']=='REVIEWED_QUADRATIC_ONE_TARGET_UD_RO_COMPONENT_PROMOTED'
assert len(poly_ud['accepted_evidence_absolute_pins'])==268
assert poly_ud['cumulative_supporting_checked_declarations']==47
assert poly_ud['new_source_game_checked_declarations']==poly_ud['source_scalar_manuscript_changes']==0
assert not poly_ud['whole_goal_complete'] and poly_ud['same_joint_conditional_auxiliary_law_required']
for group in ('documents','artifacts','receipt_pins'):
    for name,digest in poly_ud[group].items():
        path=X/'root-docs-before-polynomial-private'/name if group=='documents' else X/name
        assert sha(path)==digest,(group,name)
for name,digest in poly_ud['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
for name,digest in poly_ud['predecessor_documents'].items():assert sha(X/'root-docs-before-polynomial-ud'/name)==digest,name
poly_field=read(X/'outside-field-check/ud-polynomial/FINAL-SUBJECT-REVIEW.json')
poly_sel=read(X/'selected-promotion-review/quantitative-goal-audit/single-ud-polynomial/FINAL-SUBJECT-REVIEW.json')
poly_status=read(X/'selected-promotion-review/quantitative-goal-audit/single-ud-polynomial/FINAL-STATUS-SUCCESSOR-REVIEW.json')
assert all(poly_field['checks'].values()) and all(poly_sel['checks'].values()) and all(poly_status['checks'].values())
assert poly_field['subject_sha256']==poly_status['subject_sha256']==sha(X/'QUANTUM-UD-POLYNOMIAL-RO.md')
assert poly_sel['subject_sha256']==poly_status['prior_subject_sha256']==sha(X/'root-docs-before-ud-status/QUANTUM-UD-POLYNOMIAL-RO.md')
poly_numeric=read(X/'root-ud-polynomial/CONTROLS.json')
assert poly_numeric['script_sha256']==sha(X/'root-ud-polynomial/controls.py')
assert len(poly_numeric['rows'])==32 and poly_numeric['polynomial_controls']==108
assert poly_numeric['marker_weight_checks']==17
def u_ud(Q):
    degree2=4*Q*Q
    return min(Fraction(1),Fraction(N-1,N)*Fraction(degree2,N-degree2)) if degree2<N else Fraction(1)
def poly_expr(qa):
    R=qa+1
    return DH*min(Fraction(1),(2*R+1)**2*mu)+AH*u_ud(R)
for row in poly_numeric['rows']:
    qa=2**row['log2_QA'];R=qa+1
    assert Fraction(row['UD_bound'])==u_ud(R)
    assert Fraction(row['uncapped_component'])==poly_expr(qa)
    assert Fraction(row['capped_component'])==min(Fraction(1),poly_expr(qa))
    hm=hot if row['mode']=='prepared' else cold
    assert int(row['outside_call_cap'])==qa+hs+2**row['log2_q']*hm+3224+254
for row in poly_numeric['uncapped_crossings']:
    lo=int(row['QA_pass']);hi=int(row['QA_fail']);target=Fraction(row['uncapped_target'])
    assert hi==lo+1
    assert Fraction(row['pass_value'])==poly_expr(lo)<=target<poly_expr(hi)==Fraction(row['fail_value'])
assert [(r['QA_pass'],r['QA_fail']) for r in poly_numeric['uncapped_crossings']]==[('29741080993','29741080994'),('42060240100','42060240101')]
poly_current=read(X/'pre-start-second/polynomial-ud-current-index/CURRENT-INDEX-REVIEW.json')
assert all(poly_current['checks'].values())
assert poly_current['current_accepted_pins']==268 and poly_current['prior_accepted_pins_retained_without_hash_changes']==228
assert poly_current['subject_sha256']==sha(X/'POLYNOMIAL-UD-PROMOTION.json')
for name,digest in poly_current['evidence'].items():
    assert sha(X/'pre-start-second/polynomial-ud-current-index'/name)==digest,name
docs += ['POLYNOMIAL-UD-PROMOTION.json','QUANTUM-UD-POLYNOMIAL-RO.md',
 'root-ud-polynomial/INDEPENDENT-FIRST.md','root-ud-polynomial/controls.py',
 'root-ud-polynomial/CONTROLS.json','outside-field-check/ud-polynomial/FINAL-SUBJECT-REVIEW.json',
 'selected-promotion-review/quantitative-goal-audit/single-ud-polynomial/FINAL-STATUS-SUCCESSOR-REVIEW.json']
poly_private=read(X/'POLYNOMIAL-PRIVATE-PROMOTION.json')
assert poly_private['status']=='REVIEWED_COMPLETE_FINITE_QROM_POLYNOMIAL_PRIVATE_SOURCE_SUCCESSOR_PROMOTED'
assert len(poly_private['accepted_evidence_absolute_pins'])==321
assert poly_private['independent_complete_numeric_rows']==16
assert poly_private['probability_comparisons']==336 and poly_private['new_threshold_pairs']==32
assert poly_private['cumulative_supporting_checked_declarations']==47
assert poly_private['new_source_game_checked_declarations']==poly_private['source_scalar_manuscript_changes']==0
assert not poly_private['whole_goal_complete'] and not poly_private['classical_joint_candidate_promoted']
for group in ('documents','artifacts','receipt_pins'):
    for name,digest in poly_private[group].items():
        base=X/'root-docs-before-classical-joint' if group=='documents' else X
        assert sha(base/name)==digest,(group,name)
for name,digest in poly_private['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
for name,digest in poly_private['predecessor_documents'].items():assert sha(X/'root-docs-before-polynomial-private'/name)==digest,name
poly_full_review=read(X/'pre-start-second/polynomial-private-composition/FINAL-SUBJECT-REVIEW.json')
assert all(poly_full_review['checks'].values()) and not poly_full_review['whole_goal_complete']
assert poly_full_review['subject_sha256']==sha(X/'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md')
assert poly_full_review['root_dataset_sha256']==sha(X/'root-polynomial-private-composition/RESULTS.json')
assert poly_full_review['root_calculator_sha256']==sha(X/'root-polynomial-private-composition/bounds.py')
for name,digest in poly_full_review['private_hop_chain'].items():assert sha(X/name)==digest,name
new_full_rows=read(X/'root-polynomial-private-composition/RESULTS.json')
assert len(new_full_rows['rows'])==16 and sum(r['new_wins_minimum'] for r in new_full_rows['rows'])==6
for name,digest in new_full_rows['input_pins'].items():assert sha(X/name)==digest,name
for row in new_full_rows['rows']:
    assert row['category']=='not established'
    if row['log2_Q']==64:assert row['probabilities']['best_total']=='1.0'
threshold_cert=read(X/'outside-field-check/polynomial-query-thresholds/FINAL-CERTIFICATE.json')
threshold_data=read(X/'outside-field-check/polynomial-query-thresholds/NEW-CERTIFICATES.json')
threshold_root=read(X/'root-polynomial-private-composition/THRESHOLD-CROSSCHECK.json')
assert threshold_cert['subject_sha256']==sha(X/'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md')
assert threshold_root['status']=='PASS_32_NEW_COMPLETE_ENVELOPE_ADJACENT_PAIRS_64_ENDPOINTS'
assert threshold_root['certificate_sha256']==sha(X/'outside-field-check/polynomial-query-thresholds/NEW-CERTIFICATES.json')
assert threshold_root['script_sha256']==sha(X/'root-polynomial-private-composition/check_thresholds.py')
assert len(threshold_data['rows'])==32 and len(threshold_cert['best_rows'])==8
for row in threshold_data['rows']:
    assert int(row['Q_fail'])==int(row['Q_pass'])+1
    frac=lambda pair:Fraction(*map(int,pair))
    assert frac(row['pass_interval']['upper'])<=Fraction(1,2)<frac(row['fail_interval']['lower'])
poly_private_current=read(X/'pre-start-second/polynomial-private-current-index/CURRENT-INDEX-REVIEW.json')
assert all(poly_private_current['checks'].values())
assert poly_private_current['subject_sha256']==sha(X/'POLYNOMIAL-PRIVATE-PROMOTION.json')
assert poly_private_current['current_accepted_pins']==321
for name,digest in poly_private_current['evidence'].items():
    assert sha(X/'pre-start-second/polynomial-private-current-index'/name)==digest,name
docs += ['POLYNOMIAL-PRIVATE-PROMOTION.json','SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md',
 'SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md','QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md',
 'root-polynomial-private-composition/bounds.py','root-polynomial-private-composition/RESULTS.json',
 'root-polynomial-private-composition/THRESHOLD-CROSSCHECK.json',
 'pre-start-second/polynomial-private-composition/FINAL-SUBJECT-REVIEW.json',
 'outside-field-check/polynomial-query-thresholds/FINAL-CERTIFICATE.json']
joint=read(X/'CLASSICAL-JOINT-PROMOTION.json')
assert joint['status']=='REVIEWED_COMPLETE_CLASSICAL_JOINT_SOURCE_SUCCESSOR_PROMOTED'
assert len(joint['accepted_evidence_absolute_pins'])==357
assert joint['classical_new_rows']==24 and joint['new_half_success_crossings']==8
assert joint['QH128_all_cap_one'] and joint['classical_joint_candidate_promoted']
assert joint['cumulative_supporting_checked_declarations']==47
assert joint['new_source_game_checked_declarations']==joint['source_scalar_manuscript_changes']==0
assert not joint['whole_goal_complete'] and joint['original_level_category_statement']=='not established'
for group in ('documents','artifacts','receipt_pins'):
    for name,digest in joint[group].items():
        path=X/'root-docs-before-uniform-classical'/name if group=='documents' and (X/'UNIFORM-CLASSICAL-PROMOTION.json').exists() else X/name
        assert sha(path)==digest,(group,name)
for name,digest in joint['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
for name,digest in joint['predecessor_documents'].items():
    assert sha(X/'root-docs-before-classical-joint'/name)==digest,name
joint_root=read(X/'root-classical-joint/ROOT-JOINT-CHECK.json')
assert joint_root['status']=='PASS24_CLASSICAL_JOINT_ROWS_AND8_EXACT_ADJACENT_CROSSINGS'
assert joint_root['script_sha256']==sha(X/'root-classical-joint/check.py')
assert joint_root['subject_sha256']==sha(X/'CLASSICAL-JOINT-RO-THEOREM.md')
assert len(joint_root['rows'])==24
assert sum(r['QH_exponent']==128 and r['exact_cap_one'] for r in joint_root['rows'])==8
for receipt in ('selected-promotion-review/joint-classical-review/FINAL-SUBJECT-REVIEW.json',
                'pre-start-second/classical-joint-root-crosscheck/FINAL-SUBJECT-REVIEW.json'):
    review=read(X/receipt)
    assert all(review['checks'].values())
    assert review['subject_sha256']==sha(X/'CLASSICAL-JOINT-RO-THEOREM.md')
joint_current=read(X/'pre-start-second/classical-joint-current-index/CURRENT-INDEX-REVIEW.json')
assert all(joint_current['checks'].values())
assert joint_current['subject_sha256']==sha(X/'CLASSICAL-JOINT-PROMOTION.json')
assert joint_current['current_evidence_pins']==357
assert joint_current['prior_evidence_pins_retained_without_changes']==321
for name,digest in joint_current['current_documents'].items():
    path=X/'root-docs-before-uniform-classical'/name if (X/'UNIFORM-CLASSICAL-PROMOTION.json').exists() else X/name
    assert sha(path)==digest,name
for name,digest in joint_current['evidence'].items():
    assert sha(X/'pre-start-second/classical-joint-current-index'/name)==digest,name
docs += ['CLASSICAL-JOINT-PROMOTION.json','CLASSICAL-JOINT-RO-THEOREM.md',
 'root-classical-joint/check.py','root-classical-joint/ROOT-JOINT-CHECK.json',
 'pre-start-second/classical-joint-current-index/CURRENT-INDEX-REVIEW.json']
uniform=read(X/'UNIFORM-CLASSICAL-PROMOTION.json')
assert uniform['status']=='REVIEWED_GUARDED_PARAMETER_UNIFORM_CLASSICAL_SUCCESSOR_PROMOTED'
assert uniform['predecessor_promotion_sha256']==sha(X/'CLASSICAL-JOINT-PROMOTION.json')
assert uniform['subject_sha256']==sha(X/'PARAMETER-UNIFORM-CLASSICAL-THEOREM.md')
assert (uniform['independent_rows'],uniform['root_rational_rows'])==(144,48)
assert not uniform['whole_goal_complete'] and not uniform['retuned_QROM_established']
assert uniform['new_source_or_manuscript_edits']==uniform['new_whole_source_game_checked_declarations']==0
for name,digest in uniform['accepted_evidence_absolute_pins'].items():assert sha(Path(name))==digest,name
for name,digest in uniform['predecessor_documents'].items():assert sha(X/'root-docs-before-uniform-classical'/name)==digest,name
for name,digest in uniform['documents'].items():assert sha(X/name)==digest,name
for name,digest in uniform['receipt_pins'].items():assert sha(X/name)==digest,name
docs += ['UNIFORM-CLASSICAL-PROMOTION.json','PARAMETER-UNIFORM-CLASSICAL-THEOREM.md',
 'root-parameter-uniform-classical/uniform_bounds.py','root-parameter-uniform-classical/ROOT-CROSSCHECK.json',
 'root-parameter-uniform-classical/POSITIVE-CERTIFICATE.md']
record={
 'outcome':'REVIEWED_FINITE_RO_AND_QROM_MODEL_BOUNDS_FULL_SECURITY_GOAL_ACTIVE',
 'requirements_complete':False,
 'complete_model_advantage_theorems':{'classical_RO':'reviewed manual','finite_QROM':'reviewed manual, two independent source-first readers'},
 'original_level_category_statement':'not established',
 'original_scope_successor_review':scope_review['outcome'],
 'numeric_outputs':outputs,
 'quantum_crosscheck':{'sha256':sha(X/'quantum-composition-numeric/ROOT-CROSSCHECK.json'),
    'rows':16,'probability_checks':176,'exponent_checks':112},
 'refined_quantum_crosscheck':{'sha256':sha(X/'quantum-private-rare-numeric/ROOT-REFINED-CROSSCHECK.json'),
    'rows':16,'numeric_fields':96,'exponents':64,'strongest_reviewed_exponent_q40_Qq32':57.6833598693088},
 'classical_current_recheck':{'sha256':sha(X/'root-current-classical-recheck/ROOT-CROSSCHECK.json'),
    'rows':16,'independence':'Root reexecution against previously independent interval data; not a new blind derivation.'},
 'mechanized_components':checks,
 'query_resource_thresholds':{'adjacent_crossings':32,'rational_endpoint_checks':64,
    'independent_certificate_sha256':sha(X/'query-resource-independent/THRESHOLDS.json'),
    'root_check_sha256':sha(X/'query-resource-root/CHECK.json'),
    'second_reader_sha256':sha(X/'query-resource-formal/SECOND_READER.md'),
    'criterion':'Sufficient model probability bound <=1/2, not security category'},
 'exact_public_payload':{'bytes':75497456,'status':'REVIEWED_DIRECT_VIEW_EXTENSION_SAME_SUFFICIENT_RO_QROM_BOUNDS',
    'review_sha256':sha(X/'cache-payload-source/REVIEW.json'),
    'control_worlds':524288,'controls_are_not_full_source_or_quantum_mechanization':True,
    'whole_seed_fixture_excluded':True,'efficient_external_pk_simulator':False},
 'private_challenge_programs':{'status':'REVIEWED_EXPLICIT_CLASSICAL_ROM_RELATIVE_JOINT_ACCESS_ADAPTERS',
    'review_sha256':sha(X/'cache-payload-source/PRIVATE-CHALLENGE-REVIEW.json'),
    'eight_q_resource_rows':8,'conventional_independent_PRF_established':False},
 'payload_private_current_index_review':{'status':integration['verdict'],
    'receipt_sha256':sha(X/'cache-payload-source/INTEGRATION-FINAL-REVIEW.json')},
 'selected_graph_and_changed_child':{'status':selected['verdict'],
    'receipt_sha256':sha(X/'selected-promotion-review/INTEGRATION-REVIEW.json'),
    'selector_loss':2**56,'conditional_nonzero_S_only':True,'only_final_classical_witness':True,
    'largest_cone_public_calls':8560574462,'final_route_public_calls':8560653547,
    'new_machine_checked_declarations':0,'conventional_SPR_TCR_established':False,
    'D7_changed_child_refinement_not_new_scalar_bound':True},
 'classical_hidden_input_PRE_program':{'status':pre['verdict'],
    'receipt_sha256':sha(X/'selected-promotion-review/PRE-INTEGRATION-REVIEW.json'),
    'protected_coordinates':20229886488608768,'selector_loss':2**55,
    'selected_handle_cap':'Q_H+1','extra_preparation_hashes':254,
    'additional_node_payload_bytes':4096,'extra_memory_excludes_all_source_storage':True,
    'full256_image_challenge':True,'outside_functions_locally_simulated':True,
    'coherent_PRE_embedding_established':False,'conventional_PRE_established':False,
    'unchanged_direct_probability_bounds':True,'new_machine_checked_declarations':0,
    'independent_resource_q_columns':8,'third_reader_control_worlds':512},
 'finite_coherent_hidden_input_PRE_program':{'status':qpre['verdict'],
    'receipt_sha256':sha(X/'selected-promotion-review/QPRE-INTEGRATION-REVIEW.json'),
    'D_interior':1016949404336128,'selector_loss':2**55,
    'probability_envelope':'min(1,(sqrt(2^55*p_PRE)+2Q_q*sqrt(D_interior/2^128))^2)',
    'raw_vector_cap':2,'selected_coherent_cap':'Q_q','selected_final_classical_cap':1,
    'total_coherent_handle_cap':'2Q_q','eager_initialization_bits':'256 V_b',
    'eager_storage_bytes':'32 V_b','eager_initialization_writes':'O(32 V_b)',
    'efficient_outside_established':False,'conventional_PRE_established':False,
    'supporting_checked_declarations_added':7,'whole_source_game_checked_declarations_added':0,
    'floating_channel_controls':'6 cases x1024 worlds plus3072 final-first branches, tolerance1e-12',
    'wrong_missing_sqrt_L_expansion_rejected':True,'direct_numeric_bounds_unchanged':True},
 'easycrypt_live_environment':{'read_only_config_command':'wsl -d Ubuntu-24.04 -- /root/.opam/ec/bin/easycrypt config',
    'observed_git_hash':'r2026.07-1-g87b6f8b','configured_selected_prover':'Z3@4.8.12',
    'version_flag':'--version unsupported; identity read from successful config command',
    'new_actual_check_receipt':'private-challenge-program/EASYCRYPT-CHECK.json'},
 'canonical_type7_row_program':{'status':t7['verdict'],
    'receipt_sha256':sha(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.json'),
    'actual_rows':2269959421952,'selector_loss':2**42,'C_public_max':17392,'C_F_distinct_max':8704,
    'target_challenge_preprocessing_cap':2**32,'independent_resource_q_columns':8,
    'new_checked_declarations':0,'full_source_game_checked_declarations':0,
    'direct_probability_numerics_unchanged':True,'conventional_S_TCR_established':False},
 'bounded_query_outside_simulator':{'status':outside['verdict'],
    'receipt_sha256':sha(X/'outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json'),
    'outside_success_probability_loss':0,'replacement_scope':'B-only PRE and Row; original SOURCE law/theorems unchanged',
    'all_honest_outside_calls_included':True,'root_resource_profiles':64,'inherited_q_rows':8,
    'deterministic_tower_field':True,'hidden_same_coefficients_each_eval':True,
    'family_degree_cap':'k=min(max(1,2T),V_b)','field_bits_example_b598':8192,
    'new_checked_declarations':0,'whole_source_game_new_checked_declarations':0,
    'uniform_circuit_generation_charged':True,'practical_or_category_claim':False,
    'author_unfinished_packet_relied_upon':False},
 'fixed_public_hash_canonical_collection_component':{
    'status':standard['status'],'promotion_sha256':sha(X/'STANDARD-CANONICAL-PROMOTION.json'),
    'model':'HJ[h], separate from HJ[O]','inequality':'nonzero-seed contribution <=2^42 SuccProp4+2^21 SuccProp8',
    'hardness':'ASSUMED named canonical-first bounded collection property, not evaluated',
    'new_supporting_declarations':4,'cumulative_supporting_declarations':44,
    'new_whole_source_game_declarations':0,'fixed_sha_capacity_category':'not established'},
 'ordinary_fixed_public_hash_private_adapters':{
    'status':'EXACT_ORDINARY_PUBLIC_PARAMETER_PRIVATE_HOP_IDENTITIES_REVIEWED',
    'subject_review_sha256':sha(X/'outside-field-check/public-h-private-review/FINAL-SUBJECT-REVIEW.json'),
    'private_hardness':'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
    'private_f_output_bits':128,'private_g_output_bits':128,'public_h_output_bits':256,
    'classical_private_queries_quantum_public_computation':True,'seed_zero_aliases_retained':True,
    'signed_parameter_averaging_not_average_absolute_gap':True,
    'source_private_query_cap':'min(N_D,2181038080+q U_mode); Eval_g<=q',
    'RO_numeric_transfer':False,'fixed_h_full_H_msg_and_public_graph_bound':'OPEN'},
 'primitive_successors_current_index':{
    'status':primitive_current['status'],'receipt_sha256':sha(X/'selected-promotion-review/PRIMITIVE-INTEGRATION-REVIEW.json'),
    'accepted_evidence_pins_checked':98,'manuscript_source_numeric_changes':0},
 'restricted_canonical_linked_RO_QROM_component':{
    'status':row_review['status'],'final_receipt_sha256':sha(X/'restricted-row-third-review/FINAL-SUBJECT-REVIEW.json'),
    'one_query_completion_bound':'min(1,8*(M+1)^2/N)',
    'new_extractor_M':'Q','old_adapter_M':'Q+1',
    'source_nonzero_contribution':'min(1,(1-1/N)*(2^42*tau4+2^21*tau8)*min(1,8*(Q+1)^2/N))',
    'first_literal_BE32_and_bottom_preserved':True,'whole_runtime_separate_from_mark_queries':True,
    'root_exact_basis_controls':8192,'independent_exact_mixed_region_basis_controls':8192,
    'independent_coherent_controls':256,'terminated_optional_run_counted_as_evidence':False,
    'existing_stronger_direct_D7_bound_and_full_numeric_tables_unchanged':True,
    'fixed_SHA_or_category_certificate':False,'new_checked_whole_game_declarations':0},
 'new_dynamic_root_control':{'sha256':sha(X/'root-dynamic-hidden-controls/CHECKS.json'),'worlds':hidden['worlds']},
 'preservation':preservation,
 'artifacts':{name:sha(X/name) for name in docs},
 'remaining':'Original adequate level/category/capacity remains unestablished. Ordinary fixed-public-h private PRF hop interfaces are now closed, but their family hardness is assumed and fixed-h ideal-private H_msg/adaptive-coverage/public-graph bounds remain OPEN. Conditional canonical collection identification and a restricted full-RO one-query target component are reviewed; they do not turn fixed h into a random oracle or import unproved generic collection estimates. Standard graph/PRE properties and complete quantitative fixed-h composition remain unfinished. External pk-only cache simulation and optional full SOURCE-classifier/compiler/channel verification are distinct stronger assurance, not added completion prerequisites.'}
record['fixed_h_message_graph_symbolic_successors']={
 'status':message['status'],'promotion_sha256':sha(X/'MESSAGE-GRAPH-PROMOTION.json'),
 'accepted_pins_checked':len(message['accepted_evidence_absolute_pins']),
 'cumulative_supporting_declarations':47,'new_whole_source_game_declarations':0,
 'ordinary_dense_ITSR_loss_log2':544,'graph_NEW_selector_bits':[55,55,21,41,42],
 'same_public_h_symbolic_composition':True,'epsilon_H':'OPEN',
 'ordinary_primitive_hardness':'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
 'original_level_category_statement':'not established'}
record['ordinary_hidden_predecessor_successor']={
 'status':hidden_pre['status'],'promotion_sha256':sha(X/'HIDDEN-UD-PRE-PROMOTION.json'),
 'accepted_pins_checked':len(hidden_pre['accepted_evidence_absolute_pins']),
 'manual_interface':'ordinary one-target PRE plus254 ordinary one-target UD hops',
 'selector_bits':55,'completed_response_gate_and_image_superset':True,
 'unchanged_full_public_h_quantum_A':True,'two_final_subject_review_receipts':True,
 'conditional_algebra_second_final_premise_now_satisfied':True,
 'new_source_game_kernel_declarations':0,'fixed_h_hardness_or_category_certificate':False}
record['ordinary_hidden_predecessor_successor']['current_index_review_sha256']=sha(X/'selected-promotion-review/HIDDEN-UD-PRE-INTEGRATION-REVIEW.json')
record['remaining']='Actual fixed-h primitive hardness values and adequate level/category/capacity remain unestablished. Exact private hops, ordinary loss-aware ITSR, graph collection TCR, canonical type7 and hidden predecessor UD/PRE components now have reviewed symbolic composition. The formerly unnamed epsilon_H interface is resolved by explicit ordinary programs, while their quantitative hardness remains ASSUMED/unevaluated. No fixed-h hardness is inferred from the unchanged RO/QROM model numerics. Whole-source/compiler/game mechanization is additional assurance, not a substituted goal.'
record['target_only_random_oracle_successor']={
 'status':target_current['status'],'promotion_sha256':sha(X/'TARGET-PRE-PROMOTION.json'),
 'current_index_review_sha256':sha(X/'selected-promotion-review/TARGET-PRE-INTEGRATION-REVIEW.json'),
 'accepted_pins_checked':228,'no_prequery_opaque_X_independent_ghost_auxiliary_caller_reviewed':True,
 'one_target_PRE':'min(1,(2Q+1)^2*(2/N-1/N^2))','ordinary_remote_queries':'Q_A+1',
 'honest_outside_work_charged_separately':True,'activation_count_sum':AH,
 'explicit_conservative_component_rows':32,'all_caps_one':True,
 'uncapped_adjacent_crossings':[[99,100],[200,201]],
 'old_stronger_direct_source_bounds_preserved':True,'fixed_SHA_or_category_certificate':False,
 'new_source_game_checked_declarations':0}
record['remaining']='Adequate original classical level/category/capacity and successful minimal parameter repair remain unestablished. Explicit finite RO/QROM source bounds and ordinary symbolic adapters are reviewed; the latest target-only random-RO PRE constant and caller premises close a component interface. They do not provide fixed-SHA hardness or replace the stronger historical direct source bounds. Whole-source/compiler/game mechanization and unconditional fixed-SHA hardness are not added completion prerequisites.'
record['quadratic_one_target_UD_successor']={
 'status':poly_ud['status'],'promotion_sha256':sha(X/'POLYNOMIAL-UD-PROMOTION.json'),
 'accepted_pins_checked':268,'two_exact_final_subject_reviews':True,
 'bound':'min(1,(1-1/N)*4Q^2/(N-4Q^2)) if4Q^2<N, else1',
 'same_joint_conditional_auxiliary_law_required':True,'remote_source_call_cap':'Q_A+1',
 'exact_rational_component_rows':32,'QA32_component_display':0.01042740466035393,
 'root_polynomial_controls':108,'root_marker_checks':17,
 'uncapped_crossings':[[29741080993,29741080994],[42060240100,42060240101]],
 'old_stronger_direct_source_bounds_preserved':True,'whole_source_game_new_declarations':0,
 'fixed_SHA_or_category_certificate':False,'current_document_independent_index':poly_current['status'],
 'current_index_review_sha256':sha(X/'pre-start-second/polynomial-ud-current-index/CURRENT-INDEX-REVIEW.json')}
record['remaining']='The new quadratic ordinary one-target UD component and its source caller are manually reviewed and exact arithmetic checked. Original adequate level/category/capacity and successful smallest parameter repair remain unestablished. A source-specific private-K decision lemma has a separate final review, but is not composed into historical full bounds; private-P mixed-query and simultaneous classical candidates require independent source checks. No fixed-SHA hardness, efficient query-to-AES bridge or compiler/game mechanization is inferred.'
record['complete_polynomial_private_source_successor']={
 'status':poly_private['status'],'promotion_sha256':sha(X/'POLYNOMIAL-PRIVATE-PROMOTION.json'),
 'accepted_pins_checked':321,'source_full_review_sha256':sha(X/'pre-start-second/polynomial-private-composition/FINAL-SUBJECT-REVIEW.json'),
 'independent_new_full_numeric_rows':16,'probability_comparisons':336,'strictly_improved_rows':6,
 'q40_Q32_probability_bound_exponent':58.09317887983897,
 'new_certified_query_crossings':32,'root_endpoint_checks':64,
 'new_q40_half_success_Qpass':'1681654180826527564',
 'same_source_Win_bit_one_sided_P_one_seed_zero':True,
 'honest_cache_probability_query_loss':[0,0],
 'old_full_scalar_cells_preserved':48,'old_query_crossings_preserved':32,
 'fixed_SHA_level_category_capacity_repair':'not established',
 'supporting_checked_declarations':47,'whole_source_game_new_checked_declarations':0,
 'independent_current_document_index':poly_private_current['status'],
 'current_index_review_sha256':sha(X/'pre-start-second/polynomial-private-current-index/CURRENT-INDEX-REVIEW.json')}
record['complete_classical_joint_source_successor']={
 'status':joint['status'],'promotion_sha256':sha(X/'CLASSICAL-JOINT-PROMOTION.json'),
 'accepted_pins_checked':357,'same_source_REAL_and_joint_safe_surface':True,
 'query_coefficient':3,'honest_request_coefficient':2,'averaged_constant':6242,
 'independent_complete_rows':24,'required_QH128_rows_cap_one':8,
 'new_half_success_query_crossings':8,
 'q40_QH64_probability_bound_exponent':62.39484059815322,
 'q40_half_success_Qpass':'55925302073878813864583541683133229382',
 'root_check_sha256':sha(X/'root-classical-joint/ROOT-JOINT-CHECK.json'),
 'independent_current_index_sha256':sha(X/'pre-start-second/classical-joint-current-index/CURRENT-INDEX-REVIEW.json'),
 'old_full_scalar_cells_preserved':48,'old_query_crossings_preserved':32,
 'supporting_checked_declarations':47,'new_whole_source_game_checked_declarations':0}
record['remaining']='Complete finite-QROM private-polynomial and simultaneous classical joint source bounds now have final source and numerical reviews. The current357-pin cut preserves the previous321-pin quantum cut,48 old scalar cells,32 old query crossings and165 frozen files. Adequate original level/category/capacity and successful smallest parameter repair remain not established; all required2^128 classical-query and2^64 quantum-query rows cap1. No vacuous sufficient estimate proves an attack or repair impossibility. No source/paper/timing/old-scalar edits, fixed-SHA hardness certificate or efficient query-to-AES gate bridge are inferred.'
record['guarded_parameter_uniform_classical_successor']={
 'status':uniform['status'],'promotion_sha256':sha(X/'UNIFORM-CLASSICAL-PROMOTION.json'),
 'accepted_pins':len(uniform['accepted_evidence_absolute_pins']),
 'independent_rows':144,'root_rational_rows':48,'baseline_old_rows_preserved':24,'baseline_old_crossings_preserved':8,
 'new_source_manuscript_or_whole_game_declarations':0,'retuned_QROM_or_original_adequacy':'not established'}
record['remaining']='The guarded classical source-schema extension and exact positive certificates are reviewed, including all eight requested signing caps. The height63 illustration gives raw-query half-success certificates at Q2^125, but no original128/category/capacity or smallest repair is established. Retuned QROM requires its own uniform source proof. All historical source-model results and frozen material are preserved; a failed upper gate does not prove an attack.'
(X/'VALIDATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'outcome':record['outcome'],'model_total_cells_checked':48,'query_resource_crossings':32,'frozen_files':preservation['frozen_files'],'mechanized_component_declarations':sum(c['checked_declarations'] for c in checks),'exact_payload_extension':'reviewed','private_ROM_programs':'reviewed','localized_graph_and_changed_child':'reviewed','classical_PRE_program':'reviewed','finite_coherent_PRE_program':'reviewed','PRE_resource_columns':8}))

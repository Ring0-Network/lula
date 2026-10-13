"""Pin-check manually reviewed classical PRE promotion and cumulative index chain."""
from pathlib import Path
import hashlib,json
X=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
p=read(X/'CLASSICAL-PRE-PROMOTION.json')
selected=read(OUT/'INTEGRATION-REVIEW.json')
payload=read(X/'cache-payload-source/INTEGRATION-FINAL-REVIEW.json')
pre=read(OUT/'PRE-COMBINED-REVIEW.json')
for group in ('subject_pins','current_documents','promoted_artifacts','preserved_artifacts'):
    for n,h in p[group].items():assert sha(X/n)==h,(group,n)
for n,h in selected['documents'].items():
    assert sha(X/'root-docs-before-chain-pre'/n)==h,n
    assert p['prior_documents'][n]==h,n
for n,h in selected['promoted_artifacts'].items():assert sha(X/n)==h,n
for n,h in selected['subject_pins'].items():assert sha(X/n)==h,n
for n,h in selected['prior_review_receipts'].items():assert sha(X/n)==h,n
for n,h in payload['documents'].items():assert sha(X/'root-docs-before-selected-graph'/n)==h,n
for group in ('promoted_artifacts','prior_review_receipts'):
    for n,h in payload[group].items():assert sha(X/n)==h,n
for n,h in pre['subject_pins'].items():assert sha(X/n)==h,n
for n,h in pre['own_pins'].items():assert sha(OUT/n)==h,n
assert p['subject_review_sha256']==sha(X/'chain-pre-independent/COMBINED-REVIEW.json')
assert p['author_provenance_sha256']==sha(X/'chain-pre-adapter/PROVENANCE.json')
text=(X/'CLASSICAL-PRE-REDUCTION.md').read_text(encoding='utf8')
base=(X/'chain-pre-adapter/INDEPENDENT_DERIVATION.md').read_text(encoding='utf8')
assert base.replace('**PROVED — manual, independent first derivation; awaiting a second reader.**','**PROVED — manual source-relative derivation, accepted by an independent source-first second reader.**').strip() in text
fors=(X/'chain-pre-adapter/FORS-LOCALIZED-SUCCESSOR.md').read_text(encoding='utf8')
assert fors.strip() in text
for phrase in ('20,229,886,488,608,768','Q_H+1','full256 equality','unknown X','outside','fixed55-bit','zero'):
    assert phrase in text,phrase
assert 'No new machine-checked source declaration' in text
assert 'fullimage target' in text
assert 'prefix-image/lower-limb variant is an unpromoted proposal' in text
assert p['new_machine_checked_declarations']==0 and p['manuscript_edits']==0
assert p['full256_image_predicate'] and p['coherent_cut']=='OPEN' and p['conventional_PRE']=='OPEN'
controls=read(OUT/'PRE-CONTROL-RESULTS.json')
assert controls['script_sha256']==sha(OUT/'PRE-positive-control.py')
assert controls['ordinary_worlds']==512 and len(controls['q_resource_rows'])==8
assert all(r['selected_first_hit_couplings']==r['source_events'] for r in controls['prekey_atomic_disclosure_postkey_policies'])
# Verify the explicit source pin supplied by the reviewed subject.
release=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(release)==pre['source_sha256']
receipt={
 'verdict':'ACCEPT_CORRECTED_CLASSICAL_PRE_CURRENT_INDEX',
 'documents':p['current_documents'],
 'promoted_artifacts':p['promoted_artifacts'],
 'subject_pins':p['subject_pins'],
 'promotion_sha256':sha(X/'CLASSICAL-PRE-PROMOTION.json'),
 'prior_review_receipts':{
  'selected-promotion-review/INTEGRATION-REVIEW.json':sha(OUT/'INTEGRATION-REVIEW.json'),
  'cache-payload-source/INTEGRATION-FINAL-REVIEW.json':sha(X/'cache-payload-source/INTEGRATION-FINAL-REVIEW.json'),
  'selected-promotion-review/PRE-COMBINED-REVIEW.json':sha(OUT/'PRE-COMBINED-REVIEW.json'),
  'chain-pre-independent/COMBINED-REVIEW.json':sha(X/'chain-pre-independent/COMBINED-REVIEW.json')},
 'prior_doc_backups':{
  **{f'root-docs-before-chain-pre/{n}':h for n,h in selected['documents'].items()},
  **{f'root-docs-before-selected-graph/{n}':h for n,h in payload['documents'].items()}},
 'preserved_artifacts':p['preserved_artifacts'],
 'controls':{'selected-promotion-review/PRE-positive-control.py':sha(OUT/'PRE-positive-control.py'),
             'selected-promotion-review/PRE-CONTROL-RESULTS.json':sha(OUT/'PRE-CONTROL-RESULTS.json')},
 'source_sha256':sha(release),
 'manual_review_sha256':sha(OUT/'PRE-INTEGRATION-REVIEW.md'),
 'checker_sha256':sha(Path(__file__)),
 'checks':{
  'exact_combined55bit_namespace_and_WOTS50_separate':True,
  'selected_QH_plus_1_and_local_source_resource_caps':True,
  'full256_image_target_not_prefix_only':True,
  'local_outside_functions_not_opaque_RawOut':True,
  'unknown_predecessor_never_emitted_selected_FORS_secret_not_transmitted':True,
  'stopped_first_event_inequality_preserves_observer_prekey_partiality':True,
  'old_selected_integration_docs_match_chain_PRE_backup':True,
  'old_payload_integration_docs_match_prior_selected_backup':True,
  'scalars_calculators_graph_and_extraction_artifacts_unchanged':True,
  'coherent_conventional_category_capacity_still_open':True,
  'zero_new_checked_declarations':True,
  'whole_goal_remains_active':True},
 'new_machine_checked_declarations':0,
 'security_level_category':'not established',
 'whole_goal_complete':False}
(OUT/'PRE-INTEGRATION-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'verdict':receipt['verdict'],'documents':len(receipt['documents']),
 'checks':len(receipt['checks']),'receipt_sha256':sha(OUT/'PRE-INTEGRATION-REVIEW.json')}))

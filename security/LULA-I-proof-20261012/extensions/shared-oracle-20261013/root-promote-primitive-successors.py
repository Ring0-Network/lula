from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda n:json.loads((X/n).read_text(encoding='utf8'))
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
prior=load('selected-promotion-review/STANDARD-INTEGRATION-REVIEW.json')
assert prior['status']=='ACCEPTED_SCOPED_STANDARD_CANONICAL_CURRENT_INDEX'
assert all(prior['checks'].values())
private=load('outside-field-check/public-h-private-review/REVIEW.json')
pfinal=load('outside-field-check/public-h-private-review/FINAL-SUBJECT-REVIEW.json')
row=load('restricted-row-third-review/FINAL-SUBJECT-REVIEW.json')
base=load('restricted-row-third-review/REVIEW-RECEIPT.json')
one=load('restricted-row-third-review/ONE-QUERY-RECEIPT.json')
second=load('selected-promotion-review/standard-identification/restricted-row-qrom/ONE-QUERY-REVIEW.json')
assert private['verdict']=='ACCEPT_EXACT_ORDINARY_PUBLIC_PARAMETER_PRIVATE_PRF_ADAPTER_IDENTITIES_WITH_CHARGED_SOURCE_RELATIVE_RESOURCES'
assert all(private['checks'].values()) and all(v==0 for v in private['control_exits'].values())
assert pfinal['verdict']=='ACCEPT_FAITHFUL_FINAL_FIXED_H_PRIVATE_PRF_ADAPTER_SUBJECT'
assert all(pfinal['checks'].values())
assert row['status']=='ACCEPTED_FINAL_MANUAL_RESTRICTED_CANONICAL_QROM_COMPONENT'
assert base['controls_exit_code']==one['controls_exit_code']==0
assert second['status']=='ACCEPTED_MANUAL_ONE_QUERY_COMPLETION_AND_RESTRICTED_RO_CONSEQUENCE'
assert all(second['checks'].values())
pins={}
def add(n,h):
    p=Path(n)
    if not p.is_absolute():p=X/p
    assert sha(p)==h,str(p)
    pins[str(p)]=h
for group in ['documents','promoted_artifacts','source_subjects','backup_pins','preserved_artifacts','control_pins','prior_review_receipts','provenance_pins']:
    for n,h in prior[group].items():add(n,h)
for n,h in private['subject_pins'].items():add(n,h)
for n,h in private['own_control_pins'].items():add('outside-field-check/public-h-private-review/'+n,h)
add('outside-field-check/public-h-private-review/INDEPENDENT-FIRST.md',private['first_derivation_sha256'])
add('outside-field-check/public-h-private-review/REVIEW.md',private['manual_review_sha256'])
add('chain-pre-adapter/public-h-private/SUCCESSOR-PROVENANCE.json',private['successor_provenance_sha256'])
for n,h in pfinal['final_artifact'].items():add(n,h)
add('outside-field-check/public-h-private-review/FINAL-SUBJECT-REVIEW.md',pfinal['manual_final_review_sha256'])
for receipt in [row,base,one]:
    for entry in receipt['pins'].values():add(entry['path'],entry['sha256'])
for n,h in second['root_subject_pins'].items():add(n,h)
prefix='selected-promotion-review/standard-identification/restricted-row-qrom/'
for n,h in second['own_pins'].items():add(prefix+n,h)
receipt_names=['outside-field-check/public-h-private-review/REVIEW.json',
 'outside-field-check/public-h-private-review/FINAL-SUBJECT-REVIEW.json',
 'restricted-row-third-review/FINAL-SUBJECT-REVIEW.json',
 'restricted-row-third-review/REVIEW-RECEIPT.json','restricted-row-third-review/ONE-QUERY-RECEIPT.json',
 prefix+'ONE-QUERY-REVIEW.json','selected-promotion-review/STANDARD-INTEGRATION-REVIEW.json']
for n in receipt_names:add(n,sha(X/n))
assert sha(X/'RESTRICTED-CANONICAL-QROM.md')==row['pins']['final_subject']['sha256']
assert sha(X/'PRIVATE-FIXED-H-REDUCTION.md')==pfinal['final_artifact']['PRIVATE-FIXED-H-REDUCTION.md']
backup=X/'root-docs-before-primitive-successors'
assert not backup.exists(),'Do not replace a promoted predecessor.'
backup.mkdir()
for n in docs:shutil.copyfile(X/n,backup/n)
private_add='''**PROVED / ASSUMED — ordinary fixed-public-hash private adapters.** PRIVATE-FIXED-H-REDUCTION.md closes the exact source-relative ordinary public-parameter PRF hop interface: pReal_h <= pFJideal_h+Adv(f;B_K)+Adv(g;B_P), with all full public hashes computed by the same h, literal aliases including seed-zero, classical private queries and quantum public computation. Signed gaps/public-parameter averaging and reduction-versus-challenger costs are explicit. Private-family hardness is ASSUMED; no RO expression is substituted for the remaining fixed-hash pFJideal_h. Prefix private assumptions do not certify the lower128 H_msg route bits. The smallest remaining obligation is a fixed-hash full-output/adaptive-selection/public-graph bound.'''
row_add='''**PROVED / CITED — restricted linked-global-RO canonical target bound.** RESTRICTED-CANONICAL-QROM.md preserves pretarget other-tweak child computation, first literal BE32 acceptance, full same-function target/outside correlations and bottom mass. The independently reviewed one-query Fourier completion yields U(M)=min(1,8(M+1)^2/2^128), using SPHINCS+C TheoremE.3. A NEW pre-digest stopping extractor has M<=Q; the preserved final-evaluation program still has M<=Q+1. The unconditional source type7 component is at most min(1,(1-1/N)(2^42 tau4+2^21 tau8)U(Q)). All honest runtime/global evaluation costs remain charged separately. This restricted component neither replaces the stronger old direct D7 bound nor changes the old complete probability numerics or certifies fixed SHA/category/capacity. Supporting checked declarations stay44, with zero newly checked whole-source/game declarations.'''
for n in docs:
    text=(X/n).read_text(encoding='utf8').rstrip()
    if n=='PROOF.md':addition='\n\n## 16. Ordinary private families under a fixed public hash\n\n'+private_add+'\n\n## 17. Restricted canonical full-RO target and one-query completion\n\n'+row_add
    else:addition='\n\n'+private_add+'\n\n'+row_add
    (X/n).write_text(text+addition+'\n',encoding='utf8')
# Replace current-document entries in preservation pins by their immutable predecessor copies.
for n,h in prior['documents'].items():
    del pins[str(X/n)]
    pins[str(backup/n)]=h
assert all(sha(Path(n))==h for n,h in pins.items())
record={'status':'REVIEWED_PRIVATE_FIXED_H_AND_RESTRICTED_QROM_SUCCESSORS_PROMOTED',
 'documents':{n:sha(X/n) for n in docs},'predecessor_documents':prior['documents'],
 'predecessor_backup':'root-docs-before-primitive-successors',
 'artifacts':{n:sha(X/n) for n in ['PRIVATE-FIXED-H-REDUCTION.md','RESTRICTED-CANONICAL-QROM.md']},
 'accepted_evidence_absolute_pins':pins,'receipt_pins':{n:sha(X/n) for n in receipt_names},
 'preserved_core_artifacts':prior['preserved_artifacts'],
 'source_scalar_manuscript_changes':0,'cumulative_supporting_checked_declarations':44,
 'new_source_game_checked_declarations':0,'ordinary_private_hardness':'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
 'restricted_QROM_only':True,'new_one_query_identity_manual_and_exact_control_reviewed':True,
 'original_level_category_statement':'not established','whole_goal_complete':False}
(X/'PRIMITIVE-SUCCESSORS-PROMOTION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'promoted':list(record['artifacts']),'accepted_pins':len(pins),'supporting_helpers':44,'security':'not established'}))

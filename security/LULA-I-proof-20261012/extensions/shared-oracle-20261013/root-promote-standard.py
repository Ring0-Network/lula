from pathlib import Path
import hashlib, json, shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda n:json.loads((X/n).read_text(encoding='utf8'))
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
peer=load('outside-field-check/standard-component-review/SUBJECT-REVIEW.json')
prior=load('outside-field-check/OUTSIDE-INTEGRATION-REVIEW.json')
assert peer['verdict']=='ACCEPT_MANUAL_CONDITIONAL_FIXED_PUBLIC_HASH_CANONICAL_COLLECTION_COMPONENT'
assert all(peer['checks'].values()) and peer['independent_kernel_reexecution']['exit_code']==0
assert peer['new_source_game_security_checked_declarations']==0
for group in ['subject_pins','inherited_preserved_core_artifacts','kernel_pins']:
    for n,h in peer[group].items():assert sha(X/n)==h,(group,n)
assert sha(X/'selected-promotion-review/standard-identification/PROVENANCE.json')==peer['author_provenance_sha256']
assert sha(X/'outside-field-check/standard-component-review/SUBJECT-REVIEW.md')==peer['manual_review_sha256']
for n,h in prior['documents'].items():assert sha(X/n)==h,n
backup=X/'root-docs-before-standard'
assert not backup.exists(),'Do not replace an immutable predecessor.'
backup.mkdir()
for n in docs:shutil.copyfile(X/n,backup/n)
addition='''**PROVED / ASSUMED — fixed-public-hash canonical collection successor.** STANDARD-CANONICAL-COMPONENT.md gives an independently reviewed source-specific type7 wrapper under the explicitly chosen CF-BS-TCR-collection(h,Prop,2^32) property. Other-tweak collection access computes the genuine child before parameter release. Canonical-first BE32 selection is a legal specialization; equivalence for all accepted-counter policies is not required. Finite bottom and full same-hash correlations are retained. Lower/top fixed predicates yield the unconditional nonzero-seed component 2^42 SuccProp4+2^21 SuccProp8. This is HJ[h], not an equality to the old HJ[O] experiment. All reduction work is charged; quantitative fixed-SHA/collection/full-security bounds remain OPEN.

**PROVED / COMPUTED — limited mechanized addition.** Four independently reexecuted Lean declarations establish only a synthetic counter-policy separation. Cumulative supporting declarations are44, with zero new whole-source/game security declarations. The original scalar theorems, calculators, source and paper are unchanged. Restricted-row QROM and one-query completion candidates remain separate and are not acceptance evidence for this successor.'''
for n in docs:
    text=(X/n).read_text(encoding='utf8').rstrip()
    heading='\n\n## 15. Fixed-public-hash canonical collection component\n\n' if n=='PROOF.md' else '\n\n'
    (X/n).write_text(text+heading+addition+'\n',encoding='utf8')
record={'status':'REVIEWED_MANUAL_STANDARD_CANONICAL_COMPONENT_PROMOTED','documents':{n:sha(X/n) for n in docs},'predecessor_documents':prior['documents'],'predecessor_backup':'root-docs-before-standard','artifact':{'STANDARD-CANONICAL-COMPONENT.md':sha(X/'STANDARD-CANONICAL-COMPONENT.md')},'subject_review_sha256':sha(X/'outside-field-check/standard-component-review/SUBJECT-REVIEW.json'),'subject_pins':peer['subject_pins'],'preserved_core_artifacts':peer['inherited_preserved_core_artifacts'],'kernel_pins':peer['kernel_pins'],'new_supporting_checked_declarations':4,'cumulative_supporting_checked_declarations':44,'new_whole_source_game_checked_declarations':0,'conditional_HJ_fixed_h_only':True,'old_scalar_theorems_unchanged':True,'fixed_sha_hardness':'not established','category_capacity':'not established','whole_goal_complete':False}
assert all(sha(X/n)==h for n,h in record['preserved_core_artifacts'].items())
(X/'STANDARD-CANONICAL-PROMOTION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'promoted':'STANDARD-CANONICAL-COMPONENT.md','cumulative_helpers':44,'whole_source_game_helpers':0,'security_statement':'not established'}))

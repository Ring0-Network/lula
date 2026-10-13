from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((X/n).read_text(encoding='utf8'))
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
prior=read('MESSAGE-GRAPH-PROMOTION.json')
index=read('selected-promotion-review/MESSAGE-GRAPH-INTEGRATION-REVIEW.json')
field=read('outside-field-check/interior-preimage/FINAL-SUBJECT-REVIEW.json')
second=read('pre-start-second/interior-ud/FINAL-SUBJECT-REVIEW.json')
algebra=read('selected-promotion-review/FINAL-UD-PRE-COMPOSITION-REVIEW.json')
assert all(index['checks'].values()) and all(field['checks'].values()) and all(algebra['checks'].values())
assert second['review_status']=='ACCEPT_MANUAL_CONDITIONAL_ORDINARY_UD_PRE_INTERFACE'
assert not field['whole_goal_complete'] and not second['whole_goal_complete']
assert field['new_source_game_declarations']==second['new_source_game_declarations']==0
assert field['subject_sha256']==second['subject_sha256']==sha(X/'FIXED-H-HIDDEN-PREDECESSORS.md')
assert algebra['subject_sha256']==sha(X/'FIXED-H-COMPOSITION-WITH-UD-PRE.md')
assert all(sha(X/n)==h for n,h in prior['documents'].items())
pins=dict(prior['accepted_evidence_absolute_pins'])
def add(n,h=None):
    p=Path(n)
    if not p.is_absolute():p=X/p
    value=sha(p)
    if h is not None:assert value==h,str(p)
    pins[str(p)]=value
for n,h in field['own_pins'].items():add('outside-field-check/interior-preimage/'+n,h)
for n,h in field['peer_pins'].items():add('pre-start-second/interior-ud/'+n,h)
for n,h in field['root_candidate_and_controls'].items():add('root-interior-ud/'+n,h)
for n,h in field['root_control_independent_rerun']['pins'].items():add('outside-field-check/interior-preimage/root-control-recheck/'+n,h)
for group in ('subject_pins','prior_review_receipts','hidden_proof_premise_receipts','preserved_artifacts','provenance_pins'):
    for n,h in algebra[group].items():add(n,h)
for n,h in index['provenance_pins'].items():add(n,h)
artifacts=['FIXED-H-HIDDEN-PREDECESSORS.md','FIXED-H-COMPOSITION-WITH-UD-PRE.md']
receipts=['outside-field-check/interior-preimage/FINAL-SUBJECT-REVIEW.json',
 'outside-field-check/interior-preimage/FINAL-SUBJECT-REVIEW.md',
 'pre-start-second/interior-ud/FINAL-SUBJECT-REVIEW.json',
 'pre-start-second/interior-ud/IMAGE-EVENT-REVIEW.md',
 'selected-promotion-review/FINAL-UD-PRE-COMPOSITION-REVIEW.json',
 'selected-promotion-review/MESSAGE-GRAPH-INTEGRATION-REVIEW.json']
for n in artifacts+receipts:add(n)
backup=X/'root-docs-before-hidden-ud-pre'
assert not backup.exists()
backup.mkdir()
for n in docs:shutil.copyfile(X/n,backup/n)
addition='''

## Ordinary hidden-predecessor interface successor

**PROVED / ASSUMED — manual source-specific UD/PRE reduction.** FIXED-H-HIDDEN-PREDECESSORS.md has two independently saved derivations and exact final-subject reviews. A55-bit selector chooses a genuine typed input before the public parameter;254 stopped private-prefix hybrids keep the public full h unchanged and consistently recompute roots/counters/logical caches. Only completed exposing responses are gated. An observable final image-match superset avoids unknown-input/first-hidden tests. Ordinary one-target SM-UD pays each signed-average hop; ordinary SM-PRE accepts any final preimage. Thus the nonzero-seed final hidden contribution is at most min(1,2^55*(pi_PRE+sum_(r=0..253)delta_r)). No random-function uniformity is asserted for the original h-derived predecessors; the paid hybrids establish the terminal prior uniformity. Quantum A's public computation is unchanged and only its final classical verifier trace is extracted.

**PROVED / OPEN — full symbolic successor.** FIXED-H-COMPOSITION-WITH-UD-PRE.md substitutes this component into the earlier reviewed exact private/message/graph/type7 composition and pays the source zero-seed event once. The algebra receipt was conditional on this second final premise review; both exact hidden-subject receipts are now present and hashed before promotion. The accepted legal interface no longer leaves epsilon_H as an unnamed source probability. Actual fixed-h PRF/ITSR/UD/PRE/TCR family hardness, evaluated complete-resource advantages, adequate level/category, certified capacity and successful parameter repair remain ASSUMED/OPEN. At all eight requested q, the printable full-security claim remains "not established". Historical preceding sections/receipts retain their dated OPEN status; this successor supplies the current interface resolution only.

**COMPUTED — supporting finite checks and preservation.** Root's3072 abstract relations and the other reader's26 independent channel/selector relations, including opaque-equality and stale-root negative controls, passed. They are not source signing runs or cryptographic hardness experiments. All source/challenger, message, storage and coherent circuit costs remain charged. Cumulative checked supporting declarations stay47; this successor adds0 whole-source/game kernel declarations. Frozen source/manuscript/scalar results and prior subject/review receipts are unchanged.
'''
for n in docs:
    (X/n).write_text((X/n).read_text(encoding='utf8').rstrip()+addition+'\n',encoding='utf8')
for n,h in prior['documents'].items():
    pins.pop(str(X/n),None);add(backup/n,h)
assert all(sha(Path(n))==h for n,h in pins.items())
out={'status':'REVIEWED_MANUAL_ORDINARY_HIDDEN_UD_PRE_AND_SYMBOLIC_COMPOSITION_PROMOTED',
 'documents':{n:sha(X/n) for n in docs},'predecessor_documents':prior['documents'],
 'predecessor_backup':'root-docs-before-hidden-ud-pre','artifacts':{n:sha(X/n) for n in artifacts},
 'receipt_pins':{n:sha(X/n) for n in receipts},'accepted_evidence_absolute_pins':pins,
 'cumulative_supporting_checked_declarations':47,'new_source_game_checked_declarations':0,
 'source_scalar_manuscript_changes':0,'hidden_interface':'LEGAL_ORDINARY_UD_PRE_MANUALLY_REVIEWED',
 'evaluated_hardness':'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
 'conditional_algebra_second_final_premise_now_satisfied':True,
 'original_level_category_statement':'not established','whole_goal_complete':False}
(X/'HIDDEN-UD-PRE-PROMOTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'pins':len(pins),'helpers':47,'security':'not established'}))

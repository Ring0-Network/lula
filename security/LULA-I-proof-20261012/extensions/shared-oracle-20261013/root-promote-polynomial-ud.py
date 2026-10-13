from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((X/n).read_text(encoding='utf8'))
prior=read('TARGET-PRE-PROMOTION.json')
current=read('selected-promotion-review/TARGET-PRE-INTEGRATION-REVIEW.json')
assert all(current['checks'].values())
for n,h in prior['documents'].items():assert sha(X/n)==h,n
field_name='outside-field-check/ud-polynomial/FINAL-SUBJECT-REVIEW.json'
sel_dir=Path('selected-promotion-review/quantitative-goal-audit/single-ud-polynomial')
sel_name=str(sel_dir/'FINAL-SUBJECT-REVIEW.json')
status_name=str(sel_dir/'FINAL-STATUS-SUCCESSOR-REVIEW.json')
field,sel,status=[read(n) for n in (field_name,sel_name,status_name)]
assert all(field['checks'].values()) and all(sel['checks'].values()) and all(status['checks'].values())
subject='QUANTUM-UD-POLYNOMIAL-RO.md'
assert field['subject_sha256']==status['subject_sha256']==sha(X/subject)
assert status['prior_subject_sha256']==sel['subject_sha256']==sha(X/'root-docs-before-ud-status'/subject)
assert not any(r['whole_goal_complete'] for r in (field,sel,status))
pins=dict(prior['accepted_evidence_absolute_pins'])
def add(p,h=None):
    p=Path(p)
    if not p.is_absolute():p=X/p
    actual=sha(p)
    if h is not None:assert actual==h,str(p)
    pins[str(p)]=actual
for obj in field['pins'].values():add(obj['path'],obj['sha256'])
for record in (sel,status):
  for group in ('own_pins','primary_pins','peer_first_pins','premise_pins','preserved_artifacts'):
    for n,h in record.get(group,{}).items():
      add(sel_dir/n if group in ('own_pins','primary_pins') else n,h)
for n in (field_name,sel_name,status_name,
 'outside-field-check/ud-polynomial/FINAL-SUBJECT-REVIEW.md',
 'root-ud-polynomial/INDEPENDENT-FIRST.md','root-ud-polynomial/controls.py',
 'root-ud-polynomial/CONTROLS.json','root-docs-before-ud-status/'+subject,
 'selected-promotion-review/TARGET-PRE-INTEGRATION-REVIEW.json',subject):add(n)
backup=X/'root-docs-before-polynomial-ud'
assert not backup.exists()
backup.mkdir()
for n,h in prior['documents'].items():
    shutil.copyfile(X/n,backup/n)
    add(backup/n,h)
addition='''

## Reviewed quadratic one-target UD random-oracle successor

**PROVED / CITED — explicit ordinary quantum component.** QUANTUM-UD-POLYNOMIAL-RO.md proves u(Q,n)=min(1,(1-1/N)*4Q^2/(N-4Q^2)) when4Q^2<N, else1. The exact iid-ideal/planted-real marker laws, one-Boolean-query full-output completion, degree2Q acceptance polynomial, weight symmetrization and centered integer-grid Markov argument are independently derived. Auxiliary data must have the SAME conditional joint law in both experiments and be independent of the whole marker field; an independently supplied world-label bit is a counterexample to a weaker premise. The denominator retains between-grid overshoot. Common entangled/mixed state and adaptive source services are covered within the stated finite query interface.

**PROVED / COMPUTED — source caller and quantified component.** Ex-ante target chronology, opaqueX, Y-derived suffix/root/cache/counters, completed-response gates, SAME local code/coins and counted final call give remoteR=Q_A+1. The unchanged active-selector sum A_H=7628143271608320 and PRE selector count D_H=20229886488608768 yield min(1,D_H*kappa(R,128)+A_H*u(R,128)). Exact32 rows retain eightq values, both cache modes andQ_A2^32/2^64. AtQ_A2^32 this component is approximately0.01042740466035393; atQ_A2^64 it caps1. Uncapped-expression crossings are29741080993/94 at1/2 and42060240100/101 at1. Both final readers reproduce those rational boundaries. Exact finite controls include ordinary marker/polynomial/completion identities, actual entangled one-phase examples, and auxiliary/grid negative controls.

**PROVED — preservation and scope.** This improves the older primitive-interface route, not the stronger direct source H bound. The direct H theorem,48 complete scalar cells and32 prior resource crossings remain authoritative and unchanged. Exact N-1 miss tables may be enormous; all local storage/gates/generation work remains charged. No fixed-SHA/category/gate-cost certificate or actual forgery follows. Supporting checked declarations remain47 and newly checked whole-source/game declarations0. Private-K/private-P polynomial candidates and the simultaneous classical ledger are separate, unpromoted work; this result does not certify their full-source composition. Original adequate level/category/capacity and successful smallest parameter repair remain "not established".
'''
for n in prior['documents']:
    p=X/n
    p.write_text(p.read_text(encoding='utf8').rstrip()+addition+'\n',encoding='utf8')
assert all(sha(Path(n))==h for n,h in pins.items())
out={'status':'REVIEWED_QUADRATIC_ONE_TARGET_UD_RO_COMPONENT_PROMOTED',
 'documents':{n:sha(X/n) for n in prior['documents']},
 'predecessor_documents':prior['documents'],'predecessor_backup':'root-docs-before-polynomial-ud',
 'artifacts':{subject:sha(X/subject),'root-ud-polynomial/controls.py':sha(X/'root-ud-polynomial/controls.py'),
              'root-ud-polynomial/CONTROLS.json':sha(X/'root-ud-polynomial/CONTROLS.json')},
 'receipt_pins':{n:sha(X/n) for n in (field_name,sel_name,status_name)},
 'accepted_evidence_absolute_pins':pins,'cumulative_supporting_checked_declarations':47,
 'new_source_game_checked_declarations':0,'source_scalar_manuscript_changes':0,
 'same_joint_conditional_auxiliary_law_required':True,'unknown_target_query_cap':'Q_A+1',
 'original_level_category_statement':'not established','whole_goal_complete':False}
(X/'POLYNOMIAL-UD-PROMOTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'accepted_pins':len(pins),'helpers':47,'whole_goal_complete':False}))

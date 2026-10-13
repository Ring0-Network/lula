"""Hash-bound resource/algebra acceptance; no source or quantum program execution."""
from pathlib import Path
import json,hashlib,re
X=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
initial=read(OUT/'QPRE-REVIEW.json')
for n,h in initial['subject_pins'].items():assert sha(X/n)==h,n
for n,h in initial['own_pins'].items():assert sha(OUT/n)==h,n
prior=read(OUT/'PRE-INTEGRATION-REVIEW.json')
for group in ('documents','promoted_artifacts','preserved_artifacts','subject_pins','controls'):
    for n,h in prior[group].items():assert sha(X/n)==h,n
lean=read(OUT/'QPRE-Lean-Check.json')
assert lean['exit_code']==0 and lean['checked_declarations']==7
assert lean['source_sha256']==sha(OUT/'QPRE-Averaging.lean')
assert lean['log_sha256']==sha(OUT/'QPRE-Lean.log')
source=(OUT/'QPRE-Averaging.lean').read_text(encoding='utf8')
assert not re.search(r'\b(sorry|admit|axiom|native_decide)\b',source)
log=(OUT/'QPRE-Lean.log').read_text(encoding='utf-8-sig')
assert 'sorryAx' not in log and 'error:' not in log
assert log.count('depends on axioms:')==7
peer=read(X/'chain-pre-independent/quantum-prefix/REVIEW.json')
author=X/'chain-pre-adapter/quantum-INDEPENDENT-DERIVATION.md'
clar=X/'chain-pre-adapter/quantum-CLARIFICATION.md'
assert peer['subject_sha256']==sha(author)
assert peer['own_corrected_successor_sha256']==sha(X/'chain-pre-independent/quantum-prefix/CORRECTED-SUCCESSOR.md')
assert peer['first_expansion_status']=='INCORRECT_MISSING_SQRT_L_SUPERSEDED_NOT_PROMOTED'
subjects={
 'chain-pre-adapter/quantum-INDEPENDENT-DERIVATION.md':sha(author),
 'chain-pre-adapter/quantum-CLARIFICATION.md':sha(clar),
 'chain-pre-independent/quantum-prefix/REVIEW.json':sha(X/'chain-pre-independent/quantum-prefix/REVIEW.json'),
 'chain-pre-independent/quantum-prefix/CORRECTED-SUCCESSOR.md':sha(X/'chain-pre-independent/quantum-prefix/CORRECTED-SUCCESSOR.md')}
ownnames=['QPRE-INDEPENDENT-AVERAGING.md','QPRE-RESOURCE-REVIEW.md','QPRE-FINAL-RESOURCE-REVIEW.md',
 'QPRE-Averaging.lean','QPRE-Lean.log','QPRE-Lean-Check.json','QPRE-Algebra-Control.py','QPRE-Algebra-Control.json']
receipt={
 'verdict':'ACCEPT_CORRECTED_QPRE_ALGEBRA_AND_FINITE_RESOURCE_SCOPE',
 'subject_pins':subjects,'own_pins':{n:sha(OUT/n) for n in ownnames},
 'initial_resource_receipt_sha256':sha(OUT/'QPRE-REVIEW.json'),
 'prior_classical_current_receipt_sha256':sha(OUT/'PRE-INTEGRATION-REVIEW.json'),
 'prior_classical_documents':prior['documents'],
 'preserved_scalar_artifacts':prior['preserved_artifacts'],
 'D_cut':1016949404336128,'L':36028797018963968,
 'probability_envelope':'min(1,(sqrt(L*b_bar)+2Q*sqrt(D_cut/N))^2)',
 'cross_term':'4Q*sqrt(L*D_cut*b_bar/N)',
 'coherent_calls':'Q selected +Q outside =2Q handles',
 'final_selected_classical_calls_max':1,
 'table_initialization':'O(32V_b) data/random bytes; honest calls use same sampled table',
 'new_supporting_checked_declarations':7,
 'full_source_game_quantum_checked_declarations':0,
 'allowed_Lean_axioms':['propext','Classical.choice','Quot.sound'],
 'custom_axioms':0,'admissions':0,
 'checker_sha256':sha(Path(__file__)),
 'source_channel_scope':'Manually peer-reviewed finite source model; not proved by the supporting Lean algebra.',
 'conventional_PRE':'OPEN','efficient_outside_simulation':'OPEN','category_capacity':'not established',
 'whole_goal_complete':False}
(OUT/'QPRE-FINAL-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'verdict':receipt['verdict'],'Lean_exit':lean['exit_code'],
 'supporting_declarations':7,'full_source_declarations':0,
 'receipt_sha256':sha(OUT/'QPRE-FINAL-REVIEW.json')}))

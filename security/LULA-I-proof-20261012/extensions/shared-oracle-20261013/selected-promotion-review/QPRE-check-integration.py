"""Validate the manually reviewed finite QPRE promotion and cumulative hash chain."""
from pathlib import Path
import hashlib,json,re
X=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
p=read(X/'QUANTUM-PRE-PROMOTION.json')
prior=read(OUT/'PRE-INTEGRATION-REVIEW.json')
selected=read(OUT/'INTEGRATION-REVIEW.json')
payload=read(X/'cache-payload-source/INTEGRATION-FINAL-REVIEW.json')
resource=read(OUT/'QPRE-FINAL-REVIEW.json')
peer=read(X/'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json')
for group in ('current_documents','new_artifacts','preserved_artifacts'):
    for n,h in p[group].items():assert sha(X/n)==h,(group,n)
for n,h in p['source_subjects'].items():assert sha(X/'chain-pre-adapter'/n)==h,n
for old,backup in ((prior,'root-docs-before-quantum-pre'),(selected,'root-docs-before-chain-pre'),(payload,'root-docs-before-selected-graph')):
    for n,h in old['documents'].items():assert sha(X/backup/n)==h,(backup,n)
    for n,h in old['promoted_artifacts'].items():assert sha(X/n)==h,n
for n,h in prior['documents'].items():assert p['prior_documents'][n]==h,n
for n,h in resource['subject_pins'].items():assert sha(X/n)==h,n
for n,h in resource['own_pins'].items():assert sha(OUT/n)==h,n
assert p['peer_successor_receipt_sha256']==sha(X/'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json')
assert p['resource_algebra_receipt_sha256']==sha(OUT/'QPRE-FINAL-REVIEW.json')
assert peer['subjects']==p['source_subjects']
assert peer['all_outside_raw_calls_share_fixed_table']
text=(X/'QUANTUM-PRE-REDUCTION.md').read_text(encoding='utf8')
author=(X/'chain-pre-adapter/quantum-INDEPENDENT-DERIVATION.md').read_text(encoding='utf8')
repairs=[
 ('**PROVED — manual candidate awaiting independent second reading.**',
  '**PROVED — manual finite source-model reduction accepted by an independent source-first reader.**'),
 ('**OPEN — independent checking.** The active-CQ factorization, final first-event inclusion and selector block norm need an independent reader and finite controls before promotion. This is a newly saved manual candidate, not wholeRust mechanization.',
  '**PROVED / COMPUTED — independent checking within the stated finite interface.** The source-first second reader accepts the active-CQ factorization, final first-event inclusion and selector block norm. Independent complete-image channel controls and corrected averaging checks support their separate finite cases. Seven Lean supporting algebra/count declarations check; they do not mechanically verify the source or quantum game.')]
for before,after in repairs:
    assert author.count(before)==1,before
    author=author.replace(before,after,1)
assert author.strip() in text
for n in ('quantum-CLARIFICATION.md','quantum-RESOURCE-CLARIFICATION.md'):
    assert (X/'chain-pre-adapter'/n).read_text(encoding='utf8').strip() in text,n
for phrase in ('1,016,949,404,336,128','sqrt(L*D_int*p_PRE/N)','256V_b random bits','O(32V_b)',
               'not40 checked security theorems','A bounded-query2T-wise successor is not applied',
               'shared by coherent calls, honest classical hashing, suffix preparation and final verification'):
    assert phrase in text,phrase
assert '**PROVED — manual candidate awaiting independent second reading.**' not in text
assert p['source_game_declarations_machine_checked']==0
assert p['supporting_declarations_new']==7 and p['supporting_declarations_total']==40
assert p['conventional_PRE']=='OPEN' and p['efficient_outside']=='OPEN'
assert p['level_category']=='not established' and p['manuscript_edits']==0
lean=read(OUT/'QPRE-Lean-Check.json')
assert lean['exit_code']==0 and lean['checked_declarations']==7
assert lean['source_sha256']==sha(OUT/'QPRE-Averaging.lean')
assert lean['log_sha256']==sha(OUT/'QPRE-Lean.log')
log=(OUT/'QPRE-Lean.log').read_text(encoding='utf-8-sig')
assert log.count('depends on axioms:')==7 and 'sorryAx' not in log and 'error:' not in log
assert not re.search(r'\b(sorry|admit|axiom|native_decide)\b',(OUT/'QPRE-Averaging.lean').read_text(encoding='utf8'))
# Prior component counts are read without pinning the mutable live validation file.
v=read(X/'VALIDATION.json')
prior_components=[z for z in v['mechanized_components'] if z['source']!='selected-promotion-review/QPRE-Averaging.lean']
assert sum(z['checked_declarations'] for z in prior_components)==33
for z in prior_components:assert sha(X/z['source'])==z['sha256'],z['source']
release=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(release)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
controls={}
for folder,names in (('chain-pre-adapter',['quantum-control.py','quantum-CONTROL-RESULTS.json']),
                     ('chain-pre-independent/quantum-prefix',['control.py','CONTROL-RESULTS.json']),
                     ('selected-promotion-review',['QPRE-Algebra-Control.py','QPRE-Algebra-Control.json'])):
    for n in names:controls[f'{folder}/{n}']=sha(X/folder/n)
helperpins={f'selected-promotion-review/{n}':sha(OUT/n) for n in ['QPRE-Averaging.lean','QPRE-Lean.log','QPRE-Lean-Check.json']}
backups={}
for old,backup in ((prior,'root-docs-before-quantum-pre'),(selected,'root-docs-before-chain-pre'),(payload,'root-docs-before-selected-graph')):
    backups.update({f'{backup}/{n}':h for n,h in old['documents'].items()})
receipt={
 'verdict':'ACCEPT_CORRECTED_FINITE_QPRE_CURRENT_INDEX',
 'documents':p['current_documents'],'promoted_artifacts':p['new_artifacts'],
 'source_subjects':{f'chain-pre-adapter/{n}':h for n,h in p['source_subjects'].items()},
 'provenance_pins':{'QUANTUM-PRE-PROMOTION.json':sha(X/'QUANTUM-PRE-PROMOTION.json'),
                    'root-promote-quantum-pre.py':sha(X/'root-promote-quantum-pre.py')},
 'prior_review_receipts':{
  'selected-promotion-review/PRE-INTEGRATION-REVIEW.json':sha(OUT/'PRE-INTEGRATION-REVIEW.json'),
  'selected-promotion-review/INTEGRATION-REVIEW.json':sha(OUT/'INTEGRATION-REVIEW.json'),
  'cache-payload-source/INTEGRATION-FINAL-REVIEW.json':sha(X/'cache-payload-source/INTEGRATION-FINAL-REVIEW.json'),
  'selected-promotion-review/QPRE-FINAL-REVIEW.json':sha(OUT/'QPRE-FINAL-REVIEW.json'),
  'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json':sha(X/'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json')},
 'backup_pins':backups,'preserved_artifacts':p['preserved_artifacts'],
 'control_pins':controls,'helper_pins':helperpins,'source_sha256':sha(release),
 'manual_review_sha256':sha(OUT/'QPRE-INTEGRATION-REVIEW.md'),'checker_sha256':sha(Path(__file__)),
 'checks':{
  'accepted_source_and_both_clarifications_included_exactly':True,
  'correct_Dint_pad_and_sqrt_L_cross_term':True,
  'vector_cap2_not_unsupported_raw_cap1':True,
  'only_final_classical_guard_no_coherent_monitor':True,
  'one_shared_eager_table_init_lookup_and_honest_costs_charged':True,
  'selected_Qcoherent_plus1_final_and_two_handle_routing':True,
  'prior_PRE_selected_payload_document_backup_chains_match':True,
  'scalars_calculators_previous_promotions_unchanged':True,
  '40_supporting_only_zero_whole_source_game_checks':True,
  'two_T_wise_successor_not_promoted':True,
  'conventional_efficiency_category_capacity_still_open':True,
  'whole_goal_not_complete':True},
 'supporting_checked_declarations_total':40,'new_supporting_declarations':7,
 'whole_source_game_new_checked_declarations':0,'security_level_category':'not established',
 'whole_goal_complete':False}
(OUT/'QPRE-INTEGRATION-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'verdict':receipt['verdict'],'documents':len(receipt['documents']),
 'checks':len(receipt['checks']),'supporting_declarations':40,'whole_source_checks':0,
 'receipt_sha256':sha(OUT/'QPRE-INTEGRATION-REVIEW.json')}))

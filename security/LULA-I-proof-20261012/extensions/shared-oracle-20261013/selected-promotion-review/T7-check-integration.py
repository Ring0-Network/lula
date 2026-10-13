"""Validate manually reviewed type7/current index without rewriting historical receipts."""
from pathlib import Path
import hashlib,json,re
X=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
p=read(X/'TYPE7-PROMOTION.json')
preliminary=read(X/'TYPE7-PROMOTION-PRELIMINARY.json')
resource=read(OUT/'T7-REVIEW.json')
peer=read(X/'chain-pre-independent/type7/SUCCESSOR-REVIEW.json')
provenance=read(X/'chain-pre-adapter/type7/PROVENANCE.json')
for group in ('current_documents','new_artifacts','preserved_artifacts'):
    for n,h in p[group].items():assert sha(X/n)==h,(group,n)
for n,h in p['source_subjects'].items():assert sha(X/'chain-pre-adapter/type7'/n)==h,n
for n,h in resource['subject_pins'].items():assert sha(X/n)==h,n
for n,h in resource['own_pins'].items():assert sha(OUT/n)==h,n
assert p['peer_successor_receipt_sha256']==sha(X/'chain-pre-independent/type7/SUCCESSOR-REVIEW.json')
assert p['resource_receipt_sha256']==sha(OUT/'T7-REVIEW.json')
assert p['preliminary_promotion_sha256']==sha(X/'TYPE7-PROMOTION-PRELIMINARY.json')
assert peer['subjects']==p['source_subjects']==provenance['subjects']
for n,h in provenance['files'].items():assert sha(X/'chain-pre-adapter/type7'/n)==h,n
historical=[
 ('selected-promotion-review/QPRE-INTEGRATION-REVIEW.json','root-docs-before-type7'),
 ('selected-promotion-review/PRE-INTEGRATION-REVIEW.json','root-docs-before-quantum-pre'),
 ('selected-promotion-review/INTEGRATION-REVIEW.json','root-docs-before-chain-pre'),
 ('cache-payload-source/INTEGRATION-FINAL-REVIEW.json','root-docs-before-selected-graph')]
backups={}
for name,backup in historical:
    old=read(X/name)
    for n,h in old['documents'].items():
        assert sha(X/backup/n)==h,(backup,n)
        backups[f'{backup}/{n}']=h
    for n,h in old['promoted_artifacts'].items():assert sha(X/n)==h,n
qpre=read(OUT/'QPRE-INTEGRATION-REVIEW.json')
assert p['prior_documents']==qpre['documents']==preliminary['prior_documents']
assert p['new_artifacts']==preliminary['new_artifacts'] and p['preserved_artifacts']==preliminary['preserved_artifacts']
for n,h in preliminary['current_documents'].items():
    if n!='TERM-TABLE.md':assert sha(X/n)==h,n
term=(X/'TERM-TABLE.md').read_text(encoding='utf8')
prior_term,removed=re.subn(r'\*\*PROVED[^\n]*seed-charge convention\.\*\*.*?\n\n','',term,count=1,flags=re.S)
assert removed==1 and hashlib.sha256(prior_term.encode()).hexdigest()==preliminary['current_documents']['TERM-TABLE.md']
for phrase in ('+3, +2 and +3218','(Q_H+2q+2)/N','beta_0=(2Q_H+q+1)/N','(Q_H+3217)/N',
               'Pr[S=0]=1/N exactly once','2+1+3017+3217+5+1=6243','not a new bound or numerical revision'):
    assert phrase in term,phrase
theorem=(X/'CLASSICAL-RO-THEOREM.md').read_text(encoding='utf8')
assert '2+1+3017+3217+5+1=6243' in theorem
code=(X/'bounds.py').read_text(encoding='utf8')
for anchor in ('numerator = QH + 2*q + 3','mp.mpf(2*QH+q+2)',
               'joint_nonzero = min(mp.mpf(1),mp.mpf(QH+2*q+2)/N)',
               'beta_nonzero = min(mp.mpf(1),mp.mpf(2*QH+q+1)/N+pair_term+exhaust)',
               'graph_nonzero = min(mp.mpf(1),mp.mpf(QH+3217)/N)',
               'linear_numerator = 6*QH+3*q+6243'):
    assert anchor in code,anchor
assert 2+1+3017+3217+5+1==6243
text=(X/'TYPE7-REDUCTION-PROGRAM.md').read_text(encoding='utf8')
author=(X/'chain-pre-adapter/type7/INDEPENDENT-DERIVATION.md').read_text(encoding='utf8')
repairs=[('**PROVED — manual source-first candidate awaiting second reading.**',
 '**PROVED — manually source-derived adapter, accepted by an independent source-first reader.**'),
 ('**OPEN — remaining assumptions/gates.** Independent second reading/control checks are needed before promotion.',
 '**PROVED / COMPUTED — independent source reading and controls accepted within the named interface.** The original subject and event/stopping clarification have hash-bound source and resource reviews; no full-source kernel theorem is asserted.')]
for before,after in repairs:
    assert author.count(before)==1,before
    author=author.replace(before,after,1)
assert author.strip() in text
assert (X/'chain-pre-adapter/type7/CLARIFICATION.md').read_text(encoding='utf8').strip() in text
for phrase in ('D7_base_final','D7_base_public','2,269,959,421,952','42-bit','2^32','17,392','8,704',
               'faithful only on the source prefix','does not add a source abort','128-prefix equality'):
    assert phrase in text,phrase
control=read(OUT/'T7-CONTROL-RESULTS.json')
assert control['script_sha256']==sha(OUT/'T7-Exact-Control.py')
assert len(control['q_resource_rows'])==8
for row in control['q_resource_rows']:
    q=2**row['q_exponent']
    assert row['hot_F_cap']==min(19212937084272640,8704+2181038080+q*12816)
    assert row['cold_F_cap']==min(19212937084272640,8704+2181038080+q*33567232)
    assert row['hot_honest_outside_plus_C']==2**21*(19505+2**32)-1+q*(82090+5*2**32)+3224+17392
    assert row['cold_honest_outside_plus_C']==2**21*(19505+2**32)-1+q*(8560574463+82090+6*2**32)+3224+17392
assert p['new_supporting_declarations']==0 and p['supporting_declarations_total']==40
assert p['whole_source_game_checked_declarations']==0 and p['level_category']=='not established'
assert p['conventional_S_TCR']=='OPEN' and p['efficient_outside']=='OPEN' and p['manuscript_edits']==0
release=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(release)==provenance['source_sha256']==resource['source_sha256']
controlpins={}
for folder,names in [('chain-pre-adapter/type7',['control.py','CONTROL-RESULTS.json']),
                     ('chain-pre-independent/type7',['control.py','CONTROL-RESULTS.json']),
                     ('selected-promotion-review',['T7-Exact-Control.py','T7-CONTROL-RESULTS.json'])]:
    for n in names:controlpins[f'{folder}/{n}']=sha(X/folder/n)
receipt={
 'verdict':'ACCEPT_CORRECTED_TYPE7_CURRENT_INDEX',
 'documents':p['current_documents'],'promoted_artifacts':p['new_artifacts'],
 'source_subjects':{f'chain-pre-adapter/type7/{n}':h for n,h in p['source_subjects'].items()},
 'provenance_pins':{'TYPE7-PROMOTION.json':sha(X/'TYPE7-PROMOTION.json'),
  'TYPE7-PROMOTION-PRELIMINARY.json':sha(X/'TYPE7-PROMOTION-PRELIMINARY.json'),
  'root-promote-type7.py':sha(X/'root-promote-type7.py'),
  'chain-pre-adapter/type7/PROVENANCE.json':sha(X/'chain-pre-adapter/type7/PROVENANCE.json')},
 'prior_review_receipts':{**{name:sha(X/name) for name,_ in historical},
  'selected-promotion-review/T7-REVIEW.json':sha(OUT/'T7-REVIEW.json'),
  'chain-pre-independent/type7/SUCCESSOR-REVIEW.json':sha(X/'chain-pre-independent/type7/SUCCESSOR-REVIEW.json')},
 'backup_pins':backups,'preserved_artifacts':p['preserved_artifacts'],'control_pins':controlpins,
 'source_sha256':sha(release),'manual_review_sha256':sha(OUT/'T7-INTEGRATION-REVIEW.md'),
 'checker_sha256':sha(Path(__file__)),
 'checks':{'exact_author_and_clarification_inclusion':True,'final_public_event_names_distinct':True,
  'bottom_local_B_failure_not_global_source_conditioning':True,'source_prefix_vs_unflagged_law_precise':True,
  'challenge_preprocessing_and_posttarget_queries_separate':True,'counts_children_and8q_resources_match':True,
  'same_fixed_full256_raw_function_every_phase':True,'one_seedzero_complete_convention_reconciled':True,
  'preliminary_TERM_exactly_reconstructed_by_one_clarification_removal':True,
  'four_prior_current_document_backup_chains_match':True,'scalar_calculator_prior_artifacts_unchanged':True,
  'supporting40_new0_whole_source0':True,'conventional_efficiency_category_capacity_open':True},
 'supporting_checked_declarations_total':40,'new_supporting_declarations':0,
 'whole_source_game_new_checked_declarations':0,'security_level_category':'not established',
 'whole_goal_complete':False}
(OUT/'T7-INTEGRATION-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'verdict':receipt['verdict'],'documents':6,'checks':len(receipt['checks']),
 'q_resource_rows':8,'new_checked_declarations':0,'receipt_sha256':sha(OUT/'T7-INTEGRATION-REVIEW.json')}))

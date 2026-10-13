from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent; X=P.parent;R=X/'chain-pre-independent'/'quantum-prefix'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=json.loads((R/'SUCCESSOR-REVIEW.json').read_text(encoding='utf8'))
assert receipt['status']=='ACCEPTED_SCOPED_FINITE_QROM_RELATIVE_MANUAL'
for n,h in receipt['subjects'].items():assert sha(P/n)==h,(n,sha(P/n))
assert sha(R/'REVIEW.json')==receipt['previous_receipt_sha256']
assert sha(R/'SUCCESSOR-SECOND-READER.md')==receipt['review_sha256']
assert receipt['recheck_results_sha256']==sha(P/'quantum-CONTROL-RESULTS.json')
assert receipt['independent_recheck_exit']==0
assert sha(P/'PROVENANCE.json')=='b87d89348a7e3720ac35cdef05db3fb69bce6845b23323b7f8c856b8112098b1'
assert sha(P/'INDEPENDENT_DERIVATION.md')=='61a8c1d673008b83ba61887d762ad0e51501de039ef870b8b5a43eae7b73e0fa'
assert sha(P/'FORS-LOCALIZED-SUCCESSOR.md')=='2026eba89ac1e884785e9c38b09c9bb347d7efd35f99cc534b988db1c71d1c0b'
source=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(source)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
controls=json.loads((P/'quantum-CONTROL-RESULTS.json').read_text(encoding='utf8'))
assert len(controls['checks'])==6 and controls['D_interior']==1016949404336128
for c in controls['checks']:
 assert c['support_first']<=c['support_bound']+1e-12
 assert c['support_second']<=c['support_bound']+1e-12
peerpair={'CORRECTED-SUCCESSOR.md':'d5eb3f4e6d495691c566026bcef72c4de2a614865a0050777475568461330e51',
'CONTROL-AND-RESOURCES.md':'9b5da900c58bef0c6460b3d4d204f1e427d4aa4f4d6155e09b8eda94250aebb3'}
for n,h in peerpair.items():assert sha(R/n)==h
out={'status':'READY_FOR_ROOT_PROMOTION_SCOPED_FINITE_QROM_RELATIVE_MANUAL',
'subjects':receipt['subjects'],
'reader_receipt':{'path':'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json','sha256':sha(R/'SUCCESSOR-REVIEW.json')},
'reader_review':{'path':'chain-pre-independent/quantum-prefix/SUCCESSOR-SECOND-READER.md','sha256':sha(R/'SUCCESSOR-SECOND-READER.md')},
'own_independent_before_peer':'quantum-INDEPENDENT-DERIVATION.md saved before new peer quantum candidate was read',
'accepted_peer_corrected_pair':peerpair,'own_peer_review_sha256':sha(P/'quantum-PEER-SECOND-READER.md'),
'source_sha256':sha(source),'classical_provenance_preserved':sha(P/'PROVENANCE.json'),
'bound':'Pr_HJ[Win AND H_final | fixed nonzero S] <= min(1,(sqrt(2^55*p_PRE)+2*Q_q*sqrt(1016949404336128/2^128))^2)',
'per_selector_vector_distance':'min(2,2Q_q/sqrt(2^128)) for interior WOTS, zero for FORS/r0/dummy',
'resources':{'Selected':'Q_q coherent+1 final classical','outside':'Q_q coherent+honest source R','init_coins':'256 V_b','table_bytes':'32 V_b','init_writes':'O(32 V_b)','one_coherent_outside_lookup':'O(V_b*(b+32)) gates'},
'controls':{'own_cases':6,'own_worlds_per_case':1024,'own_exit':0,'peer_reexecuted_worlds':8192,'peer_exit':0,'source_final_first_witness_branches':3072,'non_genuine_prefix_mergers':1024},
'open':['conventional quantum PRE/fixed-SHA identification','efficient local outside quantum oracle realization','level/category certification'],
'core_numeric_bounds_changed':False,'source_manuscript_parameters_changed':False,
'files':{p.name:sha(p) for p in sorted(P.glob('quantum-*')) if p.is_file() and p.name!='quantum-PROVENANCE.json'}}
(P/'quantum-PROVENANCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'provenance_sha256':sha(P/'quantum-PROVENANCE.json'),'reader_receipt':out['reader_receipt'],'classical_provenance_preserved':out['classical_provenance_preserved']},indent=2))

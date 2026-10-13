from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;X=P.parent.parent;R=X/'chain-pre-independent'/'type7';T=X/'selected-promotion-review'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=json.loads((R/'SUCCESSOR-REVIEW.json').read_text(encoding='utf8'))
assert receipt['status']=='ACCEPTED_SCOPED_RO_QROM_RELATIVE_MANUAL'
for n,h in receipt['subjects'].items():assert sha(P/n)==h,(n,sha(P/n))
assert sha(R/'REVIEW.json')==receipt['previous_receipt_sha256']
assert receipt['independent_control_recheck_exit']==0
assert receipt['independent_recheck_sha256']==sha(P/'CONTROL-RESULTS.json')
third=json.loads((T/'T7-REVIEW.json').read_text(encoding='utf8'))
assert third['verdict']=='ACCEPT_SCOPED_FIRST_ACCEPTED_TYPE7_ROW_RESOURCES_AND_INTERFACE'
for n,h in third['subject_pins'].items():assert sha(X/n)==h
for n,h in third['own_pins'].items():assert sha(T/n)==h
source=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(source)==third['source_sha256']=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert sha(P.parent/'PROVENANCE.json')=='b87d89348a7e3720ac35cdef05db3fb69bce6845b23323b7f8c856b8112098b1'
assert sha(P.parent/'quantum-PROVENANCE.json')=='61a808273fc5f172b8f4690fe4246729aeb581559feaf9c1a5dbff1234a7d3dd'
peer=json.loads((R/'CANDIDATE.json').read_text(encoding='utf8'))
assert sha(P/'peer-recheck'/'control.py')==peer['control_source_sha256']
assert sha(P/'peer-recheck'/'CONTROL-RESULTS.json')==peer['controls_sha256']
controls=json.loads((P/'CONTROL-RESULTS.json').read_text(encoding='utf8'))
assert controls['worlds']==8192 and controls['actual_row_count']==2269959421952
out={'status':'READY_FOR_ROOT_PROMOTION_SCOPED_CLASSICAL_QROM_ROW_INTERFACE_MANUAL',
'subjects':receipt['subjects'],
'original_saved_before_peer':'INDEPENDENT-DERIVATION.md',
'scope_clarification':'Original final D7_base preserved; optional broader classical event D7_base_public; actual stop faithful prefix, unflagged comparator exact law; bottom B-local zero selected contribution',
'independent_reader_receipt':{'path':'chain-pre-independent/type7/SUCCESSOR-REVIEW.json','sha256':sha(R/'SUCCESSOR-REVIEW.json')},
'previous_reader_receipt':{'path':'chain-pre-independent/type7/REVIEW.json','sha256':sha(R/'REVIEW.json')},
'additional_resource_reader':{'path':'selected-promotion-review/T7-REVIEW.json','sha256':sha(T/'T7-REVIEW.json')},
'own_peer_reader_sha256':sha(P/'PEER-SECOND-READER.md'),
'source_sha256':sha(source),
'bound':'Pr_HJ[Win AND D7_base_final | fixed nonzero S] <= 2^42 Pr_firstAcceptedRowCollision[B wins]',
'resources':{'rows':2269959421952,'selector_bits':42,'selected_target_registrations':1,'challenger_counter_evaluations_max':2**32,'selected_handle':'Q adversarial+1 final classical','child_public_max':17392,'child_F_distinct_max':8704,'outside_init':'256 V_b bits,32 V_bbytes,O(32 V_b)writes'},
'controls':{'own_worlds':8192,'own_exit':0,'peer_reexecuted_worlds':32768,'peer_exit':0,'own_independent_recheck_exit':receipt['independent_control_recheck_exit']},
'preserved_classical_provenance':sha(P.parent/'PROVENANCE.json'),'preserved_quantum_provenance':sha(P.parent/'quantum-PROVENANCE.json'),
'open':['conventional shared-seed keyed S-TCR identification','efficient local quantum outside oracle realization','level/category certification'],
'core_scalar_numeric_changes':False,'new_kernel_declarations':0,
'files':{str(p.relative_to(P)).replace('\\','/'):sha(p) for p in sorted(P.rglob('*')) if p.is_file() and p.name!='PROVENANCE.json'}}
(P/'PROVENANCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'provenance_sha256':sha(P/'PROVENANCE.json'),'reader_receipt':out['independent_reader_receipt'],'additional_resource_reader':out['additional_resource_reader']},indent=2))

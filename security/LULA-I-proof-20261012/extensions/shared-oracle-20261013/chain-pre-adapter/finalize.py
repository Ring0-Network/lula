from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
X=P.parent
reader=X/'chain-pre-independent'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subjects={'INDEPENDENT_DERIVATION.md':'61a8c1d673008b83ba61887d762ad0e51501de039ef870b8b5a43eae7b73e0fa',
'FORS-LOCALIZED-SUCCESSOR.md':'2026eba89ac1e884785e9c38b09c9bb347d7efd35f99cc534b988db1c71d1c0b',
'INDEPENDENT_DERIVATION-FIRST.md':'c038207a453f1ab4ce7047b20b8a35b47a6b397ffa82347c02b2f468f714bcb7'}
for n,h in subjects.items():assert sha(P/n)==h,(n,sha(P/n))
receipt=json.loads((reader/'COMBINED-REVIEW.json').read_text(encoding='utf-8-sig'))
assert receipt['status']=='ACCEPTED_SCOPED_CLASSICAL_RO_RELATIVE_MANUAL'
for n in ['INDEPENDENT_DERIVATION.md','FORS-LOCALIZED-SUCCESSOR.md']:
 assert receipt['subjects']['chain-pre-adapter/'+n]==subjects[n]
for n,h in receipt['review'].items():assert sha(reader/n)==h
for n,h in receipt['independent_before_peer'].items():assert sha(reader/n)==h
c=json.loads((P/'CONTROL-RESULTS.json').read_text(encoding='utf8'))
assert c['source_worlds']==512 and c['exact_joint_law_bijection']
assert len(c['checks'])==6
for row in c['checks']:assert row['success_sum']>=row['source_first_hidden']
source=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(source)==receipt['source_sha256']==c['source_sha256']
files=sorted(p for p in P.rglob('*') if p.is_file() and p.name!='PROVENANCE.json')
out={'status':'READY_FOR_ROOT_PROMOTION_SCOPED_CLASSICAL_RO_RELATIVE',
'own_independence':'Initial WOTS source-first derivation saved before new peer reading; corrected only setup wording/type nomenclature. Combined FORS successor is explicitly attributed synthesis after peer reading.',
'subjects':subjects,'reader_receipt':{'path':'chain-pre-independent/COMBINED-REVIEW.json','sha256':sha(reader/'COMBINED-REVIEW.json')},
'reader_review':{'path':'chain-pre-independent/COMBINED-SECOND-READER.md','sha256':sha(reader/'COMBINED-SECOND-READER.md')},
'source_sha256':sha(source),
'bound':'Pr_HJ[H|fixed nonzero S] <= 2^55 Pr_selectedROuniformInputFull256PRE[B wins]',
'resources':{'wots_selector_bits':50,'combined_selector_bits':55,'protected_wots':c['wots_count'],'protected_fors':c['fors_count'],'protected_combined':c['combined_count'],'selected_calls':'Q_H+1','extra_public_hashes':254,'private_distinct':'min(N_D,1+2181038080+q U_mode)','additional_node_bytes':4096},
'controls':{'own_worlds':512,'own_policies':6,'own_exit':0,'peer_reexecuted_worlds':512,'peer_reexecuted_policies':6,'peer_exit':0,'proof_status':'Finite controls only; whole manual theorem accepted independently'},
'open':['conventional fixed-key/shared-seed PRE identification','coherent QROM stopped-cut embedding','level/category certification'],
'unchanged':['crypto source','manuscript','parameters','accepted direct RO/QROM scalar formulas'],
'files':{str(p.relative_to(P)).replace('\\','/'):sha(p) for p in files}}
(P/'PROVENANCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'provenance_sha256':sha(P/'PROVENANCE.json'),'reader_receipt_sha256':sha(reader/'COMBINED-REVIEW.json'),'source_sha256':sha(source),'files':len(files)},indent=2))

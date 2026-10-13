from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(HERE/'INDEPENDENT-DERIVATION.md')=='6c44c1b3cce9cc5438f333031258b1c392069a171b1c6358e6354af6d9aab1af'
assert sha(HERE/'control.py')=='093f5248b4873468d192c41c96d565f05298e33012272d36da0d7b09190b01c3'
assert sha(HERE/'CONTROL-RESULTS.json')=='168cc0b9e2bb1e1f7a98cc0360059504f53757f1ca216e628ced25f3bd85215b'
assert sha(HERE/'PROVENANCE.json')=='04cb096d72bdbaf8799a81a6a6ba3f57c308d00279eded633975c7891168547b'
results=json.loads((HERE/'CONTROL-SUCCESSOR-RESULTS.json').read_text(encoding='utf-8'))
assert results['source_sha256']==sha(HERE/'control-successor.py')
assert results['noncompletion_under_second_fixed_h_worlds']==8
files=['INDEPENDENT-DERIVATION.md','CLARIFICATION.md','control.py','CONTROL-RESULTS.json','PROVENANCE.json','control-successor.py','CONTROL-SUCCESSOR-RESULTS.json','make_control_successor.py','finalize_successor.py']
packet={'subject':'PUBLIC_FIXED_H_ORDINARY_PRIVATE_PRF_ADAPTER_SUCCESSOR',
 'manual_status':'INDEPENDENT_FIRST_SAVED_PEER_REVIEW_PENDING',
 'own_control_exit':0,'original_pins_preserved':True,
 'files':{f:sha(HERE/f) for f in files},
 'hardness':'ASSUMED_WITHOUT_NUMERICAL_CERTIFICATE',
 'no_external_raw_challenge':True,'private_outputs_bytes':16,
 'prekey_source_S_withheld':True,'zero_seed_aliases_retained':True,
 'quantum_private_access':'classical source services; PQ adversary publich code allowed',
 'write_boundary':'chain-pre-adapter/public-h-private only',
 'protected_source_paper_scalars_and_earlier_receipts_edited':False}
(HERE/'SUCCESSOR-PROVENANCE.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(sha(HERE/'SUCCESSOR-PROVENANCE.json'))

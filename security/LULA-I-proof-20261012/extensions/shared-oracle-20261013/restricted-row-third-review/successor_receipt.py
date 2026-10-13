from pathlib import Path
import hashlib
import json

here=Path(__file__).resolve().parent
x=here.parent
files={
    'base_review':here/'PEER-REVIEW.md',
    'base_receipt':here/'REVIEW-RECEIPT.json',
    'root_proof':x/'root-keyed-review/ONE-QUERY-COMPLETION.md',
    'root_controls':x/'root-keyed-review/one_query_completion.py',
    'review':here/'ONE-QUERY-REVIEW.md',
    'own_controls':here/'one_query_control.py',
    'own_results':here/'ONE-QUERY-RESULTS.json',
    'terminated_exhaustive_source':here/'one_query_control-exhaustive-terminated.py',
}
pins={k:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in files.items()}
assert pins['base_receipt']['sha256']=='003e3f102ebfb903ca268c5ab64f01e1a974dc43b682c33641e6e20cc904ae44'
assert pins['root_proof']['sha256']=='7def78f7f5e771e397373f7ad81c7977674669d2064a3b2ce1a31e13d31bf1f0'
assert pins['base_review']['sha256']=='8260eada5056c869c564e38ed0cd707f4ac9f1a5f9fba1c5de690763f7dee0da'
results=json.loads(files['own_results'].read_text(encoding='utf-8'))
assert results['status']=='PASS' and results['worlds']==256 and results['clean_basis_checks']==8192
assert results['mixed_region_superposition_checks']==256
obj={
    'status':'ACCEPTED_MANUAL_ONE_QUERY_COMPLETION_SUCCESSOR',
    'base_preserved':True,'pins':pins,'controls_exit_code':0,
    'completion_bound':'min(1,8*(M+1)^2/2^128)',
    'old_adapter_M':'Q+1','new_stopping_extractor_M':'Q',
    'basis_worlds':256,'clean_basis_checks':8192,'mixed_region_checks':256,
    'terminated_optional_exhaustive':{'process_id':26816,'elapsed_seconds':92.9564276,'cpu_seconds':88.5,'process_exit_code':1,'completed_result':False,'reason':'Parent requested bounded optional control'},
    'scope':'Manual exact circuit identity and restricted-row consequence, plus finite synthetic matrix tests. Zero new whole-source/kernel declarations; no old scalar or manuscript change.'
}
(here/'ONE-QUERY-RECEIPT.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'review_sha256':pins['review']['sha256'],'receipt_sha256':hashlib.sha256((here/'ONE-QUERY-RECEIPT.json').read_bytes()).hexdigest(),'status':obj['status']}))

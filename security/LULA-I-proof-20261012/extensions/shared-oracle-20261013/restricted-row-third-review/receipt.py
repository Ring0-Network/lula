from pathlib import Path
import hashlib
import json

here=Path(__file__).resolve().parent
x=here.parent
r=x.parents[3]
paths={
    'reader_first': x/'keyed-target-reader/restricted-row-qrom/INDEPENDENT-FIRST.md',
    'author_first': x/'selected-promotion-review/standard-identification/restricted-row-qrom/INDEPENDENT-FIRST.md',
    'source': r/'publications/LULA-I/release/code/lula1/src/lib.rs',
    'primary_pdf': r/'R2/R2B-joint-constraints/refs/sphincsplusc_2022_778/2022-778.pdf',
    'primary_text': r/'R2/R2B-joint-constraints/refs/sphincsplusc_2022_778/2022-778.txt',
    'review': here/'PEER-REVIEW.md',
    'controls': here/'controls.py',
    'results': here/'CONTROL-RESULTS.json',
}
pins={k: {'path':str(p), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()}
assert pins['reader_first']['sha256']=='44dcb6acf797cf27875eece1a9f52f6e8faf2c365a8a391d4d5a14812b1c419b'
assert pins['author_first']['sha256']=='74d25d6b3a7332d866ac8c11d3a0b75b37390837b02e7abc05d72332f84a31c1'
assert pins['source']['sha256']=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert pins['primary_pdf']['sha256']=='1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215'
assert pins['primary_text']['sha256']=='833bcca0db93c57c3eff21e7982eb122aa386cdb2cdcdb696721d086cd406078'
obj={'status':'ACCEPTED_MANUAL_RESTRICTED_ROW_QROM_TWO_QUERY_COMPONENT',
     'provenance':'Both prior first proofs read before this third peer review; not blind rederivation.',
     'scope':'Manual restricted static-global-fullRO proof and exact synthetic controls; no fullsource/game kernel declarations or numerical promotion.',
     'pins':pins,'controls_exit_code':0,'supporting_declarations_added':0,
     'base_bound':'min(1,8*(2*M+1)^2/2^128)',
     'old_adapter_M':'Q+1','new_stopping_extractor_M':'Q',
     'wording_clarification':'Two-call substitution does not exclude a separately established one-call oracle completion.'}
(here/'REVIEW-RECEIPT.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'review':pins['review']['sha256'],'receipt':hashlib.sha256((here/'REVIEW-RECEIPT.json').read_bytes()).hexdigest(),'status':obj['status']}))

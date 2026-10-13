from pathlib import Path
import hashlib,json
here=Path(__file__).resolve().parent
x=here.parent
files={
 'final_subject':x/'RESTRICTED-CANONICAL-QROM.md',
 'final_review':here/'FINAL-SUBJECT-REVIEW.md',
 'base_receipt':here/'REVIEW-RECEIPT.json',
 'successor_receipt':here/'ONE-QUERY-RECEIPT.json',
 'source':x.parents[3]/'publications/LULA-I/release/code/lula1/src/lib.rs',
}
pins={k:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in files.items()}
assert pins['base_receipt']['sha256']=='003e3f102ebfb903ca268c5ab64f01e1a974dc43b682c33641e6e20cc904ae44'
assert pins['successor_receipt']['sha256']=='44a7687c99f550610d70920e0dd4658c8b4f6fe74d47dec9bb7db6b9f9af5704'
assert pins['source']['sha256']=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
obj={'status':'ACCEPTED_FINAL_MANUAL_RESTRICTED_CANONICAL_QROM_COMPONENT','pins':pins,
 'unconditional_bound':'min(1,(1-1/N)*(2^42*tau4+2^21*tau8)*min(1,8*(Q+1)^2/N))',
 'new_extractor_M':'Q','old_adapter_M':'Q+1',
 'full_execution_resources_separate_from_M':True,
 'old_scalar_changes':0,'new_game_kernel_declarations':0,
 'scope':'Manual restricted linked fullRO component and source-event accounting; no complete signature-security or fixed-SHA claim.'}
(here/'FINAL-SUBJECT-REVIEW.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'subject_sha256':pins['final_subject']['sha256'],'review_sha256':pins['final_review']['sha256'],'receipt_sha256':hashlib.sha256((here/'FINAL-SUBJECT-REVIEW.json').read_bytes()).hexdigest(),'status':obj['status']}))

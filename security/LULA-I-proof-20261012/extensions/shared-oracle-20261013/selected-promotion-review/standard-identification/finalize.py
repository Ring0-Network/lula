"""Record scoped conditional keyed-wrapper provenance; no source/security execution."""
from pathlib import Path
import hashlib,json,subprocess,sys
P=Path(__file__).resolve().parent
X=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
assert sha(P/'INDEPENDENT-DERIVATION.md')=='74e2106c6c18733d03864f844817d9685db07a867972721aec485bfc9ed04e57'
assert sha(P/'CLARIFICATION.md')=='649ab0c00afa293ba64f0624338c49f2dd9c921fd2ac70d225143d308b58d289'
q=subprocess.run([sys.executable,'-I','-B',str(P/'COUNTERMODELS.py')],capture_output=True,text=True)
assert q.returncode==0,q.stderr
model=read(P/'COUNTERMODEL-RESULTS.json')
assert model['script_sha256']==sha(P/'COUNTERMODELS.py')
assert [z['success'] for z in model['counter_policy_rows']]==['1','0']
assert len(model['standalone_postkey_collection_rows'])==5
peerdir=X/'keyed-target-reader'
peer=read(peerdir/'REVIEW-RECEIPT.json')
for n,h in peer['artifacts'].items():assert sha(peerdir/n)==h,n
assert peer['peer_subject_sha256']==sha(P/'INDEPENDENT-DERIVATION.md')
assert peer['peer_clarification_sha256']==sha(P/'CLARIFICATION.md')
assert peer['control_execution_exit_code']==0
release=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert sha(release)==peer['source_sha256']=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
primary=[
 (r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\M-measure\M2-sphincs-reparam\refs\eprint_2022_346_hulsing_kudinov_tight.pdf',
 '80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3','https://eprint.iacr.org/2022/346','Definitions2/7;collection discussion;Section8 quantitative conjecture'),
 (r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\R2\R2B-joint-constraints\refs\sphincsplusc_2022_778\2022-778.pdf',
 '1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215','https://eprint.iacr.org/2022/778','Definition5.1;Section5.1/Algorithm5;DefinitionC.1 printed page30'),
 (r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\private\primary\2025-2203.pdf',
 '3c58f81a6a0b7e8e040134be1a0013b3977edefdc889e1636d4dfe79cf0e225e','https://eprint.iacr.org/2025/2203','Definitions2.2/2.3')]
prim=[]
for path,h,url,anchors in primary:
    pdf=Path(path);assert sha(pdf)==h,path
    txt=pdf.with_suffix('.txt')
    prim.append({'pdf':str(pdf),'pdf_sha256':h,'cached_text':str(txt),'cached_text_sha256':sha(txt),
                 'primary_url':url,'anchors':anchors})
prior=read(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.json')
for n,h in prior['preserved_artifacts'].items():assert sha(X/n)==h,n
for n,h in prior['promoted_artifacts'].items():assert sha(X/n)==h,n
names=['INDEPENDENT-DERIVATION.md','CLARIFICATION.md','QUANTITATIVE-SCOPE.md','COUNTERMODELS.py',
 'COUNTERMODEL-RESULTS.json','PRIMARY-AND-STATUS.md','OWN-RECEIPT.json','SUCCESSOR-OWN-RECEIPT.json','PEER-REVIEW.md']
record={
 'status':'PEER_ACCEPTED_MANUAL_ASSUMPTION_PARAMETRIC_CANONICAL_COLLECTION_COMPONENT',
 'files':{n:sha(P/n) for n in names},
 'own_first_saved_before_new_peer_proposals':True,
 'peer_first_saved_before_own_proposal_read':True,
 'peer_review_pins':{f'keyed-target-reader/{n}':sha(peerdir/n) for n in ['INDEPENDENT-FIRST.md','PEER-REVIEW.md','REVIEW-RECEIPT.json','controls.py','CONTROL-RESULTS.json']},
 'primary_files':prim,'source_sha256':sha(release),
 'prior_type7_current_receipt_sha256':sha(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.json'),
 'preserved_core_artifacts':{**prior['preserved_artifacts'],**prior['promoted_artifacts']},
 'named_security_hypothesis':'CF-BS-TCR-collection(h,Prop,Lc),canonical literalBE32 first counter and unconditioned bottom',
 'public_implementation_model':'HJ[h];one actual public fullh, not equality to HJ[O]',
 'external_oracle_route':'Distinct explicit RAW-COL-CAN32-S-TCR linked global full256O extension',
 'low_top_predicates':'Two fixed instances Prop4/Prop8;lower42-bit/top21-bit selectors',
 'conditional_component_inequality':'Pr_HJ[h][Win AND D7_base_final AND S!=0] <=2^42 SuccProp4(B_lower)+2^21 SuccProp8(B_top)',
 'closed_scoped_lemma':'Other-tweak collection access computes genuine child before parameter release',
 'counter_policy_precision':'Canonicalfirst is legal specialization;no equivalence for all valid policies required',
 'construction_parameter_precision':'r=securityparameter is constructionchoice,not mandatoryformalC1constraint',
 'countermodel_role':'Abstract policy/interface implication negatives only;not actual source/SHA attacks',
 'resource_precision':'All child/Can/source/private/raw/classifier bytes,time/gates/globalqueries counted;A query budget alone insufficient',
 'published_quantitative_transfer':'Not established;collection/finitecanonical/fullRaw/theorem budget applicability remains to audit',
 'new_checked_declarations':0,'prior_supporting_declarations_unchanged':40,
 'control_exit_code':q.returncode,'peer_control_exit_code':peer['control_execution_exit_code'],
 'source_attacks':0,'source_manuscript_numeric_changes':0,
 'fixed_SHA_hardness':'not established','security_category_capacity':'not established',
 'whole_goal_complete':False,'finalizer_sha256':sha(Path(__file__))}
(P/'PROVENANCE.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':record['status'],'own_control_exit':0,'primary_PDF_pins':3,
                 'new_kernel_declarations':0,'provenance_sha256':sha(P/'PROVENANCE.json')}))

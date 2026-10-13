from pathlib import Path
import hashlib,json

here=Path(__file__).resolve().parent
x=here.parents[1]
r=x.parents[3]
files={
 'own_first':here/'INDEPENDENT-FIRST.md',
 'source':r/'publications/LULA-I/release/code/lula1/src/lib.rs',
 'selected_graph':x/'SELECTED-GRAPH-REDUCTION.md',
 'changed_child':x/'CHANGED-CHILD-EXTRACTION.md',
 'classical_pre':x/'CLASSICAL-PRE-REDUCTION.md',
 'primary_pdf':r/'M-measure/M2-sphincs-reparam/refs/eprint_2022_346_hulsing_kudinov_tight.pdf',
 'primary_text':r/'M-measure/M2-sphincs-reparam/refs/eprint_2022_346_hulsing_kudinov_tight.txt',
 'controls':here/'controls.py',
 'results':here/'CONTROL-RESULTS.json',
}
pins={k:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in files.items()}
assert pins['own_first']['sha256']=='991257503fc6d3f0bed2c03db64e4bbbe4e6c155c6da18ef4918ac7d8ffdbef2'
assert pins['source']['sha256']=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert pins['primary_pdf']['sha256']=='80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3'
assert pins['primary_text']['sha256']=='be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561'
results=json.loads(files['results'].read_text(encoding='utf-8'))
assert results['status']=='PASS' and results['fixed_public_function_worlds']==65536
obj={
 'status':'OWN_FIRST_MANUAL_CONDITIONAL_COLLECTION_TCR_IDENTIFICATION',
 'provenance':'Saved own derivation before reading any NEW peer graph proposal. Read only source, primary definitions and previously accepted graph/changed-child/PRE reductions.',
 'pins':pins,'controls_exit_code':0,
 'model':'HJ[h]: public fixed full256 algorithm; independent ideal private F/J',
 'ordinary_game':'HK22 Definitions2/7, SM-TCR of fixed-length collection members with one challenge and other-tweak pre-release Col access',
 'member_lengths_bits':[128,256,2048,2176,4096],
 'graph_bound':'Pr[Win AND G_final AND S!=0] <=2^56 sum_m Succ(B_m,p=1)',
 'hardness':'ASSUMED, not quantified for actual SHA',
 'remaining_PRE':'Same-input hidden preimage is not target collision; interior fixed-h predecessor law and unprogrammable previous-cell gap remain',
 'new_source_or_game_kernel_declarations':0,'old_scalar_changes':0,
 'first_requires_peer_review':True
}
(here/'OWN-RECEIPT.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'first_sha256':pins['own_first']['sha256'],'receipt_sha256':hashlib.sha256((here/'OWN-RECEIPT.json').read_bytes()).hexdigest(),'controls_sha256':pins['controls']['sha256'],'results_sha256':pins['results']['sha256']}))

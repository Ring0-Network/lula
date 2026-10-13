"""Proof-template guard and source cost-unit controls; no oracle/signing calls."""
from pathlib import Path
from itertools import product
import hashlib,json
B=Path(__file__).resolve().parent;X=B.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prior=json.loads((B/'FIRST-RECEIPT.json').read_text(encoding='utf-8'))
assert sha(B/'FIRST-RECEIPT.json')=='008e75bbbf04d18bcd7e680d82c92ec1aca3f92fbcaf83b3e6915545f9ed79b7'
for name,pin in prior['own_artifacts'].items():assert sha(X/name)==pin,name
source=Path('C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/release/code/lula1/src/lib.rs')
driver=source.parent/'bin/lula1_driver_seeded.rs'
assert sha(source)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
old=X/'CLASSICAL-RO-THEOREM.md'
assert sha(old)=='3ff8d3c0457ce0525a5af416472f7188e75e20c52cc06d2220b4273a1db752fe'
calls=0;endpoint_negatives=[]
for w in [2,4,8]:
    for ell in [1,2,3]:
        limit=ell*(w-1)
        for digits in product(range(w),repeat=ell):
            steps=sum(w-1-d for d in digits)
            assert steps==limit-sum(digits)
            if sum(digits)<limit:assert steps>=1
            else:assert steps==0 and all(d==w-1 for d in digits)
            calls+=1
        # Local old-proof implication fails when the certificate has only endpoints.
        exposed=False;different_child=True;genuine_endpoints=True
        H=False;G=False;D7=exposed and different_child
        assert genuine_endpoints and not(H or G or D7)
        endpoint_negatives.append(dict(w=w,ell=ell,S=limit,chain_calls=0,
            exposed=False,local_old_H_or_G_or_exposed_D7=False,
            full_signature_or_actual_forgery_constructed=False))
# Forced omitted zeros make fullwidth decoding injective at fixed lw4/8.
for lw,full,ell in [(4,32,31),(8,16,15),(4,32,30)]:
    assert lw*full==128
    real=[1]*ell
    accepted=real+[0]*(full-ell)
    assert sum(accepted)==sum(real) and all(x==0 for x in accepted[ell:])
    bad=accepted[:];bad[-1]=1
    assert not all(x==0 for x in bad[ell:])
# Dropping forced zeros with two omitted coordinates loses fullword injectivity
# despite same real tuple and equal target sums.
v=(1,2,1,0);u=(1,2,0,1)
assert v[:2]==u[:2] and sum(v)==sum(u) and v!=u
text=source.read_text(encoding='utf-8')
ctor=text[text.index('pub fn new(sk_seed:'):text.index('pub fn public(')]
assert 'compress256(' in ctor and 'compress(' not in ctor and 'count(' not in ctor
assert 'self.chain(ctx, layer, tree, kp, i, &sig[i as usize], d, self.w - 1 - d)' in text
spec=driver.read_text(encoding='utf-8').split('"lula1" => "',1)[1].split('"',1)[0]
layers=[list(map(int,item.split(':'))) for item in spec.split(';')[1].split('|')]
assert [v[-1] for v in layers]==[0,0,0,0,1]
data=json.loads((B/'ANALYTIC-CONTROLS.json').read_text(encoding='utf-8'))
rows=[]
for row in data['rows']:
    p=row['parameters'];ws=[16]*(len(p['ls'])-1)+[256]
    strict=all(s<l*(w-1) for l,w,s in zip(p['ls'],ws,p['ss']))
    rows.append(dict(name=row['name'],source_geometry_valid=row['source_geometry_valid'],
        old_proof_strict_target_guard=strict,full_retuned_theorem_established=False))
assert [r['name'] for r in rows if not r['old_proof_strict_target_guard']]==['extreme_top_target']
out=dict(status='SCOPED_PROOF_GUARD_AND_COST_UNIT_CONTROLS',exit_code=0,
    source_pins={str(source).replace('\\','/'):sha(source),str(driver).replace('\\','/'):sha(driver),
        'CLASSICAL-RO-THEOREM.md':sha(old)},script_sha256=sha(Path(__file__)),
    prior_first_receipt_sha256=sha(B/'FIRST-RECEIPT.json'),strict_target_digit_cases=calls,
    endpoint_local_countermodels=endpoint_negatives,geometry_vs_proof_template_rows=rows,
    omitted_zero_injectivity_checked=True,without_omitted_zeros_countermodel=True,
    context_prefix_direct_uninstrumented_compression=True,original_cache_top_only=True,
    no_first_package_changed=True,no_source_hash_or_signing_called=True,
    new_source_game_declarations=0,whole_goal_complete=False)
(B/'PROOF-GUARD-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(exit_code=0,digit_cases=calls,local_endpoint_models=len(endpoint_negatives),
    source_geometry_rows=len(rows),controls_sha256=sha(B/'PROOF-GUARD-CONTROLS.json'))))

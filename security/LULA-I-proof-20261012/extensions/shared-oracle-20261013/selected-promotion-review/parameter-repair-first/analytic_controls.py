"""Parameter geometry and exact finite coefficient controls; no crypto execution."""
from pathlib import Path
from math import comb,ceil
from fractions import Fraction as F
from itertools import product
import hashlib,json
import mpmath as mp
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(B/'INDEPENDENT-FIRST.md')=='869736c449aaff9ed24eb68e352fcff46bad784be4085b013c70c6db0ab7f842'
def coeff(w,l,s):
    if l==0:return int(s==0)
    if s<0 or s>l*(w-1):return 0
    return sum((-1)**j*comb(l,j)*comb(s-j*w+l-1,l-1) for j in range(min(l,s//w)+1))
def c(m):return ceil((22+16*m+9)/64)
def geometry(a,k,hs,ls,ss):
    ws=[16]*(len(hs)-1)+[256];full=[32]*(len(hs)-1)+[16]
    return (1<=a<=31 and k>=2 and (k-1)*(1<<a)<=1<<32 and k*a+sum(hs)<=256
        and len(hs)<=256 and 0<=sum(hs)<=63 and all(0<=h<=31 for h in hs)
        and k-1<=94 and len(ls)==len(hs)==len(ss)
        and all(1<=l<=f and l<=94 and 0<=s<=l*(w-1) for l,f,s,w in zip(ls,full,ss,ws)))
base=dict(a=9,k=18,hs=[5,5,5,5,21],ls=[32,32,32,32,16],ss=[240,240,240,240,2040])
variants={'original':base,
    'height42_top22':{**base,'hs':[5,5,5,5,22]},
    'k19_one_more_real':{**base,'k':19},
    'a10_more_leaves':{**base,'a':10},
    'four_layers_merged_bottom':{**base,'hs':[10,5,5,21],'ls':[32,32,32,16],'ss':[240,240,240,2040]},
    'lower_ell31_same_target':{**base,'ls':[31,31,31,31,16]},
    'extreme_top_target':{**base,'ss':[240,240,240,240,4080]}}
rows=[];toy=0
for w in [2,4]:
    for l in [2,3,4]:
        vectors=list(product(range(w),repeat=l))
        for s in range(l*(w-1)+1):
            vs=[v for v in vectors if sum(v)==s]
            assert coeff(w,l,s)==len(vs)
            assert all(not all(y[i]>=x[i] for i in range(l)) or y==x for x in vs for y in vs)
            toy+=1
        assert sum(coeff(w,l,s) for s in range(l*(w-1)+1))==w**l
negatives=[{**base,'hs':[5,5,5,5,32]}, {**base,'hs':[11,11,11,10,21]},
    {**base,'a':13,'k':19,'hs':[5,5,5,5,21]}, # ka+h=288
    {**base,'k':96}, {**base,'a':31,'k':4}, {**base,'ls':[33,32,32,32,16]}]
assert all(not geometry(**v) for v in negatives)
with mp.workdps(260):
    for name,p in variants.items():
        assert geometry(**p)
        a,k,hs,ls,ss=[p[j] for j in ['a','k','hs','ls','ss']];r=k-1;h=sum(hs);d=len(hs)
        ws=[16]*(d-1)+[256];full=[32]*(d-1)+[16]
        remaining=sum(l*(w-1)-s for l,w,s in zip(ls,ws,ss))
        H=r+remaining;G=r*(a+1)+1+remaining+d+h;constant=H+G+d+3
        sig=20+16*r*(a+1)+4*d+16*sum(ls)+16*h
        top=hs[-1];cache=16*((1<<(top+1))-1)+4*(1<<top)
        sub=[(1<<height)*(l*w+c(l))+(1<<height)-1 for height,l,w in zip(hs,ls,ws)]
        probs=[F(coeff(w,l,s),w**f) for w,l,s,f in zip(ws,ls,ss,full)]
        pm=[mp.mpf(v.numerator)/v.denominator for v in probs]
        C=1<<32;top_p=pm[-1]
        row_complete=-mp.expm1(C*mp.log1p(-top_p))
        log_setup=mp.mpf(1<<top)*mp.log(row_complete,2)
        # This Chernoff/union exponent is an upper bound on top-row failure;
        # may exceed1, and is capped only when interpreting probability.
        failure_log=top-C*top_p/mp.log(2)
        exact_cp=probs[-1]*C
        integer_failure_exponent=top-exact_cp.numerator//exact_cp.denominator
        bounded_means=[-mp.expm1(C*mp.log1p(-v))/v for v in pm]
        fors_pk=r*(3*(1<<a)-1)+c(r);fors_sign=3*r*(1<<a)+c(r)
        prepared_all=fors_sign+sum(1+l+s for l,s in zip(ls,ss))
        actual_top_cache=prepared_all+sum(sub[i]+bounded_means[i] for i in range(d-1))
        verify=r*(a+1)+c(r)+sum(l*(w-1)-s+c(l)+height+1 for l,w,s,height in zip(ls,ws,ss,hs))
        coverage=[]
        for lq in [38,40,41]:
            q=1<<lq;t=mp.mpf(1<<a);instances=mp.mpf(2)**h
            pf=mp.fsum((-1)**j*comb(r,j)*mp.exp(q*mp.log1p(-(1-(1-1/t)**j)/instances)) for j in range(r+1))/t
            assert pf>0
            coverage.append(dict(log2_q=lq,FORS_per_candidate_exponent=float(-mp.log(pf,2))))
        rows.append(dict(name=name,parameters=p,source_geometry_valid=True,
            signature_bytes=sig,top_cache_payload_bytes=cache,H_final=H,G_final=G,
            prospective_joint_constant=constant,full_theorem_generalization='OPEN',
            subtree_compressions=sub,FORS_pk_compressions=fors_pk,FORS_sign_compressions=fors_sign,
            all_prepared_addressed_sign_compressions=prepared_all,
            top_only_cache_addressed_sign_bounded_mean_display=mp.nstr(actual_top_cache,35),
            addressed_verify_compressions=verify,top_row_acceptance=[str(probs[-1].numerator),str(probs[-1].denominator)],
            top_setup_completion_log2_display=mp.nstr(log_setup,30),
            top_row_failure_union_log2_upper_display=mp.nstr(failure_log,30),
            top_row_failure_union_exact_power_two_upper_exponent=integer_failure_exponent,
            canonical_bounded_evaluation_means_display=[mp.nstr(v,30) for v in bounded_means],
            FORS_filter_union_failure_power_two_upper_exponent_at_q40=40-((1<<32)//(1<<a)),
            FORS_component_only=coverage,full_security_certified=False))
original=rows[0]
assert (original['signature_bytes'],original['top_cache_payload_bytes'],original['H_final'],original['G_final'],original['prospective_joint_constant'])==(5720,75497456,3017,3217,6242)
assert original['subtree_compressions'][-1]==8602517503
assert rows[1]['signature_bytes']==5736 and rows[2]['signature_bytes']==5880 and rows[3]['signature_bytes']==5992
assert rows[4]['prospective_joint_constant']==5760 and rows[4]['signature_bytes']==5204
assert rows[-1]['top_row_acceptance']==['1',str(1<<128)]
assert F(2*(1<<38),1<<128)>F(1,1<<128)
out=dict(status='SOURCE_PARAMETER_ANALYTIC_CONTROLS_NOT_REPAIR_CERTIFICATE',script_sha256=sha(Path(__file__)),
    independent_first_sha256=sha(B/'INDEPENDENT-FIRST.md'),toy_coefficient_antichain_cases=toy,
    invalid_geometry_cases=len(negatives),rows=rows,
    cost_scope='Compression counts/finite-counter expectation and logical payload only;exclude message prehash,outer FORS grind,allocation/RSS and physical runtime.',
    setup_scope='Top canonical row completion only,not entire setup;union failure bound is explicitly an upper bound.',
    fixed_n=16,new_parameter_set_adopted=False,full_security_or_category_certified=False,
    new_source_game_declarations=0,whole_goal_complete=False,exit_code=0)
(B/'ANALYTIC-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
lines=['# Parameter alternatives: analytic costs only','','No row is a certified full-security repair.','',
 '|alternative|signature B|top cache payload B|H final|G final|joint constant candidate|FORS exponent atq40|','|---|---:|---:|---:|---:|---:|---:|']
for r in rows:lines.append(f"|{r['name']}|{r['signature_bytes']}|{r['top_cache_payload_bytes']}|{r['H_final']}|{r['G_final']}|{r['prospective_joint_constant']}|{r['FORS_component_only'][1]['FORS_per_candidate_exponent']:.9f}|")
(B/'ALTERNATIVES.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines));print('SHA256',sha(B/'ANALYTIC-CONTROLS.json'))

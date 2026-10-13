"""Guarded exact-binomial classical envelope; no signing/graph/timing work.

All outputs are numerical evaluations of the stated conditional source-RO bound,
not attacks, capacity/category certificates, or implemented parameter repairs.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import argparse,copy,hashlib,json,sys
import mpmath as mp

E=Path(__file__).resolve().parent;X=E.parent.parent
R=X.parents[3];SOURCE=R/'publications/LULA-I/release/code/lula1/src/lib.rs'
N=1<<128;CTR=1<<32;GRID=(24,30,38,40,41,44,50,64)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def integer(x,name,lo=0,hi=None):
    if type(x) is not int or x<lo or (hi is not None and x>hi):raise ValueError(name)
    return x
@lru_cache(None)
def coefficient(ell,w,target):
    return sum((-1)**j*comb(ell,j)*comb(target-j*w+ell-1,ell-1) for j in range(min(ell,target//w)+1))
def guard(p):
    if set(p)!={'label','a','k','layers'}:raise ValueError('exact parameter schema')
    if not isinstance(p['label'],str) or not p['label']:raise ValueError('label')
    a=integer(p['a'],'a',1,31);k=integer(p['k'],'k',2);r=k-1
    layers=p['layers']
    if not isinstance(layers,list) or not 1<=len(layers)<=256:raise ValueError('d/layer byte')
    if r>94 or r*(1<<a)>1<<32:raise ValueError('FORS root scratch/global index')
    h=0;tails=[];accept=[];seen_cached=False
    for i,l in enumerate(layers):
        if set(l)!={'h','ell','S','cached'}:raise ValueError('exact layer schema')
        hi=integer(l['h'],'individual height',0,31);h+=hi
        lw=8 if i==len(layers)-1 else 4;full=128//lw;w=1<<lw
        ell=integer(l['ell'],'ell',1,full);s=integer(l['S'],'strict target',0,ell*(w-1)-1)
        if type(l['cached']) is not bool:raise ValueError('cached boolean')
        if seen_cached and not l['cached']:raise ValueError('cache must be a top segment')
        seen_cached|=l['cached']
        c=coefficient(ell,w,s)
        if c<=0:raise ValueError('empty acceptance predicate')
        if (22+16*ell+9+63)//64>24:raise ValueError('WOTS PK tail buffer')
        tails.append(ell*(w-1)-s)
        accept.append(dict(lw=lw,w=w,full_digits=full,real_digits=ell,zero_digits=full-ell,
                           coefficient=str(c),theta_numerator=str(c),theta_denominator=str(N),
                           denominator_is_full_128_bits=True))
    if h>63 or k*a+h>256:raise ValueError('route/digest width')
    if (22+16*r+9+63)//64>24:raise ValueError('FORS root tail buffer')
    H=r+sum(tails);G=r*(a+1)+1+sum(t+1+l['h'] for t,l in zip(tails,layers))
    C=H+G+len(layers)+3
    assert C==r*(a+2)+2*sum(tails)+h+2*len(layers)+4 and C>=11
    sig=16+4+16*r*(a+1)+sum(4+16*(l['ell']+l['h']) for l in layers)
    return dict(a=a,k=k,r=r,h=h,d=len(layers),H_fin=H,G_fin=G,D7_fin=len(layers),C_p=C,
                signature_bytes=sig,acceptance=accept,
                runtime_scope='64-bit source schema, guarded indices/buffers; finite canonical partiality and absorbing setup/signing failure retained; no memory or availability certificate')
def frac_tuple(t):
    sign,mant,exp,bc=t;assert sign==0 and (mant==0 or mant.bit_length()==bc)
    return F(mant<<exp) if exp>=0 else F(mant,1<<(-exp))
def interval_tuple(v):return [list(t) for t in v._mpi_]
def iv_from_fraction(x):return mp.iv.mpf(x.numerator)/x.denominator
def point_from_fraction(x):return mp.mpf(x.numerator)/x.denominator
def exact_binomial(q,g):
    integer(q,'q');a=g['a'];r=g['r'];h=g['h'];t=1<<a
    mp.iv.dps=480
    beta=mp.iv.mpf(t-1)/t;rho=mp.iv.mpf(1)/(1<<h)
    if q==0:iv=mp.iv.mpf(0)
    else:
        iv=sum(((-1)**j*comb(r,j))*((1+rho*(beta**j-1))**q) for j in range(r+1))/t
    lo,hi=map(frac_tuple,iv._mpi_)
    lower=F(0) if q==0 else F(1,1<<(g['k']*a+h))
    lo=max(lo,lower);hi=min(hi,F(1,t));assert lo<=hi
    with mp.workdps(600):
        b=mp.mpf(t-1)/t;rh=mp.mpf(1)/(1<<h)
        pf=mp.mpf(0) if q==0 else mp.fsum((-1)**j*comb(r,j)*mp.exp(q*mp.log1p(rh*(b**j-1))) for j in range(r+1))/t
        assert point_from_fraction(lo)<=pf<=point_from_fraction(hi)
        if pf:assert point_from_fraction(hi-lo)/pf<mp.mpf('1e-300')
        value=mp.nstr(pf,220)
    return iv_from_fraction(lo)+mp.iv.mpf([0,1])*iv_from_fraction(hi-lo),F(lo),F(hi),value,pf
def one_row(p,g,qe,Qe,pf_data):
    q=1<<qe;Q=1<<Qe;pfiv,pflo,pfhi,pfstr,pfpoint=pf_data
    integer(Q,'Q')
    linear=F(3*Q+2*q+g['C_p'],N);pairs=F(q*Q+comb(q,2)+q,N*N)
    mp.iv.dps=480;miss=(mp.iv.mpf((1<<g['a'])-1)/(1<<g['a']))**CTR
    uncap=iv_from_fraction(linear+pairs)+q*miss+(Q+1)*pfiv
    lo,hi=map(frac_tuple,uncap._mpi_);caplo=min(F(1),lo);caphi=min(F(1),hi)
    with mp.workdps(600):
        pf=pfpoint
        e=mp.exp(CTR*mp.log1p(-mp.mpf(2)**-g['a']))
        u=point_from_fraction(linear+pairs)+q*e+(Q+1)*pf
        cap=min(mp.mpf(1),u)
        assert point_from_fraction(lo)<=u<=point_from_fraction(hi)
        prob=mp.nstr(cap,180);exponent=mp.nstr(-mp.log(cap,2),90)
    return dict(status='COMPUTED',parameter_label=p['label'],q_exponent=qe,Q_exponent=Qe,
                q=str(q),Q=str(Q),C_p=g['C_p'],linear_numerator=str(3*Q+2*q+g['C_p']),
                pair_numerator=str(q*Q+comb(q,2)+q),pF_exact_binomial_display=pfstr,
                pF_interval_dyadic=[interval_tuple(pfiv)[0],interval_tuple(pfiv)[1]],
                finite_outer_exhaustion_interval_dyadic=interval_tuple(miss),
                uncapped_interval_dyadic=interval_tuple(uncap),
                capped_interval_rational=[[str(x.numerator),str(x.denominator)] for x in (caplo,caphi)],
                probability_upper_envelope=prob,negative_log2_probability_envelope_not_security_bits=exponent,
                adequate_tiny_gate=False,parameter_repair=False,implemented_or_measured_variant=False)
def baseline_regression(rows,pfs):
    oldpath=E.parent/'classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json'
    old=json.loads(oldpath.read_text(encoding='utf8'));assert old['subject_sha256']=='4fa7c3b63a268bd7535a753813d109a2f768f0089df44b54223a6e34cfaf35f0'
    for row,prior in zip(rows,old['rows']):
        assert (row['q_exponent'],row['Q_exponent'])==(prior['q_exponent'],prior['QH_exponent'])
        assert row['linear_numerator']==prior['linear_numerator'] and row['pair_numerator']==prior['pair_numerator']
        with mp.workdps(300):
            now=mp.mpf(row['probability_upper_envelope']);before=mp.mpf(prior['own_numeric_probability'])
            assert abs(now-before)/before<mp.mpf('1e-175')
    crossings=[]
    # Exact affine outward threshold propagation; the baseline exhaustion is
    # bounded by 2^-4096 using (1-1/512)^512<1/2, without giant integer powers.
    for qe,prior in zip(GRID,old['half_success_crossings']):
        q=1<<qe;_,lo,hi,_,_=pfs[qe]
        def coeff(pf,e):return F(3,N)+F(q,N*N)+pf,F(2*q+6242,N)+F(comb(q,2)+q,N*N)+pf+e
        al,bl=coeff(lo,F(0));ah,bh=coeff(hi,F(q,1<<4096))
        tl=(F(1,2)-bh)/ah;th=(F(1,2)-bl)/al
        Qpass=tl.numerator//tl.denominator;Qother=th.numerator//th.denominator
        assert Qpass==Qother==int(prior['Q_pass'])
        assert ah*Qpass+bh<=F(1,2)<al*(Qpass+1)+bl
        crossings.append(dict(q_exponent=qe,Q_pass=str(Qpass),Q_fail=str(Qpass+1),exact_adjacent_rational_certificate=True))
    return dict(rows=24,all_accepted_baseline_rows_recovered=True,old_dataset_sha256=sha(oldpath),half_success_crossings=crossings)
BASE=dict(label='baseline',a=9,k=18,layers=[dict(h=5,ell=32,S=240,cached=False) for _ in range(4)]+[dict(h=21,ell=16,S=2040,cached=True)])
def examples():
    out=[copy.deepcopy(BASE)]
    p=copy.deepcopy(BASE);p['label']='illustrative_top20';p['layers'][-1]['h']=20;out.append(p)
    p=copy.deepcopy(BASE);p['label']='illustrative_a10';p['a']=10;out.append(p)
    p=copy.deepcopy(BASE);p['label']='illustrative_shortened_lower_ell';
    for l in p['layers'][:-1]:l.update(ell=16,S=120)
    out.append(p)
    out.append(dict(label='guard_edge_zero_height_one_layer',a=1,k=2,layers=[dict(h=0,ell=1,S=254,cached=False)]))
    p=copy.deepcopy(BASE);p.update(label='guard_edge_large_a_exhaustion',a=31,k=2);out.append(p)
    return out
def guard_controls():
    bad=[]
    for name,edit in [('a0',lambda p:p.update(a=0)),('a32',lambda p:p.update(a=32)),('k1',lambda p:p.update(k=1)),('empty_layers',lambda p:p.update(layers=[])),('max_target',lambda p:p['layers'][0].update(S=480)),('ell0',lambda p:p['layers'][0].update(ell=0)),('ell33',lambda p:p['layers'][0].update(ell=33)),('height32',lambda p:p['layers'][0].update(h=32)),('bad_top_segment',lambda p:(p['layers'][0].update(cached=True),p['layers'][1].update(cached=False))),('bool_as_a',lambda p:p.update(a=True)),('tail_root95',lambda p:p.update(k=96,a=1)),('digest_overflow',lambda p:p.update(a=16,k=18)),('global_fors_overflow',lambda p:p.update(a=31,k=4))]:
        p=copy.deepcopy(BASE);edit(p)
        try:guard(p)
        except ValueError:bad.append(name)
        else:raise AssertionError(name)
    for p in examples():guard(p)
    # A zero-query envelope still has C/N>1/N; pF(q0) is exactly zero.
    g=guard(BASE);iv,lo,hi,val,_=exact_binomial(0,g);assert lo==hi==0
    return dict(rejected_invalid_inputs=bad,accepted_examples=len(examples()),q0_pF_zero=True)
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--parameters',type=Path);ap.add_argument('--output',type=Path,default=E/'OWN-UNIFORM-NUMERICS.json');args=ap.parse_args()
    assert mp.__version__=='1.3.0'
    assert sha(SOURCE)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
    params=[json.loads(args.parameters.read_text(encoding='utf8'))] if args.parameters else examples()
    records=[];baseline=None
    controls=guard_controls()
    for p in params:
        g=guard(p);pfs={qe:exact_binomial(1<<qe,g) for qe in GRID}
        rows=[one_row(p,g,qe,Qe,pfs[qe]) for qe in GRID for Qe in (32,64,128)]
        if p==BASE:baseline=baseline_regression(rows,pfs)
        records.append(dict(status='COMPUTED_ILLUSTRATIVE_NOT_REPAIR' if p!=BASE else 'COMPUTED_ACCEPTED_BASELINE_REGRESSION',parameters=p,derived=g,rows=rows))
    gate=F(N,6)
    result=dict(status='OWN_GUARDED_EXACT_BINOMIAL_DATA_SAVED_BEFORE_NEW_FINAL_ROOT_SUBJECT_READ',script_sha256=sha(Path(__file__)),first_sha256=sha(E/'INDEPENDENT-FIRST.md'),source_sha256=sha(SOURCE),accepted_joint_subject_sha256=sha(X/'CLASSICAL-JOINT-RO-THEOREM.md'),mpmath_version=mp.__version__,interval_dps=480,point_dps=600,q_grid=list(GRID),Q_grid=[32,64,128],guard_controls=controls,parameter_records=records,baseline_regression=baseline,feasibility=dict(status='PROVED_ANALYTIC_NECESSITY_FOR_THIS_ENVELOPE',formula='0<tau<1 and min(1,U)<=tau imply Q<=floor(tau*N/3); positive remainder requires 3Q/N<tau',universal_C_lower=11,half_success_Q_necessary_max=str(gate.numerator//gate.denominator),tiny_tau_one_over_N_no_tuple_passes=True,Q_equal_N_all_envelopes_cap_one=True,not_attack_or_actual_insecurity=True),all_old_rows_preserved=True,new_measurements_or_source_runs=0,new_final_root_subject_read=False,QROM_retuning=False,repair_or_category_established=False,whole_goal_complete=False)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    lines=['# Independent guarded uniform classical numerics','','COMPUTED probability upper envelopes, not security levels. All nonbaseline cases are illustrative, unimplemented and not repairs.','', '| parameter | log2 q | log2 Q | -log2 capped envelope |','|---|---:|---:|---:|']
    for rec in records:
        for row in rec['rows']:lines.append(f"| {rec['parameters']['label']} | {row['q_exponent']} | {row['Q_exponent']} | {float(row['negative_log2_probability_envelope_not_security_bits']):.12f} |")
    (E/'OWN-UNIFORM-NUMERICS.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print(json.dumps(dict(status=result['status'],parameter_shapes=len(records),rows=sum(len(r['rows']) for r in records),baseline_rows_recovered=24 if baseline else None,baseline_adjacent_crossings=8 if baseline else None,sha256=sha(args.output))))
if __name__=='__main__':main()

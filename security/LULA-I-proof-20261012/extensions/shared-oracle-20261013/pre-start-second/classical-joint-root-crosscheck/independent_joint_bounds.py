"""Own affine exact classical ledger checks; no source/attack runs."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json
import mpmath as mp
E=Path(__file__).resolve().parent;X=E.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert mp.__version__=='1.3.0'
N=1<<128;exponents=(24,30,38,40,41,44,50,64)
source=X/'classical-composition-numeric/OWN-BOUNDS.json'
assert sha(source)=='9859f7e201402d8b53539bb16144add8016c7f889d923add947289dad94e50fd'
def exact_mpf(t):
    sign,mant,exp,length=t
    assert sign==0 and mant.bit_length()==length
    return F(mant*(1<<exp)) if exp>=0 else F(mant,1<<(-exp))
PF={}
for r in read(source)['rows']:
    a=r['FORS_per_raw_candidate'];qe=r['log2_signing_query_cap']
    interval=tuple(exact_mpf(a[key]) for key in ('lower_dyadic_mpf_tuple','upper_dyadic_mpf_tuple'))
    assert 0<=interval[0]<=interval[1]<=F(1,512)
    if qe in PF:assert PF[qe]==interval
    PF[qe]=interval
assert set(PF)==set(exponents)
def m(f):return mp.mpf(f.numerator)/f.denominator
def serial(f):return [str(f.numerator),str(f.denominator)]
def moment(q):
    z=mp.mpf(511)/512;bucket=mp.mpf(1)/(1<<41)
    return mp.fsum([(-1)**j*comb(17,j)*mp.exp(q*mp.log1p(-bucket*(1-z**j))) for j in range(18)])/512
def positive(q,pf):
    rho=mp.mpf(1)/(1<<41);mu=q*rho;ln_miss=mp.log(mp.mpf(511)/512)
    if mu>4096:
        deficit=mp.exp(-mu/8)+17*mp.exp(-mu/(2*512))
        lower=(1-mp.exp(-mu/8))*(-mp.expm1(mu*ln_miss/2))**17/512
        assert lower<=pf<=mp.mpf(1)/512
        return {'method':'own analytic saturation control','fractional_deficit_upper':mp.nstr(deficit,100)}
    limit=min(q,max(2400,int(mu+100*mp.sqrt(mu+1)+1800)))
    mass=mp.exp(q*mp.log1p(-rho));acc=mp.mpf(0)
    for r in range(1,limit+1):
        mass*=mp.mpf(q-r+1)*rho/(r*(1-rho))
        acc+=mass*(-mp.expm1(r*ln_miss))**17
    L=limit+1;tail=mp.exp(-mu+L*(1+mp.log(mu/L))) if limit<q else mp.mpf(0)
    rel=abs(acc/512-pf)/pf
    assert rel<mp.mpf('1e-500')
    return {'method':'own positive binomial recurrence','stop':limit,'tail_upper':mp.nstr(tail,100),'relative_difference':mp.nstr(rel,60)}
def coefficients(q,pf,exhaust):
    return F(3,N)+F(q,N*N)+pf, F(2*q+6242,N)+F(comb(q,2)+q,N*N)+pf+exhaust
def interval(q,Q):
    lo_a,lo_b=coefficients(q,PF[q.bit_length()-1][0],F(0))
    hi_a,hi_b=coefficients(q,PF[q.bit_length()-1][1],F(q,1<<4096))
    return lo_a*Q+lo_b,hi_a*Q+hi_b
rows=[];crossings=[];pchecks=[]
for qe in exponents:
    q=1<<qe
    with mp.workdps(620):
        pf=moment(q)
        assert m(PF[qe][0])<=pf<=m(PF[qe][1])
        ctrl=positive(q,pf)
        exhaustion=q*mp.exp((1<<32)*mp.log(mp.mpf(511)/512))
        pvalue=mp.nstr(pf,220)
    with mp.workdps(760):
        pf_high=moment(q)
        relative=abs(pf_high-pf)/pf_high
        assert relative<mp.mpf('1e-500')
        pchecks.append({'q_exponent':qe,'own_pF_display':pvalue,'higher_precision_relative_difference':mp.nstr(relative,60),
                        'inherited_exact_dyadic_enclosure':[serial(z) for z in PF[qe]],'own_positive_or_saturation_control':ctrl})
        for ae in (32,64,128):
            Q=1<<ae
            num_linear=3*Q+2*q+6242;num_pair=q*Q+comb(q,2)+q
            lo,hi=interval(q,Q)
            numeric=m(F(num_linear,N)+F(num_pair,N*N))+(Q+1)*pf_high+exhaustion
            assert m(lo)<=numeric<=m(hi)
            bound=min(mp.mpf(1),numeric)
            old_difference=F(3*Q+q+1,N)
            assert old_difference>0
            rows.append({'q_exponent':qe,'QH_exponent':ae,'q':str(q),'QH':str(Q),
             'linear_numerator':str(num_linear),'pair_numerator':str(num_pair),
             'own_numeric_probability':mp.nstr(bound,220),
             'own_probability_exponent_not_security_bits':mp.nstr(-mp.log(bound,2),90),
             'uncapped_lower':serial(lo),'uncapped_upper':serial(hi),
             'capped_lower':serial(min(F(1),lo)),'capped_upper':serial(min(F(1),hi)),
             'old_minus_new_uncapped_exact':serial(old_difference),
             'inherited_pF_premise':True,'own_affine_scalar_and_interval_propagation':True})
        ah,bh=coefficients(q,PF[qe][1],F(q,1<<4096))
        al,bl=coefficients(q,PF[qe][0],F(0))
        real_upper=(F(1,2)-bh)/ah;real_lower=(F(1,2)-bl)/al
        passed=real_upper.numerator//real_upper.denominator
        # Upper-expression threshold <= actual threshold <= lower-expression threshold.
        assert passed==real_lower.numerator//real_lower.denominator
        failed=passed+1
        plo,phi=interval(q,passed);flo,fhi=interval(q,failed)
        assert phi<=F(1,2)<flo
        crossings.append({'q_exponent':qe,'Q_pass':str(passed),'Q_fail':str(failed),
          'pass_interval':[serial(plo),serial(phi)],'fail_interval':[serial(flo),serial(fhi)],
          'pass_margin':serial(F(1,2)-phi),'fail_margin':serial(flo-F(1,2)),
          'floor_of_both_outward_affine_thresholds_identical':True,
          'adjacent_half_success_gate_certified_exact':True})
assert len(rows)==24 and len(crossings)==8
assert all(r['capped_lower']==['1','1']==r['capped_upper'] for r in rows if r['QH_exponent']==128)
out={'status':'OWN24_JOINT_ROWS_AND8_EXACT_AFFINE_HALF_SUCCESS_CROSSINGS_SAVED_BEFORE_NEW_ROOT_READ',
 'own_first_sha256':sha(E/'INDEPENDENT-FIRST.md'),'script_sha256':sha(Path(__file__)),
 'subject_sha256':sha(X/'CLASSICAL-JOINT-RO-THEOREM.md'),'inherited_pF_input_sha256':sha(source),
 'arithmetic':'Own affine numerator/Fraction propagation; inherited certified pF dyadics decoded independently; own620/760dps moment+positive/saturation controls',
 'exhaustion_enclosure':'0<=q*(511/512)^(2^32)<q*2^-4096, independently derived by Bernoulli inequality',
 'mpmath_dps':620,'stability_dps':760,'rows':rows,'half_success_crossings':crossings,'pF_controls':pchecks,
 'QH_exponents':[32,64,128],'q_exponents':list(exponents),
 'selected_reviewed_dataset_read_as_authorized_input':True,
 'new_root_joint_calculator_or_data_read':False,
 'new_source_game_declarations':0,'whole_goal_complete':False,'category':'not established','source_or_attack_runs':0}
(E/'OWN-JOINT-NUMERICS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
text=['# Own classical joint scalar crosscheck','',
 'COMPUTED probability upper bounds, not security levels. Exact rational scalar enclosures inherit reviewed pF intervals;620/760-digit moment checks and affine propagation are own. Required Q_H=2^128 rows are included.','',
 '| log2 q | log2 Q_H | probability-bound exponent |','|---:|---:|---:|']
for r in rows:text.append(f"| {r['q_exponent']} | {r['QH_exponent']} | {float(r['own_probability_exponent_not_security_bits']):.12f} |")
text+=['','| log2 q | Q pass at1/2 | adjacent Q fail |','|---:|---:|---:|']
for r in crossings:text.append(f"| {r['q_exponent']} | {r['Q_pass']} | {r['Q_fail']} |")
(E/'OWN-JOINT-NUMERICS.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'rows':24,'exact_crossings':8,'QH128_all_cap1':True,'Q_pass':[r['Q_pass'] for r in crossings]}))

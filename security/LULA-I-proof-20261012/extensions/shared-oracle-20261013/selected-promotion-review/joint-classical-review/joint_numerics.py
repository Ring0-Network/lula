"""New joint candidate arithmetic only; immutable historical calculators untouched."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json
import mpmath as mp
B=Path(__file__).resolve().parent;X=B.parents[1];N=1<<128
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
oldpath=X/'classical-composition-numeric/OWN-BOUNDS.json'
assert sha(oldpath)=='9859f7e201402d8b53539bb16144add8016c7f889d923add947289dad94e50fd'
def dyadic(t):
    s,m,e,b=t;assert s==0 and m.bit_length()==b
    return F(m<<e) if e>=0 else F(m,1<<(-e))
PF={}
for r in json.loads(oldpath.read_text(encoding='utf-8'))['rows']:
    pair=tuple(dyadic(r['FORS_per_raw_candidate'][n]) for n in ['lower_dyadic_mpf_tuple','upper_dyadic_mpf_tuple'])
    k=r['log2_signing_query_cap'];assert k not in PF or PF[k]==pair;PF[k]=pair
def frac(v):return [str(v.numerator),str(v.denominator)]
def m(v):return mp.mpf(v.numerator)/v.denominator
def enclosure(q,Q,p):
    linear=F(3*Q+2*q+6242,N);pairs=F(q*Q+q*(q-1)//2+q,N*N)
    lo=linear+pairs+(Q+1)*p[0]
    hi=linear+pairs+(Q+1)*p[1]+F(q,1<<4096)
    return lo,hi
def detail(lo,hi):
    return dict(lower_rational=frac(lo),upper_rational=frac(hi),
        capped_lower_rational=frac(min(F(1),lo)),capped_upper_rational=frac(min(F(1),hi)))
rows=[];crossings=[]
with mp.workdps(600):
    for k in [24,30,38,40,41,44,50,64]:
        q=1<<k;p=PF[k];t=mp.mpf(512);cells=mp.mpf(2)**41
        recomputed=mp.fsum([(-1)**j*comb(17,j)*mp.exp(q*mp.log1p(-(1-(1-1/t)**j)/cells)) for j in range(18)])/t
        assert m(p[0])<=recomputed<=m(p[1]),k
        for lQ in [32,64]:
            Q=1<<lQ;lo,hi=enclosure(q,Q,p)
            oldminusnew=F(3*Q+q+1,N)
            assert oldminusnew>0
            display=min(mp.mpf(1),m(F(3*Q+2*q+6242,N)+F(q*Q+q*(q-1)//2+q,N*N))+(Q+1)*recomputed)
            rows.append(dict(log2_q=k,log2_Q=lQ,FORS_per_candidate_exponent=float(-mp.log(recomputed,2)),
                joint_probability_display=mp.nstr(display,60),joint_probability_exponent_display=float(-mp.log(display,2)),
                old_minus_new_uncapped_linear=frac(oldminusnew),**detail(lo,hi)))
        # Uncapped expression is affine in Q. Calculate from upper enclosure, then
        # prove PASS and adjacent FAIL using exact inherited FORS brackets.
        slopehi=F(3,N)+F(q,N*N)+p[1]
        intercept_hi=F(2*q+6242,N)+F(q*(q-1)//2+q,N*N)+p[1]+F(q,1<<4096)
        v=(F(1,2)-intercept_hi)/slopehi
        passed=max(0,v.numerator//v.denominator);failed=passed+1
        plo,phi=enclosure(q,passed,p);flo,fhi=enclosure(q,failed,p)
        assert phi<=F(1,2)<flo,(k,passed)
        crossings.append(dict(log2_q=k,Q_pass=str(passed),Q_fail=str(failed),
            log2_Q_pass_display=float(mp.log(passed,2)),pass_interval=detail(plo,phi),fail_interval=detail(flo,fhi),
            pass_margin_lower=frac(F(1,2)-phi),fail_margin_lower=frac(flo-F(1,2)),adjacent_certified=True))
out=dict(status='EXACT_RATIONAL_JOINT_CANDIDATE_ARITHMETIC_NOT_PROMOTED',
    input_pins={'classical-composition-numeric/OWN-BOUNDS.json':sha(oldpath)},script_sha256=sha(Path(__file__)),
    arithmetic='Exact Fraction arithmetic inherits previously certified finite-binomial FORS outward dyadic brackets;600-digit separate finite-binomial reevaluation lies inside each bracket.',
    exhaustion='Enclosed by0<=q*(511/512)^(2^32)<=q*2^-4096;display excludes this negligible enclosure only.',
    probability_exponents_are_not_security_bits=True,rows=rows,half_success_crossings=crossings,
    new_checked_declarations=0,new_source_game_declarations=0,whole_goal_complete=False)
(B/'JOINT-NUMERICS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
lines=['# Joint classical candidate: independent arithmetic','','Probability exponents describe sufficient bounds, not security levels. Historical scalar files are unchanged.','',
 '|log2 q|log2 Q|joint probability exponent|','|---:|---:|---:|']
for r in rows:lines.append(f"|{r['log2_q']}|{r['log2_Q']}|{r['joint_probability_exponent_display']:.9f}|")
lines+=['','Eight adjacent half-success expression crossings are certified with exact rational inherited FORS intervals.','',
 '|log2 q|Q pass (bound <=1/2)|Q fail (bound >1/2)|log2 Q pass|','|---:|---:|---:|---:|']
for r in crossings:lines.append(f"|{r['log2_q']}|{r['Q_pass']}|{r['Q_fail']}|{r['log2_Q_pass_display']:.9f}|")
(B/'JOINT-NUMERICS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines));print('SHA256',sha(B/'JOINT-NUMERICS.json'))

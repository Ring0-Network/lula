"""Root arithmetic review against an independently saved rational certificate.

This is a second implementation/check, not a second blind derivation of FORS.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import mpmath as mp

HERE=Path(__file__).resolve().parent
X=HERE.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=X/'query-resource-independent/THRESHOLDS.json'
data=json.loads(source.read_text(encoding='utf8'))
assert data['script_sha256']==sha(X/'query-resource-independent/thresholds.py')
for name,digest in data['input_pins'].items(): assert sha(X/name)==digest,name
fdata=json.loads((X/'classical-composition-numeric/OWN-BOUNDS.json').read_text())
def dyadic(t):
    sign,m,e,b=t
    assert sign==0 and m.bit_length()==b
    return Fraction(m*(1<<e),1) if e>=0 else Fraction(m,1<<(-e))
fs={r['log2_signing_query_cap']:dyadic(r['FORS_per_raw_candidate']['lower_dyadic_mpf_tuple']) for r in fdata['rows']}
def rational(a): return Fraction(int(a[0]),int(a[1]))
def mpr(a): return mp.mpf(a.numerator)/a.denominator
def evaluate(q,Q,p):
    N=mp.mpf(1<<128); q=mp.mpf(q); Q=mp.mpf(Q)
    cRO=min(1,(6*Q+3*q+6243)/N+(q*Q+q*(q-1)/2+q)/(N*N)
        +q*mp.exp((1<<32)*mp.log(mp.mpf(511)/512))+(Q+1)*p)
    DD=min(1,q*(mp.sqrt((Q+q+1)/(N*N-N))+(Q+q+1)/(2*(N*N-N))))
    AA=min(1,DD+8*(Q+2)**2*(p+1/N+q/(N*N)))
    CC=min(1,(2*Q+mp.sqrt(q))**2/N+(2*(Q+2)/mp.sqrt(N)+mp.sqrt(AA))**2)
    HH=min(1,(2*Q+mp.sqrt(3017))**2/N)
    GG=min(1,8*(Q+3218)**2/N)
    ZZ=min(1,8*(Q+6)**2/N)
    coarse=min(1,1/N+min(1,2*Q/mp.sqrt(N)+(2*q+2)/N)+CC+HH+GG+ZZ)
    rare=min(1,1/N+(2*Q/mp.sqrt(N)+mp.sqrt(min(1,min(1,(2*q+2)/N)+min(1,CC+HH+GG+ZZ))))**2)
    return {'classical':cRO,'quantum_conservative':coarse,'quantum_event':rare,'quantum_best':min(coarse,rare)}

checks=[]
with mp.workdps(240):
    for r in data['rows']:
        lo=int(r['Q_pass']); hi=int(r['Q_fail']); q=int(r['q'])
        assert hi==lo+1 and r['adjacent_integer_crossing_certified']
        pass_hi=rational(r['pass_bound']['upper_rational'])
        fail_lo=rational(r['fail_bound']['lower_rational'])
        assert pass_hi<=Fraction(1,2)<fail_lo
        assert rational(r['pass_margin_lower'])==Fraction(1,2)-pass_hi
        assert rational(r['fail_margin_lower'])==fail_lo-Fraction(1,2)
        p=mpr(fs[r['log2_q']])
        a=evaluate(q,lo,p)[r['model']]; b=evaluate(q,hi,p)[r['model']]
        assert a<=mp.mpf('.5')<b
        # The inherited interval is far narrower than the exact endpoint margins.
        assert abs(a-mpr(pass_hi))<mp.mpf('1e-70')
        assert abs(b-mpr(fail_lo))<mp.mpf('1e-70')
        checks.append({'log2_q':r['log2_q'],'model':r['model'],'Q_pass':str(lo),'Q_fail':str(hi),'exact_fraction_comparisons':True,'independent_240_digit_formula_evaluation':True})
assert len(checks)==32
record={'status':'PASS_ALL32_ADJACENT_RATIONAL_QUERY_BOUND_CROSSINGS','independent_certificate_sha256':sha(source),'independent_script_sha256':data['script_sha256'],'root_script_sha256':sha(Path(__file__)),'rows':checks,'scope':'Mathematical crossings of sufficient source-model bounds, not optimal attack costs or NIST certification. Root evaluation is not a new independent occupancy derivation.'}
(HERE/'CHECK.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(record['status'])

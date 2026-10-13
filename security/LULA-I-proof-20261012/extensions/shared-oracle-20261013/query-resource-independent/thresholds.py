"""Independent exact rational outward brackets of reviewed query bound crossings.

No mpmath imports or root query-threshold outputs. FORS dyadic endpoints are
reused from the independent, pre-existing classical occupancy calculation.
Run with Python 3: python -I -B thresholds.py
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, time

HERE=Path(__file__).resolve().parent
X=HERE.parent
N=1<<128
P=1024
SCALE=1<<P
TARGET=F(1,2)
QS=(24,30,38,40,41,44,50,64)

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
FILES=("CLASSICAL-RO-THEOREM.md","QUANTUM-RO-THEOREM.md",
       "QUANTUM-EVENT-SPECIFIC-THEOREM.md", "classical-composition-numeric/OWN-BOUNDS.json")
pins={f:digest(X/f) for f in FILES}
old=json.loads((X/FILES[-1]).read_text(encoding="utf-8"))
def dyadic(t):
    sign,man,exp,bits=t
    assert sign==0 and man.bit_length()==bits
    return F(man*(1<<exp),1) if exp>=0 else F(man,1<<(-exp))
PF={}
for row in old['rows']:
    k=row['log2_signing_query_cap']
    a=row['FORS_per_raw_candidate']
    pair=(dyadic(a['lower_dyadic_mpf_tuple']),dyadic(a['upper_dyadic_mpf_tuple']))
    if k in PF: assert pair==PF[k]
    PF[k]=pair

class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert 0<=self.lo<=self.hi
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo*o.lo,self.hi*o.hi)
    __rmul__=__mul__
    def __truediv__(self,o):
        assert isinstance(o,int) and o>0
        return I(self.lo/o,self.hi/o)
    def square(self): return I(self.lo*self.lo,self.hi*self.hi)
    def cap(self): return I(min(1,self.lo),min(1,self.hi))
    def sqrt(self):
        def floorroot(x):
            t=math.isqrt((x.numerator<<(2*P))//x.denominator)
            assert F(t*t, SCALE*SCALE)<=x<F((t+1)*(t+1),SCALE*SCALE)
            return t
        a,b=floorroot(self.lo),floorroot(self.hi)
        # Inclusive upper is exact at perfect squares, otherwise +1 dyadic.
        upper=b if F(b*b,SCALE*SCALE)==self.hi else b+1
        return I(F(a,SCALE),F(upper,SCALE))

def formulas(q,Q,pf):
    classical=(I(F(6*Q+3*q+6243,N))
        +I(F(q*Q+q*(q-1)//2+q,N*N))
        +I(0,F(q,1<<4096))+(Q+1)*pf).cap()
    D=(q*(I(F(Q+q+1,N*N-N)).sqrt()+I(F(Q+q+1,2*(N*N-N))))).cap()
    A=(D+8*(Q+2)**2*(pf+I(F(1,N))+I(F(q,N*N)))).cap()
    c=( (2*Q+I(q).sqrt()).square()/N
         +(I(F(2*(Q+2),1<<64))+A.sqrt()).square()).cap()
    h=((2*Q+I(3017).sqrt()).square()/N).cap()
    g=I(F(8*(Q+3218)**2,N)).cap()
    d7=I(F(8*(Q+6)**2,N)).cap()
    delta=I(F(2*Q,1<<64)+F(2*q+2,N)).cap()
    conservative=(I(F(1,N))+delta+c+h+g+d7).cap()
    e=(c+h+g+d7).cap()
    b=I(F(2*q+2,N)).cap()
    event=(I(F(1,N))+(I(F(2*Q,1<<64))+(b+e).cap().sqrt()).square()).cap()
    best=I(min(event.lo,conservative.lo),min(event.hi,conservative.hi))
    return {'classical':classical,'quantum_conservative':conservative,
            'quantum_event':event,'quantum_best':best}

def certify(v):
    if v.hi<=TARGET: return 'PASS'
    if v.lo>TARGET: return 'FAIL'
    raise ArithmeticError('Interval straddles target: insufficient precision/input bracket')

def pair(v): return [str(v.numerator),str(v.denominator)]
def serial(v): return {'lower_rational':pair(v.lo),'upper_rational':pair(v.hi)}

started=time.time()
rows=[]
for k in QS:
    q=1<<k; pf=I(*PF[k]); memo={}
    def values(Q):
        if Q not in memo: memo[Q]=formulas(q,Q,pf)
        return memo[Q]
    for model in ('classical','quantum_conservative','quantum_event','quantum_best'):
        assert certify(values(0)[model])=='PASS'
        lo,hi=0,1
        while certify(values(hi)[model])=='PASS': lo,hi=hi,hi*2
        while hi-lo>1:
            mid=(lo+hi)//2
            if certify(values(mid)[model])=='PASS': lo=mid
            else: hi=mid
        passv,failv=values(lo)[model],values(hi)[model]
        assert certify(passv)=='PASS' and certify(failv)=='FAIL' and hi==lo+1
        rows.append({'log2_q':k,'q':str(q),'model':model,
            'Q_pass':str(lo),'Q_fail':str(hi),
            'log2_Q_pass_approx':math.log2(lo),
            'pass_bound':serial(passv),'fail_bound':serial(failv),
            'pass_margin_lower':pair(TARGET-passv.hi),
            'fail_margin_lower':pair(failv.lo-TARGET),
            'adjacent_integer_crossing_certified':True})
    print(k,[(r['model'],r['Q_pass'],r['log2_Q_pass_approx']) for r in rows[-4:]],flush=True)

out={'outcome':'CERTIFIED_RATIONAL_BRACKETS_OF_REVIEWED_BOUND_CROSSINGS',
     'target':['1','2'],'sqrt_dyadic_precision_bits':P,
     'arithmetic':'exact Python integer/Fraction; outward sqrt via integer isqrt',
     'input_pins':pins,'script_sha256':digest(Path(__file__)),
     'FORS_input':'prior independently evaluated exact-binomial outward dyadic brackets; not a new occupancy proof',
     'exhaustion_enclosure':'0 <= (511/512)^(2^32) <= 2^-4096, by (1-x)^m<=exp(-mx)<=2^(-mx), mx=2^23',
     'interpretation':'PASS certifies the accepted sufficient probability upper bound <=1/2; FAIL certifies that this sufficient bound exceeds1/2, not that any attack succeeds.',
     'security_category':'NOT_ESTABLISHED; query counts omit gate costs, time, depth and fixed-SHA implementation/refinement',
     'seconds':time.time()-started,'rows':rows}
(HERE/'THRESHOLDS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
lines=['# Independent query-resource thresholds','',out['interpretation'],'',
       '| q | Bound | Q pass | Q fail | log2(Q pass), approximate |',
       '|---:|---|---:|---:|---:|']
for r in rows: lines.append(f"| 2^{r['log2_q']} | {r['model']} | {r['Q_pass']} | {r['Q_fail']} | {r['log2_Q_pass_approx']:.12f} |")
lines += ['', 'All pass/fail comparisons use exact rational outward intervals, not the displayed floating-point logarithms.',
          'The crossings concern the reviewed bound expressions, not an attack threshold, exact optimal security, NIST category or implementation certificate.']
(HERE/'THRESHOLDS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

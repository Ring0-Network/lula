from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib, json

E=Path(__file__).resolve().parent
Z=(F(0),F(0)); ONE=(F(1),F(0)); SQRT_HALF=(F(0),F(1,2))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def mul(a,b):return a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def linear(s,rule):
    t={}
    for j,a in s.items():
        for k,c in rule(j):t[k]=add(t.get(k,Z),mul(a,c))
    return {k:a for k,a in t.items() if a!=Z}
def had(s,b):
    mask=1<<b
    return linear(s,lambda j:[(j&~mask,SQRT_HALF),(j|mask,neg(SQRT_HALF) if j&mask else SQRT_HALF)])
def perm(s,rule):return linear(s,lambda j:[(rule(j),ONE)])
def phase(s,rule):return {j:neg(a) if rule(j) else a for j,a in s.items()}
def parity(x):return x.bit_count()%2
def simulate(f,r0,r1,x,y,omit_known_phase=False,omit_uncompute=False):
    s={x|(y<<1):ONE}
    for b in [1,2]:s=had(s,b)
    def d(j):return parity(((j>>1)&3)&(r0[j&1]^r1[j&1]))
    s=perm(s,lambda j:j^(d(j)<<3))
    s=had(s,3)
    s=perm(s,lambda j:j^(f[j&1]<<3)) # Exactly one ordinary XOR query to f.
    s=had(s,3)
    if not omit_uncompute:s=perm(s,lambda j:j^(d(j)<<3))
    if not omit_known_phase:s=phase(s,lambda j:parity(((j>>1)&3)&r0[j&1]))
    for b in [1,2]:s=had(s,b)
    return s
tests=worlds=inactive=0
bad_phase=bad_garbage=None
for f in product(range(2),repeat=2):
    for r0 in product(range(4),repeat=2):
        for r1 in product(range(4),repeat=2):
            worlds+=1
            for x,y in product(range(2),range(4)):
                R=r1[x] if f[x] else r0[x]
                expected={x|((y^R)<<1):ONE}
                got=simulate(f,r0,r1,x,y)
                assert got==expected,(f,r0,r1,x,y,got,expected)
                tests+=1
                inactive+=int(r0[x]==r1[x])
                if bad_phase is None and simulate(f,r0,r1,x,y,omit_known_phase=True)!=expected:
                    bad_phase={'f':f,'r0':r0,'r1':r1,'x':x,'y':y}
                if bad_garbage is None and simulate(f,r0,r1,x,y,omit_uncompute=True)!=expected:
                    bad_garbage={'f':f,'r0':r0,'r1':r1,'x':x,'y':y}
assert bad_phase is not None and bad_garbage is not None
out={'status':'EXACT_FINITE_CONTROL_PASS','arithmetic':'Q(sqrt(2)); Fraction pairs; no floats','worlds':worlds,'clean_basis_states_checked':tests,'inactive_delta_zero_basis_checks':inactive,'boolean_queries_per_raw_xor':1,'scratch_returned_zero_and_no_extra_phase':True,'negative_omit_known_phase':bad_phase,'negative_omit_uncompute':bad_garbage,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((E/'ONE-QUERY-COMPLETION.md').read_bytes()).hexdigest(),'scope':'synthetic exact circuit control; general algebra is manual; no actual source forgery or complete game theorem'}
(E/'ONE-QUERY-CONTROL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

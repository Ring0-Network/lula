"""Independent exact matrix composition for Fourier one-call completion."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); HALF_ROOT=(F(0),F(1,2))
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def times(a,b): return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def minus(a): return (-a[0],-a[1])
def apply(state, edges):
    out={}
    for j,a in state.items():
        for k,c in edges(j): out[k]=plus(out.get(k,ZERO),times(a,c))
    return {k:a for k,a in out.items() if a!=ZERO}
def H(state,bit):
    mask=1<<bit
    return apply(state,lambda j: [(j&~mask,HALF_ROOT),(j|mask,minus(HALF_ROOT) if j&mask else HALF_ROOT)])
def swap(state,rule): return apply(state,lambda j:[(rule(j),ONE)])
def execute(f,miss,hit,state):
    # Raw register is two bits, reply is three bits, scratch is one bit.
    # 0,1 changed; 2 same-base; 3 off-length. pi(2)=pi(3)=0.
    def dot(j):
        u=j&3; z=(j>>2)&7
        return (z & (miss[u]^hit[u])).bit_count()%2
    for bit in (2,3,4): state=H(state,bit)
    state=swap(state,lambda j:j^(dot(j)<<5))
    state=H(state,5)
    state=swap(state,lambda j:j^(f[(j&3) if (j&3)<2 else 0]<<5))
    state=H(state,5)
    state=swap(state,lambda j:j^(dot(j)<<5))
    state=swap(state,lambda j:j)  # Keeps the non-oracle operations explicit.
    state={j:minus(a) if (((j>>2)&7)&miss[j&3]).bit_count()%2 else a for j,a in state.items()}
    for bit in (2,3,4): state=H(state,bit)
    return state

# Exhaust every two-point f; vary all changed full three-bit replies.
# Outside complete replies are fixed 3 and 6 identically in both tables.
worlds=basis=mixed=0
for f in product((0,1),repeat=2):
    for low0,low1,high0,high1 in product(range(8),repeat=4):
        miss=(low0,low1,3,6); hit=(high0,high1,3,6)
        worlds+=1
        for u,y in product(range(4),range(8)):
            got=execute(f,miss,hit,{u|(y<<2):ONE})
            image=(hit[u] if f[u] else miss[u]) if u<2 else miss[u]
            assert got=={u|((y^image)<<2):ONE}
            basis+=1
        # Exact coherent vector includes all regions. Together with exact
        # basis matrix equality this covers arbitrary reference entanglement.
        state={u|(u<<2):(F(1,2),F(0)) for u in range(4)}
        want={u|((u^((hit[u] if f[u] else miss[u]) if u<2 else miss[u]))<<2):(F(1,2),F(0)) for u in range(4)}
        assert execute(f,miss,hit,state)==want
        mixed+=1
out={'status':'PASS','arithmetic':'Exact Q(sqrt(2))', 'worlds':worlds,
     'clean_basis_checks':basis,'mixed_region_superposition_checks':mixed,
     'boolean_calls_per_full_xor':1,'outside_delta_zero':True,
     'controls_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Synthetic exact finite circuit matrices; general identity manual, no whole cryptographic game mechanization'}
(HERE/'ONE-QUERY-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

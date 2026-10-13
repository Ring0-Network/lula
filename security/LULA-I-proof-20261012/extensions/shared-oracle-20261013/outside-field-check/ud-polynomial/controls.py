"""Exact marker-law, finite-difference, polynomial and grid-overshoot controls."""
from collections import Counter
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent

def falling(k,d):
    out=1
    for j in range(d):out*=k-j
    return out

def bound(N,Q):
    return min(F(1),F(N-1,N)*F(4*Q*Q,N-4*Q*Q)) if 4*Q*Q<N else F(1)

weight_checks=polynomial_checks=0
actual_phase_rows=[]
for N in (2,4,8):
    lam=F(1,N)
    fields=list(product(range(2),repeat=N))
    ideal=[lam**sum(m)*(1-lam)**(N-sum(m)) for m in fields]
    real=[F(sum(m),N)*lam**(sum(m)-1)*(1-lam)**(N-sum(m)) if sum(m) else F(0) for m in fields]
    assert sum(ideal)==sum(real)==1
    for m,pi,pr in zip(fields,ideal,real):
        assert pr==sum(m)*pi
        weight_checks+=1
    # Exact REAL conditional full-row law high tableY=0 versus uniform IDEAL.
    for values in product(range(N),repeat=N):
        marks=tuple(int(v==0) for v in values)
        at=fields.index(marks)
        misses=N-sum(marks)
        assert ideal[at]/(N-1)**misses==F(1,N**N)
        assert real[at]/(N-1)**misses==F(sum(marks),N**N)
        weight_checks+=1
        if N==8:break  # Small table-law check only; never generate8^8 tables.
    for Q in range(3):
        d=min(2*Q,N)
        for fixture in range(5):
            # Nonsymmetric, convex multilinear acceptance polynomial.
            terms=[(s,((sum(s)+fixture)%5)+1) for size in range(d+1) for s in combinations(range(N),size)]
            denom=sum(c for _,c in terms)
            accept=[F(sum(c for s,c in terms if all(m[i] for i in s)),denom) for m in fields]
            pk=[sum(a for m,a in zip(fields,accept) if sum(m)==k)/comb(N,k) for k in range(N+1)]
            for k in range(N+1):
                direct=sum(F(c*falling(k,len(s)),falling(N,len(s))*denom) for s,c in terms)
                assert direct==pk[k]
            gap=sum(a*(pr-pi) for a,pr,pi in zip(accept,real,ideal))
            delta=(1-lam)*sum(F(comb(N-1,k))*lam**k*(1-lam)**(N-1-k)*(pk[k+1]-pk[k]) for k in range(N))
            assert gap==delta and abs(gap)<=bound(N,Q)
            polynomial_checks+=1
    # One actual phase query on entangled |0,0>+|1,1>, Bell-projector output.
    accept=[F(1)-m[0]-m[1]+2*m[0]*m[1] for m in fields]
    gap=sum(a*(pr-pi) for a,pr,pi in zip(accept,real,ideal))
    expected=-F(2*(N-1)*(N-2),N**3)
    assert gap==expected and abs(gap)<=bound(N,1)
    actual_phase_rows.append({'N':N,'Q':1,'signed_gap':str(gap),'upper':str(bound(N,1))})

# A grid-bounded degree4 polynomial that goes BELOW0 between grid points.
# It also violates the incorrect derivative bound d²/N derived by assuming
# continuous[0,1] merely from grid bounds; the correct denominator remains safe.
grid_n=32
def base(x):
    t=2*F(x,grid_n)-1
    return (2*t*t-1)**2
eps=min(base(k) for k in range(grid_n+1))
assert eps==F(49,16384)
grid=[(base(k)-eps)/(1-eps) for k in range(grid_n+1)]
assert min(grid)==0 and max(grid)==1
continuous_min=-eps/(1-eps)
endpoint_derivative=F(16,grid_n)/(1-eps)
assert continuous_min<0 and endpoint_derivative>F(16,grid_n)
assert endpoint_derivative<=F(16,grid_n-16)

# Pure binomial controls on small/medium weights, without any large marker table.
binomial_controls=0
for N in (8,16,32,64):
    lam=F(1,N)
    for Q in (0,1,2):
        pk=[F(1,2)]*(N+1) if Q==0 else [1-F(2*k*(N-k),N*(N-1)) for k in range(N+1)]
        gap=sum((k-1)*F(comb(N,k))*lam**k*(1-lam)**(N-k)*pk[k] for k in range(N+1))
        delta=(1-lam)*sum(F(comb(N-1,k))*lam**k*(1-lam)**(N-1-k)*(pk[k+1]-pk[k]) for k in range(N))
        assert gap==delta and abs(gap)<=bound(N,Q)
        binomial_controls+=1

assert bound(16,0)==0
marker_advice_gap=F(15,16**2) # Freeb(0) REAL-IDEAL marginal gap.
world_advice_gap=F(1)         # Independent experiment label, different auxlaw.
assert marker_advice_gap>0 and world_advice_gap>bound(16,0)
out={
 'status':'PASS_EXACT_SMALL_QUERY_UD_POLYNOMIAL_CONTROLS',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'marker_and_completion_checks':weight_checks,'nonsymmetric_polynomial_checks':polynomial_checks,
 'actual_entangled_phase_query_rows':actual_phase_rows,'binomial_controls':binomial_controls,
 'grid_negative_control':{'N':grid_n,'degree':4,'epsilon':str(eps),'continuous_minimum':str(continuous_min),'endpoint_derivative':str(endpoint_derivative),'incorrect_continuous_bound':str(F(16,grid_n)),'correct_grid_bound':str(F(16,grid_n-16))},
 'negative_auxiliary_controls':{'free_marker_bit_Q0_gap':str(marker_advice_gap),'independent_world_bit_different_joint_law_Q0_gap':str(world_advice_gap)},
 'scope':'Finite exact marker/completion/acceptance/grid identities; no source signatures, actual hash attack, large function generation, optimality or kernel proof',
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

"""Finite standard-library quantum controls, not LULA signing or an attack."""
import cmath
import json
import math
import random
from fractions import Fraction
from pathlib import Path

N=16
R=4  # full two-bit output; prefix-only programming is not used
ANC=2
points=[(tag,label,key) for tag in ('D','M') for label in range(2) for key in range(N)]+[('outside',0,0)]
rng=random.Random(202610130031)
base=[rng.randrange(R) for _ in points]
private={(tag,label):rng.randrange(R) for tag in ('D','M') for label in range(2)}
psi=[complex(rng.gauss(0,1),rng.gauss(0,1))*((-1)**base[x])
     for x in range(len(points)) for z in range(R) for a in range(ANC)]
norm=math.sqrt(sum(abs(v)**2 for v in psi))
psi=[v/norm for v in psi]
def oracle(state,table):
    out=[0j]*len(state)
    for x,answer in enumerate(table):
        for z in range(R):
            for a in range(ANC):
                out[(x*R+(z^answer))*ANC+a]=state[(x*R+z)*ANC+a]
    return out
def norm2(state): return sum(abs(v)**2 for v in state)
def dot(a,b): return sum(x.conjugate()*y for x,y in zip(a,b))
ideal=oracle(psi,base)
avg_mu=avg_trace=0.0
for k in range(N):
    for p in range(N):
        patched=base[:]
        hidden=[]
        for x,(tag,label,key) in enumerate(points):
            if (tag=='D' and key==k) or (tag=='M' and key==p):
                hidden.append(x)
                patched[x]=private[tag,label]
        mu=sum(abs(psi[(x*R+z)*ANC+a])**2 for x in hidden for z in range(R) for a in range(ANC))
        real=oracle(psi,patched)
        err=norm2([u-v for u,v in zip(real,ideal)])
        assert err<=4*mu+1e-12
        trace=math.sqrt(max(0.0,1-abs(dot(real,ideal))**2))
        assert trace<=math.sqrt(err)+1e-12
        avg_mu+=mu/N**2
        avg_trace+=trace/N**2
eligible_mass=sum(abs(psi[(x*R+z)*ANC+a])**2 for x in range(len(points)-1) for z in range(R) for a in range(ANC))
assert abs(avg_mu-eligible_mass/N)<1e-12
assert avg_trace<=2/math.sqrt(N)+1e-12

# One-query Grover phase control: the next REAL query has concentrated key mass.
# O_ideal is identity, O_real flips the unknown marked key. This is a generic
# oracle control, not a uniform full-output RO source forgery.
s=[complex(1/math.sqrt(N))]*N
grover_success=0.0
for key in range(N):
    v=s[:]
    v[key]=-v[key]
    mean=sum(v)/N
    v=[2*mean-x for x in v]
    assert norm2([u-w for u,w in zip(v,s)])<=4/N+1e-12
    grover_success+=abs(v[key])**2/N
exact=Fraction((3*N-4)**2,N**3)
assert abs(grover_success-float(exact))<1e-12
assert exact>Fraction(2,N)  # one coherent query plus final classical test

# Classical block difference on two distinct unused-key nominations.
classical_bad=sum(p in {2,7} for p in range(N))/N
assert classical_bad==2/N
known_k=5
known_x=points.index(('D',0,known_k))
known_state=[0j]*len(psi)
known_state[(known_x*R)*ANC]=1
known_mu=sum(abs(known_state[(x*R+z)*ANC+a])**2
             for x,(tag,label,key) in enumerate(points)
             if tag=='D' and key==known_k
             for z in range(R) for a in range(ANC))
assert known_mu==1>1/N

result={
    'status':'PASS_FINITE_QUANTUM_CONTROLS_ONLY',
    'keys_per_seed':N, 'coherent_full_output_bits':2,
    'ancilla_dimension':ANC, 'raw_points':len(points),
    'key_pairs_checked':N**2,
    'averaged_hidden_mass':avg_mu,
    'eligible_mass_over_N':eligible_mass/N,
    'averaged_one_query_pure_trace_distance':avg_trace,
    'conservative_bound_2_over_sqrtN':2/math.sqrt(N),
    'grover_one_query_success_and_next_real_key_weight':str(exact),
    'invalid_literal_query_plus_final_bound':str(Fraction(2,N)),
    'classical_two_nomination_channel_discrepancy':str(Fraction(2,N)),
    'known_key_negative_control_hidden_mass':known_mu,
    'scope':'Finite state inequalities and generic search discriminator; no source attack, no full QROM security proof'
}
Path(__file__).with_name('CONTROL-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

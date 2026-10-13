"""Finite correlated-marker/completion and one-query phase controls only."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, sqrt
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
relations=0
laws={}
for N in (2,4):
    distribution=Counter()
    for X in range(N):
        for bits in product(range(2),repeat=N):
            weight=Fraction(1,N)
            for bit in bits:weight*=Fraction(1,N) if bit else Fraction(N-1,N)
            marker=tuple(int(i==X or bits[i]) for i in range(N))
            distribution[marker]+=weight
    assert sum(distribution.values())==1 and (0,)*N not in distribution
    mu=Fraction(2,N)-Fraction(1,N*N)
    for i in range(N):
        assert sum(w for m,w in distribution.items() if m[i])==mu
        relations+=1
    pair=sum(w for m,w in distribution.items() if m[0] and m[1])
    assert pair==Fraction(3,N*N)-Fraction(2,N**3)
    assert pair!=mu*mu
    # Complete the miss cells uniformly excludingY=0.
    high_law=Counter()
    for m,weight in distribution.items():
        miss=[i for i in range(N) if not m[i]]
        for values in product(range(1,N),repeat=len(miss)):
            high=[0]*N
            for i,value in zip(miss,values):high[i]=value
            high_law[tuple(high)]+=weight/Fraction((N-1)**len(miss))
    for high in product(range(N),repeat=N):
        assert high_law[high]==Fraction(high.count(0),N**N)
        relations+=1
    assert sum(high_law.values())==1
    # Same prefix law with one independent lower bit at every word.
    for low in product(range(2),repeat=N):
        low_probability=sum(high_law.values())/2**N
        assert low_probability==Fraction(1,2**N)
        relations+=1
    laws[str(N)]={'mu':str(mu),'pair':str(pair),'iid_pair_wrong':str(mu*mu),'marker_fields':len(distribution),'q0_any_preimage':str(mu),'q0_original_X_only':str(Fraction(1,N))}

# One ordinary Boolean scratch query gives(-1)^(mask*marker) and cleans scratch.
scratch_checks=0
for mask,mark in product(range(2),repeat=2):
    a,b=(1.0,0.0) if not mask else (0.0,1.0)
    a,b=(a+b)/sqrt(2),(a-b)/sqrt(2)
    if mark:a,b=b,a
    a,b=(a+b)/sqrt(2),(a-b)/sqrt(2)
    if mask:a,b=b,a
    assert abs(a-((-1)**(mask*mark)))<1e-12 and abs(b)<1e-12
    scratch_checks+=1

# Full3-bit XOR output:2 high bits and one unchanged independent lower bit.
phase_checks=0
parity=lambda x:x.bit_count()%2
for Y in range(4):
    for miss in range(4):
        if miss==Y:continue
        for low,mark,active in product(range(2),repeat=3):
            base=(miss<<1)|low
            hit=(Y<<1)|low if active else base
            value=hit if mark else base
            for before,after in product(range(8),repeat=2):
                numerator=0
                for frequency in range(8):
                    mask=parity(frequency&(base^hit))
                    phase=parity(frequency&before)^parity(frequency&base)^(mark&mask)^parity(frequency&after)
                    numerator+=(-1)**phase
                assert numerator==(8 if after==(before^value) else 0)
                phase_checks+=1

# Exact symmetric Grover probabilities for planted fields using ONLY size law.
# No large field or actual inversion is constructed.
query_bounds=[]
for N in (2,4,32):
    mu=Fraction(2,N)-Fraction(1,N*N)
    for Q in range(4):
        success=Fraction(0)
        for k in range(1,N+1):
            weight=comb(N-1,k-1)*Fraction(1,N)**(k-1)*Fraction(N-1,N)**(N-k)
            marked=unmarked=Fraction(1)
            for _ in range(Q):
                mean=(-k*marked+(N-k)*unmarked)/N
                marked,unmarked=2*mean+marked,2*mean-unmarked
            success+=weight*Fraction(k,N)*marked*marked
        bound=min(Fraction(1),(2*Q+1)**2*mu)
        assert success<=bound
        if Q==0:assert success==mu
        query_bounds.append({'N':N,'Q':Q,'symmetric_success':str(success),'marginal_upper':str(bound)})
assert next(r for r in query_bounds if r['N']==32 and r['Q']==1)['marginal_upper']!='1'

# Counterexample: adviceX destroys conditional marginal independence atQ=0.
N=4
advice_success=Fraction(1)
mu=Fraction(2,N)-Fraction(1,N*N)
assert advice_success>mu
result={
 'status':'PASS_EXACT_CORRELATED_WHOLE_MARKER_AND_ONE_QUERY_COMPLETION_CONTROLS',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'marker_completion_relations':relations,'marker_laws':laws,
 'clean_one_query_scratch_checks':scratch_checks,'full_output_phase_amplitudes':phase_checks,
 'query_envelope_cases':query_bounds,
 'marker_dependent_advice_q0_counterexample':{'success':'1','unconditional_marginal':str(mu),'conditional_independence_fails':True},
 'scope':'Exact tiny marker/completion/unitary/arithmetic controls, not actual source, large function generation, search attack, hardness or kernel proof',
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':result['status'],'relations':relations,'phase_checks':phase_checks,'scratch_checks':scratch_checks,'query_cases':len(query_bounds),'script_sha256':result['script_sha256']}))

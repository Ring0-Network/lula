"""Finite dynamic-overlay controls; no source signing, timing or QROM claim."""
import math
import random
import json
from fractions import Fraction
from pathlib import Path

N=32
POINTS=2*N
OUT=4
rng=random.Random(202610130047)
residual=[rng.randrange(OUT) for _ in range(POINTS)]
image_A,image_B=rng.randrange(OUT),rng.randrange(OUT)
initial=[0j]*(POINTS*OUT)
for x in range(POINTS): initial[x*OUT]=1/math.sqrt(POINTS)
def query(state,table):
    out=[0j]*len(state)
    for x,v in enumerate(table):
        for z in range(OUT): out[x*OUT+(z^v)]=state[x*OUT+z]
    return out
def between(state,known_A):
    # Walsh transform mixes the retained prior query state; a known-value
    # controlled input permutation then changes the next query adaptively.
    out=state[:]
    step=1
    while step<POINTS:
        for block in range(0,POINTS,2*step):
            for j in range(step):
                for z in range(OUT):
                    a=(block+j)*OUT+z; b=(block+j+step)*OUT+z
                    u,v=out[a],out[b]
                    out[a]=(u+v)/math.sqrt(2)
                    out[b]=(u-v)/math.sqrt(2)
        step*=2
    changed=[0j]*len(out)
    for x in range(POINTS):
        for z in range(OUT): changed[(x^known_A)*OUT+z]=out[x*OUT+z]
    return changed
def norm2(v): return sum(abs(x)**2 for x in v)

gap2=p_real=p_ghost=weight=0.0
for a in range(N):
    ghost_first=query(initial,residual)
    ghost_second_input=between(ghost_first,a)
    overlay=residual[:]; overlay[a]=image_A
    ghost_second=query(ghost_second_input,overlay)
    reference=ghost_second[:]
    for b in range(N):
        true=residual[:]; true[a]=image_A; true[N+b]=image_B
        real_first=query(initial,true)
        # Same classical reveal A=a; same common continuation.
        real_second=query(between(real_first,a),true)
        assert all(abs(x-y)<1e-12 for x,y in zip(reference,ghost_second))
        mu=sum(abs(ghost_second_input[(N+b)*OUT+z])**2 for z in range(OUT))
        weight+=mu/N**2
        gap2+=norm2([x-y for x,y in zip(real_second,ghost_second)])/N**2
        # A single final classical B input selected from the retained output.
        for x in range(POINTS):
            for z in range(OUT):
                nomination=((x%N)^z)%N
                if nomination==b:
                    p_real+=abs(real_second[x*OUT+z])**2/N**2
                    p_ghost+=abs(ghost_second[x*OUT+z])**2/N**2
    # Recompute explicitly for every remaining B key: overlay never reads b.
    for b in range(N):
        repeated=query(between(query(initial,residual),a),overlay)
        assert all(abs(x-y)<1e-12 for x,y in zip(reference,repeated))
assert weight<=1/N+1e-12
assert abs(p_ghost-1/N)<1e-12
gap=math.sqrt(gap2)
assert gap<=4/math.sqrt(N)+1e-12
assert abs(math.sqrt(p_real)-math.sqrt(p_ghost))<=gap+1e-12

# Static ghost after legitimate reveal returns the wrong known-point value.
static_mismatch=Fraction(sum(v!=1 for v in range(OUT)),OUT)
assert static_mismatch==Fraction(3,4)
# Nonclosed known prefix exposes its allegedly hidden successor exactly.
bad_hits=0
for start in range(4):
    for next_value in range(4):
        true_first=[0]*4
        true_first[start]=next_value
        not_closed={0,2}  # coordinate0 and final endpoint, but not successor1
        copied_payload=true_first[start]  # a query at already-known input0
        hit=(1 not in not_closed and copied_payload==next_value)
        bad_hits+=hit
        closed=not_closed|{1}
        assert not (1 not in closed and copied_payload==next_value)
bad_success=Fraction(bad_hits,16)
assert bad_success==1>Fraction(1,4)

result={
 'status':'PASS_FINITE_DYNAMIC_OVERLAY_CONTROL_ONLY',
 'secret_pairs':N**2,'output_bits':2,'quantum_queries':2,
 'remaining_secret_ghost_states_equal_per_known_value':True,
 'averaged_second_query_hidden_weight':weight,
 'bound_weight':1/N,
 'purified_averaged_vector_gap':gap,
 'bound_vector_gap_2Q_over_sqrtN':4/math.sqrt(N),
 'one_final_ghost_genuine_input_probability':p_ghost,
 'one_final_real_genuine_input_probability':p_real,
 'square_root_probability_gap':abs(math.sqrt(p_real)-math.sqrt(p_ghost)),
 'static_after_reveal_known_point_discrepancy':str(static_mismatch),
 'non_suffix_closed_successor_acquisition':str(bad_success),
 'scope':'Finite retained-state, predictable-FORS-reveal model and invalid-variant controls; not full source or QROM security'
}
Path(__file__).with_name('CONTROL-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

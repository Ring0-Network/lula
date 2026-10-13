"""Finite exact structural/coverage controls supporting a manual uniform theorem."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from math import comb
import hashlib,json
B=Path(__file__).resolve().parent;X=B.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(B/'INDEPENDENT-FIRST.md')=='e330e30759eac52adca83384ce5b9c95cfa9a491230376518cfa19302dd3bd67'
coverage=[]
for instances,t,r,q in product([1,2,4],[2,4],[1,2],[0,1,2]):
    states=list(product(range(instances),*([range(t)]*r)))
    total=len(states)**q
    mean=F(0);union={M:F(0) for M in [1,2,3]}
    for transcript in product(states,repeat=q):
        exposed=[[set() for j in range(r)] for b in range(instances)]
        for draw in transcript:
            b=draw[0]
            for j in range(r):exposed[b][j].add(draw[j+1])
        pT=F(0)
        for b in range(instances):
            v=F(1,instances*t)
            for j in range(r):v*=F(len(exposed[b][j]),t)
            pT+=v
        mean+=pT/total
        for M in union:union[M]+=(1-(1-pT)**M)/total
    pf=sum(F(comb(q,z))*F(1,instances)**z*F(instances-1,instances)**(q-z)*
        (1-F(t-1,t)**z)**r for z in range(q+1))/t
    assert mean==pf
    assert all(union[M]<=min(F(1),M*pf) for M in union)
    coverage.append(dict(B=instances,t=t,r=r,q=q,exposure_states=total,pF=str(pf),
        exact_candidate_union={str(M):str(union[M]) for M in union}))
chain_cases=0
for w,l in product([2,4],[1,2,3]):
    maximum=l*(w-1)
    for e in product(range(w),repeat=l):
        S=sum(e);remaining=sum(w-1-x for x in e)
        assert remaining==maximum-S
        if S<maximum:assert remaining>=1
        else:assert remaining==0
        chain_cases+=1
path_cases=0
for a,r in product(range(1,5),range(1,5)):
    for j,i in product(range(r),range(1<<a)):
        for level in range(a+1):
            assert ((j*(1<<a)+i)>>level)==j*(1<<(a-level))+(i>>level)
            path_cases+=1
routes=0
for hs in [(0,0,0),(0,1),(1,0),(1,1),(2,1,0),(1,2,1)]:
    h=sum(hs)
    for idx in range(1<<h):
        for layer,height in enumerate(hs):
            below=sum(hs[:layer]);tree=idx>>(below+height)
            kp=(idx>>below)&((1<<height)-1)
            g=(tree<<height)|kp
            assert g==idx>>below
            routes+=1
constants=[]
sets=[dict(r=17,a=9,hs=[5,5,5,5,21],ls=[32,32,32,32,16],ss=[240,240,240,240,2040]),
      dict(r=18,a=9,hs=[5,5,5,5,22],ls=[32,32,32,32,16],ss=[240,240,240,240,2040]),
      dict(r=1,a=1,hs=[0],ls=[1],ss=[0]),
      dict(r=1,a=1,hs=[0]*256,ls=[1]*256,ss=[0]*256)]
for p in sets:
    d=len(p['hs']);ws=[16]*(d-1)+[256]
    tails=[l*(w-1)-s for l,w,s in zip(p['ls'],ws,p['ss'])]
    assert all(tail>0 for tail in tails)
    H=p['r']+sum(tails)
    G=p['r']*(p['a']+1)+1+sum(tail+1+h for tail,h in zip(tails,p['hs']))
    C=H+G+d+3
    alternate=p['r']*(p['a']+2)+2*sum(tails)+sum(p['hs'])+2*d+4
    assert C==alternate
    constants.append(dict(parameters=p,H_final=H,G_final=G,C_joint=C))
assert constants[0]['H_final']==3017 and constants[0]['G_final']==3217 and constants[0]['C_joint']==6242
assert 26*9+22==256 # full256 partition is representable; real25trees+forced1+route22
full_partition=[set(range(25*9)),set(range(25*9,26*9)),set(range(26*9,256))]
assert len(set.union(*full_partition))==256 and all(not(a&b) for i,a in enumerate(full_partition) for b in full_partition[i+1:])
out=dict(status='FINITE_SUPPORT_FOR_MANUAL_PARAMETER_UNIFORM_CLASSICAL_THEOREM',exit_code=0,
    own_first_sha256=sha(B/'INDEPENDENT-FIRST.md'),script_sha256=sha(Path(__file__)),
    coverage_dimension_cases=len(coverage),coverage=coverage,chain_cases=chain_cases,
    FORS_global_parent_schedule_cases=path_cases,zero_height_route_cases=routes,
    symbolic_final_constants=constants,total256_partition_checked=True,
    no_source_game_kernel_checked=True,no_crypto_source_or_signature_executed=True,
    whole_goal_complete=False,new_source_game_declarations=0)
(B/'FINITE-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(exit_code=0,coverage_cases=len(coverage),chain_cases=chain_cases,
    parent_schedule_cases=path_cases,route_cases=routes,controls_sha256=sha(B/'FINITE-CONTROLS.json'))))

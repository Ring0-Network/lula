"""Exact finite marker laws and degree-bounded acceptance-polynomial controls."""
from fractions import Fraction as F
from itertools import product,combinations
from math import comb
from pathlib import Path
import hashlib,json,random
E=Path(__file__).resolve().parent
def falling(n,r):
    out=1
    for j in range(r):out*=n-j
    return out
def ud(N,Q):
    d2=4*Q*Q
    return min(F(1),F(N-1,N)*F(d2,N-d2)) if d2<N else F(1)
cases=0
marker_checks=0
for N in (2,4,8):
    lam=F(1,N)
    tables=list(product((0,1),repeat=N))
    fake=[lam**sum(b)*(1-lam)**(N-sum(b)) for b in tables]
    real=[sum((F(1,N)*lam**(sum(b)-1)*(1-lam)**(N-sum(b)) for x in range(N) if b[x]),F()) for b in tables]
    assert sum(fake)==sum(real)==1
    for k in range(N+1):
        fw=sum((w for b,w in zip(tables,fake) if sum(b)==k),F())
        rw=sum((w for b,w in zip(tables,real) if sum(b)==k),F())
        assert fw==comb(N,k)*lam**k*(1-lam)**(N-k)
        assert rw==(comb(N-1,k-1)*lam**(k-1)*(1-lam)**(N-k) if k else 0)
        marker_checks+=1
    for Q in (0,1,2):
      degree=min(2*Q,N)
      for seed in range(12):
        rng=random.Random(1000*N+100*Q+seed)
        terms=[(s,rng.randint(-3,3)) for r in range(degree+1) for s in combinations(range(N),r)]
        vals=[sum(c*int(all(b[x] for x in s)) for s,c in terms) for b in tables]
        lo,hi=min(vals),max(vals)
        acc=[F(v-lo,hi-lo) if hi>lo else F(1,2) for v in vals]
        pk=[sum((a for b,a in zip(tables,acc) if sum(b)==k),F())/comb(N,k) for k in range(N+1)]
        # Monomial symmetrization formula, independent of oracle permutation symmetry.
        for k in range(N+1):
          raw=sum((F(c)*F(falling(k,len(s)),falling(N,len(s))) for s,c in terms),F())
          expect=F(raw-lo,hi-lo) if hi>lo else F(1,2)
          assert pk[k]==expect
        gap=sum((a*(r-f) for a,r,f in zip(acc,real,fake)),F())
        coupled=(1-lam)*sum((F(comb(N-1,k))*lam**k*(1-lam)**(N-1-k)*(pk[k+1]-pk[k]) for k in range(N)),F())
        assert gap==coupled
        assert abs(gap)<=ud(N,Q)
        cases+=1
# Negative control: a revealed hidden marker location defeats independent-auxiliary Q=0 premise.
assert ud(16,0)==0 and F(15,16)>ud(16,0)
N=1<<128;DH=20229886488608768;AH=7628143271608320
HS=(1<<21)*(19505+(1<<32))-1
hot=82090+5*(1<<32);cold=8560574463+82090+6*(1<<32)
def component(qa):
    R=qa+1
    pre=min(F(1),F((2*R+1)**2*(2*N-1),N*N))
    u=ud(N,R)
    return DH*pre+AH*u,pre,u
rows=[]
for qe in (24,30,38,40,41,44,50,64):
  for mode,hm in [('prepared',hot),('absent',cold)]:
    for e in (32,64):
      qa=1<<e;total,pre,u=component(qa)
      # Direct source envelope, not an exact oracle success probability.
      rows.append({'log2_q':qe,'mode':mode,'log2_QA':e,'remote_calls':str(qa+1),
       'outside_call_cap':str(qa+HS+(1<<qe)*hm+3224+254),
       'UD_bound':str(u),'PRE_bound':str(pre),'uncapped_component':str(total),
       'capped_component':str(min(F(1),total)),'display_component_float':float(min(F(1),total))})
assert all(F(r['capped_component'])<1 for r in rows if r['log2_QA']==32)
assert all(F(r['capped_component'])==1 for r in rows if r['log2_QA']==64)
thresholds=[]
for target in (F(1,2),F(1)):
    lo,hi=0,1<<64
    while lo+1<hi:
        mid=(lo+hi)//2
        if component(mid)[0]<=target:lo=mid
        else:hi=mid
    assert component(lo)[0]<=target<component(hi)[0]
    thresholds.append({'uncapped_target':str(target),'QA_pass':str(lo),'QA_fail':str(hi),
       'pass_value':str(component(lo)[0]),'fail_value':str(component(hi)[0])})
out={'status':'EXACT_CONTROLS_CANDIDATE_PENDING_INDEPENDENT_REVIEW',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'marker_weight_checks':marker_checks,'polynomial_controls':cases,
 'wrong_auxiliary_negative_control':True,'rows':rows,'uncapped_crossings':thresholds,
 'source_game_mechanization':False,'security_category':'not established',
 'existing_scalars_replaced':False}
(E/'CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'marker_checks':marker_checks,'polynomial_controls':cases,'rows':len(rows),
 'QA32_component':rows[0]['display_component_float'],'uncapped_crossings':[(r['QA_pass'],r['QA_fail']) for r in thresholds]}))

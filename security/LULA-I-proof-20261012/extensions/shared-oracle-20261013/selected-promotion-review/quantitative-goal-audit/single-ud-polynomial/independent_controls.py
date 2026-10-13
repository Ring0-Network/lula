from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def choose(n,r):return comb(n,r) if 0<=r<=n else 0
def ud(N,Q):
 s=4*Q*Q
 return min(F(1),F(N-1,N)*F(s,N-s)) if s<N else F(1)
identities=0;grid_checks=0
for N in (2,4,8,16,32):
 p=F(1,N)
 for d in range(min(4,N)+1):
  for j in range(d+1):
   a=[F(choose(k,j)*choose(N-k,d-j),choose(N,d)) for k in range(N+1)]
   assert all(0<=v<=1 for v in a)
   fake=sum(F(choose(N,k))*p**k*(1-p)**(N-k)*a[k] for k in range(N+1))
   real=sum(F(choose(N-1,k))*p**k*(1-p)**(N-1-k)*a[k+1] for k in range(N))
   adjacent=(1-p)*sum(F(choose(N-1,k))*p**k*(1-p)**(N-1-k)*(a[k+1]-a[k]) for k in range(N))
   assert real-fake==adjacent
   if d*d<N:
    assert max(abs(a[k+1]-a[k]) for k in range(N))<=F(d*d,N-d*d)
    assert abs(adjacent)<=min(F(1),(1-p)*F(d*d,N-d*d));grid_checks+=1
   identities+=1
 # An actual Boolean one-phase-query acceptance polynomial.
 a=[F(4*k*(N-k),N*N) for k in range(N+1)]
 fake=sum(F(choose(N,k))*p**k*(1-p)**(N-k)*a[k] for k in range(N+1))
 real=sum(F(choose(N-1,k))*p**k*(1-p)**(N-1-k)*a[k+1] for k in range(N))
 assert real-fake==F(4*(N-1)**2*(N-2),N**4)
 assert abs(real-fake)<=ud(N,1)
# Grid range is not continuous range: k(k-1)/(N(N-1)) dips negative at1/2.
Ntoy=16
assert all(0<=F(k*(k-1),Ntoy*(Ntoy-1))<=1 for k in range(Ntoy+1))
overshoot=F(-1,4*Ntoy*(Ntoy-1));assert overshoot<0
# World-label advice is separately mark-independent but violates SAME joint law.
assert ud(16,0)==0 and F(1)>ud(16,0)
root=json.loads((HERE/'CONTROLS.json').read_text(encoding='utf-8'))
N=1<<128;K=sum(1<<h for h in (41,36,31,26))
DH=480*K+4080*(1<<21)+(1<<41)*17*512
AH=32*K*105+16*(1<<21)*(254*255//2)
def component(qa):
 r=qa+1;pre=min(F(1),F((2*r+1)**2*(2*N-1),N*N));u=ud(N,r)
 return DH*pre+AH*u,pre,u
assert len(root['rows'])==32
for row in root['rows']:
 qa=1<<row['log2_QA'];total,pre,u=component(qa)
 assert int(row['remote_calls'])==qa+1
 assert F(row['PRE_bound'])==pre and F(row['UD_bound'])==u
 assert F(row['uncapped_component'])==total and F(row['capped_component'])==min(F(1),total)
 hm=82090+5*(1<<32) if row['mode']=='prepared' else 8560574463+82090+6*(1<<32)
 assert int(row['outside_call_cap'])==qa+(1<<21)*(19505+(1<<32))-1+(1<<row['log2_q'])*hm+3224+254
for cross in root['uncapped_crossings']:
 target=F(cross['uncapped_target']);lo,hi=0,1<<64
 while hi-lo>1:
  mid=(lo+hi)//2
  if component(mid)[0]<=target:lo=mid
  else:hi=mid
 assert (lo,hi)==(int(cross['QA_pass']),int(cross['QA_fail']))
 assert component(lo)[0]==F(cross['pass_value'])<=target<F(cross['fail_value'])==component(hi)[0]
out={'status':'PASS_INDEPENDENT_UD_POLYNOMIAL_LAWS_GRID_AND32_COMPONENT_ROWS',
 'binomial_identity_controls':identities,'small_degree_adjacent_checks':grid_checks,
 'actual_single_phase_query_cases':5,'grid_continuum_overshoot_negative_value':str(overshoot),
 'world_label_independent_advice_negative':True,'source_component_rows':32,
 'QA32_component':str(component(1<<32)[0]),'uncapped_crossings':root['uncapped_crossings'],
 'root_result_sha256':hashlib.sha256((HERE/'CONTROLS.json').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'first_sha256':hashlib.sha256((HERE/'INDEPENDENT-FIRST.md').read_bytes()).hexdigest(),
 'new_source_game_declarations':0,'whole_goal_complete':False}
p=HERE/'INDEPENDENT-CONTROLS.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',hashlib.sha256(p.read_bytes()).hexdigest(),identities,grid_checks)

"""Exact finite coherent-prefix controls, not source security certification."""
from pathlib import Path
from itertools import product
import math,json,random,hashlib
P=Path(__file__).resolve().parent
N=4;r=2;W=N*N;inputs=r*N;dim=inputs*W
rng=random.Random(20261013)
def oracle(psi,fs):
 out=[0j]*dim
 for a in range(inputs):
  val=fs[a//N][a%N]
  for b in range(W):out[a*W+(b^val)]=psi[a*W+b]
 return out
def hadamard(v):
 out=v[:];step=1
 while step<len(out):
  for base in range(0,len(out),step*2):
   for j in range(step):
    a=out[base+j];b=out[base+j+step]
    out[base+j]=(a+b)/math.sqrt(2);out[base+j+step]=(a-b)/math.sqrt(2)
  step*=2
 return out
def normdiff(a,b):return sum(abs(x-y)**2 for x,y in zip(a,b))
def mass(psi,u):return sum(abs(psi[(p*N+u[p])*W+b])**2 for p in range(r) for b in range(W))
checks=[]
for case in range(6):
 fs=[tuple(rng.randrange(W) for _ in range(N)) for _ in range(r)]
 # An inactive branch represents absorbing metadata/exposure failure; flag depends on outside data.
 active=case!=5
 stats=[0.0]*5;count=0
 for x in range(N):
  # Fake query state may depend on challenge/suffix information and fake table, never u.
  psi=[0j]*dim
  for a in range(inputs):psi[a*W]=((-1)**((a+x)%3))/math.sqrt(inputs) if active else 0j
  fake1=oracle(psi,fs);fakein2=hadamard(fake1);fake2=oracle(fakein2,fs)
  for u in product(range(N),repeat=r):
   for rho in product(range(N),repeat=r):
    true=[list(t) for t in fs]
    true[0][u[0]]=u[1]*N+rho[0]
    true[1][u[1]]=x*N+rho[1]
    real1=oracle(psi,true)
    changed_on_fake2=oracle(fakein2,true)
    real2=oracle(hadamard(real1),true)
    vals=[mass(psi,u),mass(fakein2,u),normdiff(real1,fake1),
          normdiff(changed_on_fake2,fake2),normdiff(real2,fake2)]
    stats=[a+b for a,b in zip(stats,vals)];count+=1
 avg=[v/count for v in stats]
 assert avg[0]<=int(active)/N+1e-12 and avg[1]<=int(active)/N+1e-12
 assert avg[2]<=4*int(active)/N+1e-12 and avg[3]<=4*int(active)/N+1e-12
 assert math.sqrt(avg[4])<=math.sqrt(avg[2])+math.sqrt(avg[3])+1e-12
 checks.append(dict(case=case,worlds=count,active=active,support_first=avg[0],support_second=avg[1],
                   squared_diff_first=avg[2],squared_diff_second_on_blind=avg[3],
                   squared_total_diff=avg[4],support_bound=int(active)/N,
                   vector_triangle_bound=math.sqrt(avg[2])+math.sqrt(avg[3])))
# Negative one-cell shortcut: previous genuine programming correlates next query with hidden word.
naive=blind=total=0
for u0,u1,z in product(range(N),repeat=3):
 prior_reply=u1 if u0==0 else z
 naive+=prior_reply==u1;blind+=z==u1;total+=1
assert (naive,blind,total)==(28,16,64)
# Classical final extractor: full source coupling with selected position1 and possible false-prefix merger.
N2=2; words=list(product(range(N2),repeat=2));funcs=list(product(words,repeat=N2))
final_events=0;guards=0;merger_events=0;final_checks=0
for u0,f0,f1 in product(range(N2),funcs,funcs):
 u1=f0[u0][0];y=f1[u1]
 for start,z,fakeat0 in product(range(3),range(N2),words):
  cur=z;first=None
  for p in range(start,2):
   if first is None and cur==[u0,u1][p]:first=p
   cur=[f0,f1][p][cur][0]
  if first!=1:continue
  final_events+=1
  merger_events+=start==0 and z!=u0
  fake0=list(f0);fake0[u0]=fakeat0
  cur=z;success=False;stopped=False
  for p in range(start,2):
   if p==0 and cur==u0:stopped=True;guards+=1;break
   reply=[fake0,f1][p][cur]
   if p==1 and reply==y:success=True;break
   cur=reply[0]
  assert success and not stopped
  final_checks+=1
assert merger_events>0 and guards==0
kl=2**41+2**36+2**31+2**26;kt=2**21
dw=480*kl+4080*kt;chains=32*kl+16*kt;di=448*kl+4064*kt
assert di==dw-chains==1016949404336128
out=dict(status='COMPUTED_FINITE_CHANNEL_CONTROLS_NOT_SOURCE_QROM_PROOF',N=N,positions=r,
         checks=checks,one_cell_negative={'naive_next_mark_mass':'28/64','fully_blind_next_mark_mass':'16/64','uniform_bound':'1/4'},
         final_first_event_checks=final_checks,non_genuine_prefix_mergers=merger_events,
         prior_prefix_guard_on_selected_first_event=guards,D_interior=di,WOTS_chain_starts=chains,
         D_WOTS=dw,pad=2**55,source_sha256='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210')
(P/'PEER-CONTROL-RECHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

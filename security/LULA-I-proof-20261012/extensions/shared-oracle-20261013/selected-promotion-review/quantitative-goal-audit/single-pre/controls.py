from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
N=4;tail=2;alphabet=N*tail
# Full-word one-point overlay versus the real uniform-H/challenge law.
joint=Counter();worlds=0
for h0 in product(range(alphabet),repeat=N):
    for x in range(N):
        for y in range(N):
            h=list(h0);h[x]=y*tail+h0[x]%tail
            joint[(tuple(h),x,y)]+=1;worlds+=1
assert worlds==65536
assert len(joint)==16384 and set(joint.values())=={N}
for (h,x,y),count in joint.items():
    assert h[x]//tail==y
    assert F(count,worlds)==F(1,alphabet**N*N)
# Exact N-1 miss alphabet; selected residual full-word mass is uniform.
mixture_checks=0
for y in range(N):
    hit=[v for v in range(alphabet) if v//tail==y]
    miss=[v for v in range(alphabet) if v//tail!=y]
    dist=Counter()
    for r0,r1 in product(miss,hit):
        dist[r0]+=F(N-1,N)*F(1,len(miss)*len(hit))
        dist[r1]+=F(1,N)*F(1,len(miss)*len(hit))
    assert all(dist[v]==F(1,alphabet) for v in range(alphabet));mixture_checks+=alphabet
# One-call response Fourier completion, exact character sums on full words.
def parity(v):return v.bit_count()%2
completion_worlds=0;basis_checks=0;negative_mismatches=0
for r0 in product(range(4),repeat=2):
 for r1 in product(range(4),repeat=2):
  for mark in product(range(2),repeat=2):
   completion_worlds+=1
   for x,y in product(range(2),range(4)):
    delta=r0[x]^r1[x];want=y^(r1[x] if mark[x] else r0[x])
    for yp in range(4):
     amplitude=sum(F((-1)**(parity(z&y)+parity(z&yp)+parity(z&r0[x])+mark[x]*parity(z&delta)),4) for z in range(4))
     assert amplitude==int(yp==want)
    # Deliberately dropping the queried parity phase is detectably wrong.
    if (y^r0[x])!=want:negative_mismatches+=1
    basis_checks+=1
assert completion_worlds==1024 and basis_checks==8192 and negative_mismatches>0
# Exact tiny classical output policies, not a source implementation.
policies=[]
for Q in range(N):
 total=orig=diff=0
 for h in product(range(N),repeat=N):
  for x in range(N):
   y=h[x];z=Q
   for i in range(Q):
    if h[i]==y:z=i;break
   success=h[z]==y
   total+=success;orig+=success and z==x;diff+=success and z!=x
 denominator=N**N*N
 po=F(orig,denominator);pd=F(diff,denominator);ps=F(total,denominator)
 assert po+pd==ps
 assert po==1-F(N-1,N)**(Q+1)
 assert ps==1-F(N-Q-1,N)*F(N-1,N)**(Q+1)
 assert po<=F((2*Q+1)**2,N)
 assert pd<=F(8*(Q+1)**2,N)
 policies.append({'Q':Q,'original':str(po),'different':str(pd),'success':str(ps)})
assert policies[0]['success']==str(F(2,N)-F(1,N*N))
out={'status':'PASS_FINITE_LAW_AND_ONE_QUERY_CONTROLS','overlay_worlds':worlds,'real_joint_states':len(joint),
     'residual_fullword_mixture_checks':mixture_checks,'completion_worlds':completion_worlds,
     'clean_response_basis_checks':basis_checks,'wrong_phase_negative_mismatches':negative_mismatches,
     'tiny_classical_policies':policies,
     'first_sha256':hashlib.sha256((HERE/'INDEPENDENT-FIRST.md').read_bytes()).hexdigest(),
     'clarification_sha256':hashlib.sha256((HERE/'FINITE-TABLE-CLARIFICATION.md').read_bytes()).hexdigest(),
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Finite law/character-sum controls; not a quantum optimality/source security/hardness/kernel theorem',
     'whole_goal_complete':False}
p=HERE/'CONTROL-RESULTS.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('PASS',hashlib.sha256(p.read_bytes()).hexdigest(),worlds,basis_checks)

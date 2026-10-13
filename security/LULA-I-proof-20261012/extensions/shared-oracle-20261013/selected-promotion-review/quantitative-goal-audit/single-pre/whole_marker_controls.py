from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
reports=[]
for N in (2,4):
 mu=F(2,N)-F(1,N*N);law=defaultdict(F);latent=defaultdict(F)
 for b in product((0,1),repeat=N):
  k=sum(b)
  if k:law[b]=F(k,N)*F(1,N)**(k-1)*F(N-1,N)**(N-k)
 for x in range(N):
  for bits in product((0,1),repeat=N-1):
   b=[1]*N
   for i,v in zip((i for i in range(N) if i!=x),bits):b[i]=v
   k=sum(bits)
   latent[tuple(b)]+=F(1,N)*F(1,N)**k*F(N-1,N)**(N-1-k)
 assert dict(law)==dict(latent) and sum(law.values())==1
 assert all(sum(p*b[i] for b,p in law.items())==mu for i in range(N))
 for weights in ([F(1,N)]*N,[F(int(i==0)) for i in range(N)], [F(i+1,N*(N+1)//2) for i in range(N)]):
  assert sum(p*sum(w*b[i] for i,w in enumerate(weights)) for b,p in law.items())==mu
 # G is iid exact nonzero prefix, sampled independently of the entire field.
 prefix=defaultdict(F)
 for b,p in law.items():
  for g in product(range(1,N),repeat=N):
   h=tuple(0 if b[i] else g[i] for i in range(N))
   prefix[h]+=p/F((N-1)**N)
 assert sum(prefix.values())==1
 for h in product(range(N),repeat=N):assert prefix[h]==F(h.count(0),N**N)
 # Full-word tail table independently sampled; exact size-biased real law.
 full=defaultdict(F)
 for h,p in prefix.items():
  if not p:continue
  for lower in product(range(2),repeat=N):
   word=tuple(2*h[i]+lower[i] for i in range(N))
   full[word]+=p/F(2**N)
 for word,p in full.items():assert p==F(sum(v//2==0 for v in word),N**N*2**N)
 assert sum(full.values())==1
 # Revealing b to the ghost algorithm breaks the independence requirement.
 correlated_success=sum(p*int(b[next(i for i in range(N) if b[i])]) for b,p in law.items())
 assert correlated_success==1 and correlated_success>mu
 reports.append({'N':N,'mu':str(mu),'marker_states':len(law),'prefix_states_with_mass':sum(p>0 for p in prefix.values()),
                 'fullword_states_with_mass':len(full),'independent_output_weightings':3,
                 'correlated_advice_negative_success':str(correlated_success)})
out={'status':'PASS_CORRELATED_MARK_AND_FULLWORD_LAW','reports':reports,
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact finite distribution/independence controls, not whole quantum/source theorem','whole_goal_complete':False}
p=HERE/'WHOLE-MARKER-CONTROLS.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('PASS',hashlib.sha256(p.read_bytes()).hexdigest())

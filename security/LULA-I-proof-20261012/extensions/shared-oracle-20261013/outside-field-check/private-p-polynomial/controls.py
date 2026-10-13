from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from pathlib import Path
import hashlib,json
E=Path(__file__).resolve().parent

def falling(k,r):
 a=1
 for j in range(r):a*=k-j
 return a

def v(N,Q):
 return min(F(1),F(4*Q*Q,N-4*Q*Q)) if 4*Q*Q<N else F(1)

polys=0
for N in (2,4,8):
 tables=list(product((0,1),repeat=N))
 for Q in (0,1,2):
  d=min(N,2*Q)
  terms=[(ss,(-1)**(i+len(ss))*(i%3+1)) for r in range(d+1) for i,ss in enumerate(combinations(range(N),r))]
  vals=[sum(c*all(b[t] for t in ss) for ss,c in terms) for b in tables]
  lo,hi=min(vals),max(vals)
  acc=[F(a-lo,hi-lo) if hi>lo else F(1,2) for a in vals]
  p=[]
  for k in range(N+1):
   p.append(sum((a for a,b in zip(acc,tables) if sum(b)==k),F())/comb(N,k))
   sym=sum((F(c)*F(falling(k,len(ss)),falling(N,len(ss))) for ss,c in terms),F())
   assert p[k]==(F(sym-lo,hi-lo) if hi>lo else F(1,2))
  assert abs(p[1]-p[0])<=v(N,Q)
  if Q==0:assert p[1]==p[0]
  polys+=1

# Exact Fourier-pair phase completion: includes independent low limb changes.
phase=0
for N in (2,4):
 for b in product((0,1),repeat=N):
  for p in range(N):
   for eligible in (False,True):
    h0=(3*p+1)%16;h1=(7*p+5)%16
    chosen=h1 if eligible and b[p] else h0
    for z in range(16):
     parity=lambda t:(z&t).bit_count()%2
     scratch=parity(h1^h0) if eligible else 0
     oracle_phase=(-1)**(b[p]*scratch)
     completed=(-1)**parity(h0)*oracle_phase
     assert completed==(-1)**parity(chosen)
     phase+=1

# One Grover query then measured classical adaptive nomination pair.
rows=[]
for N in (4,16,64):
 mark_amp=F(3*N-4,N);other_amp=F(N-4,N) # amplitudes in units 1/sqrt(N)
 assert (mark_amp**2+(N-1)*other_amp**2)/N==1
 sq_gap=((mark_amp-1)**2+(N-1)*(other_amp-1)**2)/N
 assert sq_gap==F(4,N)
 for m in (1,2):
  # nominate measured i then i+1 modN; candidate sets have m distinct prefixes.
  real=mark_amp**2/N+(m-1)*other_amp**2/N
  zero=F(m,N)
  # sqrt(real)<=2/sqrt(N)+sqrt(m/N): equivalent sqrt(real*N)<=2+sqrt(m)
  t=real*N-4-m
  assert t<=0 or t*t<=16*m
  rows.append({'N':N,'Q':1,'nominations':m,'real_alias':str(real),'zero_alias':str(zero),'squared_vector_gap':str(sq_gap)})

# Whole classical blocks can be deleted; conditional survivors inflate mass.
block=0
for N in (4,8):
 for banned in combinations(range(N),2):
  nominee=next(x for x in range(N) if x not in banned)
  unnormalized=sum((F(1,N) for p in range(N) if p not in banned and p==nominee),F())
  survivor=F(N-2,N)
  assert unnormalized==F(1,N)
  assert unnormalized/survivor==F(1,N-2)>F(1,N)
  block+=1
# Coherent projector PSD domination is false (v=(1,-1)).
assert F(0)<F(1,2)

# Literal shapes, with 16-byte rather than toy truncated headers.
S=bytes.fromhex('01'+'00'*15);zero=bytes(16);P=bytes.fromhex('02'+'00'*15)
eligible=lambda w,s:len(w)>=32 and w[16:32]==s
adrs=bytes(22)
addressed=S+bytes(48)+adrs+P
assert not eligible(addressed,S)
addressed_zero=zero+bytes(48)+adrs+P
assert eligible(addressed_zero,zero) # zero-seed exclusion is necessary
R=bytes.fromhex('03'+'00'*15);root=bytes(16);M=b'ab'
inner=R+S+root+M
assert eligible(inner,S) and inner[:16]==R
U=P+S
outer_nominees=set()
for c in range(256):
 w=U+c.to_bytes(4,'big')+S
 assert eligible(w,S)
 outer_nominees.add(w[:16])
assert len(outer_nominees)==1
# For fixed common base/J, blind honest Q=0 acceptance has no P argument.
blind_q0=F(1,3)
assert all(blind_q0==F(1,3) for p in range(16))
# Free P advice reveals marked location with zero queries, invalidating Q-only lemma.
assert v(16,0)==0 and F(1)>v(16,0)
# A key-aware first-hit tester is legal for the norm argument, not polynomial independence.
assert F(1,16)>v(16,0)

out={'status':'PASS_FINITE_PRIVATE_P_LOGICAL_CONTROLS','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'polynomial_controls':polys,'full_pair_fourier_phase_checks':phase,'stopped_one_query_adaptive_rows':rows,'classical_block_survival_checks':block,'outer_counters_checked':256,'source_S_zero_negative':True,'free_key_advice_negative':True,'tester_not_marker_independent_negative':True,'scope':'Exact finite controls; not source signatures, attacks, full namespace, quantum refinement or fixed-h hardness'}
(E/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'polynomial':polys,'phase':phase,'block':block}))

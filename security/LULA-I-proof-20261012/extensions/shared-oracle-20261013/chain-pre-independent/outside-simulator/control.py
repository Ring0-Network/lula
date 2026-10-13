import itertools,json
from pathlib import Path
from fractions import Fraction
from collections import Counter
P=Path(__file__).resolve().parent
class Tower:
 def __init__(self,m):
  assert m>=2 and m&(m-1)==0
  self.constants=[];self.level=0
  while 1<<self.level<m:
   s=1<<self.level
   a=next(1<<i for i in range(s) if self.trace(self.level,1<<i)==1)
   self.constants.append(a);self.level+=1
  self.m=m
 def mul(self,level,a,b):
  if level==0:return a&b
  s=1<<(level-1);mask=(1<<s)-1
  u,v=a&mask,a>>s;up,vp=b&mask,b>>s
  A=self.mul(level-1,u,up);B=self.mul(level-1,v,vp)
  C=self.mul(level-1,u^v,up^vp);D=self.mul(level-1,self.constants[level-1],B)
  return (A^D)|((C^A)<<s)
 def trace(self,level,a):
  out=0;t=a
  for _ in range(1<<level):out^=t;t=self.mul(level,t,t)
  assert out in (0,1)
  return out
 def modulus(self):
  z=1<<(self.m//2);root=z;roots=[]
  for _ in range(self.m):roots.append(root);root=self.mul(self.level,root,root)
  assert root==z and len(set(roots))==self.m
  c=[1]
  for r in roots:
   n=[0]*(len(c)+1)
   for j,a in enumerate(c):n[j]^=self.mul(self.level,a,r);n[j+1]^=a
   c=n
  assert all(a in (0,1) for a in c)
  return sum(a<<j for j,a in enumerate(c))
def rem(a,p):
 while a.bit_length()>=p.bit_length():a^=p<<(a.bit_length()-p.bit_length())
 return a
def pmul(a,b):
 c=0
 while b:
  if b&1:c^=a
  a<<=1;b>>=1
 return c
def gcd(a,b):
 while b:a,b=b,rem(a,b)
 return a
def irred(p,m):
 x=2;t=x
 for j in range(1,m+1):
  t=rem(pmul(t,t),p)
  if j<=m//2:assert gcd(p,t^x)==1
 assert t==x
 return True
fields=[]
for m in (2,4,8,16):
 f=Tower(m);mod=f.modulus();assert mod.bit_length()==m+1
 assert irred(mod,m)
 fields.append(dict(m=m,tower_trace_one_constants=f.constants,binary_modulus_hex=hex(mod),irreducible=True))
# Every byte word of length<=2 has a distinct length-sensitive code, including leadingzero strings.
def enc(w):return sum(256**j for j in range(len(w)))+int.from_bytes(w,'big')
words=[b'']+[bytes([a]) for a in range(256)]+[i.to_bytes(2,'big') for i in range(65536)]
codes={enc(w) for w in words}
assert len(codes)==len(words)==65793 and min(codes)==0 and max(codes)==65792
assert [enc(w) for w in (b'',b'\0',b'\0\0')]==[0,1,257]
f=Tower(2)
def eval_poly(cs,x):
 a=0
 for c in reversed(cs):a=f.mul(f.level,a,x)^c
 return a
families={k:[tuple(eval_poly(cs,x) for x in range(4)) for cs in itertools.product(range(4),repeat=k)] for k in (2,4)}
for i,j in itertools.combinations(range(4),2):
 counts=Counter((v[i],v[j]) for v in families[2]);assert len(counts)==16 and set(counts.values())=={1}
assert len(set(families[4]))==256, 'Vandermonde full domain map not bijective'
bits={k:[tuple(z&1 for z in v) for v in vs] for k,vs in families.items()}
rf=list(itertools.product(range(2),repeat=4))
def density(vs):
 n=len(vs)
 return [[sum(Fraction((-1)**(v[i]+v[j]),4*n) for v in vs) for j in range(4)] for i in range(4)]
assert density(bits[2])==density(rf), 'one-query phase density differs for2-wise family'
assert Counter(bits[4])==Counter({v:16 for v in rf})
# Three honest/classifier basis evaluations then one adversary basis-XOR query compute global parity.
# Counting just adversarialQ=1 selects2-wise and is invalid for this compiledT=4 experiment.
wrong=Fraction(sum(sum(v)%2==0 for v in bits[2]),len(bits[2]))
right=Fraction(sum(sum(v)%2==0 for v in bits[4]),len(bits[4]))
random=Fraction(sum(sum(v)%2==0 for v in rf),len(rf))
assert wrong==1 and right==random==Fraction(1,2)
out=dict(status='COMPUTED_TOY_FIELD_AND_QUERY_CONTROLS_NOT_FULL_SOURCE_KERNEL_PROOF',
 deterministic_tower_moduli=fields,encoded_byte_words=65793,leadingzero_codes=[0,1,257],
 gf4_two_wise_full_output_pair_checks=6,gf4_full_domain_family_seed_count=256,
 one_quantum_query_phase_density_exact=True,compiled_honest_queries=3,compiled_adversarial_queries=1,
 wrong_adversary_only_two_wise_parity_success=str(wrong),correct_full_budget_family_parity_success=str(right),
 random_function_parity_success=str(random))
(P/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

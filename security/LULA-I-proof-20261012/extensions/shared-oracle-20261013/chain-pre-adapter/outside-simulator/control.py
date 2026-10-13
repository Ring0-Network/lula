"""Independent exact finite controls for tower/k-wise whole-budget simulator."""
from functools import lru_cache
from itertools import product
from collections import Counter
from fractions import Fraction
from pathlib import Path
import random,json,hashlib
P=Path(__file__).resolve().parent
@lru_cache(None)
def mul(a,b,m):
 assert m>0 and m&(m-1)==0 and 0<=a<1<<m and 0<=b<1<<m
 if m==1:return a&b
 s=m//2;mask=(1<<s)-1;a0=a&mask;a1=a>>s;b0=b&mask;b1=b>>s
 ac=mul(a0,b0,s);bd=mul(a1,b1,s);cross=mul(a0^a1,b0^b1,s)
 return (ac^mul(bd,1<<(s-1),s))|((cross^ac)<<s)
def power(a,n,m):
 v=1
 while n:
  if n&1:v=mul(v,a,m)
  a=mul(a,a,m);n>>=1
 return v
def trace(a,m):
 v=0;x=a
 for _ in range(m):v^=x;x=mul(x,x,m)
 return v
def horner(coeff,x,m):
 v=0
 for c in reversed(coeff):v=mul(v,x,m)^c
 return v
rng=random.Random(93920261013)
fields=[]
for m in [1,2,4,8,16]:
 alpha=1<<(m-1)
 assert trace(alpha,m)==1
 vals=list(range(1,1<<m)) if m<=8 else [rng.randrange(1,1<<m) for _ in range(64)]
 for a in vals:
  assert mul(a,power(a,(1<<m)-2,m),m)==1
  assert power(a,1<<m,m)==a
 for _ in range(64):
  a,b,c=[rng.randrange(1<<m) for _ in range(3)]
  assert mul(a,b,m)==mul(b,a,m)
  assert mul(mul(a,b,m),c,m)==mul(a,mul(b,c,m),m)
  assert mul(a,b^c,m)==mul(a,b,m)^mul(a,c,m)
 if m<=8:
  assert all(mul(x,x,m)^x^alpha for x in range(1<<m))
 fields.append(dict(degree=m,alpha=alpha,absolute_trace=1,inverse_checks=len(vals),
                    all_artin_schreier_inputs_tested=(1<<m) if m<=8 else 0))
# Complete projected k-wise families on four field inputs (GF4 ->1bit).
affine=[tuple(horner(c,x,2)&1 for x in range(4)) for c in product(range(4),repeat=2)]
fullfamily=[tuple(horner(c,x,2)&1 for x in range(4)) for c in product(range(4),repeat=4)]
rf=list(product(range(2),repeat=4))
fullvalues=[tuple(horner(c,x,2) for x in range(4)) for c in product(range(4),repeat=4)]
assert len(set(fullvalues))==256
assert set(Counter(fullfamily).values())=={16} and set(Counter(affine).values())=={2}
for x,y in product(range(4),repeat=2):
 if x!=y:
  assert set(Counter((f[x],f[y]) for f in affine).values())=={4}
# Exact one-query Choi channel equality, includes arbitrary reference register.
def choi_count(fs):
 cnt=Counter();d=8
 for f in fs:
  perm=[((i>>1)<<1)|((i&1)^f[i>>1]) for i in range(d)]
  for i,j in product(range(d),repeat=2):cnt[(i*d+perm[i],j*d+perm[j])]+=1
 return {key:Fraction(v,len(fs)*d) for key,v in cnt.items()}
assert choi_count(affine)==choi_count(rf)
#Three honest reads followed by one adversarial basis query: ignorehonest budget => false.
def parity_probability(fs):return Fraction(sum((f[0]^f[1]^f[2])==f[3] for f in fs),len(fs))
assert parity_probability(affine)==1 and parity_probability(rf)==parity_probability(fullfamily)==Fraction(1,2)
# Whole adaptive post-C row registration, preserve full2-bit Row images+bottom.
rowfuncs=list(product(range(4),repeat=4))
def whole_row_output(fs):
 weights=Counter(fs);out=Counter();total=len(fs)*len(rowfuncs)
 for f,weight in weights.items():
  C=f[0]^f[1]^f[2] #counted honestpreparation evaluations, not coefficient inspection.
  for row in rowfuncs:
   accepted=[c for c in range(2) if row[2*C+c]>>1]
   if not accepted:out[(C,None,None,False)]+=weight;continue
   c0=accepted[0];Y=row[2*C+c0]
   success=f[3]==C and (row[2*(1-C)]>>1)==(Y>>1)
   out[(C,c0,Y,success)]+=weight
 return {key:Fraction(v,total) for key,v in out.items()}
assert whole_row_output(rf)==whole_row_output(fullfamily)
def success_prob(out):return sum(p for (*_,success),p in out.items() if success)
assert success_prob(whole_row_output(rf))==Fraction(3,16)
assert success_prob(whole_row_output(affine))==Fraction(3,8)
# Injective lexical encoding, including leading-zero words, and zero malformed extension.
def encode(x):return sum(256**j for j in range(len(x)))+int.from_bytes(x,'big')
b=2;V=sum(256**j for j in range(b+1));encodings=[]
for ell in range(b+1):
 for v in range(256**ell):encodings.append(encode(v.to_bytes(ell,'big')))
assert sorted(encodings)==list(range(V))
assert [encode(x) for x in [b'',b'\0',b'\0\0']]==[0,1,257]
valid=invalid=0
for ell,payload in product(range(4),range(256**b)):
 data=payload.to_bytes(b,'big')
 good=ell<=b and all(x==0 for x in data[ell:])
 valid+=good;invalid+=not good
 if good:assert encode(data[:ell])<V
assert valid==V==65793 and invalid==196351
# Static complete budget ledger; arithmetic only, no crypto/build/benchmark.
q_exps=[24,30,38,40,41,44,50,64];budgets=[]
L=2**32;hs=2**21*(19505+L)-1
for qe, Qe, mode in product(q_exps,[32,64],['hot','cold']):
 q=2**qe;Q=2**Qe;hm=82090+5*L if mode=='hot' else 8560574463+82090+6*L
 R=hs+q*hm+3224
 budgets.append(dict(q_exp=qe,Q_exp=Qe,mode=mode,T_PRE=Q+R+254,T_ROW=Q+R+17392,
                     T_PRE_classifier=Q+R+254+6000))
profiles=[]
for bb in [0,2,598,1072,65584]:
 target=max(256,8*bb+1);m=1
 while m<target:m*=2
 assert target<=m<2*target
 profiles.append(dict(byte_bound=bb,field_degree=m,bit_target=target))
out=dict(status='COMPUTED_EXACT_FINITE_CONTROLS_NOT_FULL_SOURCE_PROOF',fields=fields,
         coefficient_seeds_affine=16,coefficient_seeds_full=256,complete_field_tables=256,
         projected_tables_full=16,one_query_full_Choi_equal=True,
         query_budget_negative={'honest_calls':3,'adversary_basis_calls':1,'wrong_Qonly':'1','RF_and_correct_total':'1/2'},
         whole_postC_row_success={'RF':'3/16','correct_total_family':'3/16','wrong_Qonly_family':'3/8'},
         whole_postC_row_joint_output_law_equal=True,valid_byte_words=V,invalid_register_states=invalid,
         source_encoding=[0,1,257],static_budgets=budgets,profiles=profiles)
(P/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='static_budgets'},indent=2))

from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt,log2
import json
E=Path(__file__).resolve().parent;X=E.parent.parent
N=1<<128;M=N*N-N;TARGET=F(1,2);BITS=512
models=('conservative','event','polynomial','best')
qlogs=(24,30,38,40,41,44,50,64)
inputs={name:X/name for name in ('QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md','SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md','SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md','QUANTUM-RO-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md','classical-composition-numeric/OWN-BOUNDS.json','classical-composition-numeric/bounds.py','query-resource-independent/thresholds.py')}
pins={k:sha256(p.read_bytes()).hexdigest() for k,p in inputs.items()}
manifest=json.loads((X/'classical-composition-numeric'/'SHA256SUMS.json').read_text())
assert pins['classical-composition-numeric/OWN-BOUNDS.json']==manifest['OWN-BOUNDS.json']
assert pins['classical-composition-numeric/bounds.py']==manifest['bounds.py']
data=json.loads(inputs['classical-composition-numeric/OWN-BOUNDS.json'].read_text())
def dyadic(a):
 sign,m,e,b=a;assert sign==0 and m.bit_length()==b
 return F(m*(1<<e)) if e>=0 else F(m,1<<(-e))
PF={};pfmeta={}
for row in data['rows']:
 k=row['log2_signing_query_cap'];a=row['FORS_per_raw_candidate']
 p=(dyadic(a['lower_dyadic_mpf_tuple']),dyadic(a['upper_dyadic_mpf_tuple']))
 assert 0<=p[0]<=p[1]<=F(1,512)
 if k in PF:assert PF[k]==p
 PF[k]=p;pfmeta[k]={'enclosure':[[str(z.numerator),str(z.denominator)] for z in p],'positive_check':row['positive_crosscheck']}
assert set(PF)==set(qlogs)
# Intervals are pairs; only positive isotone operations are used.
def exact(x):return (F(x),F(x))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,k):assert k>=0;return a[0]*k,a[1]*k
def square(a):assert a[0]>=0;return a[0]*a[0],a[1]*a[1]
def cap(a):return min(F(1),a[0]),min(F(1),a[1])
def minimum(*args):return min(a[0] for a in args),min(a[1] for a in args)
def root(a,precision):
 den=1<<precision
 def endpoint(z,upper):
  n=isqrt((z.numerator<<(2*precision))//z.denominator)
  lo=F(n,den);hi=F(n+1,den)
  assert lo*lo<=z<hi*hi
  return (lo if lo*lo==z else hi) if upper else lo
 return endpoint(a[0],False),endpoint(a[1],True)
def formulas(q,Q,pf,p):
 D=cap(scale(add(root(exact(F(Q+q+1,M)),p),exact(F(Q+q+1,2*M))),q))
 A=cap(add(D,scale(add(pf,exact(F(1,N)+F(q,N*N))),8*(Q+2)**2)))
 c=cap(add(scale(square(add(exact(2*Q),root(exact(q),p))),F(1,N)),square(add(exact(F(2*(Q+2),1<<64)),root(A,p)))))
 h=cap(scale(square(add(exact(2*Q),root(exact(3017),p))),F(1,N)))
 g=cap(exact(F(8*(Q+3218)**2,N)));d=cap(exact(F(8*(Q+6)**2,N)))
 public=add(add(c,h),add(g,d));e=cap(public)
 delta=cap(exact(F(2*Q,1<<64)+F(2*q+2,N)))
 con=cap(add(exact(F(1,N)),add(delta,public)))
 baseline=cap(add(cap(exact(F(2*q+2,N))),e))
 event=cap(add(exact(F(1,N)),square(add(exact(F(2*Q,1<<64)),root(baseline,p)))))
 v=cap(exact(F(4*Q*Q,N-4*Q*Q))) if 4*Q*Q<N else exact(1)
 t=cap(scale(square(add(exact(2*Q),root(exact(min(N,2*q+2)),p))),F(1,N)))
 ap=cap(add(v,t));poly=cap(add(exact(F(1,N)),add(v,add(ap,e))))
 return {'conservative':con,'event':event,'polynomial':poly,'best':minimum(con,event,poly)}
def judge(a):
 if a[1]<=TARGET:return True
 if a[0]>TARGET:return False
 raise ArithmeticError('UNCERTIFIED STRADDLING INTERVAL')
def pair(a):return [str(a.numerator),str(a.denominator)]
def serial(a):return {'lower':pair(a[0]),'upper':pair(a[1])}
rows=[]
for k in qlogs:
 q=1<<k;cache={}
 def f(Q):
  if Q not in cache:cache[Q]=formulas(q,Q,PF[k],BITS)
  return cache[Q]
 crossings={}
 for model in models:
  assert judge(f(0)[model])
  a,b=0,1
  while judge(f(b)[model]):a,b=b,2*b
  while b-a>1:
   mid=(a+b)//2
   if judge(f(mid)[model]):a=mid
   else:b=mid
  assert b==a+1 and judge(f(a)[model]) and not judge(f(b)[model])
  # A separate outward precision must certify the same adjacent endpoints.
  for endpoint in (a,b):assert judge(formulas(q,endpoint,PF[k],256)[model])==judge(f(endpoint)[model])
  row={'log2_q':k,'q':str(q),'model':model,'Q_pass':str(a),'Q_fail':str(b),'log2_Q_pass_approx':log2(a),'pass_interval':serial(f(a)[model]),'fail_interval':serial(f(b)[model]),'pass_margin':pair(TARGET-f(a)[model][1]),'fail_margin':pair(f(b)[model][0]-TARGET),'adjacent_integer_certificate':True,'second_precision_bits':256}
  rows.append(row);crossings[model]=a
 assert crossings['best']==max(crossings['conservative'],crossings['event'],crossings['polynomial'])
 print(json.dumps({'qlog':k,'crossings':crossings}),flush=True)
results={'status':'CERTIFIED_NEW_COMPLETE_QUERY_ENVELOPE_CROSSINGS','target':pair(TARGET),'pins':pins,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'root_new_numeric_results_read':False,'sqrt_precision_bits':BITS,'independent_endpoint_precision_bits':256,'coverage_input':'reuse of hash-pinned previously reviewed exact-binomial dyadic enclosures; not a fresh occupancy theorem','FORS_enclosures':pfmeta,'monotonicity':'all nonnegative isotone operations; increasing capped v with no downward branch jump; finite min nondecreasing','best_crossing_equals_max_component_crossings':True,'rows':rows,'interpretation':'PASS proves sufficient-envelope <=1/2; FAIL proves sufficient-envelope >1/2, not attack or actual adversarial success','new_source_game_declarations':0,'whole_goal_complete':False,'old_scalars_changed':False}
(E/'NEW-CERTIFICATES.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
text=['# Independent new complete query-envelope certificates','',results['interpretation'],'','| log2(q) | Envelope | Q pass | Q fail | Approx. log2(Q pass) |','|---:|---|---:|---:|---:|']
for r in rows:text.append(f"| {r['log2_q']} | {r['model']} | {r['Q_pass']} | {r['Q_fail']} | {r['log2_Q_pass_approx']:.12f} |")
text+=['','Every adjacent endpoint and margin is certified by exact rational outward arithmetic at 512 and 256 sqrt bits. Display logarithms are not certificate inputs. The reused pF enclosure is an explicit reviewed premise. Honest computation, gates, storage, fixed SHA and categories are outside this raw-query conclusion. Old scalar/core files remain unchanged; new source/game declarations zero.']
(E/'NEW-CERTIFICATES.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
print(json.dumps({'certificate_sha256':sha256((E/'NEW-CERTIFICATES.json').read_bytes()).hexdigest(),'md_sha256':sha256((E/'NEW-CERTIFICATES.md').read_bytes()).hexdigest()}))

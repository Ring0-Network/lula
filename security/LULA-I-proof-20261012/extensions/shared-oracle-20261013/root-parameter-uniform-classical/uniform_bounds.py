"""Exact rational upper certificates for the guarded classical source schema.

No implementation or quantum retuning, attacks, signing, or timings. Probability
upper bounds are sufficient certificates, never lower bounds on attack work.
Usage: python -I -B uniform_bounds.py --params tuple.json --out result.json
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math
X=Path(__file__).resolve().parent.parent
QS=(24,30,38,40,41,44,50,64)
THEOREM=X/'PARAMETER-UNIFORM-CLASSICAL-THEOREM.md'
THEOREM_SHA='e5fc68bc269ca98672caa99ec70d5695d3d578095a62ebbfc0f99f9d8fbc394b'
SOURCE=X.parents[3]/'publications/LULA-I/release/code/lula1/src/lib.rs'
SOURCE_SHA='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
BASE={'n_bytes':16,'a':9,'r':17,'heights':[5,5,5,5,21],
 'ell':[32,32,32,32,16],'S':[240,240,240,240,2040]}

def guarded(p):
 if set(p)!=set(BASE):raise ValueError('Expected exactly '+','.join(BASE))
 if any(type(p[k]) is not int for k in ('n_bytes','a','r')):raise ValueError('Integer fields required')
 if p['n_bytes']!=16 or not 1<=p['a']<=31 or not 1<=p['r']<=94:raise ValueError('n/a/r outside theorem')
 d=len(p['heights'])
 if not 1<=d<=256:raise ValueError('Layer ID bound')
 for k in ('heights','ell','S'):
  if not isinstance(p[k],list) or len(p[k])!=d or any(type(v) is not int for v in p[k]):raise ValueError('Layer integer vectors required')
 if any(not 0<=h<=31 for h in p['heights']) or sum(p['heights'])>63:raise ValueError('Height encoding bound')
 if p['r']*(1<<p['a'])>1<<32:raise ValueError('FORS u32 index bound')
 if (p['r']+1)*p['a']+sum(p['heights'])>256:raise ValueError('Full digest coordinate bound')
 if 22+16*p['r']+9>24*64:raise ValueError('Source tail buffer bound')
 widths=[4]*(d-1)+[8]
 for lw,ell,S in zip(widths,p['ell'],p['S']):
  if not 1<=ell<=128//lw or not 0<=S<ell*((1<<lw)-1):raise ValueError('Strict target and complete digest encoding required')
 return widths

def stirling(r):
 s=[1]
 for i in range(1,r+1):s=[0]+[s[j-1]+j*(s[j] if j<len(s) else 0) for j in range(1,i+1)]
 return s

def positive_upper(q,p):
 """E[Z^r] <= Touchard_r(q/B), and 1-(1-1/t)^Z <= Z/t."""
 mu=F(q,1<<sum(p['heights']));t=1<<p['a']
 moment=sum((c*mu**j for j,c in enumerate(stirling(p['r']))),F(0))
 return min(F(1,t),moment/t**(p['r']+1))

def record(v):
 assert v>=0
 return {'numerator':str(v.numerator),'denominator':str(v.denominator),
  'display_negative_log2_approx':math.log2(v.denominator)-math.log2(v.numerator) if v else None}

def evaluate(p,q,Q):
 widths=guarded(p);d=len(widths);h=sum(p['heights']);N=1<<128
 tails=[ell*((1<<lw)-1)-S for lw,ell,S in zip(widths,p['ell'],p['S'])]
 H=p['r']+sum(tails);G=p['r']*(p['a']+1)+1+sum(t+1+hi for t,hi in zip(tails,p['heights']))
 C=H+G+d+3
 assert C==p['r']*(p['a']+2)+2*sum(tails)+h+2*d+4
 # beta^L <= exp(-L/t) <= 2^(-L/t), L/t an integer here.
 # Weakening a huge exponent to2048 avoids enormous integer allocation.
 finite_exponent=min(1<<(32-p['a']),2048)
 terms={'public_slots':F(3*Q,N),'honest_inner':F(2*q,N),'terminal_seed_constant':F(C,N),
  'full256_bridge':F(q*Q+q*(q-1)//2+q,N*N),
  'finite_counter_upper':F(q,1<<finite_exponent),
  'coverage_upper':(Q+1)*positive_upper(q,p)}
 uncapped=sum(terms.values(),F(0));cap=min(F(1),uncapped)
 signature=20+16*p['r']*(p['a']+1)+sum(4+16*(ell+hi) for ell,hi in zip(p['ell'],p['heights']))
 cache=36*(1<<p['heights'][-1])-16
 return {'q':str(q),'Q':str(Q),'H':H,'G':G,'C':C,'signature_bytes':signature,'cache_payload_bytes':cache,
  'pF_positive_upper':record(positive_upper(q,p)),
  'finite_counter_dyadic_exponent_used':finite_exponent,
  'terms':{k:record(v) for k,v in terms.items()},'uncapped_upper':record(uncapped),'capped_upper':record(cap),
  'sufficient_at_success_half':uncapped<=F(1,2),
  'necessary_half_certificate_public_fee_passes':F(3*Q+2*q+C,N)<=F(1,2),
  'actual_attack_or_work_bits_or_category_or_repair_certified':False}

def controls():
 # Exact finite binomial enumeration checks both positive inequalities.
 n=0
 for r in range(1,8):
  for q in range(0,9):
   for h in range(0,4):
    for a in range(1,4):
     B=1<<h;t=1<<a;rho=F(1,B);beta=F(t-1,t)
     p={'heights':[h],'r':r,'a':a}
     exact=sum((math.comb(q,z)*rho**z*(1-rho)**(q-z)*(1-beta**z)**r/t for z in range(q+1)),F(0))
     assert exact<=positive_upper(q,p);n+=1
 baseline=evaluate(BASE,1<<40,1<<64)
 assert (baseline['H'],baseline['G'],baseline['C'],baseline['signature_bytes'],baseline['cache_payload_bytes'])==(3017,3217,6242,5720,75497456)
 # Distinct rejected proof guards; source geometry alone is insufficient.
 invalid=[dict(BASE,S=[480,240,240,240,2040]),dict(BASE,n_bytes=32),
  dict(BASE,a=31,r=94),dict(BASE,ell=[33,32,32,32,16]),dict(BASE,heights=[32,5,5,5,21])]
 for p in invalid:
  try:guarded(p)
  except ValueError:pass
  else:raise AssertionError('Invalid tuple accepted')
 return {'exact_small_binomial_inequalities':n,'negative_guard_cases':len(invalid),'baseline_counts_bytes_recovered':True}

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--params',type=Path)
 ap.add_argument('--log2-Q',type=int,nargs='+',default=[64,125,128]);ap.add_argument('--out',type=Path,required=True)
 args=ap.parse_args()
 if any(not 0<=b<=256 for b in args.log2_Q):ap.error('Q exponent0..256')
 assert sha(THEOREM)==THEOREM_SHA and sha(SOURCE)==SOURCE_SHA
 p=json.loads(args.params.read_text(encoding='utf8')) if args.params else BASE
 guarded(p)
 out={'status':'COMPUTED_EXACT_RATIONAL_GUARDED_CLASSICAL_UPPER_CERTIFICATES',
  'proof_status':'Manual uniform source theorem; exact final review separately recorded',
  'theorem_sha256':sha(THEOREM),'script_sha256':sha(Path(__file__)), 'source_sha256':sha(SOURCE),
  'parameters':p,'baseline':p==BASE,'controls':controls(),
  'coverage_method':'Positive Touchard upper; not the exact pF nor a substituted Poisson model',
  'finite_counter_method':'beta^2^32 <=2^(-2^(32-a)); exponent weakened to min(2048,2^(32-a))',
  'rows':[{'log2_q':k,'log2_Q':b,**evaluate(p,1<<k,1<<b)} for k in QS for b in sorted(set(args.log2_Q))],
  'quantum_retuning':'NOT_ESTABLISHED','original_level_category_minimal_repair':'not established',
  'whole_goal_complete':False,'new_signatures_benchmarks_or_source_edits':0}
 args.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
 print(json.dumps({'status':out['status'],'rows':len(out['rows']),'controls':out['controls'],
  'half_success_passes':sum(r['sufficient_at_success_half'] for r in out['rows']),'whole_goal_complete':False}))

if __name__=='__main__':main()

"""Root exact verification of the new classical source ledger and required budgets."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,importlib.util
import mpmath as mp
E=Path(__file__).resolve().parent;X=E.parent;N=1<<128
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((X/n).read_text(encoding='utf8'))
own=read('pre-start-second/classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json')
review=read('pre-start-second/classical-joint-root-crosscheck/FINAL-SUBJECT-REVIEW.json')
assert all(review['checks'].values())
assert review['subject_sha256']==sha(X/'CLASSICAL-JOINT-RO-THEOREM.md')
assert review['own_dataset_sha256']==sha(X/'pre-start-second/classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json')
old=read('classical-composition-numeric/OWN-BOUNDS.json')
assert own['inherited_pF_input_sha256']==sha(X/'classical-composition-numeric/OWN-BOUNDS.json')
def dyad(t):
 s,m,e,b=t;assert s==0 and m.bit_length()==b
 return F(m<<e) if e>=0 else F(m,1<<(-e))
pf={}
for row in old['rows']:
 k=row['log2_signing_query_cap'];v=row['FORS_per_raw_candidate']
 p=tuple(dyad(v[n]) for n in ('lower_dyadic_mpf_tuple','upper_dyadic_mpf_tuple'))
 assert k not in pf or pf[k]==p
 pf[k]=p
def envelope(q,Q):
 base=F(3*Q+2*q+6242,N)+F(q*Q+q*(q-1)//2+q,N*N)
 lo,hi=pf[q.bit_length()-1]
 return base+(Q+1)*lo,base+(Q+1)*hi+F(q,1<<4096)
def m(v):return mp.mpf(v.numerator)/v.denominator
f=lambda pair:F(*map(int,pair))
source=X.parents[1]/'numerics/bounds.py'
spec=importlib.util.spec_from_file_location('frozen_pf',source)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
rows=[]
with mp.workdps(500):
 for k in (24,30,38,40,41,44,50,64):
  q=1<<k;p=mod.fors_moment(q,41,9,18,dps=500)
  assert m(pf[k][0])<=p<=m(pf[k][1])
  for e in (32,64,128):
   Q=1<<e;lo,hi=envelope(q,Q)
   peer=next(r for r in own['rows'] if r['q_exponent']==k and r['QH_exponent']==e)
   assert f(peer['uncapped_lower'])==lo and f(peer['uncapped_upper'])==hi
   assert f(peer['capped_lower'])==min(F(1),lo) and f(peer['capped_upper'])==min(F(1),hi)
   assert f(peer['old_minus_new_uncapped_exact'])==F(3*Q+q+1,N)
   display=min(mp.mpf(1),m(F(3*Q+2*q+6242,N)+F(q*Q+q*(q-1)//2+q,N*N))+(Q+1)*p)
   assert abs(display-mp.mpf(peer['own_numeric_probability']))<=mp.mpf('1e-200')*max(mp.mpf(1),display)
   if e==128:assert min(F(1),lo)==min(F(1),hi)==1
   rows.append({'q_exponent':k,'QH_exponent':e,'probability_exponent_display':float(-mp.log(display,2)),
                'exact_cap_one':min(F(1),lo)==min(F(1),hi)==1})
cross=[]
for k in (24,30,38,40,41,44,50,64):
 q=1<<k;lower,upper=pf[k]
 slope=F(3,N)+F(q,N*N)+upper
 intercept=F(2*q+6242,N)+F(q*(q-1)//2+q,N*N)+upper+F(q,1<<4096)
 root=(F(1,2)-intercept)/slope
 passed=max(0,root.numerator//root.denominator);failed=passed+1
 assert envelope(q,passed)[1]<=F(1,2)<envelope(q,failed)[0]
 peer=next(r for r in own['half_success_crossings'] if r.get('q_exponent',r.get('log2_q'))==k)
 assert int(peer['Q_pass'])==passed and int(peer['Q_fail'])==failed
 cross.append({'q_exponent':k,'Q_pass':str(passed),'Q_fail':str(failed)})
out={'status':'PASS24_CLASSICAL_JOINT_ROWS_AND8_EXACT_ADJACENT_CROSSINGS',
 'script_sha256':sha(Path(__file__)),'subject_sha256':sha(X/'CLASSICAL-JOINT-RO-THEOREM.md'),
 'peer_review_sha256':sha(X/'pre-start-second/classical-joint-root-crosscheck/FINAL-SUBJECT-REVIEW.json'),
 'peer_dataset_sha256':sha(X/'pre-start-second/classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json'),
 'inherited_pf_input_sha256':sha(X/'classical-composition-numeric/OWN-BOUNDS.json'),
 'frozen_pf_calculator_sha256':sha(source),'root_dps':500,'rows':rows,'crossings':cross,
 'QH128_all_cap_one':True,'new_source_game_declarations':0,'category':'not established',
 'scope':'Root exact Fraction crosscheck and high precision confirmation; inherited pF interval premise; no new kernel or category'}
(E/'ROOT-JOINT-CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'q40_Q64':next(r for r in rows if r['q_exponent']==40 and r['QH_exponent']==64),
 'crossings':len(cross),'QH128_all_cap_one':True}))

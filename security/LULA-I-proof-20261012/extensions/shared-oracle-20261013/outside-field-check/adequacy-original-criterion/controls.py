from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
E=Path(__file__).resolve().parent
N=1<<128;tau_c=F(1,N);tau_q=F(1,1<<64)
classical=[];quantum=[]
for k in (24,30,38,40,41,44,50,64):
 q=1<<k
 for Q in (0,1<<32,1<<128):
  floor=min(F(1),F(3*Q+2*q+6242,N))
  assert floor>tau_c
  if Q==N:assert floor==1
  classical.append({'qlog':k,'Q':str(Q),'classical_envelope_lower_floor':str(floor),'floor_greater_than_2_minus_128':True})
 for Q in (1<<32,1<<63,1<<64):
  # h alone lower-bounds every complete quantum sufficient envelope.
  h_strict_lower=min(F(1),F(4*Q*Q,N))
  if Q==1<<32:assert h_strict_lower>tau_q
  # For Q>=2^63: conservative delta>=1, event a>=1, polynomial v=1.
  if Q>=1<<63:
   assert F(2*Q,1<<64)>=1 and 4*Q*Q>=N
  quantum.append({'qlog':k,'Q':str(Q),'quantum_h_floor':str(h_strict_lower),'all_three_envelopes_cap_one':Q>=1<<63})
g0=8*3218**2
assert F(1+g0,N)>tau_c and 1+g0<N
# Exact necessary h-gate integer boundary, without floating roots.
qpass=(1<<31)-28;qfail=qpass+1
assert (1<<32)-2*qpass>0 and ((1<<32)-2*qpass)**2>=3017
assert ((1<<32)-2*qfail)**2<3017
# Noninverse control: the SAME loose valid envelope admits incompatible true risks.
loose=F(1);actual_secure=F(0);actual_insecure=F(1)
assert actual_secure<=loose and actual_insecure<=loose
assert actual_secure<tau_c<actual_insecure
# Abstract ideal uniform search control, never a cryptographic/source construction.
search=[]
for n in (2,4,8):
 size=1<<n
 for Q in (0,1,size//2,size):
  p=F(min(size,Q),size)
  assert p<=1
  search.append({'N':size,'distinct_test_budget':Q,'success':str(p)})
 assert F(size,size)==1 and F(1,size)<1
# A certificate for <=1/2 does not prove absence of exact-1/2 success.
assert F(1,2)<=F(1,2)
# Reject identifying adversary query budgets with signing capacity.
assert (1<<40)!=(1<<128) and (1<<40)!=(1<<64)
r={'status':'PASS_EXACT_CRITERION_AND_NO_CROSSING_CONTROLS','script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'classical_floor_rows':classical,'quantum_floor_rows':quantum,'quantum_Q0_envelope_lower_floor':str(F(1+g0,N)),'necessary_h_2_minus_64_Q_pass':str(qpass),'necessary_h_2_minus_64_Q_fail':str(qfail),'ideal_search_rows':search,'loose_upper_bound_does_not_determine_actual_risk':True,'strict_vs_nonstrict_threshold_negative':True,'source_valid_forgery_or_attack_constructed':False,'scope':'Algebraic controls of sufficient envelopes and an abstract search benchmark; no source attack/optimality/category conclusion','new_source_game_declarations':0,'whole_goal_complete':False}
(E/'CONTROL-RESULTS.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':r['status'],'classical_rows':len(classical),'quantum_rows':len(quantum),'necessary_h_gate':(qpass,qfail),'result_sha256':sha256((E/'CONTROL-RESULTS.json').read_bytes()).hexdigest()}))

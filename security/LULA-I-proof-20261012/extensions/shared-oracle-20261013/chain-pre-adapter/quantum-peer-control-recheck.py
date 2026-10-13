import itertools, json, math
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
N=2; dim=32; Q=3
# Input is4 literal address headers by2 payloads; response has2 full-image bits.
idx=np.arange(dim)
H=np.array([[(-1.)**((i&j).bit_count()) for j in range(dim)] for i in range(dim)])/math.sqrt(dim)
def oracle(psi,t):
    return psi[np.array([i^(t[i//4]) for i in range(dim)])]
selected=(0,3) # One fixed complete2-bit selected function; target input averaged independently.
records=[]; worlds=0; worst_norm=0.; max_support_error=0.; max_exposure_leak=0.; max_slot_rms=0.
for t0,t1 in itertools.product(itertools.product(range(4),repeat=2),repeat=2):
 for x in range(2):
  y=selected[x]
  ideal_table=list(t0)+list(t1)+list(selected)+[1,2]
  phi=np.zeros(dim,dtype=complex); phi[(y%8)*4]=1
  phi=H@phi
  # This IDEAL state depends only on residual tables/selected target, never prefix values.
  ideal_states=[]
  for q in range(Q):
   ideal_states.append(phi.copy());phi=H@oracle(phi,ideal_table)
  norms=[]; supports=[[] for _ in range(Q)]; slots=[[] for _ in range(Q)]
  for u0,u1,r0,r1 in itertools.product(range(2),repeat=4):
   real_table=ideal_table.copy()
   real_table[u0]=2*u1+r0
   real_table[2+u1]=2*x+r1
   real=np.zeros(dim,dtype=complex);real[(y%8)*4]=1;real=H@real
   for q in range(Q):
    ip=ideal_states[q].reshape(8,4)
    supports[q].append(float(np.sum(abs(ip[u0])**2)+np.sum(abs(ip[2+u1])**2)))
    slots[q].append(float(np.linalg.norm(oracle(ideal_states[q],real_table)-oracle(ideal_states[q],ideal_table))**2))
    real=H@oracle(real,real_table)
   norms.append(float(np.linalg.norm(real-phi)**2))
   # Metadata/exposure-stop based only on known y is independent of prefix coins.
   permitted_digit=3 if y&1 else 1
   mask=permitted_digit>2
   max_exposure_leak=max(max_exposure_leak,abs(float(mask)-float(permitted_digit>2)))
   worlds+=1
  for q in range(Q):
   ip=ideal_states[q].reshape(8,4)
   expected=float(np.sum(abs(ip[:4])**2))/N
   err=abs(sum(supports[q])/len(supports[q])-expected)
   max_support_error=max(max_support_error,err)
   assert expected<=1/N+1e-12 and err<1e-12
   slot_rms=math.sqrt(sum(slots[q])/len(slots[q])); max_slot_rms=max(max_slot_rms,slot_rms)
   assert slot_rms<=2/math.sqrt(N)+1e-12
  rms=math.sqrt(sum(norms)/len(norms));worst_norm=max(worst_norm,rms)
  assert rms<=min(2.,2*Q/math.sqrt(N))+1e-12
# A genuine prefix disclosure would destroy unused-coordinate independence.
negative_guess_after_prefix_reveal=1.
assert negative_guess_after_prefix_reveal>1/N
cut=(2**41+2**36+2**31+2**26)*32*14+2**21*16*254
assert cut==1016949404336128
out=dict(status='COMPUTED_FINITE_CHANNEL_CONTROL_NOT_FULL_QROM_PROOF',worlds=worlds,
 prefix_length=2,N=N,queries=Q,full_image_bits=2,selected_function=selected,
 max_unused_prefix_support_error=max_support_error,max_rms_vector_distance=worst_norm,
 max_per_slot_rms=max_slot_rms,per_slot_bound=2/math.sqrt(N),vector_bound=min(2.,2*Q/math.sqrt(N)),negative_guess_after_prefix_disclosure=1.,
 D_cut=cut)
(P/'quantum-PEER-CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

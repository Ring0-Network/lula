"""Finite exact controls for classical single-cut source coupling. No source crypto runs."""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
N=2
word=list(product(range(N),repeat=2))
functions=list(product(word,repeat=N))
source=Counter()
for u0,f0,f1 in product(range(N),functions,functions):
    u1=f0[u0][0]; y=f1[u1]
    source[(u0,f0,f1,u1,y)]+=1
latent=Counter()
for u0,x,l0,other,f1 in product(range(N),range(N),range(N),word,functions):
    f0=[None]*N
    f0[u0]=(x,l0);f0[1-u0]=other
    latent[(u0,tuple(f0),f1,x,f1[x])]+=1
assert source==latent
assert sum(source.values())==512
checks=[]
for exposure in range(3):
 for order in range(2):
  events=0; successes=[0,0]; prefix_stops=0; exposure_stops=0
  for (u0,f0,f1,u1,y),weight in source.items():
    xs=[u0,u1];fs=[f0,f1]; endpoint=y[0]
    # Atomic disclosure position depends only on public endpoint and policy.
    e=(endpoint+exposure)%3
    exposed=[e<=p for p in range(2)]
    first_reply=fs[order][endpoint]
    qs=[(order,endpoint),(1-order,1-endpoint),(1,first_reply[0]),(0,first_reply[1])]
    first=next((p for p,z in qs if not exposed[p] and z==xs[p]),None)
    events+=weight*(first is not None)
    for selected in range(2):
      # B does not know X at selected. It compares fullimage targets, never input equality.
      if e<=selected:
        exposure_stops+=weight;continue
      target=fs[selected][xs[selected]]
      for p,z in qs:
        if selected==1 and p==0 and z==u0:
          prefix_stops+=weight;break
        if p==selected and fs[p][z]==target:
          successes[selected]+=weight;break
  assert sum(successes)>=events
  checks.append(dict(exposure_policy=exposure,query_order=order,source_first_hidden=events,
                    success_sum=sum(successes),predecessor_stops=prefix_stops,
                    exposure_stops=exposure_stops,selector_loss=2))
# A naive nonaborting independent predecessor splice destroys the two-step relation.
naive_true=0; naive_total=0
for x,z,f1 in product(range(N),range(N),functions):
    naive_true+=f1[x][0]==f1[z][0];naive_total+=1
assert (naive_true,naive_total)==(48,64)
# Source chain endpoint law is identically f1(f0(u0)) and holds in every512 source worlds.
wots=480*(2**41+2**36+2**31+2**26)+4080*2**21
fors=(2**41)*17*512
assert wots==1089588072284160 and wots<2**50
assert fors==19140298416324608 and 2**54<wots+fors<2**55
sourcefile=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
assert hashlib.sha256(sourcefile.read_bytes()).hexdigest()=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
out=dict(status='COMPUTED_FINITE_CONTROL_NOT_FULL_SOURCE_PROOF',source_worlds=512,
         exact_joint_law_bijection=True,checks=checks,
         naive_wrong_splice_public_chain_relation=f'{naive_true}/{naive_total}',
         correct_source_public_chain_relation='512/512',wots_count=wots,wots_pad=2**50,
         fors_count=fors,combined_count=wots+fors,combined_pad=2**55,
         prep_max_public_hashes=254,source_sha256=hashlib.sha256(sourcefile.read_bytes()).hexdigest())
(P/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

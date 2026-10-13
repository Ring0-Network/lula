"""Independent exact first-accepted-row/full-reply controls. No source crypto runs."""
from itertools import product
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
accept=lambda y:(y//2) in (1,2) #2-bit prefix,1-bit retained lower limb.
words=range(8); accepted=[y for y in words if accept(y)]
rows=list(product(words,repeat=4))
fail=success=counteronly=afterbase=full_replaced_match=prefix_replaced_match=replaced_total=0
first=[0,0];changed_tests=changed_hits=0;bybase=[]
for C in range(2):
 sf=ss=0
 for table in rows:
  counters=[c for c in range(2) if accept(table[C*2+c])]
  afterbase+=any(accept(y) for y in table)
  if not counters:fail+=1;sf+=1;continue
  success+=1;ss+=1;c0=counters[0];y=table[C*2+c0];first[c0]+=1
  assert all(not accept(table[C*2+c]) for c in range(c0))
  assert accept(y) and table[C*2+c0]==y
  V=1-C
  for c in range(2):
   changed_tests+=1;changed_hits+=table[V*2+c]//2==y//2
   if c!=c0 and table[C*2+c]//2==y//2:counteronly+=1
  # Altering just target metadata with a fresh accepted word breaks source raw correlations.
  for yy in accepted:
   replaced_total+=1;full_replaced_match+=yy==y;prefix_replaced_match+=yy//2==y//2
 bybase.append(dict(base=C,success=ss,failure=sf))
assert (success,fail)==(6144,2048) and first==[4096,2048]
assert all(c['success']==3072 and c['failure']==1024 for c in bybase)
assert (changed_hits,changed_tests)==(3072,12288)
assert counteronly==1024 and afterbase==7680
assert full_replaced_match*4==replaced_total and prefix_replaced_match*2==replaced_total

def coefficient(w,ell,target):
 a=[1]
 for _ in range(ell):
  out=[0]*(min(target,len(a)-1+w-1)+1);window=0
  for s in range(len(out)):
   if s<len(a):window+=a[s]
   if s-w>=0 and s-w<len(a):window-=a[s-w]
   out[s]=window
  a=out
 return a[target]
low=coefficient(16,32,240);top=coefficient(256,16,2040)
assert low==5181241160064611531897369560287267312
assert top==454918678781617793203528879683071744
rows_actual=2**41+2**36+2**31+2**26+2**21
assert rows_actual==2269959421952 and 2**41<rows_actual<2**42
src=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
h=hashlib.sha256(src.read_bytes()).hexdigest()
assert h=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
out=dict(status='COMPUTED_FINITE_ROW_CONTROLS_NOT_SOURCE_SECURITY_PROOF',worlds=len(rows)*2,
         full_reply_bits=3,prefix_bits=2,counters=2,acceptance_density='1/2',
         successful=success,failure=fail,first_counter=first,per_base=bybase,
         changed_base_hits=changed_hits,changed_base_tests=changed_tests,changed_base_probability='1/4',
         counter_only_matches_excluded=counteronly,
         chronology_negative={'chosen_base_before_row':'6144/8192','base_chosen_after_row':'7680/8192'},
         resampled_target_negative={'full_raw_correlation':'1/4','prefix_digest_correlation':'1/2','correct_source_correlation':'1'},
         low_accepted_count=low,top_accepted_count=top,accepted_denominator=2**128,
         actual_row_count=rows_actual,selector_bits=42,prep_public_max=17392,prep_private_max=8704,
         source_sha256=h)
(P/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

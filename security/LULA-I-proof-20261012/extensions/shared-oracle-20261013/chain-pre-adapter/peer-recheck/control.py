import itertools, json, hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
N=2
images=list(itertools.product(range(N),repeat=2))
worlds=[]
for x0,x1,x2,r0,r1,other0,other1 in itertools.product(range(N),range(N),range(N),range(N),range(N),images,images):
    h0=[None]*N; h1=[None]*N
    h0[x0]=(x1,r0);h0[1-x0]=other0
    h1[x1]=(x2,r1);h1[1-x1]=other1
    worlds.append(((x0,x1,x2),(tuple(h0),tuple(h1))))
assert len(worlds)==512
assert len(set((x[0],h) for x,h in worlds))==512, 'ordinary ghost marginal is not bijective'
checks=[]
for policy in range(3):
 for query_order in range(2):
  hits=0; bsuccess=[0,0]; coupling_checks=0; predecessor_aborts=0; exposure_aborts=0
  for xs,hs in worlds:
    digit=(xs[2]+policy)%3 # metadata reads public endpoint only
    known=[p>=digit for p in range(2)]
    # Atomic response precedes these raw/final candidates. Digit2 keeps both hidden.
    candidates=[(query_order,xs[2]),(1-query_order,1-xs[2])]
    # Include two adaptive candidates reading the previous complete reply.
    last=hs[candidates[0][0]][candidates[0][1]]
    candidates += [(1,last[0]),(0,last[1])]
    first=None
    for j,(p,z) in enumerate(candidates):
      if not known[p] and z==xs[p]: first=(j,p);break
    hits+=first is not None
    for selected in range(2):
      if selected>=digit:
        # Candidate needs a selected coordinate hidden at first event; exposure is an abort.
        exposure_aborts+=1;continue
      stopped=False
      for j,(p,z) in enumerate(candidates):
        if p!=selected and not known[p] and z==xs[p]:
          predecessor_aborts+=int(selected==1 and p==0)
          stopped=True;break
        reply=hs[p][z]
        # selected secret itself is never read by the simulator test.
        target=hs[selected][xs[selected]]
        if p==selected and reply[0]==target[0]:
          assert hs[selected][z][0]==target[0]
          bsuccess[selected]+=1;stopped=True;break
        if first is not None and j<first[0]: coupling_checks+=1
      if first is not None and first[1]==selected:
        assert stopped, 'selected first hit was missed'
  # Uniform selector loss2: summing selected success must cover every source first-hit world.
  assert sum(bsuccess)>=hits
  checks.append(dict(policy=policy,query_order=query_order,worlds=len(worlds),source_first_hits=hits,
      selected_success_sum=sum(bsuccess),coupling_checks=coupling_checks,
      predecessor_aborts=predecessor_aborts,exposure_aborts=exposure_aborts))
# Countermodel to nonaborting unknown predecessor fabrication.
# For every hidden challenge input and independent fabricated prefix, relation holds only1/N.
relations=sum(z==x for x,z in itertools.product(range(N),repeat=2))
assert relations==N
wots=(2**41+2**36+2**31+2**26)*32*15+2**21*16*255
fors=2**41*17*512
count=wots+fors
assert 2**54<count<2**55
out=dict(status='COMPUTED_FINITE_CONTROLS_NOT_FULL_SOURCE_PROOF',ghost_worlds=512,
 ordinary_marginal_bijective=True,checks=checks,
 naive_predecessor_correct_probability='1/2',source_wots_protected=wots,
 source_fors_protected=fors,source_total_protected=count,fixed_selector_loss=2**55)
(P/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

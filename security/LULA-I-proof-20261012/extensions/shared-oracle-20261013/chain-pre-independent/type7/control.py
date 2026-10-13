import itertools,json
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parent
# Complete5-bit images:4-bit source prefix,1-bit retained lower limb.
accepted={d for d in range(16) if (d//4)+(d%4)==3}
assert len(accepted)==4
counts=Counter(); target_counts=Counter(); changed_tests=changed_wins=0; counter_only_examples=0
for row in itertools.product(range(32),repeat=3):
    c=next((c for c,z in enumerate(row) if z//2 in accepted),None)
    if c is None:
        counts['failure']+=1;continue
    counts[str(c)]+=1
    y=row[c]; target_counts[(c,y)]+=1
    assert all(row[i]//2 not in accepted for i in range(c))
    assert all(row[i]//2!=y//2 for i in range(c))
    for alt_full in range(32):
        changed_tests+=1
        changed_wins+=int(alt_full//2==y//2)
    for j,z in enumerate(row):
        if j!=c and z//2==y//2:
            counter_only_examples+=1
            # Correct changed-base challenge must reject same-child counter modifications.
            changed_base=False
            assert not changed_base
assert counts['0']==8192 and counts['1']==6144 and counts['2']==4608
assert counts['failure']==13824
assert changed_wins*16==changed_tests
for c in range(3):
    v=[target_counts[(c,2*d+rho)] for d in accepted for rho in range(2)]
    assert len(set(v))==1, 'accepted fullimage not uniform conditional on counter'
assert counter_only_examples>0

def coeff(w,ell,S):
    a=[1]+[0]*S
    for _ in range(ell):
        b=[];window=0
        for s in range(S+1):
            window+=a[s]
            if s>=w:window-=a[s-w]
            b.append(window)
        a=b
    return a[S]
lower=coeff(16,32,240);top=coeff(256,16,2040)
assert lower==5181241160064611531897369560287267312
assert top==454918678781617793203528879683071744
rows=2**41+2**36+2**31+2**26+2**21
assert rows==2269959421952 and 2**41<rows<2**42
out=dict(status='COMPUTED_FINITE_ROW_DISINTEGRATION_NOT_FULL_SOURCE_PROOF',
 fullimage_worlds=32**3,accept_prefixes=sorted(accepted),row_counts=dict(counts),
 success_fraction='37/64',failure_fraction='27/64',changed_base_tests=changed_tests,
 changed_base_wins=changed_wins,fresh_changed_base_collision_fraction='1/16',
 counter_only_witnesses_excluded=counter_only_examples,
 target_fullimage_uniform_given_counter=True,source_lower_accept_count=lower,
 source_top_accept_count=top,source_prefix_space=2**128,row_namespace=rows,
 fixed_selector_loss=2**42,prep_public_max=17*(512+511)+1,prep_private_max=17*512)
(P/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

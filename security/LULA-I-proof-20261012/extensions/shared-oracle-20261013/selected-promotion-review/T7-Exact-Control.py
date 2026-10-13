"""Exact finite full-limb first-accepted row law and source resource checks."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import hashlib,json
OUT=Path(__file__).resolve().parent

def slice_count(length,width,target):
    dp=[1]+[0]*target
    for _ in range(length):
        ndp=[0]*(target+1)
        window=0
        for s in range(target+1):
            window+=dp[s]
            if s>=width:window-=dp[s-width]
            ndp[s]=window
        dp=ndp
    return dp[target]

lower=slice_count(32,16,240)
top=slice_count(16,256,2040)
assert top==454918678781617793203528879683071744
assert 0<lower<2**128 and 0<top<2**128
N=4
images=list(product(range(N),range(2)))
cases=[]
for size in [1,2,3]:
    accepted=set(range(size))
    worlds=0; bottom=0; counters=Counter(); upper_targets=Counter(); lower_targets=Counter()
    successful=0; hits=0; early_rejected_cannot_match=0
    for row0,row1,other in product(images,repeat=3):
        worlds+=1
        row=(row0,row1)
        c=next((i for i in range(2) if row[i][0] in accepted),None)
        if c is None:
            bottom+=1
            continue
        successful+=1; counters[c]+=1
        target=row[c]
        upper_targets[target[0]]+=1; lower_targets[target[1]]+=1
        hits+=other[0]==target[0]
        for earlier in range(c):
            assert row[earlier][0] not in accepted
            assert row[earlier][0]!=target[0]
            early_rejected_cannot_match+=1
    assert worlds==512
    p=F(size,N)
    assert F(bottom,worlds)==(1-p)**2
    for c in range(2):assert F(counters[c],worlds)==(1-p)**c*p
    assert len(set(upper_targets.values()))==1
    assert lower_targets[0]==lower_targets[1]
    assert F(hits,successful)==F(1,N), 'fresh different-base target hit was incorrectly acceptance-normalized'
    cases.append({'accepted_size':size,'worlds':worlds,'success_worlds':successful,
                  'bottom_probability':str(F(bottom,worlds)),
                  'first_counter_probabilities':{str(c):str(F(counters[c],worlds)) for c in range(2)},
                  'fresh_different_base_prefix_hit_given_success':str(F(hits,successful)),
                  'canonical_lower_limb_counts':dict(lower_targets),
                  'rejected_points_checked':early_rejected_cannot_match})

rows_count=sum(2**e for e in [41,36,31,26,21])
assert rows_count==2269959421952 and 2**41<rows_count<2**42
assert 17*(512+511)+1==17392 and 17*512==8704
assert 32*(32*15+1)+31==15423 and 32*32==1024
resources=[]
for exp in [24,30,38,40,41,44,50,64]:
    q=2**exp
    resources.append({'q_exponent':exp,
     'hot_F_cap':min(19212937084272640,8704+2181038080+q*12816),
     'cold_F_cap':min(19212937084272640,8704+2181038080+q*33567232),
     'hot_honest_outside_plus_C':2**21*(19505+2**32)-1+q*(82090+5*2**32)+3224+17392,
     'cold_honest_outside_plus_C':2**21*(19505+2**32)-1+q*(8560574463+82090+6*2**32)+3224+17392})
out={'status':'PASS_EXACT_UNCONDITIONED_FULL_LIMB_ROW_AND_FRESH_DIFFERENT_BASE_CONTROLS',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'cases':cases,'source_slice_cardinalities':{'lower32x16sum240':str(lower),'top16x256sum2040':str(top)},
     'source_digest_space':str(2**128),'source_counter_cap':2**32,
     'WOTS_rows':rows_count,'selector_pad':2**42,
     'C_bottom_public':17392,'C_bottom_F':8704,'C_higher_public':15423,'C_higher_F':1024,
     'child_array_node_bytes_cap':17*1023*16,
     'q_resource_rows':resources,
     'challenge_preprocessing_calls_cap':2**32,
     'simulator_selected_queries':'Q_H+1 or Q_q coherent plus1 final classical, when canonical searches/rechecks use supplied target',
     'scope':'Finite sampler/count controls, not a complete source/challenger or conventional S-TCR proof.'}
(OUT/'T7-CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'worlds_per_case':512,'acceptance_cases':3,'q_rows':8,'WOTS_rows':rows_count}))

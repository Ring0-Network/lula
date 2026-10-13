"""Exact dependency and root-dependent residual-selection controls only."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

# Unconditional marginals31/32 do not license their product. An analysis union
# works even when two overlapping completion events are negatively correlated.
coins=list(range(32))
t=sum(c!=0 for c in coins)
a=sum(c!=1 for c in coins)
both=sum(c!=0 and c!=1 for c in coins)
pt,pa,pboth=F(t,32),F(a,32),F(both,32)
assert pt==pa==F(31,32)
assert pboth==F(15,16)<pt*pa
assert pboth==1-(1-pt)-(1-pa)

# Canonical pair(0,0), root r=H(0,0). Root-dependent row/orientation uses only
# r and an independent outside coin. Group by the full such Sigma record.
# Each group's residual single-mark probability must remain1/2.
groups={}
negative=[]
for table in product(range(2),repeat=4):
    def h(l,r): return table[2*l+r]
    root=h(0,0)
    for outside_coin in range(2):
        v=root^outside_coin
        direction=outside_coin
        vals=[h(v,x) if direction==0 else h(x,v) for x in range(2)]
        marks=sum(y==root for y in vals)
        key=(root,outside_coin,direction,v)
        bucket=groups.setdefault(key,[0,0])
        bucket[0]+=1
        bucket[1]+=(marks==1)
    # Disallowed residual-informed selection: inspect the two complete rows,
    # choose one maximizing target matches. The selected row law is biased.
    row_counts=[sum(h(l,x)==root for x in range(2)) for l in range(2)]
    negative.append(max(row_counts)==1)
assert len(groups)==4
for total,one in groups.values():
    assert F(one,total)==F(1,2)
negative_p=F(sum(negative),len(negative))
assert negative_p==F(3,8)!=F(1,2)

# Correct final lower-bound bookkeeping uses the joint probability first and a
# uniform conditional search bound second.
assert F(15,16)*F(1,3)*F(16,25)==F(1,5)
result={
    'status':'PASS_EXACT_DEPENDENCY_AND_ROOT_RESIDUAL_CONTROLS',
    'completion_marginals':str(pt),
    'completion_product':str(pt*pa),
    'actual_joint_and_union_bound':str(pboth),
    'product_shortcut_refuted':True,
    'root_table_worlds':16,
    'root_dependent_sigma_groups':len(groups),
    'each_sigma_single_mark_probability':'1/2',
    'residual_informed_selector_single_mark_probability':str(negative_p),
    'success_constant_from_safe_joint_bound':'1/5',
    'scope':'Finite dependency/framing controls, not an actual source forgery',
}
Path(__file__).with_name('JOINT-CHECKS.json').write_text(
    json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

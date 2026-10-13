"""Tiny exact conditional-row, full-image mixture and coherent oracle controls."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

M, FULL, C = 4, 8, 2
T = {1, 2}
lam = F(1, M)
groups = defaultdict(list)
for values in product(range(FULL), repeat=3):
    j = next((i for i in range(C) if values[i]//2 in T), None)
    sigma = (j, values[j], values[:j]) if j is not None else (None, None, values[:C])
    groups[sigma].append(values)
    # Exact sampler mass for the two same-child full images plus other-child image.
    weight = ((F(1,2)**j*F(1,2))/4/4**j/FULL**(C-j-1)/FULL
              if j is not None else F(1,2)**C/4**C/FULL)
    assert weight == F(1,FULL**3)

conditional_joint_checks = 0
for (j, canonical, earlier), tables in groups.items():
    if j is None:
        assert all(v[0]//2 not in T and v[1]//2 not in T for v in tables)
        eligible = (2,)  # Uniform other-child image; target is undefined.
    else:
        eligible = tuple(range(j+1,C))+(2,)
        target = canonical//2
        assert all(v[i]//2 != target for v in tables for i in range(j))
    counts = Counter(tuple(v[i] for i in eligible) for v in tables)
    assert len(counts) == FULL**len(eligible)
    assert all(F(n,len(tables)) == F(1,FULL**len(eligible)) for n in counts.values())
    conditional_joint_checks += 1

def row_pairs(y):
    return list(product([v for v in range(FULL) if v//2 != y],
                        [v for v in range(FULL) if v//2 == y]))

for target in T:
    mix = Counter()
    pairs = row_pairs(target)
    for v0,v1 in pairs:
        mix[v0] += (1-lam)/len(pairs)
        mix[v1] += lam/len(pairs)
    assert len(mix) == FULL
    assert all(p == F(1,FULL) for p in mix.values())

def fanout(y, delta, pivot):
    return y ^ (delta ^ (1<<pivot)) if (y>>pivot)&1 else y

def swap(y, a, pivot):
    different = ((y>>pivot)&1)^a
    return y^(different<<pivot), a^different

def run(x,y,a,marks,v0,v1,mask):
    y ^= v0[x]
    if mask[x]:
        delta = v0[x]^v1[x]
        assert delta
        pivot = (delta & -delta).bit_length()-1
        y = fanout(y,delta,pivot)
        y,a = swap(y,a,pivot)
    a ^= marks[x]  # ONE common Boolean XOR query.
    if mask[x]:
        y,a = swap(y,a,pivot)
        y = fanout(y,delta,pivot)
    return x,y,a

plus_checks = raw_terms = worlds = 0
for state in (0,1,None):
    mask = (False,state==0,state is not None,False)
    varying = [i for i in range(4) if mask[i]]
    base = [2,0,5,7] if state==0 else [0,2,5,7] if state==1 else [0,6,5,7]
    for choices in product(row_pairs(1),repeat=len(varying)):
        v0, v1 = base.copy(),base.copy()
        for i,pair in zip(varying,choices):
            v0[i],v1[i] = pair
        worlds += 1
        for marks in product(range(2),repeat=4):
            for x,y in product(range(4),range(FULL)):
                actual = Counter(run(x,y,a,marks,v0,v1,mask) for a in (0,1))
                value = v1[x] if mask[x] and marks[x] else v0[x]
                expected = Counter((x,y^value,a) for a in (0,1))
                assert actual == expected
                plus_checks += 1
                raw_terms += 2

# Negative wrong-conditioning control: an earlier counter is not iid uniform.
first_at_one = [v for v in product(range(FULL),repeat=2)
                if v[0]//2 not in T and v[1]//2 in T]
actual_earlier_accepted = F(sum(v[0]//2 in T for v in first_at_one),len(first_at_one))
assert actual_earlier_accepted == 0
wrong_unconditioned_accepted = F(len(T),M)
assert wrong_unconditioned_accepted == F(1,2)

result = {
    "status":"PASS_EXACT_QUANTUM_CANONICAL_ROW_CONTROLS",
    "model":{"prefix_bits":2,"full_image_bits":3,"distinct_counters":C,
             "acceptance_prefixes":sorted(T),"mark_density":str(lam)},
    "original_full_tables_checked":FULL**3,
    "conditional_joint_residual_groups_checked":conditional_joint_checks,
    "full_image_mixture_uniform":True,
    "success_at_zero_success_at_one_and_failed_masks_checked":True,
    "value_pair_worlds":worlds,"plus_basis_vectors_checked":plus_checks,
    "raw_basis_terms_checked":raw_terms,
    "one_boolean_query_and_clean_plus_ancilla":True,
    "negative_wrong_earlier_iid_rule":{"actual_accepted":"0","wrong_accepted":"1/2"},
    "one_query_scoped_bound":"min(1,8*(Q+6)^2/2^128) for fixed nonzero S",
    "two_query_fallback":"min(1,8*(2*(Q+5)+1)^2/2^128)",
    "event":"observable noncanonical accepted-target hit in finaltype7trace",
    "full_QROM_security":None,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_name("CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

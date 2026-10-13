"""Exact small table/online patch controls, not a quantum signature benchmark."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json

# Two buckets, two real trees, binary indices and a binary omitted digit.
B,t,k,q = 2,2,2,2
exposures = list(product(range(B),*(range(t) for _ in range(k))))
digest_values = list(product(range(t),range(B),*(range(t) for _ in range(k))))
probabilities = []
for dataset in product(exposures,repeat=q):
    covered = defaultdict(set)
    for bucket,*indices in dataset:
        for j,index in enumerate(indices):
            covered[(bucket,j)].add(index)
    good = sum(z==0 and all(index in covered[(bucket,j)] for j,index in enumerate(indices))
               for z,bucket,*indices in digest_values)
    probabilities.append(F(good,len(digest_values)))
mean_coverage = sum(probabilities,F(0))/len(probabilities)
occupancy = F(1,t)*sum(F(comb(q,n),B**q)*(B-1)**(q-n)*(1-F(t-1,t)**n)**k
                       for n in range(q+1))
assert mean_coverage == occupancy == F(17,128)

# Independent inner bad-output set: low half equalsS or one of three Ui values.
N,S,Ulist = 4,1,[0,5,15]
bad = {u for u in range(N*N) if u%N==S}|set(Ulist)
inner_density = F(len(bad),N*N)
assert inner_density == F(3,8) <= F(1,N)+F(len(Ulist),N*N)
mixture = Counter()
pairs = list(product([u for u in range(N*N) if u not in bad],sorted(bad)))
for v0,v1 in pairs:
    mixture[v0] += (1-inner_density)/len(pairs)
    mixture[v1] += inner_density/len(pairs)
assert len(mixture)==N*N and all(p==F(1,N*N) for p in mixture.values())

# Coherent current-patch simulation where the assignment label depends on B0.
# A prior response at x0 reveals its mark through the known coverage predicate.
# The online server then chooses patchx1 on B0=0 and patchx2 on B0=1.
pair_options = list(product(range(2,8),range(2)))
lam = F(1,4)
def fanout(v,delta,pivot):
    return v^(delta^(1<<pivot)) if (v>>pivot)&1 else v
def swap(v,a,pivot):
    d=((v>>pivot)&1)^a
    return v^(d<<pivot),a^d

checks = worlds = raw_terms = 0
label_mass = Counter()
label_bit_mass = Counter()
for marks in product(range(2),repeat=4):
    weight = F(1)
    for bit in marks:
        weight *= lam if bit else 1-lam
    label=1 if marks[0]==0 else 2
    label_mass[label] += weight
    label_bit_mass[(label,marks[0])] += weight
    for choices in product(pair_options,repeat=3):
        v0=[c[0] for c in choices]+[6]
        v1=[c[1] for c in choices]+[6]
        worlds += 1
        for x,y in product(range(4),range(8)):
            a0,a1 = (1,1) if x==label else (v0[x],v1[x])
            actual = Counter()
            for work in (0,1):
                out = y^a0
                delta=a0^a1
                if delta:
                    pivot=(delta & -delta).bit_length()-1
                    out=fanout(out,delta,pivot)
                    out,work=swap(out,work,pivot)
                work ^= marks[x]  # ONE standard B query atx.
                if delta:
                    out,work=swap(out,work,pivot)
                    out=fanout(out,delta,pivot)
                actual[(x,out,work)] += 1
            value = 1 if x==label else v1[x] if marks[x] else v0[x]
            expected = Counter((x,y^value,work) for work in (0,1))
            assert actual == expected
            checks += 1
            raw_terms += 2
assert F(label_bit_mass[(2,1)],label_mass[2])==1
assert label_mass[2]==lam

# Actual-byte I/E alias if the assigned namespace lower half isS.
s=bytes(range(1,17)); r=bytes(16); ui=r+s; c=bytes((1,2,3,4))
root=c+s[:12]; message=s[12:]
inner=r+s+root+message
outer=ui+c+s
assert len(inner)==len(outer)==52 and inner==outer
assert ui[16:32]==s

result={
    "status":"PASS_EXACT_COVERAGE_SEARCH_FACTOR_AND_ONLINE_PATCH_CONTROLS",
    "coverage_datasets":len(probabilities),"mean_raw_coverage":str(mean_coverage),
    "occupancy_formula":str(occupancy),"inner_exact_density":str(inner_density),
    "inner_union_density_cap":str(F(1,N)+F(len(Ulist),N*N)),
    "inner_full_value_mixture_uniform":True,
    "online_challenge_dependent_patch_worlds":worlds,
    "plus_basis_vectors_checked":checks,"raw_basis_terms_checked":raw_terms,
    "patch_labels_generated_as_state_not_independent_advice":True,
    "negative_fixed_label_condition":{"Pr_B0_1_given_patch2":"1","unconditional_Pr_B0_1":"1/4"},
    "negative_unguarded_inner_outer_alias":{"exact_byte_equality":True,"bytes":52,"requires_Ui_lower_equal_S":True},
    "outer_bound":"min(1,8*(Q+2)^2*E[p(Tq)]) under exogenous-template premise",
    "inner_bound":"min(1,8*(Q+2)^2*(1/N+q/N^2)) with fresh unpatched finalI",
    "source_bridge_reviewed_here":False,"full_QROM_security":None,
}
Path(__file__).with_name("CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

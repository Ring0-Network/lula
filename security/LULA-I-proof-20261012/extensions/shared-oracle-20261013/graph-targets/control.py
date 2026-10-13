"""Exact tiny DAG/residual controls; no source signing, cache build or timings."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
src=ROOT/'publications/LULA-I/release/code/lula1/src/lib.rs'
pin='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert hashlib.sha256(src.read_bytes()).hexdigest()==pin

# One target per independent domain; X1 depends on predecessor image Y0.
# Full graph exposure is conditioned explicitly. Domain 0 has two inputs,
# domain 1 three; images have two values. Outside input X0 is independent.
groups=defaultdict(list)
after_first=defaultdict(list)
for x0 in range(2):
    for f0 in product(range(2),repeat=2):
        for f1 in product(range(2),repeat=3):
            y0=f0[x0]; x1=y0; y1=f1[x1]
            G=(x0,y0,x1,y1)
            v0=f0[1-x0]  # Fresh non-designated domain-0 query.
            p1=2 if v0==0 else 1-x1  # Adaptive fresh non-target point.
            assert p1!=x1
            hit0=v0==y0; hit1=f1[p1]==y1
            groups[G].append((hit0,hit1))
            after_first[(G,v0)].append(hit1)
assert all(Fraction(sum(v),len(v))==Fraction(1,2) for v in after_first.values())
assert all(Fraction(sum(a or b for a,b in v),len(v))==Fraction(3,4) for v in groups.values())

# One target alone is insufficient if its input reads its own restriction.
self_hits=[]
for f in product(range(2),repeat=3):
    x=next(i for i in range(3) if f[i]==f[(i+1)%3])
    fresh=(x+1)%3
    assert fresh!=x
    self_hits.append(f[fresh]==f[x])
assert all(self_hits)

# Symbolic actual-source domain inventory; never materialize the full graph.
heights=[5,5,5,5,21]
keys=[1<<sum(heights[i:]) for i in range(5)]
widths=[16,16,16,16,256]
chains=[32,32,32,32,16]
trees=[1<<sum(heights[i+1:]) for i in range(5)]
domains={
 'type0_chain_coordinates':sum(k*l*(w-1) for k,l,w in zip(keys,chains,widths)),
 'type1_wots_endpoint_compressions':sum(keys),
 'type2_hypertree_internal_nodes':sum(t*((1<<h)-1) for t,h in zip(trees,heights)),
 'type3_fors_leaves_and_internal_nodes':(1<<41)*17*((1<<10)-1),
 'type4_fors_root_compressions':1<<41,
}
selected_work=17*(1+9)+1+4*(240+1+5)+(2040+1+21)
assert selected_work==3217
out={
 'status':'PASS_FINITE_DAG_AND_COUNTEREXAMPLE_CONTROLS_NOT_FULL_SECURITY',
 'source_sha256':pin,'toy_worlds':sum(map(len,groups.values())),
 'toy_complete_graph_groups':len(groups),
 'fresh_second_query_hit_probability_each_graph_and_previous_reply':'1/2',
 'two_fresh_query_hit_probability_each_exposed_graph':'3/4',
 'self_dependent_target_one_query_hit_probability':'1',
 'naive_one_query_bound_without_DAG_hypothesis':'1/2',
 'self_dependent_target_counterexamples':len(self_hits),
 'actual_symbolic_selected_domain_counts':domains,
 'actual_symbolic_total_selected_domains':sum(domains.values()),
 'final_verifier_selected_domain_calls_max':selected_work,
 'final_verifier_full_hash_calls_valid':selected_work+5+2,
 'target_hash_domain_types':[0,1,2,3,4],
 'excluded_types':[5,6,7],
 'scope':'Exhaustive tiny random-function models and source arithmetic only; no source/manscript/proof-packet mutations, signature generation or source uploads.'
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

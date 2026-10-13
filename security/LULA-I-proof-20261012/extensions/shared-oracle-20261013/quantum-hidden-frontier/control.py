"""Small exact hidden-ghost controls; not a source or quantum-security proof."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

M, FULL, LEAVES = 2, 4, 2
tables = list(product(range(FULL),repeat=M*LEAVES))
real_marginal = Counter()
unused = defaultdict(Counter)
worlds = permutation_checks = 0
finder = Counter()
finder_total = Counter()
for g in tables:
    for z in product(range(M),repeat=LEAVES):
        for w in product(range(FULL),repeat=LEAVES):
            worlds += 1
            h = list(g)
            for i in range(LEAVES):
                h[i*M+z[i]] = w[i]
            real_marginal[(z,tuple(h))] += 1
            for mask in range(1<<LEAVES):
                for point in range(M*LEAVES):
                    i,x = divmod(point,M)
                    real = h[point]
                    ghost = w[i] if mask&(1<<i) and x==z[i] else g[point]
                    finder_total[(mask,point)] += 1
                    finder[(mask,point)] += real != ghost
                    if mask&(1<<i):
                        assert real == ghost
                    for y in range(FULL):
                        assert (y^real)^real == y
                        assert (y^ghost)^ghost == y
                        permutation_checks += 2
            # Adaptive classical disclosure from the ghost's public history.
            v = g[0]  # R empty: no hidden secret is consulted.
            j = v%LEAVES
            disclosed = z[j]
            remaining = 1-j
            response = g[remaining*M+disclosed]
            history = (v,j,disclosed,response)
            unused[history][z[remaining]] += 1

assert len(real_marginal) == M**LEAVES*FULL**(M*LEAVES)
assert len(set(real_marginal.values())) == 1
assert all(set(c)==set(range(M)) and len(set(c.values()))==1 for c in unused.values())
for key,total in finder_total.items():
    mask,point = key
    i,_ = divmod(point,M)
    want = F(0) if mask&(1<<i) else F(1,M)*(1-F(1,FULL))
    assert F(finder[key],total) == want
    assert want <= F(1,M)

# Prefix comparison at a revealed point without reconciliation: exact failure.
PREFIX, IMAGE = 4, 8
hit = sum(g//2==w//2 for g,w in product(range(IMAGE),repeat=2))
stale_match = F(hit,IMAGE**2)
assert stale_match == F(1,PREFIX)
reconciled_match = F(1)

# A WOTS suffix has the same failure one step AFTER a reconciled emitted node.
# Step1 returns C2; step2 remains stale. Its prefix equals endpointC3 only1/4.
suffix_match = F(sum(g//2==end for g,end in product(range(IMAGE),range(PREFIX))),
                 IMAGE*PREFIX)
assert suffix_match == F(1,PREFIX)

result = {
    "status":"PASS_EXACT_DYNAMIC_FORS_GHOST_AND_DISCLOSURE_CONTROLS",
    "model":{"secret_alphabet":M,"full_images":FULL,"leaf_domains":LEAVES},
    "worlds":worlds,"permutation_involution_basis_checks":permutation_checks,
    "real_programmed_table_marginal_uniform":True,
    "adaptive_classical_disclosure_histories":len(unused),
    "remaining_secret_conditionally_uniform":True,
    "undisclosed_finder_mass":"3/8 <= 1/2",
    "disclosed_finder_mass":"0",
    "static_unreconciled_prefix_control":{"prefix_alphabet":PREFIX,
        "real_match":"1","ghost_match":str(stale_match),"gap":str(1-stale_match)},
    "reconciled_disclosure_match":str(reconciled_match),
    "wots_signed_node_only_control":{"queries":2,"real_endpoint_match":"1",
        "ghost_endpoint_match":str(suffix_match),"gap":str(1-suffix_match)},
    "general_quantum_unused_variable_invariant":"manual proof, not established by finite classical controls alone",
    "dynamic_source_bound":"proposed (2*(Q+17)+sqrt(17))^2/2^128, needs second-reader source/game review",
    "full_QROM_security":None,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_name("CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

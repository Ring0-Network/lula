"""Independent exact nonce/row-interface controls, not source signatures."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import cmath, math, random, json

# Global message-labelled inner programming preserves the ordinary function
# marginal conditional on each nonce assignment, including repeated nonces.
nonce_worlds=0
for r in product(range(2),repeat=2):
    law=Counter()
    for u in product(range(4),repeat=2):
        for residual in product(range(4),repeat=4):
            table=list(residual)
            for m in range(2): table[2*m+r[m]]=u[m]
            law[tuple(table)]+=1
            nonce_worlds+=1
    assert len(law)==4**4 and set(law.values())=={16}

# One clean row query on a genuinely entangled complex input, for every two-row
# two-slot full two-bit function. Outside-table branches are also exercised.
rng=random.Random(202610130063)
labels=list(product(range(2),range(2),range(4),range(2),range(2)))
psi={k:complex(rng.gauss(0,1),rng.gauss(0,1)) for k in labels}
norm=math.sqrt(sum(abs(v)**2 for v in psi.values()))
psi={k:v/norm for k,v in psi.items()}
def swap(z,aux,c):
    selected=(aux>>(2*c))&3
    return selected,(aux&~(3<<(2*c)))|(z<<(2*c))
row_cases=0
for row0,row1 in product(range(16),repeat=2):
    got={}
    expected={}
    rows=(row0,row1)
    for (u,c,z,eligible,anc),amp in psi.items():
        image=((rows[u]>>(2*c))&3) if eligible else ((u+2*c+1)&3)
        for aux in range(16):
            zz,work=swap(z,aux,c) if eligible else (z,aux)
            work ^= rows[u if eligible else 0]  # exactly ONE ROW XOR call
            zz,work=swap(zz,work,c) if eligible else (zz,work)
            if not eligible: zz ^= ((u+2*c+1)&3)  # known nuisance function
            key=(u,c,zz,eligible,anc,work)
            got[key]=got.get(key,0j)+amp/4
            want=(u,c,z^image,eligible,anc,aux)
            expected[want]=expected.get(want,0j)+amp/4
    assert got.keys()==expected.keys()
    assert max(abs(got[k]-expected[k]) for k in got)<1e-12
    row_cases+=1

# A source E point can literally be another nonce I point if the half guard
# is absent. This is a syntactic counterexample, not a real-source attack.
seed=bytes([0x31])*16
counter=0
root=counter.to_bytes(4,'big')+seed[:12]
other_message=seed[12:]
other_nonce=bytes([0x52])*16
u=other_nonce+seed
outer=u+counter.to_bytes(4,'big')+seed
inner=other_nonce+seed+root+other_message
assert outer==inner and len(outer)==52
assert u[16:]==seed  # guard stops BEFORE consulting this point

# Two new labels collide in their namespace. Reprogramming reads a new row
# and updates the cache by U, rather than retaining an obsolete per-label row.
cached={}
assigned={}
templates=[(0,1),(6,1)]
preceding=[]
qreads=0
for m in (0,1):
    preceding.append(qreads)
    assigned[m]=1
    fresh=templates[m]
    qreads+=1  # POST-instruction whole-row read, fresh value not returned
    cached[1]=fresh
def first_x(row):
    return next(v>>1 for v in row if (v&1)==0)
assert first_x(cached[assigned[0]])==3
assert first_x(templates[0])==0  # stale per-label cache would disagree
assert preceding==[0,1] and qreads==2

out={
 'status':'PASS_EXACT_SOURCE_ROW_CONTROLS_ONLY',
 'nonce_programming_worlds':nonce_worlds,
 'ordinary_inner_marginal_for_every_nonce_assignment':True,
 'complex_entangled_row_functions_checked':row_cases,
 'row_queries_per_raw_query':1,
 'plus_ancillas_exactly_clean':True,
 'guardless_outer_inner_alias_bytes':len(outer),
 'post_instruction_read_counts_before_instructions':preceding,
 'repeat_old_label_uses_latest_namespace_tuple':3,
 'stale_old_label_tuple_negative_control':0,
 'scope':'Exact finite marginal/circuit/controller controls; no source signing, timings or full QROM result'
}
Path(__file__).with_name('CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

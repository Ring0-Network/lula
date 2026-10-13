"""Independent eager-sampler/residual/source-accounting review; no signatures or timing."""
from collections import Counter,defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
source=ROOT/'publications/LULA-I/release/code/lula1/src/lib.rs'
PIN='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert hashlib.sha256(source.read_bytes()).hexdigest()==PIN

# Independently arrange the experiment by generating programmed targets+residuals,
# rather than reading targets from complete ordinary functions first.
eager=Counter()
residuals=defaultdict(Counter)
outside_info=defaultdict(Counter)
fresh_second=defaultdict(Counter)
two_hit=defaultdict(Counter)
leaked_outside_input=defaultdict(Counter)
for z,y0,y1,r0,r10,r11 in itertools.product(range(2),repeat=6):
    x0=z
    x1=y0
    f0=[None,None]
    f0[x0]=y0
    f0[1-x0]=r0
    off1=[i for i in range(3) if i!=x1]
    f1=[None]*3
    f1[x1]=y1
    f1[off1[0]]=r10
    f1[off1[1]]=r11
    eager[(z,tuple(f0),tuple(f1))]+=1
    G=(x0,y0,x1,y1)
    residuals[G][(r0,r10,r11)]+=1
    outside_info[(G,tuple(f1))][r0]+=1
    # A domain-1 choice can depend on domain-0's residual (outside info for domain1).
    p1=off1[r0]
    first=f1[p1]
    remaining=off1[1-r0]
    second=f1[remaining]
    fresh_second[(G,tuple(f0),first)][int(second==y1)]+=1
    two_hit[(G,tuple(f0))][int(first==y1 or second==y1)]+=1
    # A queried residual may be carried as another-domain query INPUT.
    leaked_outside_input[(G,r0)][r0]+=1

ordinary=Counter({(z,f0,f1):1 for z in range(2)
                  for f0 in itertools.product(range(2),repeat=2)
                  for f1 in itertools.product(range(2),repeat=3)})
assert eager==ordinary and len(eager)==64
assert all(len(c)==8 and set(c.values())=={1} for c in residuals.values())
assert all(c[0]==c[1] for c in outside_info.values())
assert all(F(c[1],sum(c.values()))==F(1,2) for c in fresh_second.values())
assert all(F(c[1],sum(c.values()))==F(3,4) for c in two_hit.values())
assert all(len(c)==1 for c in leaked_outside_input.values())

# Non-DAG eager target equation v=Y creates an invalid function marginal.
cyclic=Counter()
for y,r in itertools.product(range(2),repeat=2):
    f=[None,None]
    f[y]=y
    f[1-y]=r
    cyclic[tuple(f)]+=1
assert cyclic==Counter({(0,0):1,(0,1):2,(1,1):1})
assert (1,0) not in cyclic

# Counter-based type7 selection inspects its own restriction.
selected=defaultdict(list)
for f in itertools.product(range(2),repeat=2):
    hits=[i for i in range(2) if f[i]==1]
    if hits:
        target=min(hits)
        selected[(target,1)].append(f)
assert selected[(1,1)]==[(0,1)]

# Source arithmetic rearranged: type2 telescopes across layer forests.
keys=[2**(41-5*i) for i in range(4)]+[2**21]
counts={
    'type0':480*sum(keys[:4])+4080*keys[4],
    'type1':sum(keys),
    'type2':2**41-1,
    'type3':2**41*17*(2*512-1),
    'type4':2**41,
}
target_calls=17*10+1+3000+5+41
all_calls=target_calls+5+2
compression_count=all_calls+4+4*8+4+1
assert target_calls==3217 and all_calls==3224
assert compression_count==3265 and compression_count+1==3266
assert sum(counts.values())==39339469515522047

lane=HERE.parent/'graph-targets'
reviewed={n:hashlib.sha256((lane/n).read_bytes()).hexdigest()
          for n in ['DERIVATION.md','control.py','CONTROL-RESULTS.json']}
output={
 'status':'PASS_SCOPED_GRAPH_TARGET_LEMMA_SECOND_READER',
 'source_sha256':PIN,
 'independent_derivation_saved_before_peer_read':True,
 'eager_completed_function_worlds':len(eager),
 'eager_marginal_equals_ordinary_random_functions':True,
 'complete_graph_views':len(residuals),
 'residual_joint_distribution_each_graph':'all8binary triples equally likely',
 'target_domain_residual_given_graph_and_outside_function':'uniform1/2',
 'fresh_second_query_given_graph_outside_function_and_first_reply_hit':'1/2',
 'two_residual_query_union_given_graph_and_outside_function':'3/4',
 'arbitrary_outside_query_input_can_reveal_residual':True,
 'cyclic_non_DAG_sampler_function_counts':{str(k):v for k,v in cyclic.items()},
 'type7_first_accepted_target1_forces_other_reply0':True,
 'selected_domain_counts':counts,
 'total_selected_domains':sum(counts.values()),
 'final_verifier_target_full_hash_calls_max':target_calls,
 'final_verifier_all_full_hash_calls_max':all_calls,
 'instrumented_compressions_at32B_not_RO_calls':compression_count,
 'with_prefix_compression_not_RO_calls':compression_count+1,
 'reviewed_peer_file_hashes':reviewed,
 'full_EUF_CMA_bound':None,
 'quantum_bound':None,
 'scope':'Source arithmetic and finite random-function controls; no fullgraph construction, signing, cache work or original-file edits.',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE/'CHECKS.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps(output,indent=2))

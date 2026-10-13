"""Exact abstract message-hash interface controls; no SHA/source attack."""
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
def bits(d,start,length):
    return (int.from_bytes(d,'big') >> (256-start-length)) & ((1<<length)-1)
def digest(R,M,c):
    # All real indices and forced coordinate0, exact source41-bit route slots.
    I=2*R+(M if c==0 else 1-M)
    return (I << (256-203)).to_bytes(32,'big')
def mapped(R,M,c):
    d=digest(R,M,c)
    assert bits(d,153,9)==0
    route=bits(d,162,41)
    assert route==2*R+(M if c==0 else 1-M)
    assert (route>>5,route&31)==(0,route)
    return frozenset((route,j,bits(d,9*j,9)) for j in range(17))

canonical_fresh_pair_tests=canonical_hits=free_counter_hits=0
for R,M in product(range(4),range(2)):
    target=mapped(R,M,0)
    for R2,M2 in product(range(4),range(2)):
        if (R2,M2)==(R,M):continue
        canonical_fresh_pair_tests+=1
        canonical_hits+=int(mapped(R2,M2,0)<=target)
    free_counter_hits+=int(mapped(R,1-M,1)<=target)
assert canonical_fresh_pair_tests==56 and canonical_hits==0 and free_counter_hits==8

# Complete ideal-J functions vs first-label fresh-key-oracle caching.
request_order=(0,1,0,1,0)
nonce_laws=0
for values in product(range(4),repeat=2):
    source=[values[m] for m in request_order]
    cache={}; target_queries=0; replies=[]
    for m in request_order:
        if m not in cache:
            cache[m]=values[target_queries]
            target_queries+=1
        replies.append(cache[m])
    assert replies==source and target_queries==2
    nonce_laws+=1
assert nonce_laws==16

# Choosing a counter before the random key does not reproduce key-dependentfirstaccept.
fixed_counter_accepts=[sum(int(c==(R&1)) for R in range(4)) for c in range(2)]
assert fixed_counter_accepts==[2,2]
canonical_after_nonce_accepts=sum(int((R&1)==(R&1)) for R in range(4))
assert canonical_after_nonce_accepts==4

# Injective logical tags are decoded away, never prepended to source hash words.
def encode(S,T,M):return b'CTX'+S+T+len(M).to_bytes(4,'big')+M
def decode(x):
    assert x[:3]==b'CTX' and len(x)>=39
    S,T=x[3:19],x[19:35]
    size=int.from_bytes(x[35:39],'big')
    assert len(x)==39+size
    return S,T,x[39:]
context_cases=0
for s,t,M in product((0,1),(0,3),(b'',b'a',b'a\x00')):
    S=bytes([s])*16;T=bytes([t])*16;R=bytes([2])*16
    x=encode(S,T,M)
    S2,T2,M2=decode(x)
    assert (S2,T2,M2)==(S,T,M)
    assert R+S2+T2+M2==R+S+T+M
    assert (R+S2+T2+M2)!=(R+x)
    context_cases+=1

result={
    'scope':'Abstract exact interface controls only; no actual h/source signature run',
    'canonical_ITSR_fresh_pair_tests':canonical_fresh_pair_tests,
    'canonical_ITSR_hits':canonical_hits,
    'arbitrary_accepted_counter_coverage_hits':free_counter_hits,
    'arbitrary_accepted_counter_target_worlds':8,
    'source17real_FORS_zero9_and41route_byte_map_checked':True,
    'complete_memoized_nonce_functions_checked':nonce_laws,
    'target_query_count_for5_requests':2,
    'pre_nonce_fixed_counter_accepts_of4':fixed_counter_accepts,
    'post_nonce_canonical_accepts_of4':canonical_after_nonce_accepts,
    'logical_context_parse_preserves_actual_inner_bytes':True,
    'context_cases':context_cases,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

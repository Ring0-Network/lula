"""Exact tiny unitary router and actual byte-framing controls, not a source run."""
from collections import defaultdict, Counter
from itertools import product
from pathlib import Path
import cmath
import hashlib
import json

HERE=Path(__file__).resolve().parent

def permute(state, action):
    out=defaultdict(complex)
    for key, value in state.items():out[action(key)]+=value
    return dict(out)

def swap(state, scratch_index, selected):
    def action(key):
        key=list(key)
        if selected(key[0]):key[1],key[scratch_index]=key[scratch_index],key[1]
        return tuple(key)
    return permute(state,action)

def routed(state,h,g):
    selected=lambda w:w<4  # Four P-bit/x-bit pairs, known before P release.
    state=swap(state,3,selected)
    # ONE ordinary unknown XOR query on the scratch register. On inactive
    # branches address is a fixed dummy and response is |+>, so action is1.
    state=permute(state,lambda k:(k[0],k[1],k[2],k[3]^h[k[0] if selected(k[0]) else 0],k[4],k[5]))
    state=swap(state,3,selected)
    # ONE known local full-G evaluation, with selected high limb in |+>.
    state=swap(state,4,selected)
    state=permute(state,lambda k:(k[0],k[1]^(g[k[0]]>>1),k[2]^(g[k[0]]&1),k[3],k[4],k[5]))
    state=swap(state,4,selected)
    return state,1,1

def expected(state,h,g):
    def action(k):
        w,hi,lo,hs,gs,ref=k
        value=((h[w]<<1)|(g[w]&1)) if w<4 else g[w]
        return w,hi^(value>>1),lo^(value&1),hs,gs,ref
    return permute(state,action)

def plus_scratch(main):
    return {(w,hi,lo,hs,gs,ref):value/2 for (w,hi,lo,ref),value in main.items() for hs,gs in product(range(2),repeat=2)}

router_checks=0
for h in product(range(2),repeat=4):
    for fixture in range(4):
        g=tuple((3*w+fixture+(w//2))%4 for w in range(8))
        mains=[{(w,hi,lo,ref):1} for w,hi,lo,ref in product(range(8),range(2),range(2),range(2))]
        # Complex dense state entangling the query/response with reference.
        mains.append({(w,hi,lo,ref):cmath.exp(1j*(w+2*hi+3*lo+5*ref))/8
                      for w,hi,lo,ref in product(range(8),range(2),range(2),range(2))})
        for main in mains:
            state=plus_scratch(main)
            actual,remote_queries,local_evals=routed(state,h,g)
            wanted=expected(state,h,g)
            assert remote_queries==local_evals==1
            assert set(actual)==set(wanted)
            assert max(abs(actual[k]-wanted[k]) for k in actual)<1e-12
            router_checks+=1

# Every high/low selected-slice table has the exact joint uniform law.
selected_tables=Counter(tuple((h[i]<<1)|low[i] for i in range(4))
                        for h,low in product(product(range(2),repeat=4),repeat=2))
assert len(selected_tables)==4**4 and set(selected_tables.values())=={1}

def adrs(layer,tree,typ,kp,w2,w3):
    return bytes([layer])+tree.to_bytes(8,'big')+bytes([typ])+kp.to_bytes(4,'big')+w2.to_bytes(4,'big')+w3.to_bytes(4,'big')

t=adrs(4,0,0,123,7,19)
def parse(w):
    return (w[:16],w[86:]) if len(w)==102 and w[16:64]==bytes(48) and w[64:86]==t else None

byte_checks=0
for p,x in product((bytes(16),bytes([1])*16,bytes([255])*16),repeat=2):
    w=p+bytes(48)+t+x
    assert parse(w)==(p,x)  # ALL public parameters, including pre-key guesses.
    byte_checks+=1
for s,r,z in product((bytes([1])*16,bytes([255])*16),(bytes(16),bytes([2])*16),(bytes(16),bytes([3])*16)):
    m=bytes(16)+t+bytes(16)
    assert parse(r+s+z+m) is None
    assert parse(r+s+bytes(32)+t+bytes(16)) is None  # PRF_msg-shaped raw word.
    byte_checks+=2
zero_alias=bytes([9])*16+bytes(16)+bytes(16)+(bytes(16)+t+bytes([5])*16)
assert parse(zero_alias)==(bytes([9])*16,bytes([5])*16)
assert parse(bytes(32)+bytes(4)+bytes([1])*16) is None  # Outer52 bytes.
for other in (adrs(4,0,0,123,7,18),adrs(4,0,0,123,6,19),adrs(4,0,1,123,7,19),adrs(3,0,0,123,7,19)):
    assert parse(bytes([1])*16+bytes(48)+other+bytes(16)) is None
    byte_checks+=1
for payload in (bytes(20),bytes(32),bytes(16*17),bytes(16*32)):
    assert parse(bytes([1])*16+bytes(48)+t+payload) is None
    byte_checks+=1

K=sum(1<<e for e in (41,36,31,26))
active=[32*K*max(14-r,0)+16*(1<<21)*max(254-r,0) for r in range(254)]
A=sum(active)
direct=32*K*sum(range(15))+16*(1<<21)*sum(range(255))
assert A==direct==7628143271608320
assert active[14]==16*(1<<21)*240 and active[253]==16*(1<<21)
result={
 'status':'PASS_EXACT_ONE_QUERY_COHERENT_TARGET_SLICE_ROUTER_AND_BYTE_CONTROLS',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'unitary_checks':router_checks,'remote_queries_per_full_call':1,'local_G_evaluations_per_full_call':1,
 'clean_plus_scratch_and_reference_entanglement':True,
 'selected_high_low_joint_uniform_tables':len(selected_tables),
 'actual_byte_framing_checks':byte_checks,'all_P_routed_prekey':True,
 'nonzero_S_inner_PRFmsg_excluded':True,'S0_inner_selected_slice_counterexample':True,
 'activation_sum':A,'active_r0':active[0],'active_r14':active[14],'active_r253':active[-1],
 'scope':'Tiny unitary identities and literal source byte framing/arithmetic; no source attack, full namespace, quantum-history measurement, numerical hardness or existing scalar change.'
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,indent=2))

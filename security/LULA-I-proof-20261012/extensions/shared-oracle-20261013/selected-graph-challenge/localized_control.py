"""Exact padded-selector and source-inventory controls, not a Rust refinement."""
import ast, hashlib, json
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[4]/'publications/LULA-I/release/code/lula1/src/lib.rs'
PIN = 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN
# Reuse the agent's saved toy-function definitions, without executing its file
# or rewriting its historical output. This is a successor control, not a new
# independent peer derivation.
tree = ast.parse((HERE/'control.py').read_text(encoding='utf-8'))
defs = [n for n in tree.body if isinstance(n, ast.FunctionDef)
        and n.name in ('graph','adapter_prefix','transcript')]
scope = {}
exec(compile(ast.Module(body=defs,type_ignores=[]), 'saved_toy_defs','exec'),scope)
graph, prefix, trace = (scope[x] for x in ('graph','adapter_prefix','transcript'))
fs_space = tuple(product(range(2),repeat=2))
ordinary = Counter()
by_selector = [Counter() for _ in range(3)]
PG = 0
win = 0
for seed in range(2):
    for fs in product(fs_space,repeat=3):
        xs,ys = graph(seed,fs)
        records = trace(seed,fs,ys)
        # This toy trace stands for classical terminal verifier records only;
        # no quantum or off-route source query extraction is claimed.
        witnesses = [(d,x) for d,x,y in records if x != xs[d] and y == ys[d]]
        first = witnesses[0] if witnesses else None
        PG += first is not None
        ordinary[(seed,fs,xs,ys,tuple(records))] += 1
        for j in range(4):
            if j == 3:
                # Padded dummy returns failure without constructing a target.
                continue
            outside = {d:fs[d] for d in range(3) if d != j}
            _,_,target = prefix(seed,outside,j)
            assert target == xs[j]
            installed = tuple(fs[d] if d == j else outside[d] for d in range(3))
            newxs,newys = graph(seed,installed)
            newrecords = trace(seed,installed,newys)
            by_selector[j][(seed,installed,newxs,newys,tuple(newrecords))] += 1
            win += first is not None and first[0] == j
assert all(c == ordinary for c in by_selector)
worlds = sum(ordinary.values())
assert Fraction(win,worlds*4) == Fraction(PG,worlds)/4

L = 1<<32
W_top = (1<<21)*(16*255+1) + ((1<<21)-1)
W_small = 32*(32*15+1)+31
W_fors = 17*(512+511)+1
P_cone = W_top-1
P_extract = W_top + 4*W_small + W_fors
V_cone = (1<<21)*16
V_extract = V_cone+4*32*32+17*512
assert (P_cone,V_cone)==(8560574462,33554432)
assert (P_extract,V_extract)==(8560653547,33567232)
D=39339469515522047
assert 1<<55 < D < 1<<56
out={
 'outcome':'PASS_LOCALIZED_PADDED_SELECTOR_AND_INVENTORY_NOT_STANDARD_PRIMITIVE_OR_RUST_PROOF',
 'source_sha256':PIN,
 'toy_ordinary_worlds':worlds,
 'toy_valid_domains':3,
 'toy_selector_outcomes':4,
 'toy_dummy_outcomes':1,
 'toy_terminal_G_probability':str(Fraction(PG,worlds)),
 'toy_first_witness_padded_success_probability':str(Fraction(win,worlds*4)),
 'exact_padded_loss_identity':'Pwin=PG/4, not PG/3',
 'ordinary_marginal_preserved_for_each_valid_selector':True,
 'source_padding_selector_bits':56,
 'source_valid_domains':D,
 'source_dummy_selector_count':(1<<56)-D,
 'source_predecessor_public_cap':P_cone,
 'source_predecessor_private_cap':V_cone,
 'source_final_routed_public_cap':P_extract,
 'source_final_routed_private_cap':V_extract,
 'largest_top_node_array_bytes':16*((1<<22)-1),
 'source_setup_public_cap':(1<<21)*(19505+L)-1,
 'source_cold_public_cap':W_top+82090+6*L,
 'source_hot_public_cap':82090+5*L,
 'source_final_selected_trace_cap':3217,
 'source_final_full_trace_cap':3224,
 'scope':'Final routed honest graph/event only on nonzero-S component game. No source execution, signatures, cache build, attack, timing, installs, uploads or paper edits.'
}
(HERE/'LOCALIZED-CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

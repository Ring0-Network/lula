"""Finite DAG challenge chronology/marginal/selection controls; no crypto run."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib, json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = ROOT / 'publications/LULA-I/release/code/lula1/src/lib.rs'
PIN = 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN

FUNCTIONS = tuple(product(range(2), repeat=2))

def graph(seed, fs):
    xs = [seed]
    ys = [fs[0][xs[0]]]
    xs.append(ys[0]); ys.append(fs[1][xs[1]])
    xs.append(ys[0] ^ ys[1]); ys.append(fs[2][xs[2]])
    return tuple(xs), tuple(ys)

def adapter_prefix(seed, outside, selected):
    # The designated target is computed without inspecting its own restriction.
    xs, ys = [], []
    for d in range(selected + 1):
        x = seed if d == 0 else ys[0] if d == 1 else ys[0] ^ ys[1]
        xs.append(x)
        if d == selected:
            return tuple(xs), tuple(ys), x
        assert d != selected
        ys.append(outside[d][x])
    raise AssertionError('unreachable')

def transcript(seed, fs, ys):
    # Pre-key query first; post-key choices see root and one logical cache field.
    pre = fs[0][0]
    schedule = [(0, 0), ((pre ^ ys[2]) % 3, ys[1]), ((ys[2]+1) % 3, pre)]
    return [(d, x, fs[d][x]) for d, x in schedule]

ordinary = Counter()
adapter_worlds = [Counter() for _ in range(3)]
event_count = 0
wins = [0, 0, 0]
target_unchanged = 0
for seed in range(2):
    for fs in product(FUNCTIONS, repeat=3):
        xs, ys = graph(seed, fs)
        trace = transcript(seed, fs, ys)
        world = (seed, fs, xs, ys, tuple(trace))
        ordinary[world] += 1
        witnesses = [(d,x) for d,x,y in trace if x != xs[d] and y == ys[d]]
        first = witnesses[0] if witnesses else None
        event_count += first is not None
        for selected in range(3):
            outside = {d: fs[d] for d in range(3) if d != selected}
            prefix_xs, prefix_ys, target = adapter_prefix(seed, outside, selected)
            assert target == xs[selected]
            # Every possible selected function is available only AFTER commit;
            # selected target must remain unchanged when that function varies.
            for h in FUNCTIONS:
                newfs = tuple(h if d == selected else fs[d] for d in range(3))
                assert graph(seed, newfs)[0][selected] == target
                target_unchanged += 1
            installed = tuple(fs[d] if d == selected else outside[d] for d in range(3))
            got_xs, got_ys = graph(seed, installed)
            got_trace = transcript(seed, installed, got_ys)
            adapter_worlds[selected][(seed,installed,got_xs,got_ys,tuple(got_trace))] += 1
            if first is not None and first[0] == selected:
                d,x = first
                assert x != target and installed[selected][x] == installed[selected][target]
                wins[selected] += 1

assert all(c == ordinary for c in adapter_worlds)
worlds = sum(ordinary.values())
pg = Fraction(event_count, worlds)
pwin = Fraction(sum(wins), 3 * worlds)
assert pwin == pg / 3

heights = [5,5,5,5,21]
keys = [1 << sum(heights[i:]) for i in range(5)]
trees = [1 << sum(heights[i+1:]) for i in range(5)]
chains = [32,32,32,32,16]
widths = [16,16,16,16,256]
counts = {
    'type0': sum(k*l*(w-1) for k,l,w in zip(keys,chains,widths)),
    'type1': sum(keys),
    'type2': sum(t*((1<<h)-1) for t,h in zip(trees,heights)),
    'type3': (1<<41)*17*((1<<10)-1),
    'type4': 1<<41,
}
D = sum(counts.values())
U = sum(k*l for k,l in zip(keys,chains)) + (1<<41)*17*512
assert D == 39339469515522047
assert U == 19212937084272640
assert 17*10 + 1 + 4*(240+1+5) + 2040+1+21 == 3217
assert 3217+5+2 == 3224
out = {
    'outcome': 'PASS_TINY_ADDRESSED_CHALLENGE_CONTROLS_NOT_STANDARD_SPR_OR_SOURCE_REFINEMENT',
    'source_sha256': PIN,
    'toy_ordinary_worlds': worlds,
    'toy_selected_domains': 3,
    'ordinary_joint_marginal_exact_for_each_selected_address': True,
    'target_own_restriction_independence_checks': target_unchanged,
    'toy_G_probability': str(pg),
    'toy_first_witness_selected_success_probability': str(pwin),
    'exact_loss_identity': 'Pwin = PG / 3',
    'toy_selection_wins_by_domain': wins,
    'source_symbolic_domain_counts': counts,
    'source_total_selected_domains': D,
    'source_private_coordinate_count': U,
    'finite_loss_factor': D,
    'eager_graph_raw_data_byte_cap': 566*D + 54*U,
    'scope': 'Tiny random-function DAG and integer inventory only; no source signature, attack, cache generation, timing, upload, or manuscript change.'
}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out, indent=2)+'\n',encoding='utf-8')
print(json.dumps(out, indent=2))

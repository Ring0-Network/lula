"""Small source-layout and abstract auxiliary-view controls; no crypto execution."""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
R = HERE.parents[4]
LIB = R / 'publications/LULA-I/release/code/lula1/src/lib.rs'
DRIVER = LIB.parent / 'bin/lula1_driver_original.rs'
assert sha256(LIB.read_bytes()).hexdigest() == 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
height = 21
width = 1 << height
levels = []
for level in range(height + 1):
    off = (1 << (height + 1)) - (1 << (height + 1 - level))
    n = 1 << (height - level)
    levels.append({'level': level, 'offset_nodes': off, 'count': n,
                   'logical_offset_bytes': off * 16, 'bytes': n * 16})
assert all(a['offset_nodes'] + a['count'] == b['offset_nodes']
           for a, b in zip(levels, levels[1:]))
nodes = (1 << (height + 1)) - 1
assert levels[-1]['offset_nodes'] == nodes - 1
node_bytes = 16 * nodes
counter_bytes = 4 * width
payload_bytes = node_bytes + counter_bytes
framing_bytes = 8 + 48 + 16 + 8 + 5 + 8 + 8 + 8 + 8
assert (node_bytes, counter_bytes, payload_bytes, framing_bytes) == (
    67108848, 8388608, 75497456, 117)

# Exact toy representation: hidden predecessor X, independent public endpoint
# L, child root V, top root R, two candidate full row slots for each V.
# This tests the abstract factorization pattern, not a Rust/hash refinement.
groups = {}
bad_groups = {}
worlds = 0
for x, leaf, child, root, y00, y01, y10, y11 in product(range(2), repeat=8):
    rows = ((y00, y01), (y10, y11))
    row = rows[child]
    canonical = next((i for i, y in enumerate(row) if y == 1), None)
    view = (leaf, child, root, canonical)
    groups.setdefault(view, Counter())[x] += 1
    # Deliberately adding a private work-buffer field breaks the factorization.
    bad_groups.setdefault(view + (x,), Counter())[x] += 1
    worlds += 1
assert worlds == 256
assert all(c[0] == c[1] for c in groups.values())
assert all(c[0] == 0 or c[1] == 0 for c in bad_groups.values())

report = {
    'outcome': 'PASS_LAYOUT_AND_ABSTRACT_FACTORISATION_CONTROLS',
    'scope': 'No signature execution, no forged payload, no full cache allocation. '
             'The toy is an abstract factorization check, not source security proof.',
    'library_sha256': sha256(LIB.read_bytes()).hexdigest(),
    'driver_sha256': sha256(DRIVER.read_bytes()).hexdigest(),
    'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'height': height, 'levels': levels,
    'node_bytes': node_bytes, 'counter_bytes': counter_bytes,
    'payload_bytes': payload_bytes,
    'driver_framing_bytes': framing_bytes,
    'driver_file_bytes': payload_bytes + framing_bytes,
    'toy_worlds': worlds, 'toy_view_groups': len(groups),
    'hidden_predecessor_uniform_in_every_toy_view': True,
    'private_buffer_negative_control_nonuniform_in_every_view': True,
}
(HERE / 'CONTROL-RESULTS.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: report[k] for k in ('outcome','payload_bytes','driver_file_bytes','toy_worlds','toy_view_groups')}))

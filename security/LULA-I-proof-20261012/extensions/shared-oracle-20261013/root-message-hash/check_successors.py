"""Exact integer accounting; these losses are not security exponents."""
from pathlib import Path
import json
E = Path(__file__).resolve().parent
q_exponents = [24,30,38,40,41,44,50,64]
counts = {
    128:20229886488608768,
    256:19105114044235775,
    2048:2097152,
    2176:2199023255552,
    4096:2269957324800,
}
bits = {m:(n-1).bit_length() for m,n in counts.items()}
assert list(bits.values()) == [55,55,21,41,42]
assert sum(counts.values()) == 39339469515522047
rows = []
for e in q_exponents:
    q = 1 << e
    k = min(17,q)
    rows.append({'q_exponent':e,'k':k,'dense_loss_log2':32*k,
                 'sparse_loss_log2':(e+32)*k,
                 'fixed_h_security':'not established'})
assert [r['sparse_loss_log2'] for r in rows] == [952,1054,1190,1224,1241,1292,1394,1632]
out = {'classification':'COMPUTED exact integer accounting',
       'graph_counts':counts,'graph_selector_bits':bits,'rows':rows,
       'scope':'Reduction losses and selectors only; no new hardness, probability, capacity or category certificate'}
(E/'SUCCESSOR-COUNTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))

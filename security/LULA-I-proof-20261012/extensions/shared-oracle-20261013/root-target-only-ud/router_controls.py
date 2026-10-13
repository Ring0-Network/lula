"""Exact phase-table control for one remote plus one outside XOR query."""
from itertools import product
from pathlib import Path
import hashlib,json
E=Path(__file__).resolve().parent
parity=lambda n:n.bit_count()%2
worlds=checks=0
for remote in product(range(2),repeat=2):
  for outside in product(range(4),repeat=4):
    worlds+=1
    for x in range(4):
      s=int(x<2)
      gx=x if s else 0
      value=((remote[gx] if s else outside[x]>>1)<<1)|(outside[x]&1)
      for z in range(4):
        for y in range(4):
          numerator=0
          for k in range(4):
            remote_mask=s*(k>>1)
            outside_mask=((1-s)*(k>>1)<<1)|(k&1)
            phase=parity(k&z)^parity(remote[gx]&remote_mask)^parity(outside[x]&outside_mask)^parity(k&y)
            numerator+=(-1)**phase
          assert numerator==(4 if y==(z^value) else 0)
          checks+=1
out={'classification':'COMPUTED exact finite router control',
 'worlds':worlds,'response_amplitude_checks':checks,
 'ordinary_remote_queries_per_raw_query':1,'ordinary_outside_queries_per_raw_query':1,
 'controlled_unknown_oracle_queries':0,'exit_code':0,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Finite phase identity only; no full source, primitive hardness or quantum-game kernel proof'}
(E/'ROUTER-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))

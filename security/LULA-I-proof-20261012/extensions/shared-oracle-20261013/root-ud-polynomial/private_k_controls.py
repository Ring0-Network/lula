"""Exact small-alphabet full-word private-key overlay law; no signatures."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
E=Path(__file__).resolve().parent
vals=range(4) # one prefix bit, one retained lower bit
direct=Counter();overlay=Counter();ideal=Counter()
for oracle in product(vals,repeat=4):
  for key in (0,1):
    priv=(oracle[key]//2,oracle[2+key]//2)
    direct[(oracle,priv)]+=1
    for fullpriv in product(vals,repeat=2):
      new=list(oracle)
      for addr in (0,1):new[2*addr+key]=fullpriv[addr]
      prefix=tuple(v//2 for v in fullpriv)
      overlay[(tuple(new),prefix)]+=1
      ideal[(oracle,prefix)]+=1
assert sum(overlay.values())==8192
assert overlay==Counter({k:16*v for k,v in direct.items()})
assert len(ideal)==256*4 and set(ideal.values())=={8}
# Marginal full-word oracle is uniform; lower limbs are retained, not fixed.
marginal=Counter()
for (oracle,priv),count in overlay.items():marginal[oracle]+=count
assert len(marginal)==256 and set(marginal.values())=={32}
N=1<<128
def v(qa):
  d=4*qa*qa
  return min(F(1),F(d,N-d)) if d<N else F(1)
rows=[{'log2_QA':q,'conditional_gap':str(v(1<<q)),
       'unconditional_standalone':str(min(F(1),F(1,N)+F(N-1,N)*v(1<<q)))} for q in (0,24,32,40,50,60,63,64)]
out={'status':'PASS_SCOPED_FULL_WORD_KEY_OVERLAY_LAW',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'overlay_worlds':sum(overlay.values()),'direct_worlds':sum(direct.values()),
 'exact_real_overlay_matches_direct_joint_law':True,'ideal_function_private_map_independent':True,
 'full_output_lower_limb_preserved':True,'rows':rows,
 'source_execution_or_kernel':False,'category':'not established'}
(E/'PRIVATE-K-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'worlds':8192,'joint_law':'exact','QA32':str(v(1<<32))}))

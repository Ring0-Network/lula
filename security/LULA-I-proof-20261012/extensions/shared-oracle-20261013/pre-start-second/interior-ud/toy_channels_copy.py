"""Exact abstract stopped-chain controls, not LULA signing or a forgery."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib,json
E=Path(__file__).resolve().parent
maps=list(product(range(2),repeat=2))
controls=0
for fs in product(maps,repeat=3):
  for policy in range(8):
    def event(xs):
      # Two adaptive completed requests; an exposure <=p=2 stops.
      root=xs[3]
      first=(root+policy)%4
      if first<=2:return 0
      second=(fs[0][root]+policy//2)%4
      if second<=2:return 0
      candidate=fs[policy%3][root] ^ ((policy//4)%2)
      return int(candidate==xs[2] and fs[2][candidate]==root)
    def game(r):
      total=0
      for coins in product(range(2),repeat=r+1):
        xs=list(coins)
        for j in range(r,3):xs.append(fs[j][xs[j]])
        total+=event(xs)
      return Fraction(total,2**(r+1))
    def ud(r,random):
      total=0
      # Opaque X is coupled only for checking; simulator consumes Y/suffix.
      for prior in product(range(2),repeat=r):
        for X in range(2):
          ys=range(2) if random else [fs[r][X]]
          for Y in ys:
            xs=list(prior)+[X,Y]
            for j in range(r+1,3):xs.append(fs[j][xs[j]])
            total+=event(xs)
      return Fraction(total,2**(r+1+int(random)))
    for r in range(2):
      assert ud(r,False)==game(r)
      assert ud(r,True)==game(r+1)
      controls+=2
    terminal_pre=0
    for earlier in product(range(2),repeat=2):
      for X in range(2):
        xs=list(earlier)+[X,fs[2][X]]
        root=xs[3]
        if (root+policy)%4<=2:continue
        if (fs[0][root]+policy//2)%4<=2:continue
        v=fs[policy%3][root] ^ ((policy//4)%2)
        terminal_pre+=int(fs[2][v]==root)
    pre=Fraction(terminal_pre,8)
    assert game(2)<=pre
    assert game(0)<=pre+sum(abs(game(r)-game(r+1)) for r in range(2))
    controls+=2
out={'classification':'COMPUTED exact abstract finite channel control',
     'fixed_function_worlds':64,'policies_per_world':8,'checks':controls,
     'exit_code':0,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Three-edge binary stopped chain; no LULA signatures, source refinement, hardness or quantum-game mechanization'}
(E/'TOY-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))

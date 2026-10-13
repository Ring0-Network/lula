"""Exact small conventional-interface controls; not hash hardness tests."""
from itertools import product
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
worlds=targets=collisions=identical_input_preimages=0
seed_dependent_inputs=0
# Two public parameter values. The fixed public function description consists
# of two tweak tables with four two-bit inputs, shared across phases. At seed1
# input coordinates are permuted, rather than sampling a new target function.
for pred,tgt in product(product(range(4),repeat=4),repeat=2):
    worlds+=1
    def h(seed,tweak,x):
        table=pred if tweak==0 else tgt
        prefix=table[(x+seed)%4]
        lower=(seed^tweak^x)&1
        return (prefix<<1)|lower
    for secret in range(4):
        children=[]
        for seed in (0,1):
            collection_tweaks=[]; challenge_tweaks=[]
            def col(tweak,x):
                collection_tweaks.append(tweak)
                return h(seed,tweak,x)>>1
            child=col(0,secret)
            def challenge(tweak,x):
                challenge_tweaks.append(tweak)
                return h(seed,tweak,x)>>1
            target=challenge(1,child)
            assert len(challenge_tweaks)==1
            assert set(collection_tweaks).isdisjoint(challenge_tweaks)
            # Seed now released; full public h evaluation matches challenge.
            assert h(seed,1,child)>>1==target
            children.append(child)
            targets+=1
            for changed in range(4):
                equal=(h(seed,1,changed)>>1)==target
                tcr_win=changed!=child and equal
                if tcr_win: collisions+=1
                if changed==child:
                    assert equal and not tcr_win
                    identical_input_preimages+=1
        seed_dependent_inputs+=int(children[0]!=children[1])
assert worlds==4**8 and targets==worlds*4*2
assert seed_dependent_inputs>0 and collisions>0
assert identical_input_preimages==targets
out={'status':'PASS','scope':'Synthetic public fixed-h collection interface, chronology and PRE/TCR predicate checks; no source or SHA hardness test',
     'fixed_public_function_worlds':worlds,'registered_targets':targets,
     'different_input_prefix_collisions':collisions,'same_input_PRE_but_not_TCR_cases':identical_input_preimages,
     'seed_dependent_child_pairs':seed_dependent_inputs,
     'collection_challenge_tweak_disjoint':True,'same_full_function_retained':True,
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

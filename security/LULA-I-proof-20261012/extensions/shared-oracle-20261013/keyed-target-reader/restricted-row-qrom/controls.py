"""Exact tiny function-law, coherent-XOR and joint-state controls; no source attack."""
from itertools import product
from collections import defaultdict, Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent

def canonical(row):
    return next(((c,w) for c,w in enumerate(row) if (w>>1)==1), None)

worlds = []
groups = defaultdict(Counter)
counts = Counter()
for child in (0,1):
    for raw in product(range(4), repeat=4):
        genuine = raw[child*2:child*2+2]
        changed = raw[(1-child)*2:(1-child)*2+2]
        groups[(child,genuine)][changed] += 1
        target = canonical(genuine)
        counts[None if target is None else target[0]] += 1
        worlds.append((child,raw,target))
assert len(worlds)==512
assert counts=={0:256,1:128,None:128}
for fixed_side, distribution in groups.items():
    assert len(distribution)==16
    assert set(distribution.values())=={1}
    assert set(distribution)==set(product(range(4),repeat=2))

# Fullword Bernoulli completion retains the lower output limb exactly in law.
# 3-bit fullwords; 2-bit prefixes, one lower bit; target prefix1.
completion = defaultdict(Fraction)
target_prefix=1
hit_words=[w for w in range(8) if w>>1==target_prefix]
miss_words=[w for w in range(8) if w>>1!=target_prefix]
for w in hit_words:
    completion[w] += Fraction(1,4)*Fraction(1,len(hit_words))
for w in miss_words:
    completion[w] += Fraction(3,4)*Fraction(1,len(miss_words))
assert completion=={w:Fraction(1,8) for w in range(8)}

# A two-f-query simulation with inactive plus-state is tested coherently.
# Registers are x(2bits), output(2bits), mark scratch(1bit), plus scratch(1bit).
def transform(vector, permutation):
    result={}
    for state,amplitude in vector.items():
        dest=permutation(state)
        assert dest not in result
        result[dest]=amplitude
    return result

coherent_tests=0
for child in (0,1):
    for f in product((0,1), repeat=4):
        for side in product(range(4), repeat=2):
            for variant in range(4):
                hit=lambda x:2+((x^variant)&1)
                miss=lambda x:((x^variant)>>1)&1
                raw=lambda x:(hit(x) if f[x] else miss(x)) if x//2!=child else side[x%2]
                swap=lambda st:(st[0],st[1],st[3],st[2]) if st[0]//2==child else st
                fq=lambda st:(st[0],st[1],st[2]^f[st[0]],st[3])
                def xor_reply(st):
                    x,y,s,p=st
                    value=(hit(x) if s else miss(x)) if x//2!=child else side[x%2]
                    return x,y^value,s,p
                for x,y in product(range(4),repeat=2):
                    # Unnormalized plus is sufficient for exact equality.
                    start={(x,y,0,0):1+0j,(x,y,0,1):1+0j}
                    state=transform(start,swap)
                    state=transform(state,fq)
                    state=transform(state,xor_reply)
                    state=transform(state,fq)
                    state=transform(state,swap)
                    expected={(x,y^raw(x),0,0):1+0j,(x,y^raw(x),0,1):1+0j}
                    assert state==expected
                    coherent_tests+=1
assert coherent_tests==32768

# Joint oracle/control-state commutation, retaining hidden target work.
# A nontrivial coherent A input is carried in the joint classical-oracle blocks.
joint={}
records={}
for oid,(child,raw,target) in enumerate(worlds):
    record=(child<<4) | (0 if target is None else 8|(target[0]<<2)|target[1])
    records[oid]=record
    for x,y in product(range(4),repeat=2):
        joint[(oid,x,y,0)] = (1j)**((x+2*y+oid)%4)

def pre(st):
    oid,x,y,b=st
    return oid,x,y,b^records[oid]
def a_query(st):
    oid,x,y,b=st
    return oid,x,y^worlds[oid][1][x],b
left=transform(transform(joint,pre),a_query)
right=transform(transform(joint,a_query),pre)
assert left==right
assert len(left)==8192

# Actual byte-frame aliases: an inner hash equal to a type7 changed word forces S=0.
address=bytes([0])+bytes(8)+bytes([7])+bytes(12)
assert len(address)==22
alias_checks=0
for first_byte in (0,1,2,255):
    seed=bytes([first_byte])+bytes(15)
    changed=seed+bytes(48)+address+bytes([3])*16+(5).to_bytes(4,'big')
    assert len(changed)==106
    required_inner_r=changed[:16]
    required_inner_root=changed[32:48]
    required_message=changed[48:]
    inner=required_inner_r+seed+required_inner_root+required_message
    assert (inner==changed)==(seed==bytes(16))
    assert len(bytes(32)+(5).to_bytes(4,'big')+seed)==52
    alias_checks+=1

receipt={
    'scope':'Tiny exact mathematical controls only, no source/kernel/security-level verification',
    'joint_fullword_worlds':len(worlds),
    'fixed_genuine_side_groups':len(groups),
    'changed_fullword_pairs_per_side':16,
    'canonical_c0_mass':str(Fraction(counts[0],len(worlds))),
    'canonical_c1_mass':str(Fraction(counts[1],len(worlds))),
    'bottom_mass':str(Fraction(counts[None],len(worlds))),
    'fullword_boolean_completion_mass_each':'1/8',
    'two_query_inactive_plus_coherent_basis_tests':coherent_tests,
    'joint_commuting_control_state_entries':len(left),
    'literal_inner_alias_seed_checks':alias_checks,
    'nonzero_inner_aliases':0,
    'changed_raw_length':106,
    'outer_raw_length':52,
    'primary_bound':'SPHINCS+C2022/778 TheoremE.3:8(q+1)^2*lambda',
    'restricted_bound':'min(1,8*(2*Q+1)^2/2^128)',
    'source_nonzero_Q_cap':'Q_A_quantum+Q_A_classical+1',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(OUT/'CONTROL-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))

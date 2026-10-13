"""Exact abstract row-policy and function-composition controls; no cryptographic implementation."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib
import json

HERE=Path(__file__).resolve().parent
X=HERE.parents[2]
SOURCE=X.parents[3]/'publications/LULA-I/release/code/lula1/src/lib.rs'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(SOURCE)=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
vectors=list(product(range(4),repeat=2))
accept=lambda vector:sum(vector)==3
accepted=[v for v in vectors if accept(v)]
counts={'tables':0,'no_accepted_counter':0,'different_accepted_counter':0,
        'rejected_cached_counter_recomputed':0,'same_vector_different_counter':0}
for table in product(vectors,repeat=2):
    counts['tables']+=1
    canonical=next((c for c,d in enumerate(table) if accept(d)),None)
    if canonical is None:
        counts['no_accepted_counter']+=1
        continue
    if canonical!=0:
        continue
    proposed=1
    chosen=proposed if accept(table[proposed]) else canonical
    if accept(table[proposed]):
        assert chosen!=canonical
        assert chosen.to_bytes(4,'big')!=canonical.to_bytes(4,'big')
        counts['different_accepted_counter']+=1
        if table[0]==table[1]:counts['same_vector_different_counter']+=1
    else:
        assert chosen==canonical
        counts['rejected_cached_counter_recomputed']+=1
assert counts['tables']==256 and counts['no_accepted_counter']==144
assert counts['different_accepted_counter']==16
assert counts['same_vector_different_counter']==4
assert counts['rejected_cached_counter_recomputed']==48
p=Fraction(len(accepted),len(vectors))
assert Fraction(counts['different_accepted_counter'],counts['tables'])==p*p

# Arbitrary deterministic, addressed finite functions suffice for concatenation.
def step(chain,stage,value):return (value*3+chain+stage+1)%8
def iterate(chain,value,start,stop):
    for stage in range(start,stop):value=step(chain,stage,value)
    return value
composition_checks=0
for chain,start,digit in product(range(2),range(8),range(4)):
    prefix=iterate(chain,start,0,digit)
    assert iterate(chain,prefix,digit,3)==iterate(chain,start,0,3)
    composition_checks+=1
assert composition_checks==64

# Positive-support implication for every nonempty abstract acceptance size.
acceptance_size_checks=0
for size in range(1,17):
    good=set(vectors[:size])
    both=sum(t[0] in good and t[1] in good for t in product(vectors,repeat=2))
    assert both==size*size and both>0
    acceptance_size_checks+=1

record={
 'status':'PASS_EXACT_ABSTRACT_ROW_POLICY_AND_CHAIN_COMPOSITION_CONTROLS',
 'script_sha256':sha(Path(__file__)),
 'first_derivation_sha256':sha(HERE/'FIRST-DERIVATION.md'),
 'source_sha256':sha(SOURCE),'counts':counts,
 'p':str(p),'two_accepted_probability':str(p*p),
 'chain_composition_checks':composition_checks,
 'nonempty_acceptance_size_checks':acceptance_size_checks,
 'actual_hash_signature_or_cache_generated':False,
 'full_shared_raw_source_probability_transfer_proved':False,
 'fresh_message_forgery_or_security_failure_proved':False,
 'scope':'Abstract row-law identities and deterministic chain composition only.'}
(HERE/'CONTROLS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps(record))

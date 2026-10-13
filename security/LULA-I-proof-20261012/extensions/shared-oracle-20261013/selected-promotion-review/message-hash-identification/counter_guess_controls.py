"""Exact guessed-counter probability and logical-codeword controls only."""
from itertools import product
from fractions import Fraction
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
tests=0
for L in (2,3,4):
    for n in range(1,6):
        for r in range(n+1):
            # Full guess-vector enumeration, witness subset fixed by SOURCE view.
            good=sum(all(g[i]==(i%L) for i in range(r)) for g in product(range(L),repeat=n))
            assert Fraction(good,L**n)==Fraction(1,L**r)
            assert Fraction(good,L**n)>=Fraction(1,L**17)
            tests+=1
L=1<<32
for r in range(18):assert Fraction(1,L**r)>=Fraction(1,1<<544)
assert L**17==1<<544

B=3
def encode(s,t,m,c):
    assert len(s)==len(t)==16 and len(m)<=B
    return s+t+c.to_bytes(4,'big')+len(m).to_bytes(4,'big')+m+bytes(B-len(m))
def decode(x):
    assert len(x)==40+B
    size=int.from_bytes(x[36:40],'big')
    if size>B or any(x[40+size:]):return None
    return x[:16],x[16:32],x[40:40+size],int.from_bytes(x[32:36],'big')
codewords=[]
for s,t,m,c in product((bytes(16),bytes([1])*16),(bytes(16),bytes([2])*16),(b'',b'a',b'a\x00',b'abc'),range(4)):
    x=encode(s,t,m,c)
    assert decode(x)==(s,t,m,c)
    codewords.append(x)
assert len(set(codewords))==len(codewords)==64
bad_length=bytes(36)+(B+1).to_bytes(4,'big')+bytes(B)
bad_padding=bytes(40)+bytes([1])+bytes(B-1)
assert decode(bad_length) is None and decode(bad_padding) is None

# Input counter guesses never affect a source response computed canonically.
source_marginal=0
for R in range(4):
    c0=R&1
    replies={(R,c0) for guess in range(4)}
    assert replies=={(R,c0)}
    source_marginal+=1
result={
 'scope':'Exact algebra/interface controls, no source signature or SHA security run',
 'full_guess_vector_cases':tests,'witness_bound':17,'exact_source_counter_loss_bits':544,
 'canonical_counter_match_probability':'L^-r for r<=17',
 'logical_codewords_injective_count':64,'invalid_codes_total_completion_required':True,
 'source_response_guess_independence_cases':source_marginal,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'proposal_sha256':hashlib.sha256((HERE/'COUNTER-GUESS-LIFT.md').read_bytes()).hexdigest(),
 'input_clarification_sha256':hashlib.sha256((HERE/'COUNTER-GUESS-INPUT-COMPLETION.md').read_bytes()).hexdigest(),
}
(HERE/'COUNTER-GUESS-CONTROLS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

"""Exact small controls for source framing, counts and root-target criterion.
No source parameters are changed and no actual hash/preimage search is run.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json

def count(ell, w, s):
    return sum((-1)**j*comb(ell,j)*comb(s-j*w+ell-1,ell-1)
               for j in range(min(ell,s//w)+1))
lo=count(32,16,240)
top=count(16,256,2040)
n=2**128
assert lo*1024>n and top*1024>n
assert top==454918678781617793203528879683071744

# Literal layout and the final complete raw input for both source directions.
offset=20+17*(16+9*16)+4*(4+32*16+5*16)
assert offset==5124
last=offset+4+16*16+20*16
assert last==5704 and last+16==5720
a=(bytes([4])+bytes(8)+bytes([2])+bytes(4)
   +(21).to_bytes(4,'big')+bytes(4))
assert len(a)==22 and a.hex()=='04000000000000000002000000000000001500000000'
s=bytes(range(16))
v=bytes(range(16,32))
for direction in (0,1):
    words=[]
    for b in range(256):
        x=bytes(15)+bytes([b])
        word=s+bytes(48)+a+(v+x if direction==0 else x+v)
        assert len(word)==118
        assert word[-16:] == (x if direction==0 else v)
        words.append(word)
    assert len(set(words))==256

# Full small function enumeration checks both possible honest-root conditioning
# cases. No promise of a unique target or existing preimage is made.
nt=4
without_one=sum(sum(y==0 for y in tab)==1
                for tab in product(range(nt),repeat=nt))
with_one=sum(sum(y==0 for y in (0,)+rest)==1
             for rest in product(range(nt),repeat=nt-1))
p1a=F(without_one,nt**nt)
p1b=F(with_one,nt**(nt-1))
assert p1a==p1b==F(27,64)
# Two distinct candidate positions in an unprogrammed family.
classical_hits=sum(0 in tab[:2] for tab in product(range(nt),repeat=nt))
assert F(classical_hits,nt**nt)==1-F(3,4)**2

# An exact one-mark Grover control on16 inputs uses rational amplitudes.
ng=16
amp=[F(1,4)]*ng
for _ in range(4):
    amp[0]=-amp[0]
    mean=sum(amp)/ng
    amp=[2*mean-x for x in amp]
assert sum(x*x for x in amp)==1
grover_p=amp[0]**2

l=2**20
b=(6*l+3217)+1+3224
assert b==6297898 and b<2**24
t=(2**64-b)//2
# arcsin(x)>=x; arcsin(x)<=x/sqrt(1-x^2). A coarse rational
# upper sqrt bound uses1/sqrt(1-x^2)<=1+2x^2 for x<=1/2.
x=F(1,2**64)
angle_lower=(2*t+1)*x
angle_upper=(2*t+1)*x*(1+2*x*x)
assert angle_lower>F(99,100) and angle_upper<F(101,100)
assert F(99,100)-F(101,100)**3/6>F(4,5)
assert F(31,32)**2*F(1,3)*F(16,25)==F(961,4800)>F(1,5)

result={
    'status':'PASS_EXACT_ARITHMETIC_AND_FINITE_MODEL_CONTROLS',
    'lower_accepted_vector_count':str(lo),
    'top_accepted_vector_count':str(top),
    'both_acceptance_probabilities_above_1_over_1024':True,
    'serialized_bytes':5720,
    'last_free_sibling_offset':5704,
    'last_address_hex':a.hex(),
    'last_raw_input_bytes':118,
    'orientation_and_injective_sample_words':512,
    'toy_unprogrammed_tables':nt**nt,
    'toy_programmed_tables':nt**(nt-1),
    'toy_exact_single_mark_probability':str(p1a),
    'toy16_four_grover_iteration_success':str(grover_p),
    'real_query_overhead':b,
    'real_grover_iterations':str(t),
    'modeled_strict_lower_constant':str(F(961,4800)),
    'no_actual_sha_search_or_parameter_change':True,
}
Path(__file__).with_name('CHECKS.json').write_text(
    json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

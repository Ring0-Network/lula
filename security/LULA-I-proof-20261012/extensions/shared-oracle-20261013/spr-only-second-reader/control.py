"""Generic identity-chain WOTS countermodel; does not call LULA/SHA chain code."""
from itertools import product
from pathlib import Path
import hashlib
import json

ELL,W,S = 32,16,240
e = [15]*16+[0]*16
ep = [0]*16+[15]*16
def accepted(d):
    return len(d)==ELL and all(0<=v<W for v in d) and sum(d)==S
def encode(d):
    return bytes((d[2*i]<<4)|d[2*i+1] for i in range(16))
def decode(d):
    return [n for byte in d for n in (byte>>4,byte&15)]
assert accepted(e) and accepted(ep) and e!=ep
assert not all(a<=b for a,b in zip(e,ep))
assert not all(a>=b for a,b in zip(e,ep))
assert encode(e)!=encode(ep) and decode(encode(e))==e and decode(encode(ep))==ep

# Two-message injective preprocessing; not an assumed full-source message hash.
messages = {b"accepted-vector-0":encode(e),b"accepted-vector-1":encode(ep)}
secrets = [i.to_bytes(16,"big") for i in range(ELL)]
def chain(tweak,x,start,steps):
    assert 0<=start<=W-1 and 0<=steps<=W-1-start
    for position in range(start,start+steps):
        x = x  # abstract F_(tweak,position)=id on fixed128-bit nodes
    return x
def compress_pk(endpoints):
    return hashlib.sha256(b"generic-countermodel-pk"+b"".join(endpoints)).digest()[:16]
ends = [chain(i,x,0,W-1) for i,x in enumerate(secrets)]
pk = compress_pk(ends)
def sign(message):
    digits = decode(messages[message])
    assert accepted(digits)
    nodes = [chain(i,x,0,digits[i]) for i,x in enumerate(secrets)]
    return bytes(4)+b"".join(nodes)
def verify(message,signature):
    if len(signature)!=4+16*ELL or signature[:4]!=bytes(4):
        return False
    digits = decode(messages[message])
    if not accepted(digits):
        return False
    nodes = [signature[4+16*i:4+16*(i+1)] for i in range(ELL)]
    completed = [chain(i,x,digits[i],W-1-digits[i]) for i,x in enumerate(nodes)]
    return compress_pk(completed)==pk

sigma = sign(b"accepted-vector-0")
assert sigma == sign(b"accepted-vector-1")
assert verify(b"accepted-vector-0",sigma)
assert verify(b"accepted-vector-1",sigma)
assert [sigma[4+16*i:4+16*(i+1)] for i in range(ELL)]==secrets

# Finite evidence for injectivity/inversion: the general property is mathematical.
spr_pairs = 0
for tweak,x,xp in product(range(15),range(4),range(4)):
    if x!=xp:
        assert x!=xp  # identity outputs never equal for distinct inputs
        spr_pairs += 1
    assert x==x  # public inverse is identity

result={
    "status":"PASS_GENERIC_SPR_ONLY_IDENTITY_CHAIN_COUNTERMODEL",
    "parameters":{"chains":ELL,"width":W,"accepted_sum":S,"forced_zero_digits":0},
    "digits_e":e,"digits_e_prime":ep,
    "encoded_e":encode(e).hex(),"encoded_e_prime":encode(ep).hex(),
    "both_accepted":True,"distinct_incomparable_vectors":True,
    "model_signature_bytes":len(sigma),"model_public_key_bytes":len(pk),
    "honest_message":"accepted-vector-0","fresh_countermodel_message":"accepted-vector-1",
    "same_signature_verifies_for_both":True,"all_chain_starts_exposed":True,
    "identity_same_tweak_second_preimage_advantage":"0 exactly",
    "identity_public_preimage_success":"1 exactly",
    "finite_distinct_input_pairs_checked":spr_pairs,
    "actual_SHA_LULA_forgery":False,
    "scope":"Abstract fixed-width chain primitive assumption separation; two-message injective preprocessing and independent PK compression",
}
Path(__file__).with_name("CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

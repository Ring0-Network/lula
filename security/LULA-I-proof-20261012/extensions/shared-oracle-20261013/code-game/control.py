"""Small exact controls for the manual classical coupling; not EUF/QROM tests."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = ROOT / "publications/LULA-I/release/code/lula1/src/lib.rs"
PIN = "ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210"
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN

M = 16
ys = range(8)  # Public execution coins, independent of the unused secret.
hits = sum(k in (y, (y + 5) % M) for y in ys for k in range(M))
independent_two_guess = Fraction(hits, len(ys) * M)
assert independent_two_guess == Fraction(2, M)
surviving = [k for k in range(M) if k != 3]
survival_next_guess = Fraction(sum(k == 8 for k in surviving), len(surviving))
assert survival_next_guess == Fraction(1, M - 1)
assert survival_next_guess > Fraction(1, M)
leaked_bit_guess = Fraction(sum(k == (k & 1) for k in range(M)), M)
assert leaked_bit_guess == Fraction(2, M) > Fraction(1, M)

def address(typ):
    return bytes([4]) + (0).to_bytes(8,"big") + bytes([typ]) + (7).to_bytes(4,"big") + (3).to_bytes(4,"big") + (0).to_bytes(4,"big")

def eligible_suffix(x, seed):
    return (len(x)==102 and x[:16]==seed and x[16:64]==bytes(48)
            and x[64+9] in (5,6))

def eligible_prefix(x, seed):
    return len(x)>=32 and x[16:32]==seed

S=bytes([0x52])*16
K=bytes([0x31])*16
P=bytes([0xA5])*16
root=bytes([0xF0])*16
m=b"raw message"
private_suffix=S+bytes(48)+address(5)+K
private_prefix=P+S+m
assert eligible_suffix(private_suffix,S) and not eligible_prefix(private_suffix,S)
assert eligible_prefix(private_prefix,S) and not eligible_suffix(private_prefix,S)
for typ in (0,1,2,3,4,7):
    public_addressed=S+bytes(48)+address(typ)+bytes(16)
    assert not eligible_suffix(public_addressed,S)
    assert not eligible_prefix(public_addressed,S)

# If R=P, inner hashing reaches the secret-prefix family at label root||m.
inner=P+S+root+m
assert inner==P+S+(root+m)
assert eligible_prefix(inner,S)

# Even in the deliberately eligible U=P||S case, changing the counter does
# not create new possible prefix-key values.
U=P+S
outer_points=[U+c.to_bytes(4,"big")+S for c in range(256)]
assert all(eligible_prefix(x,S) and not eligible_suffix(x,S) for x in outer_points)
assert len({x[:16] for x in outer_points})==1
assert len(set(outer_points))==256

# Degenerate public seed can destroy disjointness; charge it, do not deny it.
Z=bytes(16)
degenerate=Z+bytes(48)+address(5)+K
assert eligible_suffix(degenerate,Z) and eligible_prefix(degenerate,Z)
assert degenerate==Z+Z+degenerate[32:]

# Fixed independent coins/tables are shared across secret-key choices. The
# private analytical flag may differ, but the continued ideal transcript does
# not read the keys or flag.
def continued_ideal(y, key):
    trace=(y,(y+5)%M,(y+9)%M)
    hidden_bad=key in trace[:2]
    return trace,hidden_bad

for y in ys:
    runs=[continued_ideal(y,key) for key in range(M)]
    assert len({trace for trace,bad in runs})==1
    assert {bad for trace,bad in runs}=={False,True}

# Full hidden-point responses extend the consumed prefixes consistently. This
# is a coupling encoding control, not a SHA-256 security claim.
F_image=bytes(range(32))
J_image=bytes(reversed(range(32)))
public_image=bytes([0xEE])*32
def coupled_raw(x):
    if x==private_suffix:
        return F_image
    if x==private_prefix:
        return J_image
    return public_image

assert coupled_raw(private_suffix)[:16]==F_image[:16]
assert coupled_raw(private_suffix)==F_image
assert coupled_raw(private_prefix)==J_image
assert len(coupled_raw(private_suffix))==32
assert coupled_raw(private_suffix)!=public_image  # Divergence after a hit is allowed.

out={
 "status":"PASS_EXACT_FINITE_AND_ENCODING_CONTROLS_NOT_A_CRYPTOGRAPHIC_PROOF",
 "source_sha256":PIN,
 "unused_uniform_key_two_guess_probability":str(independent_two_guess),
 "no_hit_conditioned_next_guess_probability":str(survival_next_guess),
 "incorrect_unchanged_posterior_guess_probability":str(Fraction(1,M)),
 "one_leaked_bit_one_guess_probability":str(leaked_bit_guess),
 "nonzero_public_seed_hidden_families_disjoint_in_control":True,
 "public_addressed_families_excluded_in_control":True,
 "inner_alias_if_R_equals_P":True,
 "outer_distinct_counter_inputs":len(set(outer_points)),
 "outer_distinct_prefix_key_candidates":len({x[:16] for x in outer_points}),
 "zero_public_seed_domain_overlap_control":True,
 "continued_ideal_transcript_unchanged_across_bad_flags":True,
 "full_32_byte_hidden_images_extend_consumed_prefixes":True,
 "scope":"No signatures, cache construction, timing, source changes or remote uploads"
}
(HERE / "CONTROL-RESULTS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))

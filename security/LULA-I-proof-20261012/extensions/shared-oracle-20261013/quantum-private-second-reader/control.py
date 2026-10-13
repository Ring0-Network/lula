"""Independent exact finite controls; not actual LULA or a QROM forgery experiment."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import random

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PIN = "ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210"
assert hashlib.sha256((ROOT/"publications/LULA-I/release/code/lula1/src/lib.rs").read_bytes()).hexdigest() == PIN

# Exact full-output ordinary-RO marginal on two disjoint private families.
# Tags separate the D/M domains even when the two numerical keys coincide.
original = Counter()
programmed = Counter()
for k,p in product(range(2),repeat=2):
    for raw_table in product(range(4),repeat=5):
        original[(k,p,raw_table)] += 16  # two independent auxiliary full images
        for f,j in product(range(4),repeat=2):
            table = list(raw_table)
            table[k] = f
            table[2+p] = j
            assert table[k] == f and table[2+p] == j
            programmed[(k,p,tuple(table))] += 1
assert original == programmed
assert sum(programmed.values()) == 65536

# Exact rational amplitude-squared calculations, with an arbitrary ancilla.
# All amplitudes are integer pairs over one common square-root denominator.
N = 4
R = 4  # complete two-bit images, both bits retained
ANC = 2
points = [(tag,label,key) for tag in ("D","M") for label in range(2) for key in range(N)] + [("outside",0,0)]
rng = random.Random(202610130107)
base = [rng.randrange(R) for _ in points]
private = {(tag,label):rng.randrange(R) for tag in ("D","M") for label in range(2)}
amplitudes = []
for x in range(len(points)):
    for z in range(R):
        for anc in range(ANC):
            sign = -1 if base[x]&1 else 1
            amplitudes.append((sign*rng.randrange(-2,3),sign*rng.randrange(-2,3)))
den = sum(re*re+im*im for re,im in amplitudes)
assert den > 0

def oracle(vector,table):
    out = [(0,0)]*len(vector)
    for x,answer in enumerate(table):
        for z in range(R):
            for anc in range(ANC):
                out[(x*R+(z^answer))*ANC+anc] = vector[(x*R+z)*ANC+anc]
    return out

def norm_squared(vector):
    return sum(re*re+im*im for re,im in vector)

ideal = oracle(amplitudes,base)
eligible_numer = sum(re*re+im*im for x in range(len(points)-1)
                     for re,im in amplitudes[x*R*ANC:(x+1)*R*ANC])
eligible_mass = F(eligible_numer,den)
average_mass = F(0)
average_trace_squared = F(0)
max_local_slack = F(0)
for k,p in product(range(N),repeat=2):
    hidden = [x for x,(tag,label,key) in enumerate(points)
              if (tag=="D" and key==k) or (tag=="M" and key==p)]
    mu = F(sum(re*re+im*im for x in hidden
               for re,im in amplitudes[x*R*ANC:(x+1)*R*ANC]),den)
    patched = base[:]
    for x in hidden:
        tag,label,key = points[x]
        patched[x] = private[(tag,label)]
    real = oracle(amplitudes,patched)
    diff = [(a-c,b-d) for (a,b),(c,d) in zip(real,ideal)]
    norm_delta = F(norm_squared(diff),den)
    assert norm_delta <= 4*mu
    overlap_re = sum(a*c+b*d for (a,b),(c,d) in zip(real,ideal))
    overlap_im = sum(a*d-b*c for (a,b),(c,d) in zip(real,ideal))
    trace_squared = 1-F(overlap_re**2+overlap_im**2,den**2)
    assert 0 <= trace_squared <= norm_delta
    average_mass += mu/N**2
    average_trace_squared += trace_squared/N**2
    max_local_slack = max(max_local_slack,4*mu-norm_delta)
assert average_mass == eligible_mass/N
assert average_mass <= F(1,N)
assert average_trace_squared <= F(4,N)

# Exact product telescope and why REAL query weight cannot be substituted.
def phase(v,key):
    return [(-x if i==key else x) for i,x in enumerate(v)]

def diffuse(v):
    average = sum(v)/len(v)
    return [2*average-x for x in v]

def real_step(v,key):
    return diffuse(phase(v,key))

def ideal_step(v):
    return diffuse(v)

def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]
uniform = [F(1,2)]*N
for key in range(N):
    real1 = real_step(uniform,key)
    ideal1 = ideal_step(uniform)
    assert real1[key]**2 == 1 and ideal1[key]**2 == F(1,N)
    real2 = real_step(real1,key)
    ideal2 = ideal_step(ideal1)
    # R^2-I^2 = R(R-I) + (R-I)I, applied to the ideal initial state.
    first = real_step(sub(real_step(uniform,key),ideal_step(uniform)),key)
    second = sub(real_step(ideal1,key),ideal_step(ideal1))
    assert sub(real2,ideal2) == add(first,second)

# Classical CQ handlers can be charged by rare-branch probability. Two
# nominations among four keys have exact channel discrepancy1/2.
classical_bad = F(sum(p in {0,1} for p in range(N)),N)
assert classical_bad == F(2,N)

# Coherent phase-service counterexample to a probability-only handler charge.
# Average over an unobserved uniform marked key: rho_R-rho_I has eigenvalues
# -4(N-1)/N^2 on the uniform vector and +4/N^2 on each orthogonal vector.
coherent_average_trace = F(4*(N-1),N*N)
assert coherent_average_trace == F(3,4) > F(1,N)
per_key_trace_squared = 1-(1-F(2,N))**2
assert per_key_trace_squared == F(3,4)

# Source-format failed-posterior and complete-image contrary controls.
remaining_keys = [key for key in range(N) if key != 0]
surviving_next_guess = F(sum(key==1 for key in remaining_keys),len(remaining_keys))
assert surviving_next_guess == F(1,3) > F(1,N)
same_prefix_full_images = (0b00,0b01)
assert same_prefix_full_images[0]>>1 == same_prefix_full_images[1]>>1
assert same_prefix_full_images[0] != same_prefix_full_images[1]
# A basis XOR query distinguishes these complete images perfectly even
# though a prefix-only description would call the two replies equal.
full_image_basis_trace_distance = F(1)

# If disjointness is dropped, one overlap cannot carry two independent
# private full images unless they happen to agree.
overlap_conflict = F(sum(f!=j for f,j in product(range(R),repeat=2)),R*R)
assert overlap_conflict == F(3,4)

out={
    "outcome":"PASS_EXACT_QUANTUM_PRIVATE_HOP_CONTROLS_AND_NEGATIVE_SCOPES",
    "source_sha256":PIN,
    "full_output_programmed_RO_joint_marginal_exact":True,
    "full_output_marginal_worlds":65536,
    "keys_per_private_family":N,"output_bits":2,"ancilla_dimension":ANC,
    "raw_points":len(points),"key_pairs_checked":N*N,
    "average_hidden_query_mass_exact":str(average_mass),
    "eligible_query_mass_over_N_exact":str(eligible_mass/N),
    "average_one_query_trace_distance_squared_exact":str(average_trace_squared),
    "bound_4_over_N_for_squared_distance":str(F(4,N)),
    "product_telescope_with_ideal_prefixes_exact":True,
    "first_real_Grover_step_next_key_mass":1,
    "corresponding_ideal_key_mass":str(F(1,N)),
    "invalid_query_plus_final_literal_budget":str(F(2,N)),
    "classical_two_nomination_channel_discrepancy":str(classical_bad),
    "coherent_handler_average_trace_counterexample":str(coherent_average_trace),
    "invalid_probability_only_one_nomination_charge":str(F(1,N)),
    "real_survival_posterior_next_guess":str(surviving_next_guess),
    "invalid_survival_uniform_guess":str(F(1,N)),
    "prefix_equal_complete_image_basis_trace_distance":str(full_image_basis_trace_distance),
    "two_private_maps_at_same_raw_point_conflict_probability":str(overlap_conflict),
    "scope":"Finite exact local controls; generic marked-oracle discriminator is not an ordinary random-function source attack. No full QROM conclusion."
}
(HERE/"CHECKS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))

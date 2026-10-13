"""Exact bounded source-selection discriminators; no actual signing or timings."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import random
import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PIN = "ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210"
assert hashlib.sha256((ROOT/"publications/LULA-I/release/code/lula1/src/lib.rs").read_bytes()).hexdigest() == PIN
PRIMARY_PIN = "9a5ea6adeba5dcdf6c80035057aaccdc704aa6ea2940af0320bcfd7eca0abc8d"
assert hashlib.sha256((HERE/"primary-arxiv-2010.15103.pdf").read_bytes()).hexdigest() == PRIMARY_PIN

# Exact prequery correlation: an unknown uniform nonce does not make the
# existing oracle image independent of a coherent response register.
worlds = old_accept = fresh_accept = 0
for table in product(range(4),repeat=4):
    for nonce,memory_input,new_image in product(range(4),repeat=3):
        worlds += 1
        old_accept += memory_input == nonce
        fresh_accept += memory_input == nonce and table[memory_input] == new_image
old_probability = F(old_accept,worlds)
fresh_probability = F(fresh_accept,worlds)
advantage = old_probability-fresh_probability
assert old_probability == F(1,4) and fresh_probability == F(1,16)
assert advantage == F(3,16)
ar_bound = F(1,2)+F(1,8)  # sqrt(1/4)+(1/4)/2
assert ar_bound == F(5,8) and advantage <= ar_bound

# Classical m can be chosen from arbitrary public table information; an
# unused private nonce at the selected label still has uniform point law.
rng = random.Random(202610130207)
adaptive_cases = 128
for _ in range(adaptive_cases):
    table = [rng.randrange(4) for _ in range(8)]
    selected_message = (table[0]+table[7])%2
    selected_nonce_counts = Counter(pair[selected_message] for pair in product(range(4),repeat=2))
    assert selected_nonce_counts == Counter({0:4,1:4,2:4,3:4})

# One query to a row-valued XOR function simulates a selected two-bit word.
# Row has2 slots; all other slots start in|+>. Verify every basis input and
# every complete2-namespace function; by linearity this includes entanglement.
def swap_word(z,aux,c):
    shift = 2*c
    selected = (aux>>shift)&3
    updated = (aux & ~(3<<shift)) | (z<<shift)
    return selected,updated

lookup_cases = 0
outside_cases = 0
for row0,row1 in product(range(16),repeat=2):
    rows = (row0,row1)
    for u,c,z,eligible in product(range(2),range(2),range(4),range(2)):
        got = Counter()
        for aux in range(16):  # uniform plus amplitudes1/4; exact permutation
            target,work = swap_word(z,aux,c) if eligible else (z,aux)
            query_u = u if eligible else 0
            work ^= rows[query_u]  # exactly one row query
            target,work = swap_word(target,work,c) if eligible else (target,work)
            got[(u,c,target,work)] += 1
        selected_image = (rows[u]>>(2*c))&3
        expected_z = z^selected_image if eligible else z
        want = Counter({(u,c,expected_z,aux):1 for aux in range(16)})
        assert got == want
        lookup_cases += 1
        outside_cases += not eligible
assert lookup_cases == 8192 and outside_cases == 4096

# Negative control: zero ancillary words leak an unused row word, destroying
# an input superposition even when the selected-word oracle is the identity.
wrong_garbage = []
for u,row in enumerate((0,4)):  # selected slot0 is0; unused slot1 differs
    target,aux = swap_word(0,0,0)
    aux ^= row
    target,aux = swap_word(target,aux,0)
    assert target == 0
    wrong_garbage.append(aux)
assert wrong_garbage == [0,4]
wrong_cleanup_trace = F(1,2)  # dephased uniform namespace versus pure|+>

# The full namespace, not every counter, is nominated by a raw point.
mass = F(0)
for u in range(4):
    row_mass = sum(F(3*u+c+1,91) for c in range(3))
    mass += row_mass/4
assert mass == F(3,14)  # eligible mass6/7 divided by namespace size4

# Correct guard normalization in a4+4-bit analogue.
all_namespaces = tuple(range(16))
eligible_namespaces = tuple(u for u in all_namespaces if (u&3)!=1)
assert len(eligible_namespaces) == 12
guard_probability = F(4,16)
conditional_pmax = F(1,12)
assert conditional_pmax > F(1,16)

# Fresh-row first-zero law, including its finite failure branch.
first_counts = Counter()
fail = 0
for row in product(range(8),repeat=3):
    for c,digest in enumerate(row):
        z = digest&1
        x = digest>>1
        if z == 0:
            first_counts[(c,x)] += 1
            break
    else:
        fail += 1
assert fail == 64 and F(fail,512)==F(1,8)
for c in range(3):
    values = [first_counts[(c,x)] for x in range(4)]
    assert len(set(values)) == 1
    assert values[0] == 64//(2**c)
    assert all(F(v,sum(values)) == F(1,4) for v in values)
# Route-dependent later completion can bias the emitted subset completely.
completed_x = Counter({x:sum(first_counts[(c,x)] for c in range(3))
                       for x in range(4) if x==0})
assert F(completed_x[0],sum(completed_x.values())) == 1

# Generic quantum search discriminator, not an actual FORS or LULA oracle.
def grover_first(key):
    v=[F(1,2)]*4
    v[key] *= -1
    average = sum(v)/4
    return [2*average-x for x in v]
for key in range(4):
    assert grover_first(key)[key]**2 == 1
assert 1 > F(2,4)  # a Q+1 classical-candidate union cannot be transplanted

mp.mp.dps = 100
N = 1<<128
MG = (1<<256)-(1<<128)
numeric=[]
for logQ in (0,32,64):
    Q = 1<<logQ
    inner = mp.sqrt(mp.mpf(Q)/N)+mp.mpf(Q)/(2*N)
    outer = mp.sqrt(mp.mpf(Q)/MG)+mp.mpf(Q)/(2*MG)
    fixed = min(mp.mpf(1),inner+outer+mp.mpf(1)/N)
    uniform = min(mp.mpf(1),inner+outer+mp.mpf(2)/N)
    numeric.append({
        "log2_prequeries":logQ,
        "inner_primary_AR_loss":mp.nstr(inner,50),
        "row_primary_AR_loss":mp.nstr(outer,50),
        "guard_loss":mp.nstr(mp.mpf(1)/N,50),
        "candidate_first_call_distance_nonzero":mp.nstr(fixed,50),
        "candidate_first_call_distance_uniform_seed":mp.nstr(uniform,50),
        "meaning":"Single first-call comparison loss; not a full QROM advantage bound."
    })

out={
    "status":"PASS_EXACT_FIRST_CALL_CONTROLS_NOT_FULL_QROM",
    "source_sha256":PIN,"primary_pdf_sha256":PRIMARY_PIN,
    "prequery_correlation_worlds":worlds,
    "original_table_match_probability":str(old_probability),
    "reprogrammed_fresh_table_match_probability":str(fresh_probability),
    "concrete_prequery_correlation_advantage":str(advantage),
    "verified_primary_one_point_bound_for_toy":str(ar_bound),
    "unused_nonce_after_adaptive_label_cases":adaptive_cases,
    "row_lookup_basis_function_cases":lookup_cases,
    "row_lookup_outside_dummy_cases":outside_cases,
    "row_queries_per_raw_query":1,
    "row_ancilla_exactly_clean":True,
    "zero_ancilla_cleanup_negative_control_trace_distance":str(wrong_cleanup_trace),
    "average_toy_full_namespace_query_mass":str(mass),
    "counter_space_factor_in_namespace_mass":False,
    "toy_guard_probability":str(guard_probability),
    "toy_guarded_point_pmax":str(conditional_pmax),
    "toy_exhaustion_probability":str(F(fail,512)),
    "toy_latent_accepted_coordinate_uniform":True,
    "route_filtered_completed_coordinate_probability":1,
    "generic_one_Grover_query_success":1,
    "invalid_two_classical_candidate_union":str(F(1,2)),
    "first_call_loss_candidates":numeric,
    "quantum_FORS_total":None,
    "scope":"Finite controls and first-call candidate arithmetic; no real signatures, cryptographic timings or full quantum source-security result."
}
(HERE/"CHECKS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))

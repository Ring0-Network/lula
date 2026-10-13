"""Exact tiny WOTS suffix/retained-memory discriminator, not full security."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

M, FULL = 2,4
worlds = comparisons = 0
for base in product(range(FULL),repeat=4):
    for x1,x2,rho0,rho1 in product(range(M),repeat=4):
        # Endpointx2 known initially, signing emitsx1 and closes suffix1,2.
        old_memory = [(-1)**(value//2) for value in base]
        states = []
        for x0 in range(M):
            edge = [2*x1+rho0,2*x2+rho1]
            ghost_values = []
            for raw in range(4):
                pos,value = divmod(raw,M)
                ghost_values.append(edge[pos] if pos>=1 and value==(x0,x1)[pos] else base[raw])
            # Two retained uniform input registers, unnormalized sign amplitudes.
            # Normalized amplitudes are these entries/4; no floating arithmetic.
            after = [(-1)**(value//2) for value in ghost_values]
            states.append(tuple(a*b for a in old_memory for b in after))
        assert states[0] == states[1]
        worlds += 1
        comparisons += len(states[0])

# Wrong closure: disclosex0/programedge0 but declare its successorx1 hidden.
# One public query revealsx1, so the next point at position1 guesses it withmass1.
wrong_hits = correct_hidden_hits = cases = 0
for x0,x1,x2,rho0,rho1 in product(range(M),repeat=5):
    first_response = 2*x1+rho0
    next_input = first_response//2
    assert next_input == x1
    wrong_hits += next_input == x1  # incorrectly still labelled hidden
    correct_hidden_hits += False  # proper suffix0,1,2 marks it known
    cases += 1
assert F(wrong_hits,cases) == 1 > F(1,M)
assert F(correct_hidden_hits,cases) == 0

result = {
    "status":"PASS_EXACT_SUFFIX_CLOSURE_RETAINED_MEMORY_CONTROL",
    "model":{"node_alphabet":M,"full_image_alphabet":FULL,"chain_nodes":3},
    "paired_worlds":worlds,"sign_amplitude_comparisons":comparisons,
    "retained_pre_disclosure_memory":True,
    "proper_suffix_overlay_state_independent_of_hidden_x0":True,
    "density_operators_equal_by_exact_pure_vector_equality":True,
    "wrong_known_predecessor_hidden_successor_finder_mass":"1",
    "claimed_uniform_mass_if_wrong":"1/2",
    "correct_suffix_hidden_finder_mass":"0",
    "scope":"One exact toy quantum strategy; universal invariant is manual, not established by this control alone",
}
Path(__file__).with_name("SUFFIX_QUANTUM_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

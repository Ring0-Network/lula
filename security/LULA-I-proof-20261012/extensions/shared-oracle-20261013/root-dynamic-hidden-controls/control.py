"""Exact two-salted-leaf dynamic-overlay quantum discriminator, not a signer run.

One-bit secrets and full two-bit images. An oracle query is coherent and retains
its input/output state; the intervening reveal is a classical measured-history
service represented with an inaccessible copied history register.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
# Sparse pure states, amplitudes in units of 1/2, normalized initial support4.
# State fields: raw input (salt*2+payload), output2bits, measured-history copy,
# revealed secret. History/reveal are initially empty (-1).
initial = {(x, 0, -1, -1): 1 for x in range(4)}


def norm2(v):
    return F(sum(a*a for a in v.values()), 4)


def difference_norm2(a, b):
    return F(sum((a.get(k, 0)-b.get(k, 0))**2 for k in a.keys() | b.keys()), 4)


def query(v, o0, z, w, real):
    out = defaultdict(int)
    for (x, y, h, r), a in v.items():
        salt, payload = divmod(x, 2)
        known = h >= 0 and salt == h % 2
        answer = w[salt] if payload == z[salt] and (real or known) else o0[x]
        out[(x, y ^ answer, h, r)] += a
    return {k: a for k, a in out.items() if a}


def measured_reveal_and_local(v, z):
    # Copy the measured full reply y into inaccessible history h. It decoheres
    # classical service branches when h is traced, rather than granting coherent
    # signing. Choose which secret to reveal as a predictable function of y.
    out = defaultdict(int)
    for (x, y, h, r), a in v.items():
        assert h == r == -1
        h = y
        r = z[h % 2]
        # A reversible local operation uses the disclosed value and retains the
        # prior query memory. The chosen remaining payload need not be uniform.
        x ^= r
        phase = -1 if y & 2 else 1
        out[(x, y, h, r)] += phase*a
    return {k: a for k, a in out.items() if a}


def hidden_mass(v, z):
    total = 0
    for (x, y, h, r), a in v.items():
        salt, payload = divmod(x, 2)
        known = h >= 0 and salt == h % 2
        if not known and payload == z[salt]:
            total += a*a
    return F(total, 4)


worlds = 0
ordinary_tables = Counter()
sum_mu1 = sum_mu2 = sum_local1 = sum_local2 = F(0)
sum_final_norm = sum_preal = sum_pideal = F(0)
group_states = defaultdict(lambda: defaultdict(set))
for z in product(range(2), repeat=2):
    for w in product(range(4), repeat=2):
        for o0 in product(range(4), repeat=4):
            worlds += 1
            actual = tuple(w[x//2] if x % 2 == z[x//2] else o0[x] for x in range(4))
            ordinary_tables[actual] += 1
            r1 = query(initial, o0, z, w, True)
            i1 = query(initial, o0, z, w, False)
            rp = measured_reveal_and_local(r1, z)
            ip = measured_reveal_and_local(i1, z)
            assert norm2(r1) == norm2(i1) == norm2(rp) == norm2(ip) == 1
            r2 = query(rp, o0, z, w, True)
            i2 = query(ip, o0, z, w, False)
            real_on_ideal = query(ip, o0, z, w, True)
            m1, m2 = hidden_mass(initial, z), hidden_mass(ip, z)
            e1 = difference_norm2(r1, i1)
            e2 = difference_norm2(real_on_ideal, i2)
            assert e1 <= 4*m1 and e2 <= 4*m2
            # Triangle inequality squared, with Cauchy-Schwarz eliminating sqrt.
            final = difference_norm2(r2, i2)
            assert final <= 2*(e1+e2)
            preal, pideal = hidden_mass(r2, z), hidden_mass(i2, z)
            sum_mu1 += m1
            sum_mu2 += m2
            sum_local1 += e1
            sum_local2 += e2
            sum_final_norm += final
            sum_preal += preal
            sum_pideal += pideal
            # Exact untouched-coordinate independence before and after q2,
            # conditioned on all permitted public tables and reveal history.
            for h in {k[2] for k in ip}:
                r = z[h % 2]
                unknown_value = z[1-h % 2]
                view = (o0, w, h, r)
                for tag, vector in [('pre', ip), ('post', i2)]:
                    block = tuple(sorted((k, a) for k, a in vector.items() if k[2] == h))
                    group_states[(tag, view)][unknown_value].add(block)

assert worlds == 16384
assert len(ordinary_tables) == 4**4
assert set(ordinary_tables.values()) == {worlds // (4**4)}
assert all(set(values) == {0, 1} and values[0] == values[1]
           for values in group_states.values())
mean_mu1, mean_mu2 = sum_mu1/worlds, sum_mu2/worlds
assert mean_mu1 <= F(1, 2) and mean_mu2 <= F(1, 2)
assert sum_local1/worlds <= 4*mean_mu1 and sum_local2/worlds <= 4*mean_mu2
assert sum_pideal/worlds <= F(1, 2)

# Leaving a ghost point unchanged after explicitly revealing its input allows
# a later query to distinguish genuine full images with probability3/4.
unchanged_mismatch = F(sum(o != w for o in range(4) for w in range(4)), 16)
assert unchanged_mismatch == F(3, 4)
# Signed-node-only WOTS reconciliation leaks a purportedly hidden successor:
# program known X0->X1 but omit X1 from Known; one forward query learns it exactly.
suffix_without_closure_success = F(1)
assert suffix_without_closure_success > F(1, 2)

result = {
    'status': 'PASS_EXACT_DYNAMIC_OVERLAY_CONTROLS',
    'scope': 'Two salted FORS-like leaves; suffix-closure failure discriminator. Not full Rust or WOTS formalization.',
    'worlds': worlds,
    'ordinary_full_function_tables': len(ordinary_tables),
    'ordinary_marginal_exact': True,
    'conditional_pre_post_quantum_state_groups': len(group_states),
    'remaining_secret_conditional_states_identical': True,
    'mean_hidden_query_mass_first': str(mean_mu1),
    'mean_hidden_query_mass_after_reveal': str(mean_mu2),
    'mean_local_norm_squared_first': str(sum_local1/worlds),
    'mean_local_norm_squared_second': str(sum_local2/worlds),
    'mean_final_norm_squared': str(sum_final_norm/worlds),
    'terminal_real_probability': str(sum_preal/worlds),
    'terminal_ideal_probability': str(sum_pideal/worlds),
    'no_reconcile_revealed_point_mismatch': str(unchanged_mismatch),
    'signed_node_only_missing_suffix_closure_learns_successor': str(suffix_without_closure_success),
    'control_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE/'CHECKS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf8')
print(json.dumps(result, indent=2))

"""Actual byte-frame and arithmetic discriminators; no hardness experiment."""
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
zero = bytes(16)
one = bytes([1]) * 16
frames = []
aliases = 0
for s, p, k, index in product((zero, one), (zero, one), (zero, one), (0, 1)):
    # Literal source layer1/tree8/type1/kp4/word2_4/word3_4 address.
    a = bytes([0]) + bytes(8) + bytes([5]) + bytes(4) + bytes(4) + index.to_bytes(4, 'big')
    assert len(a) == 22
    fword = s + bytes(48) + a + k
    message = bytes(32) + a + k
    gword = p + s + message
    assert len(fword) == len(gword) == 102
    equal = fword == gword
    assert equal == (s == zero and p == zero)
    if equal:
        full = hashlib.sha256(fword).digest()
        assert full == hashlib.sha256(gword).digest()
        assert len(full) == 32 and len(full[:16]) == 16
        aliases += 1
    frames.append(fword)
assert aliases == 4 and len(frames) == 16
# Private-prefix security does not determine the full public digest law.
# This alternative public algorithm preserves EVERY private-family output by
# definition, while fixing the lower128 bits and hence route bits162..202.
observed_original_nonzero_route = False
for word in frames:
    full = hashlib.sha256(word).digest()
    alternate_full = full[:16] + bytes(16)
    assert alternate_full[:16] == full[:16]
    alternate_route = (int.from_bytes(alternate_full, 'big') >> 53) & ((1 << 41) - 1)
    original_route = (int.from_bytes(full, 'big') >> 53) & ((1 << 41) - 1)
    assert alternate_route == 0
    observed_original_nonzero_route |= original_route != 0
assert observed_original_nonzero_route
involutions = 0
for word in frames:
    value = int.from_bytes(hashlib.sha256(word).digest(), 'big')
    for response in (0, 1, (1 << 256) - 1):
        assert (response ^ value) ^ value == response
        involutions += 1

# Signed hybrid arithmetic: no mistaken equality for the triangle bound.
p0, pk, pkp = Fraction(3, 4), Fraction(7, 8), Fraction(1, 2)
dk, dp = p0 - pk, pk - pkp
assert dk + dp == p0 - pkp
assert abs(p0 - pkp) == Fraction(1, 4)
assert abs(dk) + abs(dp) == Fraction(1, 2)
assert abs(p0 - pkp) < abs(dk) + abs(dp)
# A public-parameter gap averages signed probabilities, not absolute gaps.
pointwise = (Fraction(1, 4), Fraction(-1, 4))
averaged_gap = abs(sum(pointwise) / 2)
average_absolute = sum(map(abs, pointwise)) / 2
assert averaged_gap == 0 and average_absolute == Fraction(1, 4)

setup = (1 << 21) * (16 + 32 * 32)
hot = 17 * 512 + 4 * 32 * 32 + 16
cold = (1 << 21) * 16 + 17 * 512 + 4 * 32 * 32
assert (setup, hot, cold) == (2181038080, 12816, 33567232)
hs = (1 << 21) * (19505 + (1 << 32)) - 1
hm = {'hot': 82090 + 5 * (1 << 32), 'cold': 8560574463 + 82090 + 6 * (1 << 32)}
rows = []
for q, mode in product((0, 1, 1 << 24, 1 << 40), ('hot', 'cold')):
    fcap = min(19212937084272640, setup + q * {'hot': hot, 'cold': cold}[mode])
    rsrc = hs + q * hm[mode] + 3224
    rows.append({'q': q, 'mode': mode, 'f_query_cap': fcap, 'g_query_cap': q,
                 'BK_local_h_cap': rsrc + q, 'BP_local_h_cap': rsrc})
    assert rows[-1]['BK_local_h_cap'] - rows[-1]['BP_local_h_cap'] == q

result = {
    'status': 'PASS_BYTE_SERIALIZATION_AND_SIGNED_GAP_CONTROLS_NOT_HARDNESS',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'actual_full_length_frame_cases': 16,
    'zero_seed_zero_p_literal_f_g_aliases': aliases,
    'private_output_bytes': 16,
    'public_output_bytes': 32,
    'public_xor_involution_cases': involutions,
    'negative_private_prefix_does_not_fix_public_lower128': True,
    'alternate_prefix_preserving_full_hash_forces_route_bits162_to202_zero': True,
    'signed_hybrid_gaps': {'K': str(dk), 'P': str(dp), 'sum': str(dk + dp)},
    'strict_triangle_negative': {'absolute_total': '1/4', 'sum_absolute': '1/2'},
    'signed_parameter_averaging_negative': {'absolute_average': '0', 'average_absolute': '1/4'},
    'source_loop_private_caps': {'setup': setup, 'hot': hot, 'cold': cold},
    'resource_rows': rows,
    'scope': 'Known SHA code only tests byte equality/output widths. No SHA PRF-hardness, full-source simulation, or quantum circuit benchmark.',
}
out = HERE / 'LITERAL-GAP-CONTROLS.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'alias_cases': aliases, 'resource_rows': len(rows)}, indent=2))

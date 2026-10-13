"""Abstract finite endpoint/one-query controls; no source hash or attack."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parent
keys, addresses, alphabet = 2, 2, 4
actual = Counter()
completion = Counter()
zero = Counter()
for raw in product(range(alphabet), repeat=keys * addresses):
    for key in range(keys):
        service = tuple(raw[a * keys + key] for a in range(addresses))
        actual[(raw, service)] += 1
    for service in product(range(alphabet), repeat=addresses):
        zero[(raw, service)] += 1
        for key in range(keys):
            changed = list(raw)
            for a in range(addresses):
                changed[a * keys + key] = service[a]
            completion[(tuple(changed), service)] += 1
actual_worlds = sum(actual.values())
completion_worlds = sum(completion.values())
assert set(actual) == set(completion)
assert all(Fraction(actual[k], actual_worlds) ==
           Fraction(completion[k], completion_worlds) for k in actual)
assert len(zero) == alphabet ** (keys * addresses + addresses)
assert set(zero.values()) == {1}

# H X^b H scratch has exactly the diagonal phase (-1)^(b*d).
# Verify every full-response Fourier column, with scratch clean afterwards.
phase_columns = 0
for width in (1, 2, 3):
    word_size = 1 << width
    for r0, r1, z, bit in product(range(word_size), range(word_size),
                                 range(word_size), (0, 1)):
        d = (z & (r0 ^ r1)).bit_count() % 2
        out = {}
        for final_scratch in (0, 1):
            coefficient = sum(Fraction((-1) ** (d*t + (t ^ bit)*final_scratch), 2)
                              for t in (0, 1))
            out[final_scratch] = coefficient
        assert out[d] == (-1) ** (bit * d)
        assert out[d ^ 1] == 0
        phase = (-1) ** ((z & r0).bit_count() % 2) * out[d]
        wanted = (-1) ** ((z & (r1 if bit else r0)).bit_count() % 2)
        assert phase == wanted
        phase_columns += 1

S = bytes(range(1, 17))
P = bytes(range(16))
root = bytes(reversed(range(16)))
adrs = bytes(9) + bytes([5]) + bytes(12)
def private_word(k):
    return S + bytes(48) + adrs + k
def is_private_word(word):
    return len(word) == 102 and word[:16] == S and word[16:64] == bytes(48) and word[73] in (5, 6)
domain_checks = 0
for message in (b'', bytes(70), private_word(P), S * 8):
    assert not is_private_word(P + S + message)
    assert not is_private_word(P + S + root + message)
    domain_checks += 2
assert is_private_word(private_word(P))
assert not is_private_word(bytes(32) + bytes(4) + S)
domain_checks += 2
for kind in range(8):
    candidate = S + bytes(48) + bytes(9) + bytes([kind]) + bytes(12) + P
    assert is_private_word(candidate) == (kind in (5, 6))
    domain_checks += 1

# Finite arithmetic checks only: exact bounds and denominator guard.
bound_checks = 0
for N in (8, 16, 32, 64, 128, 256):
    for Q in range(10):
        d2 = 4 * Q * Q
        if d2 < N:
            centered = Fraction(d2, N - d2)
            assert centered >= 0
            if Q == 0:
                assert centered == 0
            assert min(Fraction(1), centered) <= 1
        else:
            # No negative-denominator expression used.
            assert d2 >= N
        bound_checks += 1

result = {
    'classification': 'COMPUTED_ABSTRACT_FINITE_CONTROLS_NOT_SOURCE_OR_ATTACK',
    'real_raw_private_endpoint_cells': len(actual),
    'actual_worlds': actual_worlds,
    'overlay_worlds': completion_worlds,
    'zero_endpoint_independent_cells': len(zero),
    'one_boolean_query_full_response_fourier_columns': phase_columns,
    'source_byte_domain_checks': domain_checks,
    'rational_bound_guard_checks': bound_checks,
    'eager_crypto_size_tables_generated': False,
    'source_calls_or_forgery_runs': 0,
    'new_source_game_declarations': 0,
    'whole_goal_complete': False,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'exit_code': 0,
}
(base / 'FINITE-CONTROLS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result))

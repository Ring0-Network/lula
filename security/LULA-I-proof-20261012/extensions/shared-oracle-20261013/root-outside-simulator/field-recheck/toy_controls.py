"""Independent exact small-field controls; standard library only, no bytecode.

These check concrete arithmetic/moment mechanisms, not the protocol call graph.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import hashlib
import json
from pathlib import Path


def mul(x, y, n):
    if n == 1:
        return x & y
    h = n // 2
    mask = (1 << h) - 1
    x0, x1, y0, y1 = x & mask, x >> h, y & mask, y >> h
    p = mul(x0, y0, h)
    q = mul(x1, y1, h)
    r = mul(x0 ^ x1, y0 ^ y1, h)
    # Known trace-one a_h is the highest tensor-basis monomial.
    aq = mul(1 << (h - 1), q, h)
    return (p ^ aq) | ((r ^ p) << h)


def power(x, e, n):
    r = 1
    while e:
        if e & 1:
            r = mul(r, x, n)
        x = mul(x, x, n)
        e >>= 1
    return r


def trace(x, n):
    out = 0
    for _ in range(n):
        out ^= x
        x = mul(x, x, n)
    return out


def binary_mod(x, p):
    while x.bit_length() >= p.bit_length():
        x ^= p << (x.bit_length() - p.bit_length())
    return x


def binary_gcd(x, y):
    while y:
        x, y = y, binary_mod(x, y)
    return x


def binary_square_mod(x, p):
    out = 0
    for i in range(x.bit_length()):
        if (x >> i) & 1:
            out ^= 1 << (2 * i)
    return binary_mod(out, p)


def conjugate_modulus(n):
    z = 1 << (n // 2)
    coeffs = [1]
    conjugates = []
    for _ in range(n):
        conjugates.append(z)
        nxt = [0] * (len(coeffs) + 1)
        for j, c in enumerate(coeffs):
            nxt[j] ^= mul(c, z, n)
            nxt[j + 1] ^= c
        coeffs = nxt
        z = mul(z, z, n)
    assert len(set(conjugates)) == n
    assert set(coeffs) <= {0, 1}
    p = sum(c << j for j, c in enumerate(coeffs))
    # Independent polynomial-basis Rabin check for power-of-two degree.
    x = 2
    halfway = None
    for j in range(1, n + 1):
        x = binary_square_mod(x, p)
        if j == n // 2:
            halfway = x
    assert x == 2
    assert binary_gcd(halfway ^ 2, p) == 1
    return hex(p)


def polynomial(coeffs, x, n):
    r = 0
    for c in reversed(coeffs):
        r = mul(r, x, n) ^ c
    return r


def phase_density(bit_tables):
    counts = Counter(bit_tables)
    total = sum(counts.values())
    return [
        [sum(Fraction(count * (-1 if row[i] ^ row[j] else 1), 4 * total)
             for row, count in counts.items()) for j in range(4)]
        for i in range(4)
    ]


def main():
    checks = {}
    for n in (1, 2, 4):
        size = 1 << n
        for x, y, z in product(range(size), repeat=3):
            assert mul(mul(x, y, n), z, n) == mul(x, mul(y, z, n), n)
            assert mul(x, y ^ z, n) == mul(x, y, n) ^ mul(x, z, n)
        checks[f'exhaustive_associativity_distributivity_degree_{n}'] = size ** 3
    n = 8
    for x, y in product(range(1 << n), repeat=2):
        assert mul(x, y, n) == mul(y, x, n)
        assert (mul(x, y, n) == 0) == (x == 0 or y == 0)
    checks['degree_8_exhaustive_pairs_no_zero_divisors'] = 65536
    for n in (1, 2, 4, 8, 16):
        assert trace(1 << (n - 1), n) == 1
        for x in (0, 1, 1 << (n - 1), (1 << n) - 1):
            assert power(x, 1 << n, n) == x
        checks[f'trace_one_and_frobenius_degree_{n}'] = True
    checks['independent_binary_irreducibility_moduli'] = {
        str(n): conjugate_modulus(n) for n in (2, 4, 8, 16)
    }
    sentinel_codes = {1}
    peer_codes = {0}
    for length in (1, 2):
        offset = sum(256 ** j for j in range(length))
        sentinel_codes.update((1 << (8 * length)) + v for v in range(256 ** length))
        peer_codes.update(offset + v for v in range(256 ** length))
    assert len(sentinel_codes) == len(peer_codes) == 65793
    checks['all_length_le_2_byte_encodings_unique'] = 65793
    assert int.from_bytes(b'', 'big') == int.from_bytes(b'\x00', 'big')
    checks['negative_bare_integer_encoding_aliases_empty_and_zero'] = True

    # One-bit version of patched XOR routing with an inactive |+> response.
    # Equal coefficients suffice here: no irrational amplitudes are needed.
    for patched, base, prescribed, response in product(range(2), repeat=4):
        actual = Counter()
        for auxiliary in range(2):
            data, spare = response, auxiliary
            if patched:
                data, spare = spare, data
            data ^= base  # The sole black-box XOR call.
            if patched:
                data, spare = spare, data
                data ^= prescribed
            actual[(data, spare)] += 1
        wanted = Counter({(response ^ (prescribed if patched else base), t): 1
                          for t in range(2)})
        assert actual == wanted
    checks['one_query_inactive_plus_patch_routing'] = True

    pair_family = [tuple(polynomial(cs, x, 2) for x in range(4))
                   for cs in product(range(4), repeat=2)]
    for x in range(4):
        for y in range(x + 1, 4):
            counts = Counter((row[x], row[y]) for row in pair_family)
            assert len(counts) == 16 and set(counts.values()) == {1}
    full_family = [tuple(polynomial(cs, x, 2) for x in range(4))
                   for cs in product(range(4), repeat=4)]
    assert len(Counter(full_family)) == 256
    counts = Counter(tuple(v & 1 for v in row) for row in full_family)
    assert len(counts) == 16 and set(counts.values()) == {16}
    checks['exhaustive_vandermonde_and_balanced_projection'] = True

    pair_bits = [tuple(v & 1 for v in row) for row in pair_family]
    full_bits = [tuple(v & 1 for v in row) for row in full_family]
    rf_bits = list(product(range(2), repeat=4))
    rho_pair, rho_rf = phase_density(pair_bits), phase_density(rf_bits)
    assert rho_pair == rho_rf
    assert rho_rf == [[Fraction(i == j, 4) for j in range(4)] for i in range(4)]
    checks['one_phase_query_exact_density_matches_rf'] = True
    # Three honest basis calls plus one adversary basis call reveal all four bits.
    # Sizing k=2 from adversary q=1 alone makes their XOR deterministically zero.
    even = lambda row: (sum(row) % 2) == 0
    wrong = Fraction(sum(map(even, pair_bits)), len(pair_bits))
    right = Fraction(sum(map(even, full_bits)), len(full_bits))
    random = Fraction(sum(map(even, rf_bits)), len(rf_bits))
    assert wrong == 1 and right == random == Fraction(1, 2)
    checks['negative_ignore_honest_calls_parity_success'] = str(wrong)
    checks['correct_saturated_total_query_family_parity_success'] = str(right)
    checks['random_function_parity_success'] = str(random)
    # T=4 implies k=min(2T,|D|)=4 on this toy domain: full-family case above.
    checks['scope'] = 'Small-field controls only; no protocol call-cap audit or quantum runtime benchmark.'
    checks['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out = Path(__file__).with_name('toy-results.json')
    out.write_text(json.dumps({'status': 'PASS', 'checks': checks}, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'results': str(out), 'checks': checks}, indent=2))


if __name__ == '__main__':
    main()

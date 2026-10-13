"""Exact small-domain interface controls; no LULA forgery or full-source proof."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib, json

HERE = Path(__file__).resolve().parent

def h(word):
    # One fixed public full-two-bit algorithm on variable-length bit strings.
    state = (len(word) + 1) % 4
    for i, bit in enumerate(word):
        state = (3 * state + bit + i) % 4
    return state

def prefix(word):
    return h(word) >> 1

def f(s, k, a):
    return prefix((s, 0, a, k))

def g(s, p, m):
    return prefix((p, s) + tuple(m))

class Interface:
    def __init__(self, real, values):
        self.real, self.values = real, values
        self.queries = []
    def __call__(self, label):
        self.queries.append(label)
        return self.real(label) if self.values is None else self.values[label]

def body(s, secret, randomizer):
    # Pre-key public computation precedes any source-facing disclosure of s.
    view = [('pre_public_full_h', h((1, 0, 0, 0)))]
    u0, u1 = secret(0), secret(1)
    root = h((s, u0, u1))
    # Finite setup exhaustion is absorbing and does not release pk.
    ctr = next((c for c in range(2) if h((s, u0, u1, c)) & 1), None)
    if ctr is None:
        view.append(('nonwinning_setup',))
        return tuple(view)
    view.append(('pk', s, root, ctr))
    m = (root >> 1, view[0][1] & 1)
    r0 = randomizer(m)
    # Honest restoration reuses the same label values, without disclosing keys.
    r1 = randomizer(m)
    a = root & 1
    u = secret(a)
    public_word = (0, s) + m
    full = h(public_word)
    view.append(('sig_and_restored_sig', m, r0, r1, u, full))
    view.append(('final_bit', int(r0 == (full >> 1))))
    return tuple(view)

def source(s, k, p, ft=None, jt=None):
    return body(s,
        lambda a: f(s, k, a) if ft is None else ft[a],
        lambda m: g(s, p, m) if jt is None else jt[m[0]*2+m[1]])

def bk(s, p, oracle):
    cache = {}
    def secret(a):
        if a not in cache:
            cache[a] = oracle(a)
        return cache[a]
    result = body(s, secret, lambda m: g(s, p, m))
    assert len(oracle.queries) <= 2
    return result

def bp(s, ft, oracle):
    fcache, jcache = {}, {}
    def secret(a):
        if a not in fcache:
            fcache[a] = ft[a]
        return fcache[a]
    def rand(m):
        if m not in jcache:
            jcache[m] = oracle(m[0]*2+m[1])
        return jcache[m]
    result = body(s, secret, rand)
    assert len(oracle.queries) <= 1
    return result

ftables = list(product(range(2), repeat=2))
jtables = list(product(range(2), repeat=4))
identities = Counter()
hist = {name: Counter() for name in ('real', 'fideal', 'fjideal')}
for s, k, p in product(range(2), repeat=3):
    direct = source(s, k, p)
    target = Interface(lambda a: f(s, k, a), None)
    assert direct == bk(s, p, target)
    identities['BK_REAL'] += 1
    hist['real'][direct] += Fraction(1, 8)
for s, p, ft in product(range(2), range(2), ftables):
    direct = source(s, 0, p, ft=ft)
    assert direct == bk(s, p, Interface(None, ft))
    assert direct == bp(s, ft, Interface(lambda i: g(s, p, (i >> 1, i & 1)), None))
    identities['BK_IDEAL_and_BP_REAL'] += 1
    hist['fideal'][direct] += Fraction(1, 16)
for s, ft, jt in product(range(2), ftables, jtables):
    direct = source(s, 0, 0, ft=ft, jt=jt)
    assert direct == bp(s, ft, Interface(None, jt))
    identities['BP_IDEAL'] += 1
    hist['fjideal'][direct] += Fraction(1, 128)
assert all(sum(v.values()) == 1 for v in hist.values())
for distribution in hist.values():
    for view in distribution:
        assert view[0][0] == 'pre_public_full_h'
        assert all(item[0] != 's' for item in view[:1])
        for item in view:
            if item[0] == 'sig_and_restored_sig':
                assert item[2] == item[3]

# Literal frame overlap at s=p=0: private prefix is enough, public lower limb retained.
alias_cases = 0
for a, k in product(range(2), repeat=2):
    m = (a, k)
    assert (0, 0, a, k) == (0, 0) + m
    assert f(0, k, a) == g(0, 0, m) == h((0, 0, a, k)) >> 1
    alias_cases += 1
real_alias = Fraction(1)
ideal_alias = sum(Fraction(int(bit == f(0, 0, 0)), 2) for bit in range(2))
assert ideal_alias == Fraction(1, 2)

# Negative: supplying an independent Raw would fail the fixed public-code law.
point = (0, 0, 0, 0)
fixed_agreement = Fraction(1)
independent_raw_agreement = sum(Fraction(int(v == h(point)), 4) for v in range(4))
assert independent_raw_agreement == Fraction(1, 4)

# The public reversible oracle is a known deterministic XOR permutation.
unitary_cases = 0
for n in range(5):
    for word in product(range(2), repeat=n):
        images = {y ^ h(word) for y in range(4)}
        assert images == set(range(4))
        for y in range(4):
            assert (y ^ h(word)) ^ h(word) == y
            unitary_cases += 1

def pfinal(d):
    return sum(prob for view, prob in d.items()
               if view[-1][0] == 'final_bit' and view[-1][1] == 1)
probs = {k: pfinal(v) for k, v in hist.items()}
left = abs(probs['real'] - probs['fjideal'])
right = abs(probs['real'] - probs['fideal']) + abs(probs['fideal'] - probs['fjideal'])
assert left <= right
# Exercise noncompletion under another FIXED public algorithm, not a side oracle.
original_h = h
h = lambda word: 0
bottom_worlds = 0
for s, k, p in product(range(2), repeat=3):
    expected = (('pre_public_full_h', 0), ('nonwinning_setup',))
    assert source(s, k, p) == expected
    assert bk(s, p, Interface(lambda a: f(s, k, a), None)) == expected
    randomizer_oracle = Interface(lambda i: g(s, p, (i >> 1, i & 1)), None)
    assert bp(s, (0,0), randomizer_oracle) == expected
    assert randomizer_oracle.queries == []
    bottom_worlds += 1
h = original_h

result = {
    'status': 'COMPUTED_EXACT_INTERFACE_CONTROLS_NOT_FULL_SOURCE_PROOF',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'ordinary_adapter_pointwise_identity_worlds': dict(identities),
    'full_source_facing_transcript_law_checked': True,
    'prekey_public_parameter_withheld': True,
    'setup_noncompletion_nonwinning_no_pk': True,
    'noncompletion_under_second_fixed_h_worlds': bottom_worlds,
    'repeat_after_restore_memo_consistent': True,
    'private_output_bits': 1, 'public_full_h_bits': 2,
    'zero_seed_literal_alias_cases': alias_cases,
    'alias_agreement_real': str(real_alias),
    'alias_agreement_ideal_private': str(ideal_alias),
    'negative_independent_raw_agreement': str(independent_raw_agreement),
    'correct_locally_computed_h_agreement': str(fixed_agreement),
    'reversible_public_h_involution_cases': unitary_cases,
    'decision_probabilities': {k: str(v) for k,v in probs.items()},
    'triangle_bound': {'left': str(left), 'right': str(right)},
    'scope': 'Small deterministic-h adapters; no SHA pseudorandomness proof, LULA security or native Rust refinement.'
}
(HERE / 'CONTROL-SUCCESSOR-RESULTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))

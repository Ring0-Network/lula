"""Historical immutable-authority component-cost and FORS occupancy model.

This retained exploratory model uses a Poisson occupancy approximation and treats
other components through assumptions. Its FORS exponents are component-model
quantities, not certified capacity or a whole-scheme security reduction. Hash-call
costs are analytical conventions; timing must be measured independently. Use the
publication model generator for the final table and its documented high-precision
controls. The numerical functions below are unchanged from the original model.
"""
import math
from functools import lru_cache

N = 16


def t_calls(l, n=N):
    return math.ceil((22 + n * l + 9) / 64)


def wots_len(lgw, n=N):
    w = 1 << lgw
    len1 = math.ceil(8 * n / lgw)
    len2 = math.floor(math.log2(len1 * (w - 1)) / lgw) + 1
    return len1, len2


def base_w_digits(x, lgw, out_len):
    w = 1 << lgw
    d = []
    for _ in range(out_len):
        d.append(x % w)
        x //= w
    return d[::-1]


@lru_cache(maxsize=None)
def wots_verify_worst_steps(lgw, n=N):
    """Max over message digit vectors of the chain steps the verifier computes."""
    w = 1 << lgw
    len1, len2 = wots_len(lgw, n)
    best = 0
    # Total = C + sum_j (w-1-c_j), C = sum_i (w-1-b_i) ranges over 0..len1(w-1), every value reachable.
    for C in range(0, len1 * (w - 1) + 1):
        # FIPS 205: csum << ((8 - (len2*lgw) % 8) % 8) before base_2^b conversion
        shift = (8 - (len2 * lgw) % 8) % 8
        cs = base_w_digits(C << shift, lgw, len2)
        tot = C + sum(w - 1 - c for c in cs)
        best = max(best, tot)
    return best


@lru_cache(maxsize=None)
def log2_fors_p(h, a, k, logq=40.0):
    """log2 of Fluhrer-Dang p (Poisson occupancy)."""
    # Streaming log-sum-exp in O(1) memory (the earlier version materialized a set of the whole Poisson
    # window, which for lam ~ 2^42 grew to tens of GB; killed by the orchestrator, see RUNS.md).
    lam = 2.0 ** (logq - h)
    t = 2.0 ** a
    loglam = math.log(lam)
    l1t = math.log1p(-1.0 / t)
    m = -math.inf
    s = 0.0

    def add(x, weight=1.0):
        nonlocal m, s
        x += math.log(weight)
        if x > m:
            s = s * math.exp(m - x) + 1.0 if m > -math.inf else 1.0
            m = x
        else:
            s += math.exp(x - m)

    def term(g):
        hit = -math.expm1(g * l1t)
        if hit <= 0:
            return None
        return g * loglam - lam - math.lgamma(g + 1) + k * math.log(hit)

    lo = max(400, int(lam - 60 * math.sqrt(lam + 1)))
    hi = int(lam + 60 * math.sqrt(lam + 1) + 200)
    for g in range(1, min(400, hi + 1)):
        x = term(g)
        if x is not None:
            add(x)
    if hi >= lo:
        span = hi - lo + 1
        stride = max(1, span // 200000)   # at most ~2e5 evaluations; Riemann weight = stride (smooth summand)
        for g in range(lo, hi + 1, stride):
            x = term(g)
            if x is not None:
                add(x, stride)
    return (m + math.log(s)) / math.log(2)


def log2_terminal_p(h, phi_log2, logq=40.0, gmax=12):
    """Generic terminal with exposure function phi(g) (log2 values; phi(0)=phi(1)=0 for one-time)."""
    lam = 2.0 ** (logq - h)
    terms = []
    for g in range(1, gmax + 1):
        if g not in phi_log2:
            continue
        lp = g * math.log(lam) - lam - math.lgamma(g + 1)
        terms.append(lp + phi_log2[g] * math.log(2))
    m = max(terms)
    return (m + math.log(sum(math.exp(x - m) for x in terms))) / math.log(2)


def costs(h, d, lgw, a, k, n=N):
    hp = h // d
    w = 1 << lgw
    len1, len2 = wots_len(lgw, n)
    L = len1 + len2
    leaf = L * (1 + (w - 1)) + t_calls(L, n)
    layer_sign = (1 << hp) * leaf + ((1 << hp) - 1)
    fors_sign = k * ((1 << a) * 2 + ((1 << a) - 1)) + t_calls(k, n)
    sign = 5 + 4 + fors_sign + d * layer_sign
    wv = wots_verify_worst_steps(lgw, n)
    verify = 4 + k * (1 + a) + t_calls(k, n) + d * (wv + t_calls(L, n) + hp)
    size = n * (1 + k * (a + 1) + h + d * L)
    return dict(sign=sign, verify=verify, size=size, L=L, leaf=leaf)


if __name__ == "__main__":
    # Self-check against published numbers: SLH-DSA-128f/128s sizes (FIPS 205 Table 2),
    # and SP 800-230 ipd SLH-DSA-SHA2-128-24 (3,856 B).
    for name, prm, size, lq in [("128f", (66, 22, 4, 6, 33), 17088, 64), ("128s", (63, 7, 4, 12, 14), 7856, 64),
                                ("128-24", (22, 1, 2, 24, 6), 3856, 24)]:
        c = costs(*prm)
        print(name, c["size"], "expected", size, "sign", c["sign"], "verify", c["verify"],
              "FORS-term exponent@2^%d" % lq, round(-log2_fors_p(prm[0], prm[3], prm[4], lq), 2), flush=True)

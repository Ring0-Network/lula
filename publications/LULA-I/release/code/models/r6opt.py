"""Historical LULA component-cost and occupancy model.

The generic few-time occupancy expressions and grinding-cost estimates are retained
from the original exploration. Their interpretation depends on the stated model;
they do not prove full adaptive-rollback security or certified signing capacity.
The reference-scheme bound remains open. Some historical cost conventions differ
from the final source-derived counts; use the paper's qualified analytical table
and its dedicated recomputation script for those results. Numerical functions are
unchanged. The large-occupancy approximation is limited by the existing assertion.
"""
import math
from functools import lru_cache

N = 16
LAMBDA = 128


def log2_binom_pmf(q, r, lp, l1mp):
    """log2 of Binom(q, r) p^r (1-p)^(q-r) given log2 p and log2(1-p)."""
    # log C(q, r) = sum_{i<r} log(q - i) - log r!  (no cancellation for huge q and small r)
    lc = (sum(math.log(q - i) for i in range(r)) - math.lgamma(r + 1)) / math.log(2)
    return lc + r * lp + (q - r) * l1mp


@lru_cache(maxsize=None)
def fors_log2_forge(k, a, h, q):
    """log2 of the Kudinov-Nick FORS sum. For mean load mu = q 2^-h <= 4096 the sum runs from r = 1 with
    ln C(q, r) accumulated exactly; for larger mu it runs over the window mu -/+ 20 sd (+300), with
    ln C(q, r) from lgamma (used only for q <= 2^44, where the absolute error is below 0.02 nats)."""
    ln2 = math.log(2)
    if h == 0:                                 # one instance carries all q signatures
        return k * math.log2(-math.expm1(q * math.log1p(-1.0 / 2 ** a)))
    lp = -h
    l1mp = math.log2(-math.expm1(-ln2 * h)) if h < 60 else -(2.0 ** -h) / ln2
    mu = q * 2.0 ** -h
    sd = math.sqrt(mu + 1)
    t = 2 ** a
    terms = []
    if mu <= 4096:
        rlo, rhi = 1, min(int(mu + 20 * sd + 300), q)
        lc = 0.0
        for r in range(1, rhi + 1):
            lc += math.log(q - r + 1) - math.log(r)
            cov = -math.expm1(r * math.log1p(-1.0 / t))
            terms.append(k * math.log2(cov) + lc / ln2 + r * lp + (q - r) * l1mp)
    else:
        assert q <= 2 ** 44
        rlo, rhi = max(1, int(mu - 20 * sd - 10)), min(int(mu + 20 * sd + 300), q)
        step = max(1, int(sd / 64))           # terms vary on the scale sd: Riemann sum with weight step
        for r in range(rlo, rhi + 1, step):
            lc = math.lgamma(q + 1) - math.lgamma(r + 1) - math.lgamma(q - r + 1)
            cov = -math.expm1(r * math.log1p(-1.0 / t))
            terms.append(k * math.log2(cov) + lc / ln2 + r * lp + (q - r) * l1mp + math.log2(step))
    m = max(terms)
    return m + math.log2(sum(2.0 ** (x - m) for x in terms))


def forsc_log2_forge(k, a, h, q):
    """EXACT per-try success of the random-message forger against FORS+C (k digest trees, the last forced to
    index 0 and not stored): the forced condition holds with probability 2^-a and is satisfied by leaf 0, which
    any signature on the instance reveals; the other k-1 trees as in FORS. Equals -a + FORS(k-1)."""
    return -a + fors_log2_forge(k - 1, a, h, q)


def fors_ok(k, a, h, q, lam=128):
    """True when the FORS bound is <= 2^-lam. Quick exact reject first: for mean load mu >= 1 the sum is at
    least P(R >= ceil(mu)) (1 - e^(-mu/2^a))^k >= 2^-2 (1 - e^(-mu/2^a))^k."""
    mu = q * 2.0 ** -h
    if mu >= 1:
        lb = -2 + k * math.log2(-math.expm1(-mu / 2.0 ** a))
        if lb > -lam:
            return False
    return fors_log2_forge(k, a, h, q) <= -lam


@lru_cache(maxsize=None)
def nu_table(lw, l):
    """number of l-tuples over [0, w-1] with each sum S (exact integers)."""
    w = 1 << lw
    dist = [1]
    for _ in range(l):
        nd = [0] * (len(dist) + w - 1)
        for s, c in enumerate(dist):
            if c:
                for x in range(w):
                    nd[s + x] += c
        dist = nd
    return tuple(dist)


def log2_grind_p(lw, z, S):
    """log2 of the per-try success of WOTS+C grinding: last z digits zero and digit sum S."""
    l = 128 // lw - z
    tab = nu_table(lw, l)
    if S < 0 or S >= len(tab) or tab[S] == 0:
        return -math.inf
    return math.log2(tab[S]) - lw * l - lw * z


def blocks(tail):
    return (tail + 9 + 63) // 64


def wots_l(lw, z):
    return 128 // lw - z


def wots_pk_cost(lw, z):
    l = wots_l(lw, z)
    return l * (1 + ((1 << lw) - 1)) + blocks(22 + N * l)


def wots_verify_cost(lw, z, S):
    l = wots_l(lw, z)
    return 1 + (l * ((1 << lw) - 1) - S) + blocks(22 + N * l)


def mean_S(lw, z):
    tab = nu_table(lw, wots_l(lw, z))
    return max(range(len(tab)), key=lambda s: tab[s])


def fors_real(k, forsc):
    return k - 1 if forsc else k


def fors_sign_cost(k, a, forsc):
    kr = fors_real(k, forsc)
    return kr * 3 * (1 << a) + blocks(22 + N * kr)


def fors_verify_cost(k, a, forsc):
    kr = fors_real(k, forsc)
    return kr * (1 + a) + blocks(22 + N * kr)


def sig_bytes(k, a, forsc, layers):
    s = N + (4 if forsc else 0) + fors_real(k, forsc) * (a + 1) * N
    for (h, lw, z, S, cached) in layers:
        s += 4 + wots_l(lw, z) * N + h * N
    return s


MSG_BYTES = 32
HMSG = (48 + MSG_BYTES + 9 + 63) // 64   # inner message hash (R || PK.seed || PK.root || m)
PRFMSG = (32 + MSG_BYTES + 9 + 63) // 64
TAIL = 20.79  # ln(2^30): grinding trials needed except with probability 2^-30 equal TAIL / p


def costs(k, a, forsc, layers):
    """layers: list (bottom first) of (h, lw, z, S, cached). Returns dict of costs in compression calls."""
    d = len(layers)
    H = [sum(L[0] for L in layers[j:]) for j in range(d)] + [0]   # H[j] = levels at and above layer j
    ver = HMSG + 1 + fors_verify_cost(k, a, forsc)
    sign_exp = PRFMSG + HMSG + 1 + fors_sign_cost(k, a, forsc)
    sign_tail = sign_exp
    if forsc:
        sign_exp += 2 ** a
        sign_tail += TAIL * 2 ** a
    keygen = 0.0
    mem = 0
    for j, (h, lw, z, S, cached) in enumerate(layers):
        lp = log2_grind_p(lw, z, S)
        grind = 2.0 ** (-lp)
        l = wots_l(lw, z)
        ver += wots_verify_cost(lw, z, S) + h
        if cached:
            sign_exp += 1 + l + S
            sign_tail += 1 + l + S
            keygen += 2.0 ** H[j] * (wots_pk_cost(lw, z) + 2 + grind)
            mem += 2 ** H[j + 1] * ((2 ** (h + 1) - 1) * N + 2 ** h * 4)
        else:
            sub = 2 ** h * wots_pk_cost(lw, z) + 2 ** h - 1
            sign_exp += sub + grind + 1 + l + S
            sign_tail += sub + TAIL * grind + 1 + l + S
    # child values of the lowest cached layer
    cached_js = [j for j, L in enumerate(layers) if L[4]]
    if cached_js:
        c = min(cached_js)
        if c == 0:
            keygen += 2.0 ** H[0] * fors_sign_cost(k, a, forsc)
        else:
            hb, lwb, zb, _, _ = layers[c - 1]
            keygen += 2.0 ** H[c] * (2 ** hb * wots_pk_cost(lwb, zb) + 2 ** hb)
    else:
        top = layers[-1]
        keygen += 2 ** top[0] * wots_pk_cost(top[1], top[2])
    return dict(verify=ver, sign_expected=sign_exp, sign_tail_2m30=sign_tail, keygen=keygen, cache_bytes=mem,
                sig_bytes=sig_bytes(k, a, forsc, layers), d=d, h=H[0])

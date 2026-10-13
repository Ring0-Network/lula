"""Accepted classical-family and fixed-parameter QROM probability envelopes.

Q counts adversarial public queries. Honest setup/signing work is separate.
Returned quantities are probability bounds, not attack work or security bits.
No parameter-uniform QROM draft is implemented in this module.
"""
from fractions import Fraction
from math import comb
import mpmath as mp
from .fors import coverage_probability, coverage_upper
from .parameters import BASELINE, Parameters, N, COUNTER_SPACE, nonnegative_integer


def _inputs(q, Q, parameters):
    nonnegative_integer(q, 'q')
    nonnegative_integer(Q, 'Q')
    if not isinstance(parameters, Parameters):
        raise ValueError('parameters must pass the guarded Parameters constructor')


def uniform_classical(parameters, q, Q, dps=240):
    """Numerical exact-binomial joint envelope with one seed-zero charge."""
    _inputs(q, Q, parameters)
    with mp.workdps(dps):
        n = mp.mpf(N)
        pf = coverage_probability(q, parameters.height, parameters.a, parameters.r, dps)
        terms = {
            'linear': mp.mpf(3*Q+2*q+parameters.classical_constant)/n,
            'full256_bridge': mp.mpf(q*Q+comb(q, 2)+q)/(n*n),
            'finite_counter': q*mp.exp(COUNTER_SPACE*mp.log1p(-mp.mpf(2)**(-parameters.a))),
            'coverage': (Q+1)*pf,
        }
        uncapped = mp.fsum(terms.values())
        return dict(terms, p_f=pf, uncapped=uncapped, total=min(mp.mpf(1), uncapped))


def classical_joint(q, Q, dps=240):
    return uniform_classical(BASELINE, q, Q, dps)


def uniform_classical_certificate(parameters, q, Q):
    """Exact rational sufficient upper, including a weakened finite-counter fee."""
    _inputs(q, Q, parameters)
    pf = coverage_upper(q, parameters.height, parameters.a, parameters.r)
    exponent = min(2048, 1 << (32-parameters.a))
    terms = {
        'public_slots': Fraction(3*Q, N),
        'honest_inner': Fraction(2*q, N),
        'terminal_seed_constant': Fraction(parameters.classical_constant, N),
        'full256_bridge': Fraction(q*Q+comb(q, 2)+q, N*N),
        'finite_counter_upper': Fraction(q, 1 << exponent),
        'coverage_upper': (Q+1)*pf,
    }
    uncapped = sum(terms.values(), Fraction(0))
    return dict(terms, p_f_upper=pf, uncapped=uncapped,
                total=min(Fraction(1), uncapped), at_most_half=uncapped <= Fraction(1, 2))


def fixed_qrom_poly(q, Q, dps=240):
    """Fixed baseline only: quadratic private K/P hops plus public HJ events."""
    _inputs(q, Q, BASELINE)
    with mp.workdps(dps):
        n = mp.mpf(N)
        good = n*n-n
        cap = lambda value: min(mp.mpf(1), value)
        pf = coverage_probability(q, dps=dps)
        row = cap(q*(mp.sqrt(mp.mpf(Q+q+1)/good)+mp.mpf(Q+q+1)/(2*good)))
        search = cap(row+8*(Q+2)**2*(pf+1/n+mp.mpf(q)/(n*n)))
        coverage = cap((2*Q+mp.sqrt(q))**2/n+(2*(Q+2)/mp.sqrt(n)+mp.sqrt(search))**2)
        hidden = cap((2*Q+mp.sqrt(3017))**2/n)
        graph = cap(8*mp.mpf(Q+3218)**2/n)
        canonical = cap(8*mp.mpf(Q+6)**2/n)
        private_k = cap(mp.mpf(4*Q*Q)/(n-4*Q*Q)) if 4*Q*Q < N else mp.mpf(1)
        alias_p = cap((2*Q+mp.sqrt(min(N, 2*q+2)))**2/n)
        private_p = cap(private_k+alias_p)
        public_union = cap(coverage+hidden+graph+canonical)
        seed_zero = 1/n
        total = cap(seed_zero+private_k+private_p+public_union)
        return dict(p_f=pf, row_distance=row, coverage_search=search, coverage=coverage,
                    hidden=hidden, graph=graph, canonical=canonical,
                    private_k=private_k, alias_p=alias_p, private_p=private_p,
                    public_union=public_union, seed_zero=seed_zero, total=total)

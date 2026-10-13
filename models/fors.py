"""Finite-binomial FORS coverage calculations and a rational positive upper bound."""
from fractions import Fraction
from functools import lru_cache
from math import comb
import mpmath as mp
from .parameters import nonnegative_integer


def _guards(q, height, a, real_trees, dps):
    for value, name in [(q, 'q'), (height, 'height'), (a, 'a'), (real_trees, 'real_trees')]:
        nonnegative_integer(value, name)
    if not 0 <= height <= 63 or not 1 <= a <= 31 or not 1 <= real_trees <= 94:
        raise ValueError('FORS dimensions outside the guarded family')
    if real_trees*(1 << a) > 1 << 32 or (real_trees+1)*a+height > 256:
        raise ValueError('FORS index or digest coordinates overflow')
    if type(dps) is not int or dps < 160:
        raise ValueError('use at least 160 decimal digits for alternating moments')


@lru_cache(maxsize=128, typed=True)
def coverage_probability(q, height=41, a=9, real_trees=17, dps=240):
    """Evaluate the exact finite Binomial law, not a Poisson approximation.

    The return value is high-precision numerical arithmetic, not a formally
    verified floating-point enclosure or a full-signature security level.
    """
    _guards(q, height, a, real_trees, dps)
    with mp.workdps(dps):
        if q == 0:
            return mp.mpf(0)
        beta = 1-mp.mpf(2)**(-a)
        if height == 0:
            return (-mp.expm1(q*mp.log(beta)))**real_trees / (1 << a)
        rho = mp.mpf(2)**(-height)
        probability = mp.fsum((-1)**j*comb(real_trees, j)*
                              mp.exp(q*mp.log1p(rho*(beta**j-1)))
                              for j in range(real_trees+1)) / (1 << a)
        if probability <= 0 or probability > mp.mpf(2)**(-a)+64*mp.eps:
            raise ArithmeticError('insufficient precision in binomial moment')
        return min(probability, mp.mpf(2)**(-a))


def positive_coverage_interval(q, height=41, a=9, real_trees=17, dps=240):
    """Independent positive sum or analytic saturation bounds, evaluated numerically.

    For small occupancy the omitted Binomial tail has a Chernoff upper bound.
    For large occupancy use P[Z<mu/2] <= exp(-mu/8). Small rounding cushions
    are included; this is not a directed-rounding arithmetic certificate.
    """
    _guards(q, height, a, real_trees, dps)
    with mp.workdps(dps):
        t = 1 << a
        if q == 0:
            return mp.mpf(0), mp.mpf(0)
        log_beta = mp.log1p(-mp.mpf(1)/t)
        if height == 0:
            value = (-mp.expm1(q*log_beta))**real_trees/t
            return max(mp.mpf(0), value-64*mp.eps), min(mp.mpf(1)/t, value+64*mp.eps)
        rho = mp.mpf(2)**(-height)
        mu = q*rho
        if mu > 4096:
            lower = (1-mp.exp(-mu/8))*(-mp.expm1(mu*log_beta/2))**real_trees/t
            return max(mp.mpf(0), lower-64*mp.eps), mp.mpf(1)/t
        limit = min(q, max(1800, int(mp.ceil(mu+100*mp.sqrt(mu+1)+1800))))
        mass = mp.exp(q*mp.log1p(-rho))
        partial = mp.mpf(0)
        for count in range(1, limit+1):
            mass *= mp.mpf(q-count+1)*rho/(count*(1-rho))
            partial += mass*(-mp.expm1(count*log_beta))**real_trees/t
        next_count = limit+1
        tail = mp.mpf(0) if limit == q else mp.exp(-mu+next_count*(1+mp.log(mu/next_count)))/t
        return max(mp.mpf(0), partial-64*mp.eps), min(mp.mpf(1)/t, partial+tail+64*mp.eps)


def coverage_upper(q, height=41, a=9, real_trees=17):
    """Exact Fraction upper: E[Z^r] <= Touchard_r(q/2^height)."""
    _guards(q, height, a, real_trees, 160)
    stirling = [1]
    for degree in range(1, real_trees+1):
        stirling = [0]+[stirling[j-1]+j*(stirling[j] if j < len(stirling) else 0)
                       for j in range(1, degree+1)]
    mu = Fraction(q, 1 << height)
    moment = sum((coefficient*mu**j for j, coefficient in enumerate(stirling)), Fraction(0))
    return min(Fraction(1, 1 << a), moment / (1 << a)**(real_trees+1))

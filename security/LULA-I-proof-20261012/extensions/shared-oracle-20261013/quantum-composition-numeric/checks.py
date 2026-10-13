"""Own complete-envelope candidate arithmetic, not a promoted QROM total."""
from pathlib import Path
from fractions import Fraction
from math import comb
import json
import mpmath as mp

mp.mp.dps=240
HERE=Path(__file__).resolve().parent
N=2**128
M=N*N-N
QES=(24,30,38,40,41,44,50,64)
QS=(32,64)

def fs(x): return mp.nstr(x,100)
def bits(x): return fs(-mp.log(min(1,x),2))
def cap(x): return min(mp.mpf(1),x)

def pf(q):
    p=mp.mpf(1)/2**41
    b=mp.mpf(511)/512
    return mp.fsum((-1)**j*comb(17,j)*mp.exp(q*mp.log1p(p*(b**j-1))) for j in range(18))/512

def compute(q,Q):
    seed=Fraction(1,N)
    classical_private=Fraction(2*q+2,N)
    d=2*mp.mpf(Q)/mp.sqrt(N)+mp.mpf(classical_private.numerator)/classical_private.denominator
    row=mp.mpf(q)*(mp.sqrt(mp.mpf(Q+q+1)/M)+mp.mpf(Q+q+1)/(2*M))
    f=pf(q)
    ac=cap(cap(row)+8*mp.mpf(Q+2)**2*(f+mp.mpf(1)/N+mp.mpf(q)/(N*N)))
    cguard=(2*mp.mpf(Q)+mp.sqrt(q))**2/N
    cpost=(2*mp.mpf(Q+2)/mp.sqrt(N)+mp.sqrt(ac))**2
    c=cap(cguard+cpost)
    h=(2*mp.mpf(Q)+mp.sqrt(3017))**2/N
    g=Fraction(8*(Q+3218)**2,N)
    d7=Fraction(8*(Q+6)**2,N)
    gm=mp.mpf(g.numerator)/g.denominator
    d7m=mp.mpf(d7.numerator)/d7.denominator
    seedm=mp.mpf(seed.numerator)/seed.denominator
    hjsum=cap(c+cap(h)+cap(gm)+cap(d7m))
    overall=cap(seedm+cap(d)+c+cap(h)+cap(gm)+cap(d7m))
    # Different arrangement: condition on nonzero seed then average/loosen.
    good_bound=cap(cap(d)+hjsum)
    weighted=seedm+(1-seedm)*good_bound
    assert overall+mp.mpf('1e-210')>=weighted
    assert abs(overall-cap(seedm+good_bound))<mp.mpf('1e-210')
    # Independent exact rational constants and expanded square-root terms.
    pure_linear=Fraction(1+2*q+2+4*Q*Q+3017+8*(Q+3218)**2+8*(Q+6)**2,N)
    expanded=2*mp.mpf(Q)/mp.sqrt(N)+mp.mpf(pure_linear.numerator)/pure_linear.denominator+4*mp.mpf(Q)*mp.sqrt(3017)/N+c
    # This arrangement uses uncapped H/G/D7/private. It gives the same finalcap.
    assert abs(overall-cap(expanded))<mp.mpf('1e-210')
    return dict(q_exponent=q.bit_length()-1,Qq_exponent=Q.bit_length()-1,
        seed_probability=fs(seedm),private_quantum_hop_uncapped=fs(d),
        private_classical_part_exact=str(classical_private),
        conditional_FORS_probability=fs(f),ROW_uncapped=fs(row),A_C_capped=fs(ac),
        source_C_guard_uncapped=fs(cguard),source_C_post_uncapped=fs(cpost),
        C_probability=fs(c),H_probability_capped=fs(cap(h)),
        G_probability_exact_uncapped=str(g),G_probability_capped=fs(cap(gm)),
        D7_probability_exact_uncapped=str(d7),D7_probability_capped=fs(cap(d7m)),
        HJ_union_probability=fs(hjsum),
        candidate_reference_probability=fs(overall),candidate_reference_bits=bits(overall),
        candidate_reference_uncapped_expansion=fs(expanded),
        candidate_weighted_seed_reference_probability=fs(weighted),
        expanded_pure_rational_exact=str(pure_linear),
        promoted_quantum_total_probability=None,promoted_quantum_total_bits=None,
        status='CONDITIONAL_COMPOSITION_CANDIDATE_PENDING_SECOND_SOURCE_C_GATE')

def main():
    rows=[compute(2**qe,2**Qe) for qe in QES for Qe in QS]
    out=dict(status='OWN_CANDIDATE_ARITHMETIC_SAVED_BEFORE_ROOT_COMPOSITION_READ',
        precision_decimal_digits=mp.mp.dps,
        controls=dict(all16_expanded_sums_passed=True,all16_weighted_seed_checks_passed=True,
                      exact_rational_components=True),rows=rows,
        promoted_quantum_total_probability=None,promoted_quantum_total_bits=None)
    (HERE/'OWN-BOUNDS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS:16 independent complete candidate sums, exact rational constants, expanded squares, single seed branch. Promoted quantum total null.')

if __name__=='__main__':main()

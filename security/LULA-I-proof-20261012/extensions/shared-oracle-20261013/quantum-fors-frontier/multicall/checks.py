"""Independent scoped quantum coverage arithmetic; not full QROM security."""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import mpmath as mp

mp.mp.dps = 240
HERE = Path(__file__).resolve().parent
X = HERE.parents[1]
ROOT = X.parents[2]
Q_EXP = (24, 30, 38, 40, 41, 44, 50, 64)
QQ_EXP = (32, 64)
N = 2**128
M = N*N-N

def fmt(x):
    return mp.nstr(x, 100)

def bits(x):
    return None if x == 0 else fmt(-mp.log(min(1, x), 2))

def fors_moments(q):
    b = mp.mpf(511)/512
    p = mp.mpf(1)/2**41
    terms = [(-1)**j*comb(17,j)*mp.exp(q*mp.log1p(p*(b**j-1)))
             for j in range(18)]
    v = mp.fsum(terms)/512
    assert 0 < v <= mp.mpf(1)/512
    return v

def fors_positive(q):
    # Independent positive occupancy recurrence; upper tail by Chernoff.
    p = mp.mpf(1)/2**41
    mu = q*p
    if mu > 600:
        return None
    cutoff = max(200, int(mp.ceil(mu + 80*mp.sqrt(mu+1) + 200)))
    mass = mp.exp(q*mp.log1p(-p))
    terms = []
    for l in range(cutoff+1):
        covered = (-mp.expm1(l*mp.log(mp.mpf(511)/512)))**17/512
        terms.append(mass*covered)
        mass *= (q-l)*p/((l+1)*(1-p))
    lo = mp.fsum(terms)
    a = mp.mpf(cutoff+1)
    tail = mp.exp(-a*mp.log(a/mu)+a-mu)/512
    return lo, lo+tail, cutoff

def numeric_rows():
    rows=[]
    for qe in Q_EXP:
        q=2**qe
        pf=fors_moments(q)
        positive = fors_positive(q)
        if positive:
            lo, hi, cutoff=positive
            # 240 digit evaluation slack; no empirical tail truncation.
            assert lo-mp.mpf('1e-215') <= pf <= hi+mp.mpf('1e-215')
        for Qe in QQ_EXP:
            Q=2**Qe
            Aq=mp.mpf(q*Q)+mp.mpf(q*(q-1))/2
            integral_lo=mp.mpf(2)/3*((mp.mpf(Q+q-1))**mp.mpf('1.5')-(mp.mpf(Q-1))**mp.mpf('1.5'))
            integral_hi=mp.mpf(2)/3*((mp.mpf(Q+q))**mp.mpf('1.5')-(mp.mpf(Q))**mp.mpf('1.5'))
            row_lo=integral_lo/mp.sqrt(M)+Aq/(2*M)
            row_hi=integral_hi/mp.sqrt(M-q+1)+Aq/(2*(M-q+1))
            # Root uses replacement, constant pmax=1/M and this safe cap.
            cap=Q+q+1
            row_root=mp.mpf(q)*(mp.sqrt(mp.mpf(cap)/M)+mp.mpf(cap)/(2*M))
            # Separately evaluate the sum cap without replacement to avoid
            # confusing two games: root did not pay namespace duplication.
            row_distinct_cap=mp.mpf(q)*(mp.sqrt(mp.mpf(Q+q-1)/(M-q+1))+mp.mpf(Q+q-1)/(2*(M-q+1)))
            assert row_lo <= row_hi <= row_distinct_cap
            guard=q/mp.mpf(N)
            dup=mp.mpf(q*(q-1))/(2*M)
            inner=8*mp.mpf(Q+2)**2*(mp.mpf(1)/N+mp.mpf(q)/(N*N))
            cov=8*mp.mpf(Q+2)**2*pf
            ac=min(mp.mpf(1), row_root+inner+cov)
            source_guard=(2*mp.mpf(Q)+mp.sqrt(q))**2/N
            source_transport=(2*mp.mpf(Q+2)/mp.sqrt(N)+mp.sqrt(ac))**2
            envelope=min(mp.mpf(1),source_guard+source_transport)
            # Independent expansion of the amplitude square.
            expanded=source_guard+4*mp.mpf(Q+2)**2/N+ac+4*mp.mpf(Q+2)*mp.sqrt(ac/N)
            assert abs(envelope-min(mp.mpf(1), expanded))<mp.mpf('1e-210')
            rows.append(dict(q_exponent=qe,Qq_exponent=Qe,
                conditional_fors_bits=bits(pf),conditional_fors_probability=fmt(pf),
                distinct_row_sum_lower=fmt(row_lo),distinct_row_sum_upper=fmt(row_hi),
                distinct_row_sum_bits_lower=bits(row_hi),distinct_row_sum_bits_upper=bits(row_lo),
                root_replacement_row_envelope=fmt(row_root),
                root_replacement_row_bits=bits(row_root),
                independent_guard_probability=fmt(guard),
                independent_duplicate_probability=fmt(dup),
                root_final_namespace_search_uncapped=fmt(inner),
                root_fors_search_uncapped=fmt(cov),
                root_AC_capped=fmt(ac),
                root_source_guard_uncapped=fmt(source_guard),
                root_source_transport_uncapped=fmt(source_transport),
                candidate_source_coverage_probability=fmt(envelope),
                candidate_source_coverage_bits=bits(envelope),
                independently_expanded_source_sum=fmt(expanded),
                positive_binomial_cutoff=positive[2] if positive else None,
                quantum_total_probability=None,quantum_total_bits=None,
                status='CANDIDATE_COVERAGE_EVENT_ONLY_NOT_FULL_QROM_SECURITY'))
    return rows

def controls():
    # Coverage: direct raw-digest enumeration, independently arranged binomial.
    B,t,k,q=2,2,2,2
    routes=list(product(range(B),range(t),range(t)))
    densities=[]
    for transcript in product(routes, repeat=q):
        hits=0
        for b,j0,j1,z in product(range(B),range(t),range(t),range(t)):
            sets=[{r[j+1] for r in transcript if r[0]==b} for j in range(k)]
            hits += z==0 and j0 in sets[0] and j1 in sets[1]
        densities.append(Fraction(hits,B*t**(k+1)))
    direct=sum(densities,Fraction())/len(densities)
    occupancy=sum(Fraction(comb(q,l),2**q)*(1-Fraction(1,2)**l)**k
                  for l in range(q+1))/t
    assert direct==occupancy==Fraction(17,128)
    # Conditioning completion on X0 biases completed routes; latent pad does not.
    latent=list(product(range(2),repeat=2))
    completed=[x for x in latent if x[0]==0]
    assert sum(x[0]==0 for x in latent)/len(latent)==0.5
    assert all(x[0]==0 for x in completed)
    # Replacement collisions: latest row, not stale message cache, must be used.
    programs=[('a',1,0),('b',1,1)]
    namespace_rows={}
    message_namespace={}
    for label,U,Xval in programs:
        message_namespace[label]=U
        namespace_rows[U]=Xval
    repeated_route=namespace_rows[message_namespace['a']]
    assert repeated_route==1
    assert repeated_route in {p[2] for p in programs}
    # Exact collision probability versus union bound on a finite toy.
    toyM,toyq=5,3
    distinct=Fraction(1)
    for j in range(toyq):
        distinct*=Fraction(toyM-j,toyM)
    coll=1-distinct
    cap=Fraction(comb(toyq,2),toyM)
    assert coll<=cap
    # Honest read omission is not a harmless equality even if public Q is0.
    Q,q,M=0,3,16
    with_reads=sum(mp.sqrt(mp.mpf(Q+r)/M)+mp.mpf(Q+r)/(2*M) for r in range(q))
    without_reads=mp.mpf(q)*(mp.sqrt(mp.mpf(Q)/M)+mp.mpf(Q)/(2*M))
    assert with_reads>0 and without_reads==0
    # Guard and namespace image sets are disjoint; density is counted full-image.
    words=list(product(range(4),range(4)))
    seed=2; target={(0,0),(3,1)}
    assert all(u[1]!=seed for u in target)
    marked=[u for u in words if u[1]==seed or u in target]
    assert Fraction(len(marked),len(words))==Fraction(6,16)
    # AR reveals x only; its y must be read. Two worlds indistinguishable from
    # the API receipt alone still have different honest source responses.
    api_receipts=[('namespace',3),('namespace',3)]
    row_values=[0,1]
    assert api_receipts[0]==api_receipts[1] and row_values[0]!=row_values[1]
    return dict(coverage_direct=str(direct),coverage_binomial=str(occupancy),
        exhaustive_transcripts=len(densities),latest_collision_repeat_route=repeated_route,
        finite_collision_probability=str(coll),collision_union_bound=str(cap),
        zero_public_queries_with_honest_reads_loss=fmt(with_reads),
        incorrect_omitted_honest_reads_loss=fmt(without_reads),
        marked_full_image_density='3/8',completion_conditioning_counterexample=True,
        reprogram_receipt_does_not_reveal_y=True,all_checks_passed=True)

def main():
    rows=numeric_rows()
    out=dict(status='INDEPENDENT_CANDIDATE_NUMERICS_AND_DISCRIMINATING_CONTROLS',
        precision_decimal_digits=mp.mp.dps,
        arithmetic_qualification='240-digit evaluation plus analytic integral and binomial-tail brackets; no formally certified directed-rounded interval package',
        assumptions=['fixed nonzero seed','HJ joint ideal complete full256 oracle',
                     'atomic classical signing, no timing or private tables',
                     'source ghost and quantum projections require independent reviews'],
        controls=controls(),rows=rows,quantum_total_probability=None,
        quantum_total_bits=None)
    (HERE/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS: 16 candidate rows; two source-square calculations; six positive-binomial checks; exact bounded controls. Full QROM total remains null.')

if __name__=='__main__':
    main()

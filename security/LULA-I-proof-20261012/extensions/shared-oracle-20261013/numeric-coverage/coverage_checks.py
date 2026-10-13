#!/usr/bin/env python3
"""Exact fresh-stream coverage controls, explicitly NOT a real signature game.

Run: python -I -B coverage_checks.py [--trials 30000] [--out DIRECTORY]
Standard library only. No signing, timing measurement, cache build or new real parameters.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import random

SEED=20261013017
B=2
T=2
K=2
Q=2
M=2


def frac(x):
    return dict(numerator=str(x.numerator),denominator=str(x.denominator),decimal=float(x))


def exposure_space(B,t,K):
    return list(itertools.product(range(B),*(range(t) for _ in range(K))))


def raw_space(B,t,K):
    return list(itertools.product(range(B),*(range(t) for _ in range(K+1))))


def transcript_sets(exposures,B,K):
    sets=[[set() for _ in range(K)] for _ in range(B)]
    for x in exposures:
        for j in range(K):
            sets[x[0]][j].add(x[j+1])
    return sets


def covered(y,sets,K):
    return y[-1]==0 and all(y[j+1] in sets[y[0]][j] for j in range(K))


def transcript_probability(sets,B,t,K):
    num=sum(math.prod(len(sets[b][j]) for j in range(K)) for b in range(B))
    return F(num,B*t**(K+1))


def occupancy_probability(B,t,K,q):
    p=F(1,B)
    miss=F(t-1,t)
    return sum((F(math.comb(q,r))*p**r*(1-p)**(q-r)*(1-miss**r)**K/t
                for r in range(q+1)),F(0))


def moment_probability(B,t,K,q):
    p=F(1,B)
    miss=F(t-1,t)
    return sum((F((-1)**j*math.comb(K,j))*(1-p+p*miss**j)**q/t
                for j in range(K+1)),F(0))


def exhaustive_coverage(B,t,K,q,M):
    """Arrangement A: enumerate every exposure transcript and every raw candidate tuple."""
    X=exposure_space(B,t,K)
    Y=raw_space(B,t,K)
    mean=F(0)
    second=F(0)
    late=F(0)
    successes=0
    joint_trials=0
    distribution=Counter()
    for exposures in itertools.product(X,repeat=q):
        sets=transcript_sets(exposures,B,K)
        p=transcript_probability(sets,B,t,K)
        assert p==F(sum(covered(y,sets,K) for y in Y),len(Y))
        distribution[p]+=1
        mean+=p
        second+=p*p
        late+=1-(1-p)**M
        for candidates in itertools.product(Y,repeat=M):
            successes+=int(any(covered(y,sets,K) for y in candidates))
            joint_trials+=1
    denominator=len(X)**q
    mean/=denominator
    second/=denominator
    late/=denominator
    assert late==F(successes,joint_trials)
    return dict(mean=mean,second=second,late=late,joint_successes=successes,
                joint_trials=joint_trials,transcripts=denominator,coverage_distribution=distribution)


def mask_probability(state,B,t,K):
    return F(sum(math.prod(state[b*K+j].bit_count() for j in range(K))
                 for b in range(B)),B*t**(K+1))


def dynamic_coverage(B,t,K,q,M):
    """Arrangement B: propagate coverage masks and multiplicities; no transcript list."""
    states={(0,)*(B*K):1}
    X=exposure_space(B,t,K)
    for _ in range(q):
        next_states=defaultdict(int)
        for state,n in states.items():
            for x in X:
                nxt=list(state)
                for j in range(K):
                    nxt[x[0]*K+j]|=1<<x[j+1]
                next_states[tuple(nxt)]+=n
        states=dict(next_states)
    denominator=len(X)**q
    mean=sum((mask_probability(s,B,t,K)*n for s,n in states.items()),F(0))/denominator
    late=sum(((1-(1-mask_probability(s,B,t,K))**M)*n for s,n in states.items()),F(0))/denominator
    return dict(mean=mean,late=late,state_count=len(states),denominator=denominator)


def exact_preview_selection(B,t,K,L):
    """Hypothetical preview/selection interface, not LULA signing."""
    X=exposure_space(B,t,K)
    Y=raw_space(B,t,K)
    successes=0
    total=0
    for y in Y:
        for previews in itertools.product(X,repeat=L):
            successes+=int(y[-1]==0 and y[:-1] in previews)
            total+=1
    expected=F(1,t)*(1-(1-F(1,len(X)))**L)
    assert F(successes,total)==expected
    return dict(L=L,probability=frac(expected),single_independent_exposure=frac(F(1,t*len(X))),
                gain_factor=frac(expected/F(1,t*len(X))),joint_trials=total,
                scope='q=1 chosen exposure after L previews; NOT a real signer attack and previews incur oracle cost')


def exact_correlated_point_reuse(B,t,K):
    """Correct marginal coverage expectation can coexist with a dependent target."""
    Y=raw_space(B,t,K)
    mean=F(0)
    successes=0
    for y in Y:
        sets=transcript_sets([y[:-1]],B,K)
        mean+=transcript_probability(sets,B,t,K)
        successes+=int(covered(y,sets,K))
    mean/=len(Y)
    actual=F(successes,len(Y))
    assert mean==occupancy_probability(B,t,K,1)
    assert actual==F(1,t)
    assert actual>mean
    return dict(expected_realized_coverage=frac(mean),dependent_target_success=frac(actual),
                violation_factor=frac(actual/mean),marginal_exposure_uniform=True,
                scope='X is chosen as the tuple of already queried Y; violates fresh independent streams, not a LULA forgery')


def exact_first_accept(B,t,K,C):
    Y=raw_space(B,t,K)
    X=exposure_space(B,t,K)
    counts=Counter()
    rejected=0
    total=len(Y)**C
    for stream in itertools.product(Y,repeat=C):
        for c,y in enumerate(stream):
            if y[-1]==0:
                counts[(c,y[:-1])]+=1
                break
        else:
            rejected+=1
    for c in range(C):
        for x in X:
            exact=F(t-1,t)**c/F(t*len(X))
            assert F(counts[(c,x)],total)==exact
    failure=F(rejected,total)
    assert failure==F(t-1,t)**C
    for x in X:
        assert F(sum(counts[(c,x)] for c in range(C)),total-rejected)==F(1,len(X))
    return dict(C=C,joint_trials=total,failure=frac(failure),
                accepted_tuple_uniform_conditioned_on_success=True,
                counter_and_tuple_factorization_checked=True)


def wilson(k,n,z=3.2905267314919255):
    p=k/n
    den=1+z*z/n
    centre=(p+z*z/(2*n))/den
    width=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return [max(0,centre-width),min(1,centre+width)]


def interleaved_success(exposures,candidates,B,K):
    """Adaptive reveal order; retain old candidates and stop immediately upon coverage."""
    seen_x=[]
    seen_y=[]
    i=j=0
    steps=[]
    while i<len(exposures) or j<len(candidates):
        choose_y=(j<len(candidates) and
                  (i==len(exposures) or not seen_y or seen_y[-1][0]==0))
        if choose_y:
            seen_y.append(candidates[j])
            j+=1
            steps.append('candidate')
        else:
            seen_x.append(exposures[i])
            i+=1
            steps.append('exposure')
        sets=transcript_sets(seen_x,B,K)
        if any(covered(y,sets,K) for y in seen_y):
            return True,steps,i,j
    return False,steps,i,j


def monte_carlo(trials,exact):
    rng=random.Random(SEED)
    X=exposure_space(B,T,K)
    Y=raw_space(B,T,K)
    late_n=inter_n=preview_n=correlated_n=0
    stopped_early=0
    orders=Counter()
    for _ in range(trials):
        exposures=[rng.choice(X) for _ in range(Q)]
        candidates=[rng.choice(Y) for _ in range(M)]
        sets=transcript_sets(exposures,B,K)
        late=any(covered(y,sets,K) for y in candidates)
        inter,steps,i,j=interleaved_success(exposures,candidates,B,K)
        assert late==inter
        late_n+=int(late)
        inter_n+=int(inter)
        stopped_early+=int(inter and (i<Q or j<M))
        orders['/'.join(steps)]+=1
        candidate=rng.choice(Y)
        previews=[rng.choice(X) for _ in range(2)]
        preview_n+=int(candidate[-1]==0 and candidate[:-1] in previews)
        correlated_n+=int(covered(candidate,transcript_sets([candidate[:-1]],B,K),K))
    rows=[]
    for name,n,p in (('independent_late',late_n,exact),
                     ('adaptive_interleaved',inter_n,exact),
                     ('preview_selected_exposure',preview_n,F(1,T)*(1-(1-F(1,len(X)))**2)),
                     ('correlated_point_reuse',correlated_n,F(1,T))):
        interval=wilson(n,trials)
        assert interval[0]<=float(p)<=interval[1],(name,n,p,interval)
        rows.append(dict(model=name,trials=trials,successes=n,empirical=n/trials,
                         exact=frac(p),wilson_ci999=interval,exact_within_ci=True))
    return dict(rows=rows,late_interleaved_pathwise_equal=True,early_success_stops=stopped_early,
                schedule_counts=dict(sorted(orders.items())),
                note='Coverage-only toy experiments. Shared oracle reuse/preview controls are deliberately different interfaces.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--trials',type=int,default=30000)
    parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    a=exhaustive_coverage(B,T,K,Q,M)
    b=dynamic_coverage(B,T,K,Q,M)
    occupancy=occupancy_probability(B,T,K,Q)
    moment=moment_probability(B,T,K,Q)
    assert a['mean']==b['mean']==occupancy==moment
    assert a['late']==b['late']
    jensen=1-(1-a['mean'])**M
    union=min(F(1),M*a['mean'])
    assert a['late']<=jensen<=union
    preview=exact_preview_selection(B,T,K,2)
    correlated=exact_correlated_point_reuse(B,T,K)
    first=exact_first_accept(B,T,K,4)
    mc=monte_carlo(args.trials,a['late'])
    result=dict(status='PASS_MODEL_SCOPED_CHECKS',seed=SEED,
                parameters=dict(B=B,t=T,K_real=K,q_exposures=Q,M_raw_candidates=M),
                coverage_expectation=dict(exhaustive=frac(a['mean']),coverage_state_dp=frac(b['mean']),
                                          occupancy=frac(occupancy),finite_moment=frac(moment)),
                late_phase=dict(exact=frac(a['late']),dp_exact=frac(b['late']),
                                jensen_upper=frac(jensen),union_upper=frac(union),
                                second_moment_pT=frac(a['second']),
                                exhaustive_joint_trials=a['joint_trials'],joint_successes=a['joint_successes']),
                transcript_pT_distribution=[dict(p=frac(p),count=n) for p,n in sorted(a['coverage_distribution'].items())],
                coverage_state_count=b['state_count'],first_accept=first,
                preview_countermodel=preview,correlated_query_countermodel=correlated,monte_carlo=mc,
                LULA_source_bound=None,LULA_adaptive_Bad_bound=None,LULA_total_euf_bound=None,
                missing_lemma='Source-bound coupling to independent fresh streams until a charged shared-input/prequery/inner-collision/secret-R bad event',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (args.out/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status=result['status'],mean=frac(a['mean']),late=frac(a['late']),
                          jensen=frac(jensen),union=frac(union),first_accept=first,
                          preview=preview,correlated=correlated,monte_carlo=mc),indent=2),flush=True)


if __name__=='__main__':
    main()

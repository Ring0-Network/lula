#!/usr/bin/env python3
"""Independent component checks; DOES NOT establish total EUF-CMA security.

Run: python -I -B bounds.py [--out DIR] [--samples 128] [--toy-trials 30000]
Dependency: mpmath==1.3.0. No key generation, cache rebuild, or crypto timing.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
import random
import statistics
import mpmath as mp

Q_EXPONENTS = (24, 30, 38, 40, 41, 44, 50, 64)
SEED = 2026101217


def textnum(x, digits=35):
    return mp.nstr(x, digits)


def bits(p):
    return float(-mp.log(p, 2)) if p > 0 else None


def fors_moment(q, h, a, k, poisson=False, dps=160):
    """Exact algebraic finite-moment expression, high-precision evaluation."""
    with mp.workdps(dps):
        p = mp.mpf(2) ** -h
        b = 1 - mp.mpf(2) ** -a
        terms = []
        for j in range(k):
            factor = mp.exp(q*p*(b**j-1)) if poisson else mp.exp(q*mp.log1p(p*(b**j-1)))
            terms.append((-1)**j * math.comb(k-1,j) * factor)
        return +mp.fsum(terms) * mp.mpf(2)**-a


def fors_positive(q, h, a, k, poisson=False, dps=160):
    """Positive recurrence with analytic tail bound; concentrated saturation for huge mu."""
    with mp.workdps(dps):
        p=mp.mpf(2)**-h
        mu=q*p
        filt=mp.mpf(2)**-a
        b=1-filt
        if mu > 4096:
            # P(R<mu/2)<=exp(-mu/8); coverage for R>=mu/2 is bounded below.
            bad=mp.exp(-mu/8)
            low=filt*(1-bad)*(1-mp.exp((mu/2)*mp.log(b)))**(k-1)
            return dict(lower=textnum(low), upper=textnum(filt), bits=bits(filt),
                        method="Chernoff saturation interval", omitted_tail_upper=textnum(bad),
                        saturation_deficit_upper=textnum(bad+(k-1)*mp.exp(-mu*filt/2)))
        stop=min(q,max(300,int(mu+20*mp.sqrt(mu+1)+300)))
        pr=mp.exp(-mu) if poisson else mp.exp(q*mp.log1p(-p))
        tot=mp.mpf(0)
        for r in range(1,stop+1):
            pr *= mu/r if poisson else (q-r+1)*p/(r*(1-p))
            cov=-mp.expm1(r*mp.log(b))
            tot += pr*cov**(k-1)
        # Chernoff: P(R>=L) <= exp[-mu] (e*mu/L)^L (valid for either distribution).
        L=stop+1
        tail=mp.mpf(0) if stop==q else mp.exp(-mu+L*(1+mp.log(mu/L)))
        low=filt*tot
        high=low+filt*tail
        return dict(lower=textnum(low),upper=textnum(high),bits=bits(low),
                    method="positive occupancy recurrence", stop=stop,
                    omitted_tail_upper=textnum(tail), weighted_relative_tail_upper=textnum(filt*tail/low))


def count_dp(total, caps):
    if total<0 or any(c<0 for c in caps):
        return 0
    if total>sum(caps):
        return 0
    d=[1]+[0]*total
    for cap in caps:
        prefix=[0]
        for v in d:
            prefix.append(prefix[-1]+v)
        d=[prefix[s+1]-prefix[max(0,s-cap)] for s in range(total+1)]
    return d[total]


def count_ie(total,caps):
    """Grouped inclusion-exclusion, independent coefficient formula, no float arithmetic."""
    if total<0 or any(c<0 for c in caps) or total>sum(caps):
        return 0
    shift={0:1}
    for step,multiplicity in sorted(Counter(c+1 for c in caps).items()):
        nxt={}
        for old,weight in shift.items():
            for j in range(min(multiplicity,(total-old)//step)+1):
                degree=old+j*step
                nxt[degree]=nxt.get(degree,0)+weight*(-1)**j*math.comb(multiplicity,j)
        shift={s:v for s,v in nxt.items() if v}
    ell=len(caps)
    return sum(c*math.comb(total-s+ell-1,ell-1) for s,c in shift.items())


def layer_sample(rng,w,ell,S):
    # All vectors accepted with same weight 1/w^(ell-1); last coordinate determined.
    while True:
        first=[rng.randrange(w) for _ in range(ell-1)]
        last=S-sum(first)
        if 0<=last<w:
            return tuple(first+[last])


def covered_count(vectors,w,S):
    minima=[min(col) for col in zip(*vectors)]
    total=S-sum(minima)
    caps=[w-1-mi for mi in minima]
    n=count_dp(total,caps)
    assert n==count_ie(total,caps)
    return n


def summarize_probabilities(ps):
    vals=[-math.log2(p) for p in ps if p>0]
    return dict(samples=len(ps), bits_of_sample_mean=-math.log2(statistics.fmean(ps)),
                median_sample_bits=statistics.median(vals),
                minimum_sample_bits=min(vals),maximum_sample_bits=max(vals),
                meaning="Monte Carlo sample statistic over independently uniform hypothetical reused encodings; NOT a security bound")


def wots_checks(samples):
    rng=random.Random(SEED)
    out=[]
    for w,ell,S in ((16,32,240),(256,16,2040)):
        layer=count_dp(S,[w-1]*ell)
        assert layer==count_ie(S,[w-1]*ell)
        examples=[]
        one=[w//2-1]*(ell//2)+[w//2]*(ell//2)
        assert sum(one)==S and covered_count([one],w,S)==1
        for j in (2,3):
            inclusive=[]
            distinct=[]
            for trial in range(samples):
                sigs=[layer_sample(rng,w,ell,S) for _ in range(j)]
                n=covered_count(sigs,w,S)
                unseen=n-len(set(sigs))
                assert n>=len(set(sigs))
                inclusive.append(n/(w**ell))
                distinct.append(unseen/(w**ell))
                if trial<2:
                    examples.append(dict(j=j,vectors=sigs,covered_inclusive=str(n),
                                         distinct_observed=len(set(sigs)),covered_excluding_observed=str(unseen)))
            out.append(dict(w=w,ell=ell,S=S,j=j,slice_count=str(layer),
                            slice_bits=math.log2(layer),acceptance_bits=ell*math.log2(w)-math.log2(layer),
                            inclusive=summarize_probabilities(inclusive),
                            exclusive=summarize_probabilities(distinct),examples=examples[-2:]))
    return out


def validate_counts():
    rng=random.Random(SEED+1)
    tests=300
    for _ in range(tests):
        ell=rng.randint(2,8)
        caps=[rng.randrange(0,20) for _ in range(ell)]
        total=rng.randrange(sum(caps)+2)
        assert count_dp(total,caps)==count_ie(total,caps)
    ell,w,S=4,4,6
    layer=[x for x in itertools.product(range(w),repeat=ell) if sum(x)==S]
    for a in layer:
        assert covered_count([a],w,S)==1
        for b in layer:
            m=tuple(map(min,zip(a,b)))
            brute=sum(all(y>=mi for y,mi in zip(x,m)) for x in layer)
            assert brute==covered_count([a,b],w,S)
    return dict(random_dp_ie_checks=tests,toy_all_pair_checks=len(layer)**2,
                toy_antichain_checks=len(layer),mismatches=0)


def wilson(success,trials,z=3.2905267314919255):
    p=success/trials
    den=1+z*z/trials
    centre=(p+z*z/(2*trials))/den
    rad=z*math.sqrt(p*(1-p)/trials+z*z/(4*trials*trials))/den
    return [max(0,centre-rad),min(1,centre+rad)]


def toy_checks(trials):
    rng=random.Random(SEED+2)
    h,a,k,q=8,3,4,256
    successes=0
    for _ in range(trials):
        r=sum(rng.randrange(1<<h)==0 for _ in range(q))
        sets=[{rng.randrange(1<<a) for _ in range(r)} for _ in range(k-1)]
        target=[rng.randrange(1<<a) for _ in range(k)]
        successes+=int(target[-1]==0 and all(t in s for t,s in zip(target,sets)))
    exact=float(fors_moment(q,h,a,k))
    ci=wilson(successes,trials)
    assert ci[0]<=exact<=ci[1],(exact,ci)
    # Fixed cohort of 64 hypothetical twice-signed WOTS toy keys; direct raw-digest trials.
    w,ell,S=4,8,12
    cohort=[[layer_sample(rng,w,ell,S) for _ in range(2)] for _ in range(64)]
    counts=[covered_count(v,w,S) for v in cohort]
    exact_w=statistics.fmean(counts)/(w**ell)
    succ_w=0
    for _ in range(trials):
        vectors=cohort[rng.randrange(len(cohort))]
        target=tuple(rng.randrange(w) for _ in range(ell))
        minima=tuple(map(min,zip(*vectors)))
        succ_w+=int(sum(target)==S and all(y>=mi for y,mi in zip(target,minima)))
    ci_w=wilson(succ_w,trials)
    assert ci_w[0]<=exact_w<=ci_w[1],(exact_w,ci_w)
    return dict(confidence="99.9% Wilson intervals, fixed seed; model validation, not a EUF experiment",
                FORS=dict(h=h,a=a,k=k,q=q,trials=trials,successes=successes,exact=exact,
                          measured=successes/trials,ci=ci,formula_within_interval=True),
                WOTS=dict(w=w,ell=ell,S=S,hypothetical_two_signature_cohort=64,trials=trials,
                          successes=succ_w,exact_conditional_on_cohort=exact_w,
                          measured=succ_w/trials,ci=ci_w,formula_within_interval=True))


def inventories():
    heights=[5,5,5,5,21]
    rows=[]
    below=0
    for i,height in enumerate(heights):
        trees=1<<(41-below-height)
        keys=trees*(1<<height)
        ell=32 if i<4 else 16
        rows.append(dict(layer=i,height=height,below=below,subtrees=trees,wots_keys=keys,
                         total_merkle_positions=trees*((1<<(height+1))-1),
                         internal_merkle_nodes=trees*((1<<height)-1),secret_chain_starts=keys*ell,
                         distinct_honest_child_messages_per_address=1))
        below+=height
    return dict(layers=rows,FORS_instances=1<<41,FORS_real_trees_per_instance=17,
                FORS_leaf_secrets_total=(1<<41)*17*(1<<9),
                WOTS_chain_secrets_total=sum(r['secret_chain_starts'] for r in rows),
                total_PRF_secret_input_universe=(1<<41)*17*(1<<9)+sum(r['secret_chain_starts'] for r in rows),
                top_cache_nodes=(1<<22)-1,top_cache_counters=1<<21,
                top_cache_bytes=((1<<22)-1)*16+(1<<21)*4,
                note="Whole universe cardinalities, NOT reduction oracle-query counts or proven security loss factors")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--samples',type=int,default=128)
    ap.add_argument('--toy-trials',type=int,default=30000)
    ap.add_argument('--h',type=int,default=41)
    ap.add_argument('--a',type=int,default=9)
    ap.add_argument('--k',type=int,default=18)
    args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for logq in Q_EXPONENTS:
        q=1<<logq
        b=fors_moment(q,args.h,args.a,args.k,dps=160)
        b2=fors_moment(q,args.h,args.a,args.k,dps=220)
        p=fors_moment(q,args.h,args.a,args.k,poisson=True,dps=160)
        with mp.workdps(220):
            precision_relative_error=abs(b-b2)/b2
            assert precision_relative_error<mp.mpf('1e-90')
        bp=fors_positive(q,args.h,args.a,args.k)
        pp=fors_positive(q,args.h,args.a,args.k,poisson=True)
        assert abs(bits(b)-bp['bits'])<1e-10
        assert abs(bits(p)-pp['bits'])<1e-10
        if logq==40:
            assert abs(bits(b)-bits(p))<0.01
        rows.append(dict(log2_signatures=logq,q=str(q),component_status="COMPUTED fixed-instance model; NOT established adaptive EUF bound",
                         FORS_binomial_per_try=textnum(b),FORS_binomial_bits=bits(b),
                         FORS_poisson_per_try=textnum(p),FORS_poisson_bits=bits(p),
                         binomial_poisson_difference_bits=bits(b)-bits(p),
                         binomial_positive_check=bp,poisson_positive_check=pp,
                         precision_relative_error_160_vs_220_dps=textnum(precision_relative_error),
                         conditional_union_budget=[dict(log2_Q_H=l,bits_advantage_upper_bound=max(0,bits(b)-l),
                             caveat="ONLY if a reduction supplies this per-query upper bound; no such reduction established here") for l in (0,32,64,128)],
                         total_euf_probability=None,total_euf_bits=None,total_status="OPEN / not established",
                         WOTS_different_message_reuse_event_reference=0,
                         WOTS_all_other_attack_terms=None,PRF_term=None,tree_term=None,H_msg_term=None))
        print(f'q=2^{logq}: FORS binomial {bits(b):.12f} bits; Poisson {bits(p):.12f}; total OPEN',flush=True)
    result=dict(parameters=dict(n_bytes=16,h=args.h,a=args.a,k=args.k,k_real=args.k-1),
                seed=SEED,dependency=dict(mpmath=mp.__version__),
                formula_scope="independent honest occupancy / fixed-instance random digest coverage",
                rows=rows,exact_count_validation=validate_counts(),
                WOTS_hypothetical_reuse_statistics=wots_checks(args.samples),
                toy_validation=toy_checks(args.toy_trials),inventories=inventories(),
                verdict="not established: full reference EUF-CMA and QROM bounds are OPEN",
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (args.out/'bounds.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    lines=['# Component results','', 'All FORS entries are fixed-instance model computations. Total EUF-CMA is OPEN.', '',
           '| signatures q | FORS binomial bits per try | FORS Poisson bits per try | conditional advantage exponent for Q_H=2^128 | total EUF bits |',
           '|---|---:|---:|---:|---|']
    for r in rows:
        lines.append(f"| 2^{r['log2_signatures']} | {r['FORS_binomial_bits']:.9f} | {r['FORS_poisson_bits']:.9f} | {max(0,r['FORS_binomial_bits']-128):.9f} | OPEN |")
    lines += ['', 'The Q_H column is budget arithmetic under an unproved per-query upper-bound premise, not a complete forgery bound.', '',
              'Exact DP and inclusion-exclusion checks passed. Toy formula checks fall within the reported 99.9% Wilson intervals.',
              'Hypothetical WOTS reuse statistics do not apply to the honest reference signer: each complete WOTS address signs one fixed child value.',
              'One signature still admits one inclusive encoding (probability 2^-128 per raw encoding hash); fresh input collisions are not excluded by an antichain.']
    (args.out/'bounds.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(dict(count_validation=result['exact_count_validation'],toy=result['toy_validation']),indent=2),flush=True)


if __name__=='__main__':
    main()

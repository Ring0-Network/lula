"""Exact finite probability/reflection controls only; no source or real hash search."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb,isqrt
import json
import mpmath as mp

mp.mp.dps=100
HERE=Path(__file__).resolve().parent

def binomial(n,p,k):
    return F() if not 0<=k<=n else comb(n,k)*p**k*(1-p)**(n-k)

def row_counts(N):
    D=N+1;alphabet=2*N
    accumulated=[0]*(N+1)
    conditional=[]
    for outside,Y in product(range(2),range(alphabet)):
        planted=outside
        other=[i for i in range(D) if i!=planted]
        shift=(Y//2)%N
        order=other[shift:]+other[:shift]
        contains=((Y&1)^outside)==0
        row=([planted]+order[:N-1]) if contains else order
        assert len(row)==N and len(set(row))==N
        counts=[0]*(N+1)
        for images in product(range(alphabet),repeat=N):
            h=dict(zip(other,images));h[planted]=Y
            M=sum(h[i]//2==Y//2 for i in row)
            counts[M]+=1;accumulated[M]+=1
        denominator=alphabet**N
        probabilities=[F(c,denominator) for c in counts]
        expected=[binomial(N-1,F(1,N),m-1) if contains
                  else binomial(N,F(1,N),m) for m in range(N+1)]
        assert probabilities==expected
        p1=F(N-1,N)**(N-1)
        assert probabilities[1]==p1>F(1,3)
        conditional.append({'outside':outside,'full_image':Y,'contains_planted':contains,
                            'M_distribution':[str(v) for v in probabilities]})
    total=2*alphabet**(N+1)
    mixed=[F(c,total) for c in accumulated]
    included=[binomial(N-1,F(1,N),m-1) for m in range(N+1)]
    excluded=[binomial(N,F(1,N),m) for m in range(N+1)]
    assert mixed!=included and mixed!=excluded
    assert mixed==[(a+b)/2 for a,b in zip(included,excluded)]
    # Exact Sigma-event factorization: choose any deterministic subset ofSigma.
    picked=[r for r in conditional if r['outside']==0 or r['full_image']%3==0]
    pSigma=F(len(picked),len(conditional))
    joint=sum((F(r['M_distribution'][1]) for r in picked),F())/len(conditional)
    assert joint==pSigma*F(N-1,N)**(N-1)
    return {'N':N,'worlds':total,'conditional_rows':conditional,
            'unconditional_mixture':[str(v) for v in mixed],
            'singleton_probability':str(mixed[1]),'Sigma_event_probability':str(pSigma),
            'Sigma_and_singleton_probability':str(joint),'all_checks_passed':True}

def bad_controls():
    # Noninjective row of two copies of one residual point: M never equals1.
    duplicate=[sum(prefix==0 for _ in range(2)) for prefix in range(2)]
    assert duplicate==[2,0]
    # An allegedly outside variable stores residual match bits; row never
    # inspects H directly but its selection is correlated with residual H.
    counts=[0,0,0]
    for matches in product((0,1),repeat=3):
        marked=[i for i,b in enumerate(matches) if b]
        unmarked=[i for i,b in enumerate(matches) if not b]
        row=(marked+unmarked)[:2]
        counts[sum(matches[i] for i in row)]+=1
    assert F(counts[1],8)==F(3,8)!=F(1,2)
    # High prerequisites with disjoint rare failures need only union bound.
    universe=set(range(128));A=universe-{0};B=universe-{1};M= set(range(64))
    pA=F(len(A),128);pB=F(len(B),128);pAB=F(len(A&B),128)
    joint=F(len(A&B&M),128);pM=F(1,2)
    assert pA>F(31,32) and pB>F(31,32)
    assert pAB>F(15,16) and pAB<pA*pB
    assert joint==F(31,64)<pM*pAB
    assert joint>=pM-(1-pA)-(1-pB)
    return {'duplicate_row_singleton_probability':'0',
            'correlated_outside_row_singleton_probability':'3/8',
            'prerequisite_marginals':[str(pA),str(pB)],
            'prerequisite_joint':str(pAB),'unjustified_product':str(pA*pB),
            'prerequisites_and_singleton':str(joint),
            'unjustified_singleton_product':str(pM*pAB),'all_negative_controls_passed':True}

def reflection_controls():
    rows=[]
    for N in (4,16,64,256):
        s=isqrt(N);assert s*s==N
        for final_check in (False,True):
            t=s//2 if not final_check else (s-1)//2
            # Represent normalized uniform state by equal rational amplitudes1;
            # its squared norm is N and is preserved by both reflections.
            amplitudes=[F(1)]*N
            for _ in range(t):
                amplitudes[0]*=-1
                mean=sum(amplitudes,F())/N
                amplitudes=[2*mean-v for v in amplitudes]
                assert sum((v*v for v in amplitudes),F())==N
            success=amplitudes[0]**2/N
            theta=mp.asin(1/mp.sqrt(N))
            closed=mp.sin((2*t+1)*theta)**2
            exact=mp.mpf(success.numerator)/success.denominator
            assert abs(exact-closed)<mp.mpf('1e-90')
            cost=2*t+int(final_check)
            assert cost<=s
            if not final_check or s>=8:assert success>F(1,2)
            rows.append({'N':N,'Q':s,'phases':t,'queries_per_phase':2,
                         'final_check_charged':final_check,'total_query_cost':cost,
                         'singleton_success_exact':str(success),
                         'singleton_success_decimal':mp.nstr(exact,40),'PASS':True})
    # Complete-image XOR/compare/uncompute on finite basis returns clean work.
    clean=0
    words=[0,3,4,7]
    for index in range(4):
        work=0
        work^=words[index]
        phase=-1 if work//2==0 else 1
        work^=words[index]
        assert work==0 and phase==(-1 if index==0 else 1)
        clean+=1
    N=2**128;s=2**64;theta=mp.asin(mp.mpf(1)/s)
    large=[]
    for final_check in (False,True):
        t=s//2 if not final_check else (s-1)//2
        probability=mp.sin((2*t+1)*theta)**2
        assert probability>mp.mpf('0.5') and 2*t+int(final_check)<=s
        large.append({'N':str(N),'Q':str(s),'phases':str(t),
                      'final_check_charged':final_check,
                      'query_cost':str(2*t+int(final_check)),
                      'success_decimal':mp.nstr(probability,70)})
    return {'finite_exact_reflections':rows,'clean_full_image_phase_basis_checks':clean,
            'large_N_analytic_evaluation':large,'all_checks_passed':True}

def main():
    out={'status':'PASS_ABSTRACT_CONDITIONED_ROW_UNION_AND_REFLECTION_CONTROLS',
         'scope':'generic finite function sampler and reflection matrix only; source binding outside audit; no signatures, attack implementation or actual hash search',
         'row_samplers':[row_counts(n) for n in (2,3,4)],
         'negative_controls':bad_controls(),'amplification':reflection_controls()}
    (HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS: conditional binomial/included laws and mixtures, singleton/Sigma identity, >1/3, correlated prerequisite controls, exact two-query phase/reflection checks. Source binding OUTSIDE audit.')

if __name__=='__main__':main()

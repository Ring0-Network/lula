"""Probability/AA successor checks only; source-to-abstract binding excluded."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib
import json
import mpmath as mp

mp.mp.dps=100
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root-preimage-criterion'/'DEPENDENCY_SUCCESSOR.md'
PIN='b403d39ccf66455acb6c5dc6776a98fdca397ec6e087ac80578d0049cd3b7249'

def count_ie(ell,w,total):
    return sum((-1)**j*comb(ell,j)*comb(total-j*w+ell-1,ell-1)
               for j in range(min(ell,total//w)+1))

def count_dp(ell,w,total):
    previous=[1]+[0]*total
    for _ in range(ell):
        current=[];window=0
        for s in range(total+1):
            window+=previous[s]
            if s>=w:window-=previous[s-w]
            current.append(window)
        previous=current
    return previous[total]

def main():
    assert hashlib.sha256(ROOT.read_bytes()).hexdigest()==PIN
    N=2**128;s=2**64;L=2**20;C=2**32;top=2**21
    B=6*L+3217+1+3224
    assert B==6297898
    t=(s-B)//2
    assert B+2*t==s
    assert 2*t+1==s-B+1
    # An exact lower angle suffices, with no numerical sine certification.
    assert 20*(B-1)<s
    lower=F(19,20)
    lower_sine=lower-lower**3/6
    assert lower_sine>F(4,5)
    # theta>=1/s and angle<=the already proved(s+1)asin(1/s)<=pi/2.
    # Therefore sin(angle)>4/5 and its square>16/25.
    theta=mp.asin(mp.mpf(1)/s)
    angle=(2*t+1)*theta
    success=mp.sin(angle)**2
    assert success>mp.mpf(16)/25
    pn=mp.exp((N-1)*mp.log1p(-mp.mpf(1)/N))
    assert pn>mp.exp(-1)>mp.mpf(1)/3
    accept_probabilities={}
    for label,ell,w,S in [('lower',32,16,240),('top',16,256,2040)]:
        count=count_ie(ell,w,S)
        assert count==count_dp(ell,w,S)
        denominator=w**ell
        assert count*1024>denominator
        accept_probabilities[label]={'ell':ell,'w':w,'target_sum':S,
            'exact_count':str(count),'denominator':str(denominator),
            'probability_exact':str(F(count,denominator)),
            'probability_above_1_over_1024':True,
            'qualifier':'combinatorics for independent uniform digits only; actual stagewise sampling/source dependency binding outside audit'}
    # Conditional per-row probability at least1/1024 => these failurebounds.
    A_failure_upper=6*mp.exp(-mp.mpf(L)/1024)
    T_failure_upper=top*mp.exp(-mp.mpf(C)/1024)
    assert A_failure_upper<mp.mpf(1)/32 and T_failure_upper<mp.mpf(1)/32
    joint=F(1)-F(1,32)-F(1,32)
    retained=joint*F(1,3)*F(16,25)
    assert joint==F(15,16) and retained==F(1,5)
    old_product=F(31,32)**2*F(1,3)*F(16,25)
    assert old_product==F(961,4800)>retained
    out={'status':'PASS_SUCCESSOR_PROBABILITY_AND_AA_ARITHMETIC_CONDITIONAL_ON_DECLARED_ABSTRACT_SAMPLER',
      'reviewed_successor_sha256':PIN,'source_to_abstract_binding':'OUTSIDE_THIS_AUDIT_NOT_VALIDATED',
      'N':str(N),'Q':str(s),'preprocessing_limit':L,'overhead_B':B,
      'phase_iterations':str(t),'two_queries_per_phase_total_with_given_overhead':str(B+2*t),
      'exact_lower_angle':'19/20','exact_Taylor_lower_sine':str(lower_sine),
      'Taylor_lower_sine_above':'4/5','conditional_singleton_success_lower':'strictly16/25',
      'conditional_singleton_probability_lower':'strictly1/3',
      'analytic_singleton_probability':mp.nstr(pn,75),
      'analytic_amplification_success':mp.nstr(success,75),
      'A_failure_bound_assuming_stagewise_row_blindness':mp.nstr(A_failure_upper,35),
      'T_failure_bound_assuming_top_row_success_law':mp.nstr(T_failure_upper,35),
      'uniform_digit_acceptance_combinatorics':accept_probabilities,
      'joint_prerequisite_lower':'strictly15/16',
      'retained_abstract_success_lower':'strictly1/5',
      'unpromoted_product_constant':str(old_product),
      'prerequisite_singleton_multiplication_condition':'T and A Sigma-measurable with residual H conditionally iid uniform',
      'query_overhead_source_counts':'treated as given abstract ledger assumptions; no source program constructed or audited',
      'actual_source_forgery_claim':'NOT_VALIDATED_BY_THIS_MATHEMATICAL_AUDIT'}
    (HERE/'SUCCESSOR-CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS: successor union/singleton/overhead/AA arithmetic; strict abstract1/5 conditional on declared sampler. Source binding OUTSIDE audit.')

if __name__=='__main__':main()

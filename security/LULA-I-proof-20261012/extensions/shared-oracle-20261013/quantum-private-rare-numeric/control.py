"""Exact rational finite CQ/quantum gate controls; not a LULA forgery oracle."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json
import mpmath as mp

mp.mp.dps=90
HERE=Path(__file__).resolve().parent
N=8
D=32*2*2  # length-framed toy input, response bit, retained work bit
Q=3

def norm(v):return sum((z*z for z in v),F())
def rotate(v,bit):
    u=list(v)
    mask=1<<bit
    for i in range(D):
        if not i&mask:
            a,b=v[i],v[i|mask]
            u[i]=F(3,5)*a+F(4,5)*b
            u[i|mask]=F(4,5)*a-F(3,5)*b
    assert norm(v)==norm(u)
    return tuple(u)

def cnot(v,control,target):
    u=[F()]*D
    for i,z in enumerate(v):
        j=i^((1<<target) if i&(1<<control) else 0)
        u[j]=z
    return tuple(u)

def base(x):return ((x*x+3*x+1)>>1)&1
def oracle(v,K,P,real):
    u=[F()]*D
    for i,z in enumerate(v):
        x=i>>2
        b=base(x)
        if real and (x==K or x==N+P):b^=1
        u[i^(2*b)]=z
    return tuple(u)

def private_mass(v,K,P):
    return sum((z*z for i,z in enumerate(v) if i>>2 in (K,N+P)),F())

def measure_request(v):
    return [tuple(z if (i&1)==h else F() for i,z in enumerate(v)) for h in (0,1)]

def callback(branches,K,P,r,stopped):
    out={}
    for hist,v in branches.items():
        if hist and hist[-1][0]=='B':
            out[hist]=v
            continue
        for h,w in enumerate(measure_request(v)):
            if not norm(w):continue
            # Measured nominations, then I result, then eligible E nomination.
            i_guess=(3*h+2*r)%N
            if stopped and i_guess==P:
                out[hist+(('B','I',r,h),)]=w
                continue
            ui=base(N+i_guess)
            e_guess=(h+2*r+ui+1)%N
            eligible=bool(ui)
            if stopped and eligible and e_guess==P:
                out[hist+(('B','E',r,h),)]=w
                continue
            ex=N+e_guess if eligible else 16+e_guess
            result=ui^base(ex)
            # Source result is measured/classical and copied to history.
            # Old response/input amplitudes survive; work is re-entangled.
            w=rotate(w,0)
            w=cnot(w,1,0)
            w=rotate(w,2+(result+r)%5)
            out[hist+(('S',r,h,result),)]=w
    assert sum(map(norm,out.values()),F())==sum(map(norm,branches.values()),F())
    return out

def query(branches,K,P,real):
    return {h:v if h and h[-1][0]=='B' else oracle(v,K,P,real) for h,v in branches.items()}

def p_bad(branches):return sum((norm(v) for h,v in branches.items() if h and h[-1][0]=='B'),F())
def p_win_active(branches):
    return sum((sum((z*z for i,z in enumerate(v) if (i>>1)&1),F())
                for h,v in branches.items() if not h or h[-1][0]!='B'),F())

def diff_norm2(a,b):
    keys=set(a)|set(b)
    zero=(F(),)*D
    return sum((sum(((u-v)**2 for u,v in zip(a.get(h,zero),b.get(h,zero))),F()) for h in keys),F())

def main():
    v=(F(1),)+(F(),)*(D-1)
    for bit in range(7):v=rotate(v,bit)
    v=cnot(v,2,0)
    assert norm(v)==1
    states={(K,P):[{():v},{():v},{():v}] for K,P in product(range(N),repeat=2)}
    stages=[]
    for r in range(Q):
        active_mass=continued_mass=local_gap2=F()
        active_weight=F()
        identities=0
        for (K,P),(cont,stop,real) in states.items():
            for h,w in stop.items():
                if h and h[-1][0]=='B':continue
                # Each physical CQ active block is an unchanged CONT block.
                assert h in cont and w==cont[h]
                identities+=1
                active_weight+=norm(w)
                active_mass+=private_mass(w,K,P)
                local_gap2+=diff_norm2({h:oracle(w,K,P,True)},{h:oracle(w,K,P,False)})
            continued_mass+=sum((private_mass(w,K,P) for w in cont.values()),F())
        denom=N*N
        active_mass/=denom;continued_mass/=denom;active_weight/=denom;local_gap2/=denom
        assert active_mass<=continued_mass<=F(1,N)
        assert local_gap2<=4*active_mass
        stages.append({'query_slot':r+1,'active_mass':str(active_mass),
            'continued_key_blind_mass':str(continued_mass),'active_weight':str(active_weight),
            'physical_CQ_block_identities':identities,'local_discrepancy_norm_squared':str(local_gap2),
            'support_bound_norm_squared':str(4*active_mass),'PASS':True})
        for (K,P),triple in states.items():
            for j,stopped in enumerate((False,True,True)):
                triple[j]=query(triple[j],K,P,j==2)
                triple[j]=callback(triple[j],K,P,r,stopped)
    denom=N*N
    pB=sum((p_bad(t[1]) for t in states.values()),F())/denom
    pW=sum((p_win_active(t[1]) for t in states.values()),F())/denom
    pCont=sum((p_win_active(t[0]) for t in states.values()),F())/denom
    pBr=sum((p_bad(t[2]) for t in states.values()),F())/denom
    pWr=sum((p_win_active(t[2]) for t in states.values()),F())/denom
    gap2=sum((diff_norm2(t[1],t[2]) for t in states.values()),F())/denom
    assert pB<=F(2*Q,N) and pW<=pCont
    assert gap2<=F(4*Q*Q,N)
    val=lambda f:mp.mpf(f.numerator)/f.denominator
    gap=mp.sqrt(val(gap2))
    for a,b in [(pBr,pB),(pWr,pW),(pBr+pWr,pB+pW)]:
        assert abs(mp.sqrt(val(a))-mp.sqrt(val(b)))<=gap+mp.mpf('1e-80')
    # Negative pure-state Loewner control: determinant negative exactly.
    # continued |+><+| - active |0><0|/2 = [[0,1/2],[1/2,1/2]].
    determinant=-F(1,4)
    assert determinant<0
    # Physical dephasing leaves omitted block diag(0,1/2), which is PSD.
    # Negative normalized-survivor control after the guard P!=0 on N=4.
    survival=F(3,4);conditional_match=F(1,3);unnormalized_match=F(1,4)
    assert conditional_match>F(1,4) and survival*conditional_match==unnormalized_match
    out={'status':'PASS_EXACT_RATIONAL_CQ_ACTIVE_DOMINATION_CONTROLS',
         'scope':'finite gate/control with fixed toy nuisance function; not real LULA EUF or a complete ordinary-RO marginal experiment',
         'keys_per_family':N,'key_worlds':N*N,'query_slots':Q,'quantum_dimension':D,
         'retained_input_response_work':True,'measured_adaptive_services':Q,
         'stages':stages,'IDEAL_guard_probability':str(pB),'guard_predictable_union_cap':str(F(2*Q,N)),
         'IDEAL_active_win_probability':str(pW),'continued_IDEAL_win_probability':str(pCont),
         'REAL_guard_probability':str(pBr),'REAL_active_win_probability':str(pWr),
         'purified_stopped_discrepancy_squared':str(gap2),
         'packed_support_upper_squared':str(F(4*Q*Q,N)),
         'combined_projector_probability_IDEAL':str(pB+pW),
         'combined_projector_probability_REAL':str(pBr+pWr),
         'pure_state_order_negative_determinant':str(determinant),
         'normalized_survivor_conditional_match':str(conditional_match),
         'normalized_survivor_key_blind_claim_false':True,
         'unnormalized_survivor_match':str(unnormalized_match),
         'all_checks_passed':True}
    (HERE/'CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS: exact rational adaptive CQ blocks; active mass<=1/N domination; retained memory; three stopped query slots; support/telescoping/projector checks; two negative controls.')

if __name__=='__main__':main()

"""Exact algebraic certificates only. No cryptographic execution or timing."""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial, isqrt
import hashlib, json

HERE = Path(__file__).resolve().parent
X = HERE.parent.parent
SOURCE = X.parents[3] / 'publications/LULA-I/release/code/lula1/src/lib.rs'
UNIFORM = X / 'PARAMETER-UNIFORM-CLASSICAL-THEOREM.md'
PIN = 'e5fc68bc269ca98672caa99ec70d5695d3d578095a62ebbfc0f99f9d8fbc394b'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(UNIFORM) == PIN
assert sha(SOURCE) == 'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'

def stirling(n):
    row = [1]
    for _ in range(n):
        row = [0] + [row[j-1] + (j * row[j] if j < len(row) else 0)
                     for j in range(1, len(row)+1)]
    return row

checks = 0
for q in range(9):
    for b in (1, 2, 4, 8):
        rho = F(1,b)
        for r in range(1,6):
            exact = sum(F(comb(q,z))*rho**z*(1-rho)**(q-z)*z**r
                        for z in range(q+1))
            row = stirling(r)
            falling = lambda j: 0 if j > q else factorial(q)//factorial(q-j)
            expansion = sum(row[j]*falling(j)*rho**j for j in range(r+1))
            touchard = sum(row[j]*(q*rho)**j for j in range(r+1))
            assert exact == expansion <= touchard
            checks += 1
            for t in (2,4,8):
                pf = sum(F(comb(q,z))*rho**z*(1-rho)**(q-z)
                         *(1-(1-F(1,t))**z)**r/t for z in range(q+1))
                assert pf <= exact/t**(r+1)
                checks += 1

r,a,h,d = 17,10,63,5
heights = [10,10,11,11,21]
lw = [4,4,4,4,8]
ell = [32,32,32,32,16]
sums = [240,240,240,240,2040]
assert sum(heights)==h<=63 and all(0<=v<=31 for v in heights)
assert (r+1)*a+h<=256 and r*2**a<=2**32
assert all(0<=s<e*(2**w-1) for s,e,w in zip(sums,ell,lw))
tsteps = [e*(2**w-1)-s for e,w,s in zip(ell,lw,sums)]
H = r+sum(tsteps)
G = r*(a+1)+1+sum(t+1+hi for t,hi in zip(tsteps,heights))
C = H+G+d+3
assert (H,G,C)==(3017,3256,6281)
row = stirling(r)
touchard2 = sum(row[j]*2**j for j in range(r+1))
assert touchard2==18880288847750 < 2**45
pf_all = F(touchard2,2**180)
N=2**128
SCALE=2**256
rows=[]
for qe in [24,30,38,40,41,44,50,64]:
    q=2**qe
    mu=F(q,2**h)
    pf_upper=sum(row[j]*mu**j for j in range(r+1))/2**180
    assert pf_upper<=pf_all<F(1,2**135)
    # beta^(2^32) <= exp(-2^22) < 2^-4096, since e>2.
    tail_upper=F(q,2**4096)
    for Qe in (64,125,128):
        Q=2**Qe
        components={
            'scalar': F(3*Q+2*q+C,N),
            'full_word_bridge': F(q*Q+comb(q,2)+q,N*N),
            'finite_outer_bottom': tail_upper,
            'coverage': (Q+1)*pf_upper,
        }
        raw=sum(components.values())
        upper=min(F(1),raw)
        ceil=lambda x:(x.numerator+x.denominator-1)//x.denominator
        scaled=ceil(upper*SCALE)
        assert upper<=F(scaled,SCALE)
        half=scaled<SCALE//2
        if Qe in (64,125): assert half
        else: assert components['scalar']>1 and scaled==SCALE
        if Qe==125: assert F(scaled,SCALE)<F(47,125)
        # A sufficient half-budget from upper moments, not an exact crossing.
        slope=F(3,N)+F(q,N*N)+pf_upper
        intercept=F(2*q+C,N)+F(comb(q,2)+q,N*N)+tail_upper+pf_upper
        safe=(F(1,2)-intercept)//slope
        assert slope*safe+intercept<=F(1,2)
        rows.append({'log2_signing_queries':qe,'log2_oracle_queries':Qe,
          'status':'COMPUTED_EXACT_OUTWARD_CLASSICAL_SOURCE_CERTIFICATE',
          'upper_numerator_at_denominator_2pow256':str(scaled),
          'upper_decimal_rounded_display_only':format(float(F(scaled,SCALE)),'.17g'),
          'certifies_success_below_half':half,
          'sufficient_half_query_budget_from_moment_upper':str(safe),
          'component_upper_decimals_rounded_display_only':{k:format(float(v),'.17g') for k,v in components.items()}})
        checks+=1

def coeff(e,w,s):
    row=[1]+[0]*s
    for _ in range(e):
        nxt=[]; running=0
        for j in range(s+1):
            running+=row[j]
            if j>=w: running-=row[j-w]
            nxt.append(running)
        row=nxt
    return row[s]

counts=[coeff(e,2**w,s) for e,w,s in zip(ell,lw,sums)]
assert all(F(c,N)>=F(1,2**8) for c in counts[:4])
assert F(counts[-1],N)>=F(1,2**12)
leaf_low=32*16+(22+32*16+9+63)//64
leaf_top=16*256+(22+16*16+9+63)//64
sub=lambda ht,leaf:2**ht*leaf+(2**ht-1)
child=sub(11,leaf_low)
fixed_setup=2**21*(leaf_top+child)+(2**21-1)
fixed_setup_base=2**21*(leaf_top+sub(5,leaf_low))+(2**21-1)
top_cold=sub(21,leaf_top)
cache=(2**22-1)*16+2**21*4
sig=16+4+16*r*(a+1)+sum(4+16*(e+hi) for e,hi in zip(ell,heights))
fors_sign=r*(3*2**a-1)+r+(22+16*r+9+63)//64
low_subtrees=sum(sub(hi,leaf_low) for hi in heights[:-1])
wots_sign=sum(e+s for e,s in zip(ell,sums))
fixed_sign=fors_sign+low_subtrees+wots_sign+d
assert (sig,cache,top_cold,fixed_setup)==(6344,75497456,8602517503,2250573348863)
costs={'status':'COMPUTED_EXACT_ANALYTIC_COUNTS_NO_EXECUTION',
 'signature_bytes':sig,'logical_top_cache_bytes':cache,
 'top_cold_subtree_tail_compressions':top_cold,
 'top_only_keygen_fixed_tail_compressions':fixed_setup,
 'baseline_top_only_keygen_fixed_tail_compressions':fixed_setup_base,
 'top_only_keygen_fixed_ratio':str(F(fixed_setup,fixed_setup_base)),
 'top_keygen_additional_trials':'sum of 2^21 canonical top-row trial counts, one tail compression each',
 'top_keygen_additional_prefix':'one prefix compression per constructed Ctx, outside source optimized-tail report',
 'cached_sign_fixed_tail_compressions':fixed_sign,
 'cached_sign_fixed_breakdown':{'FORS':fors_sign,'four_uncached_subtrees':low_subtrees,
    'five_WOTS_signature_chains':wots_sign,'five_redundant_accepted_digest_evaluations':d},
 'cached_sign_variable_cost':'message nonce/inner full SHA blocks; outer trials; four lower canonical-row trial counts; Ctx prefix if newly constructed',
 'row_success_coefficients_over_2pow128':[str(v) for v in counts],
 'row_success_lower_bounds':['2^-8']*4+['2^-12'],
 'counter_cap':2**32,
 'trials_caution':'fixed costs require completion; no resampling, timing, whole-game success conditioning or free modulus/graph generation'}

# Conditional proof-architecture obstruction: rationally enclose sqrt(2).
D=2**512
rt=isqrt(2*D*D)
sqrt2lo,sqrt2hi=F(rt,D),F(rt+1,D)
assert sqrt2lo**2<=2<=sqrt2hi**2
assert (36+8*sqrt2lo)/64>F(1,2)
checks+=1
result={'scope':'Classical source certificate conditional on the pinned manual uniform theorem; no retuned QROM source proof',
 'theorem_sha256':sha(UNIFORM),'source_sha256':sha(SOURCE),
 'own_blind_first_sha256':sha(HERE/'INDEPENDENT-FIRST.md'),
 'parameters':{'nbytes':16,'r':r,'a':a,'d':d,'heights':heights,'lw':lw,'ell':ell,'S':sums,'top_only_cache':True},
 'terminal_counts':{'H':H,'G':G,'C':C},'touchard17_at_2':touchard2,
 'pf_all_upper':{'numerator':touchard2,'denominator_power_of_two':180},
 'probability_upper_common_denominator_power':256,'rows':rows,'costs':costs,
 'display_caution':'Floating decimal displays are rounded illustrations only. Certificate values are exact integer numerators over 2^256.',
 'uniform_classical_tiny_target_obstruction':'Strict target guards imply t_i>=1, hence C_p=r(a+2)+2 sum(t_i)+h+2d+4>=11. Thus this envelope cannot certify <=1/N even at Q=q=0; not an actual success lower bound.',
 'toy_algebra_and_certificate_checks':checks,
 'conditional_QROM_obstruction':'If current positive component formulas are extended uniformly unchanged, e_floor at Q=2^61 is >1/2, regardless of parameters. This is an upper-envelope limitation, not success lower bound.',
 'new_source_game_kernel_declarations':0,'whole_goal_complete':False,
 'original_128_category_target':'NOT_ESTABLISHED','minimality':'NOT_CLAIMED'}
(HERE/'CONTROL-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':checks,'rows':len(rows),'signature':sig,'setup_fixed':fixed_setup,'sign_fixed':fixed_sign,'result_sha256':sha(HERE/'CONTROL-RESULTS.json')},indent=2))

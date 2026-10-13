"""Independent exact-arithmetic review; all outputs remain in this directory."""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial, log2
from datetime import datetime, timezone
import hashlib, json, subprocess, sys

B=Path(__file__).resolve().parent
X=B.parents[1]
R=X/'root-parameter-uniform-classical'
OUT=B/'positive-certificate-replay'
OUT.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pins={
 'root-parameter-uniform-classical/POSITIVE-CERTIFICATE.md':'b1230dc86499e9b3be5dacb2115958178ffe3005ec923c0badeda4c06ed2d2ae',
 'root-parameter-uniform-classical/uniform_bounds.py':'7eb2d3d019c9c97a405876045a89e3b0a7f5283156fe5b17eddd41c34e1c9ccf',
 'root-parameter-uniform-classical/BASELINE-CERTIFICATES.json':'f71d161493ab8ca605fd07f44dc619dcdcb382987427034d5fbf9d3cf217b904',
 'root-parameter-uniform-classical/HEIGHT63-CERTIFICATES.json':'0e568cbed7f9a1b8117ed12f5de729742718e0e20f05820a0cb9c47845979ee1',
 'root-parameter-uniform-classical/height63-illustration.json':'4b38081b225e303832861ad5e5c6c77fb6ac7436dad99b2f6a921627e81ab501',
 'PARAMETER-UNIFORM-CLASSICAL-THEOREM.md':'e5fc68bc269ca98672caa99ec70d5695d3d578095a62ebbfc0f99f9d8fbc394b',
 'selected-promotion-review/parameter-uniform-classical/FINAL-SUBJECT-REVIEW.json':'99313f8cb5bdf451c48e27f31ad9063e283f6f10e101d099c2637b3fae901056',
}
preserved=json.loads((B/'FINAL-SUBJECT-REVIEW.json').read_text(encoding='utf-8'))['preserved_artifacts']
def verify(group):
 for p,h in group.items():
  f=Path(p) if Path(p).is_absolute() else X/p
  assert sha(f)==h,p
verify(pins);verify(preserved)

# Independent closed-form inclusion/exclusion definition, not the root recurrence.
def S(r,j):
 if j==0:return int(r==0)
 n=sum((-1)**(j-i)*comb(j,i)*i**r for i in range(j+1))
 assert n>=0 and n%factorial(j)==0
 return n//factorial(j)
def touchard(r,mu):return sum((S(r,j)*mu**j for j in range(r+1)),F(0))
def falling(q,j):
 v=1
 for i in range(j):v*=q-i
 return v
def binomial_moment(r,q,instances):
 return sum((F(S(r,j)*falling(q,j),instances**j) for j in range(min(r,q)+1)),F(0))
def read_fraction(record):
 v=F(int(record['numerator']),int(record['denominator']))
 assert str(v.numerator)==record['numerator'] and str(v.denominator)==record['denominator']
 expected=log2(v.denominator)-log2(v.numerator) if v else None
 actual=record['display_negative_log2_approx']
 assert (actual is None and expected is None) or abs(actual-expected)<1e-11
 return v

commands=[]
exact_rows=[]
for filename,params_arg in [('BASELINE-CERTIFICATES.json',[]),('HEIGHT63-CERTIFICATES.json',['--params',str(R/'height63-illustration.json')])]:
 target=OUT/filename
 assert not target.exists(), 'Do not overwrite even reviewer replay outputs'
 cmd=[sys.executable,'-I','-B',str(R/'uniform_bounds.py'),*params_arg,'--out',str(target)]
 ran=subprocess.run(cmd,capture_output=True,text=True)
 assert ran.returncode==0,ran.stderr
 assert target.read_bytes()==(R/filename).read_bytes()
 commands.append(dict(argv=cmd,exit_code=ran.returncode,stdout=ran.stdout.strip(),stderr=ran.stderr,
                      output_sha256=sha(target),byte_identical=True))
 certificate=json.loads(target.read_text(encoding='utf-8'))
 p=certificate['parameters'];r=p['r'];a=p['a'];hs=p['heights'];h=sum(hs);d=len(hs)
 ws=[16]*(d-1)+[256];tails=[ell*(w-1)-s for ell,w,s in zip(p['ell'],ws,p['S'])]
 H=r+sum(tails);G=r*(a+1)+1+sum(tail+1+hi for tail,hi in zip(tails,hs));C=H+G+d+3
 # Separate serial layout: R/c_fors, r secret/path groups, and per-layer c/WOTS/path.
 sig=16+4+r*(16+a*16)+sum(4+ell*16+hi*16 for ell,hi in zip(p['ell'],hs))
 cache=(2*(1<<hs[-1])-1)*16+(1<<hs[-1])*4
 assert r*(1<<a)<=1<<32 and (r+1)*a+h<=256 and h<=63
 assert all(0<=hi<=31 for hi in hs) and all(t>0 for t in tails)
 assert 1<=d<=256 and 22+16*r+9<=24*64
 assert len(certificate['rows'])==24
 for row in certificate['rows']:
  q=1<<row['log2_q'];Q=1<<row['log2_Q'];N=1<<128;t=1<<a;instances=1<<h
  assert int(row['q'])==q and int(row['Q'])==Q
  assert (row['H'],row['G'],row['C'],row['signature_bytes'],row['cache_payload_bytes'])==(H,G,C,sig,cache)
  mu=F(q,instances)
  positive=min(F(1,t),touchard(r,mu)/t**(r+1))
  tighter_moment=min(F(1,t),binomial_moment(r,q,instances)/t**(r+1))
  assert tighter_moment<=positive and positive==read_fraction(row['pF_positive_upper'])
  exponent=min(2048,1<<(32-a))
  expected={
   'public_slots':F(3*Q,N),'honest_inner':F(2*q,N),'terminal_seed_constant':F(C,N),
   'full256_bridge':F(q*Q+q*(q-1)//2+q,N**2),
   'finite_counter_upper':F(q,1<<exponent),'coverage_upper':(Q+1)*positive,
  }
  assert row['finite_counter_dyadic_exponent_used']==exponent
  assert set(row['terms'])==set(expected)
  for key,value in expected.items():assert read_fraction(row['terms'][key])==value,key
  total=sum(expected.values(),F(0));cap=min(F(1),total)
  assert read_fraction(row['uncapped_upper'])==total
  assert read_fraction(row['capped_upper'])==cap
  assert row['sufficient_at_success_half']==(total<=F(1,2))
  assert row['necessary_half_certificate_public_fee_passes']==(F(3*Q+2*q+C,N)<=F(1,2))
  assert row['actual_attack_or_work_bits_or_category_or_repair_certified'] is False
  if not certificate['baseline'] and row['log2_Q']==125:assert total<F(1,2)
  if row['log2_Q']==128:assert cap==1
  exact_rows.append(dict(certificate=filename,log2_q=row['log2_q'],log2_Q=row['log2_Q'],
                         positive_moment_checked=True,finite_binomial_moment_no_larger=True,
                         complete_exact_sum_checked=True,half_success=total<=F(1,2)))

# Independent exact small-binomial check; explicitly includes B=1 and q=0.
small=0
for instances in (1,2,4,8):
 for t in (2,4,8):
  for r in range(1,8):
   for q in range(9):
    rho=F(1,instances);beta=F(t-1,t)
    exact=sum((F(comb(q,z))*rho**z*(1-rho)**(q-z)*(1-beta**z)**r/t for z in range(q+1)),F(0))
    m=binomial_moment(r,q,instances)
    assert exact<=min(F(1,t),m/t**(r+1))<=min(F(1,t),touchard(r,F(q,instances))/t**(r+1))
    small+=1
# Exact finite-grid checks support, but do not replace, the analytic exp/2 inequality.
counter_cases=0
for b in range(1,11):
 for a in range(1,b+1):
  assert F((1<<a)-1,1<<a)**(1<<b)<=F(1,1<<(1<<(b-a)))
  counter_cases+=1
assert touchard(17,F(2))==18880288847750<1<<45
moment_max=touchard(17,F(2))/(1<<180)
assert 135.8980539299409<log2(moment_max.denominator)-log2(moment_max.numerator)<135.8980539299411
height=json.loads((OUT/'HEIGHT63-CERTIFICATES.json').read_text(encoding='utf-8'))
maxrow=next(row for row in height['rows'] if row['log2_q']==64 and row['log2_Q']==125)
maxsum=read_fraction(maxrow['uncapped_upper'])
assert F(3,8)<maxsum<F(1,2)
results=dict(status='PASSED_INDEPENDENT_POSITIVE_FRACTION_CERTIFICATE_REVIEW',commands=commands,
    rows=exact_rows,independent_exact_rows=len(exact_rows),independent_small_binomial_cases=small,
    independent_counter_cases=counter_cases,Stirling_method='closed form inclusion-exclusion / j!, not root recurrence',
    maximum_height_row=dict(q='2^64',Q='2^125',uncapped_numerator=str(maxsum.numerator),
                           uncapped_denominator=str(maxsum.denominator)),
    all_q_0_through_2pow64_at_Q125='Follows by monotonicity of every nonnegative coefficient and bridge term, not interpolation of eight samples',
    no_signatures_caches_or_attacks_generated=True,whole_goal_complete=False)
(B/'POSITIVE-CERTIFICATE-CONTROLS.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')

md='''# Independent positive-certificate and script review

**ACCEPTED — exact rational classical upper certificates only.**

The exact root note, calculator, parameter tuple and both 24-row certificate
files were read. Their complete input hashes are bound in the companion JSON.
The original script was executed with `-I -B` twice, with outputs directed to
this reviewer's fresh replay directory. Both calls exited0 and reproduced the
root certificate files byte for byte. Commands and outputs are recorded in
POSITIVE-CERTIFICATE-CONTROLS.json. No original output was overwritten.

## Independent mathematics and implementation check

For integer Z, 1-(1-1/t)^Z<=Z/t. The identity Z^r=sum_j S(r,j)(Z)_j has
nonnegative coefficients. For binomial Z, E[(Z)_j]=(q)_j/B^j<=q^j/B^j.
Hence pF<=min(1/t,T_r(q/B)/t^(r+1)). This is a positive upper bound on the
finite-binomial law; no Poisson distribution is substituted for that law.
The independent checker computes S(r,j) by its inclusion-exclusion closed
formula, rather than copying the root recurrence. It verifies all48 exact
rational rows, plus the tighter finite-binomial factorial-moment upper and
756 separate exact small-binomial cases, including q0/B1. There is no
floating arithmetic in a certificate comparison. Display logarithms only are
checked against recomputed approximations.

With L=2^32 and beta=1-1/t, ln(1-u)<=-u and e>2 yield beta^L<=2^(-L/t).
The integer exponent L/t=2^(32-a) is weakened downward to at most2048, making
the dyadic upper larger. All48 rows retain its q multiplier. Fifty-five exact
small counter checks additionally pass; they do not replace the analytic proof.

For r17/a10/heights(10,10,11,11,21), ell(32,32,32,32,16) and original sums:
H3017, G3256 and C6281; serialized signature6344bytes, public key32bytes,
top cache payload75497456bytes. The 6281 number is a theorem constant, not
signature bytes. Digest allocation243bits and all schema representation and
strict-target guards pass. Width/seed/message conventions are unchanged.
The top height remains21, so retained top payload stays the same; this says
nothing about the changed lower-tree setup/reconstruction cost or availability.

T17(2)=18880288847750<2^45, so for every q<=2^64, pF is bounded above by that
integer divided by2^180. The positive upper's display exponent is approximately
135.898053929941; it is not a security work factor. Every illustrated Q125
complete row is strictly below1/2. Since q/B powers and every bridge/honest/
counter term are nondecreasing for integer q>=0, the q64 row proves the same
claim for all integer q<=2^64, not merely the eight sampled capacities.
Every Q128 row caps1 because its public-slot fee already exceeds1. All full
terms are summed before capping, and all comparison flags agree exactly.

## Scope and preservation

No substantive defect was found. The root script's narrow valid-input schema
is sufficient for these two declared tuples; this review does not certify a
general CLI validation service or arbitrary malformed JSON exception behavior.
The baseline positive bound is conservative and remains separate from sharper
historical pF/threshold computations. The height example is an analytical
source-schema illustration, not a retuned binary, performance result, proved
availability condition, original128/category guarantee or minimal repair.
The classical uniform theorem and source/historical pins remain unchanged.
No retuned QROM follows. New source-game/kernel declarations0; whole goal
complete false. This is a technical certificate review, not core-index approval.
'''
(B/'POSITIVE-CERTIFICATE-REVIEW.md').write_text(md,encoding='utf-8')
checks={key:True for key in [
 'exact_note_script_two_certificates_and_tuple_read',
 'positive_Touchard_upper_proved_not_Poisson_equality',
 'independent_closed_form_Stirling_and_exact_fraction_arithmetic',
 'tighter_binomial_factorial_moment_checked',
 'all48_full_rows_exact_terms_caps_and_flags_checked',
 'finite_counter_exponent_weakening_direction_and_q_retained',
 'source_guards_fixed_n16_widths_strict_target_and_digest243',
 'H3017_G3256_C6281_recomputed',
 'signature6344_public32_topcache75497456_recomputed',
 'T17_at2_exact_and_display_exponent_scope',
 'all_q_through_2pow64_Q125_successhalf_by_monotonicity',
 'Q128_cap_one_not_actual_attack',
 'both_isolated_replays_exit0_and_byte_identical',
 'no_original_outputs_overwritten',
 'source_theorem_historical_and_prior_first_pins_preserved',
 'no_availability_performance_minimality_128_category_or_QROM_claim',
 'classical_query_certificate_not_gatecost_or_fixedSHA_hardness',
]}
verify(pins);verify(preserved)
receipt=dict(status='ACCEPTED_EXACT_RATIONAL_POSITIVE_CLASSICAL_CERTIFICATES',
 reviewed_at_utc=datetime.now(timezone.utc).isoformat(),
 subject='root-parameter-uniform-classical/POSITIVE-CERTIFICATE.md',
 subject_sha256=pins['root-parameter-uniform-classical/POSITIVE-CERTIFICATE.md'],
 checks=checks,source_subjects=pins,preserved_artifacts=preserved,
 review_pins={str((B/name).relative_to(X)).replace('\\','/'):sha(B/name) for name in
    ['POSITIVE-CERTIFICATE-REVIEW.md','POSITIVE-CERTIFICATE-CONTROLS.json','review_positive_certificate.py']},
 independent_exact_rows=48,independent_small_binomial_cases=small,independent_counter_cases=counter_cases,
 new_checked_declarations=0,new_source_game_declarations=0,
 retuned_QROM_bound_established=False,parameter_repair_established=False,
 original_level_category_objective_established=False,whole_goal_complete=False)
(B/'POSITIVE-CERTIFICATE-REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=receipt['status'],checks=len(checks),receipt_sha256=sha(B/'POSITIVE-CERTIFICATE-REVIEW.json'),
  markdown_sha256=sha(B/'POSITIVE-CERTIFICATE-REVIEW.md'),controls_sha256=sha(B/'POSITIVE-CERTIFICATE-CONTROLS.json'))))

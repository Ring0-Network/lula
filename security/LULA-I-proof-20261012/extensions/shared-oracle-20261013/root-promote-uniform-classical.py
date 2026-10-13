"""Promote only the exact reviewed guarded classical successor and its numerics."""
from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((X/n).read_text(encoding='utf8'))
prior=read('CLASSICAL-JOINT-PROMOTION.json')
subject='PARAMETER-UNIFORM-CLASSICAL-THEOREM.md'
assert sha(X/subject)=='e5fc68bc269ca98672caa99ec70d5695d3d578095a62ebbfc0f99f9d8fbc394b'
receipts=['selected-promotion-review/parameter-uniform-classical/FINAL-SUBJECT-REVIEW.json',
 'pre-start-second/uniform-classical-numerics-20261014/FINAL-SUBJECT-REVIEW.json']
for n in receipts:
 r=read(n);assert r['subject_sha256']==sha(X/subject)
 if 'checks' in r:
  assert all(r['checks'].values())
 else:
  assert r['status']=='ACCEPT_GUARDED_UNIFORM_CLASSICAL_SOURCE_THEOREM_AND_SCOPED_EXACT_CERTIFICATES'
  assert all(r[k] is True for k in ('own_first_and144_rows_saved_before_final_root_read',
   'root_CLI_reruns_identical','uniform_theta_denominator_full128','zeroheight_and_d1_supported_with_guards',
   'Q_adversarial_only_honest_work_separate','private_full_raw_RO_model_preserved',
   'parameter_fixed_ex_ante_and_partiality_preserved','all8_height63_Q125_half_success_certificates',
   'allQ128_rows_cap1','universal_C_lower11_and_tiny_gate_inability','ineffective_upper_gate_not_attack'))
  assert (r['baseline_rows_recovered'],r['baseline_adjacent_rational_crossings_recovered'],r['root_exact_fraction_rows_crosschecked'])==(24,8,48)
 assert not r['whole_goal_complete']
positive=read('selected-promotion-review/parameter-uniform-classical/POSITIVE-CERTIFICATE-REVIEW.json')
assert all(positive['checks'].values())
cross=read('root-parameter-uniform-classical/ROOT-CROSSCHECK.json')
assert cross['independent_rows_checked']==144 and cross['root_exact_certificate_rows_checked']==48
for n,h in prior['documents'].items():assert sha(X/n)==h,n
backup=X/'root-docs-before-uniform-classical';assert not backup.exists();backup.mkdir()
pins=dict(prior['accepted_evidence_absolute_pins'])
for n,h in prior['documents'].items():
 shutil.copyfile(X/n,backup/n);pins[str(backup/n)]=h
addition='''

## Reviewed guarded parameter-uniform classical successor

**PROVED — manual source-schema extension.** PARAMETER-UNIFORM-CLASSICAL-THEOREM.md extends the shared-full-RO joint construction uniformly under explicit n16, lw4/8, strict target-sum, complete omitted-zero digest, address/buffer and finite-counter guards. Parameters are fixed ex ante. Two independent final subject reviews bind e5fc68bc. Honest atomic canonical cache restoration retains zero-loss transfer. Corrupt/noncanonical caches are excluded, not assumed harmless. No retuned executable or whole-source/kernel theorem is claimed.

**PROVED — exact variable fees.** Put t_i=ell_i(w_i-1)-S_i, H_p=r+sum t_i, G_p=r(a+1)+1+sum(t_i+1+h_i), and C_p=H_p+G_p+d+3. The complete upper is

`min(1,(3Q+2q+C_p)/N+(qQ+binom(q,2)+q)/N^2+q*(1-2^-a)^(2^32)+(Q+1)*p_F(q;p))`, N=2^128.

Full256 input/output aliases, one safe continued ghost, all final verifier cases, finite partiality and deterministic Q+1 candidate padding remain explicit. Baseline gives C6242 exactly. The type7 acceptance denominator remains2^128 even with shortened ell.

**COMPUTED — reproducible independent data.** The new independent evaluator covers144 rows (six guarded shapes, eight required q, three Q budgets), recovers all24 accepted baseline rows and eight adjacent half-success crossings. Root crosschecks all144 and separately48 exact rational positive-upper certificates. The latter uses a proved Touchard upper and an explicit dyadic finite-exhaustion upper, not an exact-Poisson substitution or zero exhaustion.

**COMPUTED — useful classical illustration, not an original-target repair.** For r17,a10,heights(10,10,11,11,21), original chain parameters and top-only cache: C6281, signature6344B, public key32B, payload75497456B. Exact Touchard17(2)=18880288847750 proves p_F<2^-135 for all q<=2^64. All eight Q2^125 rows have complete classical upper<1/2; monotonicity extends this certificate to intermediate q. Every Q2^128 row still caps1. The variant is analytical and unimplemented; it has no retuned QROM, availability, original128/category or minimality certificate.

**OPEN — original adequacy and next obligation.** A sufficient uniform envelope cannot certify eta<1 unless3Q+2q+C_p<=eta*N. Its failure at the full requested query budget is an upper-certificate limitation, not an attack or parameter impossibility. The remaining smallest scientific work is a sufficiently tight complete bound in a justified success/resource normalization; a retuned quantum source proof is needed before reusing baseline QROM formulas. Successful smallest repair, original level/category and certified capacity remain "not established". All historical scalars,47 supporting declarations,165 frozen files, source and current manuscript are preserved. The full goal remains active.
'''
for n in prior['documents']:
 p=X/n;p.write_text(p.read_text(encoding='utf8').rstrip()+addition+'\n',encoding='utf8')
for folder in ('root-parameter-uniform-classical','selected-promotion-review/parameter-uniform-classical',
 'pre-start-second/uniform-classical-numerics-20261014'):
 for p in (X/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:pins[str(p)]=sha(p)
for n in [subject,'root-promote-uniform-classical.py']:pins[str(X/n)]=sha(X/n)
assert all(sha(Path(p))==h for p,h in pins.items())
out={'status':'REVIEWED_GUARDED_PARAMETER_UNIFORM_CLASSICAL_SUCCESSOR_PROMOTED',
 'predecessor_promotion_sha256':sha(X/'CLASSICAL-JOINT-PROMOTION.json'),
 'predecessor_backup':'root-docs-before-uniform-classical','predecessor_documents':prior['documents'],
 'documents':{n:sha(X/n) for n in prior['documents']},'subject':subject,'subject_sha256':sha(X/subject),
 'receipt_pins':{n:sha(X/n) for n in receipts},
 'positive_certificate_review_sha256':sha(X/'selected-promotion-review/parameter-uniform-classical/POSITIVE-CERTIFICATE-REVIEW.json'),
 'root_crosscheck_sha256':sha(X/'root-parameter-uniform-classical/ROOT-CROSSCHECK.json'),
 'accepted_evidence_absolute_pins':pins,'independent_rows':144,'root_rational_rows':48,
 'old_baseline_rows_preserved':24,'old_baseline_crossings_preserved':8,
 'retuned_QROM_established':False,'original_level_category_capacity_repair':'not established',
 'cumulative_supporting_checked_declarations':47,'new_whole_source_game_checked_declarations':0,
 'new_source_or_manuscript_edits':0,'whole_goal_complete':False}
(X/'UNIFORM-CLASSICAL-PROMOTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'pins':len(pins),'independent_rows':144,'root_rational_rows':48,'whole_goal_complete':False}))

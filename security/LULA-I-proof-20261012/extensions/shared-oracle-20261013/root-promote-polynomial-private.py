from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((X/p).read_text(encoding='utf8'))
prior=read('POLYNOMIAL-UD-PROMOTION.json')
idx=read('pre-start-second/polynomial-ud-current-index/CURRENT-INDEX-REVIEW.json')
assert all(idx['checks'].values()) and idx['subject_sha256']==sha(X/'POLYNOMIAL-UD-PROMOTION.json')
receipts=['pre-start-second/private-K-polynomial/FINAL-SUBJECT-REVIEW.json',
 'outside-field-check/private-p-polynomial/FINAL-SUBJECT-REVIEW.json',
 'pre-start-second/polynomial-private-composition/FINAL-SUBJECT-REVIEW.json',
 'outside-field-check/polynomial-query-thresholds/FINAL-CERTIFICATE.json']
records=[read(n) for n in receipts]
subjects=['SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md','SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md',
          'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md']
for d,n in zip(records[:3],subjects):
    assert all(d['checks'].values()) and d['subject_sha256']==sha(X/n),n
    assert not d['whole_goal_complete']
assert records[3]['subject_sha256']==sha(X/subjects[2])
assert not records[3]['whole_goal_complete']
assert records[2]['root_dataset_sha256']==sha(X/'root-polynomial-private-composition/RESULTS.json')
cross=read('root-polynomial-private-composition/THRESHOLD-CROSSCHECK.json')
assert cross['status']=='PASS_32_NEW_COMPLETE_ENVELOPE_ADJACENT_PAIRS_64_ENDPOINTS'
assert cross['certificate_sha256']==sha(X/'outside-field-check/polynomial-query-thresholds/NEW-CERTIFICATES.json')
pins=dict(prior['accepted_evidence_absolute_pins'])
def add(p,h=None):
    p=Path(p)
    if not p.is_absolute():p=X/p
    actual=sha(p)
    if h is not None:assert actual==h,str(p)
    pins[str(p)]=actual
for folder in ('root-polynomial-private-composition','pre-start-second/private-K-polynomial',
 'pre-start-second/polynomial-private-composition','outside-field-check/private-p-polynomial',
 'outside-field-check/polynomial-query-thresholds','pre-start-second/polynomial-ud-current-index'):
    for p in (X/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:add(p)
for n in subjects+receipts+['root-ud-polynomial/PRIVATE-K-FIRST.md',
 'root-ud-polynomial/PRIVATE-P-CANDIDATE.md','root-ud-polynomial/private_k_controls.py',
 'root-ud-polynomial/PRIVATE-K-CONTROLS.json']:add(n)
for n,h in prior['documents'].items():assert sha(X/n)==h,n
backup=X/'root-docs-before-polynomial-private';assert not backup.exists();backup.mkdir()
for n,h in prior['documents'].items():shutil.copyfile(X/n,backup/n);add(backup/n,h)
data=read('root-polynomial-private-composition/RESULTS.json')
cert=read('outside-field-check/polynomial-query-thresholds/FINAL-CERTIFICATE.json')
new32={r['log2_q']:r for r in data['rows'] if r['log2_Q']==32}
bestq={r['log2_q']:r for r in cert['best_rows']}
table='| q | COMPUTED new Q=2^32 probability exponent | COMPUTED Q=2^64 upper bound | COMPUTED sufficient Q_pass at success1/2 |\n|---:|---:|---:|---:|\n'
for e in (24,30,38,40,41,44,50,64):
    table+=f"| 2^{e} | {new32[e]['exponents']['poly_total']:.6f} | 1 (cap) | {bestq[e]['Q_pass']} |\n"
common='''

## Complete finite-QROM polynomial-private successor

**PROVED — exact source decision composition.** SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md gives the REAL/idealF source Win-bit gap v=min(1,4Q^2/(N-4Q^2)) when4Q^2<N, else1. SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md separately gives idealF/realP winning probability <=ordinaryHJ winning probability+aP, with aP=min(1,v+min(1,(2Q+sqrt(min(N,2q+2)))^2/N)). P's polynomial decision and key-dependent stopped alias projector remain distinct arguments. Complete source and private services, pre-key withholding, universal interpolation budgets, literal aliases/full lower limbs and absorbing completion are preserved. Private caps areQ_A, notQ_A+1; honest P nominees include final verification. The same source Win bit and one-sided P direction suffice.

**PROVED — full formula and cache transfer.** QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md composes those hops with the unchanged ordinary HJ public components c,h,g,d7. WithN=2^128,Q=Q_A,

`epsilon_poly=min(1,1/N+v+aP+min(1,c+h+g+d7))`.

S=0 is paid once outside fixed-nonzero inequalities. The valid minimum retains the conservative, event-specific and new polynomial-private theorems. Exact honest atomic cache restoration transfers the new source event with zero probability/query loss. Seed-bearing frames, corrupt caches, timing and partial/coherent signing remain excluded.

**COMPUTED — independently reviewed whole rows and thresholds.** root-polynomial-private-composition/bounds.py and pre-start-second/polynomial-private-composition/independent_bounds.py separately evaluate all16 rows at eightq values andQ2^32/2^64;336 probability comparisons pass. Atq2^40,Q2^32 the complete probability-bound exponent improves57.6833598693 to58.0931788798. Six rows improve the retained minimum. These are probability exponents, not security work factors. Two independent exact outward threshold evaluators certify32 adjacent component/best pairs, and root checks64 endpoints. Atq2^40 the sufficient best Q_pass is1681654180826527564 withQ_fail the next integer, for success target1/2. EveryQ2^64 row remains capped1.

**OPEN — original adequate certification and repair.** The original level/category/capacity and successful smallest parameter repair remain "not established". Query certificates are sufficient model envelopes, not attacks or AES/circuit equivalence. Fixed-SHA hardness and whole compiler/kernel mechanization are separate from the requested random-oracle proof, not invented completion prerequisites. Old source/scalar artifacts,165 frozen files and publication files are unchanged;47 supporting checked declarations remain, newly checked whole-source/game declarations0. The simultaneous classical3Q candidate remains separate and unpromoted.
'''
for n in prior['documents']:
    p=X/n;addition=common
    if n=='TERM-TABLE.md':addition+='\n**COMPUTED — new whole-bound display and independently certified query endpoints.** Exponents rounded to six decimals; exact endpoints use rational certificates.\n\n'+table
    p.write_text(p.read_text(encoding='utf8').rstrip()+addition+'\n',encoding='utf8')
assert all(sha(Path(n))==h for n,h in pins.items())
out={'status':'REVIEWED_COMPLETE_FINITE_QROM_POLYNOMIAL_PRIVATE_SOURCE_SUCCESSOR_PROMOTED',
 'documents':{n:sha(X/n) for n in prior['documents']},'predecessor_documents':prior['documents'],
 'predecessor_backup':'root-docs-before-polynomial-private',
 'artifacts':{n:sha(X/n) for n in subjects+['root-polynomial-private-composition/bounds.py',
   'root-polynomial-private-composition/RESULTS.json','root-polynomial-private-composition/THRESHOLD-CROSSCHECK.json']},
 'receipt_pins':{n:sha(X/n) for n in receipts},'accepted_evidence_absolute_pins':pins,
 'independent_complete_numeric_rows':16,'probability_comparisons':336,'new_threshold_pairs':32,
 'new_best_q40_Q32_probability_exponent':58.09317887983897,
 'cumulative_supporting_checked_declarations':47,'new_source_game_checked_declarations':0,
 'source_scalar_manuscript_changes':0,'new_source_successor_kept_separate_from_old_formulas':True,
 'classical_joint_candidate_promoted':False,'original_level_category_statement':'not established',
 'whole_goal_complete':False}
(X/'POLYNOMIAL-PRIVATE-PROMOTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'pins':len(pins),'rows':16,'new_threshold_pairs':32,'whole_goal_complete':False}))

from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((X/n).read_text(encoding='utf8'))
prior=read('POLYNOMIAL-PRIVATE-PROMOTION.json')
index=read('pre-start-second/polynomial-private-current-index/CURRENT-INDEX-REVIEW.json')
assert all(index['checks'].values()) and index['subject_sha256']==sha(X/'POLYNOMIAL-PRIVATE-PROMOTION.json')
receipt_names=['selected-promotion-review/joint-classical-review/FINAL-SUBJECT-REVIEW.json',
 'pre-start-second/classical-joint-root-crosscheck/FINAL-SUBJECT-REVIEW.json']
subject='CLASSICAL-JOINT-RO-THEOREM.md'
for name in receipt_names:
 r=read(name);assert all(r['checks'].values()) and r['subject_sha256']==sha(X/subject)
 assert not r['whole_goal_complete'] and r['new_source_game_declarations']==0
root=read('root-classical-joint/ROOT-JOINT-CHECK.json')
assert root['status']=='PASS24_CLASSICAL_JOINT_ROWS_AND8_EXACT_ADJACENT_CROSSINGS'
assert root['subject_sha256']==sha(X/subject) and root['QH128_all_cap_one']
assert len(root['rows'])==24 and len(root['crossings'])==8
own=read('pre-start-second/classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json')
pins=dict(prior['accepted_evidence_absolute_pins'])
def add(p,h=None):
 p=Path(p)
 if not p.is_absolute():p=X/p
 actual=sha(p)
 if h is not None:assert actual==h,str(p)
 pins[str(p)]=actual
for folder in ('selected-promotion-review/joint-classical-review',
 'pre-start-second/classical-joint-root-crosscheck',
 'pre-start-second/interior-ud/quantitative-boundary/joint-classical','root-classical-joint'):
 for p in (X/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:add(p)
for n in receipt_names+[subject,'pre-start-second/polynomial-private-current-index/CURRENT-INDEX-REVIEW.json']:add(n)
for n,h in prior['documents'].items():assert sha(X/n)==h,n
backup=X/'root-docs-before-classical-joint';assert not backup.exists();backup.mkdir()
for n,h in prior['documents'].items():shutil.copyfile(X/n,backup/n);add(backup/n,h)
rows64={r['q_exponent']:r for r in own['rows'] if r['QH_exponent']==64}
cross={r.get('q_exponent',r.get('log2_q')):r for r in own['half_success_crossings']}
table='| q | COMPUTED probability exponent atQ_H=2^64 | COMPUTED bound atQ_H=2^128 | COMPUTED sufficient Q_pass at success1/2 |\n|---:|---:|---:|---:|\n'
for k in (24,30,38,40,41,44,50,64):
 table+=f"| 2^{k} | {float(rows64[k]['own_probability_exponent_not_security_bits']):.6f} | 1 (cap) | {cross[k]['Q_pass']} |\n"
addition='''

## Reviewed complete classical joint-ledger successor

**PROVED — simultaneous source construction.** CLASSICAL-JOINT-RO-THEOREM.md and two source-first final reviews establish a single safe-surface graph/row/private/coverage ghost. Independent fullF/J maps, genuine designated graph cells, lower limbs and residual functions retain the actual REAL marginal; literal overlaps are handled by the common first bad. Only observed replies/honest computations agree before that bad, not complete functions at unqueried hidden points. Endpoint/leaf/public images and canonical rows are safe; hidden starts/interior coordinates, fullF and surplus row answers are not granted. Atomic unsigned-J scope and permanent forward disclosure are explicit. No old incompatible advice worlds are merged.

**PROVED — full bound and unchanged interface.** Predictable raw slots carry rare weights1,2 or3 divided byN=2^128; inner privateP/nonce/endpoint risks overlap rather than create disjoint budgets. Expected role counts share one unflagged ghost and sum pathwise<=Q_H. Honest outer private aliases are contained in the already charged inner endpoint event. The fixed-nonzero constant is6241; seedzero is paid once to obtain

`E_joint=min(1,(3Q_H+2q+6242)/N+(qQ_H+binom(q,2)+q)/N^2+q*(511/512)^(2^32)+(Q_H+1)*pF(q))`.

Candidate coverage uses a deterministic bound, never expected eligible-query counts. The exact uncapped improvement from the old theorem is(3Q_H+q+1)/N. Honest atomic cache restoration transfers with zero probability/query loss. Corrupted/private/coherent/timing APIs remain outside this model.

**COMPUTED — new complete rows and exact thresholds.** Independent24 rows cover all eightq values andQ_H2^32/2^64/REQUIRED2^128. Root exact Fraction checks confirm every interval, delta and all eight adjacent half-success boundaries. Atq2^40,Q_H2^64 the probability exponent is62.39484059815322, not a security work factor. Its sufficient half-successQpass is55925302073878813864583541683133229382. EveryQ_H2^128 row caps1. Positive exact-binomial outward brackets are inherited and independently reevaluated; finite-counter exhaustion is enclosed, not setzero.

**OPEN — original certification and repair.** This is an improved complete classical source envelope, paired with the accepted polynomial-private QROM successor. It does not supply adequate128/category1 strength, a certified maximum signing capacity or a successful smallest parameter repair. All old theorem/calculator/48 scalar cells/32 threshold receipts are preserved. Source, manuscript and165 frozen files remain unchanged; supporting checked declarations47 and newly checked whole-source/game declarations0. The original printable adequacy statement remains "not established". Original criterion and analytic parameter-repair studies remain separately scoped pending their final reconciliation.
'''
for n in prior['documents']:
 p=X/n;text=p.read_text(encoding='utf8').rstrip()+addition
 if n=='TERM-TABLE.md':text+='\n**COMPUTED — classical successor display.** Rounded exponents concern probability envelopes. Exact crossing certificates use rational intervals.\n\n'+table
 p.write_text(text+'\n',encoding='utf8')
assert all(sha(Path(n))==h for n,h in pins.items())
out={'status':'REVIEWED_COMPLETE_CLASSICAL_JOINT_SOURCE_SUCCESSOR_PROMOTED',
 'documents':{n:sha(X/n) for n in prior['documents']},'predecessor_documents':prior['documents'],
 'predecessor_backup':'root-docs-before-classical-joint','artifacts':{subject:sha(X/subject),
 'root-classical-joint/check.py':sha(X/'root-classical-joint/check.py'),
 'root-classical-joint/ROOT-JOINT-CHECK.json':sha(X/'root-classical-joint/ROOT-JOINT-CHECK.json')},
 'receipt_pins':{n:sha(X/n) for n in receipt_names},'accepted_evidence_absolute_pins':pins,
 'classical_new_rows':24,'new_half_success_crossings':8,'QH128_all_cap_one':True,
 'cumulative_supporting_checked_declarations':47,'new_source_game_checked_declarations':0,
 'source_scalar_manuscript_changes':0,'new_theorem_not_old_formula_overwrite':True,
 'classical_joint_candidate_promoted':True,'original_level_category_statement':'not established',
 'whole_goal_complete':False}
(X/'CLASSICAL-JOINT-PROMOTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'pins':len(pins),'rows':24,'crossings':8,'whole_goal_complete':False}))

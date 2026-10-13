"""Fresh classical promotion hash/doc/table/affine/preservation check; own writes only."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,difflib,re
E=Path(__file__).resolve().parent;X=E.parent.parent;S=X.parents[1];P=S.parents[1]/'publications/LULA-I'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
index=read(X/'CLASSICAL-JOINT-PROMOTION.json');prior=read(X/'POLYNOMIAL-PRIVATE-PROMOTION.json')
checks={}
checks['357_actual_absolute_evidence_pins_match']=len(index['accepted_evidence_absolute_pins'])==357 and all(sha(Path(k))==v for k,v in index['accepted_evidence_absolute_pins'].items())
checks['321_prior_pins_retained_without_digest_changes']=len(prior['accepted_evidence_absolute_pins'])==321 and all(index['accepted_evidence_absolute_pins'].get(k)==v for k,v in prior['accepted_evidence_absolute_pins'].items())
for g in ('documents','artifacts','receipt_pins'):
 checks[g+'_all_actual_pins_match']=all(sha(X/n)==v for n,v in index[g].items())
checks['six_backups_exact321_prior_current_cut']=index['predecessor_documents']==prior['documents'] and all(sha(X/index['predecessor_backup']/n)==v for n,v in prior['documents'].items())
diff=[];add={};documents={}
for n in prior['documents']:
 old=(X/index['predecessor_backup']/n).read_text(encoding='utf-8');now=(X/n).read_text(encoding='utf-8')
 assert now.startswith(old.rstrip()),n
 add[n]=now[len(old.rstrip()):]
 documents[n]={'current_sha256':sha(X/n),'prior_sha256':sha(X/index['predecessor_backup']/n),'append_only_content_except_trailing_whitespace':True}
 diff.extend(difflib.unified_diff(old.splitlines(True),now.splitlines(True),fromfile=index['predecessor_backup']+'/'+n,tofile=n))
(E/'MANUAL-DIFF.txt').write_text(''.join(diff),encoding='utf-8')
common=add['PROOF.md']
checks['five_identical_append_only_additions_TERM_common_plus_table']=all(v==common for n,v in add.items() if n!='TERM-TABLE.md') and add['TERM-TABLE.md'].startswith(common.rstrip())
checks['simultaneous_source_and_rare_slot_overlap_scope_explicit']=all(z in common for z in ('single safe-surface','actual REAL marginal','not complete functions','fullF and surplus row answers are not granted','Atomic unsigned-J','risks overlap','6241','6242','deterministic bound','zero probability/query loss','REQUIRED2^128','not a security work factor','not established','47','whole-source/game declarations0'))

own=read(X/'pre-start-second/classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json')
review=read(X/'pre-start-second/classical-joint-root-crosscheck/FINAL-SUBJECT-REVIEW.json')
selected=read(X/'selected-promotion-review/joint-classical-review/FINAL-SUBJECT-REVIEW.json')
root=read(X/'root-classical-joint/ROOT-JOINT-CHECK.json')
checks['same_current_joint_subject_in_all_final_receipts']=own['subject_sha256']==review['subject_sha256']==selected['subject_sha256']==root['subject_sha256']==sha(X/'CLASSICAL-JOINT-RO-THEOREM.md')
checks['independent_final_receipts_all_checks_true']=all(review['checks'].values()) and all(selected['checks'].values()) and not review['whole_goal_complete'] and not selected['whole_goal_complete']
checks['root24_row_dataset_script_peer_and_input_hashes_match']=root['script_sha256']==sha(X/'root-classical-joint/check.py') and root['peer_review_sha256']==sha(X/'pre-start-second/classical-joint-root-crosscheck/FINAL-SUBJECT-REVIEW.json') and root['peer_dataset_sha256']==sha(X/'pre-start-second/classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json') and root['inherited_pf_input_sha256']==sha(X/'classical-composition-numeric/OWN-BOUNDS.json')

# New exact affine reconstruction from the actual retained dyadic source input.
N=1<<128;PF={}
def dyad(t):
 sign,mant,exp,b=t;assert sign==0 and mant.bit_length()==b
 return F(mant*(1<<exp)) if exp>=0 else F(mant,1<<(-exp))
for r in read(X/'classical-composition-numeric/OWN-BOUNDS.json')['rows']:
 n=r['log2_signing_query_cap'];v=r['FORS_per_raw_candidate']
 z=tuple(dyad(v[k]) for k in ('lower_dyadic_mpf_tuple','upper_dyadic_mpf_tuple'))
 if n in PF:assert PF[n]==z
 PF[n]=z
assert set(PF)=={24,30,38,40,41,44,50,64}
pair=lambda z:F(*map(int,z))
def interval(q,Q):
 p0,p1=PF[q.bit_length()-1]
 a0=F(3,N)+F(q,N*N)+p0;a1=F(3,N)+F(q,N*N)+p1
 b0=F(2*q+6242,N)+F(q*(q-1)//2+q,N*N)+p0
 b1=F(2*q+6242,N)+F(q*(q-1)//2+q,N*N)+p1+F(q,1<<4096)
 return a0*Q+b0,a1*Q+b1
actual={(r['q_exponent'],r['QH_exponent']) for r in own['rows']}
expected={(q,e) for q in PF for e in (32,64,128)}
assert actual==expected and len(own['rows'])==len(root['rows'])==24
row_checks=0
for r in own['rows']:
 qe,ae=r['q_exponent'],r['QH_exponent'];q=1<<qe;Q=1<<ae
 lo,hi=interval(q,Q)
 assert pair(r['uncapped_lower'])==lo and pair(r['uncapped_upper'])==hi
 assert pair(r['capped_lower'])==min(F(1),lo) and pair(r['capped_upper'])==min(F(1),hi)
 assert pair(r['old_minus_new_uncapped_exact'])==F(3*Q+q+1,N)
 rr=next(z for z in root['rows'] if (z['q_exponent'],z['QH_exponent'])==(qe,ae))
 assert abs(rr['probability_exponent_display']-float(r['own_probability_exponent_not_security_bits']))<1e-10
 assert rr['exact_cap_one']==(min(F(1),lo)==min(F(1),hi)==F(1))
 if ae==128:assert lo>=3 and min(F(1),lo)==min(F(1),hi)==F(1)
 row_checks+=1
checks['24_rows_numerators_enclosures_deltas_rootdisplays_and_Q128_caps']=row_checks==24
cross_checks=0
for r in own['half_success_crossings']:
 qe=r['q_exponent'];q=1<<qe;passed=int(r['Q_pass']);failed=int(r['Q_fail'])
 assert failed==passed+1
 lo,hi=interval(q,passed);l1,h1=interval(q,failed)
 assert hi<=F(1,2)<l1
 assert pair(r['pass_interval'][0])==lo and pair(r['pass_interval'][1])==hi
 assert pair(r['fail_interval'][0])==l1 and pair(r['fail_interval'][1])==h1
 assert pair(r['pass_margin'])==F(1,2)-hi and pair(r['fail_margin'])==l1-F(1,2)
 rr=next(z for z in root['crossings'] if z['q_exponent']==qe)
 assert rr['Q_pass']==r['Q_pass'] and rr['Q_fail']==r['Q_fail']
 cross_checks+=1
checks['8_exact_half_success_adjacent_pairs_and16_gates_recomputed']=cross_checks==8
table=re.findall(r'^\| 2\^(\d+) \| ([0-9.]+) \| 1 \(cap\) \| (\d+) \|$',add['TERM-TABLE.md'],re.M)
assert len(table)==8
for qlog,e,passed in table:
 qe=int(qlog);r=next(z for z in own['rows'] if (z['q_exponent'],z['QH_exponent'])==(qe,64))
 c=next(z for z in own['half_success_crossings'] if z['q_exponent']==qe)
 assert e==f"{float(r['own_probability_exponent_not_security_bits']):.6f}" and passed==c['Q_pass']
checks['TERM8_rounded_exponents_Q128caps_and_exact_Qpass_match']=True

# The previous quantum321 accepted cut remains an immutable inherited subject.
previous_current=read(X/'pre-start-second/polynomial-private-current-index/CURRENT-INDEX-REVIEW.json')
checks['latest_quantum321_prior_current_index_and_formulas_preserved']=previous_current['subject_sha256']==sha(X/'POLYNOMIAL-PRIVATE-PROMOTION.json') and all(previous_current['checks'].values())
for n,v in previous_current['subject_and_review_chain'].items():assert sha(X/n)==v,n
checks['quantum_private_full_rows64threshold_endpoint_artifacts_preserved']=True

baseline=read(X/'PRESERVATION-BASELINE.json')
frozen={str(f.relative_to(S)):sha(f) for f in S.rglob('*') if f.is_file() and not f.is_relative_to(S/'extensions')}
checks['165_frozen_packet_files_and_protected_crypto_sources_preserved']=frozen==baseline['frozen_packet'] and len(frozen)==165 and all(sha(Path(n))==v for n,v in baseline['crypto'].items())
paper=dict(baseline['current_paper'])
for n in ('AUTHORIZED-EDITORIAL-DELTA.json','AUTHORIZED-EDITORIAL-DELTA-20261013.json'):
 if (X/n).exists():
  rec=read(X/n);assert sha(Path(rec['patches_path']))==rec['patches_sha256']
  for k,c in rec['paper_changes'].items():assert paper[k]==c['before'];paper[k]=c['after']
checks['7_current_paper_files_match_authorized_editorial_cut']=all(sha(P/n)==v for n,v in paper.items())
helpers=read(X/'pre-start-second/polynomial-ud-current-index/COMPUTED-CHECKS.json')
for h in helpers['previous_helpers']:
 assert sha(X/h['source'])==h['source_sha256'] and sha(X/h['receipt'])==h['receipt_sha256']
 assert read(X/h['receipt'])['exit_code']==0
checks['47_existing_supporting_helper_sources_receipts_unchanged']=sum(h['supporting_declarations'] for h in helpers['previous_helpers'])==47
for n,r in helpers['historical_numeric_receipts'].items():assert sha(X/n)==r['sha256'] and len(read(X/n)['rows'])==16
checks['48_historical_scalar_cells_receipts_preserved']=True
old=read(X/'query-resource-independent/THRESHOLDS.json');assert len(old['rows'])==32
for n,v in old['input_pins'].items():assert sha(X/n)==v,n
checks['32_old_resource_crossing_input_pins_preserved']=True
checks['joint_promoted_but_47helpers0newgame0sourcechange_and_goalopen']=index['classical_joint_candidate_promoted'] and index['cumulative_supporting_checked_declarations']==47 and index['new_source_game_checked_declarations']==index['source_scalar_manuscript_changes']==0 and not index['whole_goal_complete'] and index['original_level_category_statement']=='not established'
out={'status':'PASS_FRESH357_PIN_CLASSICAL_JOINT_INDEX_TABLE24ROWS8CROSSINGS_AND_PRESERVATION' if all(checks.values()) else 'FAIL',
 'subject_sha256':sha(X/'CLASSICAL-JOINT-PROMOTION.json'),'prior_subject_sha256':sha(X/'POLYNOMIAL-PRIVATE-PROMOTION.json'),
 'current_pins':357,'prior_retained_pins':321,'new_pins':36,'checks':checks,'documents':documents,
 'script_sha256':sha(Path(__file__)),'manual_diff_sha256':sha(E/'MANUAL-DIFF.txt'),
 'joint_subject_sha256':sha(X/'CLASSICAL-JOINT-RO-THEOREM.md'),'own24_dataset_sha256':sha(X/'pre-start-second/classical-joint-root-crosscheck/OWN-JOINT-NUMERICS.json'),
 'root24_check_sha256':sha(X/'root-classical-joint/ROOT-JOINT-CHECK.json'),
 'rows_recomputed':row_checks,'crossings_recomputed':cross_checks,'TERM_table_rows':8,'publication_current_pins':paper,
 'new_source_game_declarations':0,'whole_goal_complete':False,'core_or_mutating_root_validator_writes':False}
(E/'COMPUTED-CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v],
                  'pins':357,'old_retained':321,'rows':row_checks,'crossings':cross_checks,'table':8,'subject_sha256':out['subject_sha256']}))

"""Fresh read-only 321-pin/current-doc/outward-endpoint promotion audit."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import hashlib,json,difflib,re
E=Path(__file__).resolve().parent;X=E.parent.parent;S=X.parents[1];P=S.parents[1]/'publications/LULA-I'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
current=read(X/'POLYNOMIAL-PRIVATE-PROMOTION.json');prior=read(X/'POLYNOMIAL-UD-PROMOTION.json')
checks={}
checks['all321_actual_absolute_pins_match']=len(current['accepted_evidence_absolute_pins'])==321 and all(sha(Path(k))==v for k,v in current['accepted_evidence_absolute_pins'].items())
checks['all268_prior_pins_retained_unchanged']=len(prior['accepted_evidence_absolute_pins'])==268 and all(current['accepted_evidence_absolute_pins'].get(k)==v for k,v in prior['accepted_evidence_absolute_pins'].items())
for g in ('documents','artifacts','receipt_pins'):
 checks[g+'_current_pins_match']=all(sha(X/k)==v for k,v in current[g].items())
checks['six_backups_exact_prior_current_cut']=current['predecessor_documents']==prior['documents'] and all(sha(X/current['predecessor_backup']/k)==v for k,v in prior['documents'].items())
diff=[];additions={};docs={}
for name in prior['documents']:
 old=(X/current['predecessor_backup']/name).read_text(encoding='utf-8');now=(X/name).read_text(encoding='utf-8')
 assert now.startswith(old.rstrip()),name
 additions[name]=now[len(old.rstrip()):]
 docs[name]={'prior_sha256':sha(X/current['predecessor_backup']/name),'current_sha256':sha(X/name),'only_append_except_trailing_whitespace':True}
 diff.extend(difflib.unified_diff(old.splitlines(True),now.splitlines(True),fromfile=current['predecessor_backup']+'/'+name,tofile=name))
(E/'MANUAL-DIFF.txt').write_text(''.join(diff),encoding='utf-8')
common=additions['PROOF.md']
checks['five_identical_additions_and_TERM_has_same_common_prefix']=all(v==common for k,v in additions.items() if k!='TERM-TABLE.md') and additions['TERM-TABLE.md'].startswith(common.rstrip())
checks['complete_formula_scope_and_original_goal_open_explicit']=all(x in common for x in ('one-sided P','S=0 is paid once','Private caps areQ_A','zero probability/query loss','probability exponents, not security work factors','64 endpoints','not established','47 supporting','whole-source/game declarations0','classical3Q candidate remains separate and unpromoted'))

full=read(X/'pre-start-second/polynomial-private-composition/FINAL-SUBJECT-REVIEW.json')
checks['complete_final_receipt_current_subject_and_all_checks']=full['subject_sha256']==sha(X/'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md') and all(full['checks'].values()) and not full['whole_goal_complete']
for k,v in full['private_hop_chain'].items():assert sha(X/k)==v,k
checks['K_P_current_subject_and_final_receipt_chain']=True
data=read(X/'root-polynomial-private-composition/RESULTS.json')
own=read(X/'pre-start-second/polynomial-private-composition/INDEPENDENT-NUMERICS.json')
comparison=read(X/'pre-start-second/polynomial-private-composition/AFTER-FIRST-COMPARISON.json')
checks['current16_rows_and336_comparisons_pinned']=len(data['rows'])==len(own['rows'])==16 and comparison['numeric_comparisons']==336 and comparison['root_new_dataset_sha256']==sha(X/'root-polynomial-private-composition/RESULTS.json') and full['root_dataset_sha256']==sha(X/'root-polynomial-private-composition/RESULTS.json')
checks['original_datasets_and_own_before_peer_first_preserved']=comparison['independent_first_sha256']==sha(X/'pre-start-second/polynomial-private-composition/INDEPENDENT-FIRST.md') and comparison['independent_dataset_sha256']==sha(X/'pre-start-second/polynomial-private-composition/INDEPENDENT-NUMERICS.json')

certificate=read(X/'outside-field-check/polynomial-query-thresholds/NEW-CERTIFICATES.json')
final=read(X/'outside-field-check/polynomial-query-thresholds/FINAL-CERTIFICATE.json')
cross=read(X/'root-polynomial-private-composition/THRESHOLD-CROSSCHECK.json')
checks['final_outward_certificate_and_root_crosscheck_exact_subject']=certificate['pins']['QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md']==final['subject_sha256']==cross['subject_sha256']==sha(X/'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md') and cross['certificate_sha256']==sha(X/'outside-field-check/polynomial-query-thresholds/NEW-CERTIFICATES.json')
for k,v in final['input_pins'].items():assert sha(X/k)==v,k
for k,v in final['own_pins'].items():assert sha(X/'outside-field-check/polynomial-query-thresholds'/k)==v,k
checks['outward_certificate_all_input_and_own_pins_match']=True
checks['threshold32_pairs_correct_models_q_grid']=len(certificate['rows'])==32 and {(r['log2_q'],r['model']) for r in certificate['rows']}=={(q,m) for q in (24,30,38,40,41,44,50,64) for m in ('conservative','event','polynomial','best')}
source_pf=read(X/'classical-composition-numeric/OWN-BOUNDS.json')
pf_seen={}
def from_dyadic(t):
 sign,mantissa,exponent,length=t
 assert sign==0 and mantissa.bit_length()==length
 return F(mantissa*(1<<exponent)) if exponent>=0 else F(mantissa,1<<(-exponent))
for row in source_pf['rows']:
 qe=row['log2_signing_query_cap'];r=row['FORS_per_raw_candidate']
 interval=(from_dyadic(r['lower_dyadic_mpf_tuple']),from_dyadic(r['upper_dyadic_mpf_tuple']))
 if qe in pf_seen:assert pf_seen[qe]==interval
 pf_seen[qe]=interval
 actual=tuple(F(*map(int,z)) for z in certificate['FORS_enclosures'][str(qe)]['enclosure'])
 assert actual==interval
checks['all8_pF_intervals_equal_actual_reviewed_prior_dyadic_inputs']=set(pf_seen)=={24,30,38,40,41,44,50,64}

# Independent fresh 448-bit outward evaluator, using expanded square formulas.
# The already reviewed pF enclosures are explicit inputs, not midpoint values.
N=1<<128;M=N*N-N;bits=448;den=1<<bits
def root(z,upper):
 a=isqrt((z.numerator<<(2*bits))//z.denominator)
 lo=F(a,den)
 hi=lo if lo*lo==z else F(a+1,den)
 assert lo*lo<=z<=hi*hi
 return hi if upper else lo
def value(q,Q,pf,up):
 r=lambda z:root(F(z),up)
 D=min(F(1),q*(r(F(Q+q+1,M))+F(Q+q+1,2*M)))
 A=min(F(1),D+8*(Q+2)**2*(pf+F(1,N)+F(q,N*N)))
 c=min(F(1),F(4*Q*Q+q+4*(Q+2)**2,N)+F(4*Q,N)*r(q)+F(4*(Q+2),1<<64)*r(A)+A)
 h=min(F(1),F(4*Q*Q+3017,N)+F(4*Q,N)*r(3017))
 g=min(F(1),F(8*(Q+3218)**2,N));d=min(F(1),F(8*(Q+6)**2,N))
 pub=c+h+g+d;e=min(F(1),pub)
 con=min(F(1),F(1,N)+min(F(1),F(2*Q,1<<64)+F(2*q+2,N))+pub)
 b=min(F(1),F(2*q+2,N));z=min(F(1),b+e);t0=F(2*Q,1<<64)
 event=min(F(1),F(1,N)+t0*t0+2*t0*r(z)+z)
 v=min(F(1),F(4*Q*Q,N-4*Q*Q)) if 4*Q*Q<N else F(1)
 C=min(N,2*q+2)
 t=min(F(1),F(4*Q*Q+C,N)+F(4*Q,N)*r(C))
 poly=min(F(1),F(1,N)+v+min(F(1),v+t)+e)
 return {'conservative':con,'event':event,'polynomial':poly,'best':min(con,event,poly)}
pair=lambda x:F(*map(int,x))
endpoints=[];worst_ratio=F(0)
for row in certificate['rows']:
 q=1<<row['log2_q'];pf=certificate['FORS_enclosures'][str(row['log2_q'])]['enclosure'];p0,p1=map(pair,pf)
 assert 0<=p0<=p1<=F(1,512)
 assert int(row['Q_fail'])==int(row['Q_pass'])+1
 assert pair(row['pass_interval']['upper'])<=F(1,2)<pair(row['fail_interval']['lower'])
 for label in ('pass','fail'):
  Q=int(row['Q_'+label]);lo=value(q,Q,p0,False)[row['model']];hi=value(q,Q,p1,True)[row['model']]
  assert lo<=hi
  margin=F(1,2)-hi if label=='pass' else lo-F(1,2)
  assert margin>0,(row['log2_q'],row['model'],label)
  worst_ratio=max(worst_ratio,(hi-lo)/margin)
  endpoints.append({'q_exponent':row['log2_q'],'model':row['model'],'endpoint':label,'Q':str(Q),'verified_exact':True})
checks['all64_adjacent_endpoint_rational_gates_recertified_at448bits']=len(endpoints)==64 and worst_ratio<F(1,1<<200)
checks['threshold_monotonicity_scope']=certificate['best_crossing_equals_max_component_crossings'] and not certificate['whole_goal_complete'] and certificate['new_source_game_declarations']==0
for qe in (24,30,38,40,41,44,50,64):
 r=[z for z in certificate['rows'] if z['log2_q']==qe]
 best=next(z for z in r if z['model']=='best')
 assert int(best['Q_pass'])==max(int(z['Q_pass']) for z in r if z['model']!='best')
old=read(X/'query-resource-independent/THRESHOLDS.json')
for r in certificate['rows']:
 if r['model'] in ('conservative','event'):
  oldname={'conservative':'quantum_conservative','event':'quantum_event'}[r['model']]
  previous=next(z for z in old['rows'] if (z['log2_q'],z['model'])==(r['log2_q'],oldname))
  assert previous['Q_pass']==r['Q_pass'] and previous['Q_fail']==r['Q_fail']
checks['old_quantum_individual_thresholds_unchanged']=True

table=re.findall(r'^\| 2\^(\d+) \| ([0-9.]+) \| 1 \(cap\) \| (\d+) \|$',additions['TERM-TABLE.md'],re.M)
assert len(table)==8
for qe,exp,Q in table:
 qe=int(qe)
 dr=next(z for z in data['rows'] if (z['log2_q'],z['log2_Q'])==(qe,32))
 tr=next(z for z in final['best_rows'] if z['log2_q']==qe)
 assert exp==f"{dr['exponents']['poly_total']:.6f}" and Q==tr['Q_pass']
 checks['TERM_table_'+str(qe)+'_matches_numeric_and_certificate']=True

# Recheck current protected manuscript/source cut and retained prior helper data.
base=read(X/'PRESERVATION-BASELINE.json')
frozen={str(f.relative_to(S)):sha(f) for f in S.rglob('*') if f.is_file() and not f.is_relative_to(S/'extensions')}
checks['frozen165_packet_files_and_crypto_sources_unchanged']=frozen==base['frozen_packet'] and len(frozen)==165 and all(sha(Path(k))==v for k,v in base['crypto'].items())
paper=dict(base['current_paper'])
for name in ('AUTHORIZED-EDITORIAL-DELTA.json','AUTHORIZED-EDITORIAL-DELTA-20261013.json'):
 if (X/name).exists():
  rec=read(X/name);assert sha(Path(rec['patches_path']))==rec['patches_sha256']
  for n,c in rec['paper_changes'].items():assert paper[n]==c['before'];paper[n]=c['after']
checks['seven_publication_files_at_authorized_current_cut']=all(sha(P/k)==v for k,v in paper.items())
previous_audit=read(X/'pre-start-second/polynomial-ud-current-index/COMPUTED-CHECKS.json')
for h in previous_audit['previous_helpers']:
 assert sha(X/h['source'])==h['source_sha256'] and sha(X/h['receipt'])==h['receipt_sha256']
 rec=read(X/h['receipt']);assert rec['exit_code']==0
checks['47_prior_supporting_helpers_source_and_receipt_pins']=sum(h['supporting_declarations'] for h in previous_audit['previous_helpers'])==47
for n,obj in previous_audit['historical_numeric_receipts'].items():assert sha(X/n)==obj['sha256'] and len(read(X/n)['rows'])==16
checks['48_prior_scalar_cells_receipts_unchanged']=True
assert len(old['rows'])==32
for n,v in old['input_pins'].items():assert sha(X/n)==v,n
checks['32_prior_resource_crossing_pins_unchanged']=True
checks['47_helpers0newgame0sourcechanges_no_classical_promotion_no_fullgoal']=current['cumulative_supporting_checked_declarations']==47 and current['new_source_game_checked_declarations']==current['source_scalar_manuscript_changes']==0 and not current['classical_joint_candidate_promoted'] and not current['whole_goal_complete'] and current['original_level_category_statement']=='not established'
out={'status':'PASS_FRESH321_PIN_APPEND_TABLE_AND64_OUTWARD_ENDPOINT_CHECKS' if all(checks.values()) else 'FAIL',
 'subject_sha256':sha(X/'POLYNOMIAL-PRIVATE-PROMOTION.json'),'prior_subject_sha256':sha(X/'POLYNOMIAL-UD-PROMOTION.json'),
 'current_pins':321,'prior_pins_retained':268,'new_pins':53,'checks':checks,'documents':docs,
 'manual_diff_sha256':sha(E/'MANUAL-DIFF.txt'),'script_sha256':sha(Path(__file__)),
 'threshold_certificate_sha256':sha(X/'outside-field-check/polynomial-query-thresholds/NEW-CERTIFICATES.json'),
 'threshold_final_receipt_sha256':sha(X/'outside-field-check/polynomial-query-thresholds/FINAL-CERTIFICATE.json'),
 'threshold_root_crosscheck_sha256':sha(X/'root-polynomial-private-composition/THRESHOLD-CROSSCHECK.json'),
 'own_outward_sqrt_bits':bits,'endpoints':endpoints,'max_interval_width_over_margin':str(worst_ratio),
 'table_rows_checked':8,'threshold_pairs':32,'publication_pins':paper,
 'whole_goal_complete':False,'new_source_game_declarations':0,'root_validator_or_core_writes':False}
(E/'COMPUTED-CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'checks':len(checks),'failures':[k for k,v in checks.items() if not v],'currentpins':321,'retained':268,'endpoint_checks':64,'table':8,'subject_sha256':out['subject_sha256']}))

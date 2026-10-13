"""Read-only independent promotion audit; outputs only beside this script."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, difflib, re

OUT = Path(__file__).resolve().parent
X = OUT.parent.parent
S = X.parents[1]
P = S.parents[1] / 'publications' / 'LULA-I'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text(encoding='utf-8'))
index = read(X/'POLYNOMIAL-UD-PROMOTION.json')
prior = read(X/'TARGET-PRE-PROMOTION.json')
checks = {}
checks['current_evidence_pin_count_268'] = len(index['accepted_evidence_absolute_pins']) == 268
checks['prior_evidence_pin_count_228'] = len(prior['accepted_evidence_absolute_pins']) == 228
checks['all_228_prior_pins_retained_unchanged'] = all(index['accepted_evidence_absolute_pins'].get(k)==v for k,v in prior['accepted_evidence_absolute_pins'].items())
checks['all_268_absolute_files_match'] = all(sha(Path(k))==v for k,v in index['accepted_evidence_absolute_pins'].items())
for group in ('documents','artifacts','receipt_pins'):
    checks[group+'_all_current_pins_match'] = all(sha(X/k)==v for k,v in index[group].items())
checks['predecessor_equals_target_pre_documents'] = index['predecessor_documents']==prior['documents']
checks['all_six_backup_pins_match'] = all(sha(X/index['predecessor_backup']/k)==v for k,v in prior['documents'].items())

diffs=[]; additions=[]; doc_records={}
for name in prior['documents']:
    old=(X/index['predecessor_backup']/name).read_text(encoding='utf-8')
    now=(X/name).read_text(encoding='utf-8')
    stem=old.rstrip()
    prefix=now.startswith(stem)
    assert prefix,name
    add=now[len(stem):]
    additions.append(add)
    doc_records[name]={'prior_sha256':sha(X/index['predecessor_backup']/name),
                       'current_sha256':sha(X/name),
                       'prior_content_preserved_except_trailing_whitespace':prefix,
                       'addition_sha256':hashlib.sha256(add.encode()).hexdigest(),
                       'addition_lines':len(add.splitlines())}
    diffs.extend(difflib.unified_diff(old.splitlines(True),now.splitlines(True),
                 fromfile='root-docs-before-polynomial-ud/'+name,tofile=name))
(OUT/'MANUAL-DIFF.txt').write_text(''.join(diffs),encoding='utf-8')
checks['six_append_only_content_changes'] = len(doc_records)==6 and all(r['prior_content_preserved_except_trailing_whitespace'] for r in doc_records.values())
checks['same_addition_all_six_documents'] = len(set(additions))==1
checks['scope_boundaries_present_in_addition'] = all(term in additions[0] for term in (
    'Q_A+1','7628143271608320','20229886488608768','SAME conditional joint law',
    'whole marker field','between-grid overshoot','newly checked whole-source/game declarations0',
    'direct source H bound','not established','Private-K/private-P polynomial candidates'))

field=read(X/'outside-field-check/ud-polynomial/FINAL-SUBJECT-REVIEW.json')
selected=read(X/'selected-promotion-review/quantitative-goal-audit/single-ud-polynomial/FINAL-SUBJECT-REVIEW.json')
successor=read(X/'selected-promotion-review/quantitative-goal-audit/single-ud-polynomial/FINAL-STATUS-SUCCESSOR-REVIEW.json')
checks['final_math_receipts_checks_pass'] = all(all(r['checks'].values()) for r in (field,selected,successor))
checks['final_math_status_successor_pins_current_subject'] = field['subject_sha256']==successor['subject_sha256']==sha(X/'QUANTUM-UD-POLYNOMIAL-RO.md')
checks['selected_prior_subject_preserved_by_exact_backup'] = selected['subject_sha256']==successor['prior_subject_sha256']==sha(X/'root-docs-before-ud-status/QUANTUM-UD-POLYNOMIAL-RO.md')
checks['all_math_receipts_whole_goal_false'] = all(not r['whole_goal_complete'] for r in (field,selected,successor))
checks['index_helpers47_newgame0_sourcechanges0_wholegoalfalse'] = index['cumulative_supporting_checked_declarations']==47 and index['new_source_game_checked_declarations']==index['source_scalar_manuscript_changes']==0 and not index['whole_goal_complete']

# Independently reconstruct activation coefficients and exact numeric rows.
N=1<<128
Klow=sum(1<<e for e in (41,36,31,26))
A=[32*Klow*max(14-r,0)+16*(1<<21)*(254-r) for r in range(254)]
AH=sum(A)
DW=32*Klow*15+16*(1<<21)*255
DF=17*512*(1<<41)
DH=DW+DF
assert AH==7628143271608320 and DH==20229886488608768
def terms(qa):
    R=qa+1
    pre=min(F(1),F((2*R+1)**2*(2*N-1),N*N))
    u=min(F(1),F(N-1,N)*F(4*R*R,N-4*R*R)) if 4*R*R<N else F(1)
    return R,pre,u,DH*pre+AH*u
HS=(1<<21)*(19505+(1<<32))-1
H={'prepared':82090+5*(1<<32),'absent':8560574463+82090+6*(1<<32)}
numeric=read(X/'root-ud-polynomial/CONTROLS.json')
expected={(q,m,a) for q in (24,30,38,40,41,44,50,64) for m in H for a in (32,64)}
actual={(r['log2_q'],r['mode'],r['log2_QA']) for r in numeric['rows']}
checks['exact_32_row_selector_coverage'] = len(numeric['rows'])==32 and actual==expected
row_records=[]
for row in numeric['rows']:
    qa=1<<row['log2_QA']; R,pre,u,total=terms(qa)
    ok=int(row['remote_calls'])==R and F(row['PRE_bound'])==pre and F(row['UD_bound'])==u and F(row['uncapped_component'])==total and F(row['capped_component'])==min(F(1),total)
    outside=qa+HS+(1<<row['log2_q'])*H[row['mode']]+3224+254
    ok=ok and int(row['outside_call_cap'])==outside
    row_records.append({'q_exponent':row['log2_q'],'mode':row['mode'],'QA_exponent':row['log2_QA'],'pass':ok})
checks['all_32_rows_reconstructed_exactly'] = all(r['pass'] for r in row_records)
checks['QA32_positive_noncap_QA64_cap'] = all((F(r['capped_component'])<1 if r['log2_QA']==32 else F(r['capped_component'])==1) for r in numeric['rows'])
crossings=[]
for c in (F(1,2),F(1)):
    lo,hi=0,1<<64
    while lo+1<hi:
        mid=(lo+hi)//2
        if terms(mid)[3]<=c:lo=mid
        else:hi=mid
    crossing=next(r for r in numeric['uncapped_crossings'] if F(r['uncapped_target'])==c)
    assert int(crossing['QA_pass'])==lo and int(crossing['QA_fail'])==hi
    assert F(crossing['pass_value'])==terms(lo)[3]<=c<terms(hi)[3]==F(crossing['fail_value'])
    crossings.append({'target':str(c),'pass':lo,'fail':hi})
checks['two_uncapped_adjacent_thresholds_exact'] = crossings==[{'target':'1/2','pass':29741080993,'fail':29741080994},{'target':'1','pass':42060240100,'fail':42060240101}]

# Preserve the pre-existing paper/source/packet cut without calling writing validators.
baseline=read(X/'PRESERVATION-BASELINE.json')
frozen={str(f.relative_to(S)):sha(f) for f in S.rglob('*') if f.is_file() and not f.is_relative_to(S/'extensions')}
checks['frozen_165_packet_files_unchanged'] = frozen==baseline['frozen_packet'] and len(frozen)==165
checks['protected_crypto_source_hashes_unchanged'] = all(sha(Path(k))==v for k,v in baseline['crypto'].items())
paper_expected=dict(baseline['current_paper'])
editorial=[]
for name in ('AUTHORIZED-EDITORIAL-DELTA.json','AUTHORIZED-EDITORIAL-DELTA-20261013.json'):
    f=X/name
    if f.exists():
        rec=read(f)
        assert sha(Path(rec['patches_path']))==rec['patches_sha256']
        for k,c in rec['paper_changes'].items():
            assert paper_expected[k]==c['before']
            paper_expected[k]=c['after']
        editorial.append(name)
checks['seven_paper_files_match_authorized_current_cut'] = all(sha(P/k)==v for k,v in paper_expected.items())

helper_specs=[
 ('root-formal/SeedGuess.ec','root-formal/easycrypt-current.json',4),
 ('formal-tree/AddressedMerkle.lean','formal-tree/check.json',5),
 ('wots-certification/ChainEvidence.lean','wots-certification/check.json',8),
 ('root-formal/SPRSeparation.lean','root-formal/SPRSeparation-check.json',4),
 ('query-resource-formal/QueryThreshold.lean','query-resource-formal/CHECK.json',7),
 ('private-challenge-program/AdapterCounts.ec','private-challenge-program/EASYCRYPT-CHECK.json',5),
 ('selected-promotion-review/QPRE-Averaging.lean','selected-promotion-review/QPRE-Lean-Check.json',7),
 ('root-keyed-review/CounterPolicy.lean','root-keyed-review/COUNTER-POLICY-CHECK.json',4),
 ('root-message-hash/DigestProjection.lean','root-message-hash/PROJECTION-CHECK.json',3)]
helpers=[]
for src,receipt,count in helper_specs:
    rec=read(X/receipt)
    assert rec['source_sha256']==sha(X/src) and rec['exit_code']==0
    assert not re.search(r'\b(sorry|admit|native_decide)\b',(X/src).read_text(encoding='utf-8'))
    helpers.append({'source':src,'source_sha256':sha(X/src),'receipt':receipt,'receipt_sha256':sha(X/receipt),'supporting_declarations':count,'kernel_reexecuted':False})
checks['47_previous_supporting_helpers_receipt_and_source_pins'] = sum(r['supporting_declarations'] for r in helpers)==47

historical={}
historical_rows=0
for name in ('quantum-composition-numeric/ROOT-CROSSCHECK.json','quantum-private-rare-numeric/ROOT-REFINED-CROSSCHECK.json','root-current-classical-recheck/ROOT-CROSSCHECK.json'):
    rec=read(X/name)
    assert len(rec['rows'])==16
    historical_rows+=len(rec['rows'])
    historical[name]={'sha256':sha(X/name),'status':rec.get('status',rec.get('outcome')),'rows':len(rec['rows'])}
    for k,v in rec.get('artifact_pins',{}).items():assert sha(X/k)==v,k
checks['48_historical_cells_remain_in_three_reviewed_sets'] = historical_rows==48
qc=read(X/'quantum-composition-numeric/ROOT-CROSSCHECK.json')
for name,digest in qc['root_output_sha256'].items():
    f=X/'root-checks'/name/'bounds.json'
    assert sha(f)==digest and len(read(f)['rows'])==8
cc=read(X/'root-current-classical-recheck/ROOT-CROSSCHECK.json')
assert cc['root_rows_compared']==16
checks['historical_numeric_receipts_and_retained_output_pins'] = True
thresholds=read(X/'query-resource-independent/THRESHOLDS.json')
assert len(thresholds['rows'])==32
for k,v in thresholds['input_pins'].items():assert sha(X/k)==v,k
checks['32_previous_resource_crossings_input_pins_unchanged'] = True

result={'status':'PASS_COMPUTED_CURRENT_INDEX_AND_PRESERVATION_CHECKS' if all(checks.values()) else 'FAIL',
 'promotion_sha256':sha(X/'POLYNOMIAL-UD-PROMOTION.json'),'prior_promotion_sha256':sha(X/'TARGET-PRE-PROMOTION.json'),
 'current_evidence_pins':268,'retained_evidence_pins':228,'new_evidence_pins':40,
 'checks':checks,'documents':doc_records,'all_row_checks':row_records,'source_coefficients':{'D_H':DH,'A_H':AH,'remote':'Q_A+1'},
 'uncapped_crossings':crossings,'previous_helpers':helpers,'historical_numeric_receipts':historical,
 'authorized_editorial_cut':editorial,'manuscript_current_pins':paper_expected,
 'script_sha256':sha(Path(__file__)),'manual_diff_sha256':sha(OUT/'MANUAL-DIFF.txt'),
 'new_source_game_declarations':0,'whole_goal_complete':False,
 'did_run_core_validator_or_rewrite_core':False}
(OUT/'COMPUTED-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'checks':len(checks),'failures':[k for k,v in checks.items() if not v],
                  'newpins':40,'rows':32,'crossings':crossings,'helpers':47,'promotion_sha256':result['promotion_sha256']}))

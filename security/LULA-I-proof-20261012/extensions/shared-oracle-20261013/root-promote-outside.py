"""Promote independently reviewed B-only bounded-query simulator, once ready.

All prior theorem/calculator and source artifacts remain immutable.
"""
from pathlib import Path
import hashlib, json, shutil

X = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda n: (X/n).read_text(encoding='utf8')
load = lambda n: json.loads(read(n))
docs = ['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
prior = load('selected-promotion-review/T7-INTEGRATION-REVIEW.json')
peer = load('outside-field-check/SECOND-READER.json')
assert peer['verdict']=='ACCEPT_SCOPED_MANUAL_BOUNDED_QUERY_CONSTRUCTION_AND_B_ONLY_REPLACEMENT'
assert all(peer['manual_acceptance'].values()) and peer['control_exit_code']==0
for n,h in peer['subject_pins'].items(): assert sha(X/n)==h,n
for n,h in peer['inherited_premise_pins'].items(): assert sha(X/n)==h,n
assert sha(X/'outside-field-check/SECOND-READER.md')==peer['review_sha256']
assert sha(X/'outside-field-check/toy_controls.py')==peer['control_source_sha256']
assert sha(X/'outside-field-check/toy-results.json')==peer['control_results_sha256']
# The author's separate successor/control packet is still being prepared.
# It is not needed or counted here: the immutable first subject is already
# independently reviewed, with a separately derived/executed control packet.
assert peer['first_independent_derivation_saved_before_peer_reads']
assert sha(X/'outside-field-check/first-independent-derivation.md')==peer['first_independent_derivation_sha256']
assert load('root-outside-simulator/RESOURCE-CHECK.json')['eight_inherited_q_rows_checked']==8
assert sha(X/'root-outside-simulator/field-recheck/toy-results.json')==peer['control_results_sha256']
for n,h in prior['documents'].items(): assert sha(X/n)==h,n
protected = dict(prior['preserved_artifacts'])
protected.update(prior['promoted_artifacts'])
assert all(sha(X/n)==h for n,h in protected.items())
backup = X/'root-docs-before-outside'
assert not backup.exists(), 'Do not overwrite a promoted predecessor cut.'
backup.mkdir()
for n in docs: shutil.copyfile(X/n,backup/n)
subject = read('chain-pre-adapter/outside-simulator/INDEPENDENT-DERIVATION.md')
old='**PROVED — manual first candidate awaiting independent reading.**'
assert subject.count(old)==1
subject=subject.replace(old,'**PROVED — manual bounded-query B-only construction accepted by an independent mathematical reader.**',1)
old='**OPEN — independent reading and controls.**'
assert subject.count(old)==1
subject=subject.replace(old,'**PROVED / COMPUTED — review and controls supplied in the successor evidence below.**',1)
old='The direct tower irreducibility/multiplication construction, exact k-wise/whole-B route, malformed-state extension and complete budget need a different reader and discriminating finite controls before promotion. No new kernel declaration is claimed yet.'
assert subject.count(old)==1
subject=subject.replace(old,'The direct tower construction, whole-B route and matched invalid-state extension have received independent manual reading and discriminating finite controls. Complete numeric source caps are inherited from the already reviewed adapters and root arithmetic checks; this is not a new source-count audit. No new kernel declaration is claimed.',1)
header='''# Efficient finite outside-function simulator

**PROVED / CITED — accepted scope.** This successor replaces only the local independent outside RF used by the PRE/type7 reduction programs. It preserves their bounded final challenge-success probabilities exactly, under the inherited finite source call caps. The original source experiment, event partition, numerical bounds and prior eager-table proofs are unchanged. The accepted implementation uses direct deterministic tower coordinates; the optional monogenic modulus route and optional full SOURCE classifier replacement are not required for this promotion.

**CITED — exact query theorem.** Zhandry, *How to Construct Quantum Random Functions*, ECCC TR12-140, Fact 2, printed page 5: https://eccc.weizmann.ac.il/report/2012/140/download/ . The theorem is applied to all function evaluations in the compiled algorithm, including honest classical calls. It supplies exact averaged bounded-query output equality, not global RF-table equality.

'''
footer='''
## Accepted successor and checks

**PROVED — exact application.** Let T_PRE=Q+H_setup+q H_mode+3224+254 and T_ROW=Q+H_setup+q H_mode+3224+17392. For the same independent Selected/private/challenge environment, p_PRE,eager=p_PRE,family and p_ROW,eager=p_ROW,family. The existing source inequalities therefore hold with family challenge advantages and no extra statistical term. For type7, condition on the independent full Row, never on the outside-dependent registered target Y/c0. The original source event H_final and exposed successful D7_base_final are retained.

**PROVED — complete deterministic charges.** Runtime coefficient/descriptor initialization uses O(km+b^2) bit writes. Emitting a uniform full gate list additionally costs O(km^2+b^2), which is charged, not free preprocessing. T Eval calls cost O(T(km^2+b^2)) gates; key/work storage is O(km+m^2+b^2) bits besides source/A/challenger storage. All uses share one hidden coefficient key and a matched fixed invalid-state extension. These are polynomial in complete source-call cap T and register-length bound b; enormous worst-case honest budgets preclude any practical or category conclusion.

**COMPUTED — evidence.** Independent first derivations preceded peer reading; the author's first save records receiving only a brief tower-route status, not peer proof details. The additional field reader saved its own complete derivation before reading either candidate. Exact small-field controls check arithmetic, trace, limited independence, full-output projection, encoding, clean oracle routing and a negative omitted-honest-call test. Root reexecuted the third reader's control and checked 64 resource examples covering eight signing caps, two adversarial budgets, two cache regimes and both adapters. These controls are not whole-source or arbitrary-degree kernel proofs. No supporting declaration is added; the existing 40 checked helpers remain unchanged.

**OPEN — original remaining target.** Conventional shared-seed keyed PRF/PRE/TCR identification, adequate level/category security and certified signing capacity remain unestablished. This result does not provide an external pk-only cache simulator, a fixed-SHA theorem or an implementation/termination refinement. Optional SOURCE-classifier reachability is not newly certified. The original full-proof goal remains active.
'''
(X/'OUTSIDE-SIMULATOR-THEOREM.md').write_text(header+subject+'\n'+footer,encoding='utf8')
addition='''
**PROVED / CITED — efficient bounded-query B-only successor.** OUTSIDE-SIMULATOR-THEOREM.md supplies the deterministic direct binary-tower polynomial family and exact bounded-query replacement for the existing PRE/type7 reductions. All honest source calls are included in T, and initialization, uniform circuit generation, clean reversible evaluation and storage are charged. The complete source probability formulas and old tables remain unchanged. Conventional primitive identification, level/category and certified capacity remain OPEN; no new kernel security theorem is claimed.
'''
for n in docs:
    if n=='PROOF.md': text='\n## 14. Bounded-query efficient outside simulator\n'+addition
    elif n=='HANDOFF.md':
        text='''
**PROVED / COMPUTED — latest continuation is PROGRESS.** The preceding response finished a separately requested paper-genre verification and made no proof progress. This continuation completes type7 current-index validation, clarifies one-time seed-zero accounting without numerical changes, and promotes an independently reviewed exact bounded-query outside simulator. Deterministic tower arithmetic avoids exponential byte-domain tables while preserving PRE/Row challenge-success laws. Root checked 64 complete resource profiles and reexecuted independent finite controls. Forty supporting checked declarations and all prior scalar/source/paper artifacts are preserved.

**OPEN — next original work.** Ordinary shared-seed primitive identification and adequate full-security level/category/capacity remain unfinished. The outside simulation resource sub-obligation is now closed for the B-only finite-input relative programs; optional full SOURCE-classifier replacement and external pk-only cache simulation are different claims. A source/primary-definition standard-identification review is running in selected-promotion-review/standard-identification. Do not invent a security certificate or repeat a filtered operational attack. Goal remains active.
'''
    else: text=addition
    (X/n).write_text(read(n).rstrip()+'\n\n'+text.strip()+'\n',encoding='utf8')
assert all(sha(X/n)==h for n,h in protected.items())
record={'status':'REVIEWED_OUTSIDE_SUBJECT_PROMOTED_CURRENT_INDEX_REVIEW_PENDING',
        'documents':{n:sha(X/n) for n in docs},'prior_documents':prior['documents'],
        'new_artifact':{'OUTSIDE-SIMULATOR-THEOREM.md':sha(X/'OUTSIDE-SIMULATOR-THEOREM.md')},
        'subject_pins':peer['subject_pins'], 'second_reader_sha256':sha(X/'outside-field-check/SECOND-READER.json'),
        'author_final_packet':'Still in progress; not relied upon. Accepted immutable first subject and independent field controls are pinned by the second-reader receipt.',
        'root_resource_sha256':sha(X/'root-outside-simulator/RESOURCE-CHECK.json'),
        'prior_type7_receipt_sha256':sha(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.json'),
        'preserved_artifacts':protected,'new_checked_declarations':0,
        'supporting_checked_declarations_total':40,'whole_source_game_checked_declarations':0,
        'B_only_probability_preservation':True,'full_source_classifier_newly_certified':False,
        'level_category':'not established','manuscript_edits':0}
(X/'OUTSIDE-SIMULATOR-PROMOTION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'promoted':'OUTSIDE-SIMULATOR-THEOREM.md','docs':6,'old_artifacts_preserved':len(protected)}))

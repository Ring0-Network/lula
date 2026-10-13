"""Promote clarified finite first-accepted-row collision adapter."""
from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:(X/n).read_text(encoding='utf8')
write=lambda n,t:(X/n).write_bytes(t.encode('utf8'))
peer=json.loads(read('chain-pre-independent/type7/SUCCESSOR-REVIEW.json'))
assert peer['status']=='ACCEPTED_SCOPED_RO_QROM_RELATIVE_MANUAL'
assert peer['clarification_read'] and not peer['numeric_changes']
for n,h in peer['subjects'].items():assert sha(X/'chain-pre-adapter/type7'/n)==h,n
resource=json.loads(read('selected-promotion-review/T7-REVIEW.json'))
assert resource['verdict']=='ACCEPT_SCOPED_FIRST_ACCEPTED_TYPE7_ROW_RESOURCES_AND_INTERFACE'
assert all(resource['checks'].values())
for n,h in resource['subject_pins'].items():assert sha(X/n)==h,n
for n,h in resource['own_pins'].items():assert sha(X/'selected-promotion-review'/n)==h,n
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
B=X/'root-docs-before-type7';assert not B.exists(),'Single-use promotion; inspect saved state before rerun.'
B.mkdir()
for n in docs:
    assert sha(X/n)==resource['prior_documents'][n],n
    shutil.copyfile(X/n,B/n)
prior={n:sha(X/n) for n in docs}
protected=['CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md','QUANTUM-COVERAGE-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md','bounds.py','bounds-event-specific.py','SELECTED-GRAPH-REDUCTION.md','CHANGED-CHILD-EXTRACTION.md','CLASSICAL-PRE-REDUCTION.md','QUANTUM-PRE-REDUCTION.md']
protected_pins={n:sha(X/n) for n in protected}
subject=read('chain-pre-adapter/type7/INDEPENDENT-DERIVATION.md')
old='**PROVED — manual source-first candidate awaiting second reading.**'
assert subject.count(old)==1
subject=subject.replace(old,'**PROVED — manually source-derived adapter, accepted by an independent source-first reader.**',1)
old='**OPEN — remaining assumptions/gates.** Independent second reading/control checks are needed before promotion.'
assert subject.count(old)==1
subject=subject.replace(old,'**PROVED / COMPUTED — independent source reading and controls accepted within the named interface.** The original subject and event/stopping clarification have hash-bound source and resource reviews; no full-source kernel theorem is asserted.',1)
header='''# Reviewed type7 canonical-row, changed-base collision reduction

**PROVED / COMPUTED / OPEN — controlling scope and event names.** This finite addressed-RO-relative chosen-base acceptance-row challenge commits the genuine child before the selected function is drawn and keeps the entire first-accepted/rejected-counter row law. The original final-forgery event stays D7_base_final: reached, honestly exposed and successfully canonical, with a changed16-byte child and equal128-bit digest. The optional larger classical raw-query event is D7_base_public, with D7_base_final subset D7_base_public. The frozen candidate's classical-public wording is read with these distinct names. Coherent queries are forwarded without measurement; extraction is only from the final classical verifier.

**PROVED — stopping precision.** The unflagged comparator has ordinary source law. Actual B can terminate early after a valid primitive collision and is faithful only on the source prefix before that stop. Missing selected canonical target causes local B failure with zero selected-source-event contribution; it does not add a source abort for an unused failed row or normalize source setup success. These controls supersede any broader reading of the preserved original text below.

'''
footer='''
## Accepted result, resources and provenance

**PROVED / COMPUTED — finite RO/QROM-relative reduction.** For every fixed nonzero public seed, Pr_HJ[Win AND D7_base_final]<=2^42 Pr[B_ROW_quantum wins]; the classical public superevent has the corresponding2^42 inequality. All candidate counters are permitted but same-child counter-only matches are excluded. The target comparison is128-prefix equality while the raw oracle and registered target retain their complete256-bit images. Canonical preprocessing uses at most2^32 selected-function evaluations inside the challenger and is charged separately from B's Q+1 selected query cap. This is not an unexplained free target or a1/p_layer loss.

**COMPUTED — exact localized accounting.** There are2,269,959,421,952 real WOTS rows in a42-bit pad. A single bottom FORS child costs17,392 public calls and8,704 private F addresses; every upper child is a height5 lower-layer tree costing15,423 public calls and1,024 F addresses, including the top row's child. Additional node payload cap278,256 bytes excludes ordinary cache, F/J, raw tables and headers. The same eager quantum outside table and initialization costs remain explicit. These source-relative resources and all eight q columns are independently checked; no numerical probability/capacity row changes.

**COMPUTED — independent checks, not complete kernel verification.** Source-first derivations were saved before reciprocal reading. The peer's clarified successor review449609b4ead61fb1c9946d97867b57ca0bc00625b76af897b51d2e5617bf27cf and third source/resource review773653e00caf9381dfc8f26987b22e41e36378f9f2fa1a8b88f28259c515ffe7 pin ordinary row/bottom behavior, fullimage correlations, event naming, target chronology and counts. Exact finite controls distinguish base selection after the function, target resampling and counter-only collisions. This promotion adds zero supporting or full-source/game kernel declarations; the previous40 supporting declarations remain intact.

**OPEN — standard challenge and security verdict.** Matching the different-base predicate does not identify this interface with published shared-seed S-TCR: S and outside functions are available before C registration, and own-row function release follows. Conventional equivalence, efficient coherent outside realization and actual level/category/capacity still require separate evidence. The complete reviewed direct RO/QROM formulas and old probability tables are unchanged; no implementation, parameter, paper or timing change is made.
'''
write('TYPE7-REDUCTION-PROGRAM.md',header+subject+'\n'+read('chain-pre-adapter/type7/CLARIFICATION.md')+footer)
def once(n,old,new):
    t=read(n);assert t.count(old)==1,(n,old);write(n,t.replace(old,new,1))
def append(n,t):write(n,read(n).rstrip()+'\n\n'+t.strip()+'\n')
append('PROOF.md','''
## 13. Acceptance-selected canonical type7 row program

**PROVED — independently reviewed source-relative interface.** TYPE7-REDUCTION-PROGRAM.md registers the fixed genuine child C before its own type7 restriction Row is sampled. The challenger retains one ordinary full256 function, returns its first accepted32-bit counter and full target word, or bottom on finite exhaustion. B runs the source pre-key/setup/signing/final phases with that same Row/outside function and memoizes only the supplied canonical target. Earlier rejections, lower limbs, off-base/off-length responses and public-cache counters remain correlated exactly. Canonical child construction uses no type7 input, so registration is not circular.

**PROVED — event and partiality.** Original D7_base_final remains a final reached honestly exposed successful row, different child V*!=C and equal complete128-bit digit digest. The larger optional classical-query event is named D7_base_public; a primitive collision found early may increase B's success but does not remove the original exposure restriction. The unflagged simulation has source law, while actual extraction preserves only the source prefix until stopping. Selected-row bottom gives B-local failure and zero selected-event mass, not an added source abort or normalization on global completion. No unknown value, coherent query-history test or prefix blinding is needed.

**PROVED / COMPUTED — exact finite loss/resources.** The2,269,959,421,952 WOTS rows fit a fixed42-bit selector; dummy indices fail. Pr_HJ[Win AND D7_base_final | S!=0]<=2^42 Pr[B_ROW_quantum wins]. B has at most Q_q coherent selected calls plus one final classical call, or Q_H+1 in the classical program. Target preprocessing<=2^32 own-function calls is separately charged. One child cone costs at most17,392 public hashes and8,704 F labels; the top row certifies a lower height5 child, so no height21 preparatory tree is required. Complete source/private/table/time/node envelopes and all eight q resource columns are in the artifact. Full256 replies are retained despite the128-bit collision predicate. Seed-zero is paid only once outside the conditional component union.

**OPEN — ordinary-family identification and capacity.** This acceptance-row/oracle interface is not silently called standard S-TCR for a shared-seed SHA family. Its chronology, allowed side functions and finite first-selection target still need exact equivalence. The program does not tighten the direct D7 term, replace any numerical table, certify a security level/category or supply efficient coherent outside evaluation. It closes the finite relative challenge-program sub-obligation, not those remaining gates.
''')
once('OPEN.md','Next supply the acceptance-selected type7 challenge program, a justified efficient outside simulator, or the still-missing standard shared-seed primitive identification.','The acceptance-selected type7 challenge program is now supplied by TYPE7-REDUCTION-PROGRAM.md. Next supply a justified efficient outside simulator or the still-missing standard shared-seed primitive identification.')
once('OPEN.md','Canonical type7\'s C-before-own-restriction acceptance-selected row program, efficient quantum outside realization and conventional identification remain original open sub-obligations; no level/category/capacity is established.','Canonical type7\'s C-before-own-restriction acceptance-selected row program is now closed within its finite RO/QROM-relative interface. Efficient quantum outside realization and conventional identification remain original open sub-obligations; no level/category/capacity is established.')
append('OPEN.md','''
**PROVED / COMPUTED — canonical-row program scoped closure.** Section13 registers C before Row, preserves its ordinary first-accepted finite-counter law and bottom mass, and extracts changed-base collisions from final classical verification with2^42 selector loss and counted challenge preprocessing. Original D7_base_final and the larger optional D7_base_public are distinct. B-local missing-target failure is not a source failure at an unrequested row. All source/private/graph/PRE/type7 finite relative program sketches are now supplied; conventional equivalence, efficient quantum outside realization and adequate level/category/capacity still require evidence. The old direct formulas are unchanged.
''')
append('TERM-TABLE.md','''
**PROVED / COMPUTED — type7 challenge supplement.** At every requested q, TYPE7-REDUCTION-PROGRAM.md has loss2^42 for the final changed-child event, Q adversarial selected calls plus one final classical call, separate2^32 challenge row preprocessing and17,392-public/8,704-F child preparation caps. Collision equality uses128 bits; the actual challenge function/target retain256 bits. This program is additional interface evidence; the direct classical/QROM D7 probability terms, complete numerics and capacity verdicts remain unchanged. No new kernel declaration is added.
''')
append('REQUIREMENT-MAP.md','''
**PROVED / COMPUTED — Points2.3–2.5/4.2 canonical target-program successor.** Section13 supplies the finite relative acceptance-selected type7 adversary with lawful C-before-ownfunction chronology, first-counter/exhaustion distribution, exact ordinary source prefix, changed-base final extraction and scalar resource loss in classical and coherent-raw games. This closes that program sub-obligation. Matching published S-TCR's different-base predicate alone is not a conventional-family equivalence. All complete probability tables and original level/category/not-established conclusions are preserved.
''')
append('HANDOFF.md','''
**PROVED / COMPUTED — additional progress in this continuation.** TYPE7-REDUCTION-PROGRAM.md is promoted after two independently saved source derivations, reciprocal reviews and third exact row/resource controls. The selected42-bit challenge keeps rejected/accepted/fullword correlations and unconditioned bottom mass. Original FINAL D7_base remains exposed/successful; the broader classical event is named separately. The generic challenge has Q+1 selected calls and up to2^32 target preprocessing, with one child cone17,392-public/8,704-F. Forty supporting checked declarations remain; this promotion adds no source/game/kernel declaration.

**OPEN — next original frontier.** Efficient outside quantum evaluation is being derived in chain-pre-independent/outside-simulator. It must simulate all honest/classifier queries, not only Q_q, provide deterministic field/domain construction and exact bounded-query observable equivalence. That new draft is not yet reviewed or part of current accepted resources. Conventional shared-seed private/graph/PRE/type7 primitive identification and adequate level/category/capacity remain unfinished. The direct source probability formulas, all older numeric cells, source/parent packet and manuscript are unchanged; goal remains active.
''')
append('SECURITY-CRITERION.md','''
**PROVED — canonical-row program preserves the security verdict.** The42-bit selected-row challenge makes target registration, preprocessing and source simulation explicit. It supplies no improved direct D7 bound or AES circuit-resource comparison. The conditional design objective2^40, fixed parameters, constant-success query certificates and complete full-budget vacuity observations remain unchanged. Conventional S-TCR and actual level/category/capacity are not established.
''')
assert all(sha(X/n)==h for n,h in protected_pins.items())
record={'status':'REVIEWED_TYPE7_SUBJECT_PROMOTED_CURRENT_INDEX_REVIEW_PENDING','source_subjects':peer['subjects'],'peer_successor_receipt_sha256':sha(X/'chain-pre-independent/type7/SUCCESSOR-REVIEW.json'),'resource_receipt_sha256':sha(X/'selected-promotion-review/T7-REVIEW.json'),'prior_documents':prior,'current_documents':{n:sha(X/n) for n in docs},'new_artifacts':{'TYPE7-REDUCTION-PROGRAM.md':sha(X/'TYPE7-REDUCTION-PROGRAM.md')},'preserved_artifacts':protected_pins,'new_supporting_declarations':0,'supporting_declarations_total':40,'whole_source_game_checked_declarations':0,'conventional_S_TCR':'OPEN','efficient_outside':'OPEN','level_category':'not established','manuscript_edits':0}
write('TYPE7-PROMOTION.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'promoted':list(record['new_artifacts']),'docs':len(docs),'preserved_artifacts':len(protected),'checked_supporting_declarations':40}))

"""Promote reviewed finite coherent PRE interface; never replace direct bounds."""
from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:(X/n).read_text(encoding='utf8')
write=lambda n,t:(X/n).write_bytes(t.encode('utf8'))
peer=json.loads(read('chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json'))
assert peer['status']=='ACCEPTED_SCOPED_FINITE_QROM_RELATIVE_MANUAL'
assert peer['all_outside_raw_calls_share_fixed_table']
for n,h in peer['subjects'].items():assert sha(X/'chain-pre-adapter'/n)==h,n
algebra=json.loads(read('selected-promotion-review/QPRE-FINAL-REVIEW.json'))
assert algebra['verdict']=='ACCEPT_CORRECTED_QPRE_ALGEBRA_AND_FINITE_RESOURCE_SCOPE'
for n,h in algebra['subject_pins'].items():assert sha(X/n)==h,n
for n,h in algebra['own_pins'].items():assert sha(X/'selected-promotion-review'/n)==h,n
assert algebra['new_supporting_checked_declarations']==7
assert algebra['full_source_game_quantum_checked_declarations']==0
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
B=X/'root-docs-before-quantum-pre';assert not B.exists(),'Single-use promotion; inspect saved state before rerun.'
B.mkdir()
for n in docs:
    assert sha(X/n)==algebra['prior_classical_documents'][n],n
    shutil.copyfile(X/n,B/n)
prior={n:sha(X/n) for n in docs}
protected=['CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md','QUANTUM-COVERAGE-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md','bounds.py','bounds-event-specific.py','SELECTED-GRAPH-REDUCTION.md','CHANGED-CHILD-EXTRACTION.md','CLASSICAL-PRE-REDUCTION.md']
protected_pins={n:sha(X/n) for n in protected}
subject=read('chain-pre-adapter/quantum-INDEPENDENT-DERIVATION.md')
old='**PROVED — manual candidate awaiting independent second reading.**'
assert subject.count(old)==1
subject=subject.replace(old,'**PROVED — manual finite source-model reduction accepted by an independent source-first reader.**',1)
old='**OPEN — independent checking.** The active-CQ factorization, final first-event inclusion and selector block norm need an independent reader and finite controls before promotion. This is a newly saved manual candidate, not wholeRust mechanization.'
assert subject.count(old)==1
subject=subject.replace(old,'**PROVED / COMPUTED — independent checking within the stated finite interface.** The source-first second reader accepts the active-CQ factorization, final first-event inclusion and selector block norm. Independent complete-image channel controls and corrected averaging checks support their separate finite cases. Seven Lean supporting algebra/count declarations check; they do not mechanically verify the source or quantum game.')
header='''# Reviewed finite coherent prefix-blinded PRE reduction

**PROVED / COMPUTED / OPEN — controlling scope.** This promoted source-relative quantum adapter uses a full256-image uniform-input addressed PRE challenge and locally generated outside functions. It preserves quantum queries without inspecting their support; only final classical verification has the known-prefix guard. Independent subject1ceca6be12a9d65e79db7ede3ce5e26bdc31fd3ebf326c245c8351cb6112a9ba and the two clarifications are accepted by the hash-bound source-first SUCCESSOR-REVIEW.json. This is not a conventional shared-seed SHA PRE certificate, a practical simulator or a security-category result. All previous direct RO/QROM scalar bounds and numerical tables are unchanged.

'''
footer='''
## Promotion, error history and actual checked scope

**PROVED / COMPUTED — corrected mixture.** The accepted upper envelope is min(1,(sqrt(2^55 p_PRE)+2Q_q sqrt(D_int/2^128))^2), with D_int=1,016,949,404,336,128. Its expanded cross term is4Q_q sqrt(2^55 D_int p_PRE/2^128). The independent first draft4937b3f45eca9112d0c3bc72246350fa1156279221d30f2155a0e7968a929f4e omitted sqrt(L) in that expansion; it is preserved and rejected. Corrected successord5eb3f4e6d495691c566026bcef72c4de2a614865a0050777475568461330e51 and the other independently saved correct subject agree. No incorrect expression enters the current artifact or calculators.

**PROVED / COMPUTED — honest service and resource precision.** The fixed eager outside table is shared by coherent calls, honest classical hashing, suffix preparation and final verification; public values are not separately resampled. Initial sampling costs256V_b random bits,32V_b data bytes and O(32V_b) writes, plus loop/index operations. The4096-byte allowance covers only extra selected-chain node payload, excluding the table, source/cache/private/message dictionaries, target/selector registers and headers. Uniform S remains the production sampler; fixed nonzero-S statements can be averaged with one external1/N zero-branch charge.

**COMPUTED — mechanical evidence.** QPRE-Averaging.lean checks seven supporting root/Cauchy/padding/cap and exact inventory declarations under the pinned Lean4.28.0/Mathlib environment. Its printed axiom sets are subsets of {propext,Classical.choice,Quot.sound}; no custom axiom, admission or native_decide is used. The source-prefix factorization, common channels and quantum reduction remain manually reviewed mathematical claims. The extension now has40 supporting checked declarations in total, not40 checked security theorems.

**OPEN — original remaining work.** Conventional private/graph/type7/PRE identification, efficient outside-oracle realization and adequate level/category/capacity bounds remain unresolved. A bounded-query2T-wise successor is not applied by this artifact; its specific source/classifier query budget and finite field implementation would need independent proof. Canonical type7's acceptance-selected first row still needs its own explicit challenge program. No manuscript, cryptographic implementation, parameter or timing result changes.
'''
write('QUANTUM-PRE-REDUCTION.md',header+subject+'\n'+read('chain-pre-adapter/quantum-CLARIFICATION.md')+'\n'+read('chain-pre-adapter/quantum-RESOURCE-CLARIFICATION.md')+footer)
def once(n,old,new):
    t=read(n);assert t.count(old)==1,(n,old);write(n,t.replace(old,new,1))
def append(n,t):write(n,read(n).rstrip()+'\n\n'+t.strip()+'\n')
append('PROOF.md','''
## 12. Coherent prefix-blinded hidden-input PRE program

**PROVED — independently reviewed finite QROM-relative adapter.** QUANTUM-PRE-REDUCTION.md removes every genuine point program in the selected WOTS hidden prefix, while the source comparator keeps them. The executable BLIND oracle returns one fixed outside function and the unchanged selected PRE restriction; honest selected-chain endpoints/suffixes use the supplied image. It stops before completed disclosure at or below the cut. Its active physical CQ query block leaves all prefix words independently uniform and unused, without conditioning on source survival or an entire private F map. Distinct literal headers make averaged marked input mass at most1/N, not r/N. Packed query telescoping gives2Q_q/sqrt(N) vector discrepancy for an interior selector, with trivial cap2; WOTS r0 and FORS selectors have zero discrepancy. No coherent query is measured.

**PROVED — common classical final guard.** After A's classical output, final verification stops before replying at any known selected-prefix genuine input and succeeds on a selected fullimage PRE match. On the source trace whose first final hidden input is the selected coordinate, neither an earlier exposure stop nor that guard occurs. The same terminal projector therefore bounds the source event by the BLIND PRE success and the vector discrepancy. Nongenuine prefixes that merge later are included; no absence-of-G assumption is needed.

**PROVED / COMPUTED — exact mixture and counted resources.** For L=2^55, N=2^128 and D_int=1,016,949,404,336,128 interior WOTS coordinates, Pr_HJ[Win AND H_final | S!=0]<=min(1,(sqrt(L p_PRE)+2Q_q sqrt(D_int/N))^2). The cross term contains sqrt(L). The challenge receives Q_q coherent calls and at most one final classical call; the router uses one selected and one outside call per raw query, with inactive plus-state response registers. Honest source calls remain separately counted. The explicit eager outside table costs32V_b storage,256V_b random bits, O(32V_b) initialization and O(V_b(b+32)) gates per coherent lookup; all public classical calls use that same table. This finite implementation is exponential in maximum input length and no PPT/practical claim is made.

**PROVED / COMPUTED / OPEN — precise closure.** The finite coherent PRE program/resource sub-obligation is now closed in its stated interface, independently reviewed. Seven local Lean supporting algebra/count declarations checked with only standard axioms; none verifies the full source/QROM program. The old direct hidden term (2Q_q+sqrt(3017))^2/N is sharper and remains the term in all complete bounds. Conventional shared-seed PRE identification, efficient outside simulation and actual level/category/capacity still need evidence. The selected acceptance-row type7 challenge is the next original program obligation.
''')
once('OPEN.md','CLASSICAL-PRE-REDUCTION.md now supplies the reviewed finite classical hidden-input program/resources; a coherent PRE cut remains OPEN.','CLASSICAL-PRE-REDUCTION.md and QUANTUM-PRE-REDUCTION.md now supply reviewed finite classical and coherent hidden-input programs/resources. Conventional PRE identification and an efficient quantum outside simulator remain OPEN.')
once('OPEN.md','The genuine-hidden-predecessor program is now closed only for the classical stopped-cut RO-relative challenge; its coherent embedding remains OPEN.','The genuine-hidden-predecessor program is now closed for the classical stopped-cut and finite coherent prefix-blinded RO-relative challenges. Conventional identification and useful simulator efficiency remain OPEN.')
once('OPEN.md','Next supply the coherent-cut error/interface lemma or the still-missing standard shared-seed primitive identification.','The coherent-cut error/interface lemma is now supplied by QUANTUM-PRE-REDUCTION.md. Next supply the acceptance-selected type7 challenge program, a justified efficient outside simulator, or the still-missing standard shared-seed primitive identification.')
once('OPEN.md','**PROVED / OPEN — stopped chain lemma and next quantum lemma.** CLASSICAL-PRE-REDUCTION.md closes the classical event-specific unknown-predecessor embedding through a latent joint coupling and stop-before-response rule, with permanent exposure and first-hit selection. It neither assumes uniform marginal independence nor fabricates the predecessor output. The next quantum lemma must implement that output coherently or charge its replacement with an exact O2H source-cut bound, preserving future exposures and full256/raw correlations. A classical first-hit monitor cannot be reused on a coherent query.','**PROVED / OPEN — classical and finite coherent chain lemmas.** CLASSICAL-PRE-REDUCTION.md closes the classical event-specific unknown-predecessor embedding. QUANTUM-PRE-REDUCTION.md supplies the fully prefix-blinded coherent comparator, active-unused-word support proof and exact vector charge; only its final classical extractor checks membership. No unknown predecessor is fabricated and no coherent query history is measured. The remaining efficiency lemma must replace the exponential eager outside table lawfully, counting honest/classifier calls as well as adversarial calls; standard shared-seed challenge identification remains separate.')
append('OPEN.md','''
**PROVED / COMPUTED — finite coherent PRE scoped closure.** The reviewed full-prefix blinding and final-only guard provide a finite QROM-relative program with exact55-bit mixture, interior-count vector error and complete eager-table costs. Seven supporting Lean declarations check only its conditional selector algebra/counts. The old independent draft's missing sqrt(L) expression is preserved/rejected. Existing direct source-model probability tables do not change. Canonical type7's C-before-own-restriction acceptance-selected row program, efficient quantum outside realization and conventional identification remain original open sub-obligations; no level/category/capacity is established.
''')
append('TERM-TABLE.md','''
**PROVED / COMPUTED — coherent PRE program supplement.** At every requested q, QUANTUM-PRE-REDUCTION.md bounds the final hidden contribution by min(1,(sqrt(2^55 p_PRE)+2Q_q sqrt(D_int/N))^2). This is a reduction-interface expression with a challenge advantage, not a new numeric security cell. Selected coherent calls<=Q_q, final Selected<=1 and total coherent handles<=2Q_q; the enormous eager outside-table cost is explicit. All previous direct H/complete probability estimates remain sharper/unchanged. Seven checked selector/count declarations supplement the manual source/QROM proof; conventional PRE, efficiency and category remain OPEN.
''')
append('REQUIREMENT-MAP.md','''
**PROVED / COMPUTED — Point4.2 reduction-program successor.** Section12 supplies the quantum genuine-hidden-input PRE program in a finite addressed-RO fullimage challenge. Its source comparator/prefix invariant, classical final guard, selector average and exact query/time/storage costs are separately reviewed. The simulation error is derived, not a claimed blanket ten-bit loss. The seven supporting Lean declarations do not prove the source-bound QROM game. Canonical type7 challenge-program closure, efficient outside realization, conventional shared-seed primitive identification and actual level/category/capacity remain unfinished.
''')
append('HANDOFF.md','''
**PROVED / COMPUTED — latest continuation is PROGRESS.** The immediately preceding goal turn promoted selected graph/changed-child/classical PRE results. This turn closes the finite coherent PRE program after two independent source-first derivations, a repaired mixture expansion, reciprocal source readings, complete-image channel controls and a third resource/algebra review. Correct expression: min(1,(sqrt(2^55 p_PRE)+2Q_q sqrt(D_int/N))^2), D_int=1,016,949,404,336,128. One-cell blinding fails its support control; the whole prefix is blinded. Coherent query support is never measured. Seven additional supporting Lean declarations bring the extension total to40; zero full-source or quantum-game declarations are newly machine checked.

**OPEN — next original work.** A selected canonical type7 first-accepted-row challenge is independently being derived in the type7 subfolders of the existing agents. It must register the genuine child before its own function, preserve row exhaustion without normalizing global setup success, and extract only a different base at a successful honestly exposed row. A potential2T-wise outside simulator is a separate efficient successor: it must count all honest/classifier calls and implement the finite string domain. Neither that successor nor a conventional fixed-SHA challenge equivalence is assumed here. Source, paper, parameters, complete scalar bounds and existing numeric tables are unchanged; goal remains active.
''')
append('SECURITY-CRITERION.md','''
**PROVED — finite quantum PRE embedding preserves the category verdict.** The new explicit coherent interface reduction pays a55-bit selector mixture and a source-prefix simulation error. It does not improve the direct H term, provide efficient gate/depth resources or certify category1. The actual eager-table initialization and lookup costs are now visible. All previously certified query crossings and full-budget vacuity observations remain unchanged; the original level/category/capacity statement is still not established.
''')
assert all(sha(X/n)==h for n,h in protected_pins.items())
record={'status':'REVIEWED_COHERENT_SUBJECT_PROMOTED_CURRENT_INDEX_REVIEW_PENDING','source_subjects':peer['subjects'],'peer_successor_receipt_sha256':sha(X/'chain-pre-independent/quantum-prefix/SUCCESSOR-REVIEW.json'),'resource_algebra_receipt_sha256':sha(X/'selected-promotion-review/QPRE-FINAL-REVIEW.json'),'prior_documents':prior,'current_documents':{n:sha(X/n) for n in docs},'new_artifacts':{'QUANTUM-PRE-REDUCTION.md':sha(X/'QUANTUM-PRE-REDUCTION.md')},'preserved_artifacts':protected_pins,'source_game_declarations_machine_checked':0,'supporting_declarations_new':7,'supporting_declarations_total':40,'conventional_PRE':'OPEN','efficient_outside':'OPEN','level_category':'not established','manuscript_edits':0}
write('QUANTUM-PRE-PROMOTION.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'promoted':list(record['new_artifacts']),'documents':len(docs),'scalar_artifacts_preserved':len(protected),'checked_supporting_declarations':40}))

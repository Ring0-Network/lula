"""Promote reviewed finite addressed adapter/refined cover; preserve scalar theorems."""
from pathlib import Path
import hashlib,json,shutil

X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pins={
 'selected-graph-challenge/LOCALIZED-FINAL-SUCCESSOR.md':'db2de01bb6dbb5f4f7d6398f12e4763d258c54820a0b3186475cbf8e0c4e14df',
 'selected-graph-challenge/LOCALIZED-SEED-SCOPE-CLARIFICATION.md':'7b95a336d715c093ca3f9831bcad9278d051de628bd875b896afc5a65ed65704',
 'selected-primitive-definitions/D7-BASE-EXTRACTION.md':'bf9af934dc0c16b96e28dedcafb71cfc6590dc17f826ada2562d99f71eaf9776',
 'selected-graph-challenge/D7-BASE-SECOND-READER.md':'a29f246ae1ba8730d2e84a9bc33f8ae8de3eca447ee6654b60b8d943c5562acf',
 'selected-primitive-definitions/LOCALIZED-SECOND-READER.md':'e4de88f8e6126522486455e588456d1665fb0aa3e18cc1469c7900c488babfba',
}
for n,h in pins.items():assert sha(X/n)==h,n
rr=json.loads((X/'selected-graph-resources/REVIEW-RECEIPT.json').read_text(encoding='utf8'))
assert rr['outcome']=='ACCEPT_LOCALIZED_ADDRESSED_RO_ADAPTER_WITH_NONZERO_SEED_SCOPE'
for n,h in rr['subject_pins'].items():assert sha(X/n)==h,n
for n,h in rr['own_pins'].items():assert sha(X/'selected-graph-resources'/n)==h,n
sr=json.loads((X/'selected-promotion-review/SUBJECT-RECEIPT.json').read_text(encoding='utf8'))
assert sr
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
B=X/'root-docs-before-selected-graph'
assert not B.exists(),'This promotion is deliberately single-use; inspect saved state before rerun.'
B.mkdir()
for n in docs:shutil.copyfile(X/n,B/n)
prior={n:sha(X/n) for n in docs}
protected=['CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md','QUANTUM-COVERAGE-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md','bounds.py','bounds-event-specific.py']
protected_pins={n:sha(X/n) for n in protected}
read=lambda n:(X/n).read_text(encoding='utf8')
write=lambda n,t:(X/n).write_bytes(t.encode('utf8'))

eager=read('selected-graph-challenge/INDEPENDENT_DERIVATION.md')
challenge=eager.split('## 2. Exact addressed chosen-target challenge\n',1)[1].split('## 3. Explicit eager adapter',1)[0]
local=read('selected-graph-challenge/LOCALIZED-FINAL-SUCCESSOR.md')
repairs=[
 ('This successor\'s unconditional reduction loss is2^56, not D.','This successor\'s selection loss in the fixed-nonzero-S component game is2^56, not D.'),
 ('Sample the source\'s three uniform seed components, hiding them and j from A;', 'For the component experiment sample S uniformly from the nonzero16-byte strings (or fix nonzero S), and sample K/P independently uniformly, hiding them and j from A;'),
 ('`Pr[B_local wins] = 2^-56 * Pr[source Win AND G_final]`.','`Pr[B_cond wins] = 2^-56 * Pr[source Win AND G_final | S != 0]`.'),
 ('The source full-forgery decomposition uses the displayed conjunction.','The source full-forgery decomposition uses the displayed conditional conjunction and one external seed-zero charge.'),
 ('The local adapter\'s exact routing/marginal remain valid on this branch.','The local router remains correct on this branch, but the routed extractor does not establish the raw-header G_final identity on S=0.'),
 ('the same2^-56 identity applies to `Win AND G_final` as a mathematical QROM adapter identity.','the same2^-56 conditional-nonzero-S identity applies to `Win AND G_final` as a mathematical QROM adapter identity.'),
]
for old,new in repairs:
    assert local.count(old)==1,old
    local=local.replace(old,new,1)
header='''# Reviewed localized addressed-RO chosen-target reduction

**PROVED / COMPUTED / OPEN — promotion and controlling scope.** This successor integrates the accepted localized program with its required nonzero-public-seed correction. All selection identities and the refined selected-handle cap apply in the fixed-nonzero-S component experiment. The full source samples S uniformly; its zero branch is charged once outside the component union. The source, scalar bounds, parameters and numerical tables are unchanged. This is a manually reviewed finite RO-relative chosen-target program, not a conventional fixed-SHA SPR/TCR certificate, not a PPT-family claim and not an implementation attack.

## Exact challenge interface inherited from the reviewed source-first definition

'''
footer='''
## Promotion provenance

**COMPUTED / PROVED — accepted subjects.** The frozen localized source db2de01bb6dbb5f4f7d6398f12e4763d258c54820a0b3186475cbf8e0c4e14df and mandatory scope correction7b95a336d715c093ca3f9831bcad9278d051de628bd875b896afc5a65ed65704 have separate resource/definition reviews. The promoted text applies six explicitly recorded scope repairs, includes the exact addressed challenge definition and preserves the correction in full below. The independent promotion review checks the current text separately. The original eager program remains a historical finite fallback; it does not drive the localized resource contract.

'''
write('SELECTED-GRAPH-REDUCTION.md',header+challenge+'\n'+local+footer+read('selected-graph-challenge/LOCALIZED-SEED-SCOPE-CLARIFICATION.md'))
d7=read('selected-primitive-definitions/D7-BASE-EXTRACTION.md')
old='This successor still requires the reader\'s final hash-bound check.'
assert d7.count(old)==1
d7=d7.replace(old,'The final corrected subject bf9af934dc0c16b96e28dedcafb71cfc6590dc17f826ada2562d99f71eaf9776 is accepted by the hash-bound independent reading a29f246ae1ba8730d2e84a9bc33f8ae8de3eca447ee6654b60b8d943c5562acf; the review is selected-graph-challenge/D7-BASE-SECOND-READER.md.')
write('CHANGED-CHILD-EXTRACTION.md',d7)

def replace_once(n,old,new):
    t=read(n);assert t.count(old)==1,(n,old);write(n,t.replace(old,new,1))
def append(n,t):write(n,read(n).rstrip()+'\n\n'+t.strip()+'\n')
append('PROOF.md','''
## 9. Localized selected-address graph challenge

**PROVED — reviewed explicit finite RO-relative program.** SELECTED-GRAPH-REDUCTION.md commits the genuine selected payload before releasing its independent full256 addressed restriction. A fixed56-bit padded selector chooses among39,339,469,515,522,047 type0–4 domains; dummy ranks fail. For nonzero S, the completed winning final-trace event obeys Pr[B_cond wins]=2^-56 Pr[Win AND G_final | S!=0]. Pre-key access, actual setup, immutable logical-payload response, initiated signing, permanent freshness and absorbing noncompletion are preserved. Coherent raw queries can be routed with one selected and one outside call, without extracting their history; only the final classical verifier witness is used. The quantum statement is a manual finite-adapter identity, not a mechanically verified quantum program.

**COMPUTED — resources without a full-forest materialization.** The largest strict predecessor cone takes8,560,574,462 public calls and33,554,432 private starts. The final five-subtree/17-tree routed extraction takes8,560,653,547 public calls and33,567,232 private starts. Classical selected-handle calls are at most Q_H+2q+4 at nonzero S; total public/private/time/message-length/storage caps are in the artifact. This does not make8.56B hashes practical or establish PPT in a growing-height family. The full-source seed-zero contribution is charged once, not once per adapter. The localized result excludes the broader adversarial-ever-query G event and the S=0 off-route raw alias.

**OPEN — conventional identification.** This selected challenger retains outside raw restrictions, commits an outside-dependent payload and releases its independent missing restriction afterwards. No equivalence with an ordinary single-key SPR/TCR game, real SHA family or category/resource target is claimed. The direct reviewed graph scalar bound remains stronger than this large selection-loss fallback; no calculator or probability table is changed.

## 10. Changed-child extraction at canonical WOTS rows

**PROVED — reviewed pointwise refinement.** CHANGED-CHILD-EXTRACTION.md proves Win subset C_cov union H_final union G_final union D7_base, where D7_base requires a reached honestly exposed successful canonical row, a genuinely changed child V*!=C_A, and equal complete128-bit digests. Genuine exposures are indexed by address, chain and position. Absent G/H, path and chain descent force equal accepted digit vectors; equal target sums then force equality coordinatewise. An unexposed key cannot have all digits terminal because240<480 and2040<4080. If the reconstructed child is already genuine, descent continues regardless of counter equality; no counter-only collision term is required there. The argument applies pointwise to quantum-produced classical signatures.

**PROVED / CITED / OPEN — consequence and boundary.** D7_base is a subset of the earlier D7_full event, so its conservative classical/QROM terms still apply unchanged. The changed-base predicate agrees with the necessary message-change clause in SPHINCS+C DefinitionC.1 (2022/778), but chronology, common parameter, side-oracle, acceptance selection and partiality still need a legal standard challenger embedding. The proof is manually reviewed, not a new machine-checked source theorem. Genuine-hidden-predecessor PRE simulation and conventional primitive identification remain the next original obligations.
''')
replace_once('OPEN.md','Conventional PRF identification, selected-address PRE/SPR/TCR challenge programs and their losses remain OPEN.','Conventional PRF identification and genuine-hidden-predecessor PRE/standard SPR/TCR identification remain OPEN. SELECTED-GRAPH-REDUCTION.md now supplies the reviewed finite RO-relative G_final program and exact selection/query/resource losses.')
replace_once('OPEN.md','The still-requested keyed PRF and addressed PRE/SPR/TCR challenge programs with exact simulator query/time losses remain OPEN.','The keyed PRF adapters and one addressed chosen-target graph adapter now have explicit ROM-relative programs/resources. Their conventional primitive identification and the genuine-hidden-predecessor PRE program remain OPEN.')
replace_once('OPEN.md','Supply one selected-address challenge with a lazy predecessor-graph simulator and an explicit extraction/query/time loss for G or the WOTS genuine-predecessor event; canonical type7 target choice must preserve its self-selected first-accepted row.','The selected-address G_final challenge is supplied with one strict-predecessor cone and routed final extraction; its nonzero-S scope and2^56 loss are reviewed. Next supply a lawful hidden-genuine-chain-input PRE embedding with an explicit source-prefix law and resource loss. Canonical type7 target choice must separately preserve its self-selected first-accepted row.')
append('OPEN.md','''
**PROVED — selected graph and changed-child scoped closures.** PROOF.md Sections9–10 and their promoted artifacts close the finite addressed-RO graph-program/resource sub-obligation and sharpen the final source event cover to D7_base. The localized adapter identity is conditional on S!=0 and only Win AND G_final; the global zero-seed charge stays single. D7_base is restricted to successful honestly exposed rows and is bounded by the old event. These are not conventional SHA PRE/SPR/TCR, full-source machine checks or level/category certificates.

**OPEN — smallest remaining chain lemma.** Embed a uniform hidden-input PRE challenge at a genuine chain coordinate without returning or programming its unknown predecessor output to the adversary. A simulator must prove equality or a charged relation on the stopped source prefixes that reach that coordinate, account for earlier exposure/first-hit selection and preserve full256 raw responses, aliases and partiality. Uniform marginal distribution alone is insufficient. A classical stopped-prefix program does not automatically handle coherent quantum queries.
''')
replace_once('TERM-TABLE.md','| Quantitative Merkle/FORS-root challenge embedding | OPEN | OPEN | OPEN |','| Merkle/FORS-root selected addressed-RO final-event adapter | PROVED manual: loss2^56, nonzero S, explicit resources; conventional SPR/TCR OPEN | Same scoped adapter | Same scoped adapter |')
append('TERM-TABLE.md','''
**PROVED / COMPUTED — selected-address and changed-child successor.** The exact finite G_final adapter has loss2^56 for every requested q, selected classical cap Q_H+2q+4, one source-relative predecessor cone and one routed extraction. Its full public/private/time/storage cost is independent of a full2^41-instance forest materialization but includes actual setup/signing costs. D7_base changes only the pointwise cover and is a subset of the previously bounded D7_full event. Thus all existing numeric cells and the complete reviewed formulas are unchanged. Conventional PRE/SPR/TCR/private PRF identification and level/category/capacity remain OPEN.
''')
replace_once('REQUIREMENT-MAP.md','| 2.4: numerical node-count SPR/TCR embedding | OPEN | Efficient honest-graph simulation/selected target challenge must be supplied. graph-targets/ explores a distinct classical statistical DAG route; no premature node multiplier. |','| 2.4: numerical node-count SPR/TCR embedding | PROVED finite addressed-RO G_final adapter/resources; conventional identification OPEN | SELECTED-GRAPH-REDUCTION.md: target-before-own-restriction,56-bit padded selector, conditional S!=0 loss2^56, localized genuine cone and final route; no naive node multiplier. Ordinary single-key SPR/TCR identification remains unproved. |')
append('REQUIREMENT-MAP.md','''
**PROVED / COMPUTED — reviewed graph/extraction successor.** Sections9–10 give the required G_final addressed-challenge program and its exact finite resource losses, plus an exhaustive changed-child cover. They preserve original signing/verification, public payload, pre-key phase and partiality. The necessary base-message inequality for published S-TCR is now present; an entire primitive-game equivalence is still OPEN. The genuine hidden-predecessor PRE adapter, useful parameter-family efficiency and actual level/category target remain original unfinished work. Extra compiler/channel mechanization remains optional assurance.
''')
append('HANDOFF.md','''
**PROVED / COMPUTED — latest proof continuation is PROGRESS.** The preceding response completed a separate manuscript genre recheck and made no proof change. This continuation promotes two already independently derived/reviewed mathematical subjects: the localized addressed graph target program with its required nonzero-S clarification, and the changed-child D7 extraction. The selector loss is2^56, selected classical calls at most Q_H+2q+4; the final graph event is Win AND G_final, not an ever-query/coherent transcript. The complete source formulas, calculators,48 result cells,32 resource crossings,33 checked supporting declarations, frozen165 files and crypto/publication pins are preserved.

**OPEN — next original frontier.** Classical stopped hidden-chain PRE embedding is being independently derived in chain-pre-adapter and chain-pre-independent. The unknown challenge input is also a predecessor's genuine output; a proposed simulator must not program or reveal it without a lawful source-prefix argument. Coherent-query handling is separate. Standard private/graph/type7 primitive identification, adequate resource/category bounds and certified signing capacity remain unfinished. No source attack, benchmark, manuscript edit, install or upload is part of this continuation.
''')
append('SECURITY-CRITERION.md','''
**PROVED — new graph/extraction results preserve the criterion.** The selected-address adapter closes an explicit finite RO-relative program/resource obligation; D7_base refines an existing pointwise event cover. Neither tightens the complete scalar probability formula nor supplies an AES gate/depth comparison. The32 previously certified query crossings and all full-budget vacuity observations remain unchanged. The original level/category/capacity verdict remains not established.
''')
assert all(sha(X/n)==h for n,h in protected_pins.items())
record={'status':'PROMOTED_REVIEWED_SUBJECTS_CURRENT_INDEX_REVIEW_PENDING', 'subject_pins':pins,'localized_scope_repairs':repairs,'prior_documents':prior,'current_documents':{n:sha(X/n) for n in docs},'new_artifacts':{n:sha(X/n) for n in ['SELECTED-GRAPH-REDUCTION.md','CHANGED-CHILD-EXTRACTION.md']},'preserved_scalar_artifacts':protected_pins,'resource_review_receipt_sha256':sha(X/'selected-graph-resources/REVIEW-RECEIPT.json'),'initial_promotion_subject_review_sha256':sha(X/'selected-promotion-review/SUBJECT-RECEIPT.json'),'level_category':'not established','manuscript_edits':0}
write('SELECTED-GRAPH-PROMOTION.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'promoted':list(record['new_artifacts']),'docs':len(docs),'scalar_artifacts_preserved':len(protected)}))

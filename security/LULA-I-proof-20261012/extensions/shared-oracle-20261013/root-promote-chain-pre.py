"""Promote scoped classical stopped-cut PRE program, never a category claim."""
from pathlib import Path
import hashlib,json,shutil
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:(X/n).read_text(encoding='utf8')
write=lambda n,t:(X/n).write_bytes(t.encode('utf8'))
receipt=json.loads(read('chain-pre-independent/COMBINED-REVIEW.json'))
assert receipt['status']=='ACCEPTED_SCOPED_CLASSICAL_RO_RELATIVE_MANUAL'
assert not receipt['numeric_bounds_changed'] and not receipt['manuscript_changed']
for n,h in receipt['subjects'].items():assert sha(X/n)==h,n
for group in ('independent_before_peer','review'):
    for n,h in receipt[group].items():assert sha(X/'chain-pre-independent'/n)==h,n
assert sha(X/'chain-pre-adapter/PROVENANCE.json')=='b87d89348a7e3720ac35cdef05db3fb69bce6845b23323b7f8c856b8112098b1'
assert sha(X/'chain-pre-independent/COMBINED-REVIEW.json')=='35e2d8722c70409cf762f447a883b8cf5c762a4eee58da32f510e64ae62604f4'
docs=['PROOF.md','OPEN.md','TERM-TABLE.md','REQUIREMENT-MAP.md','HANDOFF.md','SECURITY-CRITERION.md']
B=X/'root-docs-before-chain-pre';assert not B.exists(),'Single-use promotion; inspect saved state before rerun.'
B.mkdir()
for n in docs:shutil.copyfile(X/n,B/n)
prior={n:sha(X/n) for n in docs}
protected=['CLASSICAL-RO-THEOREM.md','QUANTUM-RO-THEOREM.md','QUANTUM-COVERAGE-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md','bounds.py','bounds-event-specific.py','SELECTED-GRAPH-REDUCTION.md','CHANGED-CHILD-EXTRACTION.md']
protected_pins={n:sha(X/n) for n in protected}
wots=read('chain-pre-adapter/INDEPENDENT_DERIVATION.md')
old='**PROVED — manual, independent first derivation; awaiting a second reader.**'
assert wots.count(old)==1
wots=wots.replace(old,'**PROVED — manual source-relative derivation, accepted by an independent source-first second reader.**',1)
header='''# Reviewed classical first-hidden-hit PRE reduction

**PROVED / COMPUTED / OPEN — controlling scope.** This promoted text combines the corrected WOTS stopped-cut program61a8c1d673008b83ba61887d762ad0e51501de039ef870b8b5a43eae7b73e0fa with the localized real-FORS extension2026eba89ac1e884785e9c38b09c9bb347d7efd35f99cc534b988db1c71d1c0b. The combined first-event bound has a fixed55-bit padded selector and covers the union of genuine currently-hidden WOTS/FORS inputs in the ordinary classical HJ game. It is a finite RO-relative uniform-input PRE reduction with an exact full256-image win predicate; it is not a conventional SHA or coherent QROM primitive certificate. The challenger supplies only the selected function and image. Outside restrictions are simulated locally; an externally fixed opaque Raw_out is not an interchangeable interface.

'''
footer='''
## Accepted subjects, controls and remaining frontier

**COMPUTED / PROVED — review.** chain-pre-independent/COMBINED-REVIEW.json35e2d8722c70409cf762f447a883b8cf5c762a4eee58da32f510e64ae62604f4 pins the two subjects and independent WOTS/FORS derivations saved before reading each peer candidate. The first WOTS draft remains preserved. The source game is not normalized on successful setup: setup/signature noncompletion is absorbing and nonwinning. The union loss is2^55, not the WOTS-only2^50 loss. Both branches use at most Q_H+1 selected calls and254 extra public hashes; their source service/byte/time/storage costs remain explicit. The4096-byte node allowance is extra selected-chain data, not a claim that total simulator memory is4096 bytes.

**COMPUTED — finite controls, not source/kernel verification.** Each independent stopped-cut control enumerates512 complete-limb worlds and six adaptive query/disclosure policies. Positive source/ghost marginal checks and the failure of an independently fabricated predecessor discriminate the intended coupling. Full-image and truncated-image PRE experiments are kept distinct; this promotion uses the full-image predicate. No new machine-checked source declaration is claimed by this manual proof.

**OPEN — exact next lemma.** Standard shared-seed keyed PRE identification and an adequate resource/category bound remain unproved. For a coherent interior cut, supply a lawful oracle simulation or an exact O2H error for the inaccessible predecessor output; the classical stop cannot be applied to quantum queries by measuring their support. A prefix-image/lower-limb variant is an unpromoted proposal and does not alter this challenge. The accepted direct classical/QROM H terms and all complete numeric tables remain unchanged.
'''
write('CLASSICAL-PRE-REDUCTION.md',header+wots+'\n'+read('chain-pre-adapter/FORS-LOCALIZED-SUCCESSOR.md')+footer)
def once(n,old,new):
    t=read(n);assert t.count(old)==1,(n,old);write(n,t.replace(old,new,1))
def append(n,t):write(n,read(n).rstrip()+'\n\n'+t.strip()+'\n')
append('PROOF.md','''
## 11. Classical stopped hidden-input PRE program

**PROVED — reviewed first-event embedding.** CLASSICAL-PRE-REDUCTION.md supplies an explicit B_PRE for the ordinary joint-private HJ experiment at nonzero S. A full256 selected random-function PRE challenge hides a uniform16-byte X and gives its full image Y. At an interior WOTS cut, the genuine predecessor's latent full response is `(X,independent lower limb)`. The executable reduction never fabricates this unknown word: it stops before its public response and uses the known image prefix to reconstruct the chain's suffix and endpoint internally. An honest completed signature that would disclose X also stops before its response. On the source prefix whose first hidden hit has the selected coordinate, neither stop has occurred. That query yields a full-image PRE answer. An r=0 WOTS or real-FORS cut similarly keeps the selected ideal-F prefix opaque and uses its known public image. All normal source metadata, public payload, pre-key phases, partiality and byte correlations are preserved on the coupled surviving prefixes.

**PROVED / COMPUTED — exact loss and resources.** There are1,089,588,072,284,160 WOTS nonterminal coordinates and19,140,298,416,324,608 real FORS secret coordinates. Fixed55-bit padding gives Pr_HJ[H | S!=0]<=2^55 Pr[B_PRE wins]. This is an inequality, since other preimages can also produce reduction wins. The WOTS-only program has a separate2^50 loss. Both localized branches use at most Q_H+1 selected calls,254 extra ordinary hashes and4096 extra node bytes, plus the already charged source setup/sign/private/memo/message storage. No whole hidden forest is generated. A skip-on-S=0 variant avoids nonzero-seed rejection sampling; composition still charges the original zero branch once. H_final is covered by this broader classical first-event bound. The direct reviewed H probability estimate is sharper and still drives every calculator/table.

**OPEN — classical scope is not quantum or conventional certification.** The challenge supplies a selected addressed random restriction, with outside functions locally simulated; it is not the previous externally fixed Raw_out challenge. A conventional shared-seed SHA PRE identification is not supplied. Checking and stopping a coherent query at the predecessor would change that query, so the classical program does not close a QROM PRE embedding. The existing complete finite-QROM theorem is independently established by its direct hidden-event lemma and remains unchanged. No level/category/capacity statement, parameter repair or implemented attack follows.
''')
once('OPEN.md','Conventional PRF identification and genuine-hidden-predecessor PRE/standard SPR/TCR identification remain OPEN. SELECTED-GRAPH-REDUCTION.md now supplies the reviewed finite RO-relative G_final program and exact selection/query/resource losses.','Conventional private PRF and shared-seed PRE/SPR/TCR identification remain OPEN. CLASSICAL-PRE-REDUCTION.md now supplies the reviewed finite classical hidden-input program/resources; a coherent PRE cut remains OPEN. SELECTED-GRAPH-REDUCTION.md supplies the finite RO-relative G_final program and exact selection/query/resource losses.')
once('OPEN.md','Their conventional primitive identification and the genuine-hidden-predecessor PRE program remain OPEN.','Their conventional primitive identification remains OPEN. The genuine-hidden-predecessor program is now closed only for the classical stopped-cut RO-relative challenge; its coherent embedding remains OPEN.')
once('OPEN.md','Next supply a lawful hidden-genuine-chain-input PRE embedding with an explicit source-prefix law and resource loss.','The classical hidden-genuine-chain-input PRE embedding now has a reviewed stopped-prefix law and exact resource loss. Next supply the coherent-cut error/interface lemma or the still-missing standard shared-seed primitive identification.')
once('OPEN.md','**OPEN — smallest remaining chain lemma.** Embed a uniform hidden-input PRE challenge at a genuine chain coordinate without returning or programming its unknown predecessor output to the adversary. A simulator must prove equality or a charged relation on the stopped source prefixes that reach that coordinate, account for earlier exposure/first-hit selection and preserve full256 raw responses, aliases and partiality. Uniform marginal distribution alone is insufficient. A classical stopped-prefix program does not automatically handle coherent quantum queries.','**PROVED / OPEN — stopped chain lemma and next quantum lemma.** CLASSICAL-PRE-REDUCTION.md closes the classical event-specific unknown-predecessor embedding through a latent joint coupling and stop-before-response rule, with permanent exposure and first-hit selection. It neither assumes uniform marginal independence nor fabricates the predecessor output. The next quantum lemma must implement that output coherently or charge its replacement with an exact O2H source-cut bound, preserving future exposures and full256/raw correlations. A classical first-hit monitor cannot be reused on a coherent query.')
append('OPEN.md','''
**PROVED / COMPUTED — classical PRE scoped closure.** The exact full-image addressed-RO PRE program covers H_W and real-FORS hidden inputs at nonzero S with2^55 padded loss, Q_H+1 selected calls and localized extra work. It uses local outside functions rather than reprogramming an opaque externally fixed outside oracle. Two source-first WOTS/FORS derivations and hash-bound final review accept the stopped coupling. Conventional private/graph/type7/PRE identification, coherent PRE cut and adequate level/category/capacity remain OPEN. No existing scalar bound is tightened or replaced.
''')
once('TERM-TABLE.md','| Generic WOTS theorem under SPR alone | PROVED false implication; one-way premise needed | Same countermodel | Same countermodel |','| Generic WOTS theorem under SPR alone | PROVED false implication; classical RO-relative PRE program now supplied, ordinary identification OPEN | Same scope | Same scope |')
append('TERM-TABLE.md','''
**PROVED / COMPUTED — classical PRE program supplement.** For every requested q the combined hidden-input reduction has loss2^55 and selected calls at most Q_H+1, with254 extra hashes and4096 extra node bytes beyond source simulation. It bounds H_final by inclusion in the chronological classical H event and preserves the full-image challenge predicate. This is additional program evidence, not a replacement for the sharper direct H bound or a new numeric cell. Standard PRE and coherent-cut embedding remain OPEN.
''')
once('REQUIREMENT-MAP.md','Exact addressed target/one-way reductions and losses remain necessary.','The localized addressed graph reduction and classical stopped-input PRE program/resources are now supplied. Their ordinary-family identification and coherent PRE embedding remain necessary.')
append('REQUIREMENT-MAP.md','''
**PROVED / COMPUTED — classical one-way program successor.** Section11 supplies the original genuine-hidden-predecessor reduction-program sub-obligation inside the classical HJ RO interface. WOTS and real-FORS first hits have exact padded selection/query/source resource caps, a joint latent predecessor law and atomic disclosure stops. This does not promote weak SPR to sufficient one-wayness or change any source/numeric value. The ordinary keyed PRE/PRF/SPR/TCR interfaces, coherent PRE cut and requested level/category/capacity still require their own evidence.
''')
append('HANDOFF.md','''
**PROVED / COMPUTED — additional progress in this continuation.** CLASSICAL-PRE-REDUCTION.md is now promoted after independent WOTS/FORS derivations and final second reading. The interior-cut problem is resolved classically by never answering its unknown predecessor image before stopping; source equality is established on selected first-hidden-hit prefixes. The combined selector loss is2^55; selected calls Q_H+1, extra preparation254 hashes and extra node payload4096 bytes. The latter excludes the full source/cache/memo/message memory. Direct scalar bounds and category verdicts remain unchanged.

**OPEN — next smallest original work.** A coherent stopped-cut lemma must preserve superpositions without inspecting query support, or pay an explicit source O2H loss for the unknown predecessor cell. Conventional shared-seed private/graph/PRE/type7 challenge identification is still unproved. The known reference finite-QROM winning bound remains valid without that generic embedding. No positive security category, exact signing capacity or smallest parameter repair is inferred from these finite programs. Source/manuscript/frozen parent files remain untouched by proof work.
''')
append('SECURITY-CRITERION.md','''
**PROVED — classical PRE program does not change security-category arithmetic.** The explicit stopped-cut reduction now gives a finite ROM-relative one-way program with2^55 selection loss and counted resources. This large fallback does not improve the direct H bound or complete envelope, and has no automatic coherent or fixed-SHA interpretation. Existing constant-success thresholds, full-budget vacuity and not-established level/category/capacity verdicts remain unchanged.
''')
assert all(sha(X/n)==h for n,h in protected_pins.items())
record={'status':'REVIEWED_SUBJECT_PROMOTED_CURRENT_INDEX_REVIEW_PENDING','subject_pins':receipt['subjects'],'subject_review_sha256':sha(X/'chain-pre-independent/COMBINED-REVIEW.json'),'author_provenance_sha256':sha(X/'chain-pre-adapter/PROVENANCE.json'),'prior_documents':prior,'current_documents':{n:sha(X/n) for n in docs},'promoted_artifacts':{'CLASSICAL-PRE-REDUCTION.md':sha(X/'CLASSICAL-PRE-REDUCTION.md')},'preserved_artifacts':protected_pins,'full256_image_predicate':True,'coherent_cut':'OPEN','conventional_PRE':'OPEN','new_machine_checked_declarations':0,'manuscript_edits':0}
write('CLASSICAL-PRE-PROMOTION.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'promoted':list(record['promoted_artifacts']),'documents':len(docs),'unchanged_artifacts':len(protected)}))

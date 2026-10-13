"""Integrate accepted private/hidden event lemmas without promoting coverage."""
from pathlib import Path
import hashlib
import json

X = Path(__file__).resolve().parent
backup = X / 'root-docs-before-quantum-update'
backup.mkdir(exist_ok=True)
names = ['PROOF.md', 'OPEN.md', 'TERM-TABLE.md', 'REQUIREMENT-MAP.md', 'HANDOFF.md', 'VALIDATION.json']
for name in names:
    target = backup / name
    if not target.exists():
        target.write_bytes((X/name).read_bytes())
(backup/'SHA256SUMS.json').write_text(json.dumps({name:hashlib.sha256((backup/name).read_bytes()).hexdigest() for name in names},indent=2)+'\n',encoding='utf8')

def paragraph_replace(s, start, replacement):
    assert s.count(start)==1, start
    a=s.index(start)
    b=s.find('\n\n',a)
    return s[:a]+replacement+s[b:]

p=X/'PROOF.md'
s=p.read_text(encoding='utf8')
s=paragraph_replace(s,'**OPEN — complete quantum composition.**', '**OPEN — efficient simulation and remaining quantum coverage.** The graph and canonical-target search reductions use potentially exponential independent advice circuits. They do not supply an efficient standard-model embedding. Reviewed source-specific quantum private replacement and dynamic hidden disclosure are now supplied below. Quantum FORS multi-call coverage and the full common-game quantum union still require review; classical scalar guesses cannot be substituted for superposition queries.')
added=r'''## 4d. Quantum joint private-input replacement

**PROVED — manually reviewed finite-QROM hop.** `quantum-private-frontier/DERIVATION.md` and the independently source-derived `quantum-private-second-reader/REVIEW.md` supply a full256 coupling on the disjoint private families. In the continued ideal game K/P are unused even by the quantum state. A coherent query has averaged private-support mass at most 1/N and purified local norm difference at most 2/sqrt(N). Classical, dephased honest services contribute at most two P nominations per initiated call and two at final verification. CPTP contraction evaluates local discrepancies on IDEAL prefixes. For fixed nonzero S,

    delta_private_Q <= min(1, 2Q_q/sqrt(N) + (2q+2)/N).

**PROVED — seed and interface.** Averaging uniform S adds at most 1/N once. The standalone unconditional expression has 2q+3 instead of 2q+2. Coherent signing, private state disclosure, timing, corruption and efficient reduction are excluded. At Q_q=2^64 the sufficient distance bound caps at one; this is not a forgery or a category statement.

## 4e. Dynamic quantum hidden-input final event

**PROVED — manually reviewed twice.** `DYNAMIC-QUANTUM-HIDDEN-THEOREM.md` retains the immutable draft checked by `quantum-hidden-second-reader/SECOND_READER.md` and `quantum-hidden-frontier/SECOND_READER_OF_ROOT.md`. Its time-dependent ghost masks still-hidden genuine points and overlays their full images after completed disclosure. WOTS disclosure closes the entire forward suffix by coordinate labels. Remaining coordinates are independent of retained ghost quantum memory; no survival conditioning or retroactive memory overwrite is used. Both honest services use the same private graph. Packing their common dilations between Q_q queries gives purified vector gap at most 2Q_q/sqrt(N).

**PROVED — common stopped examiner.** The final classical verifier stops before its first genuine, still-hidden input. Prior replies agree, so this is a common terminal channel. An unflagged ghost trace supplies at most 3017 nominations: 17 FORS plus 4*(32*15-240) lower-chain plus (16*255-2040) top-chain calls. Its probability is at most 3017/N. The square-root success inequality proves, for fixed nonzero S,

    Pr_HJ[H_final] <= min(1, (2Q_q+sqrt(3017))^2/N).

**OPEN — scope.** This is an observable final event in ordinary HJ, not a measured history of quantum hits, a complete EUF bound, efficient PRE reduction or checked Rust refinement. The full-secret graph used in other event proofs is not fed to this hidden-value game.

## 4f. The requested SPR-only WOTS premise

**PROVED — generic assumption implication refuted.** `SPR-ONLY-COUNTEREXAMPLE.md` uses an injective identity chain family with zero second-preimage advantage and a public inverse. All positions expose the same chain start; distinct fixed-sum digit vectors share identical signing blocks and endpoints. Four algebraic declarations check in `root-formal/SPRSeparation.lean`, with a zero-exit receipt. This is not an actual SHA-256/LULA I forgery. A generic WOTS theorem needs a genuine-predecessor one-way assumption; the separate RO theorem supplies a hidden-input event instead.

'''
assert '## 4d.' not in s
s=s.replace('## 5. Composition, rollback and quantum verdict',added+'## 5. Composition, rollback and quantum verdict')
s=paragraph_replace(s,'**OPEN — full quantum.**','**OPEN — full quantum.** Four quantum components now have reviewed finite-query bounds: joint private replacement, dynamic hidden final input, graph target and canonical type7 target. `QUANTUM-COVERAGE-DRAFT.md` proposes the missing sequential FORS bridge, including guarded nonce masking, full-row adaptive reprogramming and separate final inner/outer searches. Its source/AR gates and common-game composition remain under independent review. Quantum totals remain null. Plain Grover interpretation alone supplies no category certificate; K remains unavailable and no global install or private upload was performed.')
s=s.replace('Dynamic hidden-value disclosure and joint-private quantum replacement are current separate lanes.','The accepted dynamic hidden-value and private-input lemmas are separate source-game branches; the remaining coverage/composition gate stays open.')
p.write_text(s,encoding='utf8')

open_text='''# Remaining proof frontier

**PROVED — complete classical RO theorem.** `CLASSICAL-RO-THEOREM.md` supplies the reviewed C/H/G/D7 partition and common ordinary HJ projection, exact source-call caps and single seed-zero charge. The numerical table supplies all eight q values. This is a manual finite query-game result for partial atomic honest-cache interfaces, not fixed-SHA or standard-model certification.

**PROVED — accepted quantum components.** The independently reviewed private hop is min(1,2Q_q/2^64+(2q+2)/2^128) on fixed nonzero S. The dynamic hidden final event is min(1,(2Q_q+sqrt(3017))^2/2^128), reviewed twice. Graph and type7 final target events have bounds min(1,8(Q_q+3218)^2/2^128) and min(1,8(Q_q+6)^2/2^128). These statements project to the same ordinary HJ marginal; their separate advice views cannot be merged.

**OPEN 1 — sequential quantum FORS source bridge.** Smallest remaining gate: validate the global nonce-overlay invariant after guarded classical source services and instantiate adaptive full-row reprogramming with every preceding honest row read counted. Then verify the resulting padded exposure templates and final inner/outer search projections. `QUANTUM-COVERAGE-DRAFT.md` remains an immutable candidate; three source-first reviews are in progress. Selected BASE responses need not be conditionally uniform after quantum search; the underlying table is independently sampled. A failed gate leaves the total null.

**OPEN 2 — full common-game quantum union.** After coverage is established, apply the source's classical final-verifier C/H/G/D7 partition to a quantum-produced classical forgery, project each event to ordinary HJ and charge the private hop and uniform seed-zero branch once. None of the ghost comparison games is substituted into the structural partition.

**OPEN 3 — level/category and capacity certification.** The current classical bound caps at one at Q_H=2^128; the quantum private-hop bound also caps at one at Q_q=2^64. Those upper-bound failures are not attacks. A tighter sufficient bound and an explicit work/resource-to-category criterion are needed before declaring a certified q_max. The FORS per-candidate exponents alone do not establish full signer security.

**OPEN 4 — efficient generic embeddings and source refinement.** Give exact resource-aware PRF/PRE/SPR/TCR challenge programs, or state the query-model theorem's narrower scope. The graph/advice samplers may be exponential. The source coupling is manually reviewed; Lean/EasyCrypt check component statements, not the Rust program or all quantum channels.

**PROVED — SPR-only requested premise refuted.** Identity is perfectly second-preimage resistant but publicly invertible; its chains expose their starts at every position. `SPR-ONLY-COUNTEREXAMPLE.md` and four checked Lean declarations show why a genuine-predecessor assumption cannot be inferred from SPR alone. This is a generic countermodel, not a LULA I attack.

**OPEN 5 — broader cache and completion APIs.** Arbitrary accepted-counter corruption already refutes universal cache transparency. Persisted benchmark snapshots contain seed material. Public cache bytes require an auxiliary-view simulation. An implemented total abort/retry interface and arbitrary OS completion filters require separate normalization. Honest consistent cache restoration retains the declared zero probability/query transfer loss.

**OPEN — final verdict.** The full goal remains active. The reviewed classical RO theorem and four quantum components are supplied. Full QROM and level/category certification are not yet established; no unresolved term is replaced by zero.
'''
(X/'OPEN.md').write_text(open_text,encoding='utf8')

p=X/'TERM-TABLE.md';s=p.read_text(encoding='utf8')
s=s.replace('| Complete WOTS fixed-child/unexposed certificate bound | OPEN | OPEN | OPEN |','| WOTS fixed-child/unexposed certificate classification in RO | PROVED manual via H/G/D7 | Same reviewed interface | Same reviewed interface |\n| Generic WOTS theorem under SPR alone | PROVED false implication; one-way premise needed | Same countermodel | Same countermodel |')
s += '''\n**PROVED — additional reviewed quantum terms, fixed nonzero S.**\n\n| Component | All requested q values | Evidence |\n|---|---|---|\n| Private-input hop | min(1,2Q_q/2^64+(2q+2)/2^128) | quantum-private-frontier; source-first second reader |\n| Hidden genuine final input | min(1,(2Q_q+sqrt(3017))^2/2^128) | DYNAMIC-QUANTUM-HIDDEN-THEOREM; two source-first readers |\n| Sequential FORS coverage | OPEN candidate, no promoted total | QUANTUM-COVERAGE-DRAFT; source/AR gates under review |\n\n**COMPUTED — numerical status.** Current bounds.py outputs the accepted private/hidden/graph/type7 terms for both recorded budgets. quantum_total remains null pending the coverage and common-game union gates. Seed-zero is not independently added to every fixed-seed component. No exponent is a certified work factor.\n'''
p.write_text(s,encoding='utf8')
p=X/'REQUIREMENT-MAP.md';s=p.read_text(encoding='utf8')
s=s.replace('| 2.3: complete one-time WOTS bound under SPR alone | OPEN; premise insufficient for genuine predecessor branch |','| 2.3: complete one-time WOTS bound under SPR alone | PROVED false as a generic implication; strengthened premise OPEN |')
s=s.replace('Exact addressed target/one-way reductions and losses remain necessary.','SPR-ONLY-COUNTEREXAMPLE.md plus four checked Lean algebraic declarations supply an injective public-inverse countermodel. Exact addressed target/one-way reductions and losses remain necessary.')
s=s.replace('Quantum private replacement, dynamic hidden disclosure, FORS/source selection and complete composition remain OPEN; no blanket ten-bit loss.','Private replacement now has a reviewed finite-QROM distance bound2Q_q/2^64+(2q+2)/N on nonzero S; dynamic hidden final event has reviewed bound(2Q_q+sqrt(3017))^2/N. Sequential FORS/source selection and complete composition remain OPEN; no blanket ten-bit loss.')
p.write_text(s,encoding='utf8')

(X/'HANDOFF.md').write_text('''# Active full-proof goal handoff

**PROVED — accepted progress.** The complete classical RO event theorem remains unchanged. Quantum joint private replacement is now independently accepted with fixed-nonzero-seed distance min(1,2Q_q/2^64+(2q+2)/2^128). Dynamic hidden final-input acquisition is accepted by two source-first readers with bound min(1,(2Q_q+sqrt(3017))^2/2^128). Graph/type7 target events retain their reviewed bounds. Detailed source/channel and finite-control evidence is linked in PROOF.md sections4c–4f.

**PROVED — premise audit.** Four additional Lean declarations check the identity-chain countermodel: perfect second-preimage resistance does not imply one-wayness or WOTS unforgeability. This is not an actual source forgery. Generic embeddings must add the missing genuine-predecessor assumption; the statistical RO theorem already uses its hidden-input event.

**OPEN — live work.** QUANTUM-COVERAGE-DRAFT.md proposes global nonce masking, a guard for the inner/outer alias plane, full-row adaptive reprogramming with all preceding honest row reads counted, and separate final search reductions. Three source-derived reviews assess different gates. Search review accepts its conditional stage4/5 argument but requires a wording correction: underlying BASE functions are sampled independently; adaptively selected outputs need not be uniform. The immutable cut remains preserved. Do not promote a quantum total until source/AR gates and the complete common-HJ union pass.

**COMPUTED — current outputs.** bounds.py retains the independently reviewed classical expression and adds accepted quantum private/hidden fields. Both eight-row budget files were regenerated; quantum_total remains null. A fresh receipt must check their current hashes and formulas. The original reviewed calculator is preserved as bounds-classical-reviewed.py. Historical receipts do not validate new script hashes.

**OPEN — target scope.** No certified classical/quantum q_max, level1/category1 assertion, efficient standard-model embeddings or checked Rust refinement is supplied. Current sufficient bounds are vacuous at the stipulated maximum query budgets; that is not evidence of an attack. Public cache bytes, arbitrary corruption and total abort/retry remain outside honest atomic restoration.

**COMPUTED — boundaries.** All proof work is confined to this extension. The frozen parent packet, both crypto source pins and the separately authorized publication cut are preserved. No paper edit, timing measurement, cache build, global installation or private source upload is authorized by this goal.

**OPEN — handoff verdict.** FULL_GOAL_ACTIVE; FULL_QROM_NOT_YET_ESTABLISHED. The printable level/category statement remains “not established.”
''',encoding='utf8')
print('ACCEPTED_COMPONENTS_INTEGRATED_COVERAGE_TOTAL_OPEN')

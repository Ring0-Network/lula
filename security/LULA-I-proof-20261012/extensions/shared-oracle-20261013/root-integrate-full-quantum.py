"""Integrate the independently accepted finite-QROM theorem; retain open targets."""
from pathlib import Path
import hashlib
import json
X=Path(__file__).resolve().parent
theorem=X/'QUANTUM-RO-THEOREM.md'
assert hashlib.sha256(theorem.read_bytes()).hexdigest()=='94c8f29121760d1a09358257720bb123613084f07a645db9ba9296a43e49a607'
backup=X/'root-docs-before-full-quantum';backup.mkdir(exist_ok=True)
for name in ('PROOF.md','TERM-TABLE.md','OPEN.md','REQUIREMENT-MAP.md','HANDOFF.md','VALIDATION.json'):
    if not (backup/name).exists(): (backup/name).write_bytes((X/name).read_bytes())

def para(s,start,replacement):
    assert s.count(start)==1,start
    a=s.index(start);b=s.find('\n\n',a)
    assert b>=0
    return s[:a]+replacement+s[b:]

p=X/'PROOF.md';s=p.read_text(encoding='utf8')
s=para(s,'**OPEN — overall verdict.**','**OPEN — original level/category objective.** Classical level1, category1 and certified signing capacities are not established. Complete manually reviewed advantage upper bounds now exist for the explicitly specified classical RO and finite-QROM source games. This extension advances the frozen parent obligations without paper/source edits; it does not identify a query-model theorem with fixed-SHA or efficient generic primitive certification.')
s=para(s,'**OPEN — efficient simulation and remaining quantum coverage.**','**OPEN — efficient simulation and category scope.** The separate event search reductions use potentially exponential independent advice circuits. Source-specific private replacement, dynamic hidden disclosure, sequential FORS coverage and the complete common-game quantum union are now manually reviewed. Efficient generic embeddings, checked source refinement and level/category certification remain distinct obligations; no classical guessing argument is substituted for coherent queries.')
s=s.replace('Numerical classical-total fields now contain this reviewed expression; quantum-total fields remain null.','Numerical classical-total fields contain this reviewed expression. Separate quantum-total fields now instantiate the independently accepted finite-QROM theorem below.')
s=s.replace('efficient/full-QROM and level1 certification remain open.','efficient embeddings and level1/category1 certification remain open; the separately reviewed finite-QROM model transfer is given below.')
s=para(s,'**OPEN — full quantum.**','**PROVED — complete finite-QROM source-game bound, independently reviewed twice.** `QUANTUM-RO-THEOREM.md` composes the corrected sequential FORS source bound with the reviewed private/H/G/D7 terms. The accepting final-verifier classification is pathwise on classical outputs, so it applies to quantum-produced signatures. All event inequalities refer to ordinary HJ; event-only advice views are kept separate. q counts initiated requests over all branches; Q_q counts adversarial coherent complete-hash calls. Full256 images, partial noncompletion and one uniform seed-zero charge are retained.')
s=s.replace('**OPEN — printable level/category statement.** “Classical level1 and complete QROM security of this LULA I instantiation are not established. The specified classical RO experiment has a reviewed advantage upper bound; honest-cache rollback preserves that reference signing interface.”','**OPEN — printable level/category statement.** “Classical level1 and quantum category1 security of this LULA I instantiation are not established. The specified atomic honest-cache RO and finite-QROM experiments have independently reviewed winning-probability upper bounds; honest restoration preserves their reference signing interface.”')
s += '''\n## 5a. Explicit complete finite-QROM formula\n\n**PROVED — reviewed source-model theorem.** Put N=2^128, M=N^2-N and let p_F(q) be the exact binomial raw-candidate coverage probability. All following local terms are capped at one.\n\n    delta = min(1,2Q_q/sqrt(N)+(2q+2)/N),\n    D = min(1,q*(sqrt((Q_q+q+1)/M)+(Q_q+q+1)/(2M))),\n    A = min(1,D+8*(Q_q+2)^2*(p_F(q)+1/N+q/N^2)),\n    c = min(1,(2Q_q+sqrt(q))^2/N\n               +(2*(Q_q+2)/sqrt(N)+sqrt(A))^2),\n    h = min(1,(2Q_q+sqrt(3017))^2/N),\n    g = min(1,8*(Q_q+3218)^2/N),\n    d7 = min(1,8*(Q_q+6)^2/N),\n    epsilon_QROM <= min(1,1/N+delta+c+h+g+d7).\n\n**PROVED — review and transfer.** `quantum-composition-numeric/CONDITIONAL-GATE-CLOSED.md` and `quantum-composition-second-reader/SECOND_READER.md` accept the complete common-game theorem and opaque honest-cache transfer. `QUANTUM-COVERAGE-THEOREM.md` resolves fresh-row collision reads and whole-BASE-function sampling before adaptive selection. Honest atomic restoration has zero probability/query transfer loss in this model; private bytes, arbitrary corruption and total abort/retry remain outside it.\n\n**COMPUTED — numerical scope.** bounds.py produces all eight q rows at Q_q=2^32 and2^64. At q=2^40,Q_q=2^32 the conservative total exponent is about31, dominated by private query distance; every Q_q=2^64 total caps at one. These are probability upper-bound exponents, not work-factor levels or attacks. A fresh crosscheck against independently saved240-digit data is required for the regenerated output hashes.\n\n**OPEN — tighter private event bound.** QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md proposes stopping before honest public/private aliases and proving active-prefix domination without normalizing surviving keys. Its candidate success-specific loss is unreviewed and absent from this accepted theorem. It may improve small-query probability bounds but cannot by itself make the current Q_q=2^64 estimate useful.\n'''
p.write_text(s,encoding='utf8')

p=X/'TERM-TABLE.md';s=p.read_text(encoding='utf8')
s=s.replace('| Full QROM total and quantum q_max | OPEN | OPEN | OPEN |','| Complete finite-QROM source-game total | PROVED manual reviewed epsilon_QROM(2^38,Q_q) | PROVED epsilon_QROM(2^40,Q_q) | PROVED epsilon_QROM(2^41,Q_q) |\n| Certified quantum q_max/category1 | OPEN | OPEN | OPEN |')
s=s.replace('| Sequential FORS coverage | OPEN candidate, no promoted total | QUANTUM-COVERAGE-DRAFT; source/AR gates under review |','| Sequential FORS coverage | PROVED reviewed c(q,Q_q) in explicit finite HJ game | QUANTUM-COVERAGE-THEOREM; two source/AR readers and search review |')
s=s.replace('quantum_total remains null pending the coverage and common-game union gates.','quantum_total now reports the independently reviewed finite-QROM common-game union. Level/category and efficient embeddings remain open.')
s=s.replace('Classical level1 and full QROM security are not established. A complete upper bound for the specified classical RO reference experiment is supplied.','Classical level1 and category1 are not established. Complete upper bounds for the specified classical RO and finite-QROM reference experiments are supplied.')
p.write_text(s,encoding='utf8')

p=X/'REQUIREMENT-MAP.md';s=p.read_text(encoding='utf8')
s=s.replace('Sequential FORS/source selection and complete composition remain OPEN; no blanket ten-bit loss.','Sequential FORS/source selection and complete finite-QROM composition are now manually reviewed in QUANTUM-COVERAGE-THEOREM.md and QUANTUM-RO-THEOREM.md. quantum q_max/category1 and efficient embeddings remain OPEN; no blanket ten-bit loss.')
s=s.replace('| 4.2: exact full QROM bound and quantum q_max | PARTIAL / OPEN |','| 4.2: exact full QROM bound and quantum q_max | PROVED finite-model bound / capacity and category OPEN |')
s=s.replace('Generic efficient primitive reductions, actual SHA guarantees, checked Rust refinement and level1 certification remain distinct OPEN requirements.','Generic efficient primitive reductions, actual SHA guarantees, checked Rust refinement and level/category certification remain distinct OPEN requirements.')
s += '''\n**PROVED — finite-QROM gate closed.** Two source-first full-composition readers accept the exact ordinary HJ union and honest-cache transfer; the corrected C source/AR successor is separately accepted. The full quantum expression is now supplied and computed. This closes the finite-model advantage-bound sub-obligation, not the original category/capacity requirement or a mechanical source proof.\n'''
p.write_text(s,encoding='utf8')

(X/'OPEN.md').write_text('''# Remaining proof frontier

**PROVED — both source-game advantage theorems.** CLASSICAL-RO-THEOREM.md and QUANTUM-RO-THEOREM.md now supply independently reviewed full winning-probability upper bounds. The quantum result includes private replacement, sequential FORS coverage, dynamic H, graph G and canonical D7, all projected to ordinary HJ with a single seed-zero charge. Their event-only advice views remain separate. Both apply to the declared atomic, partial, opaque honest-cache model.

**OPEN 1 — improve the conservative private event loss.** The accepted quantum total uses a trace-distance hop that dominates small-query exponents and caps at one for Q_q=2^64. The smallest new lemma in QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md is active-prefix domination: stopped IDEAL unnormalized classical-history blocks are subblocks of the continued key-blind IDEAL prefix at every packed query slot. Prove this without surviving-key normalization, then apply common B/Win-noB projectors. The independent source author lane is investigating it. No accepted numeric field uses that candidate.

**OPEN 2 — certified level/category and capacity.** The complete finite-query bounds alone do not establish level1/category1 or a certified q_max. Every recorded Q_H=2^128 and Q_q=2^64 total caps at one. This is a weakness/vacuity of the sufficient bounds, not an attack. Supply a tighter adequate bound and an explicit resource/success criterion before declaring a capacity; do not equate a FORS per-candidate exponent or negative-log failure bound with a NIST category.

**OPEN 3 — efficient generic embeddings and source refinement.** Exact resource-aware PRF/PRE/SPR/TCR challenge programs and a checked Rust/channel refinement remain missing. Current eager graph/advice simulations can be exponential; manually reviewed source correspondences are not compiler/kernel proofs. Four added Lean identity-chain facts complement the existing13 structural declarations and4 EasyCrypt list lemmas, but none mechanically verifies the whole signature experiment.

**PROVED — requested SPR-only premise refuted in its stated weak interpretation.** Same-tweak fixed-width identity chains have perfect second-preimage uniqueness and trivial preimages, so that premise alone cannot prove WOTS binding. SPR-ONLY-COUNTEREXAMPLE.md and spr-only-second-reader delimit the generic model. It is not an actual SHA/source forgery; stronger cross-tweak/preimage hypotheses can exclude it.

**OPEN 4 — broader cache and completion APIs.** Arbitrary accepted-counter corruption already refutes universal transparency. Persisted benchmark snapshots contain seed material. Public cache bytes require an auxiliary-view simulation; secret recomputability is not public reconstructibility. An implemented total abort/retry interface and arbitrary OS completion filters need separate analysis. Honest consistent restoration retains zero probability/query transfer loss, including retained quantum adversarial memory, within the reviewed interface.

**OPEN — final original-goal verdict.** The full RO/QROM mathematical model bounds are supplied. Level/category certification, exact capacity, efficient primitive embeddings, source refinement and broader cache APIs are not established. The original complete-security goal remains active; no missing obligation is replaced by zero.
''',encoding='utf8')

(X/'HANDOFF.md').write_text('''# Active full-proof goal handoff

**PROVED — accepted this turn.** Complete manually reviewed finite-QROM reference advantage theorem is in QUANTUM-RO-THEOREM.md. Two source-first full-composition readers accept the C/H/G/D7 covering classification for quantum-produced classical forgeries, same ordinary HJ event projections, exact helper budgets, private final handler, single seed-zero and opaque honest-cache transfer. Corrected QUANTUM-COVERAGE-THEOREM.md resolves new-collision POST reads and BASE sampling before adaptive selection without changing equations. Private and dynamic hidden event lemmas have independent reviews. The classical theorem remains unchanged.

**COMPUTED — arithmetic.** bounds.py now returns all eight requested q values with classical and finite-QROM totals at two budgets: Q_H=2^64,Q_q=2^32 and Q_H=2^128,Q_q=2^64. At q=2^40 the first quantum total exponent is approximately31; the second budget has all totals capped1. These are probability upper-bound exponents, not security levels or attacks. Current classical16 rows were rechecked against the previously independent230-digit interval dataset. Current quantum16 rows must match preserved independent240-digit OWN-BOUNDS; use its fresh ROOT-CROSSCHECK receipt, not historical hashes.

**PROVED — premise audit.** Four new checked Lean declarations support a same-tweak SPR-only identity-chain countermodel. It refutes the weak generic assumption implication, not actual SHA/LULA I. Generic WOTS embedding must include genuine-predecessor one-wayness; the RO theorem already uses its hidden-input event.

**OPEN — active next proof lane.** quantum-private-rare-event derives a sharper event-specific private hop from source before reading root QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md. Its smallest lemma is domination of active stopped IDEAL unnormalized classical history blocks by an unflagged key-blind prefix. Avoid normalizing surviving keys, claiming pure-state Loewner domination without classical blocks, or changing the accepted master until independent review. If it passes, compare success-specific B and Win-noB square-root projectors; it still need not certify Q_q=2^64.

**OPEN — original target.** Classical level1/category1, certified capacities, efficient generic primitive embeddings, checked source/channel refinement, public private-cache views, arbitrary corruption and total abort/retry are not established. No smallest parameter repair is licensed by a vacuous sufficient bound. Printable level/category statement remains “not established.”

**COMPUTED — preservation.** Proof writes are confined to this extension. The frozen parent packet, crypto pins and separately authorized publication cut are preserved. No paper edit, timing/cold-cache benchmark, global install or private upload was made. Recheck current VALIDATION.json and preservation receipt before promoting another output cut.

**OPEN — handoff outcome.** REVIEWED_FINITE_RO_AND_QROM_MODEL_BOUNDS; FULL_SECURITY_GOAL_ACTIVE.
''',encoding='utf8')
print('FULL_FINITE_QROM_THEOREM_INTEGRATED_ORIGINAL_GOAL_ACTIVE')

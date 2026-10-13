# Updated term verdicts

**OPEN — overall.** The table retains the full requested terms. Structural classifications and conditional model bounds are not substituted for cryptographic reductions.

| Term | q=2^38 | q=2^40 | q=2^41 |
|---|---|---|---|
| Joint private-input replacement, classical shared RO | PROVED manual: min(1,(Q_H+2^39+3)/2^128) | PROVED manual: min(1,(Q_H+2^41+3)/2^128) | PROVED manual: min(1,(Q_H+2^42+3)/2^128) |
| Separate standard-model secret/randomizer PRF reductions | OPEN | OPEN | OPEN |
| FORS raw-candidate coverage-model exponent | COMPUTED 143.262538581 | COMPUTED 132.563419944 | COMPUTED 125.902530385 |
| Adaptive independent-stream scheduling bridge | PROVED: min(1,(Q_outer+1)p_F(q)), under stream premises | PROVED, same premises | PROVED, same premises |
| Actual joint-ideal adaptive FORS coverage route | PROVED manual: beta+min(1,(Q_H+1)p_F(q)) | PROVED manual, same explicit interface | PROVED manual, same explicit interface |
| FORS unknown-leaf and root event classification | PROVED manual via H/G/C partition | PROVED, same interface | PROVED, same interface |
| Honest different-child WOTS reuse event | PROVED 0 | PROVED 0 | PROVED 0 |
| WOTS fixed-child/unexposed certificate classification in RO | PROVED manual via H/G/D7 | Same reviewed interface | Same reviewed interface |
| Generic WOTS theorem under SPR alone | PROVED false implication; one-way premise needed | Same countermodel | Same countermodel |
| Classical genuine hidden-input event, nonzero seed | PROVED manual reviewed: min(1,(Q_H+3017)/2^128) | PROVED, same interface | PROVED, same interface |
| Classical canonical type7 different-pair target event, nonzero seed | PROVED manual reviewed: min(1,(Q_H+5)/2^128) | PROVED, same interface | PROVED, same interface |
| Addressed Merkle raw collision extraction | PROVED in checked fixed-length model | PROVED in checked model | PROVED in checked model |
| Classical typed0–4 alternative-input hit event | PROVED manual: min(1,(Q_H+3218)/2^128) | PROVED manual, fixed DAG | PROVED manual, fixed DAG |
| Quantitative Merkle/FORS-root challenge embedding | OPEN | OPEN | OPEN |
| H_msg source aliases/free R/counter choices, classical | PROVED manual in reviewed beta/coverage bridge | PROVED, same interface | PROVED, same interface |
| Complete classical RO winning-probability upper bound | PROVED manual: epsilon_RO(2^38,Q_H), theorem below | PROVED manual: epsilon_RO(2^40,Q_H) | PROVED manual: epsilon_RO(2^41,Q_H) |
| Certified level1 signing capacity/q_max | OPEN | OPEN | OPEN |
| Honest-cache rollback probability/query transfer loss | PROVED 0, conditional on reference bound | PROVED 0, conditional | PROVED 0, conditional |
| Complete finite-QROM source-game total | PROVED manual reviewed epsilon_QROM(2^38,Q_q) | PROVED epsilon_QROM(2^40,Q_q) | PROVED epsilon_QROM(2^41,Q_q) |
| Certified quantum q_max/category1 | OPEN | OPEN | OPEN |
| Observable QROM types0–4 final-trace target event, nonzero seed | CITED+PROVED reviewed: min(1,8(Q_q+3218)^2/2^128) | Same event bound, not full EUF | Same event bound, not full EUF |
| Observable QROM type7 final-trace target event, nonzero seed | CITED+PROVED reviewed: min(1,8(Q_q+6)^2/2^128) | Same event bound, not full EUF | Same event bound, not full EUF |

**PROVED — scope of the first row.** q counts initiated signing requests, with one final verification and key-independent opaque handles. A completed-call budget plus one pending call changes +3 to +5. The correct REAL marginal is preserved when the public seed is zero. The proof is a manual statistical coupling supported by a checked fixed-list probability lemma; it is not a checked source-level reduction.

**COMPUTED — budget interpretation.** `root-checks/bounds-QH64/` and `root-checks/bounds-QH128/` reproduce all eight requested q values. At q=2^40 and Q_H=2^64, the accepted complete classical RO upper bound has probability exponent61.404903692. At Q_H=2^128 it is the vacuous bound1. The coverage fresh-stream subterm has exponents68.563419944 and4.563419944 respectively; beta and the other route terms are additional. No probability exponent is relabelled as a work-factor security level. The independent230-digit interval calculator in `classical-composition-numeric/` checks all eight total rows.

**OPEN — printable level/category verdict.** Classical level1 and category1 are not established. Complete upper bounds for the specified classical RO and finite-QROM reference experiments are supplied. It does not certify a signing capacity or justify an actual-scheme parameter repair.

**PROVED — beta definition.** The reviewed classical joint-ideal source bridge uses beta=min(1,(2Q_H+q+2)/2^128+[qQ_H+binom(q,2)+q]/2^256+q(511/512)^(2^32)). Its corrected candidate cap is deterministic Q_H+1. It is a covered-leaf route bound; arbitrary fresh verifying node evidence is not automatically in that route.

**PROVED — complete classical RO theorem.** Put N=2^128 and let p_F(q) be the exact binomial raw-candidate coverage probability. With q initiated calls and Q_H raw adversarial complete-hash calls,

\[
\epsilon_{\rm RO}(q,Q_H)\le\min\{1,(6Q_H+3q+6243)/N
+[qQ_H+\binom q2+q]/N^2+q(511/512)^{2^{32}}+(Q_H+1)p_F(q)\}.
\]

Two independently saved source derivations/reviews accept the partition and probability projections in `CLASSICAL-RO-THEOREM.md`. This game is unconditioned, partial, atomic, honest-cache and classical. The numerical table reports this theorem, not an efficient generic primitive reduction, checked Rust refinement or fixed-SHA certificate.

**PROVED — additional reviewed quantum terms, fixed nonzero S.**

| Component | All requested q values | Evidence |
|---|---|---|
| Private-input hop | min(1,2Q_q/2^64+(2q+2)/2^128) | quantum-private-frontier; source-first second reader |
| Hidden genuine final input | min(1,(2Q_q+sqrt(3017))^2/2^128) | DYNAMIC-QUANTUM-HIDDEN-THEOREM; two source-first readers |
| Sequential FORS coverage | PROVED reviewed c(q,Q_q) in explicit finite HJ game | QUANTUM-COVERAGE-THEOREM; two source/AR readers and search review |

**COMPUTED — numerical status.** Current bounds.py outputs the accepted private/hidden/graph/type7 terms for both recorded budgets. quantum_total now reports the independently reviewed finite-QROM common-game union. Level/category and efficient embeddings remain open. Seed-zero is not independently added to every fixed-seed component. No exponent is a certified work factor.

**PROVED — reviewed private event refinement.** Define e=min(1,c+h+g+d7) and b=min(1,(2q+2)/N). QUANTUM-EVENT-SPECIFIC-THEOREM.md gives epsilon_event=min(1,1/N+[2Q_q/sqrt(N)+sqrt(min(1,b+e))]^2). Taking its minimum with the conservative theorem is valid. This is a winning-event statement, not a general state-distance improvement.

**COMPUTED — refined table.** bounds-event-specific.py and root-checks/refined-Qq32 / refined-Qq64 reproduce all eight q values. The independent96-field/64-exponent crosscheck passes for all16 rows. At Q_q=2^32 the refined source exponents for q=2^40 and2^41 are57.683359869309 and56.873275107725. At Q_q=2^64 every refined total is one. These are capped success-probability upper bounds under displayed budgets; category and capacity remain uncertified.

**PROVED / COMPUTED — query-resource supplement.** PROOF.md Section6 and query-resource-independent/THRESHOLDS.json close the requested no-crossing arithmetic for the supplied tiny-failure estimates and provide32 exact adjacent integer constant-success crossings. The table below concerns probability at most1/2, not security-category bits.

| Initiated signing cap | Classical log2(Q_pass), approximate | Best quantum log2(Q_pass), approximate |
|---:|---:|---:|
| 2^24 | 124.415037499279 | 60.423340767617 |
| 2^30 | 124.415037499279 | 60.423340767617 |
| 2^38 | 124.415031382251 | 60.423336537424 |
| 2^40 | 124.404903734342 | 60.416375433175 |
| 2^41 | 123.638290418704 | 59.998503957389 |
| 2^44 | 97.521203039111 | 47.260537854946 |
| 2^50 | 19.122188486068 | 8.049848549451 |
| 2^64 | 7.988684686772 | 1.584962500721 |

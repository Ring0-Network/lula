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
| Generic WOTS theorem under SPR alone | PROVED false implication; classical RO-relative PRE program now supplied, ordinary identification OPEN | Same scope | Same scope |
| Classical genuine hidden-input event, nonzero seed | PROVED manual reviewed: min(1,(Q_H+3017)/2^128) | PROVED, same interface | PROVED, same interface |
| Classical canonical type7 different-pair target event, nonzero seed | PROVED manual reviewed: min(1,(Q_H+5)/2^128) | PROVED, same interface | PROVED, same interface |
| Addressed Merkle raw collision extraction | PROVED in checked fixed-length model | PROVED in checked model | PROVED in checked model |
| Classical typed0–4 alternative-input hit event | PROVED manual: min(1,(Q_H+3218)/2^128) | PROVED manual, fixed DAG | PROVED manual, fixed DAG |
| Merkle/FORS-root selected addressed-RO final-event adapter | PROVED manual: loss2^56, nonzero S, explicit resources; conventional SPR/TCR OPEN | Same scoped adapter | Same scoped adapter |
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

**PROVED — seed-charge convention.** The first-row private bound, the standalone beta definition above and the standalone types0–4 bound retain their earlier unconditional or deliberately looser allowances: respectively +3, +2 and +3218. They must not be summed as if each were a sharp fixed-nonzero-seed component. The complete theorem below instead uses the separately proved fixed-S!=0 bounds (Q_H+2q+2)/N, beta_0=(2Q_H+q+1)/N+[qQ_H+binom(q,2)+q]/N^2+q(511/512)^(2^32), and (Q_H+3217)/N, together with (Q_H+3017)/N and (Q_H+5)/N. It then pays Pr[S=0]=1/N exactly once. Thus 2+1+3017+3217+5+1=6243. These are the existing `joint_nonzero`, `coverage_beta_nonzero` and graph fields used by bounds.py, not a new bound or numerical revision.

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

**PROVED — public payload and private program successor.** The exact logical top payload is admitted by CACHE-PAYLOAD-THEOREM.md with the SAME classical and quantum sufficient formulas at every requested q. PRIVATE-REDUCTION-PROGRAMS.md supplies explicit classical ROM-relative K/P challenge programs and source-relative resource caps; the sharper joint statistical term still drives bounds.py. Conventional independent-PRF certification and selected-address PRE/SPR/TCR embeddings remain OPEN. No new probability exponent or signing capacity is invented.

**PROVED / COMPUTED — selected-address and changed-child successor.** The exact finite G_final adapter has loss2^56 for every requested q, selected classical cap Q_H+2q+4, one source-relative predecessor cone and one routed extraction. Its full public/private/time/storage cost is independent of a full2^41-instance forest materialization but includes actual setup/signing costs. D7_base changes only the pointwise cover and is a subset of the previously bounded D7_full event. Thus all existing numeric cells and the complete reviewed formulas are unchanged. Conventional PRE/SPR/TCR/private PRF identification and level/category/capacity remain OPEN.

**PROVED / COMPUTED — classical PRE program supplement.** For every requested q the combined hidden-input reduction has loss2^55 and selected calls at most Q_H+1, with254 extra hashes and4096 extra node bytes beyond source simulation. It bounds H_final by inclusion in the chronological classical H event and preserves the full-image challenge predicate. This is additional program evidence, not a replacement for the sharper direct H bound or a new numeric cell. Standard PRE and coherent-cut embedding remain OPEN.

**PROVED / COMPUTED — coherent PRE program supplement.** At every requested q, QUANTUM-PRE-REDUCTION.md bounds the final hidden contribution by min(1,(sqrt(2^55 p_PRE)+2Q_q sqrt(D_int/N))^2). This is a reduction-interface expression with a challenge advantage, not a new numeric security cell. Selected coherent calls<=Q_q, final Selected<=1 and total coherent handles<=2Q_q; the enormous eager outside-table cost is explicit. All previous direct H/complete probability estimates remain sharper/unchanged. Seven checked selector/count declarations supplement the manual source/QROM proof; conventional PRE, efficiency and category remain OPEN.

**PROVED / COMPUTED — type7 challenge supplement.** At every requested q, TYPE7-REDUCTION-PROGRAM.md has loss2^42 for the final changed-child event, Q adversarial selected calls plus one final classical call, separate2^32 challenge row preprocessing and17,392-public/8,704-F child preparation caps. Collision equality uses128 bits; the actual challenge function/target retain256 bits. This program is additional interface evidence; the direct classical/QROM D7 probability terms, complete numerics and capacity verdicts remain unchanged. No new kernel declaration is added.

**PROVED / CITED — efficient bounded-query B-only successor.** OUTSIDE-SIMULATOR-THEOREM.md supplies the deterministic direct binary-tower polynomial family and exact bounded-query replacement for the existing PRE/type7 reductions. All honest source calls are included in T, and initialization, uniform circuit generation, clean reversible evaluation and storage are charged. The complete source probability formulas and old tables remain unchanged. Conventional primitive identification, level/category and certified capacity remain OPEN; no new kernel security theorem is claimed.

**PROVED / ASSUMED — fixed-public-hash canonical collection successor.** STANDARD-CANONICAL-COMPONENT.md gives an independently reviewed source-specific type7 wrapper under the explicitly chosen CF-BS-TCR-collection(h,Prop,2^32) property. Other-tweak collection access computes the genuine child before parameter release. Canonical-first BE32 selection is a legal specialization; equivalence for all accepted-counter policies is not required. Finite bottom and full same-hash correlations are retained. Lower/top fixed predicates yield the unconditional nonzero-seed component 2^42 SuccProp4+2^21 SuccProp8. This is HJ[h], not an equality to the old HJ[O] experiment. All reduction work is charged; quantitative fixed-SHA/collection/full-security bounds remain OPEN.

**PROVED / COMPUTED — limited mechanized addition.** Four independently reexecuted Lean declarations establish only a synthetic counter-policy separation. Cumulative supporting declarations are44, with zero new whole-source/game security declarations. The original scalar theorems, calculators, source and paper are unchanged. Restricted-row QROM and one-query completion candidates remain separate and are not acceptance evidence for this successor.

**PROVED / ASSUMED — ordinary fixed-public-hash private adapters.** PRIVATE-FIXED-H-REDUCTION.md closes the exact source-relative ordinary public-parameter PRF hop interface: pReal_h <= pFJideal_h+Adv(f;B_K)+Adv(g;B_P), with all full public hashes computed by the same h, literal aliases including seed-zero, classical private queries and quantum public computation. Signed gaps/public-parameter averaging and reduction-versus-challenger costs are explicit. Private-family hardness is ASSUMED; no RO expression is substituted for the remaining fixed-hash pFJideal_h. Prefix private assumptions do not certify the lower128 H_msg route bits. The smallest remaining obligation is a fixed-hash full-output/adaptive-selection/public-graph bound.

**PROVED / CITED — restricted linked-global-RO canonical target bound.** RESTRICTED-CANONICAL-QROM.md preserves pretarget other-tweak child computation, first literal BE32 acceptance, full same-function target/outside correlations and bottom mass. The independently reviewed one-query Fourier completion yields U(M)=min(1,8(M+1)^2/2^128), using SPHINCS+C TheoremE.3. A NEW pre-digest stopping extractor has M<=Q; the preserved final-evaluation program still has M<=Q+1. The unconditional source type7 component is at most min(1,(1-1/N)(2^42 tau4+2^21 tau8)U(Q)). All honest runtime/global evaluation costs remain charged separately. This restricted component neither replaces the stronger old direct D7 bound nor changes the old complete probability numerics or certifies fixed SHA/category/capacity. Supporting checked declarations stay44, with zero newly checked whole-source/game declarations.

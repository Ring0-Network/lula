# Canonical collection component under one fixed public hash

**PROVED — independently reviewed manual conditional reduction.** This is a source-specific identification of the type7 changed-base component, not a hardness proof for SHA-256 and not an equality between the fixed-hash and random-oracle source games. Source lib.rs is fixed at ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. The independently saved author's derivation, clarification and peer reviews are retained unchanged. The clarification supersedes overly broad readings of the first candidate's counter-policy discussion.

## 1. Exact primitive instance

**ASSUMED — named security property; PROVED — interface definition.** Fix one PUBLIC full256 implementation h. For every source payload length m define the linked collection

`Th_m(P,T,X) = prefix128 h(P || zero48 || Encode22(T) || X)`.

P is one uniform128-bit public parameter initially hidden from the primitive adversary. T is the literal source address, not an independently sampled key. The chosen property CF-BS-TCR-collection(h,Prop,2^32) has the following oracle: phase1 permits classical collection calls at tweaks disjoint from the eventual target tweak; the adversary registers ONE type7 tweak and C16; the challenger searches the literal20-byte payloads C||BE32(c), c=0,...,2^32-1, and returns the first accepted prefix/counter, or bottom. It then releases P. Phase2 computes the SAME public full h locally and outputs V16,c32. Success requires a nonbottom target, V!=C and prefix equality to that target. No sampling is conditioned on success.

**PROVED.** Once P and the canonical counter are known, the full target is computable using the same public h. All raw source calls use this implementation, including coincident literal inputs. Unknown lower limbs are not filled independently. Time/gates and message bytes of these evaluations are charged. An external opaque QROM interface is a different experiment and requires explicit linkage to full256 Raw access.

## 2. Relation to the published notions

**CITED.** Hülsing–Kudinov, https://eprint.iacr.org/2022/346, Definition7, supplies other-tweak collection access under a hidden parameter. SPHINCS+C, https://eprint.iacr.org/2022/778, DefinitionC.1, specifies special target collision with an acceptance predicate. Its Section5.1 choice r=security parameter belongs to that construction, not a mandatory counter-width condition in the formal C.1 wording.

**PROVED — specialization precision.** Canonical-first counter selection is a legal chosen policy. No universal equivalence to EVERY valid accepted-counter policy is necessary. The hypothesis must nevertheless explicitly name the literal BE32 payloads, first-counter rule and finite bottom branch. Hashing C||BE128(c) is not the same source input. The accepted abstract policy countermodel disproves interchangeability of arbitrary accepted-counter policies, not legality of this canonical specialization.

**CITED / OPEN.** HK22 Section8 states its generic collection-bound extension as a conjecture. This component therefore imports the formal collection interface but does not turn that conjecture, a stand-alone target bound or a different construction's quantitative bound into a proved value for this source instance. The chosen property's actual advantage remains an assumption-parametric quantity.

## 3. Source wrapper and the child chronology

**PROVED.** Work in HJ[h], with independent ideal private maps F/J and the fixed public full h. Choose the selected row before its genuine child. The child's computation uses types0–4 only, disjoint from the selected type7 tweak. It is therefore available through phase1 collection access before P is disclosed. Parameter dependence of C does not by itself make registration impossible.

**PROVED — program.** The reduction samples consistent ideal F/J, computes the genuine child using the permitted collection oracle, registers C, obtains the target and P, and starts source A's pre-key phase while withholding P/pk from A until the source's normal key transition. It then executes the actual source setup/sign/cache-restoration/final-verification interface using the same h. On a selected final exposed-successful changed-base collision it outputs V,c. A selected bottom row produces no winning selected event; it is not a global source abort or a normalized success-conditioned source distribution. The same literal function and ideal private maps are retained throughout.

**PROVED / COMPUTED — fixed predicates and selectors.** Prop4 has32 width4 digits summing240; Prop8 has16 width8 digits summing2040. They are TWO fixed primitive instances. There are2,269,957,324,800 lower rows and2^21 top rows. A42-bit padded lower selector and21-bit top selector give

`Pr_HJ[h][Win AND D7_base_final AND S!=0] <= 2^42 Succ_CF(h,Prop4)(B_lower) + 2^21 Succ_CF(h,Prop8)(B_top)`.

**PROVED.** This is the unconditional nonzero-seed contribution. The single seed-zero mass is paid elsewhere in a complete union. It must not be confused with a fixed-S conditional bound or charged again inside both predicate terms. Valid selectors induce the same unflagged source view; no independently keyed row assumption is used. All source winning fields and the reached, exposed-successful final witness from the accepted changed-child extraction remain present.

## 4. Explicit work and weaker fallback

**COMPUTED / PROVED.** Layer0 child preparation uses at most17,392 collection calls and8,704 distinct F labels. Upper child preparation uses at most15,423 calls and1,024 F labels. The canonical challenge scans at most2^32 full-hash words; this is separately charged. Source setup, q initiated signing jobs, final verification, ideal-map storage and all raw A calls are part of reduction time/gates/global-oracle resources. Source adversarial Q alone is not the complete reduction's evaluation budget. The source-private label cap is min(N_D,8704+2181038080+q U_mode), with J<=q, besides source/challenger storage.

**PROVED — conventional weaker fallback.** Without a target challenge, a successful D7 changed-base event supplies two distinct106-byte words with equal prefix128 h: the genuine child with its canonical counter, and V!=C with the forged counter, under the same seed/address. A simulator can output this ordinary collision for the TRUNCATED function. It needs no row selector, but its work still includes the source execution.

**OPEN.** Truncated-hash collision resistance alone does not yield the requested128-bit classical guarantee. Such a reduction is neither a collision for full SHA-256 nor an actual signature attack. Fixed-hash public PRE/graph/message-hash analysis, private hardness, adequate total security, category and certified capacity remain unestablished. The original complete source RO/QROM scalar theorems are unchanged.

## 5. Formal evidence and its scope

**PROVED / COMPUTED — four supporting synthetic declarations.** CounterPolicy.lean was checked under pinned Lean4.28.0 and independently reexecuted. both_policies_accepted, canonical_policy_collision, later_policy_no_changed_base_collision and no_finite_factor_from_zero_success establish the two-base abstract counter-policy separation. Their axiom sets contain only propext or are empty; no admissions, custom axioms or native_decide occur. This is NOT a kernel proof of LULA's hash function, predicates or source game. Cumulative supporting declarations become44; newly checked complete-source/game security declarations remain zero.

**COMPUTED — acceptance records.** selected-promotion-review/standard-identification/PROVENANCE.json records both independent first saves and peer controls. outside-field-check/standard-component-review/SUBJECT-REVIEW.json independently accepts this fixed-public-hash conditional wrapper, the explicit specialization and the four scoped helpers. The restricted-row QROM and one-query circuit successors are separate new candidates, not relied on here.

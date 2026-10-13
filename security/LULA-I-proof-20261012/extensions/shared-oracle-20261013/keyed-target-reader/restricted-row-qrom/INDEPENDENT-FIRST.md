# Restricted canonical source-row QROM bound: independent first derivation

This derivation is saved before reading any NEW peer proposal for this restricted quantitative lemma. It concerns the exact source-specific wrapper, not arbitrary HK collection security and not fixed SHA-256. Existing keyed-target-reader artifacts and receipts remain unchanged.

## Result and exact assumptions

Let O be one static full256 random oracle on byte strings, P a uniform16-byte seed sampled independently of O, and F/J the already named independent private ideal maps. A selected valid type7 address a is chosen before computing its genuine child C. Before target registration there are ONLY classical type0..4 collection evaluations at hidden P and independent F computations: no raw queries and no type7 collection evaluations. The source child is thereby independent of the entire selected type7 restriction of O. The selected target is the first accepted `C||BE32(c)` for c<2^32, or bottom, under one fixed low/top predicate. After registration P is released and all source-adversary pre-key/raw work occurs using the SAME O, while P/pk remain withheld from A until the ordinary source public-key transition.

**PROVED, information-theoretic query-model lemma:** Define

`U(Q) = min(1, 8*(2*Q+1)^2 / 2^128) = min(1,32*(Q+1/2)^2 / 2^128)`.

For an arbitrary posttarget algorithm making at most Q fullRaw evaluations, including classical queries, the chance of producing a different-base canonical target collision is at most `tau_kind * U(Q)`, where `tau_kind=1-(1-p_kind)^(2^32)` and p_kind is the exact128-prefix acceptance fraction. Dropping tau gives the simpler U(Q). No hidden-parameter reprogramming term is needed in this restricted game: there were no pretarget raw queries and the actual dependent child/target were generated with the same O before A started. This is not a theorem for all accepted-counter collection adversaries.

For the exact HJ source wrapper at P!=0, the sharper charged cap is `Q_eff=Q_A,q+Q_A,c+1`. Q_A,q counts every adversarial coherent fullRaw call over source pre-key and later phases; Q_A,c counts every adversarial classical fullRaw call over both phases. The +1 charges the selected final classical verifier/classifier call. All ordinary honest setup/signing/hash computations and canonical preprocessing are proved outside the changed-base region below. They remain charged as global source/challenger time and oracle resources; they are not discarded from those resources.

Accordingly each selected low/top reduction has unconditioned probability

`Pr[B_kind wins AND P!=0] <= (1-2^-128) * tau_kind * U(Q_eff)`

before selector/dummy factors. The looser `tau_kind*U(Q_eff)` is sufficient if seed-zero is already excluded externally. The source selected-event inequality remains a separate42-bit low /21-bit top selection step. No numerical category, q_max, parameter or existing scalar table is changed here.

## Primary quantitative theorem actually used

SPHINCS+C, IACR2022/778, AppendixE printed page35, DefinitionE.2 and TheoremE.3, text lines1808-1829 in `R2/R2B-joint-constraints/refs/sphincsplusc_2022_778/2022-778.txt`. TheoremE.3 states that a q-query quantum algorithm seeking a1 of a Bernoulli-lambda Boolean random function has success at most `8*(q+1)^2*lambda`. The paper attributes the result to HRS16. I use this directly for lambda=2^-128 and q=2Q, NOT LemmaE.4's broader hidden-key reprogramming argument. Primary PDF SHA256 `1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215`, primary URL https://eprint.iacr.org/2022/778.

The Boolean domain can be the whole160-bit base/counter space even though answers with base=C are ineligible. Unused same-base points are independently sampled Bernoulli points and never matter to a valid output. Thus the theorem's power-of-two domain is preserved without assuming a theorem for a non-power-of-two set.

The theorem is a query bound for arbitrary interquery quantum computation. Conditioning independent auxiliary tables merely fixes those interquery operations/advice; it imposes no computational efficiency claim and no new assumption about a physically efficient implementation of the enormous RO table.

## 1. Joint factorization, not just marginal independence

Write `H(P,a)=P||zero48||a`, length86. The selected changed region is

`D(P,a,C)={H(P,a)||V16||BE32(c): V!=C, c<2^32}`.

Its complement includes ALL other raw strings, selected-header off-length strings, all same-C counter inputs, all other addresses, all other seeds, and unaddressed metadata words. Before any posttarget raw interaction, condition on P,a,F,J, the complete type0..4 collection history and all selected-header-complement values required to compute C. Since those queried bytes have address type0..4, none equals any type7 selected-header word. Hence C is fixed by independent outside data, while all selected20-byte payload words remain an unqueried independent full256 restriction.

Now additionally fix the complete SAME-C counter row and all other side-function values outside D. This fixes target existence, c0, its fullY, every rejected same-C counter value, the untouched later same-C values, and any off-length selected raw values. Because C was fixed without reading a type7 row, disintegration of the product RO law leaves O|D a product of uniform full256 words independent of this entire side information. Conditioning on the target's first acceptance or even on the entire same-C row is lawful: it constrains ONLY complement values. It does not condition on any absence of an adversarial hit.

Let W denote all that side information, including P,a,C,c0,Y, F/J and independent A coins BEFORE A's first raw query. On nonbottom branches the joint state has the form

`rho = sum_w Pr[W=w] |w><w| tensor rho_initial,A(w) tensor RF_D(w)`.

Here RF_D(w) is an independent uniform full256 function on the now fixed changed region. This statement is about the initial JOINT state and function distribution. Conditioning on A's state AFTER its raw queries would generally destroy this independence and is not done. In the actual wrapper A's initial state can be oblivious to part of w; granting all w to a stronger search algorithm only increases its power.

For each fixed w, target y=first16(Y) is known. Its conditional distribution may be concentrated on Prop's accepted subset; this does not matter. Every fresh changed-region output has independent uniform128 prefix, so the mark probability is exactly2^-128 for that PARTICULAR y. Lower128 bits stay part of the same full function.

Since genuine-row trials are independent uniform128 prefixes before any raw interaction, target existence has exact mass tau_kind. No division by tau is used. Bottom contributes zero. Averaging the per-w U(Q) bound yields tau_kind*U(Q).

## 2. Exact Boolean-search simulation of full256 Raw

For each changed payload z=V16||BE32(c) on the full160-bit domain, sample independently:

- f(z), Bernoulli with probability1/N, N=2^128;
- G_hit(z), uniform full256 words whose prefix is y (uniform lower128);
- G_miss(z), uniform full256 words whose prefix differs from y (uniform excluded prefix and lower128).

Define R(z)=G_hit(z) if f(z)=1, and G_miss(z) otherwise. This is EXACTLY a product uniform full256 function: each full word with prefix y has probability `(1/N)*(1/N)=2^-256`; each full word with other prefix has probability `(1-1/N)*(1/(N-1))*(1/N)=2^-256`. The tables G_hit/G_miss and every side function are independent of f. Therefore granting them as arbitrary quantum-computable auxiliary advice cannot reveal any f mark.

A complete Raw XOR evaluation coherently parses the byte word, computes the deterministic flag membership in D from known P,a,C, and then evaluates R for changed words or the fixed side function otherwise. One f query computes a mark into scratch, independent G tables supply the proper256 XOR word, and a second f query uncomputes scratch. In an inactive branch the query target uses a plus-state register, on which XOR by f acts identically. Thus at most2 Boolean queries implement each fullRaw query without measuring its input or changed-region support. This remains a fixed coherent unitary for a superposition over changed and side words.

When the algorithm outputs an eligible V!=C,c whose prefix equals y, its z satisfies f(z)=1. Applying TheoremE.3 with2Q Boolean queries proves U(Q). Any algorithm-produced classical hit checks or final Raw evaluations are included in Q; they are not free. No query-history extraction or guessed no-hit event occurs.

The independent tables can be exponentially large in an exact finite domain model. That does not weaken the upper bound: the search theorem permits arbitrary interquery unitaries and we grant side advice, which strengthens the adversary. This proof does not certify an efficient local coherent-outside implementation. Conversely, it does not need such an implementation merely to upper-bound the supplied globalRaw query model.

## 3. Postponing A's pre-key phase preserves the JOINT source view

The ordinary source-RO experiment samples O,P,F/J before A's pre-key raw phase. The child and canonical target are deterministic bounded classical functions of that static O,P,F and fixed selected a. They do not use A's pre-key state or later messages. Model their computation reversibly, recording outputs and private garbage in a disjoint B register; keep bottom as a private flag and continue the unflagged comparator.

In a purified/cq oracle-table representation, both precomputation and A's adaptive raw interaction are controlled by the SAME unchanged classical O register. The former acts on (P,F,B); the latter on (A, its private randomness/measurement environment). Within each fixed O block, these are disjoint-register operations. Therefore they commute. F initialization also commutes with A's pre-key work because F is independent and inaccessible to that phase. Formally `U_pre U_A = U_A U_pre` on the joint initialized state, with measurements purified or equivalently expressed as commuting controlled channels.

Consequently the joint distribution/state of O,P,F, C, canonical target/private garbage and A's complete pre-key continuation is identical whether C/target are computed before or after A's pre-key queries. Partial tracing the hidden B data gives the same public A state, and future source services see the same O/F. All repeated and coherent Raw correlations persist. This is stronger than showing only the target's marginal distribution.

It is legitimate for B to receive P from the primitive before starting A, while withholding it and pk from A until actual source setup completes. When selected target is bottom, actual B may fail locally; its selected source event is zero. The unflagged comparator used for the joint-state argument retains the private bottom flag and does not globally abort source merely because an unrequested row lacks a counter. No timing/cache-availability observables are added; this is the existing atomic partial cryptographic model.

## 4. Honest source calls avoid the changed region at P!=0

Source pin: `publications/LULA-I/release/code/lula1/src/lib.rs` SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

Changed raw words have exact length106: P16 + zero48 + address22 + payload20. At P!=0:

1. Every typed hash has literal header P||zero48||address. If its address differs from selected a, it is outside D, regardless of input length or value. Child type0..4 calls are therefore outside, and all other type7 rows are outside.
2. Legitimate selected type7 digest/search/recheck calls always hash C16||BE32(c). Source C is the genuine FORS PK or child subtree root, stable under legitimate messages and honest cache restores. These are the SAME-base region, not D, even for rejected counters. Canonical target preprocessing is entirely same-base.
3. `hmsg_inner` uses raw word R16||P16||root16||m. Equality with a changed addressed word would force its bytes16..31 (P) to equal zero16, because zero48 occupies addressed bytes16..63. Thus any alias implies P=0. This argument is exact for arbitrary message bytes and length; it does not rely on probability or a message-length heuristic.
4. `hmsg_outer` uses inner32||BE32(c)||P16, length52. It cannot equal a106-byte changed word.
5. In HJ the private derivations/randomizer are F/J, not additional raw-O evaluations. No source secret PRF/raw equality is silently assumed. Source public-context prefix compression is represented by the already fixed complete-hash RO abstraction, not an additional whole-O call on a64-byte prefix.
6. Final verification uses other typed addresses and the same inner/outer words. The selected type7 row appears at most once in the final verifier. Its payload may have V!=C, so charge one ChangedRegion evaluation, even for a forgery that later fails root comparison. Parsing failures and never-reached rows contribute none; the uniform +1 cap is conservative.

Even adversarially selected messages cannot invalidate these exclusions: genuine source signing still reconstructs the same stable child at its indexed WOTS address. All adversarial raw calls, including those while A does not yet know P, ARE counted by Q_A,q/Q_A,c. No classifier inspects a coherent query's support. A coherent raw call always incurs at most2 f queries; a classical honest call known structurally outside D incurs none. The selected final classical call incurs at most2. Hence Q_eff=Q_A,q+Q_A,c+1 is a sufficient charged cap for TheoremE.3.

For P=0, the inner alias exclusion fails; do not discard honest changed-region calls there. Either use the complete Q_all bound or restrict the theorem/event to P!=0 and let the parent pay the single seed-zero term. This file chooses the latter for the sharper source statement.

## 5. Global resources remain explicit

Before target: at most17,392 hidden-seed Col calls and8,704 distinct F values for a bottom child, or15,423/1,024 above. Target canonical preprocessing takes up toL=2^32 full256 evaluations, all same-base. Full accepted-image retrieval, if used, is another same-base Raw call.

After target: adversarial Q_A,q coherent and Q_A,c classical Raw calls, source H_setup+q*H_mode honest classical calls and at most3224 final verifier raw calls. Here the source-relative caps remain `H_setup=2^21*(19505+L)-1`, `H_hot=82090+5L`, `H_cold=8560574463+82090+6L`. Add the target child's precomputation and any same-base accepted-fullword retrieval if not memoized. Persistent F/J tables and ordinary source caches retain their previous explicit caps. No honest work is renamed as adversarial quantum Q.

A complete posttarget Raw cap `Q_all=Q_A,q+Q_A,c+H_setup+q*H_mode+3224+1` always gives the conservative U(Q_all) for the primitive wrapper; source/query times remain finite but huge. The structural region argument justifies replacing this probability-analysis cap by Q_eff on nonzero seeds. This is an exclusion of function dependence on f, not a claim that those honest operations cost no time, memory, oracle work or gates.

If all source A raw calls are already folded into one total Q_A, use Q_eff=Q_A+1. If an alleged resource bound omits source A's classical raw calls beside its coherent Q_q, that bound is insufficient. If any pretarget Raw query is added to the challenge wrapper, this proof's initial independence must be redone; it is not granted by the general collection definition.

## Boundary

The restricted RF bound gate is closed manually under the specified global-fullRO source wrapper and primary search theorem. Low/top canonical predicates and finite exhaustion are retained; full256 raw words are not reduced to independent prefix-only functions. Arbitrary collection conjectures, fixed-h conventional hardness, efficient quantum table realization, full source/kernel verification and the original complete-security theorem remain separate obligations. No source forgery, operational attack, timing, new parameters, old-artifact edits or uploads are involved.

# Independent multicall/source coverage review

**ACCEPTED_MANUAL_SCOPED_QUANTUM_COVERAGE_ENVELOPE — fixed nonzero S only.** This review accepts the root draft's displayed source-COVER envelope in its finite, information-theoretic, atomic classical-service experiment. It does not establish a full QROM signature theorem, an efficient reduction, or a work-factor/category certificate. The root draft itself remains a candidate until its required other review is complete.

Reviewed root `QUANTUM-COVERAGE-DRAFT.md` SHA256:
`990aeb1067f9ac12235ef3982bc9d3d132cffeab5e704a7d0865a69d77e0c0ce`.
Frozen release source SHA256:
`ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

## 1. Independence and the comparison subject

My `INDEPENDENT_DERIVATION.md` was saved before opening the root draft. That derivation deliberately treated the preceding masked-IO source contract as an assumption, independently derived the multicall row-read ledger, a without-replacement alternative, latent padding, and two marked-search projections. The following nonce-hop review was conducted after reading the root draft and rereading the actual release source; it is a source-derived second reading, not a falsely claimed blind first discovery of that hop.

I accept **the root's with-replacement interpretation**, not an unnoticed substitution of my distinct-namespace game. My alternative charges `binom(q,2)/M` and uses `1/(M-r+1)`; the root does neither because its fresh-row game explicitly permits overwriting a namespace upon a new-label collision. Both are valid comparison constructions if their different semantics are retained. No numeric field combines their losses as if they were the same game.

## 2. Source planes, key setup, and nonce marginal

The source's `prf_msg`, `hmsg_inner`, `hmsg_outer`, `Signer::sign`, and `verify_root` give exactly the raw strings stated in the draft. The inner message is not a prehashed fixed-length surrogate. A length-aware register fixes the trailing message label, so two different labels cannot be the same inner point even if their randomizers coincide.

For nonzero S, every addressed honest hash starts with `S || zero[48]`; its second 16-byte block is zero. Every inner point's second block is S. Eligible outer words have their second block unequal to S and have raw length52; addressed words have length at least86. Thus the eligible E plane is disjoint from both I and the addressed honest graph. Excluded outer strings are not declared independent: their possible I overlap is precisely why the guard and final exceptional event exist.

The fixed source graph and root depend on addressed functions and F, not on J or the inner/eligible-outer restrictions. Conditional on that graph and J, selected `I_m` points are distinct and their assigned `U_m` are independent full256 words. Assigning these words and an independent residual inner table therefore preserves the ordinary full-image marginal jointly with J. This statement concerns the global programmed table, not a claim that the current public quantum state forgets earlier queries.

Setup must remain a partial/nonwinning game if its canonical searches fail. One can give the noncompleting branch a dummy root only to define unused latent variables; it contributes zero to COVER. No successful-key-generation conditioning is needed. The independent planes remain independent after any graph-only setup event, but a successful-setup normalized EUF experiment would be a different subject. This review accepts the former subject stipulated by the draft.

## 3. Dynamic nonce comparison and the stopped guard

In the ghost prefix, an as-yet-unrequested label's `R_m` is not used by a public query response. Its `U_m` is also unused before that label's first signing request. All graph data, residual I values, eligible E values, known-label overlays and source metadata are independent of its unused nonce. Adaptive choice of a new classical label consequently cannot inspect that label's unused R or U entries.

For a label currently in its atomic honest call, its U may affect outer/grinding/termination metadata. On the nonbad half, those functions are disjoint from I and do not inspect R. Completion releases only that label's nonce and creates its known overlay; a failing call supplies no output and is absorbing. The controller's choice of which labels have completed can therefore correlate with U and source routes, but cannot correlate unused R with public ghost replies. Repeated completed labels supply known data and never reenter the hidden-nonce set. Nonces are global private-map entries across Restore, not reseeded by a branch.

For each query basis input there is at most one candidate label and one candidate nonce. Averaging over the remaining ghost nonce values therefore bounds the query-register weight on all unexposed programmed I points by `1/N`. A full256 XOR oracle differing there has vector-norm discrepancy at most twice the square root of that weight. Using an IDEAL/ghost prefix and REAL suffix at each public query slot gives `2Q/sqrt(N)` by channel contraction and telescoping; it does not replace this average-prefix invariant by a posterior conditional min-entropy claim. Classical common services cost no new quantum slot because their honest inner result is supplied from the common private U map and their remaining nonbad work never reads an unexposed I point.

The guard is evaluated from U **before** any excluded outer search. It has probability at most `q/N` in the continued ghost, since at most q new-label U entries are independent uniforms; repeated labels nominate none. Its stopped terminal flag is retained, so the same vector-distance argument bounds its source probability by `(2Q+sqrt(q))^2/N`. This is not a newly added production API, and no NoBad conditioning or completed-call normalization is taken. To compare final COVER, two selected final raw evaluations may cross I through an excluded E string; the root correctly uses the conservative `2(Q+2)/sqrt(N)` final examiner cap.

## 4. ROW API, atomic reordering, and colliding labels

The checked GHHM primary Theorem1/Figure2 samples a fresh complete output value but returns only its input and side information. The root's one post-instruction full-row read is necessary. Before instruction r the tighter actual helper cap is `Q+r-1`; the root's constant `Q+q+1` safely dominates it. An original honest scalar call is not automatically free in the reduction's row-oracle query ledger. The plus-slot coherent lookup implements one raw query with one ROW query and an enormous finite clean workspace; its independently checked first-call circuit receipt remains immutable.

The guard coin is sampled first. On a good coin, the namespace is uniform in the entire eligible set of cardinality M. The Reprogram instruction selects that namespace; the known inner assignment is made afterwards within the same atomic call. No adversarial quantum query is interleaved between those steps, and the assignment's value is exactly the selected namespace. This reordering is distribution preserving in the unmodified row game, so AR applies to a genuinely fresh input distribution of point maximum `1/M`, rather than a point mass at a namespace selected externally beforehand.

When a new label collides with an old namespace, its row is resampled in the comparison game. Repeated old labels must subsequently use the **latest row stored by namespace**. Keeping a stale per-message row instead would violate the global current-function semantics. The draft expressly uses the latest namespace row; that interpretation is accepted. A bounded control shows the difference. New-label collisions still use a fresh independent row template and consume one instruction/read; repeats use the current cached namespace row, without new instructions or reads. Each route ever exposed remains among the at most q independent template routes, including routes exposed again after a collision. The comparison itself is nondeterministic relative to earlier source responses, and that difference is paid by AR rather than attributed to the production signer.

The private full-row read changes no external response interface. It evaluates an entire classical function value privately and simulates the source's needed words; a no-zero row gives an absorbing nonresponse, not a public row-failure oracle. This argument does not extend to timing, private row disclosure, coherent signing, interruptions, or coherent access to private simulator state.

## 5. Latent padding and two separate search games

Each independent row admits a disintegration with an unused uniform route X on failure and an independent uniform route at its first zero-filter word on success. Full words, unused hash bits and all other counters are retained. The finite failure probability is `(511/512)^(2^32)`. This is a full-function marginal construction, not conditioning on success. WOTS completion can depend on X, so completed-route samples need not be iid; the q latent route pad dominates all actual disclosed sets without claiming they are iid. Padding after an absorbing or early-terminal branch only enlarges the COVER event.

In the outer search helper, the latent U/templates/X and the full outside functions are independent of the BASE eligible E restriction. Known-row patches are applied according to the actual adaptive controller, never according to a frozen transcript selected by the challenge. Before activation the base word is used; after activation the independent template is used. At a final U outside every padded namespace, the word remains a base word. Conditional on the latent X, its COVER mark is iid with density p(T). Independent uniform covered/noncovered full-word tables and one Boolean query implement that full256 oracle; for p(T)=0 the mark is identically zero and no covered-output sampler is needed. The arbitrary finite register and independent advice can be enormous. The computed final witness plus one selected mark evaluation gives at most `Q+1` Boolean calls; HRS's extra1 yields the conservative `8(Q+2)^2 p(T)`.

Averaging this linear conditional bound is legitimate because the full latent X distribution is iid and independent of the challenge before simulation. It gives `E p(T)=p_F(q)`, with the forced omitted-index factor `1/512`. It is not a per-bucket maximum or a claim that the adaptively completed subset has that expectation.

The **separate inner search helper** instead keeps the BASE I function as the challenge and supplies its independent outside functions, private J, latent U and row templates as advice. It must not receive the full BASE I table. Known-label assignments are simulated locally; a fresh final label has no assignment for any transmitted R. Its residual I image is marked if its lower half is S or its full image belongs to the q padded namespaces. The two image sets are disjoint, and duplicate U values only reduce the union's cardinality, so its density is at most `1/N+q/N^2`. One selected final I evaluation gives the same conservative `8(Q+2)^2` search coefficient. The inner helper's outside advice and the outer helper's outside advice are different stronger views; no common enlarged advice view is asserted.

## 6. Accepted scoped envelope and arithmetic qualification

Write `D=q[sqrt((Q+q+1)/M)+(Q+q+1)/(2M)]` and

    A=min(1, min(1,D)+8(Q+2)^2[p_F(q)+1/N+q/N^2]).

The reviewed root envelope is

    Pr_HJ[C] <= min(1,
      (2Q+sqrt(q))^2/N
      +[2(Q+2)/sqrt(N)+sqrt(A)]^2).

Using the uncapped D inside A produces the same A because an uncapped D>=1 already forces A=1. `checks.py` evaluates all eight q values at Q=2^32 and2^64, independently expands the outer square, and computes a distinct-game row-sum integral bracket separately. Six positive-binomial/Chernoff-tail checks verify the independent alternating moment calculation. The arithmetic uses240 decimal digits and analytic real-number brackets with numerical slack; it is not falsely labelled a directed-rounded machine proof.

At q=2^40,Q=2^32 the root ROW envelope is about2^-67.9972; omitting the honest q reads would yield roughly2^-72 and is unjustified. The complete **candidate COVER envelope** is about2^-59.1929. At Q=2^64 every tested q's COVER envelope is capped1, driven already by the conservative final excluded-half event. This is vacuity of this sufficient bound, not an attack or a measured runtime.

The quantum full-forgery total stays null in this lane. Seed-zero must be charged once only in an eventual common-game unconditional coupling; this fixed-nonzero review does not silently charge it or normalize away its branch. Composition with H/G/D7 and the joint-private hop remains another reviewed obligation. No category or quantum attack-cost certification follows from these event probabilities.

Primary support: [GHHM adaptive reprogramming](https://arxiv.org/abs/2010.15103), Figure2/Theorem1 Eq2; [Hülsing–Kudinov](https://eprint.iacr.org/2022/346), §8.2 Definition9/Theorem4 quoting HRS16. Both were verified from their cached primary PDFs/text, not a secondary summary.

**Outcome: ACCEPTED_MANUAL_SCOPED_QUANTUM_COVERAGE_ENVELOPE_FIXED_NONZERO_SEED.**

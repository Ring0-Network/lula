# Selected-input primitive games: independent definition audit

Scope: source-fixed LULA I, release `src/lib.rs` SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. This derivation was saved before reading the new graph-reduction candidate. It concerns challenge interfaces and reductions, not an implementation attack, a new parameter set, or a certification claim. No manuscript or crypto source was changed.

## 1. Primary sources actually checked

**CITED.** [Hülsing–Kudinov, 2022/346](https://eprint.iacr.org/2022/346), *Recovering the tight security proof of SPHINCS+*: Definitions 2–4, 7; Appendix C Definitions 16 and 19; Appendix E Lemma 5; Theorem 1. Local PDF SHA-256 `80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3`. Its SM-TCR challenger accepts chosen messages under distinct tweaks before releasing the public parameter. Collection access permits predecessor computations at other tweaks. DM-SPR instead samples uniform challenge messages; SM-PRE hides uniformly sampled preimages. WOTS-TW uses PRF, TCR, PRE and UD, not SPR alone. The Appendix-E QROM bound is `32(Q+1/2)^2/2^n + 16Q^2/|P|`, for that exact interface.

**CITED.** [Kudinov–Hülsing–Ronen–Yogev, 2022/778](https://eprint.iacr.org/2022/778), *SPHINCS+C: Compressing SPHINCS+ With (Almost) No Cost*: Definition C.1, Theorem C.2, Appendix E Lemma E.4. Local PDF SHA-256 `1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215`. Definition C.1 supplies an acceptance-selected digest and counter, but requires a different base message to win. Lemma E.4 displays `32(Q+1/2)^2/2^n + 16Q^2/|P|`. This identifier is not a paper entitled “SPHINCS+ in the QROM.” Definition C.1 was visually checked on PDF page 33 / printed page 30; the inequality is `M != M_i`, not merely a different counter. The finite-counter/partial-source interface needs separate treatment.

**CITED.** [Kudinov–Nick, 2025/2203](https://eprint.iacr.org/2025/2203), *Hash-based Signature Schemes for Bitcoin*, Section 13 (printed pp. 29–30), footnote 8. Local PDF SHA-256 `3c58f81a6a0b7e8e040134be1a0013b3977edefdc889e1636d4dfe79cf0e225e`. This section distinguishes generic attacks, bounds based on primitive assumptions, and provable QROM primitive bounds. Its approximate ten-bit discussion describes a particular composition and factors up to 32. It does not justify subtracting ten bits from LULA I. Footnote 8 identifies FORS+C analysis as generic-attack based there.

**COMPUTED (retrieval).** Official metadata pages were fetched on 2026-10-13. Their PDF endpoints returned HTTP 403 to the web tool. Existing local primary PDFs and their text extractions were used instead. The source metadata and quoted identifiers were checked independently of peer reports.

## 2. Four inequivalent challenge interfaces

**PROVED (definition distinction).** Let `F_P(A,x)` be an addressed hash with public parameter P, and let x have fixed length m bits. The following interfaces are not interchangeable:

1. **Uniform-input SPR:** draw P and uniform X; expose `(P,A,X,F_P(A,X))`; output `x != X` with the same image. Some variants let the attacker choose A before uniform X. Uniformity is essential.
2. **Pre-key chosen-input TCR:** draw hidden P; stage 1 commits `(A,X)` through a challenge oracle and receives its image; only then release P. With a collection oracle, stage 1 can derive X from strictly different-address predecessor outputs. One challenge per A is required.
3. **Post-key adaptive SPR / chosen-target collision:** expose P, allow ordinary evaluation, then select `(A,X)` as a target and seek an alternative x. This stronger game can select X using the same restriction it later attacks. It can contain an ordinary collision search. It is not the hidden-parameter SM-TCR interface.
4. **Hidden-preimage PRE:** the challenger draws uniform hidden X and reveals only `F_P(A,X)` (and eventually P). Returning X itself is a valid solution. SPR cannot cover that case because its winning predicate requires a different input.

**PROVED.** “One target per address” does not impose any of these selection distributions. It only forbids repeated target challenges under an address. Likewise, a same-address node collision does not by itself establish a reduction to a random-input SPR challenger.

## 3. Selected honest graph: what commits legally

**PROVED (source structure).** WOTS full-chain positions use distinct type-0 addresses; endpoint compression type 1; Merkle parents type 2; FORS leaves/parents type 3 (different heights/indices); FORS root compression type 4. A designated honest graph input X_A uses starts or designated predecessor images, never the restriction at its own A. WOTS public-key endpoints do not depend on WOTS digest counters. Fixed-width raw header separation, rather than function names, establishes distinct restrictions.

**PROVED (interface sketch).** A topological graph simulator can implement a *collection SM-TCR stage* as follows: compute predecessor values through allowed other-address collection queries; commit `(A,X_A)` before any evaluation at A; obtain its designated Y_A; finish descendants through other addresses; release P only when stage 1 is over; run the target-hit adversary; return a witness at challenged A. This preserves the selected-domain rule without requiring X_A to be uniformly distributed. The chosen X_A may be deterministic given predecessor values.

**OPEN (interface compatibility, not graph acyclicity).** This sketch alone does not simulate arbitrary source raw-oracle prequeries, all public-parameter branches, or quantum oracle access during stage 1. Definition 7's classical collection interface forbids the challenged tweak entirely at the collection oracle. Appendix E supplies a different whole-THF quantum interface and an explicit hidden-P programming loss. A reduction must bind the exact challenger and all ordinary raw-oracle services; it cannot cite Definition 7 while silently giving public unrestricted access to the challenged restriction.

**PROVED (multi-length accounting).** Types 0/3-leaf have 16-byte payloads; binary parent inputs have 32 bytes; type-1 compression payloads have 256 or 512 bytes; type-4 compression has 272 bytes. Treating these as members of one shared-parameter collection is legitimate only with the required distinct-tweak restriction. A theorem for one fixed message length is not automatically a theorem for all five lengths. A joined challenge interface can register all selected addresses; otherwise partition by member length and add the corresponding event probabilities.

**PROVED (one-target selection loss).** Suppose there are D fixed admissible addresses, each used once, and a legal simulator can reserve a uniformly chosen A* before execution. If the target-hit witness is at address A and the simulation is exact for every reservation, success of that single-target simulator is `Pr(hit)/D`. This follows by summing `Pr(A*=A | transcript)=1/D` when A* has no influence on the simulated transcript. It yields `Pr(hit) <= D * Adv_single`, not a query-only bound. If a multi-target distinct-address challenger registers all D, no D multiplier is needed but D challenge calls, graph-generation time and memory must be reported. There is no justified blanket `w*l` multiplier for the whole graph.

## 4. Why random-input SPR cannot be substituted

**PROVED (distribution domination).** In a game with the *same side-information law*, suppose the conditional target density is rho_z(x), the underlying restriction at A is independent of `(Z,X)` before its target value is evaluated, and `rho_z(x) <= alpha/2^m` for every z,x. Pointwise summation gives

`Pr_selected(success) <= alpha * Pr_uniform-target(success)`.

This only compares games whose conditional side-information simulation is available and identical. It does not create that simulator. If X is deterministic given Z, the smallest such alpha is `2^m`; absence of own-restriction dependence alone gives no useful smaller alpha. For LULA's graph this means potentially `2^128`, `2^256`, `2^2048`, `2^4096`, or `2^2176` under complete predecessor advice, rather than a small Winternitz factor.

**PROVED (abort embedding under explicit access assumptions).** If a simulator first legally computes X using only other-address services, then receives an independent uniform m-bit SPR target M at A, it can continue only when M=X. Conditional on every prior state, this occurs with probability `2^-m`. It obtains success `Pr_selected(success)/2^m`, provided the complete function/side-oracle distribution is preserved on the match event. This is a valid but generally useless conversion. It is not an efficient conditional sampler for the predecessor graph.

**OPEN (smallest random-SPR lemma).** To get a better SPR conversion, supply an efficient, distribution-preserving way to embed the uniform challenge at the selected graph input together with its predecessor transcript, or prove a useful conditional-density bound for the exact admissible advice. A statement that hash outputs “look random” does not supply either obligation.

**PROVED (marginal is insufficient).** Even if an individual selected input X_A has a uniform marginal in the RO, it can be jointly constrained by `X_A = F_P(B,Z)` for a predecessor B. Receiving a uniformly sampled SPR target M at A does not supply Z satisfying `F_P(B,Z)=M`, nor authorize programming B. Conditioning on the whole predecessor graph makes X_A deterministic. Thus individual uniformity does not make the random-input challenge simulation exact. A programmable-RO embedding can address this dependency only by proving its programming and query losses; a standard-family SPR interface cannot be granted that operation.

## 5. Canonical type 7 is acceptance-selected, not DAG-selected

**PROVED (source).** At a fixed type-7 address A the payload is `V16 || BE32(c)`, where V is a canonical child independent of type 7 and c is the first accepted counter in `[0,2^32)`. The accepted digest is uniform in the fixed-sum set T only after conditioning on a successful row. Earlier same-child images lie outside T; later same-child and all other-child images are unrestricted. The accepted point X_A therefore depends on its own restriction, contrary to the selected-graph hypothesis.

**PROVED (exact sampler).** For acceptance probability p and counter cap C, success is `1-(1-p)^C`. On success, counter j has unnormalized weight `(1-p)^j p`, accepted y is uniform in T, rejected prefix entries are uniform in `T^c`, later entries uniform in the full image space. On failure the entire same-child row is rejected and has no target. This is the ordinary row disintegration, not reprogramming. Since y is accepted, rejected prefix entries cannot collide with y. A fresh later/other-child point collides with y with probability `2^-128`; no `1/p` factor is needed for this residual event.

**PROVED (two different target events).** Define

`D7_base: V* != V_A and digest(V*,c*)=y_A`,

`D7_full: (V*,c*) != (V_A,c_A) and digest(V*,c*)=y_A`.

Then `D7_base` matches the changed-base-message condition of Definition C.1, whereas `D7_full` also includes counter-only collisions. The original pointwise full-event bound remains a valid RO bound, but published Definition C.1 does not pay for its entire event. A full-payload special-TCR interface must allow `(V*,c*) != (V_A,c_A)`; it is a distinct definition.

**OPEN / smallest extraction alternative.** Instead of strengthening the primitive, prove the complete verifier-cover lemma with D7_base: if the forged child equals the canonical child, descend to that identical child even when its counter differs; only a changed child with unchanged accepted vector is charged to special-TCR. This may remove the counter-only branch from the necessary EUF extraction. It must be checked against the full accepting-path induction before changing a theorem. EUF freshness of the outer message does not, by itself, imply every intermediate WOTS child is fresh.

**PROVED (failure/conditioning distinction).** A finite-row challenger with an explicit failure marker models the source partial experiment. A challenger that conditions on all searches completing is different. If total completion probability is tau and an unconditional bound is epsilon, a safe conditional bound is `min(1,epsilon/tau)`. The exact source/abstract correspondence must state which experiment it uses. Unbounded-counter challenge algorithms cannot be substituted without this accounting.

## 6. Genuine chain predecessors need PRE or equivalent assumptions

**PROVED (logical obligation).** A forged chain can compute a hidden *genuine* predecessor and return it. Because it equals the honest input, this is a preimage solution but no second-preimage solution. The existing identity-family countermodel confirms SPR alone cannot imply target-sum WOTS security. No `w*l` factor repairs a missing implication.

**CITED / OPEN (distribution obligation).** HK22 places PRE challenges at chain cuts only after addressing the distribution of chain outputs via UD hybrids. Its PRE target is the image of a uniformly sampled hidden input, not an arbitrary public target. Reusing that theorem requires an exact chain-cut simulator, an honest-signature reachability invariant, and the relevant UD/PRF game interfaces. In the source RO, fresh distinct-address outputs have an exact uniform marginal; in a general family this cannot be assumed. Access to whole genuine graph payloads would disclose the PRE preimages and is inadmissible for this branch.

**OPEN (smallest chain lemma).** For one selected chain cut, before its preimage is revealed, construct a legal PRE challenge embedding that preserves all prior responses and supplies every later honest-signing response; show the forbidden reveal branch is excluded or explicitly charged; prove the real/embedded distribution loss using the exact PRF and UD interfaces. Enumerate its challenge count, public-oracle work and abort probability. A multi-chain theorem then adds or jointly registers those cuts. This is smaller and more precise than assuming “WOTS is secure under SPR with w*l loss.”

## 7. Verdict for the parent proof

**PROVED:** definition mismatch distinctions, DAG own-restriction blindness, exact acceptance-row selection law, trivial random-input domination/abort conversion under explicit simulator hypotheses, and distinction between genuine PRE solutions and second-preimages.

**CITED:** the named primary security games and bounds, with exact challenge semantics and locators above.

**OPEN:** efficient full shared-oracle selected-input simulator, finite-counter special-TCR source correspondence or D7_base extraction, and chain-cut PRE/UD embedding. No numerical standard-model SPR/PRE bound or uniform ten-bit loss has been established here. Existing reviewed RO/QROM bounds are unchanged.

Own derivation saved before reading any new graph candidate. All writes are confined to this folder.

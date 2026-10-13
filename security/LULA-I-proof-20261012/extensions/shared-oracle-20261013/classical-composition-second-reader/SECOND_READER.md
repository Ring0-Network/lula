# Second-reader decision: classical complete-verifier composition

Outcome: **ACCEPTED_MANUAL_CLASSICAL_COMPOSITION_IN_SPECIFIED_REFERENCE_GAME**.

Independent `DERIVATION.md` was saved from the actual source before reading the root draft or numeric composition work. I then reviewed root `COMPOSITION-DRAFT.md` (SHA256 `21ee235fec883dc8e55c8b4f8759df3d76e722292cf5a2065cae2ab2ef1536dd`) against that derivation and the repaired source-coverage bridge. The current pinned library hash is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. All exact inspected subjects are recorded in `REVIEWED-HASHES.json`.

**No blocking mathematical defect found within the declared classical, partial, atomic, honest-cache reference game.** This decision validates a manual statistical composition, not machine-checked Rust refinement, concrete SHA-256 security, quantum security, side-channel protection, a polynomial-time challenge reduction, or a 128-bit certification.

## Pointwise event classification

PROVED: the four-way split is exhaustive for every accepted fresh-message output in ordinary HJ. It is not performed in the hidden-value blinded continuation.

* The candidate's own route fixes the same exact Merkle direction/address schedule. Starting at root equality, each backward path step either gives a type2 alternate-input target hit or forces the genuine selected WOTS public key. Fixed-width ordered concatenations are injective.
* The type1 compression either gives a target hit or fixes every endpoint. Backward position-specific chain traversal either gives a type0 target hit or makes the supplied coordinate genuine.
* An unexposed WOTS key requires a still-hidden nonterminal coordinate because the accepted sum is less than the all-endpoint sum. This requires **no canonical-counter existence** for an unexposed address.
* At an exposed key, absence of a hidden-coordinate hit forces candidate digits at least the canonical digits coordinatewise. Equal accepted sums then force equality. Width4/8 decoding consumes all128 bits. Different child/counter with equal digits is exactly the final type7 event; the identical pair gives the fixed honest child.
* The upper address's fixed child root is precisely the lower verifier-route subtree: `(tree_j << h_j) | leaf_j = tree_(j-1)`, using source 470–475. Descending all five layers reaches the genuine FORS PK.
* Type4 compression and type3 global-index path descent either produce alternate-input target hits or force each genuine selected secret. A genuine undisclosed secret gives the final hidden-input event; otherwise all17 selected indices are covered at the same FORS address, potentially by different completed signatures.

The split accommodates coincident honest values, copied numerical values from other addresses, arbitrary candidate R and counters, different routes, unsigned paths, endpoints requiring zero completion hashes, and exact signature-length rejection. Only `verify` 672–674 enforces root equality; accepting the returned value of `verify_root` alone would be a different predicate.

## Common-game projection and ledger

| Component | Decision | Required interpretation |
|---|---|---|
| Joint F/J loss | ACCEPTED MANUAL | Continued ideal K/P remain unused except hidden comparisons; q counts initiated calls; raw eligibility and up to two internal/final message-input prefix candidates are counted. On fixed S!=0 the loss is `(Q_H+2q+2)/N`. |
| Adaptive COVER source bridge | ACCEPTED MANUAL AFTER EXISTING REPAIR | Literal inner/outer encodings, secret-R prequeries, endpoint-half alias, full256 inner collision, future-U namespace guess and finite counter search are charged. The final candidate cap is deterministic `Q_H+1`, never `E[N_E]+1`. On fixed S!=0 beta is `(2Q_H+q+1)/N + [qQ_H+binom(q,2)+q]/N^2 + q(511/512)^C`. |
| Hidden-value event | ACCEPTED MANUAL | Its ghost transcript agrees with ordinary HJ until the first hidden hit. Predictable canonical/leaf disclosure leaves undisclosed coordinates independent in the unflagged ghost. Conflicting prior public replies are retained after already charged hits. Full secret graph is not given to this adversary. Bound `(Q_H+3017)/N`. |
| Types0–4 target-image event | ACCEPTED MANUAL | Use its separate event-only designated-DAG strong-view augmentation. Source honest evaluations are designated; final calls at alternate inputs are charged. Its augmentation is not merged with the hidden-value game. Bound `(Q_H+3217)/N`. |
| Exposed type7 event | ACCEPTED MANUAL | Contained in separately augmented all-successful-target event. First accepted rows include rejection history/full256 suffixes and explicit failure. No source residual answers are free. Bound `(Q_H+5)/N`. |

These are probability bounds on events in the same HJ marginal. Separate advice/coupling proofs can be used to bound separate event probabilities and then summed; it is unnecessary and unsafe to give the union of all advice to a single hidden-value adversary. The root draft explicitly respects that distinction.

The source coverage bridge's unconditioned beta has an extra seed-zero `1/N`. Root uses its fixed-nonzero-S argument, not subtraction from an unconditional inequality. Averaging fixed-S bounds and charging S=0 once is valid. The REAL zero-S branch keeps the actual shared oracle, rather than pretending overlapping real inputs use inconsistent independent maps.

## Constants and arithmetic

COMPUTED independently from the actual accepted sums:

* Chains: `4*(32*15-240) + (16*255-2040) = 3000`.
* Hidden final points: `3000+17 = 3017`.
* Types0–4 final points: `3000+5+(4*5+21)+17+17*9+1 = 3217`.
* Type7 final points: at most5.
* Additional final message calls: two for the joint and coverage interfaces, with their different candidate accounting already included in their own terms.

Hence the reviewed ledger adds to

    min(1,
        (6 Q_H + 3 q + 6243)/N
        + [q Q_H + binom(q,2) + q]/N^2
        + q (511/512)^(2^32)
        + (Q_H+1) p_F(q)),
    N=2^128.

The constant is `2+1+3017+3217+5+1=6243`; the last1 is the single S=0 charge. Local adversarial verifications consume Q_H. One challenger verification supplies the separate final budgets. These are RO-call counts, not hash compressions or cycles.

q is a deterministic initiated-call cap across all restored branches. If an interface instead caps completed calls and allows one pending atomic attempt, substituting q+1 throughout is conservative. Unlimited interruption/retry without a corresponding initiated cap is not this game. Completed repeated messages reveal no new index/suffix coordinates; padding to q independent latent exposures is an upper bound, not an assertion that repeats are fresh draws.

## Completion and rollback boundaries

PROVED: the displayed bound is unconditioned; noncompletion is nonwinning. If conditioning on mathematical top readiness K with probability tau_top, `Pr[Win|K] <= Pr[Win]/tau_top` is a valid general inequality and requires no independence of Win and K. Exact `tau_top=[1-(1-p_top)^(2^32)]^(2^21)` concerns top rows, not OS allocation, thread scheduling, physical workload or Rust totality. The source has no general counter-exhaustion abort API. Nonzero-S per-component residual laws also survive metadata-only readiness conditioning, but the unconditioned combined bound plus division is sufficient and avoids silently changing other marginals.

Honest same-key cache restoration preserves fixed roots and canonical counters. Signing/query loss is zero under the stated atomic opaque interface. This does not cover corrupt accepted counters or corrupt child roots; source 648–655 checks acceptance and does not universally authenticate/minimize every supplied cache entry. Secret-bearing benchmark fixture files are not the adversarial snapshot API. No publicly computable-cache claim is used.

## Independent finite discriminator

`python -I -B classifier_control.py` exited0. It exhaustively checked **16,384** typed binary-value worlds with two radix3 chains, fixed sum2, arbitrary endpoint compressor and all numerical collisions allowed. All accepted candidates were classified as a hidden-input witness (294,912), alternate-input target witness (237,568), or exact exposed canonical digits/genuine inputs (49,152). No unexposed-key candidate or changed accepted digit vector escaped. This validates the small classifier invariant only; it does not establish source security or cryptographic probabilities.

## Remaining scientific limits

The complete manual classical inequality is accepted **under the root's specified ideal-RO/reference interface**. Stronger requested claims still need different work: machine-checked source refinement, efficient standard-model primitive reductions, QROM composition, concrete security-level interpretation, robust malicious-cache handling, and broader implementation/side-channel interfaces. In particular, a bound capped at1 for large Q_H is not a demonstrated forgery or a capacity/security certificate. Do not infer 128-bit complete-signer security from FORS-only figures or this summed upper bound.

No manuscript, source, peer derivation or frozen security packet was changed. The authorized editorial changes mentioned by root are unrelated to the cryptographic source binding reviewed here.

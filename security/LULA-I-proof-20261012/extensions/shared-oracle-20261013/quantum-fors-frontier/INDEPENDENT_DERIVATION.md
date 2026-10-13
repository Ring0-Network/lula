# Independent quantum FORS source-selection frontier

**PROVED (independence receipt).** Saved before reading any future peer quantum-FORS proof or an imported adaptive-reprogramming theorem. The derivation starts from the fixed source and the already independently proved elementary coherent-query support inequality. It proposes a conservative first-signing-call comparison; the primary-source check and executable controls will follow. No full QROM forgery bound is asserted.

## 1. Source/game boundary

**COMPUTED.** Frozen release source hash is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Source message functions 164-187 and signing 601-617 give

    R = Tr128 J(m),
    I(R,m)=R||S||root||m,
    U=O(I(R,m)),
    E(U,c)=U||BE32(c)||S,
    D_c=O(E(U,c)).

The first accepted c has zero in the omitted nine-bit coordinate. Its remaining used coordinates are a bucket in B=2^41 and 17 leaf indices in t=512. The real source has C=2^32 distinct counter strings; no implemented exhaustion-return API is added.

**ASSUMED (restricted first-call experiment).** Begin in the JOINT F/J ideal game, with full256 F and J private maps and one complete-output public O. Consider the first initiated classical signing request after key setup, with at most Q coherent raw-O queries before that request and no earlier signing use of J. The message is chosen adaptively from the adversary's current state but is classical. Public keys and setup graphs use typed restrictions outside I/E. Fixed nonzero S separates every I input from typed graph inputs. O is represented by a finite injective length-aware raw register with full256 XOR outputs; its universe contains all relevant honest inputs and all I strings for allowed messages. No compression access, timing/private query transcript, interrupted service, or coherent signing is included. Honest remaining operations are an atomic partial computation and can be treated as a common future channel. This restriction is deliberate: full multi-call composition remains a separate obligation.

**PROVED (fresh R).** At the first classical signing message m, J(m) is an unused private map entry. Conditional on the ideal public-prefix history and selected m, R is uniform128 and independent of that history. This does NOT make O(I) independent of the adversary's quantum memory: coherent prequeries can already have queried every possible R in superposition.

## 2. Elementary inner-point envelope without a borrowed theorem

**PROVED (finite global inner ghost).** Conditional on the typed setup graph, fix S and root. Sample independent full256 V(m) for every allowed inner-message label and private full256 J(m), together with an ordinary O_0. For each label define I_m=I(Tr J(m),m). These strings are injective in the pair (R,m), and their header bytes16..31=S distinguish them from typed setup. Define O_1(I_m)=V(m) and O_1(x)=O_0(x) elsewhere. The ordinary full-function marginal of O_1 is correct: conditional on J and the outside setup restrictions, independently assigned full images replace distinct entries of the independent inner restriction. The outside graph/root is unchanged.

**PROVED (one input/one randomizer).** A raw string in the fixed inner family identifies one suffix m and one R candidate. At any IDEAL prequery to O_0, all J/V entries remain unused by the prefix. Average input mass on the hidden set {I_m}_m is therefore <=2^-128, even if the prefix chooses its query state using O_0 answers. Using the support inequality ||(U_1-U_0)psi||<=2 sqrt(mu), product/channel telescoping with IDEAL prefixes bounds the first-call comparison distance by

    Delta_inner,first <= min(1,2Q/2^64).

**PROVED (comparison semantics).** REAL prefix queries use O_1, which is an ordinary O independent of the private J map in its marginal; its first source I evaluation returns V(m). The comparison prefix queries use O_0. At the atomic first call the public function is made O_1, the source uses fresh R and V(m), and both sides use that same O_1 in subsequent source/future operations. Thus in the comparison game U=V(m) is independently uniform256 conditional on its pre-call history and adaptively selected m. This is a statistical reprogramming comparison game; its combined past/post oracle transcript is not an ordinary unchanged random oracle. It is not a claim that original prequeries can be ignored.

The comparison changes an entire finite inner family conceptually, which supplies the elementary Q/sqrt(N) envelope. It is not optimal and does not license fresh independent U at every later call: after the public function switches to O_1, future coherent queries may correlate with other V(m). A tighter one-point adaptive theorem and a sequential programming construction need separate verification.

## 3. Independent full-U row resampling envelope

**PROVED (random row point mass).** For U uniform256 independent of the pre-call ordinary table/state, let Row(U)={E(U,c):0<=c<C}. Every eligible raw query nominates exactly one full U prefix. Average query mass on Row(U) is <=2^-256. There is no C multiplier in this support calculation: a raw string fixes its counter as well as its prefix.

**PROVED (row sampler marginal).** Sample U independently at the outset but hide it, sample an ordinary base table O_0 and independent full256 W(c), and define O_U(E(U,c))=W(c), O_U(x)=O_0(x) elsewhere. Given U, the full function O_U is ordinary uniform. Its marginal is independent of U. Thus U may equivalently be sampled after the adversarial prehistory, even if its classical message selection is adaptive. The public typed setup graph is unchanged because row strings are52 bytes.

**PROVED (same-channel alignment).** Compare a prefix using O_U against one using O_0, with the same post-call function O_U in both. Their state distance is <=2Q/2^128 by the same ideal-prefix support telescope. A common classical channel then selects m, lazily assigns unused J(m) its fresh R and unused V(m) the independent U, fills other private labels independently, applies the inner-family assignments, and runs the source. This selected-label assignment preserves the full J/V map distribution because no J/V entry was used in the first-call prefix, and U is independent of the entire ordinary marginal O_U. Reprogramming the inner family is the same post-channel in both sides; fresh-point function labels are not separately overwritten after a quantum query.

**PROVED (alias guard).** If U[16:32]!=S, the row strings have bytes16..31 different from S and hence cannot overlap the inner family. On this guard the two programming operations commute and the source's outer row is exactly the independent W(c) stream. The uniform fresh U violates the guard with probability2^-128. Keep that branch in the actual shared-oracle semantics and charge it if replacing it by a clean independent-row experiment; do not condition U on avoiding the guard and still use a2^-256 support probability.

**PROVED (conservative first-call bridge candidate).** Combining the two comparisons, plus one guard branch and an additional uniform-seed branch if S is not fixed nonzero, gives a conservative statistical bridge to a first-call latent fresh outer row:

    fixed nonzero S: Delta_first <= min(1,2Q/2^64+2Q/2^128+2^-128),
    uniform S:      Delta_first <= min(1,2Q/2^64+2Q/2^128+2*2^-128).

This manually derived comparison and its same-channel selected-label argument require independent review before promotion. It is only a first-call statement. No peer proof was used to formulate it here.

## 4. First acceptance, full namespace and partial completion

**PROVED (fresh row law).** In a freshly resampled outer row each full256 W(c) is independent uniform. Its omitted digit Z_c is independent of its bucket/17 leaf coordinates X_c. For every c<C, the event of first acceptance at c depends only on Z_0,...,Z_c. Therefore X_c at that accepted counter is uniform on [B]x[t]^17 and independent of the accepted counter/rejected Z prefix. Unused digest bits do not affect this law.

**PROVED (finite exhaustion).** No accepted counter has probability f=(511/512)^(2^32). The comparison may retain this failed-row branch as absorbing noncompletion, with an independently sampled latent X that is never emitted. Then f is explicit but need not be charged merely to state the partial comparison. Replacing it by an always-successful service costs f; normalizing on success needs a separate division/conditioning statement. Later WOTS searches may also prevent completion and can depend on the selected route; no uniformity is claimed after conditioning on the entire signature's successful return. Independent latent route draws can be padded only after their source correspondence is proved.

**PROVED (repeated message).** R and I are memoized for repeated m. Repeating m does not generate a fresh U or row and must reuse the same route. This first-call bridge cannot be applied repeatedly to old labels.

## 5. Missing full-QROM obligations

**OPEN (primary tight lemma).** Verify an exact primary adaptive-reprogramming/O2H theorem, including the point distribution, oracle-output/public disclosure, coherent query budget and constants. Its tighter loss cannot be guessed from a remembered formula or replaced by the elementary bound without checking what it samples/reprograms.

**OPEN (sequential source bridge).** Build one transcript-consistent multi-call programming game preserving earlier inner points, full outer rows and repeated-message memoization, including U collisions with prior row namespaces, I/E raw aliases, pre-key/adaptive coherent queries and absorbing partial searches. A one-call result is not the adaptive two-stream theorem required for arbitraryq.

**OPEN (quantum coverage candidates).** Quantum queries do not supply a classical list of Q_H+1 independent candidate digests. The classical retained-candidate padding argument cannot be transplanted. A quantum averaged/transcript coverage search reduction with adaptive disclosures and explicit extraction is still needed.

**Status: INDEPENDENT_FIRST_CALL_DERIVATION_SAVED; PRIMARY_CHECK_AND_CONTROLS_PENDING; FULL_QROM_TOTAL_OPEN.**

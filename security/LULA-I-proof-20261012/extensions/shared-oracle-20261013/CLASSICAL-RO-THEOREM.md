# Reviewed classical complete-verifier RO theorem

**PROVED — manual theorem accepted by two source-derived independent readers.** This is a direct information-theoretic classical RO bound for the fixed source game, not an efficient primitive reduction, a checked Rust refinement, a fixed-SHA guarantee, or QROM security. All component statements must refer to the same ordinary joint-private ideal source experiment. The entire secret graph is never added to that experiment.

## 1. Common experiment and source binding

**ASSUMED — model.** Let N=2^128, q count initiated reference signing calls, and Q_H cap adversarial classical complete-hash queries, including pre-key calls. There is one final public verification. Retain the parent source experiment: three independent uniform seed components; ordinary full256 public oracle; memoized independent full256 F(A), J(m) for privatized seed derivations and message randomizers; honest opaque snapshots; only completed signature responses; no timing, cache bytes, private hash transcripts, or corrupted cache. A noncompleting setup/signing call reaches no winning completion. Do not condition the probability space on no prior bad event or on successful setup.

**COMPUTED — fixed source.** Release library digest is ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. `sign` 601–668 fixes its child at each full WOTS address and exposes one canonical suffix vector; `verify_root` 688 onward determines the route from transmitted R, c_F and follows exactly five addressed WOTS/Merkle reconstructions. The FORS root compressor and each WOTS PK compressor use ordered fixed-length node vectors.

**PROVED — compatible views.** For each component, take the probability of its event in this same ordinary HJ experiment, for a fixed nonzero public seed S. A component proof may upper-bound that event in a separately augmented experiment whose projection is HJ, embedding the original adversary by ignoring its extra advice. Full secret-graph advice is permissible for the public target-image event, but impermissible for the hidden-value event. These advice experiments are not merged. The hidden-value coupling bounds the probability of the first hidden hit in ordinary HJ by agreement until that hit; classification below is performed in HJ, not in its blinded continuation.

## 2. Four verifier-relevant events

**PROVED — definitions.** Exposed means legitimately disclosed by a completed signature at that indexed coordinate, permanently across branches.

* C: the final FORS route satisfies the zero filter and all 17 selected genuine secrets have been exposed at the selected instance. The coverage lemma already includes retained public candidates, old rejected/accepted honest grinding points, and one fresh final point.
* H: some public query, including the final verification trace, evaluates a type0 chain point on its genuine currently unexposed payload, or a height-zero type3 FORS point on its genuine unexposed secret. Exposure of a chain includes its forward suffix, not just its starting disclosed value. Endpoint-only positions are initially public in the proof's safe public-surface extension.
* G: a public query in types0–4, including the final trace, evaluates a different payload from the honest designated graph payload at the same actual encoded address and returns the same truncated honest output. This is a target-image hit, not necessarily a full256 collision.
* D7: a public type7 query, including the final trace, at an exposed successful canonical row has a different (child,counter) pair from its honest canonical pair and the same full128 digest slice. The stronger all-row target event upper-bounds this exposed-row event.

## 3. Exhaustive accepting forgery split

**PROVED — manual structural lemma.** In ordinary HJ with S nonzero, every accepting final signature on a fresh message satisfies C or H or G or D7.

Start at the accepted top public root. Compare the forged top authentication reconstruction with the honest mathematical top path for the same chosen route. Its address/direction schedule agrees exactly. The checked addressed Merkle lemma yields either a different-input/equal-output witness, which is G in the actual final trace, or identical leaf and path. In the latter case the forged WOTS PK equals its genuine PK.

At any layer whose reconstructed root equals the honest root, apply that same argument, then classify the equal WOTS PK:

1. If the ordered reconstructed endpoint vector differs from the genuine vector, its final type1 compression is G.
2. Otherwise the endpoints match. If some supplied chain start at its claimed digit e_i differs from the genuine value at that position, follow its addressed completion until its first merger with the genuine chain. The preceding payloads differ and their images agree at the same type0 position: G. A claimed endpoint position with different supplied value cannot have equal endpoints, so this case never needs a nonexistent chain call.
3. Otherwise every supplied start is genuine. If this WOTS address is unexposed, sum e=S<ell(w−1) forces at least one e_i<w−1. The verifier's first chain call at this genuine unexposed predecessor is H. No canonical vector need exist at that unexposed address.
4. If the address is exposed with canonical vector x and e differs from x, equal digit sums imply e_i<x_i for some i. Because x_i<=w−1, that e_i is nonterminal and remains outside the exposed suffix. The first chain call there is H.
5. If e=x but the verifier's (child,counter) differs from the canonical pair, digit decoding is injective over the entire128 output bits (width4/8 and lengths32/16). The final type7 query is D7.
6. Otherwise the same child and canonical counter have been reconstructed. This child is fixed by the key and address: the FORS PK at layer0 or the selected lower-subtree root above it. The latter is the honest root for the next lower layer on this exact route.

Thus, in the absence of H/G/D7, downward induction over the five layers yields the genuine selected-instance FORS compressed PK. If its reconstructed ordered root vector differs, final type4 compression is G. Otherwise each selected FORS tree reconstructs the genuine root. Apply the addressed Merkle lemma with the actual global-index schedule: a changed leaf/path gives a type3 internal G witness; otherwise the reconstructed leaf image is genuine. A supplied secret different from its genuine secret yields a height-zero type3 G witness. A genuine unexposed secret yields H in that same final leaf call. If none of these occurs, all17 genuine selected secrets were exposed, and acceptance supplies the omitted-coordinate zero filter: C.

This proof does not restrict comparison to signed paths and does not call an unexposed canonical certificate replay. The witness queries are in the ordinary verifier trace, not hypothetical adversarial queries or private graph evaluation.

## 4. Scalar budget and single seed-zero accounting

**PROVED — independently reviewed conditional component ledger.** For every fixed nonzero S, the already reviewed component lemmas give:

\[
\delta_J=(Q_H+2q+2)/N,\qquad
\beta=(2Q_H+q+1)/N+(qQ_H+\binom q2+q)/N^2+q(511/512)^{2^{32}},
\]
\[
\Pr_{HJ}[C]\le\beta+(Q_H+1)p_F(q),\quad
\Pr_{HJ}[H]\le(Q_H+3017)/N,
\quad\Pr_{HJ}[G]\le(Q_H+3217)/N,
\quad\Pr_{HJ}[D7]\le(Q_H+5)/N.
\]

Use untruncated upper sums and cap the final result at one. All components are conditional on a fixed nonzero S, but not on avoiding any other bad event. Average those fixed-S bounds, then separately pay Pr[S=0]=1/N once. This is not subtraction of a seed charge from unrelated unconditional inequalities.

**COMPUTED — independently reviewed consolidated arithmetic.** With initiated-call convention,

\[
\epsilon_{\rm RO}(q,Q_H)\le\min\left\{1,
\frac{6Q_H+3q+6243}{N}
+\frac{qQ_H+\binom q2+q}{N^2}
+q(511/512)^{2^{32}}
+(Q_H+1)p_F(q)\right\}.
\]

The constant is 2+1+3017+3217+5+1=6243. For a completed-call convention permitting one pending call, substitute q+1 everywhere as a safe deterministic initiated cap. No work-factor or bit-level label is inferred merely from this success-probability sum.

**PROVED — promotion gate passed within the stated RO game.** Both `classical-composition-second-reader/SECOND_READER.md` and `classical-composition-numeric/REVIEW.md` independently accept the exhaustive split, common-game projection, source call caps, initiated-query convention and single seed-zero charge. Their first derivations were saved before this reviewed draft was read. The immutable reviewed draft digest is 21ee235fec883dc8e55c8b4f8759df3d76e722292cf5a2065cae2ab2ef1536dd. Classical RO total fields now contain this bound; generic primitive reductions and full QROM remain OPEN.

## 5. Completion conditioning, rollback, and target meaning

**PROVED — setup normalization when a valid unconditioned bound exists.** If cryptographic top-row completion K has probability tau_top and other physical success is assumed, Pr[Win|K]<=Pr[Win]/tau_top. Exact tau_top is [1−(1−p_top)^(2^32)]^(2^21). This inequality needs no independence of Win and K. Noncompletion was already nonwinning in the unconditioned game. It supplies no guarantee of allocation, thread scheduling, Rust totality, or fixed-SHA success.

**PROVED — conditional cache transfer.** In the honest-cache atomic model, exact deterministic transparency transfers this reference event probability with zero probability/signing-query loss and only bookkeeping time overhead. Corrupt-but-undetected counters do not satisfy that interface and no claim of publicly computable cache is made.

**OPEN — intended certification.** This accepted classical theorem is not an efficient standard-model PRF/SPR/TCR reduction or a complete QROM theorem. Its conservative numerical value may fail a literal 2^-128 failure criterion, especially for Q_H=2^128. Such vacuity is not a forgery attack or a proof of inadequate actual work factor. The requested level/category statement must remain “not established” unless its precise resource-security criterion and all relevant reductions are established.

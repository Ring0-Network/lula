# Independent quantum one-target graph-event derivation

Saved before reading the `quantum-graph-targets` author files. This derivation is an information-theoretic event bound in a specified classical-signing / quantum-public-oracle ideal game. It is not an efficient cryptographic reduction, QROM privatization proof or complete signature theorem.

## Primary theorem checked directly

The official [ePrint 2022/346](https://eprint.iacr.org/2022/346), Hülsing and Kudinov, *Recovering the tight security proof of SPHINCS+*, was opened online. The online PDF fetch returned HTTP 403. The cached primary PDF `R8/R8B-immutable-authority/refs/eprint-2022-346.pdf` was then inspected directly with pypdf; its SHA-256 is `80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3`. Physical page 23 contains Definition 9 and Theorem 4. The problem is to output a marked input for a randomly sampled Boolean function, with independent Bernoulli marking density lambda. Its quantum-query bound is

```
Succ_lambda <= 8 lambda (Q_B+1)^2.
```

The theorem concerns a classical output x whose Boolean value is one. It does not bound an unmeasured notion of having ever included a marked point in a superposition.

## Graph and residual image factorization

The pinned source uses complete SHA-256 images and 128-bit graph-node slices. Its SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Consider the honestly fixed one-target-per-address graph for types 0–4: chain-position hashes, WOTS public-key compression, Merkle nodes, FORS leaf/internal nodes, and FORS-root compression. At each relevant encoded address A, the graph fixes one canonical raw input x_A and target prefix y_A. Fixed-width domain/address framing binds an alternative raw point to at most one A.

The conditional graph-table argument must expose graph points before residual points using the actual acyclic dependencies: chain inputs derive from previous-position outputs, compression from endpoints, tree parents from children, and FORS-root compression from roots. Secret chain/leaf starts are external independent maps in the joint ideal game. The graph must not select its input for A by inspecting residual outputs at the same A. Subject to that exact graph-sampling lemma, residual raw points remain mutually independent uniform full 256-bit images after exposing the complete G, including canonical full-image suffixes.

For each finite-register raw input x, sample independently a Bernoulli mark f(x) with lambda=2^-128. At a relevant residual point, sample a full 256-bit image a_x uniformly among images whose first128 bits differ from y_A, and b_x with first128 bits y_A and independent uniform remaining128 bits. Set

```
O_f(x) = a_x if f(x)=0, b_x if f(x)=1.
```

This is exactly uniform on all 256-bit images: each prefix has probability 2^-128, and each suffix is uniform. At canonical graph points or other points outside the event language, set a_x=b_x to the appropriate known graph/independent outside-table image; their mark is ignored. All such nuisance data and the whole G must be independent of f. The resulting oracle preserves the full image interface, not merely its truncated graph slice. Pre-key quantum queries are included because f and the coherent full table are fixed from the beginning; revealing the same G early only enlarges information.

The raw input domain must be a finite bit-string/length register admitting injective encodings. Every fixed finite adversarial circuit has such a register bound. The result is uniform in that bound. An infinite-oracle Hilbert-space assertion cannot be substituted without a model definition. The source's selected valid compressed addresses must be injective; arbitrary layer truncations outside the selected parameter set are excluded.

## Exact one-Boolean-query oracle simulation

Let delta_x=a_x XOR b_x. The desired full function query is XOR by `a_x XOR f(x) delta_x` in a 256-bit response register. XOR by a_x is free relative to the Boolean query budget. For delta_x!=0, choose a pivot j with delta_x[j]=1. Define L_delta as the reversible fanout of pivot bit j into each other bit i with delta_x[i]=1. It is involutory and maps e_j to delta_x. Thus

```
L_delta X_j^f L_delta = XOR(f delta_x).
```

To apply X_j^f with one ordinary Boolean function-oracle call, prepare a one-qubit work register in |+>, coherently swap it with response bit j, call `|x,t> -> |x,t XOR f(x)>` once, and swap back. The work register returns exactly to |+>, because the swapped-in response position is |+> and is untouched during the Boolean call. Undo its preparation to return to |0>. The response pivot has been flipped by f(x). All pivot computations, fanout and swaps are controlled coherently by x. For delta_x=0, do not swap; the query acts on |+> and has no effect. Hence the same one query works coherently across marked, unmarked, outside and canonical branches without retaining a mark ancilla.

This independently supports a clean one-query simulation, provided the theorem's oracle is the ordinary Boolean XOR oracle and the full table data is free independent advice. A straightforward compute/control/uncompute construction also works with two Boolean queries; it yields a weaker but safe alternative. Merely computing f into |0> and discarding the resulting ancilla after one query is invalid.

## Output extraction and verifier allowance

A reduction must obtain an observable alternative raw graph input x with O_f(x)'s prefix y_A, so that f(x)=1. It may run the original adversary and classical signer, then the classical final verifier with an explicit trace and compare that trace to G. A same-output/different-input witness present in the final trace can then be output as a classical Boolean-search solution. This requires the graph classification/extraction result; query amplitude alone gives no output witness.

The signer may be simulated from G and independent outside tables only if its graph queries are canonical. Its other message/type7 calls must be outside the relevant graph families under the literal shared-oracle guards; uncharged residual calls by arbitrary corrupted caches or extra APIs are excluded. Signing preparation is not automatically free just because a paper calls it preprocessing. Full G revelation is conceptual and may be enormous; no efficient simulation is claimed.

For the selected source parameters, final verification uses at most 3217 **types 0–4** complete hash calls. Independently count: 17 FORS paths each have one leaf hash plus nine parent hashes, and one roots-compression call, giving 171. Four lower WOTS layers each have 32 base16 digits of accepted sum240, so exactly `32*15-240=240` remaining chain hashes, one PK compression and five Merkle hashes: 246 each, totaling984. The top layer has 16 base256 digits of accepted sum2040, so `16*255-2040=2040` remaining chain hashes, one PK compression and 21 Merkle hashes:2062. Total171+984+2062=3217. Rejected verifications stop earlier. This is a source call bound under accepted fixed sums, not a latency bound.

With Q_q adversarial full-oracle quantum queries including pre-key queries, the one-query reduction uses at most Q_B=Q_q+3217 Boolean calls, provided all other source interactions are represented by f-independent data and canonical points. Then the observable graph-witness event is bounded by

```
min(1, 8 (Q_q+3218)^2 / 2^128).
```

The safe two-query simulation instead gives `min(1,8(2(Q_q+3217)+1)^2/2^128)`. The extra +1 in each expression comes from the primary average-search theorem, not a free verification. This event bound does not prove that every fresh-message forgery produces a graph witness, does not cover secret inversion/FORS coverage/type7 target events, and does not imply category-1 or full QROM security.

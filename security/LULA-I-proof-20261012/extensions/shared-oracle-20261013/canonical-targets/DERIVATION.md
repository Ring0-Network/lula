# Independent first-accepted type-7 target derivation

**Scope:** an independent manual classical complete-hash random-oracle derivation from the pinned source, saved before consulting any peer report for this obligation. This is a same-address digest-target event lemma and a top-cache grinding-completion calculation. It is not complete signature security, a QROM lemma, an efficient primitive reduction, or a claim of guaranteed source termination.

## 1. Exact source subject and separation

`release/code/lula1/src/lib.rs` SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. `WotsC::digest` at 216–220 hashes the complete raw string

```
X_A(V,c) = S16 || zero48 || Addr22(A,type=7,w2=0,w3=0)
           || V16 || BE32(c).
```

Its length is 106 bytes, including the precomputed public-seed block. Its returned digest is the first 128 bits of the complete 256-bit SHA output. The fixed-width raw encoding is injective in the actual compressed address, V and c. The pinned parameter set has layers 0–4; casting layer to one byte therefore causes no address truncation alias. This statement does not extend to arbitrary caller-supplied layers beyond 255 or noncanonical address encodings.

`WotsC::digits` consumes all 128 digest bits for the selected widths 4 and 8. Consequently equality of the full decoded digit vectors is equivalent to equality of 128-bit digest slices. This would need revision if a width left unconsumed bits. `accept` requires the configured suffix digits to be zero and the full sum to equal s. Here z=0 for every layer. `grind` starts at c=0 and increments a u32 until the first accepted vector, with C=2^32 distinct counter strings.

For each honestly fixed address A, its child V_A is an entire graph function of the seed/private derivations, WOTS chain and compression hashes, and Merkle/FORS hashes of types 0–6. `compute_subtree` at 479–484 uses WOTS public keys, not digest counters; `child_value` at 486–496 returns a FORS public key or a child subtree root. Although the operational cache is built together with counters, its stored tree roots are computed from WOTS public keys and do not depend on those counters. The public graph can therefore be specified independently of the type-7 oracle restriction. It is not necessary to claim that arbitrary functions of an oracle graph are independent of arbitrary hash outputs.

This derivation uses that precise type separation in the already specified classical joint F/J ideal game. Honest graph inputs of other address types cannot equal a type-7 input. More generally, the same target sampling argument is available whenever the honest graph is determined by keys and an independent oracle restriction. Alias losses concerning private derivations or other message hash interfaces belong to the shared-oracle game bridge and cannot be omitted when composing a real-source claim.

## 2. Exact conditional row sampler

Condition first on keys and the graph outside type 7. Fix A, its child V_A, the acceptance set T_A within M=2^128 digest slices, and p_A=|T_A|/M. Let D_c be the first 128 bits of O(X_A(V_A,c)), for c in [C]. Distinct raw points have independent uniform full 256-bit images. If the row succeeds, define c_A as its first accepted counter and y_A=D_c_A. Otherwise record the failed-row marker bottom.

An exact disintegration of the entire type-7 row is:

1. Sample success/failure with success probability `s_A=1-(1-p_A)^C`.
2. On success, sample c_A with `Pr(c_A=j | success)=(1-p_A)^j p_A/s_A`, for 0<=j<C. Sample y_A uniformly from T_A, independently of c_A.
3. For each earlier same-child counter c<c_A, sample D_c independently uniformly from the complement of T_A. Set D_c_A=y_A. For later same-child counters and all other-child payloads, sample independent uniform digest slices.
4. On failure, sample all C same-child D_c independently uniformly from the complement of T_A. There is no y_A or canonical counter to expose. Other-child payloads remain uniform.
5. Every full 256-bit image has an independent uniform remaining 128-bit suffix, including the canonical point. Repeated raw queries reuse the same full image.

For any particular successful row assignment, the product of the sampler's weights is

```
[(1-p)^j p] [1/|T|] [1/(M-|T|)]^j [1/M]^(C-j-1)
= M^(-C).
```

The failure assignment has weight `(1-p)^C/(M-|T|)^C=M^(-C)`. Thus the sampler has the exact iid-row marginal, including full images after adding independent suffixes. For p=0 or p=1, use the corresponding degenerate branch instead of dividing by an empty set.

Rows at different encoded addresses are independent even if their children collide. A type-7 raw point outside a row's fixed-child family remains uniform. It is important that the target is chosen from this row's first accepted same-child counter, without looking at residual other-child or later-counter images.

## 3. Target event, prequeries and adaptivity

Give the adversary the complete honest graph and every successful row's `(V_A,c_A,y_A)` at the start of an augmented experiment; failed rows reveal only bottom. This increases information compared with exposing targets as signing reaches them. The conditional sampler above reproduces the original joint oracle/target distribution, so this is an exact initial-information extension, not a reprogramming with a different marginal.

Define Bad_7 to be a raw query to a point X_A(V,c) with a successful target row at A, `(V,c)!=(V_A,c_A)`, and digest slice equal to y_A. Charge each distinct raw point at its first evaluation.

After any transcript, all exposed target data, and previous complete oracle outputs:

- An earlier same-child counter has a rejected slice and cannot equal accepted y_A: conditional probability zero.
- A fresh later same-child counter or other-child point has an independent uniform slice: conditional probability exactly 1/M.
- The canonical point returns y_A with probability one but is excluded from this event.
- A repeated point is not a new attempt; any hit was charged at its first evaluation.
- A failed row has no target; no Bad_7 event is defined there.

Every raw byte string identifies at most one actual encoded address and payload; there is no multiplication by the number of exposed targets. For a deterministic cap Q_H on adversarial raw oracle evaluations, the union bound is

```
Pr(Bad_7) <= min(1,Q_H/2^128).
```

The stronger experiment also permits the adversary to choose its addresses and payloads after seeing all targets, so adaptive allocation across rows does not defeat this bound. Queries before original key/target disclosure are included by placing their ordinary algorithm in the initial-information experiment and letting it ignore the additional information until its scheduled disclosure. Do not start counting only after a canonical certificate is first exposed. Old residual points whose values become useful after target disclosure must already have been charged at their first evaluation.

One final challenger verification can add one fresh type-7 point for **each layer it actually reaches**, rather than just one for the full signature. With d=5 layers, a safe cap is `Q_H+d`; repeated or canonical final points add no new Bad_7 hit. If local adversarial verification uses the raw oracle, its calls are already within Q_H. This is a target-event bound and not a proof that every changed digest or child is an extraction witness; that classification remains separate.

In applying this raw-query event to the signing game, honest operations must expose no additional residual type-7 answers for free. Honest grinding at fixed children queries only rejected earlier counters and the canonical point, whose constraints are already represented in the augmented experiment; canonical counters, roots and WOTS signatures depend on that disclosed data and the graph outside type 7. Honest, consistent cache restoration satisfies this restriction. Arbitrary cache corruption or a caller invoking public digest APIs on other payloads needs separate query accounting. The shared-oracle game's nonzero-S guard separates message-inner and private message-randomization inputs from addressed type-7 strings; outer message inputs are too short to alias them. Its relevant alias losses cannot be silently dropped when composing this event lemma.

Revealing the graph and all targets is a conceptual information extension for an upper bound. It may be enormous and is not an efficient simulator or an efficient target-challenge embedding. The graph domain must be fixed by the selected valid parameters, independently of type-7 outputs; this is not an adversarially chosen graph after looking at residual images.

The full128 digit encoding connects the event to equal accepted WOTS digit vectors: if forged and honest vectors are equal at A but `(V*,c*)!=(V_A,c_A)`, the forged raw point is a Bad_7 hit. If vectors differ, this lemma says nothing about chain preimages, mergers or changed endpoint compression.

## 4. Top-cache grinding completion

The selected parameter literal in `src/bin/lula1_driver_original.rs` is four uncached `(h=5,lw=4,z=0,s=240)` layers and one cached `(h=21,lw=8,z=0,s=2040)` layer. In `Signer::keygen` at 512–541, the top cached layer has no higher layer, so `nsub=1` and `nleaf=2^21`. Each of its rows has 16 eight-bit digits and acceptance condition sum=2040. The count is exactly

```
a_top = [x^2040](1+x+...+x^255)^16
      = sum_{j=0}^7 (-1)^j binom(16,j) binom(2040-256j+15,15),
p_top = a_top / 256^16.
```

Because all row addresses differ and V_A is independent of the type-7 restriction, their first-C success indicators are iid Bernoulli with probability `1-(1-p_top)^C`, even conditional on the entire graph. The exact cryptographic-grinding completion probability of all top cache rows is

```
tau_top = [1-(1-p_top)^(2^32)]^(2^21).
```

The failure probability is `1-tau_top`, bounded by `2^21(1-p_top)^(2^32)`. Conditional on completion, each row has the successful-row sampler above, independently; all later/other-child residual points remain uniform. Conditioning on cache completion must be stated explicitly if the resulting game samples only completed keys. Alternatively retain the partial KeyGen experiment and charge noncompletion separately.

This probability is for the specified complete-hash random-oracle source model. It is not a probability theorem about arbitrary fixed seeds under actual fixed SHA-256, nor an observed completion frequency. Other finite graph computations, valid parameters/positive threads and successful allocation are assumed. OS failure, scheduling and memory exhaustion are outside this cryptographic calculation. A row with no accepted counter causes wraparound repetition in an unchecked build or overflow failure in a checked build; the source has no general counter-exhaustion abort API. The result therefore provides neither unconditional total correctness nor a runtime upper bound.

## 5. Controls to execute independently

A tiny exhaustive finite-alphabet control will compare the iid-table marginal against the successful/failed conditional sampler, and test fresh residual hit probabilities with all targets exposed. A wrong-target-selection control will select an accepted target using residual outputs; such a rule can make a residual hit certain and shows why the exact first-same-child-acceptance rule is necessary. The real top acceptance count will be recomputed both by inclusion-exclusion and integer dynamic programming. These checks validate small finite identities and arithmetic, not the entire Rust implementation or complete security.

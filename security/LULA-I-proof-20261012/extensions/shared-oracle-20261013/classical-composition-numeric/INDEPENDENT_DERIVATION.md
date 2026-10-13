# Independent classical composition derivation

**PROVED (independence receipt).** This derivation was saved before reading the new root candidate or the new canonical-target proof. The fixed source/game were re-read first. Prior completed graph/hidden component reviews were known from my earlier independent assignments; their new composition proofs were not read. No source, paper, frozen packet, or earlier result was changed.

## 1. Fixed source-game object

**COMPUTED.** Release source SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Relevant code: typed full addresses 69-98, WOTS chain/compression 239-276, FORS paths 396-413, fixed honest WOTS child 486-499, completed deterministic signing 601-667, final verification 679-733.

**ASSUMED (HJ).** Ordinary classical EUF-CMA game after the explicitly declared joint privatization: independent memoized F values for type-5/type-6 secrets and independent J(m) randomizers; all remaining code hashing uses one ordinary full-output 256-bit O with the exact source's raw encodings and 128-bit prefix truncation. One fixed parameter set and one root, honest atomic completed calls, no secret hash-call/cache/timing/fixture exposure, at most q signing queries and Q_H adversarial full-O queries. Signing/metadata searches are partial: a nonterminating setup or signing request never reaches a winning completion. No normalization on successful setup is assumed. Fix nonzero public seed unless a zero-seed event is explicitly added. This is an ideal-game statement, not a real-SHA or QROM theorem.

**PROVED (honest reference graph).** For every typed honest node address there is one designated input and one image; full WOTS position addresses distinguish consecutive hashes. Each full WOTS key address has one fixed honest child V_a. All completed honest exposures at that address use the smallest accepted counter c_a and its same full 128-bit digest vector e_a. FORS secrets and WOTS chain positions are indexed, not globally interchangeable just because their numeric values coincide. Exposure accumulates over every completed signing response across every restored branch.

## 2. Four events on this same ordinary HJ probability space

**PROVED (C).** The final message digest passes the omitted-index zero filter, and its selected FORS bucket b and all 17 selected real-tree indices lie in the sets exposed by completed signing responses before final verification. The final message is fresh. R and the counter remain arbitrarily selected by the adversary. This is an actual-transcript coverage event, not just a fixed-bucket expectation.

**PROVED (H).** An adversarial public call or a call in final verification supplies a genuine WOTS chain-position value at its own full type-0 address before that coordinate has been legitimately revealed, or a genuine FORS secret at its own height-zero type-3 leaf address before that leaf has been revealed. WOTS suffix closure is included in legitimate knowledge. Known endpoints and exposed suffixes are not charged. This is an addressed original-input event.

**PROVED (G).** An adversarial public call or final-verifier call in a type-0/1/2/3/4 honest graph restriction supplies a payload different from that address's designated honest payload, yet its 128-bit output prefix equals the designated honest image. This is an addressed alternative-input image event; it is not a collision somewhere in the enormous graph.

**PROVED (D7).** At a full WOTS type-7 address having been exposed by a completed honest signature, an alternative payload (V,c) != (V_a,c_a) yields the same entire 128-bit digest e_a as the canonical point. Calls before the exposure can be counted retrospectively if they are later used; final verification itself also supplies the needed evaluation. An enlarged event may include every key whose canonical point exists, even if never exposed. Honest computations at the designated point do not create D7.

## 3. Exhaustive backward reconstruction

**PROVED (Merkle/path step).** If a forged path reconstructs an honest subtree root and no G occurred, the root computation used its designated ordered child pair. Its path child therefore equals the honest child. Repeat down the path: every ordered pair is designated, every supplied sibling agrees, and the reconstructed leaf is the honest WOTS-PK image. If an alternative ordered pair first merges into an honest image, its very hash call is G. This reasoning does not assume the forged path was previously transmitted in a signature.

**PROVED (WOTS-PK step).** With no G, an honest WOTS-PK image can only be obtained from its designated ordered endpoint tuple. Each reconstructed chain endpoint must be the corresponding genuine endpoint. An arbitrary chain start at digit y_i that reaches the genuine endpoint without G must itself be X_(a,i,y_i): trace backward through addressed positions, using the first merge into a genuine suffix. A start already at w-1 needs no hash and is the public endpoint.

**PROVED (unexposed WOTS key).** At a key never exposed by a completed honest signature, only endpoints are legitimately known. An accepted vector has sum S strictly below ell*(w-1), so some y_i < w-1. The first verifier hash for that chain inputs its genuine still-hidden X_(a,i,y_i), giving H. Thus in an accepting execution without H or G every used WOTS key must have been exposed.

**PROVED (exposed WOTS key).** At an exposed key, the legitimately known suffix threshold is e_i. Without H, a genuine chain input at y_i cannot have y_i < e_i. Hence y_i >= e_i for every chain. Acceptance gives sum y_i = sum e_i = S, forcing y=e. This implies equality of the entire 128-bit type-7 prefix because the fixed parameter set has no omitted WOTS digits. If the forged child/counter payload differs from (V_a,c_a), its type-7 evaluation is D7. In the absence of D7 the forged child is exactly V_a and the counter exactly c_a.

**PROVED (hypertree descent).** Acceptance fixes the final top root to the public key. Apply the Merkle and WOTS steps at the top address. With none of H,G,D7, the input child of that WOTS certificate is the genuine uniquely addressed layer-3 subtree root. Continue downward through the same route. At layer 0 this pins the reconstructed FORS public key to its genuine type-4 image. The fact that verification calculates bottom-up does not affect this logical backward implication.

**PROVED (FORS descent).** Absence of G at type-4 roots compression forces its 17-root tuple to be designated. Apply the ordered-pair path argument independently to each real tree. Each supplied secret hashes to its genuine leaf image. A different secret causing that image is G; a genuine unexposed secret causing it is H. Therefore without H or G every supplied leaf secret was previously exposed at its own selected coordinate. The verifier checks the forced omitted-index zero condition. All selected real indices are covered at the chosen bucket, giving C.

**PROVED (classification).** On nonzero-seed HJ executions,

    accepting fresh forgery => C OR H OR G OR D7.

This classification includes arbitrary forged R/c, every path and every chain value, unvisited subtrees, known numeric values copied to other addresses, and same-vector child substitutions. It does not need a canonical counter at every unqueried key. Existence is needed only for completed genuine exposures.

## 4. Independent event bound interfaces

**PROVED (H interface, prior independent result).** A continued input-oblivious comparison oracle, with predictable suffix-closed exposure and old replies retained, gives

    Pr_HJ[H] <= min(1,(Q_H+3017)/2^128).

The source-programmed ordinary HJ and comparison experiment agree until the first hidden hit. Hidden coordinates are uniform in the unflagged comparison history, NOT conditional on REAL no-hit histories. Extra advice can include endpoints, FORS leaf images and public nodes; it cannot include secret/interior chain payloads.

**PROVED (G interface, prior independent result).** The full honest graph may be granted to an enlarged adversary for this event alone. It preserves the ordinary-O marginal and leaves residual alternative-input outputs iid conditional on graph and independent outside-function tables. Projection to an adversary ignoring advice gives

    Pr_HJ[G] <= min(1,(Q_H+3217)/2^128).

No full graph payloads are subsequently given to the H adversary. Separate augmented event experiments project to the same unaugmented ordinary HJ; their advice views do not define a common stronger hidden-value game.

**PROVED (independent D7 sampler argument).** Conditional on the honest graph, each WOTS type-7 restriction has fixed child V_a independent of that restriction. Let A be its accepted full-prefix slice. Sample c_a as the first success over its finite counter plane, or undefined if none. Conditional on c_a and e_a, earlier counter prefixes at V_a are uniformly rejected; the canonical point is designated; later counters and every different-child input retain independent uniform full images. Full unused tails are sampled consistently. This is exactly the ordinary random-function distribution disintegrated by first-accepted metadata. One can grant all such canonical metadata to the enlarged adversary, including undefined status, without granting hidden graph payloads to the separate H game.

At a fresh alternative type-7 point, a prefix from the rejected predecessor plane cannot equal accepted e_a; any other residual prefix matches it with probability 2^-128. The designated point is excluded. A previously queried alternative equality was already an event at its first evaluation. This handles prequeries and first-accepted selection without treating the canonical target as an unconditional uniformly chosen 128-bit value. The target itself is uniform on A, but the relevant fresh residual reply is uniform on all prefixes (or rejected and harmless).

**PROVED (D7 candidate bound).** Final verification uses at most five type-7 calls, so the enlarged event yields Pr_HJ[D7] <= min(1,(Q_H+5)/2^128). This prospective bound must be checked against the new canonical-target lane; no peer proof was used to derive it here.

**PROVED (safe simple union interface).** If a source-bound C term U_C is proved on this same ordinary HJ game, then the above classification gives

    Adv_HJ <= min(1,U_C + (3*Q_H+6239)/2^128),
    6239 = 3017+3217+5.

**PROVED (joint G/D7 candidate sharpening).** The same enlarged experiment can grant the full honest graph plus the above type-7 canonical metadata when bounding G OR D7. Conditional on this advice, a raw full address belongs to exactly one graph or type-7 restriction. Alternative outputs are iid uniform, or rejected prefixes which cannot hit an accepted type-7 target. All known designated points are excluded. Hence public queries contribute at most Q_H/2^128 and final-verifier calls contribute (3217+5)/2^128, giving

    Pr_HJ[G OR D7] <= min(1,(Q_H+3222)/2^128),
    Adv_HJ <= min(1,U_C + (2*Q_H+6239)/2^128).

This uses one G/D7 event sampler, not expected query counts from different hybrids. H remains a separately projected event with weaker advice. The sharpening is a new independent composition derivation and awaits cross-check.

**OPEN (C/source bridge and unconditional loss binding at this save point).** The actual source C bound must be read and verified, including deterministic Q_H+1 candidate padding, finite outer counter search, raw alias exclusions, fresh messages with arbitrary R, retained earlier E queries and one extra final draw. The real-to-HJ loss must also be read and bound to the same unconditioned game. Zero-seed charges cannot be informally subtracted from two unconditional triangle bounds. Until that inspection, no complete real-source scalar total is claimed in this file.

**Status: INDEPENDENT_CLASSIFICATION_AND_CANDIDATE_COMPOSITION_SAVED.** Ready to read accepted component lanes and the root candidate.

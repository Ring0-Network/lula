# Independent classical accepted-forgery classification

Saved before reading the root composition draft or numeric composition reports. Scope: deterministic event classification and the experiment obligations needed to combine separate classical statistical lemmas. Complete concrete-SHA, QROM, side-channel and source-totality security are not asserted.

## Pinned subject and game

Source: `publications/LULA-I/release/code/lula1/src/lib.rs`, SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Parameter driver SHA256 `a18799fba64ec1a6370e18e0d5d4b21108109cf9022fc8d7195e55d860a08c4b`, line 9: FORS k=18,a=9,forced-last-index-zero; heights [5,5,5,5,21], four radix-16/sum-240 WOTS layers and one radix-256/sum-2040 layer, all z=0.

Define HJ as the ordinary ideal game after a separately valid joint F/J hop: private derivations and message randomness use independent full32 maps; public addressed hashes use a classical complete-output RO. Work on nonzero public seed S and honest cache/opaque snapshots. The adversary receives public keys and completed signatures, has at most Q_H public raw RO evaluations (including prequeries), and submits one candidate on a message not previously returned by Sign. Intermediate signature buffers, caches containing secrets, seed fixture contents, internal hashes and timing are not disclosed. Initiated and completed signing counts must be distinguished when specifying the hop and coverage budgets. Completed honest signatures at a WOTS address expose one fixed canonical digit vector and its suffix positions; repetitions expose the same values.

PROVED (source): `verify` 672–674 accepts only exact public-root equality. `verify_root` alone 679–729 returns an implied root and is not this acceptance predicate. Signature lengths are checked at 680–682. The 17 actual FORS trees follow `real_trees` 341–343; verifier checks the dropped eighteenth index equals zero at 701–705. The candidate's R and outer counter are unrestricted serialized choices; no canonical source-counter requirement is checked there.

## Four events in the same HJ execution

* COVER: the candidate's routed bottom FORS address has, separately for every j=0,...,16, its candidate leaf index among indices disclosed by completed honest signatures at that same address. All 17 can come from different signatures. This is an index-coverage event, not a claim that the candidate signature is identical to an old signature or message.
* HID: a charged public raw call or final verification call to a protected chain-position/type0 or FORS-leaf/type3 point uses the genuine designated input while that coordinate is still undisclosed. Coordinate identity and monotone exposure matter: a numerical duplicate at another address does not make this coordinate disclosed. Initially all WOTS endpoints are public; an exposed canonical signature makes each chain suffix from its canonical digit onwards known. Selected FORS secrets are exposed on completed calls.
* ALT04: a charged raw call or final verification call at a type0,1,2,3,4 address has an input different from that address's designated honest graph input but returns its designated 128-bit image. One address gives one target; events do not compare against every image globally.
* CAN7: a charged raw call or final verification call at an exposed WOTS address uses child/counter different from that address's honest fixed child/first accepted counter, yet returns the same full 128-bit digit digest. Exposed keys necessarily have a canonical counter; no canonical counter is assumed for an unexposed key.

The larger Bad7 event that grants all successful canonical targets at the beginning contains CAN7. Failed rows have no target and cannot be exposed by a completed honest signature.

## Backward classification from the accepted top root

PROVED pointwise, without probabilities: outside HID, ALT04 and CAN7, every accepted candidate satisfies COVER.

1. Fix the candidate's 41-bit route I. Source `tree_leaf` 470–475 gives at layer j: leaf=(I>>b_j) mod 2^h_j and tree=I>>(b_j+h_j), where b_j is the sum of lower heights. Therefore the upper address's fixed child subtree is exactly the lower layer's verifier-route subtree: `(tree_j<<h_j)|leaf_j = tree_(j-1)` for j>0. This is a same-route argument, not a requirement that the candidate uses any previous message route.
2. At the top, equality to pk_root fixes the honest target output at the highest type2 address. Traverse the candidate authentication path backward, using the same ordered child concatenation and address schedule as `Subtree::build` 291–307 and `root_from_path` 322–329. If any payload differs while its parent output equals the target, ALT04 occurs. Otherwise equality of concatenations forces the on-path child and sibling to be the honest values. Induction reaches the honest WOTS public-key leaf.
3. Type1 endpoint compression 251–262 and 269–276 then either produces ALT04 or forces every candidate chain endpoint to equal its honest endpoint.
4. For each chain, traverse backward from endpoint position w-1 to its candidate digit y_i. The verifier hashes at exactly position-specific type0 domains 239–245 and 269–274. Any differing input producing the designated next-position output is ALT04. Otherwise the supplied chain value is the genuine X_(y_i). If y_i=w-1, it is the already public endpoint and no hash was needed; lower positions are protected coordinates.
5. If this WOTS address is unexposed, every position below w-1 is still hidden. Since the accepted sum S is strictly smaller than l(w-1), at least one y_i<w-1. The final verifier must hash at that point, yielding HID. This does not assume that an unexposed address has any first accepted counter.
6. If the address is exposed, let e be its fixed canonical digit vector. Absence of HID forces y_i>=e_i for every i because precisely those suffix coordinates are known. Both accepted vectors have sum S, so sum(y-e)=0 with nonnegative coordinates forces y=e. For lw=4 or8 all 128 digest bits are consumed (222–227); equality of digit vectors therefore means equality of the full128 digest. If candidate child/counter differs, the verifier's type7 call 720 is CAN7. Otherwise the candidate child equals the honest fixed child.
7. Apply steps 2–6 at every layer, descending from layer4 to0. The child equality at an upper exposed key supplies exactly the honest lower-subtree root required by step1. At layer0 it supplies the honest fixed FORS public key.
8. At FORS type4 compression 371–376 / 396–412, absence of ALT04 forces all 17 candidate tree roots to equal honest roots. Traverse each nine-step global-index authentication path backward (344–368 versus403–408); absence of ALT04 fixes the selected honest leaf image. At height0 either the supplied input differs (ALT04), or it is the genuine selected FORS secret. If that coordinate was not disclosed by a completed same-address signature, the final leaf hash at403 yields HID. Consequently every one of the 17 selected coordinates was disclosed, which is COVER.

Numerical collisions between honest values at different positions/addresses do not invalidate this logic: equality is literal at the designated address. Guessing a still-hidden designated input, even by copying another known equal value, is HID. An alternate-input image equality at the proper address is ALT04. Concatenation is fixed-width and injective. The fixed tree schedule cannot be replaced by an arbitrary user-supplied leaf or hash address.

## Exact resource counts and source restrictions

COMPUTED from the fixed acceptance sums:

| Final verification family | Maximum calls |
|---|---:|
| WOTS type0 chains | 4*(32*15-240)+(16*255-2040)=3000 |
| WOTS type1 endpoint compression | 5 |
| Merkle type2 | 4*5+21=41 |
| FORS type3 leaves | 17 |
| FORS type3 internal nodes | 17*9=153 |
| FORS type4 root compression | 1 |
| Total types0–4 | 3217 |
| Protected hidden-input points | 3000+17=3017 |
| Type7 WOTS digest | 5 |
| Message inner/outer | 2 |
| Complete hash calls, all above | 3224 |

These are calls, not compression counts, CPU cycles, timings or signature capacity. Early rejection lowers the maxima. No degree/graph-node multiplier is introduced by the literal addressed-event budgets. Honest source construction queries designated types0–4 points only. Honest canonical grinding queries rejected earlier type7 rows and the target, never a free residual row. Corrupt accepted cache counters or manipulated roots invalidate that canonical-exposure invariant and are outside scope (648–655 checks acceptance, not minimality or root integrity).

## Common-game projection obligations

PROVED classification is in one ordinary HJ run. For a union bound, each separate statistical lemma must bound the probability of its corresponding HJ event, possibly through a valid coupling; its disclosure augmentation need not be the same augmented experiment as another lemma.

* ALT04 can use an event-only full designated-graph view. It does not imply that those graph payloads can be added to the real signing transcript without leaking hidden values.
* HID requires a distinct hidden-value ghost coupling and predictable disclosures. Equality of the HJ and ghost transcripts until HID and retention of previously answered conflicting raw points after HID must be shown; merely asserting independence conditional on no hit is invalid.
* CAN7 is contained in the all-targets Bad7 event, whose full-output conditional first-accepted-row sampler handles prequeries and explicit failed rows. No free residual type7 outputs may be supplied by the honest source interface.
* COVER remains a message-digest/index process in HJ. Deterministic classification does not prove the adaptive coverage probability. The source-to-coverage bridge must count all eligible outer trials, repeated U/candidate handling, adaptive inner trials, secret-R repeats/collisions and candidate-final verification. Those are separate from the typed graph event lemmas.

ASSUMED/OPEN until reviewed against the actual common-game construction: source totality/partial execution interface, the joint F/J hop with exact initiated-call budget, and the adaptive coverage bridge. Any claim of a complete bound must cite those actual lemmas instead of silently replacing HJ by independently sampled experiments. The classification itself has no missing canonical-existence premise.

For the nonzero-S branch, event bounds are pointwise in S; no division by Pr[S!=0] is needed. The S=0 event has probability 2^-128 for uniform seed and must be charged **once** in the initial game hop/branch, with the REAL marginal retained there. Adding +2^-128 to every local lemma double-counts that exceptional event and obscures the game.

No generic successful-OS-execution conditioning is used. If key generation is conditioned solely on all top canonical rows existing, that is metadata-only conditioning and the residual typed-event laws remain unchanged; the overall seed/coverage/secret-R experiment must still state its own marginal and interface. Mathematical readiness is not an arbitrary OS termination assertion.

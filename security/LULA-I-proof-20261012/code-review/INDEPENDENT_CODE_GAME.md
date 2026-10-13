# Independent code-bound game and reduction audit

Status: **OPEN complete-signature bound; PROVED honest-cache transcript equivalence in the declared mathematical interface; COMPUTED source counts and native controls.** This derivation was written before reading other agents' new proofs or numerical reports. It changes no implementation or manuscript. It uses no new timing measurements or full-size cache construction.

## 1. Fixed executable object and binding

**COMPUTED.** `SOURCE_AND_COUNTS.json`, produced by `python -I -B derive_counts.py`, binds three library copies and the current manuscript. Original and private-library SHA-256 are `c5b16f35ec9e3a826e5d8100dbbc4d3a8287e3e52fd567a24e95f03bb7243ab5`; release-library SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. The only difference is the first documentation-comment block. From `use sha2::digest` onward their LF-normalized bodies share SHA-256 `e4cadabc50975580725a46eef0d2ade4fa06bdfc408f5b9c08a36dbb1e5c32c3`. Anchors below refer to release `code/lula1/src/lib.rs`; the same line numbering applies to original/private bodies.

**PROVED (source derivation).** The fixed harness parameter string at `src/bin/lula1_snapshot.rs:9` is `18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1`. Thus only layer 4 is cached. `Params::sig_bytes` at 439–446 gives 5,720 bytes. Top cache payload is 75,497,456 bytes. Each layer contributes 596 signature bytes, despite the different top width and height.

**ASSUMED.** For the cryptographic game, sample all 48 seed bytes uniformly and secretly. `Signer::keygen` at 498–508 receives caller-supplied seed bytes; it does not supply randomness. Fixed benchmark fixture seeds do not instantiate secure key generation.

**OPEN (interface).** Both searches use `u32` counters and `ctr += 1` (228–236, 608–616). Release arithmetic can wrap; debug builds can panic. If every counter fails, release searches can loop forever. The game below treats the reference as a partial deterministic algorithm and a nonterminating call as having no completed response. To claim totality or explicit failure semantics, add a finite-search failure contract and account for its probability. This audit does not edit it.

## 2. Exact EUF-CMA experiment

**PROVED (definition/source binding).** Define the fixed-parameter reference `Sign°(sk,m)` by `s.sign(m,false)`, with no `bind_digest_to` call. Sample seed, execute key generation, publish `(pk_seed,root)` and retain signer context. A may query raw byte strings adaptively at most q times. The oracle returns only a completed reference signature. A outputs `(m*,sigma*)`; it wins exactly when `m*` is bytewise unequal to every earlier queried message and `verify(p,pk_seed,root,m*,sigma*) == true`. The code's root-equality wrapper is at 672–674, not merely `verify_root` returning some root. A nonterminating signing call prevents further completed interaction. State the setup completion convention separately; do not silently condition on successful setup without charging or defining that conditioning.

**PROVED.** This is ordinary EUF-CMA, not strong unforgeability: a second valid signature on a previously queried message is not a win. It is the exact raw-message interface: no standardized context, prehash mode, application tag, or separate digest API is inserted.

**PROVED.** A can choose every serialized signature byte. At 679–730 verification enforces exact length, the FORS forced-index condition, each WOTS target-sum condition, and final root equality. It does not enforce a secretly derived randomizer, minimal FORS counter, or minimal WOTS counters.

| Adversarial field | Bytes / offsets | Code-enforced restriction |
|---|---:|---|
| Raw message m* | arbitrary bytes | freshness against actual queried messages |
| R | 16, offset 0 | none; it is input to H_msg |
| FORS counter | 4, offset 16 | resulting omitted index must be zero; minimality untested |
| 17 FORS revealed values | 17 × 16, within offset 20–2739 | transformed into leaves; no secret-origin check |
| 17 FORS authentication paths | 17 × 9 × 16, same region | reconstructed roots feed FORS-root compression |
| WOTS counter at layer i | 4, offset 2740+596i | digest must meet target-sum predicate; minimality untested |
| Lower WOTS chain values | 32 × 16 per layer 0–3 | complete addressed chains and compress endpoints |
| Top WOTS chain values | 16 × 16 at layer 4 | same rule with width 256 |
| Lower authentication paths | 5 × 16 per layer 0–3 | derive next root |
| Top authentication path | 21 × 16 | final reconstructed root equals public root |

The claimed root, public seed, and fixed parameters are experiment inputs, not extra signature fields controlled by A.

## 3. Oracle inputs and domain separation

**PROVED (serialization).** Write `B = pk_seed || 0^48`, `AD(j,t,type,kp,u,v)` for the 22-byte encoding at 69–95, and `Tr16` for the first 16 hash-output bytes. All integer fields are big-endian within cryptographic inputs. `Ctx::th` implements `Tr16 SHA256(B||AD||input)` with normal SHA-256 padding (121–147).

| Primitive / call | Exact input to SHA-256 | Output | Source |
|---|---|---:|---|
| WOTS secret PRF | B || AD(j,t,5,kp,chain,0) || sk_seed | 16 | 161–163, 248–250 |
| FORS secret PRF | B || AD(0,t,6,kp,0,g) || sk_seed | 16 | 348–350, 391 |
| WOTS chain F | B || AD(j,t,0,kp,chain,position) || chain_value | 16 | 239–245 |
| WOTS PK T_l | B || AD(j,t,1,kp,0,0) || concatenated endpoints | 16 | 251–256 |
| Hypertree H | B || AD(j,t,2,0,height,index) || left || right | 16 | 291–306, 322–330 |
| FORS leaf F | B || AD(0,t,3,kp,0,g) || secret | 16 | 348–351, 402–404 |
| FORS internal H | B || AD(0,t,3,kp,height,global_index) || left || right | 16 | 359–365, 405–409 |
| FORS root T | B || AD(0,t,4,kp,0,0) || 17 roots | 16 | 370–376 |
| WOTS message hash | B || AD(j,t,7,kp,0,0) || child_value || BE32(counter) | 16 | 216–220 |
| PRF_msg | sk_prf || pk_seed || raw message | 16 | 164–168 |
| H_msg inner | R || pk_seed || pk_root || raw message | 32 | 170–172 |
| H_msg outer | inner_digest || BE32(counter) || pk_seed | 32 | 174–187 |

**PROVED (restricted domain property).** Types 0–7 distinguish the addressed construction families. Fixed layer numbers 0–4 fit the one-byte layer field. The tree, keypair, chain/height, and position/index ranges for this parameter set fit their fields. FORS leaf calls have height zero and 16-byte inputs, internal nodes have height ≥1 and 32-byte inputs. FORS global indices `j*2^(a-height)+local` distinguish the 17 trees at each height. Hypertree `T_TREE` keypair stays zero while WOTS domains include the leaf keypair. Recomputing the *same* node or chain step repeats the same address deliberately.

**OPEN / false requested universal assertion.** It is false that every pair of distinct call sites has a distinct address or distinct function family. Build and verification deliberately hash identical nodes at identical addresses. `PRF` and chain F both delegate to `th`, with separation provided by type, not distinct independent code functions. More substantially, `PRF_msg`, H_msg inner and H_msg outer have no literal function tags. They all use SHA-256, and their input languages are not disjoint. For example, for `R=sk_prf` and `m0=pk_root||m1`, the PRF_msg input on m0 is exactly the H_msg-inner input on `(R,m1)`. This is a structural overlap counterexample, not a demonstrated attack: R needs to equal the unknown secret. Adversarially finding that equality needs a probability bound. Independent random functions per *name* do not directly model this implementation. The smallest missing lemma is a single-oracle input-encoding/bad-overlap hybrid, including secret-input guesses and variable message lengths. Alternatively explicit tags would define a different construction, which is outside this audit.

**ASSUMED / OPEN.** SHA-256 as a random oracle is a modeling assumption. Treating PRF_msg as a decisional PRF is an additional assumption or a derived secret-prefix-RO lemma; it is not HMAC and no standard-HMAC theorem applies by syntax. The derived-key PRF is keyed by `sk_seed` as a suffix, with public `pk_seed` and address prefix. Its secret entropy is 128 bits, not 384; `sk_prf` is a separate 128-bit secret. The type-5 and type-6 output vectors share one keyed family and can be covered by one correctly defined multi-query PRF hybrid. Exact independence of deterministic R from every observation is false literally: signatures expose R, repeats reproduce it, and distinct inputs can collide. In a PRF hybrid, fresh distinct-message outputs may be independent uniform *before their revelation*; a reduction must handle previously revealed outputs, adversarial oracle guesses and collisions.

## 4. Explicit signing sequence

**PROVED (source flow).** On m, execute PRF_msg once, H_msg inner once, and H_msg outer at counters 0 through the first accepted forced-index counter. Extract the 17 real indices from bits 0–152, require bits 153–161 zero, and route index I from bits 162–202. For each of the 17 FORS trees, build 512 PRF-derived leaves and 511 internal nodes, rederive the selected secret, append its nine-node path, and compress the 17 roots. For layer 0 through 4, derive `(tree,leaf)` by `tree_leaf`; choose the canonical WOTS message counter by grinding or read its honest precomputed counterpart. Build the subtree or read the honest cached top subtree. Recheck the chosen counter's target-sum predicate. Derive each chain start, advance to the digest digit, append counter/chain values/path, and set current child value to the subtree root. Code anchors: `tree_leaf` 470–476; `sign` 601–668; FORS 383–394; key preparation 498–584.

**PROVED.** Verification does not recompute any private chain start or require the canonical counter. It derives an implied bottom FORS PK from arbitrary signature evidence, then derives each next subtree root from arbitrary chain values and paths. Therefore a proof cannot model the verifier's child values as necessarily honest. Honest *signing* child values are fixed; adversarial *verification* child values can differ, and that is exactly what WOTS certification must bind.

## 5. Address namespace, PRF query counts, and repeated WOTS use

**COMPUTED.** Each address below is `(layer,tree,keypair)`, not merely a leaf coordinate local to one tree. The complete namespace counts are symbolic; no enormous forest was materialized.

| Layer | Height | Number of subtrees | WOTS keys | Chain starts | Merkle nodes per tree | All Merkle nodes |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 5 | 68,719,476,736 | 2,199,023,255,552 | 70,368,744,177,664 | 63 | 4,329,327,034,368 |
| 1 | 5 | 2,147,483,648 | 68,719,476,736 | 2,199,023,255,552 | 63 | 135,291,469,824 |
| 2 | 5 | 67,108,864 | 2,147,483,648 | 68,719,476,736 | 63 | 4,227,858,432 |
| 3 | 5 | 2,097,152 | 67,108,864 | 2,147,483,648 | 63 | 132,120,576 |
| 4 | 21 | 1 | 2,097,152 | 33,554,432 | 4,194,303 | 4,194,303 |

FORS instances: 2^41. Real FORS secret locations per instance: 17×512 = 8,704; all instances have 19,140,298,416,324,608 such locations. All WOTS chain-start locations total 72,638,667,948,032. Combined secret-PRF location namespace: **19,212,937,084,272,640**. Internal Merkle-node queries are public hash queries, not PRF queries; do not include them in the PRF query count unless the reduction itself additionally queries a PRF there.

**COMPUTED.** Source invocation counts:

| Operation | PRF invocations | Distinct secret-PRF addresses within that operation |
|---|---:|---:|
| No-cache minimum keygen | 33,554,432 | 33,554,432 |
| Prepared top-cache keygen | 2,181,038,080 | 2,181,038,080 |
| Prepared full signature | 12,961 | at most 12,816 |
| Uncached full signature | 33,567,393 | at most 33,567,232 |

Prepared-sign counts equal `17(512+1)+4(32×32+32)+16`. Uncached adds all top starts `2^21×16`. Signing recomputes chain starts already used for PK construction, hence invocation and distinct-location counts differ. A PRF replacement may memoize by address and preserve deterministic repeated values. For q reference signing queries, a safe invocation upper bound is `33,554,432 + q×33,567,393` after minimum keygen; prepared setup uses `2,181,038,080 + q×12,961` instead. A distinct-query bound is also capped by the complete namespace count. PRF_msg has ≤q distinct message queries. These are source counts, not independently proved security loss constants; the final reduction must state which simulator queries it needs beyond honest execution.

**PROVED (same-value lemma).** For every fixed key and WOTS address `(j,t,kp)`, honest signing always signs the same 16-byte value. For j=0 it is the full deterministic FORS public key at `(t,kp)`, independent of the selected FORS indices. `Fors::sign` builds all real trees and `roots_pk` uses their fixed roots (383–394). For j>0 it is root of child tree `(j−1,(t<<h_j)|kp)`, as `child_value` specifies (486–496). The root is fixed by the secret seed and address. Reference counter selection always starts at zero. Thus every repeated use reveals the same digit vector, chain values and counter at *all five layers*, including the bottom layer. Honest-cache restoration preserves this statement.

**OPEN / incorrect requested model.** A random local leaf in `2^h_j` does not define a complete WOTS address. Under an ideal uniform route, the marginal complete-address spaces are 2^41, 2^36, 2^31, 2^26, 2^21 from bottom to top. Repeated complete-address occupancy is real, but different honest WOTS messages at an address have probability zero, not a Poisson probability of two exposures. Therefore the proposed `Pr[key used ≥2] × Pr[two-vector target-sum forgery]` describes a different signing oracle. H1's different-vector model cannot be substituted into an honest LULA bound. A same-value lemma avoids that particular attack; it does **not** prove WOTS unforgeability.

**PROVED (combinatorial fact).** If y≥x coordinatewise and both have sum S, then sum(y−x)=0 with every term nonnegative, hence y=x. This proves an antichain property only. A fresh child value V* and chosen counter c* can hash to the already exposed vector x; that needs message-digest target-preimage/TCR accounting even without a different chain vector. A forged non-forward chain value needs addressed chain preimage/second-preimage accounting; changed endpoints compressed to the same WOTS PK need a type-1 collision/second-preimage event. A complete WOTS lemma must include all three cases, multiple target keys, adaptivity, the free counter, and reduction costs. The loss `w×ell` is not established here merely by the antichain argument.

## 6. FORS forced tree correction

**PROVED.** The signer and verifier enforce that the eighteenth digest index is zero (609–615, 701–704). `Fors::real_trees` returns `k−1=17` (341–345); only j=0 through 16 are built and signed (347–368, 383–394), and root compression covers only those 17 roots. No eighteenth secret exists in this instantiation. Therefore the objective's sentence “any signature reveals leaf zero of the last tree” is false. Correct lemma: a valid signature's hash digest satisfies the omitted-index condition; the remaining indices select revealed secrets in 17 real trees. The forced-bit condition contributes a 2^-9 trial-acceptance factor in an ideal uniform outer-hash model; this is not evidence for an implicit transmitted secret.

**ASSUMED / OPEN.** The supplied coverage formula is an idealized expected transcript-coverage probability for a random trial and independently distributed occupancy/indices. Its source correctness, finite-q exactness, adaptive signing behavior, adversarial R/ctr choices, hash-query allocation, and tree/leaf replacement events must be justified in the full game. A count of expected covered leaves is not itself the complete signature reduction. This code audit does not reproduce a numerical FORS bound or turn per-trial work exponents into absolute EUF-CMA advantages.

## 7. Exhaustive certification-tree split

**PROVED (structural lemma, no numerical bound).** Fix the entire mathematical honest key graph from the secret seed, even at addresses never visited by signing. Reconstruct the adversarial top path. If its reconstructed root equals the public root, compare its ordered child pair at the top node to the honest pair at the same address. If the pair differs but hashes to that root, obtain an equal-output/different-input collision or second-preimage witness at that addressed type-2 function. If the pair is equal, descend toward the reconstructed leaf. At each level either obtain such a witness or descend through a child equal to its honest counterpart. Thus either a addressed internal-hash witness exists, or the reconstructed leaf equals the honest WOTS PK at the routed address. This does not require a previous honest signature at that route.

**PROVED (next decomposition).** Once a reconstructed WOTS PK equals its honest value, compare compressed endpoint strings. Unequal endpoint strings with equal PK give a type-1 equal-output/different-input witness. Equal endpoints force analysis of the chain values and addressed chain paths. If these are honest reachable suffixes, the antichain property restricts the accepted vector to an exposed vector when there is an exposure. A new child value producing that vector gives a type-7 digest target event; an unexposed key or non-forward chain value requires a chain/secret-derivation event. If the child value equals its honest value, descend to the next layer and repeat. At the bottom, analyze FORS-root compression and the 17 addressed FORS trees analogously, then separate covered-index signatures from new secret/leaf witnesses and message-hash routing events.

**OPEN (reduction obligation).** The proposed dichotomy “shares a full path with an honest signature or has a first divergent node” is not sufficient as a reduction to an *observed signature*: a valid forgery may route through a previously unsigned honest leaf. Comparison must be to the complete honest key graph, with oracle programming and the cost of generating or lazily committing graph nodes specified. Changing one lower root can be certified by adversarial WOTS evidence; treating every intermediate verifier root as honest would skip this case. The structural split above is exhaustive, but a simulator able to extract an SPR/TCR challenge at the right address with the stated time and query loss has not been constructed. Union-bounding all conceptual nodes without accounting for chosen targets and reduction effort can give enormous or vacuous losses. Count nodes explicitly, but do not automatically multiply a generic SPR advantage by all of them and call the proof complete.

## 8. Cache semantics and smallest native controls

**PROVED (honest transfer).** For the fixed successfully generated key, a full honest top cache stores precisely the deterministic top subtree and the first accepted counter for each fixed child value. Message randomization/routing and FORS do not consult it. At each layer, prepared or absent computation therefore has identical child values, counters, chain values and authentication paths. Honest old snapshots are unchanged copies: `sign(&self,...)` has no mutable cache writes. Successful preparation proves the top canonical counter exists. All uncached searches otherwise coincide, so termination and completed bytes agree. An atomic snapshot/restore simulator can retain handles locally and answer every signing request with the reference oracle. It changes neither queried messages nor completed signatures; it needs exactly the same q signing queries. **Transfer probability loss δ=0 in that interface**, with bookkeeping/time overhead to be stated separately. This transfers an applicable reference bound; it supplies none itself.

**PROVED / false universal corruption assertion.** `sign` reads cached subtree, root, path and counter without checking a node against the public root (637–641). It checks only `w.accept(digits(digest(...counter)))` (647–655). A rejected cached counter is replaced by the canonical search. A different accepted counter is retained even if nonminimal. No path authentication or outgoing full-signature verification occurs before return. A malformed container can index out of bounds/panic; no general abort-or-recompute result is implemented.

**COMPUTED (actual library miniature, widths unchanged).** `toy-cache-control/src/main.rs` imports the unmodified release library and uses actual WOTS widths/chain counts/sums, two height-one layers and tiny FORS. `cargo run --release --offline --manifest-path toy-cache-control/Cargo.toml --target-dir toy-cache-control/target` returned code 0. The counter was 643 canonically; another accepted counter 2377 produced different signature bytes accepted for the same message. An invalid counter regenerated the exact original bytes. Flipping a used cached sibling returned a different signature rejected by Verify. Flipping the cached top-root entry alone did not change signature bytes: that root is only assigned to the final unused `cur`. These are discriminating native controls, not a fresh-message forgery, full-parameter benchmark, or cryptanalytic security result.

**OPEN / corrected cache theorem.** Universal transparency for arbitrary cache writes is false. Cache bytes are secret-key-derived public-key objects, not shown efficiently computable from the 32-byte public key. In particular the public root does not provide all its Merkle leaves or paths, and top counters depend on child roots not included in the public key. They may be intended as nonsecret auxiliary data, but that requires an auxiliary-information game and simulation lemma. “Recomputable” means recomputable with the secret key; it does not mean recomputable from pk. Honest atomic rollback security needs neither a public cache-recovery algorithm nor a claim that exposing cache bytes is harmless, because the original interface does not expose them. A stronger cache-exposure theorem needs to reveal the exact payload, compare it to public transcripts, and prove the missing auxiliary-information lemma.

**PROVED (harness distinction).** Snapshot harness `lula1_snapshot.rs:42–54` additionally writes all 48 seed bytes and the public root into its private fixture before the cache. Loading at 59–89 checks shape/magic and installs root/nodes/counters; it does not authenticate their cryptographic correctness. That private measurement fixture is not a safe public-cache artifact and is distinct from the 75,497,456-byte payload. Reading the whole fixture grants the secret key outright. The public release intentionally excludes such fixture files. Any formal cache-exposure model must exclude the seed header or acknowledge trivial key compromise.

## 9. Minimal missing lemmas and verdict

1. **OPEN — shared-hash domains:** single-RO encoding/bad-overlap bound for PRF_msg and H_msg, rather than assuming independent names where encoded strings can overlap.
2. **OPEN — secret derivation:** correctly keyed multi-query PRF/secret-prefix-RO reductions with source-bound query counts, repeated-address consistency and secret-query guessing.
3. **OPEN — routing and coverage:** adaptive R/ctr outer-hash sampling and FORS coverage reduction including free forgery fields, plus addressed leaf/tree/root collision terms.
4. **OPEN — WOTS certification:** one-fixed-child-value-per-key security including digest target events, chain inversion and endpoint-compression binding; a two-distinct-vector reuse formula is not that lemma.
5. **OPEN — tree extraction:** programmable/lazy honest-graph simulator with challenge selection, exhaustive lower-root substitution cases and explicit losses/time.
6. **OPEN — composition:** actual H0…Hm programs and extraction reductions for this exact verifier; no sum of open component terms is asserted here.
7. **OPEN — stronger cache interface:** authenticated/canonical corruption handling is absent; public-cache exposure requires a separate auxiliary-information lemma and cannot reveal the benchmark seed header.
8. **OPEN — totality/QROM:** finite search semantics, quantum-access model and exact applicable QROM theorems are not provided by this source audit.

**PROVED / COMPUTED final conclusion.** Honest deterministic restoration does not multiply WOTS digest exposures. Arbitrary accepted-counter corruption can do so. The manuscript already distinguishes these interfaces and already states the omitted FORS-tree semantics correctly. The new objective overstates both. The complete classical 128-bit EUF-CMA bound, signing capacity certified by such a bound, and a QROM category-1 reduction are **not established by this audit**. The largest structural correction is to replace the proposed WOTS occupancy-reuse term with the same-fixed-value certification lemma and its still-open concrete security bound. Do not modify the construction or the manuscript to manufacture closure.

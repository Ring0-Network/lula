# Exact top-cache payload: separate observer-view extension

Saved from the pinned source and the already reviewed component theorems, before reading any new cache-payload source/root/peer report. No operational forgery, signing implementation, cache generation or timing experiment is constructed here.

## 1. Object and status

**COMPUTED — source binding.** Release library SHA256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Source keygen 500–583, `compute_subtree` 479 onward, `child_value` 487 onward, and Subtree 283–323 determine the object below. The fixed top layer has height21, width256, length16, target2040 and 2^21 key pairs. Its cache consists of one level-major top Subtree and one counter vector. Its mathematical payload is

    L = (all 2^22−1 top Merkle nodes, all 2^21 first-accepted counters).

The leaf-level nodes are compressed WOTS public keys, not chain starts or signature blocks. A top counter is the first acceptable digest counter for its fixed layer3 child-subtree root. The payload size is 16(2^22−1)+4(2^21)=75,497,456 bytes. This definition excludes a secret seed, context, private-map table, fixture header, partial computation, duration, cache file metadata and any lower-layer cache.

**ASSUMED — new interface.** Extend the reviewed source game solely by supplying L as a classical setup response after successful cryptographic top-row completion; if setup does not complete, no payload or public key response is emitted and the branch is absorbing/nonwinning. Classical atomic signing, consistent opaque restoration, bounded raw oracle access and the single-root source verifier otherwise remain unchanged. The disclosure does not count as an adversarial hash query. Keys and oracle tables are sampled before pre-key queries, as in the reviewed game. No successful-completion conditioning is used.

**PROVED — manual mathematical candidate, independent review required.** In this exact extension the reviewed classical RO, conservative finite-QROM and event-specific finite-QROM upper formulas remain valid with no extra additive exposure loss. The argument is a separate extension of every component's observer interface; it is not an implication from the opaque-cache theorem alone. The component samplers and query bounds are inherited from the already reviewed mathematical theorems. This file proves compatibility of L with their sufficient hypotheses, not a fresh efficient primitive reduction or a checked Rust refinement.

## 2. Exact joint sampler; counters are not independent of all public data

**PROVED — source dependency.** Top WOTS PKs are computed by complete chains, independent of a message digest or counter. Top Merkle images are their addressed tree DAG. The child V_A for a top key A is a layer3 subtree root; the layer3 subtree is also built from complete WOTS PKs. These values are determined by private F and designated types0–4, independently of the type7 restriction at A. Top nodes never use the counter value.

**PROVED — first-counter disintegration.** Conditional on the graph outside type7, each top fixed-child row has C=2^32 independent full256 images, digest prefix alphabet N=2^128 and acceptance set T of density p. With probability `(1-p)^C` it fails; otherwise the first accepted index j has unconditioned mass `(1-p)^j p`, its digest is uniform in T, its earlier same-child outputs are iid uniform outside T, and its later/other-child outputs are iid uniform. Full-image suffixes are independent uniform128 bits. The product weights of every specified row equal N^(-C), before appending the suffixes. Distinct row addresses are independent even when child values coincide. This is the reviewed canonical sampler, including failed rows.

**PROVED — joint dependencies retained.** Counter j constrains the same child's previous row entries. In particular, j is not independent of the entire type7 function and can help identify its child if that function is known. We never replace the disclosed counters by independent geometric samples detached from the real row. Instead sample the graph, the complete type7 function with that exact row law, and derive L from them. This preserves the full joint distribution, including public raw queries before disclosure and retained quantum memory. It is harmless below because the protected challenge in each component is a different residual plane or coordinate, not because counters disclose no information about every possible secret.

## 3. Private replacement: unchanged loss, including setup disclosure

**PROVED — common setup channel.** For fixed nonzero S, the reviewed private coupling uses independent full256 F(A), J(m), O0 and unused master K/P, with REAL oracle O1 patched on the private K/P families. All public typed top-cache computations are outside those private families: their header is S||0^48 and type is 0–4 or7; private K-family types are5/6, while the P-family has bytes16–31 equal to nonzero S. Consequently REAL and IDEAL keygen derive the same private F values, graph, counter rows, completion branch and L. Setup disclosure is the same classical channel in both games; it is not a new discrepancy term.

**PROVED — IDEAL unused-master invariant.** In continued IDEAL, L depends on F and O0 but not on unused K/P. Even an adversary that chooses measured signing messages using L and retains a quantum register from pre-key queries has its state independent of those unused master keys. A raw input still nominates at most one K or P. Thus support mass is <=1/N, and the coherent private vector gap remains 2Q/sqrt(N). Honest/final source I/E calls still nominate at most 2q+2 P values; L contains no J values. Classical joint-private distance stays `(Q_H+2q+2)/N`; quantum distance stays `min(1,2Q/sqrt(N)+(2q+2)/N)` for fixed nonzero S.

**PROVED — event-specific stop.** L is also a common channel in the refined private stopped game. Active CQ-block deletion and the one common terminal projector B-or-W remain available. The alias term b=min(1,(2q+2)/N) is unchanged. The comparison's HJ winning upper e must be the cache-disclosed HJ bound established in sections4–6, rather than silently reused from the opaque game.

## 4. H: public surface plus type7, without hidden predecessor advice

**PROVED — safe extended environment.** The reviewed hidden sampler samples all nonterminal chain values and FORS secrets independently uniform, samples endpoints and every compressed/Merkle/FORS image independently as its typed DAG outputs, and assigns consistent designated oracle images. Its safe public surface already contains all top cached nodes and all layer3 child roots V_A. The type7 restrictions are independent of the protected predecessor coordinates and FORS secret coordinates. Sample those entire restrictions as outside randomness, and derive the first accepted counters from V_A and those restrictions. Thus `(safe surface, type7 functions, L, setup completion)` is independent of the remaining protected coordinates at time zero. This uses the ghost sampler, not conditioning on a full private F table.

**PROVED — predictable exposure and quantum memory.** Ghost raw replies do not consult hidden predecessor inputs. After L disclosure they can depend on the extended outside environment; source route/digit selection uses J, message replies, V_A and type7 functions, not remaining predecessor values. All legitimate WOTS disclosures remain suffix-closed; FORS disclosures remain indexed secret disclosures after atomic completion. The continued ghost's undisclosed coordinates remain unused/uniform even with retained quantum memory and adaptive measured requests. No normalization on absence of a previous hidden hit, completed setup, or a particular counter vector is made.

Therefore classical H remains `(Q_H+3017)/N` and final quantum H remains `min(1,(2Q+sqrt(3017))^2/N)`. The stop-before-first-hit examiner and the 3017 candidate count are unchanged. Knowledge of all cached compressed PKs does not itself mark their WOTS predecessor coordinates exposed.

## 5. C: L is independent outside data for each message challenge

**PROVED — separate planes.** For fixed nonzero S, the addressed types0–7 generating L are disjoint from the inner I language (bytes16–31=S) and eligible outer E language (52-byte inputs). In HJ, F and J are independent private maps. L and its completion flag do not depend on J or either challenge plane; its top root is simply an outside-derived public header parameter. C's classical fresh-J predictions, inner fresh-output/namespace checks and coverage stream padding therefore tolerate L as initial outside advice.

**PROVED — QROM source bridge and search projections.** The global R_m/U_m sampler conditional on J and outside graph still has its ordinary inner-function marginal with L present. Before a new request, ghost R_m/U_m remain unused; L does not expose them. Atomic completion tests and signature material are common services derived from the outside environment plus that request's outer template. AR row reprogramming includes the same Q+q+1 row-read ledger. In the separate fresh-outer search, L is independent of BASE outer marks and the padded coverage template; in the separate final-inner exceptional search, L is independent of BASE inner marks and the latent U_i. The adversary may choose labels using L and challenge replies: assignments are generated online, not conditioned on challenge-dependent logs. The two helper advice views are not merged.

Thus the already reviewed classical C bound beta+(Q_H+1)p_F(q) and quantum c formula are unchanged. L never provides a new honest J oracle or a free I/E image lookup.

## 6. G and D7: only their own stronger event advice is used

**PROVED — G projection.** G's sampler already allows the complete designated types0–4 graph and complete outside function tables. L consists of graph nodes plus counters derived using the outside type7 table, so it is a deterministic function of that allowed advice. Conditioning on L introduces no new dependence of a selected alternate type0–4 residual image on its designated target. Classical G stays `(Q_H+3217)/N`; quantum G stays `min(1,8(Q+3218)^2/N)`.

**PROVED — D7 projection.** D7's sampler already allows the full graph, each successful row's V,c,y, failed-row markers, canonical full images and earlier rejected entries. L is a projection of that advice. Its successful top-row counters are not mistakenly treated as independent of earlier rejects; their exact conditioning is already present. Eligible later/other-child residual images remain iid uniform conditional on that full sigma. Classical D7 stays `(Q_H+5)/N`; quantum D7 stays `min(1,8(Q+6)^2/N)`.

**PROVED — advice separation.** The hidden H experiment never receives G's full secret payload graph; the coverage final-inner experiment never receives its BASE inner table. Each component separately embeds the same ordinary L-disclosed HJ adversary, whose additional payload is simulated by that component's permissible advice. The union bound is taken over that one ordinary HJ marginal. There is no single grand experiment granting all helper advice to an EUF adversary.

## 7. Composition and limitations

**PROVED — deterministic split unchanged.** Initial L supplies no chain start/predecessor value and no FORS secret. The meaning of exposed remains completed-signature suffixes/selected secrets. The accepted final-verifier split C-or-H-or-G-or-D7 therefore applies pointwise with L present; it does not classify an adversary by how it obtained its final bytes.

**PROVED — same upper formulas.** With N=2^128 and q initiated requests, the exposed-payload classical upper is

    min(1,(6Q_H+3q+6243)/N
        +(qQ_H+q(q-1)/2+q)/N^2
        +q(511/512)^(2^32)+(Q_H+1)p_F(q)).

For the conservative finite-QROM upper retain `min(1,1/N+delta+c+h+g+d7)` from the reviewed theorem. For the refined upper retain `min(1,1/N+[2Q/sqrt(N)+sqrt(min(1,b+e))]^2)`, with e=min(1,c+h+g+d7) and b=min(1,(2q+2)/N). All fixed-nonzero component inequalities are uniform in S, and S=0 is charged once. The exact payload adds zero probability/query loss in these finite information-theoretic formulas, while it changes the observer interface and memory allowance.

**PROVED — completion handling.** Keep failed top rows and absorbing noncompletion in the sampler. Supplying L only on completion is a common channel, not conditioning all transcripts on that event. If a separately defined completed-key game is needed, a general unconditioned bound may be divided by tau_top; this extension does not remove that normalization requirement.

**OPEN — minimum remaining links.** Independent review of this extension's source dependency and joint observer projection is required before promotion. A mechanically checked source-to-channel refinement is still absent. A simulator from pk and public data is not supplied and does not follow from private-seed recomputability. An actual serialized cache/fixture must be proved to contain exactly L and no seed/context/extra fields before this theorem can describe its disclosure. Corrupt counters, partial buffers, mutable cache responses, timing, full secret fixture disclosure, actual SHA-256, efficient embeddings and security-category/resource certification remain outside this result. No claim of equality between cache-disclosed and opaque adversary advantages is made: only the same sufficient upper bound is derived for both.


**PROVED / COMPUTED — promotion scope.** The immutable subject above was reviewed independently. Acceptance and exact source/subject/control pins are in `cache-payload-source/REVIEW.json`. The source candidate remains unchanged. Historical review-pending wording above is superseded by this acceptance; it does not broaden the mathematical interface or claim security-category certification.

**PROVED — loss terminology.** No additional term is needed in the same sufficient probability upper bounds for the payload-disclosed game. This is not equality of the optimal opaque and disclosed adversarial advantages, and not a zero-loss black-box reduction from public payload to a pk-only observer. Honest cache/reference transcript equality is within the same payload-disclosed interface.

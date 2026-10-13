# Exact honest top-cache payload and the public auxiliary-view obligation

**PROVED / COMPUTED / OPEN — source-first derivation.** This report was derived from the pinned release library, the parent source/game audit and previously accepted component arguments. No new sibling-agent candidate was read. It contains no forgery construction, runtime measurement, full-cache generation, source change or manuscript change. Its public-payload extension is a proof candidate, not a promotion of the already reviewed opaque-cache theorem.

## 1. Fixed object and disclosure boundary

**COMPUTED — live source binding.** Release `publications/LULA-I/release/code/lula1/src/lib.rs` has SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. The fixed parameter string in the release drivers has only layer 4 cached. `LayerCache` at 450–454 contains `subtrees: Vec<Subtree>` and `ctrs: Vec<Vec<u32>>`; `Subtree` at 281–285 contains a height and a level-major node vector. The payload-byte accounting at 574–582 includes node bytes and counter bytes only. It excludes Vec allocation headers, capacities, allocator overhead, parameter metadata, seed/context fields and file framing.

**PROVED — object of this report.** Define a canonical logical byte string `C_top = concat(top_nodes) || concat(BE32(top_counters))`. This big-endian counter encoding is an explicitly defined observer encoding, not a claim about Rust native memory layout or the little-endian harness fixture. The logical vectors identify exactly the same data under either encoding. The observer does not read `Signer.ctx`, keys, hash transcripts, transient chain values or in-flight worker results. The value is immutable after successful preparation; old and fresh snapshots disclose the same payload.

**COMPUTED — exact decomposition.** Let H=21 and L=2^21=2,097,152. There is one cached top subtree, tree index zero.

| Logical field | Elements | Bytes | Source dependency |
|---|---:|---:|---|
| WOTS PK leaves, height 0 | 2,097,152 nodes | 33,554,432 | Each is the type-1 compression of 16 type-0 chain endpoints at address `(4,0,kp)` |
| Merkle internal nodes, heights 1–21 | 2,097,151 nodes | 33,554,416 | Addressed type-2 hash of the ordered lower-level pair |
| First accepted WOTS counters | 2,097,152 u32 values | 8,388,608 | Canonical type-7 row for the fixed layer-3 child root |
| Total logical payload | 4,194,303 nodes plus counters | **75,497,456** | Deterministic given key and oracle, when preparation completes |

**PROVED — node order and indexing.** For level ell in `[0,21]`, width is `2^(21-ell)`, level offset is `2^22 - 2^(22-ell)` and `nodes[offset+i]` is node i at that level. At ell=0 the offset is zero. At ell=21 the offset is 4,194,302, so the last node is the 16-byte public root. Internal addresses are `AD(4,0,type2,kp0,height=ell,index=i)`; leaves are compressed WOTS public keys, not bare chain endpoints. `Subtree::build` 291–307 and `auth` 312–318 establish the ordering. The thread chunks are concatenated in launch order at 526–553, so leaf/counter order is increasing item index, independent of completion order.

**PROVED — what is absent.** The payload contains no WOTS chain start, nonterminal chain value, individual chain endpoint, FORS secret, FORS leaf/path, child-root array, canonical digest vector, randomizer table or secret seed field. A top counter corresponds to a child root but does not serialize that child root. The compressed leaves nevertheless depend cryptographically on private chain starts; absence of literal seed bytes is not a nonleakage proof.

## 2. Exact field dependency graph

**PROVED — source formulas.** Write K=`sk_seed`, P=`sk_prf`, S=`pk_seed`, B=`S || zero48`, and O for the complete SHA-model oracle. For top leaf u and chain i:

`start[u,i] = Tr16 O(B || AD(4,0,5,u,i,0) || K)`;

`X[u,i,0]=start[u,i]`, and `X[u,i,p+1]=Tr16 O(B || AD(4,0,0,u,i,p) || X[u,i,p])` for p=0,...,254;

`L[u]=Tr16 O(B || AD(4,0,1,u,0,0) || concat_i X[u,i,255])`.

The top node vector is the addressed Merkle closure of `L`. These formulas follow from `WotsC::sk`, `chain`, `pk` and `compress_pk`, 239–263. No counter occurs in these formulas.

**PROVED — counter dependency.** For each u, `V[u]=root(compute_subtree(layer3,tree=u))`, by `child_value` 486–495. That layer-3 subtree has 32 WOTS keys, each with 32 width-16 chains. Its root is computed from direct chain-endpoint PKs and Merkle hashes; it does not recursively construct or sign layer-2/FORS children and does not need lower canonical counters. `c[u]` is the least c in `[0,2^32)` whose type-7 digest `Tr16 O(B || AD(4,0,7,u,0,0) || V[u] || BE32(c))` has 16 base-256 digits summing to 2040. Preparation loops at 538–540 and `grind` at 228–236 establish this first-accepted definition.

**PROVED — direct and indirect independence boundaries.** In the real source, both L and V depend on K, S and raw addressed hash restrictions. The payload has no direct or indirect P dependency: no cache construction call invokes `prf_msg`, `hmsg_inner` or `hmsg_outer`. It has no direct FORS-secret dependency because the top child's `compute_subtree(3,u)` computes layer-3 PKs directly. Existing signatures and the complete logical key graph may correlate it with other graph values through the common K and public O. Therefore these source dependencies alone do not imply independence from every adversarial observation.

**ASSUMED / PROVED within the existing joint-private ideal model.** After F/J privatization, starts at distinct type-5/6 addresses are independent memoized ideal values, and K/P become unused coins. In the accepted programmed graph representation, all WOTS endpoints, compressed PKs, FORS leaf images, internal nodes and roots are part of the safe public graph surface. Hidden FORS secrets and WOTS interior predecessor coordinates are independent of that surface. Type-7 rows depend only on public-surface V values and their own outside function restriction. Hence `C_top` is a measurable function of that safe surface and type-7 row metadata, without reading any protected predecessor or J message nonce. This is a representation-dependent statement; conditioning on the entire private F table would invalidate it.

## 3. The seed-bearing benchmark fixture is a different object

**PROVED — exact driver serialization.** `lula1_driver_original.rs` save at 42–57 writes: magic 8 bytes; all 48 seed bytes; public root 16 bytes; number of layers as LE64; one presence byte per five layers; cached subtree count as LE64; subtree height and node count as LE64 each; node vector; counter count as LE64; counters as LE32. For exactly one top subtree, framing is `8+48+16+8+5+8+8+8+8=117` bytes, so file length is **75,497,573 bytes**. Seed bytes occupy file offsets `[8,56)`. The load routine reconstructs `Ctx` from these bytes at 62–65. The fixture is a private whole-signer persistence artifact, not a payload-only public cache representation.

**PROVED — scope consequence.** A payload-only disclosure theorem must explicitly exclude this file and context/seed-bearing memory. Merely stripping a filename, claiming values are recomputable, or counting 75,497,456 payload bytes does not convert the actual fixture into the permitted public view. This report neither reads a live fixture nor proposes exposing one.

## 4. Public-payload game and exact observer interface

**PROVED — definition.** Define `Exp_payload` as the existing finite ordinary full256-RO EUF-CMA game, but after successful honest setup return `(S,root,C_top)` instead of `(S,root)`. The adversary still receives only classical completed signatures, controls no cache bytes, and has the same adversarial raw-query cap Q and initiated-sign cap q. On cryptographic setup noncompletion the experiment is absorbing/nonwinning and returns no payload. No conditioning on successful preparation is implicit. The payload is copied as immutable classical advice before post-setup adversarial interaction. Pre-key quantum/classical queries remain allowed. Branches restore the same honest immutable logical cache. This is stronger than opaque snapshots and distinct from cache corruption, timing, physical RAM observation or a coherent signing interface.

**PROVED — observer program sketch.** `Observe(signing_environment)` reads only `(cache[4].subtrees[0].nodes, cache[4].ctrs[0])`, validates logical shapes at the definition boundary, encodes the two ordered arrays, and returns C_top if successful setup exists. The shapes are mathematical interface restrictions, not newly installed source checks. Observe performs no raw hash query and reveals no private/context field. With all auxiliary state generated inside the challenger, a reference-challenger interface can carry these fields alongside its key and return them initially; that is not a public-key-only simulator.

**PROVED — correct internal simulation interface.** In the ideal graph experiment, `Sim_payload(surface,row_metadata)` copies the top compressed leaves/Merkle closure and the first-success counter for each top child-root row. It uses no protected coordinate, message nonce, or challenge Boolean mark. Its input includes the actual sampled safe graph surface and canonical type-7 metadata associated with the same oracle as the adversarial queries. This is an exact internal observer projection with potentially enormous finite advice. It is neither an efficient external simulator with input only pk nor permission to independently choose cache/root/oracle values.

## 5. Why the requested public-key-only explanation is unsupported

**PROVED — distinction.** Deterministically recomputable from `(sk,O)` is not equivalent to efficiently computable from `pk` with no additional primitive access. Source cache construction expressly invokes secret type-5 PRF inputs and evaluates whole chain/child-root graphs. It contains no implementation of a pk-only reconstruction routine. The canonical counter cannot be recomputed by the public verifier from that counter alone because its canonical child root is absent from the cache payload.

**PROVED in the accepted ideal graph marginal — zero-query obstruction.** The first compressed top leaf L[0] is a uniform node independent of S and the top root: the graph sampler chooses each own-address full image independently before programming its designated point, including the final root image. Thus a randomized algorithm whose entire input is pk and which gets no oracle information predicts the genuine L[0] with probability exactly 1/N. Exact cache recovery would predict that field. This refutes an unconditional exact pk-only/no-primitive-access reconstruction claim in the very model being used for the proof. It does not establish impossibility for an oracle-access simulator, a programmed-RO simulation, or the fixed SHA-256 function; those interfaces need their own statement and proof.

**OPEN — efficient external simulation.** The smallest external claim would be a joint-view simulator with pk and authorized oracle/reduction interfaces whose `(cache, oracle, signing transcript)` distribution matches the real disclosure experiment, with explicit cost and programming loss. Sampling independent nodes/counters and forcing the existing public root is not that lemma: parent/child hash equations, chain compression, canonical rows and future signatures must all be correlated correctly. No such efficient simulator is supplied here, and it is unnecessary to state an information-theoretic direct bound if an auxiliary-view argument can be proved instead.

## 6. Smallest direct auxiliary-view lemma

**OPEN — proposed lemma `PayloadObserverCompatibility`.** Extend each already reviewed component experiment separately with its own correct early classical observer output C_top. Prove that the coupled ordinary marginal is `Exp_payload`, that the respective protected variables/Boolean mark fields remain independent of the observer and IDEAL query state exactly as required below, and that the common source channels/terminal split retain their previous query counts. This avoids the false claim of reconstructing payload from public key. No component's stronger advice may be merged into another component's experiment.

| Component | Required field-level argument | Existing scalar loss expected if lemma closes |
|---|---|---|
| Joint private hop, including event-specific refinement | Cache generated from coupled F values, public graph and type-7 rows; no K/P use in continued IDEAL. Setup has no message I/E alias nomination. Observe is common CQ setup output. | Same private discrepancy/event projector bound; no per-cache-element charge |
| Hidden predecessors H | Nodes are subset of safe surface; counters are public-surface-child/type-7 metadata. Neither observer nor metadata chooses suffix disclosure by reading a remaining hidden predecessor. Initial Known contains endpoints only; counters do not count as WOTS suffix exposure. | Same `(Q_H+3017)/N` or `(2Q+sqrt(3017))^2/N` |
| Alternative graph images G | Full designated graph/outside-table advice already includes every payload field. Counters use type-7 outside restriction, not eligible residual type0–4 mark bits. | Same G bound |
| Canonical type-7 event D7 | Top counters are subset of all canonical row metadata already in its separately augmented advice. Root graph does not depend on type-7 marks. | Same D7 bound |
| Adaptive FORS coverage C | Payload belongs to graph/type-7 restrictions disjoint from source inner plane on nonzero S and from eligible 52-byte outer plane. It is independent of unused J nonces, fresh U assignments and outer row templates/search challenges in the respective reductions. Labels remain online functions of the actual quantum history including C_top. | Same C source/search/reprogramming budget |
| Final verifier split | Definition of an exposed secret/suffix remains completed-signature exposure, because payload includes neither. Authentic node/counter advice does not remove the `C or H or G or D7` path classification. | No new event term |

**PROVED — structural implication if this exact lemma is established.** The accepted ordinary classical/QROM formulas would apply to `Exp_payload` with unchanged scalar bounds, followed by the already proved honest-cache transparency coupling with delta=0. This conditional implication is not a completed public-cache security theorem. An accepted second reading of all field-level independence claims, especially H's continued-IDEAL factorization and C's source/AR challenge separation, is the remaining gate.

**OPEN — excluded variants.** Seed-bearing fixtures, public compression traces, hidden chain work buffers, mutable/corrupted payloads, failed in-flight counters and physical timing observations are different auxiliary views. They are not reduced to C_top by this lemma. No complete security category or fixed-SHA assertion is inferred from a public-payload result even if the lemma is closed.

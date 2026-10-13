# Independent canonical-target derivation

Status: PROVED for the expressly stated classical random-oracle experiment; source refinement and complete security remain OPEN. Written before reading the canonical-targets author's derivation.

## Source and experiment

Pinned `publications/LULA-I/release/code/lula1/src/lib.rs`, SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

PROVED (source semantics): `digest` hashes child value V (16 bytes) followed by a big-endian u32 counter under the address's type-7 header (216–220). `accept` tests the fixed digit sum and the zero suffix (225–227). `grind` starts at zero and returns the first accepted row (228–236); it has no explicit failure return at counter exhaustion. For the fixed parameters z=0, each digest uses all 128 output bits. Each address has one honest child V: a fixed FORS public key at layer 0 or a fixed lower-subtree root at upper layers (486–496). WOTS public keys and these roots do not consult type 7 (251–262, 291–330, 341–376, 479–496). Thus V is independent of its own type-7 restriction in a typed classical RO game with independent private type-5/6 maps.

ASSUMED experiment boundary: independent ideal private maps after a valid shared-oracle privatization hop; fixed uniform seed, nonzero public seed S; opaque honest cache/snapshot operations; no corrupt cache or internal raw-query/timing leakage. A classical adversary makes at most Q_H charged raw hash calls, including prequeries, and submits one final candidate checked by the source verifier. Setup/signing may be partial. The source uses real SHA-256, whereas this lemma concerns an ideal shared RO. No theorem about real SHA-256 is asserted here.

## Exact full-output sampler

Write M=2^128, C=2^32, and let A be the address's accepted 128-bit digit-sum slice, with p=|A|/M. For fixed V, its C counter rows are independent full 256-bit outputs. Let kappa be the first accepted row, or bottom if no row is accepted. PROVED:

* Pr[kappa=c]=(1-p)^c p for 0<=c<C; Pr[kappa=bottom]=(1-p)^C.
* Given kappa=c, row c has a uniform prefix in A and an independent uniform 128-bit suffix. Earlier rows have independent uniform prefixes outside A and independent uniform suffixes. Later rows remain independent uniform full 256-bit strings.
* Given bottom, all C row prefixes are independently uniform outside A and all suffixes are independent uniform 128-bit strings.
* Rows for other child values, and other payload lengths, are independent uniform full outputs in both branches.

Sampling this conditional table at the start and mixing over kappa reproduces the entire original RO restriction exactly, including arbitrary prequery orders. It does not authorize overwriting a previously answered raw point. Merely sampling a truncated accepted prefix without the rejection history or full-output suffixes is insufficient.

## Scalar target event

Define Y as the canonical accepted prefix for addresses with kappa != bottom. Bad7 occurs at a charged raw query to that address with payload x different from V||BE32(kappa), whose output prefix equals Y. It is an event about this address's designated target, not a collision against all address targets.

PROVED: expose, for analysis, the entire designated public graph, each kappa, each full target image and every earlier rejected row. Expose no later-counter or other-child residual answers for free. Conditional on this strong view, a fresh residual raw point has an independent uniform prefix, so its probability of matching Y is 1/M. Earlier rejected rows cannot equal accepted Y. The target point is excluded; repeating a previously nonmatching raw point creates no new opportunity. On a repeat of a matching point Bad7 already occurred. Addresses with bottom have no designated accepted target. Every raw typed query names one address, so no total-address factor arises. The adaptive union bound is

    Pr[Bad7] <= min(1, (Q_H+5)/M).

The extra five are the at most five type-7 digest calls made by one final source verification (715–721), regardless of adversarial V/c and early rejection. Source honest grinding and honest cache checks query only earlier rejected rows or the designated target (228–236, 539–540, 636–655); they provide no residual answers for free. Malicious accepted cache counters can query later rows and are outside this boundary.

The raw-point coefficient is 1/M, not 1/|A|: conditioning a candidate on acceptance changes its distribution and cannot be obtained for free. The strong-view projection proves a target-collision event only; disclosure of full graph payloads may reveal chain/FORS secrets and cannot be used as an EUF-CMA simulation. None of this proves hidden-value secrecy, FORS coverage, the shared-oracle hop, a computational SPR reduction, an efficient ghost simulator, a quantum query bound, or complete signature security.

## Top-cache readiness and counts

COMPUTED from source: only layer 4 is cached in the fixed parameters. Source 517–523 gives nsub=1, nleaf=2^21 and exactly N_top=2^21 canonical planes (addresses layer=4, tree=0, keypair=0,...,2^21-1). Different child values need not be distinct because the full keypair addresses are distinct. Conditional on the non-7 graph, the planes are independent and have the same p_top. Therefore PROVED:

    tau_top = [1-(1-p_top)^C]^(2^21),
    p_top = [x^2040](1+x+...+x^255)^16 / 2^128.

This is the probability of mathematical counter availability for every required top cache entry. It is not arbitrary OS keygen totality: positive worker count, memory, allocation, threads, panics, I/O and any workload time limit remain separate. The source does not return bottom; exhausted checked arithmetic panics, while wrapping arithmetic may loop forever.

Conditioning specifically on these top planes having kappa != bottom does not alter residual point uniformity, since the event is entirely target metadata. Hence the scalar bound survives that precise mathematical success conditioning. An arbitrary actual execution-success condition is not covered and must not silently be substituted.

The count 246 refers to one lower layer's maximum non-7 verification calls: fixed sum 240 chain steps + one endpoint compression + five authentication-node calls. Its type-7 digest adds one, making 247 calls for that layer. The Bad7 budget is five across all layers, not 246, and N_top is neither 246 nor the 2^22-1 top Merkle-node count.

## Prequeries and shared-input bridge

PROVED within the typed RO experiment: prequeries are charged raw queries to the same originally sampled function. Matching a future target point is excluded from Bad7; matching a non-designated point to that target is counted without reprogramming. The proof grants target metadata to the adversary from the start, which only strengthens this particular event analysis.

OPEN outside that experiment: an actual source-to-typed-game hop must account for secret-input guesses, prequeries and any unaddressed input overlap. S!=0 ensures source unaddressed message-hash/secret-R inputs cannot syntactically coincide with a typed header in the identified cases; uniform S=0 must be charged once in the overall reduction or handled in its REAL branch. Do not add that event repeatedly to every local lemma.

## Tiny falsification control

The accompanying exhaustive finite control uses four possible prefix values, a two-value accepted slice, three counter rows, and two independent suffix values. It checks the rejection law, the full target/suffix law, fresh residual uniformity conditional on all permitted strong-view metadata, and the exact geometric/bottom masses. It also demonstrates that two freely exposed residual answers let one final selected query match with probability 7/16 rather than 1/4. Thus unrestricted residual disclosure is a genuine invalid strengthening, not a harmless presentation choice.

# LULA I: source-bound security proof attempt

**OPEN — final verdict.** Complete classical EUF-CMA security, a certified signing limit, and a QROM category-1 reduction are **not established**. This document closes several structural and numerical obligations and identifies the smallest remaining proof obligations. It does not edit the construction or `LULA-I.tex`. A component work exponent is never substituted for a complete advantage bound.

## 1. Status convention and fixed object

**PROVED** denotes a mathematical derivation under its explicit premises; source-derived invariants are identified as such. **COMPUTED** denotes executed arithmetic or finite controls. **CITED(source)** identifies externally established results, whose applicability remains a separate obligation. **ASSUMED** identifies a model or hypothesis. **OPEN** identifies an unclosed statement. A checked abstract lemma is not a checked refinement of the Rust implementation.

**COMPUTED — binding.** `code-review/SOURCE_AND_COUNTS.json` binds the original, private frozen, and release libraries. Original/private SHA-256 is `c5b16f35ec9e3a826e5d8100dbbc4d3a8287e3e52fd567a24e95f03bb7243ab5`. Release SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Their LF-normalized bodies from the first Rust import are identical; only the leading documentation comment differs. The current manuscript SHA-256 is `d33229794b2b69644aa77851e09e146dda53480f8b2e70721c06b81d91587ebe`. The requested naming note is already in that baseline.

**COMPUTED — parameters.** Hash nodes are 16 bytes. The public key is 32 bytes. The input seed is 48 bytes, split into two 128-bit secrets and a public 128-bit seed. The five heights are `(5,5,5,5,21)`; the first four WOTS encodings have `(w,l,S)=(16,32,240)`, the last `(256,16,2040)`. FORS builds 17 real height-9 trees and tests a zero condition on the omitted eighteenth index. Signature length is

\[
16+4+17(1+9)16+4(4+32\cdot16+5\cdot16)+(4+16\cdot16+21\cdot16)=5720.
\]

**COMPUTED — cache.** The configured top cache contains `(2^22-1)` 16-byte nodes and `2^21` four-byte counters: 75,497,456 payload bytes. Only the top layer is cached. The private benchmark snapshot's seed header is not part of this payload and is not safe to disclose.

## 2. Exact forgery experiment

**ASSUMED — setup distribution.** A production experiment draws a uniform secret 48-byte seed; the source itself accepts a caller-supplied seed. Fixed benchmark seeds are not a production key distribution. SHA-256 is modeled as **one shared random oracle**, unless a justified encoding hybrid establishes independent restrictions. Treating differently named routines as independently sampled oracles is not a source fact.

**PROVED — definition.** Fix the stated parameters, and use the ordinary single-root verifier, not the library's dual-branch interface. Let `SignRef(sk,m)` be `Signer::sign(m,false)` and `Verify` be the exact Boolean wrapper at release library lines 672–674. A has a permanent set of queried raw-byte messages, at most q signing calls, at most Q_H adversarial hash calls, and a stated computation budget T. Define the following experiment:

```text
seed <- uniform {0,1}^384
(sk, pk) <- configured key generation(seed), including the prepared top cache
if setup does not complete: no winning completion
S <- empty set; n <- 0
SignOracle(m):
    require n < q
    n <- n+1; S <- S union {m}
    return only a completed SignRef(sk,m)
    [if this call never completes, no further completed interaction occurs]
(m*, sigma*) <- A(pk, SignOracle, shared SHA oracle)
return (m* not in S) and Verify(pk,m*,sigma*)
```

**OPEN — completion convention for a total oracle.** Actual 32-bit grinding counters wrap in unchecked release arithmetic or panic in checked builds. No explicit exhaustion response is implemented. A theorem for a total or finitely failing oracle requires a finite-search/failure model and its probability. The declared common partial completed-call interface already supports the conditional transcript transfer without that extra totality premise. Conditioning on successful key generation must be declared and related to the unconditioned game, rather than silently renormalizing it. This report uses completed transcripts of a partial deterministic algorithm.

**PROVED — adversarial control.** A chooses every byte of R, the FORS counter, all 17 FORS values and paths, all five WOTS counters and chain values, and all five authentication paths, as well as the fresh message. The verifier checks exact length, the omitted-index zero condition, target-sum acceptance and final root equality. It checks neither the origin of R nor minimality of any counter. A second valid signature on an already queried message is not an ordinary EUF-CMA forgery.

**PROVED — detailed field table.** Offsets and sizes are in `code-review/INDEPENDENT_CODE_GAME.md` §2. R occupies bytes 0–15, the FORS counter 16–19, FORS evidence 20–2739, and layer i begins at `2740+596i`. All these fields are adversarially controlled in a forgery. Fixed parameters and the public key are not signature-controlled fields.

## 3. Actual hash interfaces and domain obligations

**PROVED — serialization.** Put `B=PK.seed || 0^48`, and let `A(j,t,type,kp,u,v)` encode a one-byte layer, eight-byte tree, one-byte type, four-byte keypair and two four-byte words. Integer fields are big-endian. The addressed routines use `Trunc16(SHA256(B||A||input))`. The source's prepared compression state implements the ordinary padded hash; it is not an extra oracle.

| Status | Family | Exact suffix after B | Output |
|---|---|---|---|
| PROVED(source) | WOTS secret derivation | `A(j,t,5,kp,chain,0) || SK.seed` | 16 bytes |
| PROVED(source) | FORS secret derivation | `A(0,t,6,kp,0,g) || SK.seed` | 16 bytes |
| PROVED(source) | WOTS chain | `A(j,t,0,kp,chain,position) || chain_value` | 16 bytes |
| PROVED(source) | WOTS endpoint compression | `A(j,t,1,kp,0,0) || endpoints` | 16 bytes |
| PROVED(source) | Hypertree node | `A(j,t,2,0,height,index) || left || right` | 16 bytes |
| PROVED(source) | FORS leaf / node | `A(0,t,3,kp,height,global_index) || secret_or_children` | 16 bytes |
| PROVED(source) | FORS root compression | `A(0,t,4,kp,0,0) || 17 roots` | 16 bytes |
| PROVED(source) | WOTS digest | `A(j,t,7,kp,0,0) || child || BE32(counter)` | 16 bytes |

**PROVED — unaddressed calls.** `PRF_msg(m)` hashes `SK.prf || PK.seed || m` and truncates to 16 bytes. `H_inner(R,m)` hashes `R || PK.seed || root || m` to 32 bytes. `H_outer(inner,c)` hashes `inner || BE32(c) || PK.seed` to 32 bytes. Exact call sites, address ranges, and primitive-source anchors are in the independently derived oracle table, §3–4 of the code report.

**PROVED — addressed separation.** Types 0–7 and bounded fixed-parameter coordinates distinguish the intended addressed operations. Recomputations intentionally repeat the same encoded oracle input. The proposed assertion that every different call site must have a different address is therefore too strong even for honest construction and verification.

**PROVED — structural overlap counterexample.** Choose `R=SK.prf` and `m0=root||m1`. Then the complete input of `PRF_msg(m0)` equals the complete input of `H_inner(R,m1)`. This is a counterexample to disjoint input languages; it is not an efficient attack, since the adversary does not know SK.prf. `code-review/DOMAIN_OVERLAP_CONTROL.json` records the literal-input check.

**OPEN — smallest encoding lemma.** Bound shared-oracle overlaps, secret-input guesses and prequeries for the actual variable-length formats. A proof may then introduce independent restrictions with a charged bad event. Adding tags or importing an HMAC theorem would change the object or assume a theorem for a different routine. Literal independence of deterministic R from everything observed is false: R is revealed, repeats repeat it, and distinct outputs can collide. The useful target is pseudorandomness of an unrevealed fresh-message R in a correctly coupled shared-oracle hybrid.

## 4. Secret derivation and query counts

**COMPUTED — honest invocation bounds.** Minimum no-cache setup invokes the secret PRF 33,554,432 times. Prepared setup invokes it 2,181,038,080 times. A prepared signature invokes it 12,961 times; a cold signature 33,567,393 times. The actual configured setup in §2 prepares the top cache, even though its reference signing calls disable cache use. Its honest-execution bound is therefore

\[
U_{\rm actual\ reference}(q)=2{,}181{,}038{,}080+33{,}567{,}393q.
\]

**COMPUTED — other setup/signing combinations.** Prepared setup with cached signing gives `2,181,038,080+12,961q`. Disabling cache preparation during setup and then signing uncached gives `33,554,432+33,567,393q`; that minimum-setup variant requires its own setup-completion convention. These counts are not silently substituted for the actual §2 experiment.

**COMPUTED — distinct versus repeated calls.** One prepared signature uses at most 12,816 distinct secret addresses, one cold signature at most 33,567,232. The entire possible secret-PRF namespace contains 19,212,937,084,272,640 addresses; a memoized hybrid's distinct-query bound is capped by that number. PRF_msg has at most q distinct signing-message queries. These integers count secret derivations, not public internal nodes or canonical-search trials. The detailed per-layer forest inventory is in `SOURCE_AND_COUNTS.json` and the numeric output.

**OPEN — PRF hybrid.** A multi-query decisional PRF assumption can pay for replacing the combined type-5/type-6 family by a memoized random map, and a separate assumption can pay for fresh-message randomization. A reduction B must answer the adversary's shared public SHA queries consistently with secret-suffix/prefix evaluations. The source-bound honest counts above are not automatically the full simulator's query count. No concrete PRF advantage is assigned or invented here.

## 5. FORS+C: what the calculation establishes

**PROVED — omitted-tree correction.** The eighteenth digest index is checked to be zero but no eighteenth tree or secret is instantiated. The 17 real selected secrets are transmitted. Consequently the extra `2^-9` factor is a public filter on a raw digest candidate, not the probability of selecting a disclosed secret in a hidden extra tree.

**ASSUMED — fixed-instance coverage model.** Take B=2^41 instances, t=512 leaves per real tree, K=17, independent uniform honest selections, and an independently selected candidate instance. Its occupancy is N~Bin(q,1/B). Conditional on N=r, independently sampled candidate indices are covered with probability `(1-(1-1/t)^r)^K`. The average raw-candidate probability is

\[
p_F(q)=t^{-1}\mathbb E[(1-(1-t^{-1})^N)^K].
\]

**PROVED — finite-moment identity.** With b=1-1/t, the exact binomial expression is

\[
p_F(q)=t^{-1}\sum_{j=0}^{K}(-1)^j {K\choose j}(1-B^{-1}+B^{-1}b^j)^q.
\]

**COMPUTED — independent checks.** The finite-moment and positive occupancy recurrence agree; the latter uses an analytic omitted-tail bound. Binomial and Poisson evaluations agree within 0.01 bit at q=2^40 (actual difference about 2.18×10^-11 bits). Both 160- and 220-decimal evaluations agree to the stated tolerance. Numerical tolerances plus analytic tail bounds are not a directed-rounding interval certificate. The positive recurrence and high-precision checks substantially reduce ordinary cancellation risk.

| q | Status | -log2 p_F per raw candidate | Conditional exponent after Q_H=2^128 |
|---|---|---:|---:|
| 2^24 | COMPUTED(model) | 178.421820108 | 50.421820108 |
| 2^30 | COMPUTED(model) | 167.771253729 | 39.771253729 |
| 2^38 | COMPUTED(model) | 143.262538581 | 15.262538581 |
| 2^40 | COMPUTED(model) | 132.563419944 | 4.563419944 |
| 2^41 | COMPUTED(model) | 125.902530385 | 0 (bound vacuous) |
| 2^44 | COMPUTED(model) | 98.521203051 | 0 (bound vacuous) |
| 2^50 | COMPUTED(model) | 20.122193182 | 0 (bound vacuous) |
| 2^64 | COMPUTED(model) | approximately 9 | 0 (bound vacuous) |

**PROVED — budget arithmetic, conditional premise.** If each adversarial opportunity has conditional success probability at most p, the union bound is `min(1,Q_H p)`. Its exponent is `max(0,-log2 p-log2 Q_H)`. At q=2^40, a 132.5634-bit per-trial exponent therefore does not imply probability 2^-128 after 2^128 adversarial hash queries. Such a demanded probability would require a per-query upper bound no greater than 2^-256. This distinguishes an attack work factor from failure probability at a specified resource budget.

**OPEN — smallest adaptive-coverage lemma.** The computed average must be related to adaptive signing, public prequeries, forged R/ctr choices and fresh query points in the shared oracle. For a realized transcript with covered sets C_(b,j), a uniform fresh complete digest has coverage probability `(Bt)^-1 sum_b product_j |C_(b,j)|/t`. A reduction must control its distribution and any dependence on future signing choices. A preselected target instance must pay probability 1/B in a full-digest trial. The fixed-instance average cannot simply be declared the best adaptive forger's success probability.

## 6. WOTS+C: repeated addresses and exact counting

**PROVED — one fixed honest value at every address.** A WOTS address includes `(layer,tree,keypair)`. At layer zero the signed value is the full deterministic public key of that FORS instance, independent of which leaves are revealed. At each higher layer it is the root of the uniquely addressed child subtree. Thus all five layers sign one fixed child value and one canonical accepted digit vector per full address. Repeated routing does not create different honest WOTS messages. The requested Poisson two-different-message reuse term is not the reference signer's security term.

**PROVED — antichain.** If y_i≥x_i for every coordinate and both vectors sum to S, every y_i-x_i is nonnegative and their sum is zero, so y=x. This is machine-checked as `Lula.fixed_sum_antichain`; it restricts forward-only chain derivation, not arbitrary chain inputs or new message/counter encodings.

**PROVED — inclusive reachable count.** After hypothetical exposures x^(1),...,x^(j), put m_i=min_t x_i^(t), D=S-sum_i m_i and u_i=w-1-m_i. The inclusive count is

\[
N(m)=[z^D]\prod_i(1+z+\cdots+z^{u_i})
=\sum_{J\subseteq[\ell]}(-1)^{|J|}{D-\sum_{i\in J}(u_i+1)+\ell-1\choose\ell-1},
\]

**PROVED — counting convention.** Negative remaining-degree terms are zero. Inclusive raw-digest coverage is `N(m)/w^ell`; conditioned on target-sum acceptance it is `N(m)/|slice|`. Subtract only the number of distinct previously observed vectors for a *distinct-encoding* statistic. That exclusion is not ordinary EUF-CMA freshness, which concerns the message. After one exposure N=1, so an independent fresh raw encoding has probability 2^-128 of matching the old encoding. A fresh child value and free counter can collide with that vector.

**COMPUTED — exact slices.** The `(16,32,240)` slice has 5,181,241,160,064,611,531,897,369,560,287,267,312 vectors; the `(256,16,2040)` slice has 454,918,678,781,617,793,203,528,879,683,071,744. Prefix-sum integer DP and inclusion–exclusion passed 300 random and 1,936 exhaustive toy pair checks. H1/CE source calculations were crosschecked with the inclusive/exclusive distinction. Their hypothetical reuse results are not an attack on real SHRINCS or on the honest LULA reference.

**OPEN — smallest WOTS certification lemma.** From arbitrary verifying chain values, either extract an addressed chain inversion/SPR witness, an endpoint-compression binding witness, or a new child-value/counter digest that reproduces an exposed encoding. Handle unexposed keys and repeated fixed values, multiple targets, chosen counters and exact query losses. A blanket w*l loss is not derived by the antichain fact. The honest different-message reuse event is zero; other WOTS attack terms are not zero.

## 7. Merkle authentication and the exhaustive split

**PROVED — structural split.** Compare a reconstructed top path with the complete honest key graph, including routes never observed in a signature. At a fixed addressed parent whose output equals the honest parent, a different ordered child pair yields an equal-output/different-input hash witness. Otherwise both children equal the honest pair, and the comparison descends. Repeating yields either an addressed node witness or equality of the leaf WOTS public key. Compare compressed chain endpoints next, then chain values and the certified child value; recurse through the five layers and FORS-root compression. This includes changed lower roots authenticated by arbitrary WOTS evidence.

**OPEN — smallest extraction lemma.** Construct a lazy, consistent honest-graph/challenge simulator and prove its extraction probability, time, hash queries and SPR/TCR notion. A forgery need not share an entire path with a previously observed signature: it can route to an unqueried honest address. An abstract first-divergence list lemma is checked, but it neither supplies the correct challenge embedder nor pays for a huge conceptual forest.

**COMPUTED — inventories, not losses.** Subtree counts are `2^36,2^31,2^26,2^21,1`; node counts per tree are `63,63,63,63,4194303`. Their products and FORS-node counts are reproduced by the script and independent source audit. Multiplying these counts by a generic SPR advantage without a concrete embedding argument can give a vacuous bound and is not a completed tree reduction.

## 8. Hybrid ledger and reduction-program obligations

**OPEN — ledger status.** The following are explicit *proposed* games. Their definitions identify the missing obligations; they are not asserted to be equivalent. No missing step is hidden in “similarly.”

| Games / change | Reduction sketch: inputs, queries, output | Payment and status |
|---|---|---|
| H0: exact shared-SHA reference game | Run A with actual verifier and partial reference oracle; record raw SHA and signing inputs | PROVED definition |
| H0→H1: replace type-5/6 derivations by a memoized random family | B1 accepts a real/ideal keyed-function oracle; queries it at secret-derivation addresses; builds the required honest nodes; answers A's public SHA interface consistently; outputs A's exact winning bit | OPEN joint-PRF/shared-SHA simulation; honest U(q) known, full simulator count not established |
| H1→H2: replace unrevealed message randomizers by a memoized uniform map | B2 accepts a real/ideal message-PRF oracle; preserves repeats; computes H_inner/H_outer and signatures from its answers; outputs the winning bit | OPEN fresh-R coupling, secret guesses and shared-input overlaps |
| H2→H3: expose independent route/leaf selections through lazy outer hashing | B3 maintains the shared oracle table, records prequeried outer points and inner collisions, models finite first-acceptance search without changing forced bits | OPEN bad-overlap/prequery/termination bounds; no gratuitous independent-oracle assumption |
| H3→H4: classify a verifying forgery against the honest key graph | B4 reconstructs the exact verifier, descends at equal parents, returns the first equal-output/different-input addressed witness or its WOTS/FORS classification | PROVED structural classification; OPEN challenge embedding and extraction losses |
| H4→H5: bound WOTS certification substitutions | B5 uses the classified chain, endpoint or digest witness; returns a primitive challenge witness, or proves the honest child equals the verified child | OPEN precise SPR/TCR/digest reduction with free counters and multiple targets |
| H5→H6: covered FORS leaves versus new evidence | B6 returns a secret/leaf/tree/root witness for changed evidence, or charges coverage of the realized transcript and fresh-message routing | OPEN adaptive coverage bound and message-hash target/collision bound |

**PROVED — algebraic closure only.** Once every transition has a proved difference bound and H6's success has a proved bound, the triangle inequality adds those bounds. This does not establish any transition. The requested `Adv_PRF + epsilon_FORS + sum epsilon_W + epsilon_tree + epsilon_Hmsg` can be used only after its terms absorb all stated overlap, encoding, selection and failure events without omission or double counting.

**OPEN — term table.** `TERM-TABLE.md` gives the q=2^38,2^40,2^41 cells. The model FORS row is COMPUTED, the different-message WOTS reuse subevent is PROVED zero, and full PRF/FORS/WOTS/tree/H_msg/total cells are OPEN. No total bits, smallest full-security threshold, or certified q_max is computed from unknown terms. The fixed-instance exponent crossing in the manuscript is explicitly not such a threshold.

## 9. Honest restoration and corruption

**PROVED — honest cache theorem.** For a successfully generated key, consistent caches contain the same addressed nodes and smallest accepted counters as recomputation. Message randomization and FORS selection ignore the cache. Induction through the five layers gives identical child values, counters, signature bytes and paths. Searches in common uncached layers are the same partial computations; successfully prepared counters already exist. Honest restoration replaces only one consistent representation of this common partial function by another.

**PROVED — conditional rollback transfer.** In the atomic interface, snapshots give opaque handles, never cache bytes or secret seeds. Simulate every signing query using the reference oracle, allocate handles sequentially and validate restoration handles. Keep freshness over all branches. Common termination/completion behavior and identical completed signatures give the same public transcript and winning event. Thus, **if** the exact reference has bound epsilon_ref(q,T,Q_H),

\[
\operatorname{Adv}_{\rm honest\ rollback}(A)\le
\epsilon_{\rm ref}(q,T+T_{\rm bookkeeping},Q_H),\qquad\delta_{\rm probability}=0.
\]

**OPEN — numeric specialization.** No certified q_max or lambda can be substituted because epsilon_ref is not established. The conditional theorem remains meaningful and its zero query/probability loss is preserved. Bookkeeping consumes time and storage; zero cryptographic loss is not zero runtime.

**COMPUTED — corruption counterexample.** The native control imports the unmodified library, retains actual WOTS widths and target sums, and shrinks only tree heights/FORS for a cheap discriminator. Canonical counter 643 and accepted alternative 2377 produce different valid signatures on the same message. A rejected counter recomputes canonical bytes. A flipped used sibling returns an invalid signature; a flipped unused top-root slot changes nothing. This refutes universal corruption transparency and the claim that every trusted corrupt entry must cause verification failure. It is not a fresh-message forgery or a full-parameter attack.

**PROVED(source) — why.** The signer trusts the cached path and counter, and checks counter *acceptance*, not minimality. There is no full outgoing-signature verification or cache authentication. An accepted alternate counter can expose another chain vector. Malformed containers can also panic. A model that defines inconsistent-cache access to abort proves a property of that model, not a behavior implemented for arbitrary Rust cache corruption.

**OPEN — public-cache exposure.** Recomputability with sk does not imply efficient reconstructibility from pk. The public root does not reveal every node, child root or canonical counter. A stronger auxiliary-information theorem needs the exact exposed payload and a simulator. Moreover, the benchmark snapshot header contains the full 48-byte seed; disclosing that entire fixture discloses the key. The honest rollback theorem does not disclose the fixture or cached bytes.

## 10. Quantum reading and proof boundary

**COMPUTED — plain search reading (assumed search model).** For the fixed-instance FORS search model alone, square-root search gives exponents 71.631269291, 66.281709972 and 62.951265192 at q=2^38,2^40,2^41. These are rounded from the unrounded computations. This is a component search-cost interpretation, not a QROM reduction, full signer bound or automatic NIST classification.

**CITED(NIST) — category meaning.** NIST category 1 compares attack resources with exhaustive AES-128 key search across relevant cost metrics. It is not defined as advantage at most 2^-64 after exactly 2^64 quantum oracle calls. See [NIST security evaluation criteria](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post-Quantum-Cryptography-Standardization/Evaluation-Criteria/Security-%28Evaluation-Criteria%29). A QROM theorem must state both the classical signing-query budget and quantum hash-query budget and the meaning/cost of those queries.

**OPEN — actual QROM bound.** `formal/QUANTUM.md` records exact primary-source formulas, their premises and the applicability audit. Imported SPHINCS+ bounds are not automatically a theorem for this custom verifier, omitted FORS tree, target-sum encodings, secret derivations and shared untagged message hashing. No universal “ten-bit loss,” quantum q_max or category-1 certificate is asserted.

## 11. Mechanization and independent checks

**COMPUTED — formal execution.** All seven declarations in `formal/LulaLemmas.lean` pass local Lean 4.28.0 with pinned Mathlib and AXLE: sum monotonicity, fixed-sum antichain, consistent restored-cache equality, adaptive oracle transcript identity, adaptive honest-restoration identity, conditional successful-output safety, and an equal-or-first-divergence list lemma. Their transitive axiom sets are subsets of `{propext, Quot.sound}`. Aristotle independently returned the antichain proof; AXLE's declaration comparator accepted the unchanged statement and a narrow-import adaptation passed the local kernel. `formal/FORMAL_REPORT.md` records identities and logs. Finite `Option` outcomes in these abstract models do not model a Rust hanging call directly. Proofs under consistency/output-safety hypotheses do not establish those hypotheses for arbitrary Rust cache states.

**COMPUTED — other proof tools.** `formal/CacheModel.ec` and its checker log concern an abstract optional-abort oracle model. The model's treatment of invalid caches must remain explicit. Local K availability and executable-semantics obligations are reported separately; a tool inventory is not a Rust semantics proof. No private crypto source was uploaded merely to obtain a green theorem.

**COMPUTED — crosschecks.** Exact DP/IE checks, original R6/IA/H1/CE crosschecks, precision comparisons and two 30,000-trial toy experiments are recorded in `numerics/`. The toy coverage probabilities fall within reported 99.9% Wilson intervals. These check mathematical models, not a full EUF-CMA attack. `code-review/SECOND_READER.md` was written only after its independent code/game derivation was saved and critiques every modeled term.

## 12. Minimum remaining obligations and printable statement

| Status | Smallest missing lemma |
|---|---|
| OPEN | Shared-SHA input-encoding/secret-guess/prequery hybrid for the actual primitive formats |
| OPEN | Joint secret-derivation and message-randomizer PRF reductions with complete simulator resource counts |
| OPEN | Adaptive route/leaf-selection and FORS covered-set bound with forged R and counters |
| OPEN | Same-fixed-child WOTS certification including encoding-target events, chain inversion and endpoint binding |
| OPEN | Lazy honest-graph challenge embedding and exhaustive tree extraction with explicit losses |
| OPEN | Complete explicit hybrid composition and exact message-hash collision/target contribution |
| OPEN | Finite counter-exhaustion/setup-completion interface and its probability, if a total algorithm is claimed |
| OPEN | QROM applicability and concrete quantum-secure primitive bounds for this exact scheme |
| OPEN, separate stronger interface | Public-cache auxiliary-information simulation; corrupted-cache canonicality/authentication is not implemented |

**OPEN — public statement permitted by these results.** “Complete EUF-CMA security of LULA I is not established. Honest cache restoration preserves the common deterministic reference signing function under the stated atomic interface, with zero signing-query loss. The independently reproduced fixed-instance FORS+C model gives 143.2625 and 132.5634 bits per raw digest trial at 2^38 and 2^40 signing queries, respectively; these are component figures, not a bound for the complete signer.”

**OPEN — parameter changes.** The full bound has not been shown to fail at q=2^38; it is undefined because its reduction terms are open. There is therefore no derived smallest parameter change restoring a proved target. Raising a component exponent would not close the missing encoding, certification or composition lemmas. No new parameter set or timing claim is invented.

# Independent second reading: finite bounded-query outside simulator

**Verdict: ACCEPT_SCOPED_MANUAL_BOUNDED_QUERY_CONSTRUCTION_AND_B_ONLY_REPLACEMENT.** Both independently authored candidates supply an exact finite-domain simulator with deterministic polynomial resource bounds. Acceptance is for the general field/family/circuit argument and its use with a complete inherited query cap. It is not a new derivation of the protocol-specific source call counts, a checked whole-source theorem, an actual quantum benchmark, or fixed-SHA security certification.

## Independence and immutable subjects

I saved `first-independent-derivation.md` with SHA256 `c6b1b31b95100e10d484e06ba839d2b36d2e1393d18add5e7710d6bf52364a69` before reading either candidate. I then read the following files, relative to the parent shared-oracle-20261013 directory:

| Subject | SHA256 |
|---|---|
| chain-pre-independent/outside-simulator/INDEPENDENT-DERIVATION.md | 5555569b844c8a30ee5d58bdca9121e84a45fe5dd62474d0f0fb64df5c009680 |
| chain-pre-independent/outside-simulator/CLARIFICATION.md | 4e0ae20f94a1af80b5a86cd14bab4b8873589a62f4c15eb519757bf3e64f01c7 |
| chain-pre-independent/outside-simulator/ROUTES-CLARIFICATION.md | 383dc9c6b0de9417fe44ca6c66dc69874143aba970b98511df745e256461ede4 |
| chain-pre-adapter/outside-simulator/INDEPENDENT-DERIVATION.md | 939f4c5fc75e4f8be5dbbb56d45dd8a70f9d6c839e03625776ca271691df7c9e |

The registry and existing receipts consulted for inherited program premises were `PRIVATE-REDUCTION-PROGRAMS.md` (`feff3d899edcb0b675970eaf915c221d837a47ab7357828758f0f0a40c923f89`), `selected-promotion-review/QPRE-FINAL-REVIEW.json` (`dba62fbc8e945687a9ea77f6615988d22c9e874523f900c031da24b0007d112c`), and `selected-promotion-review/T7-REVIEW.json` (`773653e00caf9381dfc8f26987b22e41e36378f9f2fa1a8b88f28259c515ffe7`). Their source binding is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. I did not reread or independently certify the entire Rust source or accepted PRE/Row adapters. The final QPRE receipt links a separate resource review; it does not itself enumerate the extra254 cap. That cap remains an inherited accepted-adapter premise, as instructed by root.

## Algebra and construction

1. The lexical rank `sum_(j<ell)256^j + BE(x)` maps each length block to a contiguous interval and is injective on empty and leading-zero strings. Its largest rank is V_b-1. For b>=1, ceil(log2 V_b)=8b+1. My independently derived sentinel encoding is an alternative valid injection; it does not alter either reviewed candidate.
2. The trace-one quadratic construction works for every power-of-two field degree reached by the tower, not merely the toy degrees. Trace nonzeroness follows either from the polynomial degree argument in the first candidate or from the explicit alpha_(2m)=alpha_m*t construction in the second. The image of z^2+z is exactly the trace-zero subspace, so the quadratic is irreducible. The direct trace-one element is indeed the highest tensor-basis bit. This simplifies deterministic setup without changing the family proof.
3. Four recursive lower-field products give M(2m)<=4M(m)+O(m), hence O(m^2) BIT gates. This correctly charges multiplication by the public trace-one constant as an additional product. Construct the classical straight-line circuit first, then reversibly compute/copy/uncompute it; recursively doubling already reversible subcalls is an unnecessary alternate implementation and is not the stated bound.
4. The first candidate's basis scan costs O(m^4) deterministic bit work. Its optional modulus construction is sound: the last tower generator has a Frobenius orbit of length m, because any proper orbit length divides m/2 and would put it in the embedded half-degree subfield. The conjugate product has binary coefficients and is irreducible. O(m^2) tower-field operations give O(m^4) bit work; O(m^2) bits suffice for its growing coefficient list/work. Direct tower evaluation can omit this conversion entirely.
5. Independent uniform m-bit coefficients and an invertible Vandermonde minor give uniform field values at every set of at most k distinct points. A fixed surjective 256-coordinate projection gives independent FULL256 replies, including all lower limbs. With k=min(2T,V_b), the saturated case is the actual full finite-domain RF law; otherwise the limited-query theorem supplies exact bounded behavior. No claim of full RF-law equality is valid in the nonsaturated case.
6. Keeping Horner accumulators, computing each product in fresh output, and clearing arithmetic scratch realizes a clean XOR oracle even when the input field element is zero. Per-call O(km^2+b^2), key km, and clean work O(km+m^2+b^2) are conservative valid bounds. Field arithmetic is not unit cost. For T>=1, the total leading evaluation work is O(Tkm^2), ordinarily O(T^2m^2), not O(Tm^2).
7. The second candidate's O(km+b^2) initialization is a bit-write/descriptor claim. If an explicit full gate list must be emitted during initialization, charge O(km^2+b^2) additional circuit-generation work; that is absorbed by its stated whole O(T(km^2+b^2)) resource bound for T>=1. A succinct uniform recursive evaluator needs only its public tower descriptor. This distinction does not invalidate the total polynomial bound.

## Quantum interface and application

The fixed length-plus-padded-byte representation and zero reply on invalid/noncanonical states must be used in BOTH the original finite oracle model and the family model. The second candidate makes that extension explicit, including routing validity. The first candidate's fixed common invalid reply is acceptable on the same matched-extension condition. No claim is made for a baseline that grants independent random replies to malformed encodings while the simulator returns zero.

Each oracle matrix entry is linear in its table indicators; after at most T total calls, final averaged density entries are polynomials of degree at most2T. Every term mentions at most2T distinct inputs. The moments agree under limited independence, yielding equality of the full averaged output state and every bounded final event. Classical honest calls can be purified as basis-state quantum queries. Thus setup, source generation, signing, suffix/C preparation, final verification/extraction, prekey queries and adversary queries must all contribute to T. Expected-only caps, observed input-length maxima, or a reset cap after setup do not suffice.

The preferred B-only route is the clean application. Keep the original source theorem and independent Selected/private environment unchanged; replace B's own outside function and preserve the complete final PRE/Row success distribution. The cap T_PRE=Q+H_setup+qH_mode+3224+254 and T_ROW=Q+H_setup+qH_mode+3224+17392 have the correct structural composition given the inherited reviewed source/adapter caps. Selected/Row challenge operations are separate auxiliary operations, not outside Eval calls, but their actual work remains separately charged. I do not independently recertify those numeric constants.

For type7, fix the independently sampled full Row function and other independent auxiliary randomness before applying Fact2; compute C and register its target as part of the adaptive program. Do NOT fix or condition on Y/c0 as independent advice when those values were computed from C and therefore depend on the outside function. Pre-sampling an independent full Row is a mathematical coupling, not a requirement to allocate its whole table in the actual implementation. The Row oracle/preprocessing costs remain part of the inherited external challenge interface.

The optional full SOURCE-comparator route is conditionally valid if every patch value/header test is an independent fixed auxiliary computation and the terminal event classifier has its complete charged base-query cap. One base-query patched XOR can be implemented by conditionally swapping the response register with a256-qubit |+> auxiliary response on the patch branch, issuing the base XOR, swapping back, then XORing the prescribed patch reply. The |+> response is unchanged by any XOR, so this uses exactly one base call. Merely issuing a base call into the real response and then adding a prescribed reply would be wrong. The arithmetic 4*32*15+16*255=6000 and 4*32+16+17=161 is correct; reachability/completeness of that protocol classifier remains an inherited/compiler obligation. This optional route is unnecessary for the B-only implementation acceptance.

Coefficients must remain internal to Eval. Function-dependent initial advice, secret-key inspection in target choice/cache/logging, fresh coefficient resampling per call, or a later uncounted query changes the compared algorithm and invalidates the replacement. Each coherent and honest classical Eval must use the SAME sampled polynomial.

## Independent executable controls

`toy_controls.py` ran under Python3.13 with `-I -B` and exited0. SHA256 `6a77af6696df3a09ac3adf415f364ecaeab352ee04a6a71421d0fad5724a5bc3`; results SHA256 `1e2f3506d22c22ab930cc61742075c8132410bcebefa3642b8ebe5cce9df424f`.

- Exhaustive associativity/distributivity in degrees1,2,4 and all65,536 degree8 pair tests for commutativity and absence of zero divisors passed.
- Trace-one/Frobenius controls in degrees1,2,4,8,16 passed. Independently computed conjugate moduli0x7,0x13,0x17b,0x178e7 passed polynomial-basis gcd/Frobenius irreducibility checks.
- All65,793 byte strings of length<=2 had distinct codes under BOTH candidate lexical rank and my sentinel injection. A negative bare-integer encoding aliases empty and one zero byte.
- Exhaustive GF4 coefficient tests give uniform outputs at all six distinct-point pairs; the degree3 family enumerates all256 complete four-point field tables exactly once, and its projected binary outputs are balanced.
- An exact rational one-phase-query density matrix equals the uniform-function density matrix under the pairwise-independent projected family.
- Three honest basis queries followed by one adversary basis query reveal a parity invariant in an incorrectly adversary-only-sized pairwise family: parity-zero probability1, compared with1/2 for RF. The correctly total-query-sized saturated family restores1/2. This is a concrete negative control for omitted honest calls.
- The inactive-|+> single-query patch router passed every one-bit base/prescribed/response/branch combination; the full256-bit construction is its tensor-product extension.

These finite controls detect concrete implementation and scope errors. They do not constitute a kernel proof of the general construction, a protocol source-call audit, or a quantum runtime measurement. No external candidate, source, manuscript, numerical theorem bound or prior receipt was modified.

## Closed and remaining obligations

Closed by this independent manual reading: deterministic field construction with charged arithmetic; injective finite encoding; full256 limited independence; clean reversible evaluation; exact general bounded-total-query replacement; and the B-only PRE/Row equality argument under inherited complete caps and independent auxiliary interfaces.

Remaining: conventional keyed PRE/PRF/TCR identification, fixed-SHA claims, category/q_max certification, physical termination/implementation refinement, and whole-source mechanization. Optional source-comparator/classifier source reachability is not newly certified here. This receipt does not close those frontiers.

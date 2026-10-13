# Independent numeric verdict

**COMPUTED.** `bounds.py` completed with exit code 0. `crosscheck_originals.py` completed with exit code 0 after fixing isolated-Python local module loading. All files and inputs are in English. No manuscript edit, timing experiment, key generation, cache construction, real SHRINCS attack, or peer-proof reading was performed.

## Evidence and reproducibility

Run from this directory with Python 3.13 and mpmath 1.3.0:

    python -I -B bounds.py
    python -I -B crosscheck_originals.py

The first script writes `bounds.json` and `bounds.md`; the second writes `ORIGINAL_CROSSCHECK.json`. The JSON records script hashes, original input hashes, numeric parameters, precision checks, omitted-tail bounds, exact count checks, raw component probabilities, and explicit nulls for all unestablished total-security quantities. No original script is imported by `bounds.py`. Original-script imports happen only in the second, read-only crosscheck.

**COMPUTED.** Two algebraically different numerical methods are used: positive occupancy recurrence and finite alternating exponential moments. Both binomial and Poisson models are evaluated. The alternating moment result is checked at 160 and 220 decimal digits; its recorded relative precision difference is below 10^-90. Positive occupancy sums have analytic Chernoff bounds on omitted probability. These controls support the reported digits; they are not a machine-checked floating-point interval-arithmetic certificate.

| Signatures q | Fixed-instance FORS+C bits per raw digest try | Poisson bits | Complete EUF-CMA bound |
|---|---:|---:|---|
| 2^24 | 178.421820108 | 178.421820079 | OPEN |
| 2^30 | 167.771253729 | 167.771253728 | OPEN |
| 2^38 | 143.262538581 | 143.262538581 | OPEN |
| 2^40 | 132.563419944 | 132.563419944 | OPEN |
| 2^41 | 125.902530385 | 125.902530385 | OPEN |
| 2^44 | 98.521203051 | 98.521203051 | OPEN |
| 2^50 | 20.122193182 | 20.122193182 | OPEN |
| 2^64 | 9.000000000 | 9.000000000 | OPEN |

**COMPUTED.** At q=2^40 the binomial/Poisson discrepancy is about 2.18e-11 bits, well below 0.01 bit. The positive sum's omitted-tail upper bound relative to its covered probability is approximately 8.47e-737. At q=2^64 the saturation deficit is less than 3.10e-3557, explaining the 9-bit ceiling. The original R6 function refuses its high-load q=2^64 path with `AssertionError`; the original IA Poisson window gives 8.99999998889 bits. Neither failure was silently substituted for an exact original-script computation.

## Exact target-sum counting

**COMPUTED / PROVED formula.** Integer DP and independent grouped inclusion-exclusion agree on 300 randomized cap/sum cases, all 1,936 pairs of the 44-point toy slice (w=4, ell=4, S=6), and 44 one-point antichain checks. Original H1 and CE count routines agree on 20 independent sampled pairs for each actual LULA configuration.

| Actual configuration | Exact slice cardinality | Slice bits | Raw digest filter cost |
|---|---:|---:|---:|
| w=16, ell=32, S=240 | 5181241160064611531897369560287267312 | 121.962709151 | 6.037290849 bits |
| w=256, ell=16, S=2040 | 454918678781617793203528879683071744 | 118.453091993 | 9.546908007 bits |

**COMPUTED (hypothetical reuse only).** Over 128 independent pairs per configuration, the sampled mean inclusive per-hash coverage corresponds to 33.8424 bits for the 32-chain configuration and 25.7420 bits for the 16-chain configuration. Sample medians are 38.5133 and 27.8270 bits. These small Monte Carlo samples are illustrative component statistics; they are neither rigorous population bounds nor evidence of a real SHRINCS forgery. The script also evaluates three hypothetical encodings, with all raw vectors and exact example counts saved.

**PROVED (scope distinction).** H1's count is inclusive; CE's experiment subtracts the number of signed vectors, assuming distinct vectors. For a general input, subtract only the number of DISTINCT vectors. More importantly, a fresh message can collide with an existing accepted encoding: one signed vector has inclusive coverage 1/2^128, so it is incorrect to assign zero EUF advantage merely because the slice is an antichain. All totals must include that digest-binding route.

## Reference signer invariant and inventories

**PROVED (code-level mathematical invariant; not a machine verification).** In the original benchmark library:

- `tree_leaf` (line 470) selects the full tree coordinate and leaf coordinate from the 41-bit index.
- `child_value` (line 486) binds layer zero to a fixed FORS public key and higher layers to a fixed child subtree root.
- `WotsC::grind` (line 228) chooses the smallest accepted counter for a fixed address and fixed child value.
- `Signer::sign` (line 601, canonical uncached branch line 642) signs this invariant child value and passes the fixed subtree root to the next layer.

Therefore repeated honest reference use of a complete WOTS address reveals the same position vector. The event 'one reference address signs two distinct child messages' is impossible under the fixed-key reference semantics. This does not close the chain/hash-binding security terms; it removes an incorrectly proposed occupancy-based two-message-reuse term. It does not cover arbitrary accepted cache-counter substitution.

**COMPUTED (whole addressed universe, not security-loss factors).** Layers 0..4 have 2^36, 2^31, 2^26, 2^21, and 1 subtrees, and respectively 2^41, 2^36, 2^31, 2^26, and 2^21 WOTS key addresses. Their total Merkle position counts, including leaf public keys, are 4,329,327,034,368; 135,291,469,824; 4,227,858,432; 132,120,576; and 4,194,303. There are 19,140,298,416,324,608 addressed FORS secret leaves and 72,638,667,948,032 WOTS chain starts, giving 19,212,937,084,272,640 distinct PRF secret-derivation input addresses in the entire parameter universe. A lazy hybrid would query each input at most once; repeated recomputation does not create a new distinct PRF input. Actual signer touched inputs and adversary-selected query budgets must still be bounded in the reduction; this inventory cannot be substituted for them without explaining the loss.

**COMPUTED.** The top cache has 4,194,303 nodes and 2,097,152 counters, totaling 75,497,456 bytes of node/counter arrays. Signature layout is 16+4+17*(9+1)*16+4*(4+32*16+5*16)+(4+16*16+21*16)=5,720 bytes. All five WOTS-plus-path serialized parts are exactly 596 bytes; the final one has fewer chain values and a longer authentication path.

## Toy checks

**COMPUTED.** The fixed seed is 2026101217, with independent offsets for separate experiments. For h=8,a=3,k=4,q=256, 30,000 direct coverage trials produce 26 successes (0.000866667); the exact binomial model gives 0.000852026 and lies within the 99.9% Wilson interval [0.000459516,0.001633981]. For w=4,ell=8,S=12, a fixed cohort of 64 hypothetically twice-signed keys has exact inclusive raw-digest coverage 0.006024837; 30,000 trials produce 185 successes (0.006166667), within interval [0.004847209,0.007842464]. These validate model formulas, not a complete toy EUF-CMA oracle implementation.

## What the request's security equations do not establish

**PROVED (arithmetic).** If a classical conditional per-query advantage bound p is supplied by a valid reduction, Q_H attempts have union bound min(1,Q_H*p). At q=2^40, p=2^-132.5634 would give component exponent 4.5634 at Q_H=2^128; it would not give total advantage 2^-128. At q=2^38 that exponent would be 15.2625. Work-factor bits and residual advantage exponents are different quantities.

**ASSUMED reading, not QROM proof.** Plain square-root search interprets the q=2^38 and q=2^40 FORS work factors as about 2^71.6313 and 2^66.2817 quantum iterations. It says nothing by itself about the full QROM signer, exact quantum losses, or the requested f(Q_q,q). No QROM limit is computed in this directory.

**OPEN (smallest missing obligations).** Supply an adaptive transcript/query lemma upgrading fixed-instance average coverage into the relevant EUF-CMA bound; prove PRF and message-randomizer replacements for the actual secret-prefix/truncated SHA implementation; prove WOTS child/digest binding and chain forgery extraction with exact oracle losses; prove the exhaustive tree/hypertree divergence reduction; then combine the games and account for shared primitive domains. Cache-counter substitution and the quantum game require separate treatment. Until those obligations are closed, no smallest q for *total* 128-bit security exists as an established result.

**Paper-printable verdict:** “Complete EUF-CMA security of LULA I is not established. The independently reproduced fixed-instance FORS+C coverage model gives 143.2625 and 132.5634 bits per digest trial at 2^38 and 2^40 signatures, respectively; these component figures are not a reduction for the complete signer.”

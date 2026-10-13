# LULA I proof audit

## Proved statements

1. Correctness, conditional on successfully generated keys, terminating searches, honest cache entries, fixed parameter set and complete output. Chain completion reconstructs every endpoint; path induction reconstructs every root.
2. Deterministic transparency for honest complete/absent cache states and deletion of whole configured layers. Canonical smallest counters, fixed child values and seed-derived subtrees produce the same bytes and agree on termination for successfully generated keys in the mathematical interface. This does not establish all-message totality or native failure handling.
3. Atomic rollback transfer for one common deterministic reference function. It preserves keys, all public transcripts, and the union of signed messages. Q signing queries map to Q reference queries, with no probability or additional adversarial hash-query loss. Local bookkeeping uses O(number of commands) word-RAM operations with sequential handles; honest signing-oracle work and handle bit costs are separate. Shared termination behavior is a necessary premise.
4. Constant-sum vectors form an antichain under coordinatewise domination. This is a combinatorial property, not full WOTS+C security.
5. Generic split-secret counterexample: each frozen/linear-path signer can be reduced to a secure base signer, yet two rollback branches reveal both independent shares of its secret key. This demonstrates the absent converse.

All proofs are written mathematical arguments. No Lean/EasyCrypt proof check is claimed. The old EasyCrypt artifact is unexecuted historical material.

## Unresolved cryptographic obligations

| Obligation | Needed evidence | Present boundary |
|---|---|---|
| Seed/PRF derivation | Exact model and addressed multi-target reduction | Secret-prefix hashes are not automatically HMAC |
| Message randomizer | Security for exact prefix/truncation construction under adaptive inputs | Standardized SLH-DSA uses different function/interface |
| Hmsg/selection | Bound adversarial R/counter steering, routing and accepted-object acquisition | Uniform occupancy evaluates only one attack |
| FORS+C | Complete adaptive few-time-key bound with target and query losses | No generic EUF upper bound established |
| WOTS+C | One-digest-per-address proof plus digest/counter substitution, inversion and collision bounds | Canonicality helps repeated-certification exposure only |
| Merkle/root compression | Explicit binding properties, addresses and target counts | Truncated outputs require exact attack-model accounting |
| Whole composition | Single-key EUF-CMA at Q=2^40 and declared T/q_H | Open; do not label occupancy exponent a security level |
| Quantum | QROM/primitive/whole-composition reductions, separate resource model | Open; generic Grover scale is not a theorem for scheme |
| Two-branch extension | Domain separation, outer-root binding, union-of-branches reduction | Conditional; single-reference equality is inapplicable |
| Faults/writes | Cache integrity and canonical counter check; parser/crash semantics | Alternative accepted counter changes native output |
| Mid-call restore | Complete execution-state and publication model | Atomic model only |
| Timing/other leakage | Leakage-aware security game and constant-time/side-channel audit | Public transcript game omits time |

## Counterexamples and interventions

The replayed reset-randomizer toy forges with 2,712 hash trials; its two controls were not forged by that procedure. The replayed random-start counter toy forges after six distinct digests and eight candidate counters, while its canonical control fails to forge within 2^20 attempts. The native accepted-noncanonical-counter test changes output on the same message and verifies. These are mechanism-specific falsifications with bounded controls, not proof of the surviving scheme.

## Source corrections retained in manuscript

- Replace “only deterministic key-derived memory is safe” with equality/joint simulation of observable signing behavior. Random eviction/diagnostics can be harmless.
- Replace general stateful/stateless equivalence with the one-way freeze implication and the stronger sufficient common-reference condition.
- Replace “worst signing100586” with observed sample maximum. Model tail112189 is probabilistic, not WCET.
- Count prefix initialization:3265 instrumented,3266 executed verification compressions for32-byte input.
- Separate the ideal occupancy exponent from full classical security. No inherited FIPS/SPHINCS theorem is applied to mismatched functions.
- Give source-exact setup expectation; recovered model overcounts by2^22 relative to total executed expectation under its uniform search model.

## Submission verdict

A self-contained research case-study manuscript is built. The complete 128-bit classical security theorem, quantum theorem, hardened implementation, certified timing and broad novelty assessment remain open. Authors must assess whether this limited contribution is suitable for submission. No IACR acceptance or scientific certification is asserted.

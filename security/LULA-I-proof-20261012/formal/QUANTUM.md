# Quantum-security lane: independent derivation

This document was derived independently before reading the other agents' new reports. Labels apply to individual claims. It neither edits the manuscript nor establishes a complete security bound.

## Verdict and notation

**OPEN — a QROM EUF-CMA theorem for the actual LULA I implementation is not established.** No numerical maximum signing capacity follows from the cited theorems without the missing reductions below. The cheap Grover reading can be computed for an assumed attack predicate, but it is not a reduction for this signer and does not certify NIST category 1.

Use `q_s` for classical signing-oracle queries and `Q_q` for the adversary's quantum hash-oracle queries. `D_q ≤ Q_q` is quantum query depth. A reduction uses `Q_B` queries, not necessarily `Q_q`; hashing the simulated signing responses and checking the final forgery can increase this budget. Classical signing access is the model here; no superposition signing oracle is claimed.

**PROVED (arithmetic distinction):** a search work exponent of 64 does not mean success probability at most `2^-64` after `2^64` queries. A generic 128-bit-output preimage search can attain constant success at order `2^64` quantum queries. **CITED:** NIST categories compare attack resources with specified benchmark primitives; they are not fixed statistical failure probabilities ([official evaluation criteria, A.5](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post-Quantum-Cryptography-Standardization/Evaluation-Criteria/Security-%28Evaluation-Criteria%29)). Therefore the objective's phrase “2^-64-equivalent” must be separated into a chosen query budget and an independent success threshold.

## Plain Grover reading

**ASSUMED:** suppose an attack reduces to coherent unstructured search over a fixed Boolean predicate of marked density `p_F(q_s)`, with each predicate call implemented coherently and its cost counted. Then constant-success search takes order `p_F(q_s)^(-1/2)` predicate queries. These are not necessarily one SHA-256 call each.

**COMPUTED (conditional on that model):** if `b_F=-log2 p_F`, the associated query-work exponent is `b_F/2`. The independent numeric lane's binomial values give 71.631269291 at `q_s=2^38`, 66.281709972 at `2^40`, and 62.951265192 at `2^41`. `quantum_arithmetic.py` reads and hashes its `../numerics/bounds.json`, preserving the fixed-instance scope, and evaluates conditional search arithmetic for all eight requested capacities. These exponents describe the FORS predicate only, not the full signer. A 128-bit hash-output search separately has generic exponent 64.

**OPEN:** the selected address, accepted counter, and revealed leaf sets depend on adaptive signing and grinding. One must prove that the target predicate has the required joint distribution under that adversary and oracle history. Averaging a fixed-instance binomial distribution does not prove the selected-set QROM property. Repeated messages provide deterministic repeats, not independent new draws.

## Exact published tools and their hypotheses

**CITED — average-case search:** Hülsing–Kudinov, ePrint 2022/346, Theorem 4 (citing HRS16), states `Succ ≤ 8 λ (Q_B+1)^2` for the specified random Boolean-function distribution of marked density `λ`. This is a query upper bound on success in that problem. Using `λ=p_F` is conditional on a distribution-preserving reduction, which is missing for LULA I. Source: [Recovering the tight security proof of SPHINCS+](https://eprint.iacr.org/2022/346), §8 / Theorem 4.

**CITED — adaptive SM-TCR:** that paper Appendix E, Lemma 5 gives

`Succ_SM-TCR(A) ≤ 32 (Q_q+1/2)^2 / 2^n + 16 Q_q^2 / |P|`.

It constructs two `2 Q_q`-query adversaries: an average-search adversary and one distinguishing a programmed public-parameter slice. The game has distinct challenge tweaks, a classical target/challenge oracle, a two-stage adversary, and a random tweakable function. The hidden-then-revealed public parameter and challenge restrictions are part of the game, not optional implementation details. LULA I needs a simulator showing that its public seed, accepted-digest grinding and hash domains meet these conditions.

**CITED — selected-set WOTS+C:** SPHINCS+C, ePrint 2022/778, Appendix E, Lemma E.4 gives the same concrete expression for its `S-TCR(+C)` game. The selected-counter oracle `O+C`, allowed tweak prefixes and distinct addresses in that definition are essential. Appendix D, Theorem D.1 reduces multi-instance WOTS+C EUF-naCMA to this selected-set property plus WOTS-TW security, with additional time `d · len · w` measured in tweakable-hash evaluations. It is not a direct EUF-CMA theorem for any fixed-sum encoder or arbitrary SHA concatenation. Source: [SPHINCS+C](https://eprint.iacr.org/2022/778).

**CITED — semi-classical O2H:** Ambainis–Hamburg–Unruh, *Quantum Security Proofs Using Semi-classical Oracles*, Theorem 1 gives

`|P_left − P_right| ≤ 2 sqrt((D_q+1) P_find)`

when `G,H` agree outside a set `S`, with the stated jointly distributed inputs, oracle puncturing and Find experiment. There is also a square-root-probability statement and special punctured-game variants with smaller constant. This formula does not mean “halve the hash bits” or “lose ten bits.” A concrete LULA I hybrid must define `S`, the programmed oracle, the Find event and bound `P_find`. Source: [author's publication page](https://kodu.ut.ee/~unruh/publications/semiclassical.html), [primary proceedings paper](https://www.iacr.org/archive/crypto2019/116940359/116940359.pdf), ePrint 2018/904.

**CITED — repaired SPHINCS+ composition:** 2022/346 Theorem 3 sums PRF, PRF_msg, ITSR, SM-UD (with factor `w`), SM-PRE, several SM-TCR terms and SM-DSPR. It does not reduce only to SPR. Its Table 1 explicitly labels the tight multi-target SM-DSPR and ITSR generic bounds conjectured, and SM-PRE partly based on that conjecture; the later formalized proof must be distinguished from a proof of ideal-function bounds. These hypotheses cannot be erased by writing “QROM.” Source: [2022/346](https://eprint.iacr.org/2022/346), Theorem 3, §8 / Table 1.

## The “approximately ten bits” statement

**CITED:** Kudinov–Nick, *Hash-based Signature Schemes for Bitcoin*, revision 2025-12-05, §13 pp.30–31 distinguishes (a) generic attacks, (b) reductions with assumed hash-property advantages, (c) reductions plus QROM property bounds. It reports approximately 123 bits for standardized parameters under option (b), and roughly ten bits loss when adding certain provable-property constants under (c). Footnote 8 says FORS+C security there still uses a generic-attack approach. It subsequently selects parameters by option (a). This is an explanatory comparison for those constructions, not a plug-in ten-bit correction for LULA I. Source: [ePrint 2025/2203](https://eprint.iacr.org/2025/2203).

**COMPUTED (illustration, not a LULA bound):** setting `n=128`, `|P|=2^128` in the published SM-TCR formula gives approximately `48 Q_q^2 / 2^128` for large `Q_q`. Relative to the coefficient-one expression the success-bound loss is `log2 48 = 5.5849625` bits, or `2.79248125` bits in constant-success query-work exponent. At `Q_q=2^64` this upper bound exceeds one and is vacuous after clipping; this is not an attack or evidence of insecurity. Additional reduction factors, budgets, decision-problem bounds and composition terms matter. Thus ten bits cannot be recomputed for LULA I until its reduction is supplied.

## Per-term obligations

| Term | Status | Smallest remaining obligation |
|---|---|---|
| PRF and PRF_msg | ASSUMED / OPEN | Actual keyed SHA calls must be modeled by quantum-secure PRFs or reduced with exact key and query budgets; deterministic outputs are pseudorandom only computationally and under that hypothesis. |
| FORS+C coverage | COMPUTED model / OPEN QROM | Distribution-preserving adaptive selected-address / selected-counter coverage reduction with concrete `Q_B(Q_q,q_s)` and abort behavior. |
| WOTS+C antichain | PROVED in Lean | Only vector non-extension at equal sums; still needs chain inversion, compression collisions, selected-digest security and correct one-message-per-address argument. |
| Merkle / hypertree | OPEN | First divergence is an exhaustive combinatorial split, but its embedding into the right distinct-tweak SPR/TCR challenge needs a concrete simulator. |
| Cache / rollback | PROVED conditional abstract transfer | Consistent restored states return the reference outcome; identify actual code refinement and permitted views. Arbitrary corrupt caches are not covered. |
| Composition | OPEN | List all actual hybrids, their selected-set and addressing hypotheses, distinguish `q_s`, challenge-target counts and `Q_B`, then sum concrete advantages. |

**OPEN — printable verdict:** “Post-quantum EUF-CMA security of the complete LULA I signer is not established. The FORS+C model has a conditional Grover search interpretation; a construction-specific QROM reduction and a certified quantum signing limit remain open.”

## Cross-review after independent derivation

**COMPUTED / independently cross-reviewed:** `../code-review/INDEPENDENT_CODE_GAME.md` was read only after the initial document above was saved. Its source-bound findings agree with direct inspection of release `lib.rs:601–668`: arbitrary cached accepted counters are retained, cached authentication paths are not checked by Sign, and the signature-return path does not run Verify. A second accepted counter can expose another WOTS vector. The numeric lane supplied the exact q40 per-try figure used in `quantum_arithmetic.py`; its conditional classical union exponent at `Q_H=2^128` is 4.563419944, not 128.

**PROVED (scope correction):** the conditional restoration theorem excludes cache exposure and arbitrary cache writes. Private measurement snapshots contain the secret seed. Cache contents being recomputable with the secret key does not establish efficient simulation from the public key; a secret-header snapshot cannot be offered to an adversary under the honest-rollback game.

**OPEN — exhaustive tree reduction:** the Lean list divergence theorem ensures a first differing position exists if two finite paths differ. For cryptographic extraction the comparison must be to the complete honest key graph, including unqueried addresses, rather than only previously observed signature paths. The path lemma does not supply that graph simulator or a numerical SPR/TCR loss.

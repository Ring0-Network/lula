# Trade-offs of LULA I against the alternatives, at a stated signing limit (for the paper)

Status: draft for the paper's author. Written 2026-10-12. The paper itself is not modified.
Every number carries one label: **[measured]** this campaign, **[derived]** computed here from a published formula or from our model files,
**[source]** copied from a cited document, **[premise]** assumed, not proved.

## 1. Why this document exists

The first campaign ranked nothing, because the candidates were built for different signing limits. A fair comparison fixes the limit first.
Two limits matter, and they give different answers:

- **2^64 signatures** (what FIPS 205 SLH-DSA-128s/128f are built for).
- **2^40 signatures** (LULA I's design point, from the research record R6A; the manuscript does not state it yet, see editor finding FND-001).
- **2^24 signatures** (NIST SP 800-230 initial public draft, April 2026, "limited-signature" parameter sets).


> **Standing limits (apply to every row and sentence below).** (a) LULA I's security under cache loss or restore is a **premise of the conditional transfer theorem** (the reference-signer bound is assumed), not a closed proof. (b) No attack was run against real SHRINCS; that a reused counter breaks it is an argument, not an experiment.

## 2. The claim to correct

An earlier note said the SP 800-230 set for 2^24 signatures (3,856 B) is smaller than LULA I (5,720 B), so LULA I's size advantage "could disappear".
Verified: **the numbers are right and the conclusion is conditional.** At 2^24 signatures a 3,856 B signature exists and is smaller than LULA I's.
It is not comparable at the other limits, and it pays in signing time (section 4).

## 3. Same security reading at several limits

Estimator: Fluhrer–Dang equation (1), the probability per hash query that a forger completes a FORS forgery, signatures spread by a Poisson
model over the 2^h leaves (file `R8/R8B-immutable-authority/work/ia_model.py`, which reproduces the published FIPS 205 and SP 800-230 signature sizes exactly:
17,088 / 7,856 / 3,856 B [derived, checked]). Value = −log2 of that probability, in bits. Only the FORS term is shown; WOTS+ and tree hashing are assumed at the
n = 16 level, as in FIPS 205. This is a classical few-time-signature bound, not a full proof.

| Parameter set | Signature | Bits at q = 2^24 | 2^30 | 2^40 | 2^50 | 2^64 |
|---|---|---|---|---|---|---|
| SP 800-230 SLH-DSA-128-24 (h22 d1 a24 k6) [source+derived] | 3,856 B | 128.6 | 95.9 | **36.1** | 0 | 0 |
| FIPS 205 SLH-DSA-128s (h63 d7 a12 k14) [source+derived] | 7,856 B | 207.0 | 201.0 | 191.0 | 180.0 | 133.7 |
| FIPS 205 SLH-DSA-128f (h66 d22 a6 k33) [source+derived] | 17,088 B | 240.0 | 233.9 | 218.3 | 196.5 | 131.4 |
| LULA I (FORS+C k18/k'17, a9, h41) | 5,720 B | not recomputed here | not recomputed | 132.6 FORS term [source: R6A record, exact FORS+C formula] | decays gradually [source: R6A] | not claimed |

Reading:

- The 3,856 B set is **only valid up to its limit**. At 2^40 signatures its few-time layer retains about 36 bits, far from 128. Using it beyond 2^24 is a break, not a degradation to be tolerated.
- LULA I's FORS term holds 128 bits at 2^40. The 5,720 B vs 3,856 B difference buys 16 more bits of signing budget in the exponent (2^40 vs 2^24), a 65,536× larger limit.
- LULA I's **hypertree bound at 2^40 is not established** [premise]; the 132.6-bit figure is for the FORS term only. The rollback theorem is a conditional transfer, not a proof.
- The 2^64 columns show why FIPS 205 is large: it pays for a limit nobody may need. LULA I does not claim 2^64.
- Limit: every LULA I figure in this section rests on the premise above (the reference-signer bound); none of it is a closed proof.

## 4. The cost side, at each limit

| Item | SP 800-230 128-24 | FIPS 205 128s | FIPS 205 128f | LULA I |
|---|---|---|---|---|
| Signature | 3,856 B [source] | 7,856 B [source] | 17,088 B [source] | 5,720 B [measured] |
| Public key | 32 B | 32 B | 32 B | 32 B |
| Signing, hot | about 1.52e9 SHA-256 compressions [derived] ≈ 0.2–0.26 s at 0.135–0.168 µs each (Kudinov–Nick figures) [derived, not measured here] | 268.6 ms median [measured] | 12.0 ms median [measured] | 4.60 ms median, cache in memory [measured] |
| Verification | 397 compressions [derived] | 0.268 ms [measured] | 0.719 ms [measured] | 0.141 ms [measured] |
| Persistent state | none required | none | none | optional 75,497,456 B cache; **no signing state** |
| Cost if the helper state is lost | none | none | none | 330.8 s and 346.2 s, N = 2 [measured]; about 5.5 min |
| Signing speed-up allowed by caching | yes: SP 800-230 states caching hypertree levels, or all of it, does not change security [source] | n/a | n/a | the design uses it |

About the 128-24 signing figure: it is dominated by two terms, FORS with a = 24 (6 trees of 2^24 leaves, about 3.0e8 compressions) and one 2^22-leaf hypertree layer (about 1.2e9).
Caching the whole hypertree would cost about 2^23 nodes × 16 B = 134,217,712 B [derived], a bigger file than LULA I's, and would leave the FORS term (about 3.0e8 compressions,
roughly 40–50 ms) untouched. No cache of the FORS trees is practical (6 × 2^25 nodes × 16 B ≈ 3.2 GB [derived]). LULA I's "no signing state" is measured on one key and rests on the premise above, not on a closed proof. This row was **not measured here**: a measurement on the M2 engine
is pending until the stability campaign finishes and the machine is quiet again.

## 5. Statement that the data supports

1. At **2^24 signatures**, SP 800-230 gives a smaller signature (3,856 B vs 5,720 B) and no state, at roughly 40–50× LULA I's hot signing time [derived, to be measured].
2. At **2^40 signatures**, the 3,856 B set is not secure (about 36 bits). The comparable stateless choices are Kudinov–Nick rows, which are research proposals, not standards.
   Rows built for 2^40 in their Table 1 [source, ePrint 2025/2203]: WOTS+C 3,952 B (h44 d4 a16 k8 w256, 3.57e8 compressions to sign); FORS+C 4,372 B; PORS+FP 4,036 B and 4,480 B.
   Measured here: the 3,952 B reconstruction signs in 3.6 s median and the 4,036 B third-party Go row in 1.9 s [measured, unoptimized]. They are smaller than LULA I by 1.2–1.8 KB and about 400–800× slower to sign.
3. At **2^64 signatures** only SLH-DSA-128s/128f apply; LULA I is out of scope there.
4. LULA I trades **setup and recovery cost for signing speed**: 45.2 billion hash calls and 2,216 s once [measured, N = 1] to build the cache, 6–8 s to load it, up to 5.5 min after a total cache loss.
   Nothing signed depends on the cache's age or content (measured on one key; security consequence is the conditional theorem, a premise, not a closed proof).
5. Limit on points 1–4: no attack was run against real SHRINCS, and LULA I's rollback security is a premise of the theorem, not a closed proof.

## 6. Trade-off against schemes with state (the backup problem)

| Question | Stateful scheme (SHRINCS stateful, XMSS, LMS) | Stateless (SLH-DSA, KN rows) | LULA I |
|---|---|---|---|
| What happens when a backup is restored? | The counter goes back; the same one-time key can sign a second, different message. | Nothing changes; there is no counter. | Nothing changes; the cache is only a speed-up. |
| Consequence | Forgery is easier after two signatures at the same index. For WOTS+C target-sum chains one signature is safe; two expose coordinatewise minima with sum below the target S. [derived, argument not run against real code] | None from a restore. | None from a restore [measured: 100/100 and 50/50 overlapping signatures byte-identical from an old snapshot]. |
| Capacity | SHRINCS stateful: 210 signatures, then a 2^32 fallback [measured: refusal at q = 211, fallback 3,680 B] | Limited by the parameter set (2^24, 2^40, 2^64) | 2^40 design [source: R6A] |
| Operator duty | Persist the counter atomically, forbid restores | None | Optional cache management |

Limits of this statement:

- The claim "a restored backup does not change what LULA I signs" is measured on one key and one old snapshot. Its security consequence rests on the conditional transfer theorem; the reference-signer bound is a premise.
- A silent rollback of SHRINCS was timed (324 B, 49 ms) but **no recombination attack was run**. That a counter reuse breaks a target-sum scheme is an argument [derived], not an experiment.
- Stateless schemes also repeat leaves by chance; their bounds in section 3 already count that.

## 7. What to write in the paper (suggested wording, for the editor)

- State the design limit of 2^40 signatures explicitly, with the 132.6-bit FORS figure and the explicit remark that the hypertree term is not established.
- Replace any "smaller than" or "faster than" claim by a table with the limit as the first column (sections 3–4).
- Name SP 800-230 128-24 as the smaller option **for 2^24 signatures**, and say it has about 36 bits left at 2^40.
- Report LULA I's cost as a pair: hot signing and verification, and the cache build and loss costs. Never report only the first.
- Keep "maximum observed latency" wording; do not turn any of these into a bound.

## 8. Not done

- No new timing of SP 800-230 128-24 on this machine; the 0.2–0.26 s figure is a hash-count conversion.
- LULA I's bits at q = 2^24 and at 2^30 were not recomputed.
- The KN rows' own security is the generic-attack analysis of the source; FORS+C had no formal reduction in that text.
- No second hardware platform; no stability claim here (that is the campaign in `M-measure/LULA-I-stability-20261012-b1/`, still running).

## 8b. To-do: compare at the same signing limit, including 2^64

Answer to the question "should we also evaluate LULA I at 2^64?": **yes**. Today LULA I is read at 2^40 and SLH-DSA at 2^64, which is not equal-limit.
Note: LULA I's hypertree height is h = 41, but its design limit is 2^40 signatures (R6A). Do not mix the two numbers.

- [x] T1 (done 2026-10-12). Compute LULA I's exact FORS+C bound (Kudinov–Nick formula, as in R6A) at q = 2^24, 2^30, 2^40, 2^50 and 2^64; fill the empty cells of the table in section 3.
- [x] T2 (done). State what LULA I actually offers at q = 2^64 with the current parameters (R6A says only "decays gracefully beyond 2^40"; give the number in bits, or say it is below 128).
- [ ] T3. If LULA I is below 128 bits at 2^64, find the smallest parameter change that reaches 128 bits at 2^64 (hypertree height, FORS trees k and a) and report its signature size, signing hashes and cache size. This is the equal-limit rival of SLH-DSA-128s (7,856 B) and 128f (17,088 B).
- [ ] T4. Run the same estimator on every candidate at 2^24, 2^40 and 2^64, and print one table with the limit as the first column.
- [ ] T5. Measure SP 800-230 128-24 on the quiet machine after the stability campaign; also measure a Kudinov–Nick row at 2^40 with an optimized implementation if one is available.
- [ ] T6. Close the two standing limits if possible: a proof or a precise statement of the reference-signer bound for LULA I, and a recombination attack on real SHRINCS.
- [ ] T7. Until T1–T4 are done, the paper must not say "LULA I is smaller/faster than SLH-DSA" without the limit beside it.

Limit: T1–T4 use a classical FORS-term bound. The hypertree term and the quantum reading stay premises.

## 9. Sources

- NIST SP 800-230 ipd: `M-measure/M2-sphincs-reparam/refs/nist_sp800-230_ipd.txt` (Table 1).
- FIPS 205 sizes and Fluhrer–Dang eq. (1): `R8/R8B-immutable-authority/work/ia_model.py` (self-check reproduces 17,088 / 7,856 / 3,856 B).
- Kudinov–Nick Table 1 (signing limits 2^40 and 2^30, 2^20): `M-measure/LULA-I-comparison-20261011-a1/sources/hashsig-go/spec/eprint-2025-2203-kudinov-nick.txt`.
- LULA I operating point (2^40, 2^-132.6): `R6/R6A-state-as-accelerator/REPORT.md`, `tex/ra.tex`, `tex/closing.tex`.
- Measurements: `M-measure/LULA-I-comparison-20261011-a1/results/FINDINGS.md`, `summary.csv`.

## 10. Result of T1 and T2: LULA I's FORS+C bound by signing limit

Computed with `forsc_log2_forge` (R6A `r6opt.py`, exact FORS+C formula, h = 41, a = 9, k = 18 with the last tree forced) and checked against the Poisson model of `ia_model.py` (both give 132.56 at 2^40). Bits = −log2 of the per-try forgery probability, FORS term only [derived].

| q | 2^24 | 2^30 | 2^40 | 2^44 | 2^50 | 2^56 | 2^64 |
|---|---|---|---|---|---|---|---|
| LULA I, bits | 178.4 | 167.8 | **132.6** | **98.5** | 20.1 | 9.0 | 9.0 |

- LULA I meets 128 bits up to about 2^41 signatures, not 2^44. Past 2^40 the bound falls fast (about 34 bits between 2^40 and 2^44), so the R6A phrase "decays gracefully beyond 2^40" does not describe this table. The editor must not repeat it.
- At 2^64 only the 2^-9 forced-tree term remains: LULA I gives no useful security there. T3 (smallest change to reach 128 bits at 2^64) is still open.
- Still the FORS term only; the hypertree term is a premise.

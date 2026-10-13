# Findings of the LULA I comparison campaign (2026-10-12; executor: Claude Sonnet 5.5; unreviewed)

All numbers are from `results/summary.csv` (generated from `raw/`). One pinned logical core (10), BelowNormal, one thread, machine
in use by other user processes (per-job load in `raw/load-records.jsonl`, typically 1-70 %). No quiet-machine cohort and no
synthetic-load cohort was run. N is small for several cells. "max" is always the **maximum observed latency**, not a guarantee.
Times in ms unless stated. Sizes are transmitted signature bytes.

## Hot signing and verification (message 32 B; the 1 KiB and 64 KiB rows are in `summary.md`)

| Candidate (evidence) | Signature | Sign N | Sign median / p99 / max | Verify median / p99 / max |
|---|---|---|---|---|
| LULA I, cache in memory (measured) | 5,720 B | 1000 | 4.60 / 5.72 / 30.5 | 0.141 / 0.190 / 5.63 |
| SLH-DSA-SHA2-128f, OpenSSL 3.5.7 (measured) | 17,088 B | 1000 | 12.0 / 21.8 / 44.1 | 0.719 / 1.02 / 3.91 |
| SLH-DSA-SHA2-128s, OpenSSL 3.5.7 (measured) | 7,856 B | 100 | 268.6 / 367.9 / 408.4 | 0.268 / 0.362 / 0.500 |
| SHRINCS author C B32, stateful (measured) | 324-3,508 B (grows 16 B per signature) | 200 | 48.5 / 71.8 / 96.7 | 0.120 / 0.273 / 0.642 |
| SHRINCS author C B32, stateless fallback (measured) | 3,680 B | 20 | 472 / 617 / 617 | 0.448 / 0.537 / 0.537 |
| SHRINCS third-party Go, stateful (measured) | 336-3,520 B | 200 | 6.34 / 14.8 / 21.0 | 0.029 / 0.056 / 0.376 |
| SHRINCS third-party Go, fallback (measured) | 4,064 B | 10 | 1,785 / 4,776 / 4,776 | 0.915 / 1.39 / 1.39 |
| KN 4,036 B, third-party Go (measured) | 4,036 B | 12 | 1,898 / 4,450 / 4,450 | 0.905 / 1.78 / 1.78 |
| KN 3,952 B, own reconstruction (measured) | 3,952 B | 20 | 3,614 / 4,128 / 4,128 | 0.542 / 1.12 / 1.12 |

## Recovery and cold paths (message 32 B)

| Event | Observation |
|---|---|
| LULA I, one-core key generation plus cache build | 1 observation: 2,216 s, 45.2 billion hash calls, cache payload 75,497,456 B, peak working set 122.8 MB, harness write 23.9 s |
| LULA I, fresh process with the persisted cache | N = 10: file load 6.2 s median (8.3 s max) then first signature 3.96 ms median (5.28 ms max) |
| LULA I, total cache loss (seed only) | N = 2 signatures in one process: 330.8 s then 346.2 s. The second is not faster: nothing re-warms. The historical 703.99 s was on a saturated machine |
| LULA I, old snapshot (two branches, same snapshot file) | 100/100 and 50/50 overlapping signatures byte-identical; see `snapshot-branches.md`. The signer holds no mutable signing state, so this is the expected result |
| LULA I, byte equality prepared / fresh / cache loss | 12/12 identical; 14/14 vectors pass the independent verifier (`VALIDATION.md`) |
| SHRINCS author C, detected state loss | **INVALID, withdrawn 2026-10-12.** The driver (inherited from the previous campaign's `m3_native.c`) called `shrincs_restore(sk.seed, ...)` with the 16-byte secret seed where the routine needs the 48-byte seed (`sk_seed ‖ sk_prf ‖ pk_seed`); the restored key therefore had a different public key, and the timings are for a different key. This was found independently by the manuscript's author-agent and confirmed from the saved vectors. The `shrincsC-detected-loss-*` cells in `summary.csv` must not be used. |
| SHRINCS author C, silent rollback (state reset before every signature) | timing only: 324 B, sign 49 ms; no recombination attack was run |
| SHRINCS author C, exhaustion | stateful signatures 3,636 / 3,652 / 3,668 B, the signer refuses at q = 211, fallback 3,680 B; 3 runs, every signature verifies |
| KN 4,036 B (Go), fresh process / cache absent | sign 2.0 s median (N = 3); 2.16 s (N = 2) |

## What the data supports, and what it does not

- LULA I signs at about 4-5 ms and verifies at about 0.14 ms in the hot state, with a 5,720 B signature, against 12 ms / 0.72 ms / 17,088 B
  for SLH-DSA-128f and 268 ms / 0.27 ms / 7,856 B for 128s. The price is state that is cheap to carry only if the 75.5 MB cache
  survives: a loss costs about 5.5-5.8 minutes for the next signature (one observation pair), and loading the persisted file costs 6-8 s.
- SHRINCS stateful signatures are small only at the start (324 B) and grow to about 3.7 KB before the 210-signature stateful budget
  ends; its stateless fallback has 2^32 leaves (below the 2^40 filter). Its fallback signing time grows with message length
  (3.6 s median, 10 s maximum observed at 64 KiB for the C code; 12 s median for the Go code). [inference] the grinding loop
  rehashes the message on every attempt; this was not isolated by a controlled test.
- The KN 3,952 B reconstruction signed in 3.2-3.6 s on the pinned P core, slower than the 2.2 s smoke on an efficiency core. Cause not
  isolated (load, SMT sibling, or P-core clocking); treat the cell as an upper bound for this unoptimized reconstruction, not as the
  authors' implementation.
- Verification of the KN rows and the SHRINCS fallback has tails above 1 ms (p99 1.1-1.8 ms).
- Not a ranking. The security-normalized cohort is **not established**: only SLH-DSA has a read reduction behind it and LULA I's
  rollback bound is a premise (`security-matrix.md`). SHRINCS stateful fails the 2^40 capacity filter and its silent rollback is unsafe by design.

## Not done

- No quiet-machine or synthetic-load cohort; the gate "controlled environment" was not met.
- No hash-call counts, CPU-time or cycle columns (recorded as NA); no per-phase peak memory except the LULA I build.
- SLH-DSA fresh-process/setup cells; S42 re-measurement; LULA I per-phase restore costs beyond file load.
- No recombination attack was run against SHRINCS silent rollback; no formal argument for any row.
- The paper (`LULA-I.tex`/`.pdf`) was not changed: baseline SHA-256 `bec2b482…d10c9` / `7cacf509…f28e` still hold.

## Corrections added on 2026-10-12 (after the first write-up)

- **Detected-loss cells withdrawn** (see the table row above). The corresponding line in `CELL-STATUS.md` ("detected state loss ... MEASURED") is superseded by this note.
- **Median convention.** `summary.md`/`summary.csv` use the midpoint median for even N. The campaign's own branch summary (`snapshot-branches.md`) used the upper middle value; the manuscript recomputed it with the midpoint.
- **Go adapter labels.** The Go adapter's `prepared`, `fresh` and `missing` scenarios run the same uncached algorithm; only the `fixture_load` interval differs. They are not cache-recovery measurements.
- **Exhaustion.** The `exhaustion` scenario installs stored index 207 and then selects the fallback itself; it does not call the stateful API at the switch point and therefore observes no refusal.
- **Stability.** None of the numbers in this folder is a stability claim. A controlled repetition is in `M-measure/LULA-I-stability-20261012-b1/`.

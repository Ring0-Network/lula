# RUNS — stability campaign b1 (UTC)

| # | When | What | State |
|---|---|---|---|
| 1 | 2026-10-12 15:07:46 | Second LULA I key: `LULA_KEY_BYTE=82`, `build/m3_ra_key.exe prepare LULA-I vectors/lula1-key2.cache`, via `bounded_run.py` on logical 8 (efficiency core), BelowNormal, timeout 12,000 s (pid 9648). Source change: `seed_a()` in the copy of `m3_ra.rs` reads `LULA_KEY_BYTE` (default 0x31 = the original key). Binary digests in `build/digests.txt` | running |
| 2 | 15:10 | Sampler `scripts/sampler.ps1` (1 Hz: total, logical 10, logical 11, frequency of logical 10, busy processes) writes `raw/sampler.csv`; stops when `raw/sampler.stop` exists | running |
| 3 | 15:15 | Protocol Amendment 1 (gate thresholds), written before any measurement of this campaign | done |
| 4 | 15:20 | Controller `scripts/stability_campaign.py` (pid 34700): waits for `vectors/lula1-key2.cache` and for `m3_ra_key.exe` to exit, then runs 6 blocks (hot cells, keys alternating) and 3 windows (5 fresh processes plus 1 cache-loss process each), each job behind the quiet gate | waiting for the key |
| 5 | 15:26 | `scripts/analyze.py` dry run on empty data | ok; rerun at any time, it writes `results/STABILITY-FINDINGS.md` with `STATUS: PARTIAL` until `raw/campaign-DONE.txt` exists |

Expected duration: key 2 preparation about 40–70 minutes on an efficiency core; the blocks about 5–8 minutes each plus 3-minute gaps; the three cache-loss processes about 6 minutes each. Gate waits depend on how busy the user's machine is; the gate log is `raw/gate.jsonl`.
Not yet done: the independent-verifier replay of this campaign's LULA I vectors (`raw/*.vec.txt`) and the byte-equality check across states; run them after `campaign-DONE.txt` (reuse `M-measure/LULA-I-comparison-20261011-a1/scripts/independent_check.py` with this folder's `raw/`).
| 6 | 2026-10-12 16:59 | The first controller start waited 20+ minutes at the gate because the machine was busy (a backup process, restic, used about 2 cores). The user closed their applications and authorized closing what was needed. restic (pid 30836) was **suspended** (not killed) with NtSuspendProcess; it must be resumed after the campaign (`raw/suspended-restic.json`). The WMI sampler was replaced by scripts/sampler.py because it used 20-90 % of a core; its output is kept as `raw/sampler-wmi-version-contaminated.csv. Controller restarted cleanly; the failed gate log is `raw/gate-attempt0-busy-machine.jsonl. No measurement had been taken. |

| 7 | 2026-10-12 20:29 | Campaign finished (`raw/campaign-DONE.txt`): 72 jobs, 0 failed, 0 contaminated, 0 gate timeouts. Sampler stopped. restic pid 27372 resumed; pid 30836 no longer existed. `scripts/analyze.py` rerun: STATUS COMPLETE. `scripts/verify_vectors.py`: independent verifier passed 36/36 LULA I vectors; byte equality: one signature per (key, message) across hot, fresh and cache-loss states | done |

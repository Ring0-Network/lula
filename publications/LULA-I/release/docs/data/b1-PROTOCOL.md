# Stability campaign b1 — protocol (written before any result of this campaign)

Date: 2026-10-12. Executor: Claude (Sonnet 5.5), no sub-agents. Trigger: the user's request "necesito que lo tengas todo bien medido, estable y todo eso".
Parent campaign (not modified, not merged): `M-measure/LULA-I-comparison-20261011-a1/`. This campaign repeats the cells that support the paper's headline comparison under controlled conditions and reports **stability** (between-block spread), not only a pooled distribution.

## What "stable" means here (fixed before measuring)

- A cell is **stable** if (i) its block medians span at most 5 % of their mean, (ii) every block passed the quiet gate, and (iii) the p99 of any block is at most 3x that block's median. Otherwise it is reported **unstable** with the numbers; a cell is never dropped for being unstable.
- A cell is **inconclusive** if fewer than 4 gated blocks completed.
- The maximum is always the *maximum observed latency*, never a bound. Nothing here certifies a worst-case execution time.

## Machine and pinning

- Intel Core Ultra 7 255U (2 P cores with SMT, 10 E-class cores), Windows 11 Pro 26300, Balanced power plan (unchanged; the plan is recorded, not altered).
- Timing core: logical processor 10 (P core). Its SMT sibling, logical processor 11, must be idle (gate below). One computational thread per job. Priority BelowNormal (the user's machine remains usable); the effect of this choice is recorded by the sampler, not assumed.
- Memory ceiling 2.75 GiB per job (job object), as in the parent campaign.

## Quiet gate (applied before every job, after a 5-second settle)

Pass requires, over the sampler rows of the last 20 seconds (at least 3 rows): mean total processor utility <= 30 %, mean logical 10 <= 8 %, mean logical 11 <= 8 %. If a gate does not pass within 25 minutes, the job is skipped and logged as `gate_timeout`; the block is then incomplete. Gate readings and timestamps are logged for every job, pass or fail.

**Amendment 1 (2026-10-12 15:15 UTC, before the first measurement of this campaign):** the thresholds first written were total <= 15 %, logical 10 <= 5 %, logical 11 <= 5 %, 20-minute wait. The first samples showed the user's machine busy with desktop applications and services (total 34-106 %), and the sampler itself needs about 1-3 s per sample, so the stricter thresholds and the 5-second window were unattainable. The timing core and its SMT sibling are the quantities that matter, so they keep a tight bound; the total bound is relaxed and the window widened. No result of this campaign had been seen when this amendment was made.

## Continuous sampler (whole campaign)

A separate low-priority process records once per second: total utility, utility of logical 10 and 11, processor frequency of logical 10, and the number of processes above 3 % CPU (names logged). Per job, from the job's start and end timestamps, the analysis reports mean/max of logical 11 and of the total, and mean frequency of logical 10. A job is **contaminated** if logical 11 averaged > 15 % or the total averaged > 45 % during the job, or if fewer than 3 sampler rows fall inside it. Contaminated jobs are kept in the raw data, flagged, and reported in a separate row; the stability verdict uses only uncontaminated jobs.

## Cells and sample sizes

| Cell | Per block | Blocks | Notes |
|---|---|---|---|
| LULA I prepared, 32 B / 1 KiB / 64 KiB (sign + verify) | N = 1000 each | 6 | blocks alternate key 1 and key 2 (3 blocks each); fixture keys, cache loaded from file |
| SLH-DSA-SHA2-128f, 32 B / 1 KiB / 64 KiB | N = 1000 each | 6 | OpenSSL 3.5.7, hedged (default) mode; a new key per process |
| SLH-DSA-SHA2-128s, 32 B / 1 KiB / 64 KiB | N = 200 each | 6 | same |
| LULA I fresh process (load + first sign), key 1 | 5 processes | 3 | one block of 5 per time window |
| LULA I cache loss (first sign after seed only) | 1 process | 3 | one first signature per process; independent processes, never "two calls in one process" |

Order of jobs inside a block is a seeded shuffle (seed 20261012); blocks are separated by at least 3 minutes of wall time. Keys: LULA I key 1 is the parent campaign's fixture (`LULA_KEY_BYTE` default 0x31); key 2 uses `LULA_KEY_BYTE=82` and is prepared on logical 8 (efficiency core) before the campaign starts.

## Validity checks run on this campaign's own output

Every LULA I vector is replayed through the independent Python verifier (`verify_ra.py`); signatures for the same key and message must be byte-identical across prepared / fresh / cache-loss states; the driver's negative tests must pass; every job must exit 0.

## Statistics reported (per cell, per block, pooled over uncontaminated blocks)

N, min, median (midpoint for even N), p95, p99 (nearest rank), maximum observed, block-median range, coefficient of variation of block medians, number of gated and contaminated blocks. Pooled quantiles are reported next to, not instead of, the block-wise ones.

## What this campaign does not control (stated in advance)

CPU temperature, power-limit throttling, other agents' use of the machine outside the gate, the OS's own background work below the gate thresholds. Hardware cycle counters are not available. OpenSSL is not a build equivalent of the Rust LULA I code; the comparison remains an implementation comparison, not a security-normalized one.

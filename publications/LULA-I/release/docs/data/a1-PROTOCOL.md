# Protocol (declared before any comparative result; written 2026-10-12 UTC)

Contract: the kickoff pasted by the user on 2026-10-11 (`00_orchestration/inputs/external_lula1_eval_kickoff_block1.md`).
One orchestrator-executor (Claude Sonnet 5.5) works alone. No agent was launched. The user's weekly limit is nearly
exhausted, so this campaign is partial by design: every cell below is MEASURED, PENDING or UNAVAILABLE with a cause.
Nothing is merged from M3.

## Machine and pinning

- Intel Core Ultra 7 255U, 12 cores / 14 logical, Windows 11 Pro 26300, 32 GiB, Balanced power plan (measured, `env/`).
- Compute core: logical processor 10 (P core with SMT). Sibling logical 11 must carry no campaign work.
- Every job runs through `scripts/bounded_run.py` (copy of M3's runner, SHA-256 in `build/digests.txt`): inherited
  affinity, BelowNormal priority, 2.75 GiB committed-memory limit, timeout, job-tree kill. One computational thread.
- Other user processes (browsers, backup app, MCP servers) were running and are not killed. Load is sampled per run
  where stated. No run is called "quiet" or "isolated".

## Statistics

- Hot cells: as many calls as the budget allows, up to 1,000. N planned and N achieved are always stated.
- Cold and recovery cells: N = 1 observation each; reported as one observation with its condition, never as a
  distribution.
- Reported per cell: min, median, p95, p99, maximum observed (nearest-rank), N. The maximum is called
  "maximum observed latency", never a worst-case guarantee.
- A timeout is a censored observation and a lower bound, never a finite maximum.

## Eligibility rules

- Whole-message processing is required for the primary cohort. Messages 32 B, 1,024 B and 65,536 B.
- An experimental harness serializer is labeled as such. A fresh process that redoes key generation is not a cache
  restore.
- A reimplementation carries its own label and does not take the row of a published optimized implementation.
- No security level is attributed to a row by name or by hash width.

## Planned cells and their state at the time of writing

See `results/CELL-STATUS.md`.

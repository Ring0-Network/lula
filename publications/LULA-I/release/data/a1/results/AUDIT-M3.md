# Audit of the previous campaign M3 (2026-10-11) — results of kickoff items 4.1–4.7 and section 16

Campaign folder: `M-measure/LULA-I-comparison-20261011-a1/`. The previous campaign `M-measure/M3-LULA-I-shrincs-kn-2026-10-11/`
is untouched. Nothing from M3 is merged into this campaign. Labels: [measured] script output here, [file] read from a
file, [inference] reasoning, not tested.

## Baseline identity (kickoff section 3)

[measured] `LULA-I.tex` SHA-256 `bec2b482…d10c9` and `LULA-I.pdf` SHA-256 `7cacf509…f28e` both match the kickoff.
The paper is unchanged by this work.

## Live process check (kickoff section 4)

- [measured] No process from M3 is alive. The only python processes are unrelated (backup app, sessions viewer,
  blender MCP).
- [file] `raw/LULA-I-full-prepare.process.json` still says `status: running` (start 2026-10-11T18:00:08Z, pid 13100,
  `affinity_mask 1`, no exit code). [measured] No process 13100 exists, no `m3_ra`/`ra` process exists, and
  `vectors/LULA-I.cache` does not exist; its stdout and stderr are empty. Conclusion: the full preparation never
  finished and left no cache. The `running` label is stale. It was NOT consumed.

## The seven findings

| # | Finding | Result |
|---|---|---|
| 1 | `kn4036-prepared-32.csv` | [measured] n = 12 signs, 12 verifies, 4,036 B signature in every row. Completed job does not validate the adapter as the best published implementation; Go with the timer problem in finding 2. KN rows stay "unvalidated adapter". |
| 2 | `ns = 0` durations | [measured] zeros are real rows of the Go timer, not instantaneous operations. Verify of stateful SHRINCS: 215/235, 37/40, 39/40, 39/40, 94/96, 8/8 zeros; KN verify 4–6/12 zeros. Nonzero values cluster at 0.50, 0.51, 0.53, 1.00, 1.01 ms. [inference] cause: Go's Windows monotonic clock follows the system timer tick (about 0.5 ms), so anything shorter reads 0 or one tick. Consequence: no sub-millisecond Go timing from M3 can be used. No epsilon was substituted and no row was dropped. Fix required before any Go timing: a QueryPerformanceCounter reading or batching many calls per timed interval. |
| 3 | `body_bytes` vs `sig_bytes` | [measured] they differ by 12 B (SHRINCS 324/336, 340/352, 1,012/1,024 and 4,052/4,064). The transmitted size must use `sig_bytes`. Stateful 336 B and 352 B signatures, 1,024 B at capacity rows, stateless fallback 4,064 B. |
| 4 | Native driver build | [file] `native-driver-build` failed with exit 1: `build/compat/arpa/inet.h:3` and `:4` redefine `htonl`/`ntohl`, which `winsock.h` already declares as `u_long PASCAL`. [inference] fix: guard the compat header (`#ifndef _WIN32`) or include `winsock2.h` there. Smoke executables `shrincs-c-b32.exe` and `shrincs-cpp-b32.exe` exist but are not campaign drivers. Not fixed in this session. |
| 5 | Full LULA I preparation | see "Live process check": never completed. A new one-core preparation was started here (below). |
| 6 | Topology | [measured] this run reads the topology with `GetLogicalProcessorInformationEx`: logical 0–1 are one P core with SMT (mask 0x3), logical 10–11 another (mask 0xC00), the other 10 cores are single-thread lower-efficiency-class cores (masks 0x4, 0x8, 0x10, 0x20, 0x40, 0x80, 0x100, 0x200, 0x1000, 0x2000), for 12 cores and 14 logical processors in total. Affinity to logical 0 or 4 alone does not isolate a physical P core when its sibling is busy. [decision] this campaign pins logical 10 and keeps logical 11 free of campaign work; sibling activity must still be logged per run. |
| 7 | Go settings | [file] `GOMAXPROCS=1`, `GOAMD64=v1`. Not audited further: GC threads, SHA dispatch and instrumentation costs are open. |

## Timer quality consequence

Any verification below about 1 ms measured by the M3 Go adapter is not a latency. Rows with `ns = 0` must stay in the
denominator of any M3 evidence and be marked "below timer resolution".

## Open obligations from this audit

1. Fix or replace the Go timer; re-time KN and SHRINCS stateful verify.
2. Fix the compat header and rebuild the native drivers, one worker, documented diff.
3. Complete the LULA I preparation (running, see `RUNS.md`) and validate the cache against the original vectors
   before any hot or recovery timing.

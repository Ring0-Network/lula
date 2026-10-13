# LULA I experiments

## Publication replay

Intel Core Ultra7 255U,12 physical/14 logical cores; Windows11; Rust1.97.1 x86_64-pc-windows-msvc, LLVM22.1.6; sha2=0.10.9. Release opt-level3, codegen-units1, LTOtrue. Native process sets affinity mask1 and BelowNormal priority before computation. Python replay sets the same affinity and priority for itself and its children. No foreign workload is killed or paused. Frequency, thermal state and foreign concurrency are not controlled. SHA backend is runtime-selected and no matched enable/disable ablation is claimed.

Full verification input is one recovered32-byte message/signature fixture. Small correctness input is64 distinct four-byte messages with two height3 WOTS layers and four height4 FORS trees. The miniature set is not the security parameter set in the manuscript.

| Scenario | N | Min ms | Median ms | p95 ms | p99 ms | Max ms |
|---|---:|---:|---:|---:|---:|---:|
| full_verify_ms | 1000 | 0.1334 | 0.1360 | 0.1465 | 0.1847 | 0.8732 |
| mini_hot_ms | 64 | 0.2037 | 0.2113 | 0.2327 | 0.2384 | 0.2709 |
| mini_absent_ms | 64 | 0.3750 | 0.3932 | 0.4159 | 0.4249 | 0.4697 |

`evidence/native-replay-final.json.raw.csv` contains all1000 verification durations in execution order; stats use nearest-index rounding with Rust tie behavior. Eight selected field flips and two nonexact lengths reject. All64 honest prepared/deleted/restored comparisons are byte-identical and verify. The accepted-noncanonical-counter write yields a different accepted signature. These are explicit finite assertions in the isolated driver.

An initial exploratory aggregate had a33.069ms verification maximum and a33.4401ms small-set cold maximum. It lacked raw repetitions. The final rerun added raw verification retention and was not requested to demonstrate a more favorable maximum; both aggregates are retained. Neither maximum establishes a bound on future latency.

## Replayed negative controls

Independent verifier:12/12 recovered signatures accepted; all per-vector changed messages/signatures rejected. Main set accounts for3 vectors. Restored-generator toy: forgery at2712 collision trials; fresh-entropy and deterministic controls resist that particular attack. Random-counter toy: six distinct accepted upper counters, forgery at8 search trials; canonical control resists2^20 tested candidates. See evidence output files and replay.json for exact commands, timings and exits.

## Historical full-scale data

| Scenario | N | Min ms | Median ms | p99 ms | Max ms |
|---|---:|---:|---:|---:|---:|
| SessionA signing |2000|7.5307|8.6292|10.1841|19.0632|
| SessionA verification |2000|0.2575|0.2904|0.3619|17.0741|
| SessionB signing |1000|3.6627|5.6331|7.5957|9.1269|
| SessionB verification |1000|0.1221|0.1942|0.2666|1.4863|
| Lifecycle prepared |200|9.0253|9.4523|18.7203|21.2229|
| Lifecycle restored |200|9.0427|9.9752|12.7912|14.7487|
| Lifecycle absent |1|703995.7424|703995.7424|not estimated|703995.7424|

Historical p95/raw per-operation repetitions are unavailable. No interpolated quantile is invented. Full-scale absent-case byte equivalence is observed, not rerun here. Affinity mask16, one benchmark thread, highest thread priority, varying foreign load,32-byte messages. Preparation used12 workers and took990.62s/383.01s in sessionsA/B,838.60s in lifecycle; rebuilding took14031.05s under saturation. These are setup+cache times, not single-core minimal key-generation latency. Peak working set122384384B is historical. Cache payload75497456B is exact and excludes allocations.

## Work audit

3265 instrumented verify calls omit one actual prefix compression. Valid total3266 for32-byte input. Hot signing fixed count96082 plus the FORS outer-trial count and four lower WOTS search counts. Observed signing max100586 is not a source-bound maximum. Recovered model heuristic tail112189 and mean96858 are distribution-dependent; the expected sign formula overcounts by1 and setup expectation by2^22 relative to actual total executed setup. Keygen rounded observed exponent35.396 remains historical.

## Required comparisons that remain incomplete

No completed controlled same-machine signing comparison against native SLH-DSA/SHRINCS/KN; no full-scale new hot/absent/keygen quantile campaign,64KiB message sweep, matched SHA backend ablation, atomic-crash test or certified WCET. Primary-spec size/work comparison is separated from latency. Existing measurement lane artifacts are preserved without claiming that running labels establish a live process or completed results.

## Partial comparison edition, 12 October 2026

See BENCHMARK_INTEGRATION.md and editorial/benchmark-r4 for the immutable cutoff, raw statistics, independent adapter audit, included recovery observations and pending cells. This extends the historical/replay record above; it does not replace those evidence classes.

## Final retained campaign cut, 12 October 2026 at 14:52 UTC

All four controllers and 81 retained processes completed. The 477-file snapshot contains 64 campaign CSVs, 132 operation groups and four LULA branch-vector files. BENCHMARK_INTEGRATION.md and editorial/benchmark-r5 are the current record; the earlier partial cut remains benchmark-r4.

The final edition incorporates42 Sign/Verify summary rows,4 branch-signing distributions,4 fresh-process paired-median rows,7 whole-process peak-memory rows and exact auxiliary signature-component decompositions. These are implementation observations under active host load, without a common-security rank or a guaranteed maximum. Campaign narrative corrections and continuing exclusions are documented in the integration record. Historical and earlier replay evidence above remain separate. No timing rerun occurred during integration.

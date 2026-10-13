# Retained-data reproduction

Run these commands from the release root with CPython 3.10 or later. The checks were executed with CPython 3.13. No third-party Python package is needed for either command.

```text
python -I -B analyze.py
python -I -B verify_vectors.py
```

The first command reads `data/` and writes `recomputed/`. It reaggregates elapsed measurements, independently checks the follow-up workload gates and declared stability criterion, and recovers historical table fields from their retained summaries. The second checks the public known-answer vectors with a separate implementation of the project specification, plus one message-bit and one signature-byte change per vector. A failed numeric or vector check exits unsuccessfully. Neither command invokes signing, prepares a key, loads a cache, or reruns a timed benchmark.

The principal generated files are:

- `recomputed/a1/summary.csv`: the retained campaign aggregation, including explicitly labelled untimed control rows.
- `recomputed/data/RECOMPUTED_DATA.json`: exact admitted first-campaign statistics, paired initialization samples, whole-process memory peaks, snapshot overlaps, historical summary-source fields, and the raw-duration publication replay.
- `recomputed/b1/stability_by_job.csv` and `stability_by_cell.csv`: follow-up campaign analysis.
- `recomputed/stability-audit/VALIDATED_STABILITY.json`: independent integer-nanosecond recomputation, gate windows, per-block and pooled statistics, telemetry checks, and saved-vector checks.
- `recomputed/verification/VECTOR_CHECKS.json`: the 14 first-campaign and 36 follow-up vector checks, with complete-public-key/message groups.
- `recomputed/verification/historical-independent-check.txt`: 12 historical vectors across four parameter sets.

For elapsed campaign statistics, medians are midpoint medians and p95/p99 use nearest rank. Untimed sentinels are not eligible for latency tables. The publication replay retains 1,000 decimal-millisecond durations; its quantiles use the historical Rust nearest-index convention, with half-integer index ties rounded upward. Decimal formatting residues below one nanosecond are rounded back to integer nanoseconds for that replay only.

`data/a1/admitted-rows.json` preserves the file lists and original admitted-summary assertions. The portable analysis recomputes every statistic from those raw files before comparing it with an assertion; it does not use the asserted median as its answer. `timing_eligible: false` identifies untimed controls in the generated JSON. The seven historical rows are different: only original aggregate summaries survive, so their fields can be independently rounded and checked, but their underlying distributions and missing p95 values cannot be reconstructed.

## Evidence and execution boundaries

The first campaign retains endpoint load samples; the follow-up retains a preceding-20-second workload gate and approximately one-second CPU busy-time sampling. All 72 follow-up timed jobs completed with exit code zero, and key-2 preparation is a separate process. No frequency-scaled CPU-utility guarantee or physical isolation of the SMT sibling follows. The implemented controller had no separate five-second settle delay. Temperature, instantaneous frequency, and short contention bursts were uncontrolled.

The follow-up uses two LULA I fixture keys, three prepared blocks per key, 15 fresh processes on key 1 with a 32-byte message, and three individual first signatures after cache loss. It does not estimate a dependable cache-loss tail from three points. SHA2-128s verification at 1 KiB and 64 KiB fails the declared p99/median stability criterion and remains reported. Maximum observed latency is not a mathematical worst-case bound. Backends, compilers, signing modes, and query assumptions differ; no common-security ranking follows.

Byte equality across prepared, reloaded, and absent-cache follow-up outputs is directly checked only for key 1 and the 32-byte message: 21 saved vectors. Other follow-up groups contain three prepared outputs each. Vector validation is finite correctness evidence, not a cryptographic reduction, malicious-cache guarantee, adaptive-forgery proof, or real attack against SHRINCS. The full LULA I reference-signer security bound remains a premise of rollback transfer.

## Sanitized archival records

Historical filenames and construction labels have been converted to public LULA I names. Host-specific paths have been converted to release-relative archival references. Recorded process arguments document the original invocation; a reference to an omitted binary or cache is not a directly runnable benchmark command. Numerical fields, timestamps, public keys, messages, and signature bytes are preserved. Two setup stdout records omit the `seed_hex` field containing benchmark key material. Their public keys, setup times, counts, and sizes remain available.

The release excludes cache fixtures, executable/build outputs, Go toolchains, private key files, and operating-system caches. Fixed benchmark seed-byte recipes can regenerate test fixtures through the separately documented code build. Public vectors contain public-key seed and root, message, and signature; the public-key seed is not a private signing seed. `data/COPY_HASHES.json` records pre- and post-sanitization hashes without disclosing host paths. The exact substitution and original-path mapping is retained privately by the editor.

The six archival campaign PDF plots are excluded: some display obsolete internal labels, while the old recovery plot uses a marginal-median sum, labels the minimum of two cold calls as the first call, and includes a withdrawn detected-loss measurement. The old cache plot also uses the smaller cold call rather than the first call. The current audited manuscript figures are released separately under `paper/figures/`. Plot regeneration and specification/model calculations are separate tasks from these dependency-free timing and vector checks. See the release's table-provenance map and model scripts for the distinct source, derived, and premise fields.

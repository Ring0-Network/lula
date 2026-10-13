# Commands and source binding

Read the actual source directly before any peer report for this new obligation. The independent first-save artifact is `DERIVATION.md`; subsequent additions clarify interface/composition limitations but do not replace that derivation.

Source subject:

- `publications/LULA-I/release/code/lula1/src/lib.rs`: SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.
- Parameter subject `publications/LULA-I/release/code/lula1/src/bin/lula1_driver_original.rs`: SHA-256 `a18799fba64ec1a6370e18e0d5d4b21108109cf9022fc8d7195e55d860a08c4b`.

PowerShell `Get-Content -Encoding UTF8` read the relevant direct-source slices; `Get-FileHash -Algorithm SHA256` measured these identities. An initial attempted read of nonexistent `lula1_driver.rs` reported file not found; directory inventory then located the actual `lula1_driver_original.rs`. No fallback source was invented.

Run from this directory:

```
python -I -B check_targets.py
```

Two runs returned exit code 0, before and after removing unused script bindings. The second run's output is recorded in `CHECKS.json`. It uses only the Python standard library, exact `Fraction`/integer arithmetic, and explicitly labelled high-precision approximate logarithms. The full exact symbolic tau is recorded without materializing astronomical powers.

Final validation checks both source hashes against these expected values and verifies a local SHA-256 manifest excluding the manifest itself. No timings, new dependencies, remote upload, global configuration change or proof-tool execution occurred.

# Portable code and retained experiments

These are publication copies of the owned measurement controllers, independent verifier, native LULA I library and drivers, and exploratory models. The original campaigns remain unchanged. The code uses Apache-2.0; dependency licenses are listed in the release NOTICE. The Rust library implements deterministic signing and honest-cache equivalence. Its rollback-security transfer is conditional on the applicable reference bound. Timing and cache availability remain observable; arbitrary cache corruption and a full adaptive reference reduction are outside the proved claim.

Place this directory at `code/` in the release root. Retained a1 and b1 inputs belong under `data/a1/raw/` and `data/b1/raw/`. Original data and new measurements are separate: controllers write to `reruns/a1/` and `reruns/b1/`; analysis writes to `generated/a1/` and `generated/b1/`. The optional environment variables `LULA_CAMPAIGN_ROOT`, `LULA_RESULTS_ROOT`, and `LULA_BUILD_ROOT` override these locations. Never point a controller at retained data when running a new campaign.

## Recompute retained statistics and verify vectors

From the release root, with Python installed:

```powershell
python -B code/controllers/a1/aggregate.py
python -B code/controllers/a1/independent_check.py
python -B code/controllers/a1/compare_snapshot.py
python -B code/controllers/b1/analyze.py
python -B code/controllers/b1/verify_vectors.py
```

The a1 analyzer retains the original midpoint median and nearest-rank percentile conventions. The snapshot comparator retains its historical upper-middle median convention. The b1 vector comparator groups by `(pk_root, message)` as the original script did; this script alone does not establish equivalence for arbitrary complete public keys. The shipped independent verifier checks signature validity and rejection of altered messages and signatures. These are finite controls, not an unforgeability proof.

`controllers/a1/plots.py` is the **historical diagnostic generator**, not the publication figure generator. Its recovery chart adds marginal medians and calls the smaller cold observation a first-signature estimate; its Pareto and two-point cache line also lack the final paper's separation of assumptions. The arithmetic is retained for provenance. Do not use these figures as the paper's reported evaluation. Use the separate publication regeneration script supplied at release level.

## Build the owned LULA I executables

The original build profile is retained: Rust edition 2021, optimization level 3, one codegen unit, LTO, no debug information, and `sha2 = 0.10.9` with compression support. Cargo.lock pins transitive versions. Use the compiler version recorded by the retained campaign when reproducing its build environment; a fresh compilation is a new binary and does not inherit historical timing measurements.

```powershell
cargo build --release --locked --manifest-path code/lula1/Cargo.toml -j 1 --target-dir build/cargo-target-lula1
Copy-Item build/cargo-target-lula1/release/lula1_driver_original.exe build/lula1_driver_original.exe
Copy-Item build/cargo-target-lula1/release/lula1_driver_seeded.exe build/lula1_driver_seeded.exe
Copy-Item build/cargo-target-lula1/release/lula1_snapshot.exe build/lula1_snapshot.exe
```

The original driver always uses fixture byte `0x31`. The seeded driver accepts decimal `LULA_KEY_BYTE`, defaulting to 49; the second fixture uses 82. Both variants are kept because the historical campaigns used different binaries. The fixed parameters named `lula1` serialize a 5,720-byte signature and a 32-byte public key. Auxiliary `mini`, `nc`, and `dual` driver options are retained historical controls; they are not LULA I performance or security results.

## Regenerate fixtures instead of distributing key or cache files

The fixture seeds are public benchmark inputs, not production keys. For each chosen byte, the driver repeats it 32 times, applies the existing SHA-256 fixture labels in the source, and derives the 48-byte seed deterministically. The original hash-input labels and cache-format magic remain unchanged; changing those bytes would change the experimental fixtures. No serialized secret key or cache is shipped.

Full LULA I cache preparation is expensive. The following commands execute it deliberately; they are not part of smoke checks:

```powershell
New-Item -ItemType Directory -Force reruns/a1/raw,reruns/a1/vectors,reruns/b1/raw,reruns/b1/vectors | Out-Null
python -B code/controllers/a1/bounded_run.py --cpu 10 --timeout 14400 --prefix reruns/a1/raw/lula1-full-prepare --cwd . build/lula1_driver_original.exe prepare lula1 reruns/a1/vectors/lula1.cache
$env:LULA_KEY_BYTE = '82'
python -B code/controllers/b1/bounded_run.py --cpu 8 --timeout 14400 --prefix reruns/b1/raw/lula1-key2-prepare --cwd . build/lula1_driver_seeded.exe prepare lula1 reruns/b1/vectors/lula1-key2.cache
Remove-Item Env:LULA_KEY_BYTE
```

Preparation prints the derived public benchmark seed, public key, cache sizes, compression count, and persistence time. The cache contains 75,497,456 payload bytes and a 75,497,573-byte serialized fixture for these parameters. `fixture-metadata.json` supplies hashes measured from both retained cache files; regenerated hashes must be checked against that metadata before claiming fixture identity. No cache hash has been inferred from the public key.

## External C and Go dependencies

The four C files in `adapters/` are owned harness or reconstruction code. External dependencies are unavailable in this bundle:

| Adapter | Required source/runtime | Historical build conditions |
|---|---|---|
| `slhdsa_ossl.c` | OpenSSL 3.5.7 libcrypto, with message-signing EVP exports | clang 22.1.8, `-O3 -mno-avx`; set `LULA_OPENSSL_DLL_DIR` to the DLL directory, or pass it as the optional final argument |
| `m3_native_shrincs_c.c` | SHRINCS C commit `345b0a64ce8d00c16c35952375dea6d13ec48c85` | clang `-O3 -mno-avx -DSHRINCS_B32 -std=c17`, OpenSSL development library, campaign compatibility modifications documented separately |
| `m3_native_shrincs_c_ex.c` | Same SHRINCS C commit and dependencies | Same flags; driver positions its counter near the endpoint and explicitly routes fallback; it does not test an upstream refusal API |
| `kn3952.c` | Same external address/hash/WOTS+C/XMSS primitives and reconstruction parameter changes | clang `-O3 -mno-avx`; 3,952-byte local reconstruction, not author code or interoperability evidence |

The SHRINCS C checkout lacks a verified redistribution license. Its bodies and copied headers, including the derived full configuration header, are excluded. Fetching a public checkout is not evidence that this release can redistribute it. The owned adapters alone cannot build those two SHRINCS executables or the KN reconstruction. Consult NOTICE for the exact upstream status and any separately supplied owned modifications. The controller expects output names `slhdsa_ossl.exe`, `shrincs-c-b32.exe`, `shrincs-c-b32-ex.exe`, and `kn3952.exe` in `build/`.

The Go controller requires [hashsig commit da711b11f03c4af0d610996f89848e9e15770b73](https://github.com/andrepatta/hashsig/tree/da711b11f03c4af0d610996f89848e9e15770b73), the campaign QPC timer adapter, and the new owned driver addition documented in docs/GO_ADAPTER.md. The campaign used Go 1.27.2, one build worker, `GOMAXPROCS=1`, `CGO_ENABLED=0`, `-trimpath`, and `-buildvcs=false`. Set `LULA_HASHSIG_SOURCE` to the externally prepared checkout's `go/` directory and, if needed, `LULA_GO` to the Go executable. `build_go.py` preserves an offline module proxy and local caches: required modules must already be present. It outputs `build/hashsig_driver.exe`.

With that external driver built, fixtures are regenerated by `hashsig_driver.exe prepare kn4036 reruns/a1/vectors/go-kn4036.json` and `hashsig_driver.exe prepare shrincs reruns/a1/vectors/go-shrincs.json`. The pinned driver uses deterministic public fixture seeds. The upstream C fixture uses the upstream key-generation RNG; a new C fixture does not reproduce the old key by merely repeating a command. No original serialized C secret fixture is included.

## Run new measurements and exploratory models

The a1 sequence is `run_campaign.py`, then `run_shrincs.py`, `run_go.py`, and `run_extra.py`. Each latter controller waits for its preceding completion marker. Scripts preserve the original logical CPU 10, seeds, repetition counts, message sizes, waits, memory limits, BelowNormal priority, timeouts, and serial execution. CPU 10 must exist and have its topology checked on the new host; affinity alone does not establish a matched physical machine or controlled load. b1 requires `sampler.py` running in another terminal before `stability_campaign.py`; it retains its original six-block gate and sampling rules. These commands are full campaigns, not quick validation commands.

The three `models/` files retain their exploratory numerical functions. `ia_model.py` prints component occupancy estimates; `r6opt.py` supplies historical helper functions without a main routine; `rollback_reuse.py` writes `generated/models/rollback_reuse.out.json` or the path in `LULA_MODEL_OUTPUT`. The last model assumes uniform encodings and is not a real SHRINCS forgery. Its main sampling experiment can take time. For a small control, import it and call `brute_force_check()` instead. The paper's final high-precision model tables use the separate release-level recomputation script, rather than promoting these historical approximations into security guarantees.

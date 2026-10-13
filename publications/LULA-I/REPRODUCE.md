# Reproduce LULA I

Run from this publication directory. Original research files remain unchanged. `private/source-snapshots.json` maps the public LULA I name to original internal source paths and SHA256 hashes. A source hash pins the subject even though this research directory has no Git repository/commit identity.

## PDF

```powershell
pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex
bibtex LULA-I
pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex
pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex
```

Dependencies: MiKTeX/TeXLive with llncs, splncs04, algorithm2e, CM-Super, TikZ, placeins, booktabs and hyperref. Use the same manuscript/bibliography and replay-results.tex; do not regenerate result tables from unrelated runs.

## Bounded executable replay

```powershell
python -I -B scripts/replay.py
Push-Location private/implementation/work/rust
cargo build --release --offline --bin publication -j 1
Pop-Location
& private/implementation/work/rust/target/release/publication.exe evidence/vectors_RA36.txt evidence/native-replay-final.json
python -I -B scripts/finalize_docs.py
```

The internal vector filename is retained solely to locate the original implementation evidence. Replay is Windows-specific for CPU affinity/priority. Exactly one logical CPU is selected; physical-core isolation is not established. The source has SHA dispatch and the flags are in Cargo.toml; no target-cpu override is used. The helper writes raw verification durations next to the JSON result. Re-running changes observed timing results; preserve originals under a new path if comparing campaigns. Finalize_docs only regenerates supporting prose/tables from the selected stored result; it does not run a full-scale signer.

## Expensive historical full-scale reproduction

The private implementation contains original `ra.rs`/`decisive.rs`/`dual.rs` driver snapshots when included in the manifest. Original locators and commands are in the manifest. Main parameter string:

```text
18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1
```

Original driver example, run within its Rust crate after compiling its bin:

```powershell
cargo build --release --offline --bin ra -j 1
target/release/ra.exe LULA-I '18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1' 1 1000 output.json vectors.txt 1 1
```

This prepares the full cache and runs one uncached transparency signature. Budget tens of billions of setup compressions and billions for cold signing; the one-worker setup can take much longer than historical12-worker setup. The original driver raises thread priority; this is a documented reproduction of its behavior, not the publication's BelowNormal driver. Do not mistake it for a matched modern campaign. Use a new output directory and do not overwrite preserved historical artifacts.

Historical aggregate files cannot reconstruct missing raw samples or p95. The original spec/derivation and frozen-state controls are private source evidence. A replay of the copied controls does not create a whole-scheme proof.

## PDF QA

Use `pdftoppm -png -r 110 LULA-I.pdf qa/page`, inspect every rendered page and run `pdffonts`/`pdfinfo`. Source/log/text scans must show no undefined citation/reference, overfull box, forbidden internal name in manuscript/PDF metadata, or mismatched numeric table. PDF text and font inspection alone cannot prove visual correctness.

## Regenerating the first comparison, without new timing jobs

Run `python -I -B scripts/integrate_comparison.py` from this directory. It reads the immutable raw cut and the independently audited JSON, creates comparison-results.tex and two vector PDFs, and launches no benchmark. Python matplotlib is required. BENCHMARK_INTEGRATION.md records source provenance, timing boundaries, unfinished cells and the limits of reproducing historical executable inputs. Rebuild LULA-I.tex after regeneration; public source ZIP includes the generated input and figure PDFs, while the private package holds raw data and the generator.

## Current campaign edition (r5)

The result generator now reads editorial/benchmark-r5/campaign and its independent numerical audit. Run `python -I -B scripts/integrate_comparison.py`, then build LULA-I.tex as above. It launches no signing jobs. It regenerates the final primary/auxiliary/branch distributions, paired first-use and whole-process-memory tables, exact component decompositions and two corrected vector figures. SOURCE_MANIFEST.json pins all477 inputs. Original six campaign plots remain private evidence and are excluded unchanged because recovery aggregation, labels and cohort assumptions are unsuitable. See BENCHMARK_INTEGRATION.md for current scope and still unmet protocol conditions.

## Gated follow-up and analytical model (r11)

Extract all three private archives as described in PACKAGE_LAYOUT.md. `python -I -B scripts/audit_stability.py` reaggregates retained raw observations and saved vectors into qa/stability-recomputation; `python -I -B scripts/check_coverage_model.py` recomputes the seven coverage-model quantities into qa/MODEL_RECOMPUTATION.json. These commands launch no timing jobs or parameter search. `python -I -B scripts/integrate_stability.py` regenerates the follow-up input/ECDF from the frozen cut. Model outputs are not full security bounds. The retained75 MiB derived cache is digest-only in the package; raw timings and signatures do not require rebuilding it.

## Gated follow-up and analytical model (r11)

Extract all three private archives as described in PACKAGE_LAYOUT.md. `python -I -B scripts/audit_stability.py` reaggregates retained raw observations and saved vectors into qa/stability-recomputation; `python -I -B scripts/check_coverage_model.py` recomputes the seven coverage-model quantities into qa/MODEL_RECOMPUTATION.json. These commands launch no timing jobs or parameter search. `python -I -B scripts/integrate_stability.py` regenerates the follow-up input/ECDF from the frozen cut. Model outputs are not full security bounds. The retained75 MiB derived cache is digest-only in the package; raw timings and signatures do not require rebuilding it.

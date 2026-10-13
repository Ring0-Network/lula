# LULA I reproducibility bundle

LULA is Ring0 Labs' research family of hash-based signature schemes. This bundle accompanies **LULA I: Rollback-Resilient Hash-Based Signatures with Cache-Accelerated Signing**, published by Lugel Labs. It contains the manuscript, our implementation and experimental controllers, retained observations, public verification vectors and analytical models.

The bundle is prepared locally and has not been deposited publicly. The intended [GitHub repository](https://github.com/Ring0-Network/lula) was not accessible anonymously on October 13, 2026. This archive contains the manuscript, retained observations and reproduction tools; the repository link is not a verified public release.

## Read and reproduce

Read [the paper](paper/LULA-I.pdf), [its editable source](paper/LULA-I.tex), [security scope](SECURITY_SCOPE.md) and [third-party notices](NOTICE.md). Original benchmark records and release transformations have different byte hashes; the private handback preserves the exact provenance map. Public data retain numerical observations, time stamps and distributions while removing host paths, key material and private names.

From the bundle root, with Python 3.13:

```sh
python -m pip install -r requirements.txt
python -I -B analyze.py
python -I -B verify_vectors.py
python -I -B code/models/verify_paper_models.py
python -I -B code/models/verify_paper_tables.py
python -I -B code/models/regenerate_figures.py
python -I -B check_manifest.py
```

The first commands reaggregate retained observations and check saved signatures; they do not launch expensive signing benchmarks. Recomputed output goes under `recomputed/`, which is outside the frozen manifest. History summaries are source records, not recoverable per-call samples. The analysis report distinguishes direct reaggregation, derived arithmetic, published specification values and summary-only checks.

To build the paper, install a LaTeX distribution with `llncs`, `splncs04`, CM-Super, `algorithm2e`, TikZ, `placeins`, `booktabs`, `hyperref` and their dependencies, then run in `paper/`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex
bibtex LULA-I
pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex
pdflatex -interaction=nonstopmode -halt-on-error LULA-I.tex
```

This repository copy omits the author's contact email to meet the release's privacy requirement. The main manuscript retains the author-requested contact. The technical text, numbers, figures, assumptions and scientific limitations agree between those copies.

## What the measurements establish

The measurements come from one physical machine and jobs with a pinned logical processor. Affinity and a quiet gate do not prove exclusive physical-core use, fixed frequency or identical compiler and hash backends. The first campaign, gated follow-up, historical sessions and publication replay remain separate cohorts.

Maximum means maximum observed latency, never a mathematical worst-case bound. The follow-up's cache-loss evidence comprises three individual first-signature observations. SLH-DSA-SHA2-128s verification at 1 KiB and 64 KiB is unstable under that campaign's declared criterion. Warm-cache signing hides substantial preparation and recovery costs.

The author-selected objective is conditional use through 2^40 signing queries across all restored branches. The classical raw-candidate FORS+C model gives 143.3 at 2^38, 132.6 at 2^40 and 125.9 at 2^41; those figures concern the FORS term only. The full reference-signer and hypertree bound remains open. The rollback transfer theorem assumes an applicable reference bound, honest cache states and observations between completed signing calls.

No forgery was run against a real SHRINCS implementation. The counter-reuse calculations concern models; exact counting and independent controls do not establish a measured attack on the pinned implementation. No common-security performance ranking or certified signing capacity follows from the retained experiments.

## Files and licenses

- `paper/`: five TeX inputs, bibliography, metadata, vector figures and compiled PDF.
- `code/`: our native implementation, adapters, controllers and analytical models. External dependencies remain separately pinned and attributed.
- `data/`: retained timing, process, gate, sampler and public-vector records.
- `docs/`: protocols, analytical tradeoffs, source mappings, exclusions and reproduction limits.

The manuscript describes the mechanism, its conditional security argument, serialization and computational costs. Six tables retain the parameter, wire, work, component-model and selected latency results; its two diagrams explain the construction and the rollback counterexample. [Extended evaluation records](docs/research/extended-evaluation/README.md) preserve the detailed measurement procedures, full distributions, historical observations, analytical scenario grid and execution records. These materials remain outside the article. The table checker independently checks six current table labels (37 listed rows or fields) and 21 archived labels (141 listed rows or fields); the archive is not the current manuscript.

Our code is [Apache-2.0](LICENSES/Apache-2.0.txt). Our text, data, figures and documentation are [CC BY 4.0](LICENSES/CC-BY-4.0.txt). [LICENSE](LICENSE) specifies the scope. Third-party works retain their own terms and are excluded where a redistribution license could not be verified.

Cache files, compiled benchmark binaries, toolchain installations, operational secrets and stored private-key files are excluded. Benchmark fixture recipes use publicly documented deterministic bytes for testing only. Rebuilding a full cache is expensive and is not part of the saved-data checks.

`MANIFEST.sha256` binds shipped files except itself. `EVIDENCE-MANIFEST.sha256` separately binds the code, data, model and documentation payload; it excludes manuscript files. Generated analyses and build scratch are excluded from both manifests.

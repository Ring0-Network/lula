# LULA I reproduction-package layout

Extract these private evidence ZIPs into the same fresh directory:

1. LULA-I-research-package.zip: current public sources, implementation snapshots, historical evidence, scripts and earlier reviews. The current PDF is delivered separately to keep each Page upload below 10 MiB.
2. LULA-I-campaign-evidence.zip: all 477 frozen first-campaign files under editorial/benchmark-r5/campaign, plus their manifest.
3. LULA-I-stability-evidence.zip: editorial/stability-r11, including 398 retained follow-up files, timing/process/telemetry/vector records, baselines, model sources and independent audits. The 75,497,573-byte derived cache fixture is represented by digest rather than embedded; rebuilding it requires the recorded expensive preprocessing. Reaggregation and saved-signature checking do not require that fixture.
4. LULA-I-editorial-closure.zip: preserved historical R13 baseline, original build, claim/condition trace, two independent reuse audits, frozen model sources and reproduction checks. Its report describes the preceding 43-page/131-word revision, rather than the current cut. The exact already-delivered archive is preserved.
5. LULA-I-goal-closure.zip: historical R14 goal audit, 44-page/132-word revision records, complete updated sentence/condition and numerical-source maps, current build/visual/protection checks, task report and all-22-row portable model verification.

The current FINAL_STATUS.md and qa/EDITOR_BRIEF_COMPLETION_REPORT.md supersede older current-version statements. R13 receipts remain historical; current root sources and the R15 writing audit describe the latest prose cut. The optional LULA-I-abstract-review.zip preserves the preceding narrow 114-word edit and is not required data evidence.

LULA-I-source.zip is self-contained for typesetting: main source, four inputs, bibliography, bbl, metadata and three vector PDFs. Install llncs/splncs04, CM-Super, algorithm2e, TikZ, placeins, booktabs, hyperref and dependencies. Build pdflatex, bibtex, pdflatex twice. The extracted ZIP independently builds to identical PDF text; its PDF timestamps need not be identical.

For retained evidence, run python -I -B scripts/audit_stability.py and scripts/check_coverage_model.py; regenerate tables/figures with scripts/integrate_comparison.py and scripts/integrate_stability.py without launching timing jobs. Current model reproduction: python -I -B editorial/goal-r14/models/recompute_models.py --table operating-model.tex. Python, matplotlib and mpmath are needed. Exact source hashes, scope boundaries and original campaign contexts remain in the manifests.

Matched timing reproduction requires the separately pinned upstream libraries/toolchains and new output paths. Recorded hashes do not certify compiler equivalence, exclusive-core execution or full security. The private Page files do not establish public release or a code/data license; Q3 remains an author TODO. No real-SHRINCS forgery is launched by these editorial/model checks.

## Current writing supplement

LULA-I-writing-pass.zip contains the current writing audit and preserves earlier editions as historical evidence. Extract it last for the R15 review. The final 45-page PDF and all five current TeX inputs are delivered separately and in the source ZIP. The supplement contains the fresh baseline, claim/condition/reader trace, coverage of 95 nodes and 32 patterns, exact patches and rollback, and build, visual and independent source-ZIP checks. The isolated Z3 binary is excluded; install provenance and the reproduction command are included. Repository proposals are local artifacts, not a claim that GitHub contains them.


## Licensed local release

LULA-I-release.zip is the prepared repository tree: paper, owned code, retained data, source/notice/exclusion documentation, licenses and manifests. Its paper omits the contact email. The separate main PDF/source bundle retains the author-requested contact. Both have 45 pages and identical scientific source bodies.

LULA-I-release-audit.zip is private handback: exact original/public substitution maps, license-source evidence, independent checks and delivery receipts. It is not part of the public repository payload. The R15 writing archive and earlier technical/editorial archives retain their dated cuts. GitHub remains private and empty; no public release or remote mutation is implied by these local files.

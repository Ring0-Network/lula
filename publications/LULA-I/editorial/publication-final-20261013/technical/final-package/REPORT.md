# Independent delivery-package check

**ACCEPT within the reviewed mechanism-paper scope. No unresolved delivery finding.** The source archive, reproducibility archive and contact-bearing submission PDF exist and have the final hashes below. This receipt verifies local files; it does not establish public deposit, successful ePrint submission, full-signature security, a signing-capacity certificate or a security category.

| Deliverable | Independently computed SHA256 |
|---|---|
| `LULA-I-source.zip` | `0ee172e6b85b983c6cc4995ba48f826323717d0fe58eab57ce1eddf2cac7d140` |
| `LULA-I-release.zip` | `6546da0a82bae701816ec45b05b7060413a3784c0109d884f76a600bae21cb29` |
| `LULA-I.pdf` | `bc805dcfd00c4f8b489efba80311cb49fde8835618c719a4136b288484966110` |

## Source closure and archive contents

**COMPUTED:** The source ZIP has exactly nine unique, safely relative entries: the main TeX, bibliography, three live included TeX inputs, empty unused replay input, compiled bibliography, submission metadata and build README. Recursively following `input/include` finds the complete four-file live TeX closure. The bibliography is included. Both figures are native TikZ in the main TeX; there is no unshipped external image dependency. All eight entries that correspond to existing publication files are byte-identical to those files.

**COMPUTED:** The release ZIP has 887 unique members: exactly the 886 entries in `MANIFEST.sha256`, plus that manifest itself. Every listed byte hash matches. Its `EVIDENCE-MANIFEST.sha256` has 872 entries, all present and matching. Against the pinned pre-closure evidence manifest, 870 entries are unchanged; only `README.md` and `code/models/verify_paper_models.py` differ. Their exact before/after hashes independently match `root/PACKAGING.json`. The unchanged cryptographic source remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

**COMPUTED, bounded content check:** Archive names exclude private directories, Git state, caches/fixtures, binaries, target/build/generated/rerun/recomputed/output directories, Python bytecode and LaTeX scratch outputs. The text-format content scan finds no absolute `C:/Users` / `C:\Users` / `/home/user/` host paths or author contact in the release archive; no private-key PEM block or populated secret-key/seed hexadecimal JSON field is found. Public signature vectors and public-key fields are expected evidence. These checks support the exclusion of accidental private research/build material and identifiable secret payloads; a text-pattern scan is not a universal entropy or data-loss-prevention theorem. The contact deliberately included in the separate submission source/PDF is authorized publication metadata.

## Current versus repository paper

**COMPUTED:** The release paper and main paper have the same number of source lines. The exact sole TeX difference is line 40: the repository copy omits `\email{angel@r-0.org}` and its following line break. The `hypersetup` line is identical; all other main TeX bytes and the included inputs, bibliography and compiled bibliography are identical. No technical claim, figure, table or number differs.

**COMPUTED:** Both PDFs have 21 pages. Extracted page text is identical on pages 2–21, and identical on page 1 after removing the main copy's email line. Independent rasterization at 72 dpi yields byte-identical page pixels for pages 2–21. The contact is present on the main first page and absent from the repository first page and repository PDF metadata. Own first-page renderings were inspected; no clipping or malformed title/abstract was found. Root's complete visual review of all 21 main pages is separate cited evidence, not represented as a second complete visual review here.

The parent reported that an initial archive-build attempt used the main working directory and refreshed the main PDF's metadata. This review therefore binds the current `bc805dcf...` PDF, not the superseded `4bab4f33...` hash. Both ZIP hashes are unchanged. The refreshed `PACKAGING.json` now agrees with the current PDF. No technical-source difference was introduced by that rebuild.

## Real command checks from the packaged files

**COMPUTED:** The verified release ZIP was safely unpacked only under this reviewer's `technical/final-package/unpacked-release/` directory. Commands used the packaged scripts and their actual CLI defaults; generated output therefore remained inside this authorized review subtree, never in the delivered bundle.

The following all exited 0:

1. `python -I -B analyze.py`: retained-data reaggregation, telemetry checks and 36 existing public-vector replays with 72 changed-message/signature checks passed. This did not generate signatures, keys, caches or timing samples.
2. `python -I -B code/models/verify_paper_models.py`: current mechanism-paper scope checked exactly three FORS rows and separately checked all 22 archived extended rows. Its model outputs retain the component-only caveat.
3. `python -I -B code/models/verify_paper_tables.py`: six current tables / 37 checked rows and 21 archived tables / 141 checked rows passed. The preceding `analyze.py` is a required input-generation step, as ordered in the README; invoking this table checker alone in a fresh extraction before analysis lacks its generated JSON inputs.
4. `python -I -B check_manifest.py`: all 872 evidence hashes and 886 complete-manifest hashes passed after the commands; generated recomputation is excluded from the shipped namespace.

**CITED and independently checked as retained evidence:** Root's `SOURCE-ARCHIVE-CHECK.json` records four successful isolated LaTeX/BibTeX commands. The corresponding log hashes match the files in `root/source-archive-build/`. Independently reading that isolated compiled PDF confirms all 21 pages' extracted text equals the current delivered main PDF. This reviewer did not perform another compilation.

## Scope and preservation

The prior accepted technical review remains unchanged. No archive, manuscript, source, campaign datum, old scalar or private proof was edited by this reviewer. The only new cryptographic execution in this package check was verification of already-public retained vectors through the documented analysis command. No signing/key-generation/forest/cache construction, benchmark, forgery, timing experiment, upload or remote publication was performed.

`CHECKS.json` records the independent archive/hash/content checks and exact CLI outputs. `FINAL-PACKAGE-REVIEW.json` binds this report, the checker, the final subjects and the retained compile evidence. Acceptance is for delivery of the conditional mechanism paper; the original full-security goal remains unresolved.

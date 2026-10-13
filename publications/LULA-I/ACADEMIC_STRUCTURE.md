# Reader-ordered LULA I article

The author supplied the local Li et al. reference, *Efficient Pseudorandom Correlation Generators over Z/p^kZ*, as a structural example. The comparison concerns article organization and register, not its mathematical results or conference formatting. The supplied PDF, its contents, introduction/contributions/overview and efficiency treatment were inspected. The reference's cryptographic claims and complete proofs were not independently verified.

The local reference presents motivation and contributions, preliminaries, assumptions and constructions, then efficiency; supplementary mathematics follows the references. Its short performance context and explicit restrictions for broken parameters are scientific qualifications, rather than operational ledgers. LULA I adopts this reader order while preserving its existing A4/LNCS preamble and author-requested content.

## Current structure

1. Introduction, contributions and related work.
2. Preliminaries: notation, rollback game and observation model.
3. LULA I construction.
4. Correctness and security: canonical counters, cache transparency, rollback transfer, adaptive-branch counterexample and FORS+C component analysis.
5. Cache-accelerated signing.
6. Signature format and computational cost, including selected elapsed-time observations.
7. Discussion.
8. Conclusion.

References and the mathematical search/cost appendix follow. The requested final Note is retained. The abstract remains 94 words; both compiled PDFs have 21 pages.

## Changes and checks

Contributions no longer use C1-C5 checklist labels. Related work and the security definitions are subordinate to their explanatory sections. Correctness and rollback results form one security section. The component coverage model is placed with security rather than wire-format costs. Repeated reference-bound notices are consolidated without removing the abstract, threat-model, theorem or conclusion qualifications.

The preamble, five algorithms, two lemmas, one theorem, three proof bodies, mathematical environments, displayed formulas and two construction diagrams are unchanged. The bibliography source and all numerical table values are unchanged. The saved-data checker passes six current labels and 37 listed rows or fields, separately from its archived 21/141 scope. Builds have no unresolved references, changed-label requests or overfull boxes. All 21 main pages were visually reviewed; front matter, security boundaries, costs and the final note were also inspected individually.

Current TeX and extracted PDF text contain no evidence-manifest, author TODO, public-deposit placeholder, Creative Commons/CC BY license notice, license-management section or execution cutoff. Administrative and reproduction records remain outside the article. This review does not change repository legal terms, prove the open reference-signer bound or publish remotely.

Exact patches, baseline/source digests, build/visual checks and current package hashes are in `editorial/li-structure-20261012/`. The current generator is `scripts/academic_structure.py`; earlier generators are guarded against restoring their retired structures. Older reports describe their dated cuts.

Outcome: COMPLETE_WITHIN_SCOPE.

The follow-up recheck in `editorial/li-structure-20261012/RECHECK.md` confirms the cleanup. It adds one sentence identifying the six-block pooled latency samples and two LULA I keys; no numerical table value or cryptographic claim changed. Both PDFs and current delivery archives were rebuilt and checked after that clarification.

A final academic-register pass is recorded in `editorial/li-register-final-20261012/`. Five terminology/header edits remove residual control and adapter jargon and clarify the compact implementation security statement. All numeric table rows, abstract, mathematical bodies and bibliography were preserved. Main/repository PDFs and both current delivery archives were rebuilt; the isolated source archive produces identical extracted PDF text. All 21 refreshed page renders were inspected.

The 2026-10-13 genre recheck in `editorial/li-genre-final-20261013/REVIEW.md` independently confirms the absence of internal workflow material. One sentence describing proof length was replaced by its technical condition. Both 21-page PDFs and current source/repository archives were rebuilt; mathematical content and all numeric inputs remain unchanged.

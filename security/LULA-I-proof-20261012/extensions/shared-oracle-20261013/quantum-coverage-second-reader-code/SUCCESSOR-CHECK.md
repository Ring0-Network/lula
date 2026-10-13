# Corrected quantum coverage successor check

Outcome: **ACCEPTED_CORRECTED_MANUAL_QUANTUM_COVERAGE_SUCCESSOR_SCOPED**.

Reviewed immutable cut SHA256 `990aeb1067f9ac12235ef3982bc9d3d132cffeab5e704a7d0865a69d77e0c0ce` against successor `QUANTUM-COVERAGE-THEOREM.md`, SHA256 **24a031417b42ba03d266c638a4c3f94dae8887ffd8cf13f584b21387e6d01217**. Both hashes matched the requested pins. A complete `git diff --no-index` was inspected; its exit1 denotes the expected differences, not a failed check. `check_successor.py` exited0 and verified all12 indented formula lines are exactly unchanged.

## Exact material changes

| Locator | Successor change | Decision |
|---|---|---|
| Title / opening / status labels / §5 | Candidate/pending wording becomes manually reviewed scoped envelope, with source/AR and search review locators. Full-forgery composition remains a separate gate. | Consistent with accepted component reviews; no full-QROM or category promotion. |
| §3, honest-query ledger | Every new-message instruction, **including a sampled old-U collision**, makes one POST whole-row read and updates the namespace-keyed cache. Only later repeats reuse the latest cached row. | Resolves the ambiguous no-read collision sentence; matches the independently tested controller and Q+q+1 ledger. |
| §4, outer branch | The independently sampled BASE outer **function** is factored before adaptive input selection; a selected response need not be conditionally uniform. | Resolves the search-reader/source-reader wording issue. Pointwise marking is the proof mechanism; the selected output is not assigned a fresh iid law. |
| §4, inner branch | The same whole-function distinction is explicit; selected responses may be biased by quantum search. | Correct for the independently sampled BASE inner function and target set. |
| §4, advice / outer eligible branch | Advice is explicitly event-only; T identity is used only after the bridge. The final fresh outer branch excludes all padded namespaces, rather than merely already activated namespaces. | Consistent with the inner exceptional search targeting the padded q-U list. This clarification leaves no future padded-namespace gap and changes no bound. |
| §4, enlarged views / §5 limitations | The two search advice views must not be merged; full-forgery common-game composition remains separately reviewed. | Preserves the entropy/advice ordering required by the AR argument. Future target/template advice is not supplied to the original AR sampler. |

Global nonce sampler, guard order, finite coherent register, classical atomic service semantics, initiated-call convention, partial noncompletion, ROW codomain, primary AR constants, POST-query budget, collision overwrites, repeated-label handling, density terms, final two-call allowance and all equations remain unchanged.

The earlier one-row circuit and source/AR acceptance apply to this successor. The source hash binding remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`; no implementation edit is part of this promotion.

This receipt supplies the source/AR clarification gate for the **manual finite HJ COVER envelope**. It does not independently promote a complete signature quantum total, fixed-SHA theorem, efficient reduction, physical leakage claim, capacity guarantee or category certificate. Source, peer/root artifacts, manuscript and frozen proof packet were read only.

Reproduce the artifact-level check with `python -I -B check_successor.py`; `SUCCESSOR-CHECK.json` records the hash/equation assertions. Any later change to either pinned subject requires a new receipt.

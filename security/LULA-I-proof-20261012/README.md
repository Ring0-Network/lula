# LULA I security-proof packet

**Outcome: SCOPED_PROOFS_AND_COMPUTATIONS_COMPLETE_FULL_SECURITY_OPEN.**

This packet answers the author-provided proof request against the frozen implementation. It contains a complete obligation ledger, source-bound game, derivations and calculations, meaningful small machine-checked lemmas, counterexamples to overbroad requested premises, and an explicit **not established** verdict for full EUF-CMA/QROM security. Neither the paper nor the implementation was edited. No signature benchmark or full cache generation was run.

## Read and reproduce

1. Read `PROOF.md`, then `TERM-TABLE.md` and `OPEN.md`.
2. Read `code-review/INDEPENDENT_CODE_GAME.md` for exact verifier fields, primitive inputs, source anchors and cache controls.
3. Read `numerics/NUMERIC_REPORT.md` and `numerics/DERIVATION.md` for model scope and precision/tail limits.
4. Read `formal/FORMAL_REPORT.md` and `formal/QUANTUM.md` for checker, axiom, source and quantum-applicability records.

Run from this directory:

```powershell
python -I -B bounds.py --out results
python -I -B validate_delivery.py
python -I -B formal/verify_formal.py
```

The numeric dependency is `mpmath==1.3.0`, already present in the recorded environment. No installation was performed. `--h`, `--a` and `--k` change only the FORS coverage model; WOTS checks and inventories remain those of the actual fixed LULA I parameter set. See `numerics/requirements.txt`.

`bounds.py` reports every requested signing-query count. Full security terms remain null/OPEN; unknown is never encoded as zero. Outputs cover model per-candidate exponents, explicit hash-query-budget arithmetic, exact target-sum counting, toy coverage checks and conceptual address inventories. They are not a full signature attack or timing evaluation.

Formal replay uses the exact commands in `formal/ENVIRONMENT.json` and `formal/lean-local.json`. The local Lean/Mathlib and EasyCrypt toolchains already existed. AXLE checked the small abstract developments; Aristotle proved the independent antichain statement and its returned artifact was separately checked. No private signature source was submitted to obtain a proof. K tools were unavailable, so `formal/CacheSemantics.k` remains UNCHECKED with its replay command in the report.

## Independent criticism

The numerical and code/game agents each saved their independent derivation before reading the other's new work. The code agent subsequently reviewed every numerical term in `code-review/SECOND_READER.md`. Both reviewed the root synthesis; all three concrete review corrections were incorporated: total-oracle exhaustion wording, actual prepared-setup PRF count, and unrounded quantum exponent rounding.

## Current scientific verdict

Honest cache restoration preserves the common partial deterministic signing function, with zero signing-query/probability transfer loss in the stated atomic interface. Reference WOTS keys sign one fixed child value per complete address, so the proposed different-message occupancy-reuse attack model does not apply to honest operation. Accepted noncanonical cached counters nevertheless refute universal arbitrary-corruption transparency.

Full security still needs shared-hash/PRF, adaptive FORS, WOTS certification, tree extraction and composition reductions. The QROM property formulas documented in the primary sources cannot be imported without the construction-specific hypotheses. Neither a certified classical signing limit nor a certified quantum signing limit was established.

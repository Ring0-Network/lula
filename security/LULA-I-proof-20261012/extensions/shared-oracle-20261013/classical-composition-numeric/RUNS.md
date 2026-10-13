# Reproducible commands and checks

All commands run in this owned directory. Dependencies: Python 3.13 and the already installed mpmath 1.3.0. No signing, key generation, cache building, timing campaign, installation, manuscript edit, peer-file write, or private upload occurred.

1. Source-first reading and `INDEPENDENT_DERIVATION.md` save completed before reading new root/canonical composition proofs.
2. `python -I -B bounds.py`: an initial run exited 1 on the saturation assertion `upper <= 1/512`. Outward interval rounding can straddle this known exact probability cap for q=2^64. The valid interval was intersected with the analytically proved positive-expectation cap p_F <= 1/512; no formula or root coefficient changed. The repaired run exited 0.
3. The successful independent calculation saved `OWN-BOUNDS.json` and `OWN-BOUNDS.md` before either root numerical result was read. It uses 230-digit interval evaluation, a positive occupancy recurrence with omitted-tail control, and exact rational coefficient recombination.
4. Root outputs were then read. `python -I -B crosscheck_root.py` exited 0; all 16 rows and each displayed per-term decimal matched. The relative tolerances reflect 45-digit root serialization (30 digits for the negligible exhaustion term), rather than pretending rounded decimal strings are exact interval endpoints.
5. Formatting-only spacing in the generated cross-check Markdown was corrected, and the checker was rerun. This does not alter any numerical calculation or comparison.

Outcome: ACCEPTED_MANUAL_CLASSICAL_COMPLETE_SOURCE_RO_EVENT_BOUND and PASS_ALL_16_ROOT_ROWS_AND_CLASSICAL_TERM_LEDGER. Optional joint G/D7 sharpening is not used; actual SHA, standard-model reductions, work-factor certification, checked Rust refinement, and full QROM remain outside this accepted model result.

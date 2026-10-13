# Commands and receipts

1. Read source WOTS+C lines225–275 and actual `lula1_driver_original.rs` parameter literal with PowerShell `Get-Content -Encoding UTF8`; library hash `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.
2. Save the own source-first argument before inspecting supplied Lean declarations/receipt.
3. Read and hash `root-formal/SPRSeparation.lean` (`bec31567ae07abbdf8ae868b2d2f804fe469dce276d938bf6fdd8a24e1a425da`) and `SPRSeparation-check.json` (`49c4fde2f4d390bc9123f053cd446a8cde2ce453275b306a34df42f59865601f`).
4. Invoke the exact pinned existing WSL Lean4.28.0 / Mathlib command from the prior receipt. Initial invocation yielded a running exec session; polling completed with exit0 and all four axiom reports. `LEAN_RECHECK.json` records actual completion output. No new proof source, custom axiom or checker configuration was added.
5. Run `python -I -B control.py`; exit0. It writes the local exact countermodel `CHECKS.json`.
6. Recheck source/Lean/old-receipt identities and create/verify a local SHA-256 manifest excluding itself.

No installation, code/paper/frozen edit, remote upload or large benchmark occurred. Identity chain steps are explicitly the toy model; no LULA binary or SHA chain primitive is called by the countermodel.

# Commands and exact checking scope

1. Read pinned release `src/lib.rs` lines118–187 and the previously accepted `quantum-private-frontier/DERIVATION.md`; the already reviewed Sign/final verifier anchors were checked against the saved source binding. No new root/peer rare-event report was read before the first independent save.
2. Saved `INDEPENDENT_DERIVATION.md` SHA256 `8d0ee8492931f89dd27e7e5dc4328dc11aa011a3f3bbdb08a7a17f0bd7e43a17`, ran the initial exact block controls, and announced readiness to the parent.
3. Only after the parent supplied the review gate, read the entire `../QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md` and hashed it: `081545e57dd6ac3341bca85e4c2a22ff016747c4c58591a110324e80d397d8e2`.
4. Added the shared-terminal marked-XOR/phase and second-query active-prefix controls and ran `python -I -B control.py` from this directory. Exit0; output recorded in `CHECKS.json`. Controls use exact rational arithmetic and exact radical comparisons by squaring. They are finite channel controls, not implementation/signature-security proofs.
5. Read and hashed current deliverables; `REVIEWED-HASHES.json` binds read-only subjects and `SHA256SUMS.json` binds this lane's artifacts except itself. Native PowerShell `Get-FileHash -Algorithm SHA256 -LiteralPath` verifies the manifests.

The candidate and old conservative theorem/master/manuscript were never edited. No Lean, source build, benchmark, cache build, remote service or global configuration change was required. The proof is manual and its essential classical atomic-service/finite-register/refinement boundary is explicit.

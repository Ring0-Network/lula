# Cell status (final for this session, 2026-10-12)

MEASURED = raw data in `raw/`; AUDITED = earlier evidence read, not re-measured; NOT DONE / UNAVAILABLE = cause given.
All controllers finished (`raw/campaign-DONE.txt`, `shrincs-DONE.txt`, `go-DONE.txt`, `extra-DONE.txt`); every job completed with exit 0.

| Candidate / scenario | State |
|---|---|
| LULA I, one-core key generation and cache build | MEASURED, 1 observation (2,216 s) |
| LULA I hot sign/verify, 32 B / 1 KiB / 64 KiB, N = 1000 each | MEASURED |
| LULA I fresh process with persisted cache, 32 B, 10 processes | MEASURED |
| LULA I total cache loss, 32 B, 2 signatures in one process | MEASURED (N = 2) |
| LULA I old snapshot, two branches, 32 B and 1 KiB | MEASURED (byte equality 100/100 and 50/50; `snapshot-branches.md`) |
| LULA I independent verification and byte equality | DONE (`VALIDATION.md`) |
| SLH-DSA-SHA2-128f (N = 1000) and 128s (N = 100), OpenSSL 3.5.7, 3 sizes | MEASURED |
| SLH-DSA fresh process / context re-creation | NOT DONE |
| KN 3,952 B reconstruction (own code), 3 sizes, 3 fresh processes | MEASURED, labeled reconstruction |
| KN 4,036 B third-party Go, QPC timer, 3 sizes, fresh and cache-absent | MEASURED (N = 12 per size) |
| SHRINCS author C B32: stateful, fallback, silent rollback, fresh process, exhaustion | MEASURED |
| SHRINCS author C B32: detected state loss | INVALID, withdrawn 2026-10-12 (wrong seed layout passed to the restore routine; see FINDINGS.md) |
| SHRINCS third-party Go: stateful and fallback | MEASURED |
| M3 evidence (Go, coarse timer) | AUDITED only (`AUDIT-M3.md`); not merged |
| Security matrix | WRITTEN, provisional |
| Summary tables and 6 vector figures | GENERATED (`summary.md`, `summary.csv`, `figures/`) |
| Quiet-machine and synthetic-load cohorts | NOT DONE |
| Paper integration | NOT DONE |

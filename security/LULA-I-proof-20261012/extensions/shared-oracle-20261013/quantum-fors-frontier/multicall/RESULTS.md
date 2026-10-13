# Scoped quantum coverage arithmetic

**Candidate coefficients only; full QROM forgery totals remain null.** The source/ROW contract received this lane's manual acceptance in ROOT_REVIEW.md; root promotion still requires its independent review gate.

N=2^128, M=N^2-N. Q denotes coherent adversarial raw calls. All entries below use the root's with-replacement ROW game; the separate distinct-namespace integral bracket is in CHECKS.json. No timing or crypto implementation measurement was run.

| log2(q) | log2(Q) | FORS component bits | ROW envelope bits | Candidate source-COVER bits |
|---:|---:|---:|---:|---:|
| 24 | 32 | 178.421820108 | 87.9971877252 | 59.2284464888 |
| 24 | 64 | 178.421820108 | 72.0 | 0.0 |
| 30 | 32 | 167.771253729 | 81.8390359524 | 59.2284446992 |
| 30 | 64 | 167.771253729 | 66.0 | 0.0 |
| 38 | 32 | 143.262538581 | 70.9888160935 | 59.227692903 |
| 38 | 64 | 143.262538581 | 57.9999999893 | 0.0 |
| 40 | 32 | 132.563419944 | 67.9971877254 | 59.1928657541 |
| 40 | 64 | 132.563419944 | 55.999999957 | 0.0 |
| 41 | 32 | 125.902530385 | 66.4985924922 | 57.7432672824 |
| 41 | 64 | 125.902530385 | 54.999999914 | 0.0 |
| 44 | 32 | 98.5212030507 | 61.9998239113 | 31.5211284551 |
| 44 | 64 | 98.5212030507 | 51.9999993121 | 0.0 |
| 50 | 32 | 20.1221931818 | 52.9999972483 | 0.0 |
| 50 | 64 | 20.1221931818 | 45.9999559738 | 0.0 |
| 64 | 32 | 9.0 | 31.9999999998 | 0.0 |
| 64 | 64 | 9.0 | 31.5 | 0.0 |

A zero exponent denotes a capped probability1: a vacuous sufficient envelope, not a proved attack. Component bits are negative log probabilities at the displayed budgets, not security-category certificates. At q=2^40,Q=2^32, honest post-instruction reads change the ROW term from an unjustified roughly2^-72 to the safe roughly2^-67.9972.

Checks: two independently arranged source-square calculations, six positive-binomial/Chernoff-tail checks against the alternating exact moment identity, direct toy full-digest coverage versus exact binomial occupancy, collision/latest-row behavior, completion-selection bias, mandatory honest reads, disjoint full-image target counting, and Reprogram output non-disclosure. First-call eight manifest entries unchanged.

240-digit arithmetic plus analytic real-number brackets and numerical slack is reported honestly; this is not a formally verified directed-rounded implementation.

**Outcome: ACCEPTED_MANUAL_SCOPED_QUANTUM_COVERAGE_ENVELOPE_FIXED_NONZERO_SEED.**

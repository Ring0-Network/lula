# LULA I claim ledger

This ledger distinguishes source facts, proved statements, conditional cryptographic statements, historical observations, and new bounded executions. No score is a security certificate. C07 and C21 are retained historical entries from the wider research program, not claims of this manuscript.

| ID | Claim | Status and evidence | Boundary or falsifier |
|---|---|---|---|
| C01 | The fixed format has 5,720 signature bytes and 32 public-key bytes | Derived from `Params::sig_bytes`, serialization, independent parser and three main-set KATs; `sec:cost` (Signature format and computation costs) | Other parameter sets have other sizes |
| C02 | Seed material is 48 bytes | Direct split in KeyGen | Expanded root/context/cache add storage |
| C03 | Cache payload is 75,497,456 bytes | Exact integer formula and historical payload accounting | Not peak RSS or allocation total |
| C04 | Honest complete/absent/restored caches produce the same signature | Proved for successfully generated keys and honest modeled states, including agreement of termination; deterministic induction; new 64-message miniature comparison; historical two full-scale uncached comparisons | Does not cover edited entries, partial frames, timing, malformed container state |
| C05 | A common deterministic reference signer transfers EUF-CMA to atomic rollback with equal advantage | Proved shared-partial-oracle transcript simulation, zero signing-query/probability/adversarial-hash-query loss, constant word-RAM bookkeeping per command; honest signing work is separately counted | Reference security is an explicit unproved premise |
| C06 | Frozen-state security alone does not imply rollback security | Generic split-secret construction in `sec:rollback` (Rollback resilience) and recovered C7 countermodels | Different claim from cache transparency |
| C07 | Coverage-model per-raw-trial exponent is -132.5634 at 2^40 signing queries | Numerical evaluation of uniform binomial occupancy and independent indices | Not total EUF advantage or a 128-bit reduction |
| C08 | Valid 32-byte-message verification records 3,265 compressions; actually executes 3,266 | Source derivation and new 1,000-repeat counter assertion; uncounted Ctx prefix initialization adds one | Valid signature, exact source, fixed message length |
| C09 | Prepared signing count is 96,082+G_F+sum(G_j) for 32-byte input | Exact source accounting | Searches variable; observed 100,586 is not a maximum over keys/messages |
| C10 | Setup historically recorded log2 count 35.396 | Historical rounded counter; expected model source-corrected in paper | Not exact fixed count, not one-core wall time; model overcounts expected executed setup by 2^22 |
| C11 | Prepared medians 5.6331/8.6292/9.4523 ms | Three separately labeled historical scenarios | Different load and samples; do not combine into one controlled run |
| C12 | Full-scale cache loss took 703.9957424 seconds | Historical n=1, identical bytes, 8,602,614,065 counted compressions | Not rerun; insufficient for a latency distribution |
| C13 | 720 restore schedules showed no gain for a toy cache model | Historical toy-family record | Not 720 production cryptographic experiments; no 128-bit implication |
| C14 | A restored message-independent randomizer permits the reproduced toy collision forgery | New replay of recovered control, exit 0; 2,712 hash trials | 22-bit routing; controls resist only that tested attack |
| C15 | Random-start upper counter caching permits the reproduced toy recombination forgery | New replay, six digests, eight forging counter trials, exit 0 | Control's 2^20 failed attempts do not prove security |
| C16 | Acceptance of a corrupted counter is insufficient for byte transparency | New native miniature control: different accepted output for same message | Arbitrary-write fault model; not by itself an EUF forgery |
| C17 | New verifier replay has N=1000, p95 available, full raw durations | `evidence/native-replay-final.json.raw.csv` and source driver | One fixed fixture; original exploratory max 33.069 ms retained |
| C18 | Current SHRINCS draft pk48B, stateful548-4619B, fallback5777B | Primary SHA-pinned draft retrieved 2026-10-11 | Specification declares proof TODO; differs from earlier author-code parameters |
| C19 | KN3952 and KN4036 have distinct component sets | KN component choices motivate source-identified reconstructions; retained auxiliary same-host observations in `sec:benchcomparison` | No checked exact conformance/reduction; no common-security winner |
| C20 | No complete full-instantiation 128-bit classical or quantum proof supplied | Proof audit and manuscript `sec:security` and `sec:limits` | Do not infer from architectural similarity, occupancy calculation, or finite controls |
| C21 | Dual extension is distinct and adds a tag and other root | Exact original dual source; +17 bytes per branch | Needs joint two-branch/outer-root reduction; cannot use one-function theorem |
| C22 | Novelty is limited to audited integration and case-study evidence | Related work includes prior caching, counter compression and variable layers | A comprehensive novelty study remains open |

Public naming is LULA I throughout; internal implementation locators appear only in the private manifest/reproduction package.

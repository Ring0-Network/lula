# Independent second-reader review: canonical targets

Outcome: **ACCEPTED_MANUAL_CLASSICAL_TYPE7_EVENT_AND_TOP_READINESS_ONLY**.

I saved `DERIVATION.md` and an independently written exhaustive control before reading any canonical-targets report. I then read `canonical-targets/DERIVATION.md`, `RESULTS.md`, `check_targets.py`, `CHECKS.json`, `COMMANDS.md`, and its manifest. No material error was found in the stated target-event lemma or exact top-cache probability. No source, manuscript, earlier proof packet, or peer report was edited.

## Per-obligation verdict

| Obligation | Verdict | Independent reason / exact source anchor |
|---|---|---|
| One honest child per type-7 address, independent of own restriction | PROVED in the stated typed RO experiment | `child_value` 486–496 returns FORS PK or lower root; `compute_subtree` 479–484 uses endpoint PKs. WOTS PK 251–262 and tree/FORS builders do not consult type 7. Honest cache roots are computed independently of stored counters. |
| Literal input injectivity | PROVED for selected parameters | Header is S16\|zero48\|Addr22 plus V16\|counter4: exactly **106 unpadded bytes**. `Adrs::new` 73–78 truncates layer to u8, so the claim properly remains restricted to fixed layers 0–4; `digest` 216–220 fixes w2=w3=0. |
| First accepted counter and failed-row sampler | PROVED | Source 228–236 returns first acceptance. Conditional rejection prefixes, accepted target prefix and residual prefixes have the exact product law. The bottom branch is necessary and correctly retained. |
| Full 256-bit outputs | PROVED | Uniform independent 128-bit suffixes accompany every row, including rejected and canonical rows; repeated raw strings return the same entire image. Author's derivation includes this explicitly. Its finite control checks prefixes, while my separate control additionally checks full-image and suffix laws. |
| Prequeries and old useful points | PROVED for target event | Sample the joint function and metadata once, then answer prequeries consistently. Count at first evaluation even before original disclosure. No oracle overwrite or free prequery reset is permitted. |
| Earlier rejected rows versus residual rows | PROVED | Earlier same-child rows cannot match accepted Y. Fresh later or other-child rows have prefix match probability 2^-128. A repeated nonmatching point cannot newly cause Bad7. Bottom has no target. |
| Scalar address count | PROVED | Each raw input identifies one address and one designated target. Exposure of every target changes no residual row distribution. No total graph/key factor is needed for this **same-address event**. |
| Raw budget Q_H+5 | PROVED within stated interface | Final verification 715–721 reaches at most five digest evaluations. Adversarial child/counter choices are included. Early rejection and repeated/canonical points can only decrease fresh opportunities. Local adversarial verification must already be charged in Q_H. |
| Honest operations supply no residual type-7 answers for free | PROVED for honest caches and source-only signing | `grind` 228–236 evaluates rejected prefix and canonical target; top setup 539–540 does the same. `sign` 636–655 checks the honest canonical counter or grinds. An accepted corrupt cache counter can instead evaluate a later row: excluded, correctly stated by author. Public arbitrary digest API use must be charged. |
| Graph/target strong view projects only an event | PROVED / limitation retained | The augmentation yields an upper bound on Bad7. Full graph payload exposure can reveal secret chain/FORS inputs. It is not a secrecy game, EUF-CMA simulator, efficient reduction or quantum argument. Author states the event and efficiency restrictions; keep the secret-payload distinction explicit when composing. |
| Exact top number and readiness | COMPUTED / PROVED | Parameter driver line 9 selects top (h=21,lw=8,z=0,S=2040); `keygen` 517–523 has nsub=1, nleaf=2^21 and **2,097,152** distinct canonical address planes. `tau_top=[1-(1-p_top)^(2^32)]^(2^21)`. Repeated V values do not merge addresses. |
| Conditioning on cache completion | PROVED for mathematical row success only | Top-success depends exclusively on canonical metadata, leaving residual law unchanged. Arbitrary OS/time-limit/implementation success conditions require their own argument. This is correctly distinguished from total termination. |
| Exhaustion, OS failure and runtime | OPEN / correctly excluded | `grind` has no explicit no-counter API; checked u32 increment can panic and unchecked increment can repeat forever. Threads=0 fails before ordinary worker completion; allocation and scheduling are not covered. The probability is neither actual fixed-SHA empirical frequency nor a runtime guarantee. |

## Independent arithmetic and controls

Own `control.py`, run with `python -I -B`, exited 0. It enumerates **32,768** full-image toy tables and **84** strong views, checks exact success/bottom masses (1/2,1/4,1/8,1/8), full accepted-image uniformity, and residual match probability 1/4 in every permitted view.

A negative control grants two residual answers for free and permits one selected raw query: match probability becomes **7/16 > 1/4**. Therefore the restriction on free residual disclosure is essential. The author's different negative control also correctly rejects target selection that inspects residual outputs.

Independent inclusion-exclusion recomputation agrees with the author's two-method count:

    |A_top| = 454918678781617793203528879683071744,
    p_top = 1777026088990694504701284686261999 /
            1329227995784915872903807060280344576.

The exact rational floor yields `floor(2^32*p_top)-21 = 5741859`. Since `(1-p)^C <= 2^(-Cp)`, the stated conservative `1-tau_top <= 2^-5741859` is valid. The sharper decimal logarithms are estimates and correctly marked approximate. The symbolic tau expression is exact.

The possible number **246** is a different resource: lower verification performs 32*15−240=240 chain steps, one endpoint compression and five Merkle-node calls; adding its type-7 digest gives 247. This is not the canonical-plane count or the global Bad7 verification budget.

## Composition boundaries that must survive

1. The typed-game law presupposes the shared-oracle/secret-input bridge. Nonzero public seed, alias accounting, entropy/opaque-handle restrictions and partial-operation normalization are not discharged by this row lemma. Charge S=0 once in the combined argument, rather than duplicating it across local lemmas.
2. The first-accept conditional table is a statistical ghost construction, possibly exponentially large. Do not claim a polynomial-time challenge embedding from it.
3. Equality of all decoded digits equals equality of the 128-bit slice for widths 4 and 8. If child/counter differ, that is the proved Bad7 event. Unequal digits, hidden predecessors, changed endpoints, FORS reuse and accepted signatures at previously unqueried keys remain separate obligations.
4. Failed rows are explicitly represented. No all-key counter-existence premise is silently assumed; tau concerns only required top-cache rows.
5. The target lemma remains classical. No QROM or concrete-SHA security statement follows from its finite control.

## Identity checks

Current source hash matches `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`; parameter driver hash matches `a18799fba64ec1a6370e18e0d5d4b21108109cf9022fc8d7195e55d860a08c4b`. All five entries in the author's `SHA256SUMS.json` matched at review. The author's script was inspected but not rerun in its directory, preserving the write boundary. Own control receipts are in `CONTROL-RESULTS.json`.

No required mathematical correction. Recommended composition clarification: explicitly name the metadata-only cache-success condition and prohibit uncharged later/other-child outputs when using the event lemma inside a larger game. The existing author's text already substantially supplies both restrictions.

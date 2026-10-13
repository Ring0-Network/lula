# Current baseline source-bound calculator

**PROVED / COMPUTED â€” scope.** This separate calculator evaluates the current manually proved complete classical joint ledger and polynomial-private quantum envelope, retaining the two older complete quantum alternatives. It does not overwrite any historical bounds.py. All numerical exponents mean negative-log2 probability upper bounds, never guaranteed work bits, a category, an optimal attack threshold or a repair certificate. The original adequacy target remains **OPEN / not established**; see [the criterion audit](../adequacy-original-criterion/VERDICT.md).

Run in this directory with the installed Python/mpmath (no installation or source execution):

```powershell
python -I -B bounds.py
python -I -B bounds.py --params baseline.json --log2-QH 64 --log2-Qq 32 --out selected.json
python -I -B bounds.py --log2-QH 64 128 --log2-Qq 32 64 --out output-directory
```

**COMPUTED â€” interface.** Defaults cover all eight log2(q) values24,30,38,40,41,44,50,64 and both classical64/128 and quantum32/64 adversarial query exponents. --out accepts a JSON file or directory. --dps defaults600 and refuses values below500. Results record exact outward binary endpoint tuples, approximate displayed exponents, every classical ledger/quantum component, all three quantum complete bounds and their pointwise minimum. Source, driver, theorem, frozen helper, parameter and calculator SHA256 provenance is recorded. A changed source/helper/theorem pin is refused until manual review.

**COMPUTED â€” baseline geometry.** baseline.json fixes16-byte nodes;17 real FORS trees plus one forced zero coordinate; a9; five heights5,5,5,5,21; lw4,4,4,4,8; ell32,32,32,32,16; sums240,240,240,240,2040; BE32 counters; top-only cache. Signature size is5720 bytes and logical cache payload75497456 bytes. The measurement-driver fixture is payload+117=75497573 bytes and contains48 seed bytes: that file is distinct from the public logical cache experiment.

**COMPUTED / ASSUMED â€” analytic compression costs.** The optimized public-seed block is precomputed. Each typed call costs ceil((22+payload_bytes+9)/64) tail compressions. One WOTS leaf PK costs ell*w+that endpoint-compressor cost; a height-h subtree costs2^h times the leaf cost plus2^hâˆ’1 parent blocks. TOP cold rebuilding is therefore2^21*4102âˆ’1=8602517503 tail compressions. Its signing tail adds16+2040 private/chain steps, one final digest check and the top grinding trials. Top-only keygen also computes each top leafâ€™s uncached immediate child subtree: its fixed tail cost is2^21*20805âˆ’1=43631247359, plus canonical-row trials. The script derives these integers from its parameters rather than running a forest. Add one compression per Ctx construction for the seed-block precomputation; source CALLS omits that precomputation.

**ASSUMED / COMPUTED â€” counter expectations.** Acceptance cardinalities are exact integer coefficients checked by DP and inclusionâ€“exclusion, divided by2^128 including omitted-digit-zero conditions. Under the explicitly stated fresh-uniform type7 row model, the script reports finite2^32-attempt bottom mass, expected charged trials through success/bottom, and conditional-on-success means. Full top-setup conditional means are labelled as such; no successful-run normalization is applied to complete security bounds. These are counts/expectations, not timing data.

**COMPUTED â€” numerical verification.** The exact finite-binomial FORS moment is computed by the frozen helper at600 and700 decimal digits, checked for relative stability, and independently enclosed by600-digit outward interval arithmetic. A positive binomial recurrence with a rigorous analytic omitted-tail bound, or a Chernoff saturation interval, must overlap. Positive-tail enclosure precision is reported honestly; it is not automatically700 digits. Poisson is not substituted in the complete bounds.

**OPEN â€” retuning boundary.** --params can request analytic geometry with n16, lower-layer lw4 and final top-layer lw8. Total height is at most63, because source tree_leaf cannot shift by64. The chosen diagnostic domain uses individual heights1..31; zero-height layers can be representable in source, so this narrower domain is not an exhaustive parameter search or a minimality claim. If ANY baseline parameter differs, complete bounds are refused: output has diagnostic moments/bytes/cache/costs and empty classical/quantum result lists, and the program returns2. Source geometry checks include digest/index/buffer/shift bounds. The strict S<Smax condition is reported separately; geometry or that condition alone never certifies a retuned forgery skeleton. Even an allowed(a,k,d,h,ell,S) change requires a uniform source proof before complete-bound evaluation. No verifier/source parameter is changed.

**COMPUTED â€” default complete-bound exponents.** Values below are approximate probability-bound exponents;0 means the envelope caps1.

| log2(q) | Classical QH=2^64 | Classical QH=2^128 | Best quantum Qq=2^32 | Best quantum Qq=2^64 |
|---:|---:|---:|---:|---:|
| 24 | 62.415037499 | 0.000000000 | 58.109705808 | 0.000000000 |
| 30 | 62.415037499 | 0.000000000 | 58.109704065 | 0.000000000 |
| 38 | 62.415025251 | 0.000000000 | 58.109342075 | 0.000000000 |
| 40 | 62.394840598 | 0.000000000 | 58.093178880 | 0.000000000 |
| 41 | 61.136144503 | 0.000000000 | 57.238884503 | 0.000000000 |
| 44 | 34.521203045 | 0.000000000 | 31.521128447 | 0.000000000 |
| 50 | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 |
| 64 | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 |

**PROVED â€” preservation.** Honest/private/message/circuit/storage costs are not erased by the raw-query axis. No source signatures, timing measurements, forest generation, attack, global install, manuscript edit or historical scalar/calculator edit occurs. New source/game/kernel declarations0; whole original adequacy/category/repair goal remains incomplete.

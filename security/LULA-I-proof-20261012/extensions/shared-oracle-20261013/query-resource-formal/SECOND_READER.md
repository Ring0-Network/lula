# Second reader: exact outward query-resource threshold calculation

**ACCEPTED — arithmetic implementation and threshold semantics within the reviewed theorem/input scope.** My independent monotonicity and integer-gate derivation was saved first in `INDEPENDENT_DERIVATION.md` (SHA256 563b24e74fce13bb58e597a1262db15552eecb4949410ebe8a6ea716749c181c). I subsequently read the other agent's complete `thresholds.py` and derivation and inspected all 32 saved endpoint records. I did not execute that agent's script, inspect a root threshold candidate to construct my derivation, or overwrite its artifacts. The saved endpoint/margin inspection is recorded in `SECOND_READER_CHECK.json`.

## Reviewed immutable identities

| Artifact in query-resource-independent | SHA256 |
|---|---|
| thresholds.py | 713cd9030c212e88948be1116ff6f8b1edae99f62b330ea446dbf56edc8b7da6 |
| INDEPENDENT_DERIVATION.md | e0ecff4325d7b35171bb822b8b99dc865bffe7536eed41b2b778da8563d3ae2a |
| THRESHOLDS.json | 2933457f2045d24a6633eefd356ac33902f0961462b765dffa03b73dae317da7 |

The four stored input hashes match the current three reviewed theorem files and `classical-composition-numeric/OWN-BOUNDS.json`. The table below reviews this exact artifact cut; future changes require renewed inspection.

## 1. Formula correspondence

I compared every term in `formulas` with the three reviewed theorem expressions. N=2^128, M=N^2-N, the initiated signing cap, classical coefficient 6Q+3q+6243, binomial q(q-1)/2, all source alias terms, quantum AR component D, nested A/c caps, h/g/d7 offsets, delta, single seed-zero contribution and event-specific shared projector match. The classical exhaustion probability is enclosed, rather than dropped.

The quantum `best` expression is the pointwise minimum of the conservative and event-specific valid full-source envelopes. It does not substitute a purported global ordering between them. In particular, the event-specific envelope can be numerically larger near this constant-success target even when it improves much smaller winning bounds. Using the minimum remains valid and nondecreasing; its endpoint enclosure takes the minimum of both lower bounds and the minimum of both upper bounds. This is the correct interval for the minimum, including when the tighter envelope changes across a boundary.

## 2. Exact interval arithmetic

The dyadic input decoder maps a nonnegative mantissa/exponent tuple to its exact rational value, without decimal rounding. Its sign and mantissa bit-length assertions reject an inconsistent representation. Repeated occupancy rows for a signing cap must agree exactly. This faithfully reuses the earlier independently accepted p_F enclosure; it does not newly prove the occupancy formula or its numerical tail enclosure.

All `I` intervals are constrained to 0<=lo<=hi. Addition and multiplication of such intervals propagate endpoints monotonically. Division is restricted to a strictly positive integer, as required by every denominator here. Squaring is sound specifically because all interval values are nonnegative. Capping at one is monotone and its endpointwise application is sound.

For sqrt(x), put S=2^1024 and t=isqrt(floor(x*S^2)). Integer square-root arithmetic gives t^2<=floor(x*S^2)<(t+1)^2, equivalently t^2/S^2<=x<(t+1)^2/S^2. The implementation also asserts this exact rational inequality. Applying this at the two interval endpoints supplies an outward enclosure; if the upper endpoint equals b^2/S^2 it retains b/S exactly, otherwise it uses (b+1)/S. There is no inward floating-point rounding in these gates.

The exhaustion enclosure is valid: (511/512)^(2^32)<exp(-2^23)<2^(-2^23)<2^-4096. Consequently [0,q/2^4096] safely encloses the unchanged classical term. At the tested q<=2^64 this remains negligible, but its inclusion means the boundary certificate is for the original mathematical expression rather than one with a term removed.

The approximate logarithm and elapsed wall-clock field are metadata only. Neither participates in an interval comparison, formula evaluation, endpoint selection or security claim.

## 3. Integer gate and saved records

`certify` reports PASS only when the interval upper endpoint is <=1/2 and FAIL only when the lower endpoint is >1/2. A straddling enclosure raises an exception. Exponential bracketing and integer bisection maintain one passed and one failed endpoint, then terminate only at adjacent integers. Monotonicity proved independently in my first derivation licenses the conclusion for every smaller/larger query cap. Inclusivity at equality is correct.

I independently decoded every saved rational interval and checked all 32 unique (q,model) endpoint pairs. Each Q_fail=Q_pass+1. All 64 endpoint intervals are well ordered and in [0,1], all saved passing upper endpoints are <=1/2, and all saved failing lower endpoints are >1/2. Each saved pass margin equals 1/2 minus its interval upper endpoint, and each saved fail margin equals its interval lower endpoint minus 1/2. Artifact/input pins match. These checks inspect recorded certificates; they are not a rerun of the author's implementation or an independent evaluation of its entire scalar formulas. My code review above supplies the latter implementation assessment.

The current script assumes and asserts a passed Q=0 for its eight designated q. It does not implement a general `NO_CERTIFIED_NONNEGATIVE_QUERY_BUDGET` output for arbitrary inputs. This is not a defect for the explicitly finite delivered table because all designated rows have certified positive endpoints. It would need that branch before reuse as a general-purpose threshold interface. The mathematical convention in my first derivation handles the empty case explicitly.

At q=2^40, the saved classical adjacent pair is 28158377811508036555700208997110311281 / 28158377811508036555700208997110311282; the quantum minimum pair is 1538654937033492218 / 1538654937033492219. At q=2^64 the respective pairs are 254/255 and 3/4. These integers are checks of sufficient-envelope crossings, not attack results.

## 4. Security meaning and remaining scope

The author correctly states that a passed cap proves winning probability at most 1/2 for every adversary within that raw-query cap in the reviewed source model. It excludes winning probability strictly greater than 1/2, while allowing equality. The next sufficient bound being above 1/2 does not establish any adversary attaining that probability. Monotonicity of an upper bound cannot be inverted into a success lower bound.

No attack, runtime, optimal security level, NIST category, actual SHA guarantee, implementation/refinement certificate, public-cache guarantee or corrupt-cache guarantee is claimed. The original tiny-failure gates remain separate and do not become satisfied by this new constant-success resource table. The prior p_F enclosure and reviewed source-model theorems remain trusted mathematical inputs to this calculation; this review does not mechanize them.

**Outcome: ACCEPTED_EXACT_OUTWARD_THRESHOLDS_WITHIN_REVIEWED_MODEL.** No blocking defect found. The only generalization gate is the unimplemented empty-budget branch for arbitrary inputs, which is outside the fixed eight-q artifact scope. Full security/category certification remains not established.

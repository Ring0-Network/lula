# Canonical-target results

**MANUALLY_PROVED_SCOPED:** the exact conditional first-accepted row sampler preserves the original classical random-oracle table distribution. At a fresh noncanonical query, matching that address's exposed accepted 128-bit target has conditional probability zero for earlier same-child counters and exactly `2^-128` for later/other-child points. All targets can be exposed first. Prequeries and repeated points are covered by counting first raw evaluations, including before original disclosure.

Hence `Pr(Bad_7) <= min(1,Q_H/2^128)` for the raw-query target event; one final verification reaches at most five type-7 points, giving a safe `(Q_H+5)/2^128` event bound when they are not already included. There is no multiplier for the number of exposed addresses. This requires graph/seed/parameters fixed independently of the type-7 restriction, literal input injectivity, honest consistent caches, and no uncharged residual type-7 information from the signing interface. Composition retains the standing shared-oracle alias losses.

**COMPUTED_EXACT:** top WOTS+C acceptance count, by independent inclusion-exclusion and integer dynamic programming:

```
454918678781617793203528879683071744
```

Dividing by `256^16` gives approximately `0.00133688584247832636618495809082518860539375888154`. For `2^21` independent top-cache rows and `C=2^32` distinct counters,

```
tau_top = [1-(1-p_top)^C]^(2^21),
1-tau_top <= 2^21(1-p_top)^C <= 2^-5741859.
```

The last bound is a deliberately coarse rigorous bound obtained from `(1-p)^C <= 2^(-Cp)` and an exact rational floor of Cp. The decimal log2 of the sharper union bound is approximately `-8289304.379876739`; it is labelled approximate in `CHECKS.json`. The source does not implement a general counter-exhaustion abort, and these statements are neither actual fixed-SHA probabilities nor runtime bounds.

**SMALL_EXACT_CONTROLS_PASS:** 256 finite toy tables reproduce the sampler marginal exactly; 24 conditional point checks distinguish rejected/canonical/uniform points. With both toy targets exposed, adaptive row selection still yields the fresh residual target hit `1/4`. A wrong rule choosing the target after inspecting a residual point yields hit `1/2` and conditional hit 1 for one exposed target, refuting an unconditional target-independence shortcut. These are model controls, not executable full-signature attacks.

**OPEN:** formal source refinement, efficient target/challenge embedding, extraction for unequal WOTS digits and chain/compression witnesses, complete EUF-CMA composition and QROM full-signature security. No Lean run was needed for this finite-disintegration derivation. No implementation, paper, earlier proof packet or timing record was changed.

Outcome: **MANUAL_TYPE7_EVENT_AND_TOP_COMPLETION_DERIVED**.

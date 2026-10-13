# Full-term status table

Every FORS number is a fixed-instance model computation. OPEN cells are not zero and are not assigned bits.

| Term / status | q=2^38 | q=2^40 | q=2^41 |
|---|---|---|---|
| Secret-derivation PRF advantage | OPEN | OPEN | OPEN |
| Message-randomizer/shared-SHA advantage | OPEN | OPEN | OPEN |
| Adaptive FORS forgery bound | OPEN | OPEN | OPEN |
| Full WOTS certification bound (all five layers) | OPEN | OPEN | OPEN |
| Merkle/FORS-root extraction bound | OPEN | OPEN | OPEN |
| H_msg and free-counter contribution | OPEN | OPEN | OPEN |
| Full EUF-CMA total | OPEN | OPEN | OPEN |
| FORS raw-candidate model exponent | COMPUTED 143.262538581 | COMPUTED 132.563419944 | COMPUTED 125.902530385 |
| Honest different-child WOTS reuse subevent | PROVED 0 | PROVED 0 | PROVED 0 |
| Honest-cache probability transfer loss | PROVED 0, conditional | PROVED 0, conditional | PROVED 0, conditional |

PROVED 0 for one subevent does not close the full WOTS term. Zero transfer loss does not establish the reference bound.
The smallest full signing-limit crossing and full quantum q_max are not established.

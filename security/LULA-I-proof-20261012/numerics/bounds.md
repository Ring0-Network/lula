# Component results

All FORS entries are fixed-instance model computations. Total EUF-CMA is OPEN.

| signatures q | FORS binomial bits per try | FORS Poisson bits per try | conditional advantage exponent for Q_H=2^128 | total EUF bits |
|---|---:|---:|---:|---|
| 2^24 | 178.421820108 | 178.421820079 | 50.421820108 | OPEN |
| 2^30 | 167.771253729 | 167.771253728 | 39.771253729 | OPEN |
| 2^38 | 143.262538581 | 143.262538581 | 15.262538581 | OPEN |
| 2^40 | 132.563419944 | 132.563419944 | 4.563419944 | OPEN |
| 2^41 | 125.902530385 | 125.902530385 | 0.000000000 | OPEN |
| 2^44 | 98.521203051 | 98.521203051 | 0.000000000 | OPEN |
| 2^50 | 20.122193182 | 20.122193182 | 0.000000000 | OPEN |
| 2^64 | 9.000000000 | 9.000000000 | 0.000000000 | OPEN |

The Q_H column is budget arithmetic under an unproved per-query upper-bound premise, not a complete forgery bound.

Exact DP and inclusion-exclusion checks passed. Toy formula checks fall within the reported 99.9% Wilson intervals.
Hypothetical WOTS reuse statistics do not apply to the honest reference signer: each complete WOTS address signs one fixed child value.
One signature still admits one inclusive encoding (probability 2^-128 per raw encoding hash); fresh input collisions are not excluded by an antichain.

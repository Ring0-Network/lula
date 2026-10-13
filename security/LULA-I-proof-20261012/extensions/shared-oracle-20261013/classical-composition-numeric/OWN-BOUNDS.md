# Independent conservative classical RO evaluation

min(1,(6Q_H+3q+6243)/2^128 + (qQ_H+q(q-1)/2+q)/2^256 + q(511/512)^(2^32) + (Q_H+1)p_F(q))

Negative base-2 logarithm of a capped advantage upper bound, NOT a work factor or a per-candidate component exponent.

| q | Q_H | FORS per-candidate exponent | Total capped-bound exponent |
|---:|---:|---:|---:|
| 2^24 | 2^64 | 178.421820107685 | 61.415037499278 |
| 2^24 | 2^128 | 178.421820107685 | 0.000000000000 |
| 2^30 | 2^64 | 167.771253729325 | 61.415037499237 |
| 2^30 | 2^128 | 167.771253729325 | 0.000000000000 |
| 2^38 | 2^64 | 143.262538581063 | 61.415031371502 |
| 2^38 | 2^128 | 143.262538581063 | 0.000000000000 |
| 2^40 | 2^64 | 132.563419944118 | 61.404903691648 |
| 2^40 | 2^128 | 132.563419944118 | 0.000000000000 |
| 2^41 | 2^64 | 125.902530384766 | 60.638290368512 |
| 2^41 | 2^128 | 125.902530384766 | 0.000000000000 |
| 2^44 | 2^64 | 98.521203050680 | 34.521203039111 |
| 2^44 | 2^128 | 98.521203050680 | 0.000000000000 |
| 2^50 | 2^64 | 20.122193181815 | 0.000000000000 |
| 2^50 | 2^128 | 20.122193181815 | 0.000000000000 |
| 2^64 | 2^64 | 9.000000000000 | 0.000000000000 |
| 2^64 | 2^128 | 9.000000000000 | 0.000000000000 |

Every interval uses 230-digit outward arithmetic. A second positive occupancy calculation with tail control overlaps the finite-moment interval. Exact rational arithmetic recombines the additive constants. The full dyadic endpoints and each term are in OWN-BOUNDS.json. No root output was read to generate these values.

Status: COMPUTED_ACCEPTED_MANUAL_CLASSICAL_RO_BOUND; WORK_FACTOR_AND_QROM_CATEGORY_NOT_ESTABLISHED.

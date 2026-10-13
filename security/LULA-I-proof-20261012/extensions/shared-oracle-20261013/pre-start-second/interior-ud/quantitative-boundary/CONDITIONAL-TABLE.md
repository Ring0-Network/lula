# Hypothetical capped UD envelope

**COMPUTED — arithmetic only.** Assume, solely for this diagnostic, each constructed UD adversary satisfies delta<=min(1,12 Q_B/2^64). Applicability to fixed h or its full same-h interface is unproved. PRE is optimistically set to zero only to test whether the UD term already saturates. Values are probabilities/envelopes, never security bits.

Q_B=Q_A+H_setup+q H_mode+3224+254. Every table row's 2^55*254 amplified UD envelope caps at 1, already with PRE=0.

## Q_A=2^32

| q | Q_B hot | per-hop hypothetical cap hot | Q_B absent cache | per-hop hypothetical cap absent cache | aggregate cap, PRE=0 |
|---|---:|---:|---:|---:|---:|
| 2^24 | 369296591885962645 | 0.24023530 | 584976792773725589 | 0.38053987 | 1 |
| 2^30 | 23067525480057933205 | 1 | 36871058336874761621 | 1 | 1 |
| 2^38 | 5902989675558892211605 | 1 | 9436694086904000286101 | 1 | 1 |
| 2^40 | 23611931680502204861845 | 1 | 37746749325882637159829 | 1 | 1 |
| 2^41 | 47223854353759955062165 | 1 | 75493489644520819658133 | 1 | 1 |
| 2^44 | 377790771779368457866645 | 1 | 603947854105455374634389 | 1 | 1 |
| 2^50 | 24178608826423180659789205 | 1 | 38652662095292743332924821 | 1 | 1 |
| 2^64 | 396142326864551706029266570645 | 1 | 633285215621710620865920503189 | 1 | 1 |

## Q_A=2^64

| q | Q_B hot | per-hop hypothetical cap hot | Q_B absent cache | per-hop hypothetical cap absent cache | aggregate cap, PRE=0 |
|---|---:|---:|---:|---:|---:|
| 2^24 | 18816040661300546965 | 1 | 19031720862188309909 | 1 | 1 |
| 2^30 | 41514269549472517525 | 1 | 55317802406289345941 | 1 | 1 |
| 2^38 | 5921436419628306795925 | 1 | 9455140830973414870421 | 1 | 1 |
| 2^40 | 23630378424571619446165 | 1 | 37765196069952051744149 | 1 | 1 |
| 2^41 | 47242301097829369646485 | 1 | 75511936388590234242453 | 1 | 1 |
| 2^44 | 377809218523437872450965 | 1 | 603966300849524789218709 | 1 | 1 |
| 2^50 | 24178627273167250074373525 | 1 | 38652680542036812747509141 | 1 | 1 |
| 2^64 | 396142326882998450098681154965 | 1 | 633285215640157364935335087509 | 1 | 1 |

**PROVED — analytic saturation of this hypothetical expression.** Before the per-hop cap, the aggregate coefficient is exactly 381/64 times Q_B. Its outer cap therefore reaches 1 for any integer Q_B>=1; the nontrivial threshold is Q_B<64/381. This says the proposed sufficient envelope is uninformative. It is neither an attack nor a conclusion about actual fixed-h hardness.

Exact fractions, unclipped values and threshold computations are retained in CONDITIONAL-ENVELOPE.json.

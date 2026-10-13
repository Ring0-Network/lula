# Quantum graph-event second-reader report

**Outcome: ACCEPTED_INFORMATION_THEORETIC_GRAPH_EVENT_BOUND.** The one-Boolean-query simulation is valid, the finite-register full-image factorization is exact under the stated graph/outside-function sampling premise, and the final classical-verifier extraction supports the displayed average-search bound. No blocking counterexample was found in this scoped argument. This is not complete QROM security, an efficient reduction or a NIST category certificate.

## Independence and identities

`INDEPENDENT_DERIVATION.md` was saved before reading the quantum authoring lane. It independently derived the Boolean factorization, clean pivot-and-swap simulation, final witness requirement, and 3217 verifier-call budget. Only then were the author `DERIVATION.md`, `CHECKS.json` and `control.py` read.

Reviewed author identities:

- `quantum-graph-targets/DERIVATION.md`: `1a050363698b8d8913c6032773af943ac4860efb167ec9d12d8efc45f4811af9`.
- `quantum-graph-targets/control.py`: `d767056627f484608aa5663a45fe873156ca0089059689752aebc170f4502d6e`.
- Pinned release `code/lula1/src/lib.rs`: `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.
- Primary ePrint 2022/346 cached PDF: `80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3`.

The [official primary paper](https://eprint.iacr.org/2022/346) was accessed online. Its PDF endpoint returned 403, so the existing primary cached PDF was inspected directly with pypdf at physical page 23. Definition 9/Theorem 4 give the Boolean average-search bound `8 lambda (Q_B+1)^2`. No SPHINCS+ full security theorem was applied to custom code.

## Case-by-case review

| Obligation | Finding |
|---|---|
| One target per type0–4 address | The event uses the designated raw graph input/output and compares only alternatives at that same actual encoded address. Exact own-domain-blind graph sampling is an inherited premise. Giving all graph secrets may enable ordinary signing, but does not turn canonical graph calls into marked alternative inputs. |
| Full256 oracle interface | Accepted. At each residual point, independent Boolean mark density `2^-128`, a marked value with fixed target prefix/uniform tail, and an unmarked value with uniform non-target prefix/uniform tail mix to uniform256. Responses retain all bits. Prefix-only replacement would not be the same quantum interface. |
| Graph and outside advice | Accepted under the explicitly stated eager graph sampling premise. Actual outside **function tables**, graph points and independent pair tables are granted; arbitrary outside query logs may encode residual values and cannot be fixed as independent advice. This restriction is correctly present. |
| Finite quantum register | Accepted. An explicit length-and-content encoding avoids variable-length padding alias. Bernoulli marks are sampled independently over every register word; eligibility masks ignore irrelevant marks rather than force them to zero. The argument is uniform in any fixed finite register size, not an undefined infinite oracle construction. |
| Pre-key queries | Accepted. The coherent table is fixed at time zero. Conditioning on fixed nonzero S and giving G early increases information while preserving oracle chronology. No oracle is reprogrammed after a prior superposition query. Seed/parameter selection after oracle inspection would be a different model. |
| Single-query simulation | Accepted independently. An involutory pivot fanout T maps delta to a basis pivot. Conjugating a pivot flip by T gives XOR by delta. Swapping a `|+>` work qubit with the selected response pivot lets one ordinary Boolean XOR query flip that pivot; swapping back restores the work qubit to `|+>` with no garbage. On irrelevant branches, querying `|+>` is the identity. No measurement or free controlled oracle is used. |
| Two-query fallback | Accepted. Compute mark, controlled full-value XOR, uncompute mark is valid and costs two Boolean queries. A one-query version that leaves the mark in a discarded `|0>`-initialized ancilla would be invalid: it can decohere input branches. |
| Honest work | Accepted only in the declared ideal interface. Honest graph queries are canonical and supplied by G; other honest functions are independent outside restrictions on nonzero S. Arbitrary cache corruption, additional APIs, signing in superposition, free residual answers or an unproved private-function replacement are not silently admitted. |
| Observable event/extraction | Accepted. The adversary produces classical bytes; the reduction runs a classical final verifier and records actual calls. If an alternative same-address target hit appears, its raw input is an output Boolean-search witness. No inference is made from a point having occurred in a query superposition. The event can occur in an ultimately rejected trace, which only makes the event larger. |
| Exact final budget | Accepted. 171 FORS calls, 984 lower-layer WOTS/PK/tree calls, and 2062 top-layer calls give 3217. Fixed accepted digit sums control remaining chain lengths. Five type7 calls and two message calls are outside this event restriction and consume no mark queries here. This is a complete-hash call count, not compression-count or latency evidence. |
| Unconditional seed branch | Accepted. A uniform seed gives a `2^-128` zero-S charge. Sharing it across other hops requires one shared stopped-coupling argument. It cannot be deleted from separate unconditional bounds by bookkeeping alone. |

## Independent algebra for the one-query claim

Write `delta=V0 XOR V1`. For a nonzero pivot bit j, the reversible map

```
T(z) = z XOR [z_j (delta XOR e_j)]
```

is its own inverse and sends delta to e_j. Therefore `T X_j^b T` is translation by `b delta`. This remains correct when j and delta depend coherently on x. The bitwise circuit is a permutation and introduces no relative phase.

For irrelevant words, the Boolean query flips a work qubit in `|+>` and leaves it unchanged. For eligible words, the controlled swap makes the query act on the original response pivot while the response's temporary pivot is `|+>`. The second swap restores the independent work state. Thus the response action is exactly XOR by the full sampled value and the work state is independent of x and the mark. Linearity extends the pointwise identities to superpositions across the eligibility mask.

This argument uses free precompiled pair-table lookups that are independent of the Boolean oracle. Those circuits can be exponentially large. The theorem is query-complexity/information-theoretic; no efficient table simulator or challenge embedding follows.

## Retained quantitative statement

For Q adversarial coherent full-function queries, including pre-key queries, and one final classical verification,

```
Q_B <= Q+3217,
Pr(E_graph | fixed nonzero S)
 <= min(1,8 (Q+3218)^2 / 2^128).
```

The primary theorem supplies 8 and the final +1; the source inventory supplies 3217. A safe two-query fallback is

```
min(1,8 [2(Q+3217)+1]^2 / 2^128).
```

With independently uniform S and no successful-setup renormalization, add `2^-128` before capping at 1. The event is an actual final-trace alternative-input target collision for types0–4. There is no missing factor for the number of addresses because each raw input binds to one same-address target, and the Boolean search problem already averages over all eligible inputs.

## Executed control and residual scope

Copied the reviewed author control unchanged to `reviewed_control.py` in this reviewer directory and ran `python -I -B reviewed_control.py`. Exit code 0; all outputs were confined here. The exact control checks 73,728 basis-plus-ancilla vectors / 147,456 raw terms over 144 value-pair worlds and all16 mark tables. It also verifies uniform weights over all64 pairs of residual images. Its source and both primary PDF hashes passed. `CHECKS.json` records this run. This is a finite circuit check in addition to the manual general algebra, not formal verification of the entire source graph sampler.

Efficient simulation, proof-assistant source refinement, full signature witness classification and extraction, hidden-secret inversion, adaptive FORS coverage, type7 target binding in a quantum model, quantum privatization and composed QROM security remain separate obligations. The event bound becomes vacuous at sufficiently large query budgets and is not a category1 assertion. No paper, implementation, author lane, earlier packet, or global configuration was edited or uploaded.

# Quantum FORS/source-selection handoff

**Outcome: FIRST_CALL_SOURCE_BRIDGE_CANDIDATE; PRIMARY_CONSTANT_VERIFIED; EXACT_CONTROLS_PASS; FULL_QUANTUM_FORS_OPEN.**

Source-first work was saved in `INDEPENDENT_DERIVATION.md` before reading the primary AR theorem or any future peer quantum-FORS report. The later `DERIVATION.md` gives a tighter primary-backed first-call comparison and labels its independent-review gate explicitly.

## Concrete progress

**CITED primary constant.** In Grilo-Hövelmanns-Hülsing-Majenz, arXiv2010.15103v2, Theorem1 Eq(2) has one-instruction event-distance loss `sqrt(Q*pmax)+(Q*pmax)/2`. Figure2 programs a fresh uniform full image and returns the selected point/side information. Theorem6 allows arbitrary post-instruction queries. The downloaded author PDF was checked directly, including printed pages6-7; SHA-256 is `9a5ea6adeba5dcdf6c80035057aaccdc704aa6ea2940af0320bcfd7eca0abc8d`.

**PROVED candidate source mapping.** For the first classical signing message, fresh private R gives the inner point exact pmax=2^-128, while original O(I) remains potentially correlated with prequery memory. A primary one-point hop makes U a fresh uniform256 value and keeps subsequent verification consistent. A second primary hop resamples the whole outer counter row at U. After charging the lower-half alias guard2^-128, U has uniform eligible namespace size `2^256-2^128`, so this row hop uses that exact density.

**PROVED coherent row construction.** Full row-valued XOR output is finite. Swapping the original full256 output into coherently selected slot c, with all other slots in |+>, querying once, and swapping back gives exact selected-word action and clean ancillary state. This avoids a 2^32 query-count multiplier. It instead requires 2^40 ancillary qubits for the real counter space: no efficient/PPT simulation is claimed.

**Candidate first-call loss for fixed nonzero S:**

    sqrt(Q/2^128)+Q/(2*2^128)
      +sqrt(Q/(2^256-2^128))+Q/(2*(2^256-2^128))
      +2^-128,

capped at1. Uniform S adds one further2^-128. At Q=2^64 the candidate is approximately `2.3283064368097468323100938533666124478539191860017e-10`, dominated by the inner AR term. This is a source-programming comparison distance for one first call, not a QROM forgery probability.

## Executed checks

`python -I -B control.py` returned exit0 and wrote `CHECKS.json`:

- 16,384 worlds show a prequery correlation discriminator: the original image matches stored response with probability1/4, while an independent reprogrammed image gives1/16. The exact difference3/16 refutes treating an unknown nonce as an unqueried quantum point; it is below the primary toy bound5/8.
- 128 adaptive classical-label cases preserve the unused private nonce's exact uniform law.
- 8,192 basis/function cases verify the one-query row lookup, including 4,096 outside/dummy cases and exact cleanup. Linearity covers superposed counters/namespaces and external entanglement.
- A zero-ancilla wrong variant leaves unused-row garbage and has trace-distance1/2 after disposal, demonstrating why the|+> construction is needed.
- Full-namespace mass is eligible mass divided by the namespace size, without a counter-space multiplier. The alias guard's conditional density uses the smaller eligible space exactly.
- Fresh first-zero rows have uniform latent accepted coordinates and an explicit finite failure branch. Later route-dependent completion can completely bias the emitted subset.
- A generic marked-oracle Grover control beats a classical Q+1 candidate union. It is not an actual FORS or LULA attack; it discriminates the invalid query-padding shortcut only.

## Remaining scope

**OPEN:** independent review of the first-call reduction and row-valued lookup application; a common sequential q-call source game preserving previous programmed points/rows, U collisions and repeated-message memoization; a quantum adaptive coverage/search reduction with observable extraction; and full QROM composition. The first-call theorem cannot be multiplied/used as fresh evidence for repeated m. No classical Q_H+1 candidate stream, a Q->Q^2 substitution, category certificate, or full quantum total is supplied.

The standing full quantum FORS field remains null. This lane adds no benchmark, actual signing, cache preparation, source change, manuscript edit, frozen-packet modification or private upload.

# Quantum-private hop: results and handoff

Outcome: **MANUAL_FINITE_QUANTUM_PRIVATE_DISTANCE_LEMMA_DERIVED; FULL_QROM_OPEN**.

**MANUALLY_PROVED:** with independently uniform128-bit private K/P and public S, Q coherent full256 public-RO calls, q initiated classical atomic signing requests, one final classical verification, and the expressly bounded finite input register,

    Delta_joint_quantum <= min(1, 2Q/2^64 + (2q+3)/2^128).

For fixed S!=0 the +3 is +2; the single extra1 is the uniform zero-seed branch. This is an upper bound on REAL/JOINT-IDEAL event-probability distance. It is not a whole-signature forgery bound or a claimed optimal constant.

The full-output coupling programs the two disjoint private families at time zero and preserves the genuine ordinary-RO REAL marginal. Queries before public-key disclosure see that same pre-existing function. In the continued IDEAL, K/P are unused and hidden-family query mass averages at most1/N. A coherent query costs at most2/sqrt(N) in trace distance. Each classical signing transition adds at most two literal P nominations, independent of its counter-loop length; its CQ discrepancy costs at most2/N. Final verification adds at most two more. Adaptive classical scheduling is handled by convexity over history blocks and the pathwise query/call caps.

**COMPUTED:** `python -I -B quantum_control.py` exited0. In a finite two-bit-output model with an ancilla, it checked256 key pairs over65 raw points. The averaged changed-support mass equals eligible query mass divided by16, and the mean one-query pure-state trace distance was0.3108607295023955, below the conservative0.5 bound. These numerical inequalities are finite controls, not formal verification of the theorem.

**COMPUTED negative controls:** one Grover step on an unknown marked key gives success and subsequent REAL key weight121/256, exceeding the naive one-query-plus-final literal budget1/8. A known-key query has hidden support mass1, refuting the1/N premise if key blindness is lost. The generic marked-oracle control is not a LULA attack and does not have the full uniform-RO marginal required by the source lemma; it discriminates the invalid reasoning shortcut only.

**CITED context:** the primary [BBBV paper](https://arxiv.org/pdf/quant-ph/9701001) supplies the query-magnitude hybrid precedent. The local constants and source-service accounting are independently derived; `PRIMARY-COMPARISON.md` distinguishes this from importing an uninstantiated O2H theorem.

**ASSUMED boundaries:** finite raw-register encoding; honest uniform seed entropy supplied externally; complete hash rather than compression access; classical signing requests; honest opaque caches/snapshot handles; no partial buffers, timing or private transcripts; initiated-call cap across branches; absorbing noncompletion. A coherent signing oracle or secret-bearing fixture interface needs a new analysis.

**OPEN:** second-reader validation of the full channel proof, machine-checked source semantics, efficient simulation, tighter specialized O2H loss, and quantum versions/composition of FORS coverage, hidden-value acquisition, graph targets and canonical digest targets. No full QROM or128-bit complete-signer claim is made.

No source, manuscript, root report or frozen proof packet was changed. The derivation was saved before new quantum-private peer work and before primary-source comparison.

# Refined finite-QROM source winning bound

**PROVED — manual source-model refinement, independently reviewed.** Preserve the conservative QUANTUM-RO-THEOREM.md and the original two-projector draft081545e… unchanged. Source-first derivations in quantum-private-rare-event, quantum-private-rare-second-reader and quantum-private-rare-numeric agree on the stopped-controller mechanism. The two independent reviewer reports accept the source gate and explicitly justify the shared terminal projector below. This result refines a winning event rather than asserting a smaller general state distance. Its arithmetic has a separately saved independent16-row dataset.

## 1. Fixed experiment and faithful stops

**ASSUMED — identical interface.** Fix nonzero S, N=2^128 and the reviewed full256 REAL/F/J/O0 coupling. Keep classical atomic source services and final verifier, finite coherent raw-query registers, q initiated calls over all branches and Q adversarial complete-output queries. Honest opaque consistent caches, absorbing noncompletion and no private-byte/timing/coherent-signing disclosure are unchanged. The ordinary unflagged HJ game remains the reference for its winning bound.

**PROVED — common stopped source channels.** Both proof controllers detect an honest/final public I/E private-family alias immediately before its hash reply and record an absorbing classical B. Before B, public source hashes use identical O0 images and private derivations use identical F/J. Addressed source hashes cannot alias on nonzero S. The entire nonalias source computation and completion are thus common channels. No coherent adversarial query is detected, measured or stopped. This is not a new production abort interface.

## 2. Unnormalized active-prefix argument

**PROVED — physical CQ domination.** Represent the continued IDEAL prefix by dephased classical sampled-environment and complete measured-history blocks, each containing the retained coherent query/work state. In a fixed block, its active stopped IDEAL prefix is the same unnormalized block or zero according to the no-earlier-alias indicator. This holds inductively up to the first alias, including numbered query-slot packing and early absorption. Consequently the active physical CQ state is dominated by the continued state. It is not normalized after selecting surviving keys.

**PROVED — query mass and purification.** The continued IDEAL leaves K/P unused. Every raw basis word nominates at most one private-family key, so averaged support mass is at most1/N. Deleting classical active blocks cannot increase that mass. The support expectation has the same value in a common purification with orthogonal copies of those records. A full-output XOR discrepancy has squared vector norm at most four times support mass. Pack common stopped services between Q charged query slots, using identity/plus padding on inactive histories. Telescoping gives purified vector gap a=2Q/sqrt(N). No assertion P*rho*P<=rho for arbitrary coherent pure states is used.

## 3. A single terminal event

**PROVED — source-event containment.** Let W be final fresh acceptance without B. They are disjoint records in the stopped experiment. Every winner in ordinary REAL either encounters its first B before the winning continuation or follows exactly the no-B stopped path through W. Hence its winning probability is at most stopped REAL probability of E=B-or-W.

**PROVED — ideal projection.** In the key-blind unflagged IDEAL continuation, honest/final public source hashes nominate at most2q+2 P values, independent of the outer grinding length. Its first-alias probability is bounded by b=min(1,(2q+2)/N). Stopped IDEAL W is contained in ordinary unflagged HJ Win. For any fixed-seed HJ winning upper bound e capped at one,

    Pr_IDEAL_stop(E) <= min(1,b+e).

This uses neither independence nor a merged auxiliary-advice game. The B and ordinary HJ winning upper bounds may overlap in their continued representation; that only loosens the sum.

**PROVED — one-projector bound.** Apply the same orthogonal terminal projector for E to the paired stopped purifications. Its projected norm is the square root of event probability, so

    Pr_REAL_original(Win | fixed nonzero S)
       <= min(1,[2Q/sqrt(N)+sqrt(min(1,b+e))]^2).

The vector loss is paid once. This is no greater than the valid two-separate-projector envelope. It does not imply a smaller general trace distance.

## 4. Complete reference bound and honest rollback

**PROVED — full finite-QROM instantiation.** Take e=min(1,c+h+g+d7), with the reviewed fixed-nonzero HJ component formulas in QUANTUM-RO-THEOREM.md. All are original-game probabilities; their separate event-only advice is not supplied to this stopped source adversary. Average nonzero seeds and charge the actual zero-seed branch once. A refined unconditional reference bound is

    epsilon_event(q,Q) <= min(1,1/N+
      [2Q/sqrt(N)+sqrt(min(1,min(1,(2q+2)/N)
                                 +min(1,c+h+g+d7)))]^2).

The minimum of this and the preserved conservative theorem is also valid. The existing exact transcript/channel coupling transfers it to honest atomic cache restoration with zero probability/query loss. Corruption, private snapshots, timing, partial buffers and retryable total services remain outside this interface.

## 5. Evidence and remaining targets

**COMPUTED — supporting controls.** Independent exact rational controls check retained quantum memory, measured adaptive source callbacks, inactive query padding, CQ active-block equality, private support and terminal projector inequalities. Negative controls refute pure-state Loewner domination and normalized surviving-key uniformity. These controls are finite discriminators, not mechanical verification of the source/channel theorem.

**COMPUTED — numerical reproduction.** bounds-event-specific.py evaluates this expression from current pinned conservative component rows. The separate240-digit dataset in quantum-private-rare-numeric predates reading those refined root outputs. At q=2^40,Q=2^32 its exponent is about57.68336. At Q=2^64 the refined estimate still caps at one. No runtime, actual forgery or work-factor level is measured here.

**OPEN — category criterion and implementation scope.** This remains a manual finite-query source-model theorem, not an efficient generic PRF/PRE/SPR/TCR embedding, checked Rust refinement, fixed-SHA statement or level/category capacity certificate. The original tiny-failure thresholds at maximum search budgets need separate examination against conventional security meanings. The full security goal stays active.

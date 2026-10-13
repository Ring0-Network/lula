# Smallest remaining lemmas

**OPEN 1 — shared oracle.** Show that the actual secret-prefix/suffix and message-hash encodings can be simulated as the desired restricted random functions except for an explicitly bounded bad-input event, with adversarial SHA prequeries and all raw message lengths included.

**OPEN 2 — derivation PRFs.** Give the two concrete hybrid distinguishers, consistent public-oracle answers, repeat memoization, query counts including simulator work, and exact advantages for the combined secret-derivation family and fresh-message randomizer. No unconditional independence statement survives after R is revealed.

**OPEN 3 — adaptive FORS.** Derive a joint distribution/coverage bound for adaptively chosen signing messages, first accepted counters, adversarial forged R/counters and every charged candidate query. Relate the computed fixed-instance average to that full game. Separately extract new leaf/tree/root witnesses.

**OPEN 4 — WOTS certification.** For a key that honestly certifies one fixed child value, classify arbitrary verifying chain evidence into chain inversion, endpoint compression binding, or a fresh child/counter digest target event; prove exact multi-target/selective-counter losses. The antichain fact alone excludes only forward extension to a different vector.

**OPEN 5 — graph embedding.** Construct an efficient/lazy complete honest-key-graph simulator, including previously unsigned routes, and turn the exhaustive first-divergence classification into the exact addressed SPR/TCR challenge with explicit time and success losses.

**OPEN 6 — composition.** Supply actual reductions for each proposed H0–H6 transition, absorb domain/prequery/message-hash and finite-search events exactly once, and sum the established bounds. Until then, total probability, total bits and certified q_max are undefined.

**OPEN 7 — total API, if claimed.** Define key-setup and signing exhaustion/abort semantics and bound their probability for a total or finitely failing oracle. This is an additional API theorem; it is not required merely to state the conditional transfer for identical partial completed-call interfaces.

**OPEN 8 — quantum reduction.** Map the exact construction to applicable quantum-secure PRF and selected-set/tweakable-hash properties, define q_s, Q_q and reduction query Q_B separately, then instantiate the full sum. A square-root interpretation of one FORS model is not that proof.

**OPEN 9 — stronger cache view, separately scoped.** If the adversary receives cached bytes, define the exact auxiliary information and simulate it; recomputability with sk is insufficient. Do not expose the benchmark fixture's seed header. If arbitrary cache writes are admitted, the current accepted-counter control already refutes universal transparency; authentication/canonicality enforcement would change the implementation and is outside this task.

**PROVED — no numerical parameter repair follows yet.** An undefined full bound has not been shown to fail at q=2^38. Increasing parameters does not prove these missing lemmas. No smallest parameter modification is justified by the present results.

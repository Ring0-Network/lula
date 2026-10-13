# Independent source-to-iid FORS namespace derivation

**PROVED / OPEN scope:** this is an independent manual derivation from the pinned source and the already reviewed joint F/J ideal game. It was saved before reading the authoring lane's new FORS bridge. It concerns classical namespace freshness and latent signing draws, not a complete forgery bound or a source refinement proof.

**COMPUTED (source binding):** release `code/lula1/src/lib.rs` SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. `prf_msg`, inner and outer hashing are at 164–187; signing uses them at 603–617; final verification at 697–704. The joint ideal game replaces secret derivations by memoized F/J, retains a shared public complete-hash 256-bit RO, and does not expose seed/cache bytes, timing or in-flight values.

## Independent event inventory

**DEFINED:** write `M=2^128`, `L=2^256`, `S=pk_seed`, `r=root`, and let `d` be the number of distinct initiated signing messages, bounded by the initiated-query budget q. For a new message m, its randomizer is `R_m=first16(J(m))`; its inner string is `I_m=R_m||S||r||m`; its full inner image is `U_m`. Outer points are `E(U,c)=U||BE32(c)||S`. Memoization makes repeated messages reuse the same R, U, counter and selected FORS indices/route.

**PROVED (no randomizer birthday term needed):** distinct messages have distinct inner strings even when their R values coincide. Fixed-width framing gives `I(R,m)=I(R',m') => R=R' and m=m'`. Thus charging a 128-bit randomizer birthday collision is unnecessary for this source's inner namespace uniqueness.

**PROVED (public-seed guard):** on `S!=0^16`, addressed honest inputs have zeros in bytes 16–31 while every inner string has S there. They cannot alias. Outer strings have length 52 and no addressed input is that short. Charge the zero-public-seed event by `1/M` rather than assume global separation on it. This charge may be shared with the joint privatization coupling if the combined proof tracks the same event once.

**PROVED (inner/outer guard):** an outer point has bytes 16–31 equal to the lower half of U, while an inner point has S there. Hence requiring `U[16:32]!=S` excludes every inner/outer input alias, independent of the root distribution or message length. Without the guard, an alias is possible only for a four-byte message with additional suffix equalities; I do not assume those root suffixes are uniformly random.

**PROVED (unpredictable new-message inner prequery):** each raw query that parses as an inner string for a not-yet-initiated message predicts one literal 128-bit R for that label. The fresh memoized J value has not been used by the program. The continued unflagged auxiliary execution must not reveal its analytical prediction flag. At most Q_H such raw predictions have total hit probability at most `Q_H/M`; there is no extra q factor because each prediction specifies one message label, and the label is tested only before its first initiation. Raw queries after that label was initiated are expected queries of an already disclosed randomizer, not unpredictable guesses.

**PROVED (outer namespace freshness):** a fresh U is a uniform 256-bit value. A signing outer family aliases another signing family iff their U values agree. It aliases an earlier raw outer point only if its U matches that point's first 32 bytes. These contribute signing U birthday pairs and signing-U/raw-prefix pairs, not 128-bit R birthday pairs.

**PROVED (fresh-message candidate collision):** a final forgery on a fresh m cannot have an inner string equal to a signing inner string. It can have a prequeried adversarial inner string. Its U can then match a signing U if a raw candidate-inner image previously hit that signing value, or if a later signing U hit an earlier such image. For an unqueried final inner input, the final verifier introduces one additional fresh 256-bit image, with at most d signing-U targets. One cannot forget this final-verifier draw.

**PROVED (one relevant 256-bit object per raw query under guards):** a relevant raw outer input whose U prefix could match a guarded signing U has bytes 16–31 different from S. It cannot also be an inner input. A relevant raw inner input has bytes 16–31 equal to S; if it is also syntactically outer, its U prefix has lower half S and cannot match guarded signing U. Thus one raw query contributes either a relevant outer-prefix candidate or a fresh-message inner-image candidate, rather than two relevant 256-bit objects. Replays of known signing inner inputs cannot serve a fresh-message forgery and must not be counted as fresh independent candidate images.

## A sufficient conservative bridge loss

**PROVED (manual bounded-game counting, pending source-to-model verification):** source/auxiliary agreement can fail on zero S, a predicted new-message inner point, a relevant fresh inner image with lower half S, a signing U/raw-candidate collision, a signing-U collision, or exhaustion of the finite counter range. A sufficient conservative loss, for q initiated requests and Q_H raw adversarial queries including prequeries, is

```
beta <= min(1,
  (2 Q_H + q + 2)/M
  + (q Q_H + q(q-1)/2 + q)/L
  + q (511/512)^(2^32)).
```

The 128-bit term consists of zero S (1), new-message R predictions (Q_H), relevant raw candidate-inner images with lower half S (at most Q_H), signing U lower halves (at most q), and one fresh final-verifier U lower half (1). The 256-bit term consists of at most qQ_H signing/candidate pairs, signing/signing pairs and q targets for a fresh final-verifier image. Using d instead of q can sharpen the source-specific term, but q is a safe cap. These are event-distance charges, not attacks or full-signature advantages.

**OPEN / proof detail to audit:** the author must specify an auxiliary execution with fresh private U and full outer tables per first message initiation, first-writer-wins public-table consistency, and no output/stopping branch on analytical Bad. Counts relying on fresh later coins are valid until first divergence; counts predicting a fixed unused J label require the continued unflagged/key-independence argument. A survival-conditioned uniform-posterior assertion would be invalid.

## Accepted bits, rejected outputs and partiality

**PROVED (ideal table property):** first acceptance tests only bits 153–161 of a full 256-bit outer image. Its 17 real nine-bit indices occupy bits 0–152; its 41-bit route occupies bits 162–202. For independent fresh outer images, the first accepted image's retained indices and route are jointly uniform and independent of the rejected trial count and rejected trial outputs' retained bits. This is a statement about an unconditioned auxiliary draw, not a statement after conditioning on no collision/guess Bad event.

**PROVED (finite search distinction):** the u32 loop has only `2^32` distinct counter inputs. If all fail, wraparound repeats them or a checked build panics; new independent draws do not continue forever. Its iid-table exhaustion probability is exactly `(511/512)^(2^32)`. An infinite geometric sampler differs from the partial source on that event and must charge it. Conditioning on a completed search gives a uniform accepted retained vector, but is not a license to normalize the complete source experiment on setup/signing success without controlling the changed distribution.

**PROVED (rejected outputs are not extra iid exposures):** failed outer hashes reveal no FORS certificate and no new signing exposure. A rejected or later accepted output from a known signing U family cannot verify a fresh-message forgery unless its fresh inner hash also reproduces that U, which is the 256-bit candidate collision event. Raw oracle queries must still be included in Q_H; rejected output knowledge is not free random-oracle access by the adversary.

**PROVED (latent draws and adaptive stopping):** the auxiliary process can reserve independent route/index draws for all q distinct-message slots, even if the adversary stops earlier. The actual exposed sequence is a prefix/subsequence of those slots with exact repeats for repeated messages. Adding unused independent exposures up to q can only increase coordinate-wise coverage. The exposed transcript conditioned on an adversarial stopping rule, completion or absence of Bad need not itself be iid; the coupling uses latent unconditioned draws and explicit failure charges instead.

**OPEN (scope):** the accounting assumes an atomic absorbing partial-signing interface and q initiated attempts. Retryable failures or unlimited interrupted attempts need a different attempt budget. The iid latent signing model alone does not prove an adaptive FORS coverage theorem, efficiency of the simulator, or the complete signer's EUF-CMA bound.

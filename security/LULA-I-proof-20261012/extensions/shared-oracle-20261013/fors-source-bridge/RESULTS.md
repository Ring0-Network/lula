# Source-bound coverage bridge: result and review boundary

**PROVED under the stated joint ideal game; manual source refinement.** The source's actual I(R,m)=R||S||root||m and E(U,c)=U||BE32(c)||S interfaces admit a stopped coupling to the prior independent exposure/candidate streams. The derivation is in `DERIVATION.md`. It is not a full reference-signer security proof, a theorem about fixed SHA-256, or a QROM result. Root synthesis must await the requested independent rederivation of the source coupling.

## Bound

For q initiated atomic signing requests, Q_H raw classical adversarial SHA queries and one final verification, define

    beta = min(1, (2Q_H+q+2)/2^128
                  + [q Q_H+binom(q,2)+q]/2^256
                  + q(1-1/512)^(2^32)).

Then the joint ideal game's covered-leaf route has upper bound

    min(1, beta + min(1,(Q_H+1)*p_fixed(q))).

**ASSUMED:** the inherited classical shared complete-SHA random-oracle game and joint ideal F/J replacement, uniform independent key components, atomic completed-call interface, fixed actual parameters, and ordinary fresh-message verification. The bound concerns coverage of honest disclosed FORS leaves, not all ways of producing verifying signatures. Other chain/node/root witnesses require separate extraction.

**PROVED — main improvements.** Public inner prequeries predict one unseen ideal J(m) value at their unique raw message suffix, so their total charge is Q_I/2^128, without a q multiplier. Repeating R across different messages does not alias their complete inner inputs. Restricting eligible outer inputs to U[16:32]!=S removes literal I/E aliases while charging any actual inner-derived U ending in S. Namespace guesses and relevant full-U collisions then account for public previewing and replaying honest grinding points.

**PROVED — counting qualification.** Let N_I/N_E be actual random distinct-query counts in the disjoint input classes. Detailed probability bounds use their expectations Q_I/Q_E, not an observed count and not separately maximized allocations. Since N_I+N_E<=Q_H pathwise, qQ_I+qQ_E<=qQ_H. The q factor is necessary for a U-prefix guess that has no message label; one guessed namespace may match any future honest inner output. Honest/honest and final/honest collisions add binom(q,2)+q pairs.

**REPAIR — independent review finding.** An intermediate paragraph originally used Q_E+1 as the candidate padding cap after Q_E had been defined as E[N_E]. That was invalid: an expectation is not a pathwise cap, and the adaptive allocation can depend on the realized coverage. The repaired derivation uses N_E+1<=Q_H+1 for actual counts and pads only to deterministic Q_H+1. The displayed final bound already used Q_H+1 and is unchanged. Expectation notation remains only in predictable bad-event pair accounting. Before/after hashes are preserved in `PADDING_CAP_REPAIR.json`.

**PROVED — full final-point partition.** An old rejected honest digest cannot pass the zero filter. An old accepted digest, or an unevaluated counter in an old honest U namespace, can serve a fresh message only through a charged inner-U collision. An old nonhonest public outer point is a retained candidate. An unqueried nonhonest final point is the extra one verification opportunity. Eligible outer points cannot be addressed or inner-language points. Previously rejected outputs are not renamed accepted samples.

## Public-seed and composition scope

**PROVED — unconditional scope.** Beta explicitly pays 2^-128 for S=0. All input-language separations use S!=0. For any fixed nonzero S, omit that one term to obtain the corresponding alpha bound; there is no source modification rejecting a zero seed. Averaging that argument, with success bounded by one on the zero branch, gives the unconditional beta. No successful-setup conditioning or survivor-posterior renormalization is performed.

Two independent unconditional triangle bounds yield delta_joint+beta and pay the zero-S branch twice conservatively. Paying it once requires a simultaneous coupling with a shared first-bad flag. The derivation does not silently subtract the duplicate contribution or claim that a fixed-nonzero statement is automatically unconditional.

## Executable controls

**COMPUTED.** `python -I -B bridge_checks.py` completed with exit code 0. A later run, after adding the exhaustive final-point discriminator, also completed with exit code 0. `CHECKS.json` identifies the original source/driver hashes, validates 12 source-interface snippets, records exact rational controls and exposes sufficient-loss components for several raw-query budgets. No signing API, full cache, timing measurement or manuscript edit was executed.

The exact controls are:

- Two four-valued unseen message-randomizer predictions: actual hit 7/16, total-prediction union bound 1/2; the naive q-times-total bound is 1. A single fixed message prediction remains 1/4 under repeated signing.
- Two messages with two-valued R: R repeats with probability 1/2, but full I inputs never alias. Omitting the message in a negative control creates alias probability 1/2.
- Reduced literal I/E framing: four unrestricted intersections, zero eligible intersections. A full 52-byte source-format overlap is constructed without hashing and is excluded exactly because its U half equals S. This artificial root is a format witness, not a generated signing key.
- Two counter points with one guessed U prefix: one future U hits with probability 1/4; two future U draws give 7/16, bounded by q times the distinct-prefix probability. Counter count is not namespace count.
- Survivor-conditioning control: an unconditioned candidate bit has probability 1/2; an adaptive prefix-guess schedule makes its probability 3/4 after conditioning on no guess hit. This confirms why the proof uses unconditional stopped coupling/padding.
- Relevant inner-U collisions: one honest target, two public values and one final value have exact collision probability 37/64, within the three-target union bound 3/4.
- All 16 reduced (U,c) final cases are partitioned into endpoint bad event, rejected honest point, accepted honest replay, new counter in old namespace, retained public candidate, or extra final point. A deliberately preinstalled accepted first-counter value correlates the honest exposure with a public candidate and is caught by Bad_Epre.
- Adaptive-budget control: N(T)=0 or2 gives mean count1. Correlating allocation with transcript coverage gives actual success3/8, exceeding the invalid expectation-count bound1/4, while deterministic cap2 yields valid union bound1/2. This directly discriminates the repaired intermediate step.

These finite controls discriminate accounting and input cases; they do not exhaust all adversarial algorithms or mechanize the source proof. Full reference/cached EUF bounds and the QROM bound remain null in the result receipt.

## Review obligation

**OPEN:** independently validate the manual source-to-game coupling and its stopped-event budget. Then integrate it with the already proved joint private-input replacement and prove the exhaustive full-signature forgery classification, efficient witness extraction, and remaining primitive/composition terms. A counterexample within these stated good events was not found by this derivation; the finite controls alone do not establish its absence.

**Outcome:** JOINT_IDEAL_FORS_COVERAGE_BRIDGE_DERIVED; INDEPENDENT_SOURCE_REVIEW_PENDING; FULL_EUF_CMA_NOT_ESTABLISHED.

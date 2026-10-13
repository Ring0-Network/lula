# Independent second-reader verdict: conservative classical composition

**Outcome: ACCEPTED_MANUAL_CLASSICAL_COMPLETE_SOURCE_RO_EVENT_BOUND.** I independently derived the exhaustive source-verifier classification before reading the root candidate or the canonical-target lane. I then checked the conservative root composition against the accepted component proofs. No missing accepting-fresh-forgery branch or incompatible game projection was found in the stated classical, partial, atomic single-root source experiment. This is a direct complete-hash RO theorem within that model, not an efficient standard-model primitive reduction, fixed-SHA guarantee, checked Rust refinement, QROM result, or work-factor/capacity certification.

## Exact reviewed subject

Root candidate `COMPOSITION-DRAFT.md` SHA-256 at review: `21ee235fec883dc8e55c8b4f8759df3d76e722292cf5a2065cae2ab2ef1536dd`.

Fixed release `lib.rs` SHA-256: `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

Component derivation hashes at review:

| File | SHA-256 |
|---|---|
| code-game/DERIVATION.md | 2c84f14175c0ffd1685210926a15cd033a867be934f027c6a2f29e24eadfdfa3 |
| fors-source-bridge/DERIVATION.md | 2515bbec53db0cf3bde805c38a0c6c00ac45cd899c3c1407a7d6e81ab7978752 |
| hidden-values/DERIVATION.md | 6c612d407aa326634a3c5d3591a5b22d55a331774679fc2b46dff038bb9f15ed |
| graph-targets/DERIVATION.md | 3a61a88cbad28796c62ae94484d984ad3ed73320612f64469ad987c6e809346c |
| canonical-targets/DERIVATION.md | 74171ac638fd9daa7cc05881612c1ace8681f153ced29e7af806985d17835dd6 |

I read the repaired FORS and canonical-target second-reader reviews, and the earlier independent hidden/graph reviews, after my own classification was saved. No paper, source, frozen packet, or peer output was modified.

## Classification and common-game checks

**PROVED (same probability space).** C,H,G,D7 are defined as events of the same ordinary joint F/J source game HJ for fixed nonzero S. The H blinded continuation only proves an event-distance statement, with agreement until first H, and does not replace the space in which classification is performed. G and D7 may use separate full-graph advice experiments whose projections are HJ. These enlarged views are not fed into H and are not substituted into the complete EUF experiment. An adversary ignoring the extra advice is the required projection. This eliminates the apparent conflict between full secret-graph exposure for collision analysis and secrecy needed for hidden inputs.

**PROVED (actual final trace).** Acceptance fixes the top root. Ordered same-address Merkle reconstruction, endpoint compression, and addressed chain completion give genuine starts or an actual G witness. An unexposed WOTS key must contain a nonterminal genuine start, hence H. An exposed key with a different accepted vector has at least one digit below its known suffix, hence H. An equal vector and changed child/counter produces D7 because all 128 digest bits are consumed. Otherwise its child equals the fixed honest child. Downward induction pins the FORS PK; roots compression, paths and leaf hashes give G,H,or previous exposure of all selected real secrets. Acceptance supplies the omitted zero filter, hence C. The argument does not presume that a forged path was previously signed, does not presume a canonical vector at every unused key, and includes adversarial R/c and every serialized field.

**PROVED (final counts).** H gets 3000 WOTS chain completions plus 17 FORS leaves: 3017. G gets those chain completions, FORS leaf/path/root work, five PK compressors and 41 hypertree path nodes: 3217 complete calls. D7 gets one digest per reached layer: at most 5. Final I/E evaluations are the separate +1 draw/output obligations in the FORS bridge and two public-secret candidates in joint privatization. Local adversarial verification must already consume Q_H. No compression-operation count is substituted for a complete public-O evaluation count.

**PROVED (partial setup/signing).** q bounds initiated atomic requests, not only successful returns. Failed/nonterminating metadata searches reveal no partial output and prevent winning completion. The game is unconditioned; no division by successful-search probability occurs in any component sum. The FORS bridge conservatively pads latent unused exposures to q and uses deterministic Q_H+1 candidate padding, not expected eligible-query counts. Arbitrary retry-after-failure, free extra verifier calls, intermediate disclosures, timings and corrupt cache are different interfaces.

**PROVED (source-to-HJ loss).** Joint private replacement pays `(Q_H+2q+2)/N` for fixed nonzero S. Unused K/P independence is asserted in the unflagged joint-ideal execution, not in the REAL posterior. Each ordinary raw query identifies at most one literal private-key guess family. Honest I/E calls add at most two P candidates per initiation and two for final verification. Billions of typed tree hashes neither multiply this candidate count nor supply free hidden queries.

**PROVED (single seed-zero charge).** Every component statement used here is first established for every fixed nonzero S with uniform independent unused private K/P. Average these uniform bounds over nonzero S, then upper-bound the complete REAL winning probability on S=0 by 1 and add `1/N`. This is a direct conditional calculation, not subtraction from two unrelated unconditional triangle estimates. The upper bound on the whole nonzero branch can drop its probability weight conservatively. The derivations themselves give the necessary fixed-S versions explicitly; their displayed unconditional standalone formulas are not what is added here.

## Exact coefficient recombination

**PROVED.** Put `N=2^128`, `C=2^32`, and

    p_F(q) = (1/512) E[(1-(511/512)^T)^17],
    T ~ Binomial(q,1/2^41).

For fixed nonzero S, add the accepted uncapped terms:

    delta_J: (Q_H+2q+2)/N
    beta:    (2Q_H+q+1)/N
              + [qQ_H+binom(q,2)+q]/N^2
              + q(511/512)^C
    C:       (Q_H+1)p_F(q), in addition to beta
    H:       (Q_H+3017)/N
    G:       (Q_H+3217)/N
    D7:      (Q_H+5)/N.

Then add `1/N` for S=0 once. The coefficient identities are

    Q_H: 1+2+1+1+1 = 6,
    q:   2+1 = 3,
    constants: 2+1+3017+3217+5+1 = 6243.

Consequently the reviewed conservative bound is

    epsilon_RO(q,Q_H) <= min(1,
       (6Q_H+3q+6243)/N
       + [qQ_H+binom(q,2)+q]/N^2
       + q(511/512)^(2^32)
       + (Q_H+1)p_F(q)).

Each component can independently be capped at one, but leaving positive terms uncapped and capping only the final sum is a valid conservative upper bound and simplifies exact arithmetic. The result is an advantage upper bound parameterized by q and Q_H; `-log2` of it is an exponent of that upper bound, not a security work factor, a per-candidate exponent, or proof of an attack.

**PROVED (setup conditioning when separately requested).** For the real-source top-row completion event K under the declared complete-hash model and physical success assumptions, `Pr(Win|K) <= Pr(Win)/Pr(K)`. The top row child graph is independent of type 7, so `Pr(K)=[1-(1-p_top)^(2^32)]^(2^21)`. This is unnecessary for the unconditioned partial theorem and does not justify conditioning on arbitrary execution success, time limits or memory scheduling. Partial preparation has no new abort API.

## Standing limits and optional improvement

**OPEN (outside model).** The result does not establish a standard-model secret-PRF/SPR/TCR reduction, a QROM signer theorem, actual SHA-256 security, timing leakage protection, arbitrary-corruption transparency, a polynomial worst-case simulator, or a checked source semantics refinement. None is smuggled into the accepted direct RO event statement. A claimed category or concrete signing capacity needs its separately specified resource-success criterion; a vacuous sufficient bound is neither an attack nor an empirical result.

**UNPROMOTED (optional separate improvement).** My independent derivation offers joint G/D7 conditioning to replace their separate Q_H terms by one and obtain a 5Q_H leading coefficient. The reviewed root target remains the conservative 6Q_H version. The optional sharpening is not used in this verdict or in the requested numerical validation; it needs a distinct peer review.

**Status: BASE_CLASSICAL_COMPOSITION_ACCEPTED_BY_THIS_INDEPENDENT_READER.** Independent executable numerical and toy receipts will be saved here; they do not change this immutable reviewed root candidate.

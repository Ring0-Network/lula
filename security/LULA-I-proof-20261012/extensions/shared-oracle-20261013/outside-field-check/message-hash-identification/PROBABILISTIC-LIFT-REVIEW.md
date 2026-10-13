# Independent review: ordinary free-counter ITSR with counter-guess loss

**Verdict: ACCEPT_MANUAL_LAWFUL_ONE_SIDED_PRIMARY_FREE_COUNTER_ITSR_LIFT; HARDNESS_UNEVALUATED.** Own new firstc558 was saved before reading selected9c1f. The earlier canonical-family separator remains valid and immutable; its family is H_can, whereas this reduction assumes ITSR of an explicitly different H_free linked to the fixed h.

## Subject and controlling refinements

Reviewed selected `COUNTER-GUESS-LIFT.md` SHA256 `9c1fadb8eedc8dbf19f20800a0950836433c00f0782297d9f315fca0328433ca`, plus `COUNTER-GUESS-INPUT-COMPLETION.md`, `COUNTER-GUESS-MAP-CLARIFICATION.md`, and `COUNTER-GUESS-SOURCE-ROUTE.md`. Input completion states a fixed40+B-byte input register, injective valid S16||Z16||c4||length4||M||padding and an explicit two-hash invalid-code completion using the SAME h. The source adapter queries only valid codewords. The specified complete family, including invalid inputs, belongs in any insecurity assumption; none of its hardness is proved.

The route-first450-bit output refinement fixes a public field permutation: (S,Z,I41) followed by17 real9-bit indices. MAP's virtual route width297 includes256 common/chosen context bits; it supplies no297-bit route entropy and changes no source h41 formula. The actual full256 inner/outer source hashes and byte frames remain unchanged. Neither the source filter nor a nonexistent eighteenth secret is folded into this17-coordinate map.

## Why the all-label route is lawful and stronger than my abort route

On every new source M, B chooses uniform32-bit guess g before querying the PRIMARY oracle on Enc(S,Z,M,g). The oracle returns fresh uniform R AND the mapped output. B stores only R for its source J[M]; it does not use the guessed mapped word to select source indices, decide source completion, choose future messages, or return source data. B computes the actual canonical c0 and complete signature locally with its retained F and the SAME public h. Repeated messages reuse that J nonce and canonical result.

Uniform R is independent of the chosen guess/input by the primary definition. Source-visible behavior does not consult the returned guessed target data or guess. Fixed h is read-only public code; target evaluations neither program it nor create a new random-function transcript. Thus the full adaptive source-facing channel, including quantum A's continuation, is exactly SrcFJideal_h and is independent of the guess vector. This statement would FAIL if B filtered out oracle replies based on guessed-image acceptance, aborted whenever g!=c0, forwarded the guessed digest to A, or used it in future source decisions. None of those operations occurs in the accepted program.

The proof then chooses its witness set AFTER the source final event. In each Win AND indexed C_cov history, choose an earliest completed signature exposing each of the17 final tuples and deduplicate message labels. Its size d<=min(17,q) and its canonical counters are functions of the source history, not guesses. Conditional on that history, all d guesses match with probability L^-d, L=2^32. On those matches the corresponding registered PRIMARY tuple sets equal the source witness sets. Extra targets from incorrect guesses can only enlarge the covering union. Final M* is fresh among every initiated source request, so the encoded candidate is a new primitive input regardless of nonce/counter collisions.

Therefore the selected bound is correct:

Succ_primary_ITSR(H_free;B_all) >= L^-17 Pr_SrcFJideal_h[Win AND C_cov],

Pr_SrcFJideal_h[Win AND C_cov] <= min(1,2^544 Succ_primary_ITSR(H_free;B_all)).

For a fixed q<17 the exponent can be sharpened to min(17,q), but the stated17 bound is conservative. B_all uses q_distinct<=q primary targets, ALL source signing work and no artificial guess abort. Its source marginal does not change when guesses are wrong. Natural setup/search/downstream signature noncompletion remains absorbing and contributes zero; no1/tau normalization, nonce resampling or seed-zero penalty is introduced.

My own first's full-query ABORT program instead matches every queried canonical counter and obtains L^q. Its sparse selector program uses at most k=min(17,q) primary targets but adds a Q^k factor, Q the padded power-of-two message-ordinal range, giving (Q L)^k. Both are valid alternatives with different programs/resources; neither contradicts B_all's stronger probability loss. In this source-relative setting B_all's q target calls preserve the exact source marginal and avoid the selector factor, while the sparse alternative can matter if target count itself is constrained. Their insecurity parameters must reflect q versus k and their actual runtime; no success value is equated across those different adversaries by assertion.

## Event, context, resources and scope

The event remains Win AND C_cov, with fresh final M*, valid filter/parser/root acceptance and17 real indexed tuples at one I covered by COMPLETED honest responses across branches. It is not bare coverage, an old-message forgery, or a bound for H/G/public-graph replacements. B retains its own consistent F to generate all source signature auxiliaries; F is not advice or an extra oracle to A. Actual S/root/F/setup correlation is retained; no independent uniform root is substituted. Tags are logical input/output metadata decoded before evaluating the literal source h words.

Primary H_free is TOTAL and freely evaluates any supplied counter. It does not stop/condition its nonce sampler on the zero9 predicate. Ineligible guessed targets may still be registered; B's source candidate is eligible and the matched witnesses are canonical eligible source targets. A filtered/non-returning target sampler would be a different game and break the stated source-nonce coupling.

Each ordinary target costs one full inner and one full outer evaluation plus parsing/map costs; its invalid-code branch has the stated two-hash cost. B independently performs the complete actual source canonical search and remaining setup/FORS/WOTS/final work, private dictionaries/cache/message storage and quantum public-h circuit/generation costs. Challenger work is separately charged. Public A computation/runtime is not reduced to nominal A-only hash-query counts. This is a finite source-relative program, not a practical benchmark.

ITSR of the exact free-counter/tagged/total family is an explicit named assumption. The2^544 factor is a mathematical reduction loss, not a measured or certified security level. Neither the450-bit output nor297-bit route field is asserted random. No generic ITSR/RO estimate, canonical-family hardness, private-prefix hardness, or HJ[h]=HJ[O] identity is imported. Adequate fixed-h numerical security, other public primitives and complete category/capacity remain OPEN.

## Independent finite controls

`probabilistic_lift_controls.py` exited0. It enumerates4,624 small selector/nonce/guess worlds with17 REAL coordinates, source-derived context/auxiliary relation, adaptive second-message choice, repeated labels and natural counter bottom. All-label source-view distributions are identical for every guess vector. Wrong NONwitness guesses can remain wrong while the primitive wins, directly disproving the need to match all signing labels. For the two-message two-witness case source coverage1 gives all-label success1/4 and sparse success1/8; in the repeated/adaptive/bottom case source coverage3/4 gives all-label success3/16 and sparse success27/512. These exact toy numbers validate the distinct probability/resource mechanisms, not source or SHA security. Every natural-bottom probability is unnormalized.

The controls also attach an optional virtual eighteenth filter coordinate and show identical winning outcomes without additional targets/counter guesses. The general optional variant below supplies its manual justification.

I also read the peer's reciprocal review c43480c9 and receipt b3633fdc. I copied and independently reexecuted both current peer control scripts in my own `counter-guess-peer-recheck` folder; both exited0 and their result files are byte-identical to the peer's pinned outputs. The first checks60 guess-vector cases and64 injective valid input codes. The second checks54 adaptive source-history/witness cases, retained dummy/duplicate selector slots, and unnormalized natural completion masses3/4,11/16,43/64,171/256. These are finite coupling/interface controls, not source signatures, SHA attacks or a checked quantum proof.

## Optional k18 MAP variant, without an eighteenth source secret

Define an alternative PRIMARY map using all18 source9-bit digest fields, including the forced index at positions153–161. On a source-eligible final candidate that virtual coordinate is0. Every canonical matched witness target has the same forced0. C_cov's17 tuples ensure that a nonempty collection of witness signatures exists at the final common I; one of these already supplies the virtual(I,17,0) tuple. Thus the same d<=17 matched messages cover all18 virtual coordinates. B_all still pays at most L^17 and the sparse route still needs at most17 witness labels, not18.

This is a different precise MAP/family instance: route297 plus18*9 bits gives459 virtual output bits in a route-first layout, or an untagged203-bit source-field layout may be specified separately. There is NO additional private/FORS tree or secret exposure, and no extra uniformity or generic-gamma assumption. The18-coordinate variant is optional and is not needed to validate the reviewed17-coordinate lift.

## No new security kernel claim

This lift is a manual adaptive-channel/covered-witness argument. The previously reviewed three DigestProjection helpers prove only their bit-function statements, not this ITSR reduction or source execution. No new kernel declaration is added by this lift; all old canonical-separation, first-save, source, manuscript, numeric and prior-receipt artifacts remain intact.

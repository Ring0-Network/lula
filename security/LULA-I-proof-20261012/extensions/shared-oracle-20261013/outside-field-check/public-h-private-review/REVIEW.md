# Independent review of ordinary private PRFs for public fixed h

**Verdict: ACCEPT_EXACT_ORDINARY_PUBLIC_PARAMETER_PRIVATE_PRF_ADAPTER_IDENTITIES_WITH_CHARGED_SOURCE_RELATIVE_RESOURCES.** This is an independent source-first mathematical review of the named private hops. It proves no hardness or numerical private advantage and imports no RO estimate.

## Independent first save and reviewed subject

My `INDEPENDENT-FIRST.md` SHA256 `ce1595126df47f472fed0a7a1489840f1fabbc4e8490604e73baeaa397014cca` was saved before opening the author's new private-hop packet or controls. I inspected the release source `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`: source prefix initialization/typed hashing at109–147, private functions161–168, key generation498 onward, signing601 onward, and exact final verification672 onward. The independent first argument derives the ordinary game, chronology, signed identities, zero-seed aliases, partiality, and private-label caps.

Reviewed immutable author subject: `chain-pre-adapter/public-h-private/INDEPENDENT-DERIVATION.md`, SHA256 `6c44c1b3cce9cc5438f333031258b1c392069a171b1c6358e6354af6d9aab1af`. Controlling clarification: `020a34efad2c4553e5b4f7d47d3a8acaaa424365c84940452f1d6c4605952d6e`. Successor provenance: `b9caf4515b86f911182e9117224d43569da2672ba64d25501fac73ab08047ed5`. The original and successor controls were inspected, copied byte-for-byte into this reviewer's authorized folder, and independently executed there, both with exit0. The original author's files/results remain untouched.

## Exact ordinary interfaces and identities

The family definitions are precisely

f_K^S(A)=prefix128 h(S||zero48||AD22(A)||K16),
g_P^S(M)=prefix128 h(P16||S16||M).

S,K,P are independent uniform16-byte strings. h is ONE fixed public full256 implementation, available for ordinary local or clean quantum computation. The PRF challenger supplies only the private128-bit function interface. Its query outputs need no independently simulated lower128 limbs: source private functions use only16 bytes, while all raw/public full256 computations still evaluate the same h. No separate sampled Raw, domain retagging, word patching or key-distinctness premise is used.

For a fixed S these are ordinary keyed-family real/random games. For source's random S, the named public-parameter experiment samples S independently and discloses it to B. This definition gives exact averaged game identities. The source adversary's interface can still withhold S/pk until setup: knowledge by the reduction is not disclosure to A. A game that keeps S secret from B is different and is not silently substituted.

Let p0,pF,pFJ denote final source Win probabilities under real private functions, ideal F only, and ideal F/J. B_K returns the exact source Win bit with its f oracle and independently sampled P. B_P returns that bit with its g oracle and a persistent independently sampled F. Their SIGNED gaps are exactly

p0-pF=Pr[B_K^real=1]-Pr[B_K^ideal=1],
pF-pFJ=Pr[B_P^real=1]-Pr[B_P^ideal=1].

The absolute value of each equals that PARTICULAR distinguisher's PRF advantage under the stated convention, with no factor1/2. A supremum family insecurity upper-bounds these particular advantages. The total absolute gap is bounded by their sum, not equal to it. In a pointwise-S presentation average the signed probabilities first; an average of absolute pointwise gaps is an upper bound, not necessarily the same advantage. The clarification makes this distinction correctly.

## Source chronology, correlation and partiality

Both reductions retain A's pre-key quantum continuation, withholding S and pk; run the obligatory adapted top-prepared setup; release the resulting pk only on completion; answer atomic CLASSICAL signing requests; preserve exact complete-message freshness; and perform the source verifier with final-root equality. Every private call is intercepted, so unreachable placeholder key fields are never used by an unadapted private routine. Final verification calls no private interface.

All private-oracle calls are classical setup/signing labels. Quantum A may compute the public h coherently, with the charged clean reversible circuit and matched input-register convention. The proof does not require coherent private PRF queries, a quantum lazy private table, or classical simulation of A's amplitudes. It uses the same interleaved quantum adversary computation and the exact private-service replies in the corresponding game arms.

Literal aliases, including those at S=0, are retained in REAL because h is unchanged. In IDEAL the private map is replaced while local raw h remains h, exactly as the ordinary PRF game defines. Guessed secret-word public evaluations are an allowed distinguishing strategy charged to computation; they are not prohibited, independently completed, or bounded by an old RO guessing formula. The two private-hop identities include S=0 and need no added seed-zero term. A later nonzero-S component bound may charge that case once in its own assembly.

The same finite partial-service totalization is used in all game arms: at most2^32 distinct counter attempts, no invented exhaustion transcript, and absorbing nonwinning behavior on noncompletion. Completion probabilities may differ between arms and are included in the ordinary oracle gap. No native Rust overflow/termination theorem is inferred. Persistent maps/memoization reuse labels across repeated messages, source recomputation, and honest restoration; fresh random outputs are not asserted independent of a signature that already reveals them.

## Resources

The source dependency loops reproduce the setup private count2^21*(16+32*32)=2,181,038,080. Conservative distinct per-signature caps are hot17*512+4*32*32+16=12,816 and cold2^21*16+17*512+4*32*32=33,567,232. Selected secrets/chain starts are repeated labels, so their extra invocations do not increase distinct-label caps. Their invocation counts hot12,961 and cold33,567,393 agree with the additional repeated source derivations. Final verification adds zero private calls. Thus f queries/F-map storage are capped by min(N_D,U_setup+qU_mode), and g queries by q. These are concrete reduction budgets, not A's public hash count. The source namespace N_D and public-call ledger are inherited reviewed bounds; no complete new namespace/public-call audit is claimed here.

B_K locally evaluates known-P randomizers, adding at most q public h calls to R_src=H_setup+qH_mode+3224; B_P gets them from its g oracle and has R_src local calls. Adversarial public-h circuit calls and inlined h work are accounted for disjointly from t_A. The source's very large honest work, serialization, dictionary operations, cache/tree storage, message bytes and circuit-generation costs remain charged. A whole-hash call is not a compression count or a zero-cost oracle operation.

The first candidate's runtime explicitly excludes private-challenger execution. Its clarification supplies total-execution costs: REAL B_K's challenger may evaluate D private102-byte frames; REAL B_P's challenger evaluates up to q frames of32+|M| bytes. IDEAL challengers instead sample/store one16-byte value per first label. This distinction is correct, and neither cost is a new external Raw query. The stated source-relative runtime/storage envelopes are conservative, not practical timing or cryptographic-security certificates.

## Executed controls and limits

The peer original controls enumerate8 REAL worlds,16 F-ideal/P-real worlds and128 fully ideal worlds, matching the complete TOY source-facing transcript against the adapters. They check memoized restoration, pre-key disclosure order, prefix-only private versus full public output, four scaled zero-seed alias cases,124 public XOR involution cases, and an independent-Raw negative. The original fixed toy algorithm completes every setup search; the original receipt's bottom flag only represented a branch in the program. The successor correctly adds eight constant-public-h worlds that actually exhaust setup, return nonwinning/no-pk views and make no B_P randomizer query. These are concrete toy examples of the absorbing branch, not exhaustive actual-LULA noncompletion verification.

My additional actual-byte control tests16 full102-byte f/g frame combinations and verifies the four S=P=zero aliases using the literal70-byte message zero32||AD22||K16. Public SHA evaluation is used solely to check equal-byte/equal-output serialization and16-byte versus32-byte output widths, not to estimate pseudorandomness. The message contains the test K; this is a byte-identity control, not an adversarial forgery or key-recovery experiment. It also checks48 full256 XOR involutions, eight source-relative resource profiles, signed telescoping, a strict triangle example, and signed-parameter cancellation.

All three control executions exited0. The negative arithmetic controls show total absolute gap1/4 while the sum of private absolute gaps is1/2, and averaged signed gap0 while average absolute pointwise gap is1/4. They directly guard the exact distinctions in the review.

Closed: source-relative ordinary public-fixed-h private adapter identities, chronology/correlation/zero-seed accounting, classical-private/quantum-public interface, and the declared complete resource convention. Remaining: hardness and numerical advantages of f/g, public-component/final-forgery bounds for fixed h, conventional/full-security assembly, category/capacity and checked source/quantum-game refinement. No earlier external-RO/QROM residual term or numerical theorem is transplanted. No kernel theorem is added, and no source/manuscript/global/prior-receipt file is edited.

**Explicit full-message-hash frontier.** The two private assumptions concern only128-bit outputs. They certify neither the complete H_msg digest distribution nor its lower128 bits used in the FORS/hypertree route, adaptive coverage, or the full public source graph. A simple logical countermodel replaces any public h by h'(word)=prefix128 h(word)||zero128. Every f/g output remains IDENTICAL for every input/key/seed, so any private-prefix PRF hypothesis has exactly the same meaning, yet H_msg's lower128 output bits and route bits162–202 are fixed rather than uniform. This is a property non-implication, not an actual SHA alteration/attack. The additional executable control checks this byte identity and forced route on the same test frames. SrcFJideal_h therefore is not identified with HJ[O], and a separate fixed-h full-message-hash/adaptive-coverage/public-graph lemma remains OPEN.

# Independent second-reader review: hidden coordinates

**Outcome: PASS_SCOPED_CLASSICAL_HIDDEN_VALUE_LEMMA.** No counterexample was found within the author's stated predictable-disclosure, continued-ideal, nonzero-seed joint F/J ideal game. The source-model selector argument is justified manually for the fixed source. This approves a component event/coupling bound, not full EUF-CMA security, an efficient reduction, a real-SHA theorem, successful-setup normalization, or any QROM bound.

## Independence and immutable subject

I saved `INDEPENDENT_DERIVATION.md` before reading the author's `hidden-values/DERIVATION.md`. The source was read directly, including address encoding, WOTS construction/grinding, FORS generation and verification, fixed child values, completed signing, and final verification. Source SHA-256 remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

Reviewed author files:

- `hidden-values/DERIVATION.md`: SHA-256 `6c612d407aa326634a3c5d3591a5b22d55a331774679fc2b46dff038bb9f15ed`.
- `hidden-values/control.py`: SHA-256 `1ee8f066f09529c10a550b29e5a0209f4510851a07f5cd7374311f2183ba077c`.
- `hidden-values/CONTROL-RESULTS.json`: SHA-256 `3f920be9247a863ace947cd82b8cfd78ac4411746246d45f18c1f33065c8c56b`.

I read the author's controls and their saved receipt, but did not run that writer script in the author's directory. Independent executable checks are owned here and ran with exit 0.

## Findings against exact passages

| Obligation | Author locator | Independent result |
|---|---|---|
| Ordinary RO marginal | DERIVATION.md 17-19 | PASS. Each chain step uses a different full address; its designated input depends on earlier restrictions. Independent full-image sampling plus residual completion gives the ordinary full-function marginal jointly with F starts. Exact leaf and two-step chain distributions were independently enumerated in two arrangements and agree. |
| Public advice must conceal protected inputs | 21-23 | PASS. Endpoints, FORS leaf images, and public compression/node graph are independent of hidden prefixes in the eager sampler. Interior chain images are also later chain payloads and cannot be included. The author's explicit exclusion of the earlier full-payload graph is essential. |
| Dynamic exposure must preserve old replies | 27-35 | PASS. The continued ideal table never overwrites a prior reply. Newly installed points are fresh on coupled no-hit paths; disagreement after a previously charged hit is permitted. Full images, including their unused halves, are installed once. |
| Adaptive hidden-coordinate independence | 39-41 | PASS within the continued ideal experiment. “Unflagged” must mean the analytical flag is absent from the public history, not conditioning on flag=false. Line 41 explicitly prohibits the latter conditioning. The continued execution neither branches on nor stops at a hit. Predictable selection plus suffix closure leaves remaining variables unused and independent. |
| Actual source selection | 43-47 | PASS manually. Source `child_value` 486-499 fixes a child per full WOTS address. Type-7 grinding 216-237 examines public child/counter values in separate restrictions. H_msg routes use independent J and public function replies in disjoint raw languages for nonzero seed. Consequently digit/leaf selection does not inspect protected prefixes. The source's internal output buffer is not public before return. No checked Rust refinement is claimed. |
| Prequeries | 57, 65 | PASS with the explicit interpretation that Q_public includes every adversarial public-O evaluation, including prekey calls. Eager key/latent sampling before an unobserving prekey phase preserves the joint marginal; future exposure does not erase an earlier hit. Old replies cannot be reprogrammed at key generation or reveal time. |
| Final altered verifier schedule | 59-65 | PASS. Acceptance fixes four lower digit sums to 240 and the top sum to 2040, hence chain-completion counts 4*(32*15-240)+(16*255-2040)=3000. Add 17 FORS leaf hashes: 3017. Early rejection reduces it. Later forged route/address choices remain predictable functions of prior public history. |
| Seed-zero qualification | 65-67 | PASS standalone. Fixed nonzero-seed bound has no zero-seed term; uniformly chosen seed adds 2^-128 if charged here. A composition that charges it once must construct a simultaneous stopped coupling; two independently unconditional triangle bounds cannot silently discard a duplicate. |
| Broader event classification | 71-73 | PASS as a boundary argument. A different chain payload reaching the genuine endpoint must meet a designated same-address image at some step; a genuine unseen payload is the hidden event. This alone does not handle fresh child/counter certifications or FORS coverage. |
| Partial search/global existence | 77-87 | PASS scoped. The partial interface only reveals values after completed calls and does not condition on success. No global canonical-vector existence event is needed for the hidden event. Optional all-key densities/counts and conservative exponents were independently checked by exact integer computation. |

The sentence “A known suffix/leaf query ... is answered consistently” at line 55 should be read as consistency with the retained ideal table and, before the first charged hit, with the reference graph. After a charged conflict the retained table can disagree with the graph; line 33 explicitly permits that. I do not require an edit because this qualification is already stated.

## Exact independent controls

Command: `python -I -B control.py`, run from this owned directory; exit code 0. It makes no real signature, key generation, cache, timing, source modification, or upload.

- Leaf ordinary-function-first and ghost-first full joint distributions agree across 32 equally weighted worlds per arrangement.
- Two addressed chain restrictions agree across 512 equally weighted worlds per arrangement; this checks the intermediate coordinate dependency as well as the endpoint advice.
- Invalid survival uniformity: in the two-point REAL model, a second guess after conditioning on a first non-hit succeeds with probability 1, not 1/2. The author explicitly excludes this argument.
- In 128 continued-ideal reveal worlds, the remaining prefix guess is 1/2 in every public-history group; two adaptive guesses have union probability 3/4 <= 1. All 128 old replies remain unchanged, all 64 no-prior-hit installs match the designated image, and all 48 conflicting prior-hit replies are retained.
- Invalid silent reprogramming visibly changes an old reply with probability 3/8 in the tiny model.
- Invalid hidden-driven suffix choice leaks the entire one-bit predecessor while preserving a two-digit target sum of 3: guess success 1 instead of 1/2. Thus constant sum by itself is insufficient.
- Invalid omission of suffix closure makes a supposedly hidden successor computable with probability 1 from a known predecessor. The author's suffix closure excludes this case.
- Exact convolution independently confirms lower/top sum-slice cardinalities, 2,269,957,324,800 lower keys and 2,097,152 top keys, both densities >= 1/1024, and optional all-key/top-only exhaustion upper bounds 2^(-4194262) and 2^(-4194283).

## Accepted statement and remaining boundary

For the fixed nonzero-seed classical joint F/J ideal game, with predictable atomic exposure and a deterministic adversarial full public-O call cap Q_public,

    Pr[first coordinate-specific hidden-input event]
      <= min(1, (Q_public + 3017) / 2^128).

The bound is proved in the unflagged input-oblivious comparison execution and transfers to the source-programmed reference experiment by agreement until the first event. B in the author's general union statement must be a deterministic call cap, not an expected class count. Private honest graph evaluations do not constitute public candidate guesses; their secret inputs are not disclosed. This hybrid's public table and private graph evaluation are deliberately distinct after a charged event, so it must not be described as an ordinary single public RO on every bad continuation.

The smallest remaining composition obligation is to project this coupling back to the unaugmented joint F/J game and combine it with separately proved public-graph collision, WOTS certification, routing coverage, and real-to-joint-ideal losses. Granting full hidden payload graph advice to the common adversary would invalidate this lemma. Separate component bounds can use different harmless enlarged views before projecting to the common original game; that does not authorize merging all those advice views into one hidden-value experiment.

Efficient simulation, successful-setup conditioning, actual SHA-256, a complete source refinement, and QROM hidden-value protection remain outside this review. No total-security number or general category claim is established here.

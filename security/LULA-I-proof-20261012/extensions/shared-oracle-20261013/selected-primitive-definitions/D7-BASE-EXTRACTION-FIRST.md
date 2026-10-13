# Counter-insensitive child descent and the changed-child D7 event

**PROVED — pointwise model lemma, manual proof.** This is an event-classification refinement for the existing finite RO/QROM source model. It does not change the source, any scalar bound, or any primitive challenge assumption. Its proof uses only final classical verification. No signature or implementation attack is constructed.

## 1. Fixed premises and events

Release source SHA-256: `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Signatures are parsed by the actual verifier, and acceptance includes equality of its final returned root with the genuine public root. `Some(root)` by itself is not acceptance.

Work with the deterministic reference signer and honest consistent caches. Across all oracle requests/restored branches, a WOTS address A has one fixed genuine child C_A and one first-accepted canonical counter c_A. Every honest signature at A therefore has the same digit vector x_A. Cache faults that cause the signing oracle to accept noncanonical counters are outside this premise. Abort/noncompletion paths are nonwinning, without normalizing on completion.

Let G_final be the event that a final verifier query at a type-0…4 address uses a payload different from its designated genuine payload but returns its designated genuine node image. Let H_final be the event that a final verifier query uses a genuine nonterminal chain input or genuine FORS secret not in the honest exposure/forward-closure set. This is an event about final inputs, not a statement that the adversary cannot know them and not a measured quantum-query-history event.

Define

`D7_base := exists a reached WOTS address A: V*_A != C_A and digest_A(V*_A,c*_A) = digest_A(C_A,c_A)`.

The starred V is the child value actually computed from the preceding portion of the forged signature, immediately before that WOTS digest is checked. There are at most five reached addresses. Digits use all 128 digest bits for the fixed widths 4 and 8, so equality of their complete vectors is equality of these digest values.

## 2. Local addressed-path lemma

**PROVED.** Suppose an addressed path produced by the final verifier equals a genuine subtree root. In the absence of G_final, its reached leaf public key equals the genuine leaf public key at the routed leaf address.

Proof: compare at the root. The actual final hash equals the designated root image. If its ordered child-pair input differed from the designated ordered pair, that very query would witness G_final. Therefore the ordered pair is identical. Its selected child must equal the corresponding genuine child. Repeat for the path's next parent, preserving the left/right order specified by the routed leaf bits. This finite descent reaches equality of the leaf public key. A depth-zero path starts with that equality directly. Authentication siblings may be arbitrary adversarial bytes; the argument makes no prior assumption about them.

The WOTS leaf is an addressed compression of an ordered endpoint vector. Once its public key equals the genuine public key, absence of G_final at type 1 forces every endpoint in that vector to equal the corresponding genuine endpoint. This applies even when the forged starting chain value differs from its genuine value.

## 3. Local chain lemma and equal sums

**PROVED.** If a reached forged chain finishes at the genuine endpoint and G_final does not occur, its starting value at position y is the genuine value at position y.

Proof: if the starting value differs, the two chains finish equal. Choose the first transition after which they coincide. That transition has different input from the designated genuine input and equal designated output at that exact type-0 address, witnessing G_final. If y=w-1 there is no transition and endpoint equality itself establishes starting equality.

**PROVED.** For an honestly exposed WOTS address A, absence of H_final then requires `y_i >= x_A,i` in every coordinate. If `y_i < x_A,i`, the starting genuine value is outside the honest forward-closure. Since `y_i <= w-2`, verification evaluates that genuine nonterminal value at the corresponding chain address, witnessing H_final. Each honest exposure at A has the same x_A; previous restored branches add no different vector under the fixed premises.

Both digit vectors satisfy the same fixed target sum S. Summing `y_i >= x_A,i` and using equal sums yields `y=x_A`. Hence their full digests are equal.

**PROVED.** An unexposed WOTS address cannot verify in the absence of G_final and H_final. Endpoint equality and the local chain lemma would force every nonterminal starting value to be genuine and unexposed. To avoid H_final all positions would have to be terminal, `y_i=w-1`; their sum would be `l*(w-1)`, strictly greater than S. The fixed instances satisfy 240<32*15 and 2040<16*255. This contradicts the actual digit-acceptance check. Thus every reached WOTS address in an accepting no-G/no-H signature has an honest canonical vector against which comparison is legitimate.

## 4. Counter-insensitive descent

**PROVED.** At a reached exposed WOTS address, after equal digits have been established, exactly the following distinction is needed:

- If `V*_A != C_A`, digest equality supplies D7_base with the genuinely different base child.
- If `V*_A = C_A`, the computed child is already the genuine child. Descend into that child. It is immaterial whether `c*_A=c_A`: the purpose of this step is child equality, and it has already been established.

In particular, a counter-only digest collision is unnecessary to the next induction step. This proof does not assert byte-identical signatures for arbitrary noncanonical counters, nor that a counter-only modification is forbidden by verification. It only asserts that such a modification cannot invalidate the equality needed for child descent.

## 5. Full final-verifier classification

**PROVED.** With C_cov denoting coverage of the 17 real FORS leaf indices in the routed instance by honest signatures, the accepting fresh-message event is covered pointwise by

`Win subset C_cov union H_final union G_final union D7_base`.

Start at the final public root. Apply the addressed-path lemma to layer 4; apply compression and chain lemmas; either obtain G_final/H_final, or equal digits. At equal digits obtain D7_base if the child differs; otherwise descend to that genuine layer-3 subtree root, without testing counter equality. Repeat down layers 3,2,1,0. Source routing ensures the child subtree index matches the next lower layer's routed tree; the immutable genuine child rule is independent of the chosen counters.

At the layer-0 child, the computed FORS public key equals the genuine one. Absence of G_final at its type-4 root compression forces all 17 ordered real FORS roots to equal their genuine roots. For each root, the addressed-path lemma forces the reached leaf image to equal the genuine leaf image at its chosen index. At the type-3 leaf hash, absence of G_final forces the supplied secret to equal the genuine secret. If this secret was not honestly exposed, that final evaluation is H_final. Otherwise its index lies in the honest exposure set for that real FORS tree. All 17 indices therefore satisfy C_cov. The actual outer counter/filter still has to pass the forced-eighteenth-index-zero verification check; this proof neither invents an eighteenth secret nor discards that check.

Freshness is used in defining Win and the existing C_cov source bridge. Freshness of the outer message is not used to assume every internal child is different; the descent explicitly handles equal internal children. The proof is pointwise in the final classical signature/verifier trace, so a quantum adversary's coherent internal queries do not require measurement or query-history extraction.

## 6. Extraction program sketch

**PROVED (manual finite program specification).** The mathematical extractor receives the genuine graph and honest canonical/exposure bookkeeping internally; these are not provided to the EUF adversary.

1. Run the ordinary final verifier on the returned classical signature and message. If it fails, return no witness. Retain its ordered classical trace and compare the returned root with the public root.
2. Compare the reached top path and WOTS compression against genuine designated values. Return G_final at the first divergent-input/equal-output transition, if any.
3. For each chain, compare against its designated trajectory and honest exposure closure. Return G_final at a first merger or H_final at a genuine hidden nonterminal input, if any.
4. The no-witness remainder has equal accepted digit vectors. If the child differs, return `(A,C_A,c_A,V*_A,c*_A)` as the changed-base D7 witness. If the child is equal, descend without a counter-equality test.
5. Repeat through the five WOTS layers; then inspect all 17 FORS components, returning G_final/H_final or the covered-index certificate.

This program certifies the event-cover implication and specifies witness fields. It is not an efficient public simulator, a complete standard-model primitive adversary, or a source/Rust refinement. Any selected challenge adapter still has to supply the corresponding genuine records legally and account for time/query work.

## 7. Consequence and remaining challenge boundary

**PROVED.** `D7_base subset D7_full`, so every previously accepted scalar bound for D7_full remains conservative without any numeric change. This refined extraction eliminates the counter-only interface mismatch identified in the independent definition audit.

**CITED / OPEN.** The changed-base condition matches [2022/778 Definition C.1](https://eprint.iacr.org/2022/778), visually checked on printed page 30. It does not, by itself, match all other aspects of that challenger: stage chronology, hidden common parameter, side-oracle access, finite first-accepted counter search and unconditioned setup still need a lawful reduction. No standard S-TCR reduction or security-category claim follows from the pointwise refinement alone.

**OPEN (formal check).** This is a manually derived source-model induction, not a Lean/EasyCrypt checked theorem. A checker would need precisely the canonical-child routing relation, addressed path-merger lemma, exposure-closure chain lemma, and actual verifier decomposition above. No new axiom or admission is used to label it machine checked.

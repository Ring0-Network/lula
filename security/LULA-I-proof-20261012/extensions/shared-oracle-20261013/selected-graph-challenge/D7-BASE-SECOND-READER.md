# Independent second reading of counter-insensitive child descent

**PROVED — manual model review accepted with the corrected exposed-row definition.** Subject `selected-primitive-definitions/D7-BASE-EXTRACTION.md` SHA `bf9af934dc0c16b96e28dedcafb71cfc6590dc17f826ada2562d99f71eaf9776`. Its first draft `D7-BASE-EXTRACTION-FIRST.md` SHA `8b39805bea96f5c10a5d4e689355544cc1b82d3265121d60cca0733a16095c6d` remains preserved. No machine-checked or cryptanalytic claim is made by this review.

## Source and independent reasoning

Before reading the candidate I had inspected the pinned source's WOTS chain/PK rules, FORS graph, `Signer::sign` and `verify_root` for the graph challenge. I independently reasoned through the local counter issue: equal child value itself suffices for the next root descent, so equality of the canonical and transmitted counters is not needed. I then read the entire saved first draft and checked the final successor against that subject. The source pin remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

The source verifier hashes the currently reconstructed child and transmitted counter to determine its full digit vector, performs actual target-sum acceptance, completes ordered chains, compresses endpoints, and reconstructs the routed parent root. The hash-domain path lemma and first-merger argument therefore apply exactly to those final queries. Every endpoint equality either exposes a same-address alternative-input target hit or forces the supplied starts to be genuine at the indicated positions. This argument covers terminal positions separately, where no chain query exists.

For an exposed address, a digit below its single canonical coordinate uses a genuine nonterminal input outside that coordinate's forward suffix; absence of H_final requires componentwise larger/equal digits. Their fixed equal sums force identical complete vectors. For an unexposed address, accepting target sums240 and2040 are strictly below full-terminal sums480 and4080, forcing at least one genuine hidden nonterminal call. No unexposed canonical counter is needed for this latter argument.

Equal full vectors mean equal full128-bit type7 digests because z=0 and the source's widths4 and8 exhaust128 bits. If the reconstructed child differs from the fixed canonical child, the digest equality is the changed-base D7 witness. If it equals that child, descent to the next lower genuine subtree/FORS root already follows, even when the transmitted counter differs. Counter-only digest collisions consequently need not be charged in this event cover.

The accepted corrected D7_base definition restricts witnesses to honestly exposed addresses with successful canonical rows. I requested this repair: the first draft's all-reached-address wording did not literally imply the existing exposed-row D7_full event, and a canonical counter need not exist at an unexposed exhausted latent row. The proof already forces exposure outside G_final/H_final before using D7_base, so this repair changes neither the induction nor its scalar consequence. Exposure is explicitly coordinate-indexed rather than an unlabelled set of equal node bytes.

## Accepted consequence and limits

The corrected manual source-model statement

`Win subset C_cov union H_final union G_final union D7_base`

is valid under the existing reference/honest-cache/partial-source premises. The refined event is a literal subset of the accepted exposed-row D7_full event, so prior conservative classical and quantum scalar bounds remain valid without any numerical change. The FORS conclusion uses only17 real exposed secrets plus the actual omitted-coordinate zero filter; it invents no eighteenth secret.

The pointwise result does not need a measured coherent oracle history, so it applies to a quantum adversary that eventually emits a classical signature. The manual proof is not a Lean/EasyCrypt source refinement, not a conventional S-TCR challenger embedding, and not an actual implementation attack. Counter-extraction chronology, common public parameter and challenger side-interface equivalence remain independent open obligations. No source or manuscript file was edited by this reader.

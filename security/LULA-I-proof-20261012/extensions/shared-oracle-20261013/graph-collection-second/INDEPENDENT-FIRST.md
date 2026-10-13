# Independent first derivation: fixed public h and genuine graph collection-TCR

COMPUTED: This file was written before reading the new first-agent proposal, restricted-row-third-review/fixed-h-graph-identification, or any new graph proposal. The only old extension documents read were CHANGED-CHILD-EXTRACTION.md and SELECTED-GRAPH-REDUCTION.md, solely to identify the old final witness and its source-tag/raw-header ambiguity; no ordinary fixed-h conclusion is imported from them.

COMPUTED: Release lib.rs SHA256 is ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. HK22 cached PDF SHA256 is 80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abbeb3fabdd6d40d4ffe3c3; text SHA256 is be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561. Primary source was read directly. The release driver parameter line 9 was independently checked, without executing it.

## 1. Precisely scoped conclusion

PROVED (manual finite reduction, under the following model assumptions): An ordinary one-target HK22 Definition 7 collection-SM-TCR reduction exists for each fixed payload length, when h is ONE fixed publicly evaluable full-256-bit function and the addressed family is defined literally from it. No independent selected-row oracle, programmed full-h restriction, or missing-row release is required. This is a reduction identity/inequality; it supplies no hardness estimate for h or SHA-256.

ASSUMED: h:{0,1}* -> {0,1}^256 is fixed and publicly evaluable, including reversibly for the source adversary's finite-register quantum access. Its exact description/evaluation resources are available to the reduction. Ideal F maps valid private ADRS22 labels to Node16; ideal J maps complete message byte strings to Node16. Both are persistent, independent lazy random functions, private to the source simulator; A has no direct F/J secret oracle. All restored source states are honest immutable consistent snapshots, and source requests are classical atomic calls. S is sampled uniformly from {0,1}^128 independently of F,J,A and all source coins. This is the ideal-F/J hybrid, not the unmodified source's real PRF security claim.

ASSUMED: The bounded partial cryptographic interpretation of the source counter loops makes a failed actual search absorbing/nonwinning after at most L=2^32 attempts. Native overflow, allocation, scheduling and instrumentation are outside this interpretation. No conditional normalization on setup/signing completion is allowed.

OPEN: A full quantitative security assertion, a growing-parameter PPT claim, a real-source PRF bridge, and an opaque external full-h RO/QROM identification remain separate obligations. The fixed-h program below is not permission to supply a new side oracle in the latter model.

## 2. Exact family and primary game obligations

CITED: HK22 printed pp.4-6, Definition 2 (cached text lines177-187) samples P before A1, gives A1 classical target queries (T_i,M_i), reveals P only to A2, demands distinct target tweaks and M' != M_j with equal outputs. Definition 3 (188-196) instead samples hidden uniform inputs and has no inequality requirement. Definition 7 (241-270, especially267-268) gives A1 a classical collection oracle at the hidden common P, with challenge-tweak set disjoint from ALL collection-query tweaks, regardless of message length. HK22 explicitly introduces the collection to allow payload dependence on earlier function outputs, even of the same function at different tweaks.

PROVED: Define for every relevant byte length l,

    Th_(8l)(P,a,x) = prefix128(h(P || zero48 || a || x)),
    P in {0,1}^128, a in {0,1}^176, x in {0,1}^(8l).

The family is a single fixed public-h collection with common P. The seed-prefixed addressed raw input has length86+l bytes. The source's Ctx::new/th implements precisely the SHA-256 specialization: one unpadded 64-byte P||zero48 prefix block followed by ADRS22||payload and ordinary SHA padding, with the total length included (lib.rs109-147). For fixed P, the 22-byte address boundary and payload boundary are unambiguous. Variable lengths identify collection members; length is not appended as an invented domain-separation tag.

PROVED: ADRS22 is layer byte [0], big-endian tree64 [1..9], type byte [9], big-endian keypair32 [10..14], chain/height32 [14..18], hash/index32 [18..22] (69-95). At the fixed release parameters all used layer values fit the source's u8 cast and valid fields are injective; no generic unbounded-parameter injectivity is claimed.

PROVED: Genuine type0 payloads are one16-byte chain node; type1 is the ordered endpoint concatenation, 512 bytes at layers0..3 and256 bytes at layer4; type2 is an ordered32-byte child pair; type3 is16 bytes at FORS leaves and32 bytes at positive heights; type4 is the ordered17-root concatenation of272 bytes. These follow from239-277,291-307,344-412 and driver line9: k18,a9,FORS+C, heights(5,5,5,5,21), WOTS widths(4,4,4,4,8), z0. Collection bit lengths are128,256,4096,2048,2176 respectively. Counter type7 is20 bytes and not a graph challenge here.

## 3. Why genuine target preparation is legal

PROVED: For every fixed graph address d, its genuine payload X_d is computed from private F starts and strict public predecessors, without computing Th(P,d,anything). A type0 target at position p uses the F-labelled start and earlier positions0..p-1, all with different w3. Type1 uses type0 endpoints. Type2 uses leaf type1 images and nodes at lower heights. A type3 leaf uses its type6 F-labelled start; an internal type3 uses lower-height children with source global indices. Type4 uses type3 roots. These dependencies are acyclic and source-address injectivity separates d from every public predecessor. No canonical type7 counter, public root, signature, public graph advice, or hidden-row-success assumption is needed to determine X_d.

PROVED: Preparation calls the HK22 collection oracle only at these strict predecessor addresses. It never calls it at d at ANY length, including a length different from |X_d|. It may re-use previous responses at other addresses. Since genuine predecessor nodes are128 bits, the collection oracle's128-bit outputs are sufficient: no secret full256 suffix completion or guessed suffix is necessary. F,J are sampled privately with their same persistent law; J is not needed in the cone.

PROVED: X_d depends on P through predecessor images. This is permitted adaptive dependence in Definition7, not an independence assumption. The payload is not replaced by a random independent vector or externally advised genuine graph. The challenger still keeps P hidden during all of this preparation.

## 4. Exact program, selectors and continuation

PROVED: Fix a payload-length class V_l of all valid genuine type0..4 addresses with payload length l. Let N_l=|V_l| and b_l=ceil(log2 N_l). The two-stage reduction B_l is:

1. B_l,1 samples b_l bits r. If r>=N_l, it makes no challenge query and returns a dummy flag. Otherwise it un-ranks d from a fixed public ordering of V_l, samples/private-memoizes F as needed, and computes X_d via only the legal collection predecessor queries above. It sends its SINGLE classical challenge (d,X_d), receives the128-bit image, and saves d,X_d,F state, source-independent coins and selector state. It does not run source A or reveal the seed. Target count p=1, hence target DISTINCT is immediate.
2. B_l,2 receives P. A dummy selector returns failure. On a valid selector, it now runs A from its original pre-key initial state with its original coins and full quantum/classical public h interface. B knows P but does not give P or any setup graph information to A until the actual source setup API returns it. A's raw public h interface is the SAME fixed h; its inputs are evaluated with their exact full256 results. No router, row overwrite, truncated/full256 completion or A-state restart is used.
3. Only when A requests source setup, execute the actual source setup and counter searches with S=P and the persisted independent F/J functions. Give precisely the pk and authorized logical cache payload produced by source setup. Run actual subsequent source calls, restores and signature generation with persistent Seen/exposure state and exact source freshness. Failures remain absorbing/nonwinning. A's pre-key raw h queries, including superpositions and direct guesses at the eventual target plane, occur in B2, after the primitive key reveal; they are part of A's preserved source pre-key continuation, not forbidden B1 collection queries.
4. Run the actual final classical verifier; acceptance requires equality to the actual pk.root, not merely Some(root). Save its actual reached addressed type0..4 records in chronological order. Compute the genuine routed graph after A using the same h,P,F, and choose the FIRST differing-payload/equal-prefix128-output witness, before testing the selector or length. If source Win holds and this first witness has length l and address d, output its complete actual payload X'; otherwise fail. Equality X'=X_d is explicitly rejected.

PROVED: For fixed h and F,J coins, the hidden preparation is merely evaluation of the same genuine DAG, with no change to h. Even if h has pathological collisions, the DAG is defined by exact source coordinates and deterministic payload values. A's entire source view, including public full256 raw queries and quantum continuation, is identical for every valid selector. Source setup may reuse private predecessor computations but exposes no extra values. There is no runtime/microtiming secrecy claim: this is the mathematical source interface.

PROVED: A may learn genuine intermediate nodes from authorized cache exposure; this changes its strategy and final witness but not reduction legality or the selector independence. Final classical extraction measures no coherent query history.

## 5. Exact identities and event boundaries

PROVED: Let G_addr be the existence of a genuine SOURCE-ADDRESSED type0..4 record in the final classical verifier whose actual payload differs from that coordinate's genuine X and whose128-bit output equals the genuine image. Let E_l be source Win AND G_addr AND the first such witness has payload length l. With dummy branches retained,

    Pr[B_l wins] = 2^(-b_l) Pr[E_l].
    Pr[Win AND G_addr] = sum_l 2^(b_l) Pr[B_l wins]
                         <= sum_l 2^(b_l) InSec_collection-SM-TCR(Th_(8l);resources_l,p=1).

This identity is unconditional in source seed and completion, and holds for quantum A with final classical output. It uses only inequality of PAYLOADS at the same complete address, not different addresses, messages, counters or raw-h words at distinct contexts.

PROVED: If the old G_final is defined by arbitrary raw header matching rather than actual source-addressed call provenance, nonzero S makes every final verifier type0..4 matching header a routed graph call. The inner word R||S||root||m cannot equal S||zero48||ADRS22||x, because its second16 bytes would require S=0; the outer word is only52 bytes. At S=0, inner aliases at off-route graph addresses can occur. To preserve that old broader event without redefining it, B2 additionally aborts on P=0, giving

    Pr[B_l^nz wins] = 2^(-b_l) Pr[E_l AND S!=0],
    Pr[Win AND G_raw] <= 2^(-128) + sum_l 2^(b_l) Pr[B_l^nz wins]
                     <= 2^(-128) + sum_l 2^(b_l) InSec_collection-SM-TCR(Th_(8l);resources_l,p=1).

The all-seed ordinary HK22 game is retained; no hidden-key rejection/resampling is introduced. Alternatively, a primitive with parameter space explicitly restricted to nonzero seeds yields the conditional identities. A full composition pays the seed-zero branch once globally. This file does not silently replace old G_raw by G_addr.

PROVED: A final query with X'=X_d and equal output is NOT a TCR win, even if its input was previously hidden. Hidden-input recovery belongs to a PRE-type event. HK22 Definition3 specifically requires challenger-sampled uniformly random hidden payloads; genuine chain interiors and concatenated graph payloads are generally dependent/nonuniform, so only specially justified private-start cases can directly match that PRE game. No whole-graph PRE reduction is asserted here.

## 6. Computed class sizes and conservative resources

COMPUTED (integer arithmetic only): Let K_i=2^(41-sum_(j<i) h_j) be the count of layer-i WOTS keys and T_i=K_i/2^(h_i) its subtrees. The independent sums are:

| bytes l | N_l | b_l | contributing graph calls |
|---|---:|---:|---|
|16|20,229,886,488,608,768|55|sum_i K_i*l_i*(w_i-1) + 2^41*17*512|
|32|19,105,114,044,235,775|55|sum_i T_i*(2^(h_i)-1) + 2^41*17*511|
|512|2,269,957,324,800|42|K_0+K_1+K_2+K_3|
|256|2,097,152|21|K_4|
|272|2,199,023,255,552|41|2^41|

COMPUTED: Total D=39,339,469,515,522,047. These are selector counts, not hardness or capacity estimates. Each B_l has one fixed family member length; a selector choosing a variable member is not silently called a single fixed-m HK22 game.

COMPUTED: Conservative maximum predecessor cone public queries P_cone=2^21*(16*255+1)+(2^21-2)=8,560,574,462 and F entries V_cone=2^21*16=33,554,432, achieved by a type2 top root. Collection queries exclude its final root address. Length-specific cones can be much smaller; using this maximum for all five reductions is conservative.

COMPUTED: Complete post-A routed extraction costs at most P_ext=8,560,653,547 public addressed h evaluations and V_ext=33,567,232 F entries: one top subtree W_top=8,560,574,463, four lower subtrees of15,423 calls each, one17-tree FORS instance17,392. Only the reached five subtrees and routed FORS instance are needed, not the 2^41 entire forest. Genuine graph extraction has no counter search. The final verifier type0..4 count is at most3217: WOTS chain suffixes 4*(480-240)+(4080-2040)=3000, five compressors,41 Merkle nodes,170 FORS path/leaf nodes and one roots compressor. Add five type7 calls and two message-hash calls for total3224.

COMPUTED: With L=2^32, source top-prepared setup public-h cap is H_setup=2^21*(19505+L)-1 and F-distinct cap U_setup=2^21*(16+32*32)=2,181,038,080. A cold initiated sign uses at most H_cold=W_top+82090+6L public calls and U_cold=33,567,232 distinct F labels; hot uses H_hot=82090+5L and U_hot=12,816. J is charged once per requested complete message, memoized consistently; actual noncompleting prefixes satisfy the same caps. These count mathematical h calls, not SHA compressions, runtime or observed execution.

PROVED: For q initiated source sign calls and Q_h adversarial public full-h queries, a conservative total logical-h-equivalent work cap is

    P_cone + 1 challenge + H_setup + q*H_mode + Q_h + 3224 + P_ext.

The B1 collection oracle is used at most P_cone times; B1 target count is1. B2 public h evaluations are charged by actual full-input byte lengths and h's public evaluation cost. No h oracle query is free merely because the function is public. Total private F entries are bounded by V_cone+U_setup+q*U_mode+V_ext; overlaps can only decrease this deliberately double-counted cap. A's complete messages and finite quantum input-register lengths must also be included in time/space resources. Quantum h evaluation uses the supplied actual circuit cost; no hidden quantum transcript is stored. Streaming chains and subtree arrays avoid retaining billions of chain transitions; a largest16*(2^22-1)=67,108,848-byte node array suffices for one top tree, in addition to source cache/work arrays and F/J/A state. Source keygen itself has additional item/counter arrays. This is a finite manual resource specification, not a benchmark or a claim of practical/PPT reduction efficiency.

## 7. Controls and smallest remaining lemma

PROVED: The positive control is selecting the coordinate of the canonical first genuine witness: the exact saved X_d is its target, the actual X' is unequal and hashes to the saved image under the SAME fixed h. A nonselected address, wrong payload length, equal genuine payload, failed actual source setup/sign, malformed or nonfresh final pair, or dummy selector returns failure. An illegal preparation query at d at ANY length invalidates the reduction rather than creating a new oracle. A modified h inconsistent with preparation is rejected as another model. F/J label persistence is mandatory across preparation and source continuation. Every control follows directly from the specified predicates/program; no signature attack was generated or executed.

OPEN: A machine-checked source refinement would mechanize the acyclic cone/address exclusion, exact source/full-h evaluation equality, preserved source continuation and canonical final-witness selector. For ONE fixed public h, no extra missing-row primitive lemma is needed for this manual game reduction. For a different model with only opaque external fullh RO access, the smallest missing lemma is legal SAME full256 oracle access/implementation in the HK22 challenge environment, preserving pre-key quantum source queries and correlations while P is hidden, with an explicit resource budget. Def7's128-bit collection interface alone is not that lemma. No appendix RO bound is transplanted and no numerical SHA-256 hardness conclusion is made.

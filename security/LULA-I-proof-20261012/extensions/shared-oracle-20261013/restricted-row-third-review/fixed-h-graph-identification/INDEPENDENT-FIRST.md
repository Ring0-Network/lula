# Source-first fixed-public-hash graph identification

**PROVED (manual conditional reduction) / CITED (primitive definition) / ASSUMED (hardness).** Saved before reading any NEW other-agent graph-identification proposal. This reader has read the already accepted selected-graph and changed-child reductions, the release source and the primary HK definitions. This is a new conventional-interface identification, not a blind rederivation of those previously accepted source witnesses. Existing artifacts, source, manuscript and scalar calculators remain unchanged.

## 1. Actual public function and target primitive

**ASSUMED (model definition).** Fix one public deterministic full256-bit algorithm h on byte strings, including its public circuit description. For any literal payload length m define

`Th_m^h(S,A,X)=prefix128(h(S16||zero48||A22||X)), |X|=m bits`.

Use the SAME h everywhere, including its complete32-byte reply to unaddressed full-hash computation. Model HJ[h] uses independent ideal private F/J; it is distinct from HJ[O]. No independent row resampling, RO numerical bound or SHA-256 hardness follows from this definition. Quantum source adversaries can evaluate the public h algorithm locally; those evaluations, ordinary source work and simulation overhead belong in the primitive adversary's time/gate budget. An external opaque Raw oracle with a separate law is not silently added.

**CITED.** HK22, https://eprint.iacr.org/2022/346, Definition2 defines SM-TCR for an n-bit output with distinct target tweaks; a first-stage adversary chooses target messages via classical hidden-parameter Th queries, then receives the public parameter and produces a DIFFERENT message at a registered tweak with equal output. Definition7 additionally permits classical collection queries before public-parameter release at tweaks disjoint from ALL challenge tweaks, including other message-length members. It expressly supports dependencies on other functions/tweaks. It does not require the target to be independent of the public parameter. It does not permit a preparatory query at the registered tweak merely because that query uses another input length. The cited PDF/text pins appear in the receipt.

The present source-shaped public graph needs members m in `{128,256,2048,2176,4096}` bits. They correspond to16-byte chain/FORS leaves,32-byte ordered node pairs,256-byte top WOTS endpoint vectors,272-byte17-root FORS vectors and512-byte lower WOTS endpoint vectors. Source final G witnesses have the same length as their genuine targets. The unrestricted adversarial-Raw G superevent can include other lengths; this reduction identifies G_final only. Hash equality is128-bit prefix equality, not full256 collision resistance.

## 2. Genuine target payload before public seed release

**PROVED (source reading).** For a selected valid type0--4 address d, its genuine payload X_d can be built by independent F and strict-predecessor collection calls, none at d:

* Type0 WOTS transition at position r: take its ideal F start and evaluate preceding positions0,...,r-1 at different w3 tweaks. X_d is the current16-byte value. Position0 needs no collection call.
* Type1 WOTS compressor: build the ordered endpoint vector using type0 chain tweaks and independent F starts; all type0 tweaks differ from selected type1.
* Type2 Merkle node: build both designated child nodes through strictly lower-height tree tweaks and WOTS leaves. The selected parent address never appears among those strict predecessors.
* Type3 FORS leaf at height0: X_d is one independent F-derived secret; its private label is type6 and not a public collection query. For a type3 internal node, build its ordered child pair at lower-height/different-index type3 tweaks.
* Type4 FORS roots compressor: build all17 real roots at type3 tweaks and concatenate them in source order.

These address exclusions are across the entire collection, not just within one member. They follow the literal22-byte address (type at offset9, height/chain at14..17, index/position at18..21) and acyclic source dependency. The largest cone is the selected height21 type2 root:8,560,574,462 public collection calls and33,554,432 ideal F starts. No type7 grind or canonical-counter success is needed in this cone. The private outputs are sampled by labelled maps, preserving subsequent source reuse.

**PROVED.** The reduction does not need S to perform this preparation: each public hash call is made through the hidden-S collection oracle, supplying its known predecessor payload. Hence the former objection "predecessor hashes need the hidden common seed" prevents standalone Definition2 preparation, but does NOT prevent Definition7 collection preparation. No challenge key is sampled early or exposed illegally. After computing X_d, submit exactly one target challenge at (d,X_d). The response is its128-bit image Y. Only then receive S. Full target-image retrieval, if needed, uses the now public h on the literal word; its extra work is charged and uses the same deterministic algorithm, with no programmed image.

## 3. Exact ordinary collection-TCR adversary

**PROVED (program sketch).** To avoid silently changing a fixed-length primitive into an unformalized joined challenge, define one adversary B_m for EACH of the five lengths. A joined-member notation is possible under HK's stated convention, but the separate-member formulation below needs no new convention.

1. Before learning S, sample exactly56 selector bits j. Use the accepted deterministic unranking of D=39,339,469,515,522,047 graph addresses. If j is dummy or selects a length other than m, take a nonwinning branch; if the primitive syntax demands exactly one target query, register any fixed m-bit message at a fixed valid tweak and return failure after release. Do not run source A on that branch.
2. For a valid selected d with length m, sample independent labelled private F/J and compute X_d through strict-predecessor collection queries at tweaks other than d. Submit the ordinary challenge query (d,X_d), recording Y=Th_m^h(S,d,X_d). There is only one challenge tweak, so target DISTINCT holds; the preparatory collection/challenge tweak intersection is empty.
3. Upon receiving S, fail locally if S=0 for consistency with the original nonzero-seed component. Otherwise run A's complete source pre-key phase with S/pk withheld. The public h implementation is available as it is in the source experiment. Run ordinary source setup, honest/genuine-cache signing and final verification using this same h and the same F/J maps. Only release pk/logical public cache after ordinary successful setup. Preserve source absorbing noncompletion; do not abort for unrequested failed rows.
4. After A returns its classical candidate, run the actual final verifier, retain its source-shaped graph trace and compare its root with the public root. Rebuild the five routed subtrees and real FORS instance using the SAME h and F maps, exactly as in the accepted localized graph extractor. Find the canonical first final type0--4 query with a payload different from its designated genuine input and equal128-bit output. This first-witness selection is independent of j.
5. Output its changed payload X* to the primitive only if the source Win bit is true, its address equals d and its payload length is m. The ordinary SM-TCR winning predicate then holds: X*!=X_d and Th_m^h(S,d,X*)=Y. Otherwise return failure. No coherent-query history is inspected. This final classical extraction works for a quantum A; its entire internal state and h evaluation semantics are preserved.

**PROVED (source law).** For any valid j, the precomputed cone contains only reduction-private work, using the actual hidden-parameter primitive and fixed h. All later source values are evaluations of the same h and labelled F/J. The private preparation therefore changes no A-visible distribution or function. It can be placed before A's pre-key phase because it depends only on the key's public seed and ideal private maps, not A's output. There is no need to substitute an independent selected hash restriction, condition on source completion, or assume absent adversarial pre-key hits. Public logical cache values are those from the actual source setup, not additional graph advice.

**PROVED (selection).** Let G_final,m mean the canonical first G_final witness has payload length m. With exactly the extraction above,

`Pr[B_m wins] = 2^-56 Pr_HJ[h][Win AND G_final,m AND S!=0]`.

The equality concerns these constructed adversaries and the exact first-witness rule, not optimal primitive/source advantages. Summing disjoint first-witness length classes yields

`Pr_HJ[h][Win AND G_final AND S!=0] <= 2^56 * sum_m Succ_SM-TCR,collection(Th_m^h;B_m,p=1)`.

Each primitive probability already averages its uniform public parameter and B_m's local seed-zero failure. Do not insert an extra eta factor into an assumed unconditional primitive advantage. A complete source union can pay S=0 once externally. One can alternatively use an explicitly defined joined-member primitive for the randomized length selection, but should not relabel a single fixed-m Definition2 game as that joined game without saying so.

## 4. Explicit resources and limitations

**PROVED / COMPUTED.** Each B_m uses one challenge query and at most8,560,574,462 pre-release collection queries, all at other tweaks. Private target preparation uses at most33,554,432 F labels. Its routed extraction uses at most8,560,653,547 public h evaluations and33,567,232 distinct F labels. Source setup/signing caps H_setup,qH_mode and final3224 remain separate; primitive local h work additionally includes t_A's actual computation and at most one full target retrieval. A conservative public-work cap is

`P_cone +1+H_setup+q*H_mode+3224+P_extract`,

plus the actual source-A time/gates and query/message-byte handling. The old ideal external-RO Q count is not itself a fixed-h conventional runtime bound. Source/A state, labelled F/J dictionaries, messages/Seen, logical cache, tree arrays, final trace and prefix/source buffers retain the previously explicit storage envelope. This is finite but enormous at the concrete parameters; no feasible benchmark or PPT-in-height claim follows. Challenged output is128 bits, and conventional hardness must be stated at THESE collection/preprocessing/time resources.

**ASSUMED / OPEN (hardness only).** Identifying the ordinary game does not prove any actual SHA-256 advantage bound. A complete fixed-h theorem may assume collection-TCR of the stated Th_m^h members under their explicit resources. It cannot import the direct HJ[O] numerical graph term, HK's standalone generic formula, or a128-bit label merely from the interface match. HK's collection generic-bound conjecture and the concrete primitive's hardness are distinct from the reduction's legal chronology.

## 5. Hidden-predecessor PRE is a different obligation

**PROVED (predicate distinction).** H_final can be a verifier call whose input is EXACTLY the genuine but unexposed chain predecessor or FORS secret. Such a hit satisfies a preimage predicate; it does NOT produce an input different from the registered target. Ordinary SM-TCR and SPR cannot bound that event merely by renaming it a collision. A successful preimage adversary is allowed to recover the original input itself.

**CITED / OPEN.** HK Definition3 SM-PRE samples a uniform hidden target input; Definition7 supplies only other-tweak collection access in the first phase. Ideal F starts/FORS secrets are uniform128-bit values, but an interior WOTS predecessor is a source-derived chain value under fixed h. It need not be uniform. More importantly, installing the primitive's unknown target as an interior predecessor would require its preceding public h output to contain that unknown value. One cannot program the SAME public fixed h at that preceding input while preserving its public algorithm. Giving the reduction its own sampled predecessor instead changes the primitive chronology/target-input law; revealing an unknown target before source signatures changes source exposure.

The smallest missing interior-PRE lemma is therefore a lawful source-derived-hidden-input PRE/UD transfer preserving fixed-h predecessor/endpoint, private F and later exposure correlations, OR a distinct explicitly named source-generated-target preimage assumption with the actual distribution and resources. The already accepted classical stopped-cut RO construction and coherent-QROM error are not ordinary fixed-h PRE identification: they rely on latent oracle-cell coupling unavailable for a fixed public algorithm. Uniform start/FORS subsets may admit specialized PRE programs, but no claim that they close the entire H_final term is made here.

**Verdict: ORDINARY_COLLECTION_TCR_GRAPH_COMPONENT_IDENTIFIED_CONDITIONALLY; INTERIOR_HIDDEN_PREDECESSOR_PRE_NOT_IDENTIFIED.** No cryptographic level, scalar upgrade, complete-security theorem, new parameter set or operational attack follows. New source/game kernel declarations: zero.

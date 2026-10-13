# Localized selected-target adapter for the final verifier graph event

**PROVED / COMPUTED / OPEN — separate successor.** This document preserves the original eager candidate and narrows its extraction event explicitly to the final classical verifier trace, the actual event used by the accepted final-forgery split. It replaces whole-forest preparation by one selected strict-predecessor cone and one final routed honest graph. It is a finite source-relative addressed-RO challenge program, not an ordinary SHA or single-key SPR/TCR reduction, a practical runtime claim, a source implementation change, or a forgery construction. Source pin and the addressed challenge definition are unchanged.

## 1. Deterministic padded address selection and precommit target computation

**PROVED.** Before A starts, sample exactly56 uniform bits to obtain j in `[0,2^56)`. Fix a deterministic unranking of the full D=39,339,469,515,522,047 valid type0–4 addresses. If j>=D, return the challenge's failure symbol immediately and do not start A. Otherwise set d*=unrank(j). Valid domains each have probability exactly2^-56; there is no rejection-sampling time tail and no claim of uniform distribution conditional on retaining the dummy branch. This successor's unconditional reduction loss is2^56, not D.

Sample the source's three uniform seed components, hiding them and j from A; when binding to HJ, K/P remain unused and F/J are memoized independent full256 maps. The public S is known to the adapter/challenger, but withheld from A's pre-key phase. Acquire the addressed challenge's outside raw function on the complement of `S||zero48||d*||all payloads`. Compute only the strict-predecessor closure necessary for X_d*, following the genuine source rules. Every predecessor address is different from d*. Type5/6 private starts are outside d*, even at S=0. No canonical type7 counter is needed to determine these type0–4 payloads, and no counter search is performed during this preparation.

Commit X_d* before receiving the selected restriction H_d*. Then acquire the full256 target image and install the same exact whole-word router as the eager candidate. All other addresses stay ordinary lazy memoized RO restrictions. Do not compute the selected address's descendants except when actual source setup/signing/final-extraction calls require them. There is no selected-restriction prequery and no overwritten answered point.

**COMPUTED — exact worst cone.** A selected type2 top root, at height21, requires all top WOTS leaf PKs and every lower top Merkle node, excluding its own final root hash. This is the largest cone:

`P_cone = 2^21*(16*255+1) + (2^21-2) = 8,560,574,462`

public full-hash calls and

`V_cone = 2^21*16 = 33,554,432`

private starts. Other type2 cones are smaller; one top type1 compressor has4,080 predecessor transitions, one type0 target has at most254 predecessor transitions and one private start, and the largest whole FORS instance has17,392 public calls and8,704 private starts. These are source-model query counts, not SHA compressions or timings. In HJ the private starts are independent F values; in real-source mode they are additionally raw type5/6 calls.

## 2. Faithful source phases and partiality

**PROVED.** Start A only after commitment and installation. Forward its full pre-key raw interface, preserving the same continuation and total adversarial query cap Q_H across setup and post-key phases. Only after A requests setup, run the normal top-prepared source setup through the router and private adapters. Prepare exactly the source's top cache and its canonical counters. Return pk and, in the logical-payload game, exactly C_top. Initiated atomic signing requests then execute the actual source sign routine, using the requested honest cache mode, restoring only immutable consistent snapshots, and sharing global Seen/message exposure history. Internal computations may reuse previously memoized genuine values; no new graph or seed advice is disclosed. The source's type7 canonical searches are neither eagerly expanded over the entire forest nor subjected to irrelevant exhaustion checks.

Totalize each actual source counter loop to at mostL=2^32 attempted counters, preserving its defined absorbing nonwinning continuation if it has no success. A failed actual setup emits no pk or cache; a failed actual signing call emits no signature. The selected cone never introduces this failure because it has no counter loop. Only counters actually needed by source setup/signing can cause source absorption. Physical panics/allocation/scheduler behavior and native overflow remain outside the partial cryptographic model.

Finally execute the exact public verifier on A's final classical pair, preserving its ordered raw hash trace and comparing the returned root to pk.root. A source noncompletion or malformed/freshness failure cannot yield source Win. No reduction stop is chosen because the challenged domain happens to be encountered.

## 3. Local final-witness extraction without a full forest

**PROVED — event scope.** Let G_final be the existence of a type0–4 query in the final actual classical verification trace with payload different from that address's genuine payload and truncated output equal to its genuine output. This is the witness event used by the accepted pointwise final forgery classification. It excludes arbitrary off-route raw adversarial hits, pre-key raw hits and coherent quantum query support. No inference about the broader ever-query event G is made from the local extractor.

On a completed final verification, store at most3217 selected-type query records in their original chronological order, including full raw words and full256 responses. The route is fixed by the verifier's actual R,c_F and inner/outer outputs. If the verifier stops before obtaining a valid route, it has no type0–4 trace and G_final is false. Once a route exists, determine each `(tree_i,leaf_i)` by the actual `tree_leaf` schedule. Compute the genuine mathematical subtree at each of the five route layers plus the genuine17-tree FORS instance at the route's bottom address. Use the same router, source seeds/F and ordered source tree rules. These computations need no canonical counters or fresh signatures. They are post-A reduction work and are not returned to A.

All final trace type0–4 addresses belong to this routed graph: type0/1 addresses use the selected WOTS key at a route layer; type2 addresses use that layer's Merkle path; type3/4 addresses use the selected FORS instance. Creating complete chains and genuine subtree arrays therefore determines their genuine designated payloads and outputs. The source's single designated payload per address remains unique, even if a forged value selected a different digit or its trace node differs. For a malformed later digest, the earlier trace is still covered by the same complete route; its final absence of Win is treated separately below.

Process the recorded trace in chronological order or compare its records against genuine graph calls as they are streamed. Retain the lowest trace index matching the G_final predicate. This witness rule uses only the ordinary full oracle, the fixed source key/graph and A's final classical trace; it never tests whether its address equals d* until after the witness has been selected. Output the candidate payload iff that first witness exists, its domain equals d*, and (for the `Win AND G_final` contribution) the exact source Win bit is true. Otherwise output the failure symbol.

**COMPUTED — extraction resources.** One top subtree costs

`W_top = 2^21*(16*255+1)+(2^21-1) = 8,560,574,463`.

Each lower height5 subtree costs32*(32*15+1)+31=15,423, and the17-tree height9 FORS instance costs17*(512+511)+1=17,392. Therefore the exact complete routed graph cap is

`P_extract = W_top + 4*15,423 + 17,392 = 8,560,653,547`

public calls, with at most

`V_extract = 2^21*16 + 4*32*32 + 17*512 = 33,567,232`

distinct private starts. Memo overlap with previous cone/setup/sign work may lower these costs, but is not required by the bound. There is no2^41 or full-D extraction multiplier. Materializing all8.56B chain records is unnecessary: generate each chain sequentially, keep its endpoint, compare only against already recorded final trace coordinates, and keep ordinary tree node arrays. The largest top node array is16*(2^22−1)=67,108,848 bytes; the pre-root cone lacks its final16-byte root. F memo storage is separately charged and is not assumed free.

## 4. Exact source marginal and target-selection probability

**PROVED — partial oracle independence.** For each valid selected d*, its X_d* is determined by key coins and strict predecessor/outside restrictions, all independent of the missing own restriction. Installing a fresh independent H_d* therefore produces exactly an ordinary shared full256 O and its actual honest graph. The precomputed cone has no visible output to A. Preparing different cones for different d* changes the reduction's private work, not the source view, and does not condition O on setup completion or overwrite prior A responses. This gives the same ordinary source experiment for every valid j. The final witness computation uses that same function and no incompatible advice extension.

Thus a joint coupling samples an ordinary O, key and A randomness first and independently selects j. For every completed source world with a canonical first G_final witness at address d, exactly one valid j selects d; all other selected addresses and dummy j values fail this particular extraction. Hence

`Pr[B_local wins] = 2^-56 * Pr[source Win AND G_final]`.

If extraction is allowed on any completed final trace without checking Win, the equality instead concerns the completed-trace G_final event. The source full-forgery decomposition uses the displayed conjunction. This identity does not rely on the adversary's address being uniformly distributed and does not give graph advice to A. It is valid with public logical cache payload because that payload is generated by actual source setup using the same oracle and omitted on failure. It is not a replacement for the broader G event's own statistical bound.

## 5. Complete localized resource envelope

**COMPUTED / PROVED.** Put H_setup=2^21*(19,505+L)−1, U_setup=2,181,038,080, H_cold=W_top+82,090+6L, H_hot=82,090+5L, U_cold_distinct=33,567,232 and U_hot_distinct=12,816. These are the frozen source caps for public calls excluding private restrictions; each real-source sign additionally uses one raw message randomizer. The final verifier cap is3224. A deterministic cap on both challenge oracle handles combined, excluding F/J local sampling in HJ, is

`R_HJ <= P_cone + 1 + H_setup + q*H_mode + Q_H + 3224 + P_extract`.

HJ additionally uses at most

`V_cone + U_setup + q*U_mode_distinct + V_extract`

memoized F entries before namespace-capping, and at most q message-label J queries. In the real-source variant add V_cone+U_setup+q*U_mode_invocations+V_extract raw private calls and q raw message-randomizer calls; U_cold_invocations=33,567,393, U_hot_invocations=12,961 are the actual source invocation caps. Distinct F entries can be bounded by the smaller distinct numbers because independent F is memoized. Noncompleting prefixes cannot exceed these caps. This deliberately double-counts cone/extraction overlaps to avoid an unproved reuse assumption.

**PROVED — selected handle refinement on S nonzero.** A conservative selected-handle cap is the total R_HJ or corresponding real-source cap. More sharply, every honest selected graph address is visited at most once during normal setup, at most twice per initiated source sign (subtree/full-tree computation and WOTS prefix signing), at most once in the final verifier and at most once in routed extraction. The cone never queries its own selected restriction; the initial target image uses one call. All honest type7, E52, private type5/6, and (for S nonzero) I/real-message-randomizer words lie outside the selected header. Thus classical selected H_d* invocations are at most

`Q_H + 2q + 4`.

No extra charge is needed merely because the source repeatedly uses an already known private F value; its full function is memoized. On S=0 variable-length message words may overlap the selected plane: use the unrefined total cap or charge the whole S=0 branch once at final composition. The local adapter's exact routing/marginal remain valid on this branch. Do not subtract a seed-zero term from already unconditional game probabilities.

**PROVED — work and memory meaning.** With balanced dictionaries, byte input copying, streaming chains and ordinary node arrays, reduction work is bounded by t_A plus C times its charged public/private/challenge calls multiplied by `(599+log2(total charged calls+2))`, plus the total actual adversarial query/message byte lengths and dictionary membership/copy costs. Selection consumes exactly56 random bits. The graph/source operations already determine digest parsing and loop overhead. Finite input lengths and oracle costs are explicit; nothing is reported as measured time.

Own memory contains A state, at most the bounded private F map and message J/Seen dictionaries, actual top logical cache, one largest67,108,848-byte tree array, the selected target and predecessor-working data, and at most3217 selected verifier records. The latter require at most3217*(598+32) bytes before bookkeeping because a source-shaped selected raw word has at most598 bytes. Each private F entry stores an address22 and full256 value32, plus dictionary overhead. A deliberately generous sequential-source own-data envelope is `54*V_F + M + q*5720 + 75,497,456 + 64*2^22 + 64*17*1023 + 3217*630 + 1024` bytes, excluding A state, dictionary/node headers and message-label pointer arrays. Here V_F is the F-entry cap above and M is total stored requested/final message bytes. The64*2^22 working allowance covers source setup items/leaf/counter vectors and ordinary tree-generation/extraction arrays, rather than retaining every chain transition. Predecessor-cone work arrays can be released after the target payload is saved. Pointer overhead is separately O(V_F+q+3217) fixed-width words in this concrete fixed-address model. Full local public-query memoization is optional and is not included; the challenge handles themselves retain their correlated function. In a byte-level dictionary model, take T=R_total+V_F+q+2 and add `(M+L_A)*(1+log2(T))` byte-comparison/copy work to the preceding call/operation envelope; L_A is total adversarial raw-input bytes. Thus variable-length messages do not silently have unit-cost dictionary comparisons. Challenger oracle memory is not thereby proved inexpensive.

**OPEN — efficiency/certification.** The localized adapter saves the full-D/U forest cost and gives a genuine original-source final-event reduction, but the concrete predecessor/extraction caps still approach8.56B hashes and normal prepared setup can be much larger. A growing-height family has exponential graph work in h, so a PPT-in-security-parameter claim requires a separate parameter/resource comparison and is not made. Standard SM-TCR/DM-SPR or ordinary single-key family identification remains open: the selected addressed challenge keeps outside raw restrictions available and independently releases its missing full256 restriction after commitment. The public seed S is sampled/known to the adapter before commitment. These features must be compared exactly with any cited primitive game rather than renamed away.

## 6. Quantum scope

**PROVED / OPEN.** If A has a finite-register coherent raw interface and classical source service calls, perform the same irreversible work only in the reduction's private classical source state; the public router is a reversible header partition without querying/recording the coherent transcript. Each adversarial logical query can be forwarded with one selected and one outside XOR invocation, using legal inactive dummy inputs and plus-state response registers, as in the eager addendum. Its full oracle marginal is independent of selected j. Only the final classical signature/verifier trace is used by extraction, so the same2^-56 identity applies to `Win AND G_final` as a mathematical QROM adapter identity. The primitive handle count charges up toQ_q coherent calls to each handle, in addition to the separately counted honest classical calls; their sum is2Q_q, not Q_q. No quantum-ever-hit extraction or machine-checked QROM program is asserted. The exact conventional quantum challenge identification remains open.

# Guarded prefix randomization for interior WOTS predecessors

**OPEN — candidate requiring independent review.** This is a proposed ordinary SM-UD/SM-PRE adapter in HJ[h], not an accepted security theorem or source edit. Public full h never changes. All prospective advantages refer to the exact Th_128^h family and the complete constructed adversary resources. No numerical hardness is asserted.

## 1. Per-coordinate stopped experiment

**COMPUTED — source anchors.** Release lib.rs:239–245 advances a typed chain; :258–267 derives endpoints/signature positions; :601–668 completes a source signing response. A chain of width w hashes predecessors at positions p=0,...,w-2. Source top width256 therefore has maximum p254. The source graph namespace of128-bit public payloads has20,229,886,488,608,768 coordinates, requiring55 selector bits. FORS secrets are uniform start coordinates; WOTS interior coordinates are the additional challenge.

**OPEN — proposed experiment.** Select a typed chain and predecessor p independently before the public parameter. In experiment K_r, replace its first min(r,p) internal chain outputs by independent uniform Node128 coins, consistently across all honest graph/cache/tree/signature computations. Retain actual public h at every address/raw word; the replacements change only the hypothetical signer's retained reference values. Other F/J labels keep their original independent ideal-private laws. Treat unsuccessful setup/search as absorbing nonwinning. Stop before a COMPLETE honest response would expose this chain at any position e<=p. Internal retrieval of opaque values for computing known images is not exposure.

**OPEN — selected event.** E_p means source Win in this stopped experiment and a final classical verifier trace includes the selected typed T_p on the experiment's genuine predecessor x_p. It does not test that this is the globally earliest hidden event. The original canonical unexposed H_final witness implies the corresponding E_p; the stop loses no original winning witness paths. This larger event avoids requiring a distinguisher to compare a candidate with an earlier opaque predecessor.

## 2. Proposed ordinary UD hop for r<p

**OPEN — constructed program.** Submit tweak T_r before P to an ordinary one-target SM-UD challenge. The challenger samples unknown uniform X and supplies either Y=Th(P,T_r,X) or an independent uniform Y. Set the selected internal x_r to opaque X; it is the F start at r0 and a previous independent replacement coin at r>0. Sample all earlier replacement coins independently. After P, set x_{r+1}=Y and compute all later positions using actual h. Recompute affected endpoints, roots, canonical counters, signatures and logical caches from this consistent graph. Do not reuse any old h evaluation or old root from another experiment.

**OPEN — observability.** On retained responses e>p>r the simulator needs only Y and its public-h suffix. All requested response fields needing opaque X trigger the completed-response stop. The selected x_p is known for r<p, so E_p is a computable distinguishing bit without testing hidden earlier prefix values. Public A may compute full h coherently, including the selected tweak and guesses for X; no query is recorded, blocked, reprogrammed or conditioned away. Real Y should couple to K_r; random Y should couple to K_{r+1}. This coupling is the lemma under review.

## 3. Proposed terminal PRE adapter

**OPEN — constructed program.** In K_p, x_p is uniform independent of P and earlier replacement coins. An ordinary SM-PRE challenger at T_p supplies the next image Y while retaining unknown X=x_p. Continue source operations using Y and its suffix. For every retained final classical call at T_p whose image equals Y, the call input is a legal PRE answer; it need not equal X. Thus PRE success should upper-bound E_p without an uncomputable original-input test. A final call touching the selected input in a different public context remains an ordinary actual-h computation.

## 4. Aggregate candidate and constraints

**OPEN — proposed inequality.** Per p, Pr[K_0:E_p] <= Succ_PRE(B_p)+sum_(r<p) Adv_UD(B_{p,r}). A uniform55-bit selector over all genuine128-bit public coordinates may yield the aggregate source contribution <=2^55*(Succ_PRE(B_PRE)+sum_(r=0..253) Adv_UD(B_UD,r)), using K_r with prefix min(r,p). On p<=r the hop is unchanged; B_UD,r returns0 and its contribution cancels. Invalid selectors use a fixed legal dummy challenge and fail. Signed selected-event gaps average before absolute value. Source seed-zero failure is local to each primitive program; a full source union pays that mass once outside.

**OPEN — obligations.** Prove persistent replacement consistency and the graph's acyclic dependence, exact completed-response stopping semantics, selected-event decidability with an opaque earlier value, both ordinary challenge marginal laws and quantum public continuation, and correct aggregate selector averaging. Count challenger evaluation and source setup/signing/coherent circuit/secret-map/cache/message resources. An accepted manual adapter would close a legal interface only; actual SHA family hardness, numeric adequacy and category/capacity would still require evidence. No full forest or operational forgery is generated.

**CITED — motivation only.** HK22 (https://eprint.iacr.org/2022/346), WOTS-TW Claim2, uses undetectability to randomize chain predecessors before its PRE reduction. Its nonadaptive one-time signing theorem is not imported as a theorem for this adaptive LULA source. The proposed source-specific stopped programs above require their own proof.

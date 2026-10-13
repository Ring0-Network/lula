# Independent first: hidden interior WOTS inputs via ordinary UD and PRE

This derivation was saved before reading any new `pre-start-second/interior-ud` work or root interior candidate. It uses the pinned release Rust, HK22 primary definitions, and the previously accepted indexed exposure/event convention. **Manual conditional program derivation; no hardness, numerical security, source refinement or checked security kernel claim.**

## 1. Fixed source and primary premises

Release `lib.rs` SHA256 ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210: the actual typed hash is f_a^S(x)=prefix128 h(S16||zero48||a22||x16), with the SAME public full h (lines121–151). A chain at key address A and coordinate i has x_0=F(A,i), x_(t+1)=f_(A,i,t)^S(x_t), t=0,...,w-2 (239–267). Here F means the independent ideal private-start function in SrcFJideal_h, after the separately justified private-PRF hop. A theorem directly for literal original private starts h(S||zero48||type5||K) requires that private-hop gap; ordinary UD alone does not make those starts uniform.

Source WOTS endpoints enter ordered public-key compression (251–262), then Merkle roots (291–307,479–483). The canonical WOTS+C digit row is derived from the genuine LOWER child (485–495), not from this WOTS key's own chain prefix. Caches are built bottom-up and preserve endpoint roots/counters (498–584); signing uses the canonical row, emits chain nodes and auth paths, and propagates the genuine subtree root (601–667). Repeated/restored honest signatures at one key have the same genuine child and successful digit vector. A final verifier has ordinary classical typed calls (679–729). The indexed event convention is `CHANGED-CHILD-EXTRACTION.md` §1: H_final concerns a genuine hidden nonterminal INPUT, not a coherent-query no-hit event.

HK22 primary text SHA256 be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561, printed5, Definitions3–4 (text188–208): SM-PRE samples uniform hidden input X and returns f_T^P(X); SM-UD returns either f_T^P(U), U uniform hidden, or an independent uniform output. Tweaks are distinct; the common random P is released AFTER A1's challenge queries. Honest secret services are classical, adversaries can be quantum (159–166). Definition7 collection services permit extra pre-release evaluations only at challenge-disjoint tweaks (241–268). The WOTS-TW prefix-hybrid mechanism is in Claim2 (437–511); its signature-position-dependent selection must not be imported silently into the current public-key-first source.

## 2. Select an edge before the parameter or source transcript

Fix a genuine serialized key address A, chain coordinate i and INTERIOR position p with 1<=p<=w-2. Let a_t be its actual type0 22-byte tweak at position t. Choose (A,i,p) by public finite geometry BEFORE P/S, rather than computing it from canonical digits or the final witness. Sampling an index from a finite geometry does not require generating its full graph. For multiple source components, use their ACTUAL contexts/serialized addresses and source interface; do not invent branch tags or assume independent actual tweak occurrences. This first proves a component for one consistent SrcFJideal_h graph.

Let E_source,e be the part of Win AND H_final witnessed by a final selected type0 call with input exactly x_p and with x_p outside completed honest forward closure at that indexed coordinate. In a successful completed source history, a signature at this key with digit d_i<=p would expose x_p by forward closure. Therefore E_source,e implies that no completed honest signature at this key has d_i<=p. Call this the exclusion gate, an exposure gate on classical service responses, NOT a restriction on adversarial h evaluations.

Stop the selected reduction if it would need to complete such an honest signature. This does not remove any E_source,e contribution. If a request would later fail rather than complete, the original source already absorbs and is nonwinning. The gate is also allowed at setup when a completed cached signature is not actually exposed: merely building an endpoint/cache must NOT be counted as adversarial exposure. Use the gate only when processing an actual honest response requiring the unavailable selected prefix. Canonical row failure and all other source noncompletion remain absorbing without conditioning or resampling.

## 3. Prefix-cut games and observable larger event

For r=0,...,p define G_(e,r). Replace only the selected chain's prefix by an independent uniform value U_r at position r, and compute x_(r+1),...,x_(w-1) using the SAME f_t/h. All other ideal F entries, J values, public context, roots, ordered compression inputs, ancestor canonical rows and source cache are generated consistently from these suffix values. On the selected key, allow only responses whose digit d_i>p; on other keys simulate the ordinary source. Missing earlier selected nodes are not exposed or used. This is an explicit artificial prefix-cut hybrid, not an assertion that its missing prefix is a literal source trajectory.

For r=0 the full source starts are genuinely uniform. Its source-facing setup, endpoint/root/cache law and every allowed honest response are EXACTLY those of the original ideal-private source stopped at the exposure gate. The selected F entry can be an opaque uniform challenge input: no allowed source response or root computation requires its value. Other F entries remain sampled and consistently memoized by B. F is never supplied as advice or an oracle to A.

Use the LARGER statistic C_(e,r): source Win, no completed selected-key response with digit<=p, and some final call at the actual selected tweak a_p with input v satisfying f_(a_p)^S(v)=x_(p+1). The simulator knows x_(p+1) and its suffix. It need not decide whether v is literally the opaque predecessor, nor which hidden edge is canonically first, nor whether some earlier unknown prefix value equals v. It only records the classical final trace and runs the ordinary verifier/root comparison. Multiple applicable final calls can be handled by a deterministic first qualifying call. Original E_source,e is contained in C_(e,0), even if C also counts a different preimage or a graph-replacement branch.

This enlargement is deliberate. No whole-source H/G/D7 classifier is needed by any primitive program. Indexed completed exposure is handled by the single selected key/coordinate gate. Final root acceptance is against the genuine root of the CURRENT prefix-cut game, never a stale original root transplanted into a different chain distribution.

## 4. Ordinary UD program for each r<p

B_UD,e,r in primitive A1 selects the FIXED tweak a_r and requests exactly one SM-UD challenge Y. It then requests P. No setup or collection query is required before P is released. In A2 it sets S=P privately, retains the source adversary's ordinary pre-key quantum continuation without releasing S/root prematurely, and runs setup/source signatures using the selected suffix beginning x_(r+1)=Y. Everything below that cutoff is omitted; all ordinary other source calls use public h once P is known. Recompute/cached evaluations use the same Y and suffix. Do not query a_r through an auxiliary collection oracle during the hidden-P phase.

When Y=f_(a_r)^P(U), its known suffix and all allowed responses have EXACTLY G_(e,r) law. When Y is uniform, they have G_(e,r+1) law. Since r<p, the entire suffix through x_p and x_(p+1) is computable from Y; the larger statistic C is computable in either case without any unknown earlier input. Return its indicator. Therefore

|Pr[C_(e,r)]-Pr[C_(e,r+1)]| = Adv_SM-UD(f_h;B_UD,e,r).

This is an ORDINARY standalone single-target SM-UD program: the source adversary's public-key release does not have to coincide with the primitive's disclosure of P to B. B can learn P first, compute the source roots/cache, and only then release the public key to A. This gives a simple lawful route with a geometry-selector loss. The primary collection extension is also legal if used, but is unnecessary for this fixed-edge program. An adaptive tweak selected from source digits AFTER P release would instead violate the ordinary stage ordering; that different route needs its own justification.

## 5. Ordinary PRE program for the final cut

B_PRE,e in A1 requests one SM-PRE target at a_p, receiving Y=f_(a_p)^P(X) for a hidden uniform X, then requests P. It constructs source setup, root, cache and all allowed signatures from selected next node x_(p+1)=Y, exactly as above. It never needs X or the original selected F start. This source-facing channel is EXACTLY G_(e,p)'s channel because its cut input U_p is uniform and used only through that image; source Win and the gate are likewise computable from the channel.

On the larger candidate event, output the final selected-call input v. The ordinary PRE relation f_(a_p)^P(v)=Y holds, whether v=X or a different preimage. Thus

Pr[C_(e,p)] <= Succ_SM-PRE(f_h;B_PRE,e).

The PRE program does NOT test equality with hidden X and does NOT receive X, an inversion oracle, a programmable h or all private F entries as adversarial advice.

## 6. Lawful bound and resources

For EACH predetermined interior edge e=(A,i,p),

Pr[Win AND selected-original-hidden-input event E_source,e]
<= Succ_SM-PRE(f_h;B_PRE,e) + sum_(r=0,...,p-1) Adv_SM-UD(f_h;B_UD,e,r).

This bound closes a legal reduction route, not a numerical hardness claim. A finite global interior event can be covered by summing these edge bounds over the actual finite geometry, or a separately specified selector can incur the appropriate reciprocal selection probability. No observed witness may be used to choose a stage1 target retroactively. No claim of a tight or adequate multiplier, old RO bound, uniform actual h-derived predecessor, or whole-graph source-law equality after r>0 follows. Ordinary UD/PRE insecurity is for the exact same fixed-h typed family and complete resource budgets.

Each primitive program makes ONE primary target query. Source work remains full actual setup, child/grind/cache/signature/final-verifier work on the simulated suffix graph, with consistent private dictionaries, message bytes, pre-key and continuing quantum public-h computation. Root/counter recomputation and selector costs are charged. A fixed chosen chain tail adds at most w-1 public typed evaluations if not already needed; the prefix cut can remove other simulator work but does not make original honest calls free. Source geometry/arithmetic and public circuit generation/workspace are explicit costs. This derivation neither runs all namespaces nor certifies inherited scalar source counts or polynomial cost in log(namespace size). Finite completed-call/bottom conventions must remain the previously specified bounded experiment, not an unproved native-overflow refinement.

## 7. Three routes and smallest discriminating controls

Route1: the fixed-edge standalone UD/PRE programs above, with potentially large geometry-selector/sum costs, appear lawful. Route2: a collection-based batch prefix hybrid might reduce those costs, but must make stage1 tweak selection and challenge-disjoint support queries explicit; it cannot be claimed from HK's WOTS-TW theorem by name. Route3: a direct original-hidden-predecessor primitive would bypass the UD loss but is a DIFFERENT assumption. No rejection/exact-input guessing is required for Route1.

Small finite controls should distinguish (a) replacing one prefix while recomputing roots/cache, versus keeping the old root; (b) source event equality with opaque predecessor versus the observable matching-image superset; (c) the completed-response gate, repetitions/restores and unnormalized natural failure; (d) ordinary challenge-before-P selection versus an illegal digit-dependent target after P. These controls are not real source forgeries or hardness experiments. A counterexample to simple uniform-input substitution is any non-balanced first chain function: x_p is then nonuniform although the start is uniform. It refutes an exact-law transplant without UD, but does not refute the legal UD hybrid above.

# Independent dynamic quantum hidden-value model

Saved before reading `DYNAMIC-QUANTUM-HIDDEN-DRAFT.md` or a peer quantum hidden lane. Scope: a finite classical-server/coherent-public-RO model for the final classical genuine-unexposed-input event. It is not a classical query-history event for quantum queries, nor full QROM signature security.

## Pinned source and protected coordinates

Source `release/code/lula1/src/lib.rs` SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Work after the joint F/J ideal hop, for fixed nonzero public seed S, classical atomic source signing, honest opaque snapshots, and a finite injective raw-query register. Both worlds' private classical server evaluates the same fixed programmed public function G and private F/J maps. Source keygen/signature return is partial; noncompletion is nonwinning. No timing, internal query transcript, private buffer or seed/cache bytes are disclosed.

For each full WOTS key/chain, sample values X_p independently uniformly in N=2^128, p=0,...,w-1. Each chain position has its own type0 full address (239–245). Program its designated input X_p, p<w-1, to have prefix X_(p+1) and independent uniform128 suffix. X_0 is the corresponding private F prefix (248–250). For each FORS leaf, sample secret X independently uniformly and program its height-zero type3 point to an independently sampled public leaf image (344–350). Full images are256 bits and repeated inputs are consistent.

The rest of the addressed DAG is programmed at its honest inputs from the start. Its safe public surface Phi comprises endpoints, FORS leaf images, endpoint-compression and internal-node/root images, and independent suffix/metadata randomness. It does **not** include interior chain values or FORS secret payloads. Nonprotected designated inputs depend only on Phi/other nonprotected predecessors. A topological typed-DAG sampler gives a fixed G with the ordinary complete-RO marginal in this finite joint-private model. The separately required full source/RO refinement is not replaced by assuming arbitrary graph data is independent.

## Dynamic overlay and known closure

Keep an independent residual table R at every protected raw domain. Initial Known includes all WOTS endpoints, which are in Phi; no secret FORS leaf is known. A completed honest signature at a WOTS address reveals its canonical X_e and makes **the entire suffix e,...,w-1 known**, while a completed FORS signature makes its selected secrets known. Known is a monotone global union across restored branches. No exposure is rolled back, and a partial call reveals no secret coordinate. A repeated address has the same canonical vector.

Define the ghost public quantum oracle O_Known: at a designated protected point whose input coordinate is in Known, return the full programmed G image; at other protected points return R; on every nonprotected domain return G from the start. Before each public query it is a well-defined full-output XOR unitary. It is explicitly time-dependent after classical disclosures. It is **not** asserted to be a fixed ordinary random oracle.

Past quantum states are retained unchanged when a reveal changes the future oracle. An earlier ghost residual answer can conflict with the newly programmed G answer; there is no classical query log and no claim that the old answer is retrospectively overwritten in memory. Previous real/ghost state discrepancy is already charged by the prior query hybrid. A static residual oracle after reveal would be incorrect.

Suffix closure is essential: if X_p is known, the programmed output prefix X_(p+1) must also be known. Otherwise a query at a supposedly harmless known input immediately leaks a supposedly still-hidden next coordinate. FORS revealed secrets output only public Phi. It is permissible to retain all known suffix values as auxiliary classical proof state or grant them in a safe strengthened interface; actual signatures transmit only X_e. These auxiliary known values may affect ghost answers, but remain independent of the still-hidden coordinates.

## Predictable disclosure and retained quantum memory

PROVED invariant under the specified ghost experiment: condition on its full residual/nonprotected tables, Phi, measured classical history and the values of Known. Every remaining coordinate is independent uniform, and its value is independent of the adversary's accumulated quantum density operator. The statement concerns **remaining** coordinates, not previously revealed ones, and does not condition on failed hidden guesses.

Induction:

1. Initially safe Phi is independent of hidden prefixes/secrets; private F/J and G generation must satisfy the stated sampler law.
2. A ghost query unitary is determined by R, Phi and Known values only. It never depends on a still-hidden input coordinate or a still-hidden output value. Hence it cannot correlate the adversary's state with remaining coordinates.
3. The measured message, route and canonical digit/counter selection are determined by this state and outside-protected data. Source `child_value`486–496 is FORS PK or lower-subtree root, independent of secret payloads. Type7 grinding216–236 consumes Phi child values. Source route601–617 uses J and unaddressed message hashes; S!=0 separates those from protected addressed domains. Thus the set of coordinates about to become known is chosen without inspecting their hidden values.
4. Reveal the selected coordinates and close their WOTS suffixes atomically at completed return. Adaptive revelation of an independently sampled field at predictably selected indices preserves independence of the other coordinates, including numerical duplicates. The retained quantum state can depend on newly revealed values after subsequent operations, but not on the remaining field.

The real adversary state need not be keyblind. No source-secret-driven selection of indices is allowed. Canonical constant sum alone is insufficient to prove predictability; the actual child/type7 construction supplies it here.

## Coherent query hybrid

At a ghost public query the fixed G and O_Known differ only at designated points with still-hidden inputs. Each raw string identifies at most one actual protected coordinate because chain positions/type and FORS global leaf indices are fully addressed. The ideal query's averaged input mass on that hidden set is at most1/N by the invariant; no total-coordinate multiplier occurs.

For a common purification, the unitary difference on that support has norm at most2, giving an averaged global vector error at most2/sqrt(N) per coherent query. All classical server calls and disclosure updates are **common channels** because they evaluate G in both experiments. They can be dilated identically and introduce no comparison error.

Group arbitrary common measured/classical service operations between numbered coherent-query slots. Slot j runs until the next adversarial public coherent query or absorbing termination, then supplies a controlled identity for inactive branches. This gives Q slots under a deterministic query cap without a sqrt(random-activation) accounting mistake. A common Stinespring dilation handles the intervening classical measurements, private computation and adversarial operations. On each continued ghost state the unused-coordinate mass bound applies. Telescoping yields

    ||Psi_real - Psi_ghost|| <= 2Q/sqrt(N)

before the terminal examination. This is an elementary purified hybrid, not an O2H extraction claim and not a bounded-efficiency source simulator. In particular, no event saying a quantum query 'hit' a hidden point is inserted into the adversary's history.

## Common stopped terminal examiner

The final signature/message are measured classical outputs. Define H_final as the first genuine still-hidden type0 chain input or height-zero type3 FORS secret input encountered in the final verifier trace. Known stays fixed during verification; verification is not a legitimate signature disclosure.

Construct a terminal examiner that, just before each protected classical hash, checks the coordinate/input equality. If it is a hidden genuine input, emit H and stop **before returning any hash answer**. Otherwise evaluate the hash normally. Before that first hit, G and O_Known agree on every actual examined input: known points use G, non-genuine hidden-domain inputs use the same residual value, and nonprotected domains agree. Therefore this stopped examiner is a common channel for the two input states and matches the actual real verifier's H_final event. No hypothetical private graph evaluation is counted as a final witness.

To bound the ghost examiner's H probability, use a different analytical **unflagged continuation**: run the verifier with O_Known and never branch on the hidden equality flags. Its classical candidate list is a function only of the ghost state, R/Phi/Known and the candidate bytes, independent of remaining coordinates. Each nominated unknown coordinate is genuine with probability1/N unconditionally. First-hit agreement identifies the same H event in the stopped examiner. Do not assert a1/N posterior after conditioning on all earlier misses.

For fixed source parameters and every reached accepted digit vector, verification has3000 type0 chain calls plus17 FORS leaf calls, hence at most3017 hidden candidates. Rejection can only reduce this count. The unflagged ghost examiner's hidden event probability is at most3017/N.

A common event projector on purifications gives the amplitude comparison

    |sqrt(Pr_real[H_final])-sqrt(Pr_ghost[H_final])|
       <= 2Q/sqrt(N).

Consequently

    Pr_real[H_final] <= min(1, (2Q+sqrt(3017))^2/N).

This is a final classical acquisition/witness event. It does not bound a nonexistent list of quantum-query hits. q affects the history/Known set but adds no direct loss under predictable atomic disclosures. Fixed S!=0 is the local scope; charge S=0 once in the overall source-to-joint-game bridge, not repeatedly in this lemma.

## Required controls and open boundaries

Two small failure controls are decisive: a static ghost remaining residual after revelation has a large discrepancy at a now-known point even though hidden support is empty; and a known-input overlay without suffix closure discloses an allegedly hidden successor immediately. A positive finite control should retain a prior entangled query state, disclose one independent coordinate, update only its known overlay, and verify that the remaining coordinate changes no ghost state.

OPEN: independent validation of the common Stinespring/grouped-slot construction, full programmed-DAG/source refinement, finite-domain/partial-service exactness, and the other QROM event terms. This does not establish complete quantum security, a concrete SHA guarantee, efficient challenge embedding or any signing capacity/security level.

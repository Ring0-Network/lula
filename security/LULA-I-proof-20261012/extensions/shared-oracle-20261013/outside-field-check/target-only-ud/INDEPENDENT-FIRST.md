# Independent first: target-only public queries in the full shared random oracle

Saved before reading any new target-only peer derivation or root target-only artifact. Parent supplied the research direction and, during derivation, a proposed all-parameter slice/phase router; this is independent source/primary checking, not a claim of discovering that direction. **Scope: ideal-private source with ONE full shared random oracle O: bytes->256 bits, not fixed SHA, not an old-scalar update or a complete security certificate.**

## 1. Actual byte slice and full-output law

Pinned release lib.rs SHA256 ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. Typed f outputs prefix128 O(S16||zero48||T22||x16) (121–151). Address layout is layer1/tree8/type1/kp4/w2_4/w3_4 (69–95); source valid layer indices0..4 preserve injectivity. Fix an ACTUAL selected type0 chain-step tweak T*, or a selected type3 height-zero FORS tweak for terminal PRE, ex ante.

The target slice MUST contain ALL parameter words, not only the later-revealed source S:

W_T* = {P16||zero48||T*22||x16 : P,x in Node16}.

Every member has102 bytes. Let H(P,x) be an unknown independent random128-bit function on this slice's parameter/payload pair. Let G(w) be an independent random256-bit function on the entire finite raw-byte envelope. Define full shared O by

O(w) = H(P,x)||low128 G(w), if w parses into W_T*;
O(w) = G(w), otherwise.

H and G are sampled independently and the selected parsing map is injective. Thus O is exactly a full256 random function: its high and lower limbs on every word are independent uniform, and different words have independent outputs. The same literal raw word always has the same output, whether reached by A or by an honest role. G's unused high limb on selected words is irrelevant; this representation invents no separate source namespaces or source-word changes. Lower bits are NOT replaced by zero, discarded from A's reply or correlated with H.

Across all P, the restricted H is an ordinary random tweakable function with a singleton tweak: key/parameter P,128-bit input and128-bit output. It can equally be realized by the selected-tweak restriction of a full random Th family. A's pre-key oracle queries may range coherently across P, so every selected word routes to H before S is known. Restricting only the eventual S slice would change this pre-key oracle unless an unknown-S coherent router were additionally available; that route is not claimed.

## 2. One ordinary H query per coherent full-O call

The selected membership flag s(w), parsed(P,x), and an off-domain dummy are reversible public computations independent of the hidden parameter. An XOR oracle controlled by this flag can be implemented with one ordinary H query: prepare an n-qubit |+> response scratch register, conditionally SWAP it with the main HIGH response when s=1, apply ordinary U_H to parsed(P,x) (dummy when s=0), then undo the SWAP and address computation. XOR leaves |+> invariant on inactive branches. The scratch returns to |+> in all branches, while active high response gets H(P,x). Hence no hypothetical controlled-black-box primitive or second uncomputation query is assumed.

Apply the analogous locally known G circuit to BOTH response limbs off-slice and only the lower limb on-slice. Its unwanted high action can be masked by the same |+>/SWAP technique, or equivalently use the Fourier phase mask ((1-s)*z_high,z_low). The remote H phase mask is s*z_high. These masks add exactly the phase of z dot O(w), then Fourier-transform the main response back. This alternative gives the same one-remote-query router. A full response register may be entangled with A/workspace; the identities are linear and apply coherently without measuring s, w, P or A's state.

All reversible parsing, masks, swaps, known G evaluation and cleaning work is charged. No-hit restrictions and selected-word blocking are unnecessary. O_A is one shared full-output oracle before and after public-key release; it has no programmed values.

## 3. Audit every honest possible selected-slice use

Use the already reviewed fixed-edge prefix-cut programs, with the common S!=0 conjunction. For active UD hop r<p, T* is the selected T_r; for terminal PRE it is selected T_p or the selected FORS leaf. Every designated honest selected edge uses the challenge image Y directly, persistently across roots/cache/recomputations. Its opaque predecessor is not needed by any retained response. Earlier overwritten private edges are skipped consistently; every retained selected-chain response begins beyond p, hence beyond r. Other type0 calls have distinct full serialized address, as do other type3 leaf/index or positive-height calls. The target edge's only honest designated computation is therefore intercepted, not evaluated through H repeatedly.

All nonselected typed calls are off-slice by length or address: type7 has20-byte payload/106-byte raw input; ordered Merkle pair hashes have32-byte payload/118-byte raw input; WOTS public-key compression has16 or32 Node16 endpoints; FORS root compression has17 Node16 roots. Private F/J are independent persistent ideal maps; literal private PRF hash calls have already been removed by the separate private hops, and their original fixed-h alias law is not invoked here.

Raw message inner input is R16||S16||root16||M. If it happened to have length102, membership in W_T* would still require its bytes16..63 to be all zero. Its bytes16..31 are the nonzero source S, so it is off-slice for EVERY first parameter P, including a P numerically equal to R. Outer message input has length52, so is off-slice. This is why the S!=0 qualifier matters: at S=0 a raw message can conceivably alias the selected slice, and must not be declared off-target for free. The existing program fails locally at S0; a master source union pays that mass once externally.

The final classical verifier can reach the selected actual typed edge at most once per parsed fixed source graph path: each WOTS chain step is run once, or the selected FORS leaf is run once. Its one actual H evaluation must be counted and its returned image reused for the selected image-match statistic/PRE output relation. In UD the final selected C event is at T_p, which is not T_r for an active hop; its check is locally off-target. Full final root/freshness verification still runs, using the routed full O throughout. Any unforeseen extra selected-slice use would invalidate this precise cap; it must be charged, not suppressed.

Consequently a source adversary making Q_A COMPLETE raw O queries, including all coherent pre-key and continuing public calls, yields Q_unknown<=Q_A+1 public H queries. The ordinary target service itself is one challenge query and is separately accounted by the primary game, not an additional adversarial evaluation of H. Source setup/signing may be enormous, but its other oracle calls are to the locally known independent G and ideal F/J, rather than this unknown H.

## 4. Finite local simulation remains honestly charged

This is not a free exponential G table. Fix an ex-ante raw-byte envelope covering all A/source/auxiliary words. Sample a deterministic finite2T_all-wise independent random-function representation with full256 replies, using the previously accepted bounded quantum random-function simulator. T_all counts ALL locally simulated G invocations, including every honest classical setup/grind/signature/final call and A's coherent calls; it is not Q_A+1. Its generation, field/key construction, evaluator gates, storage, persistent private maps and circuit workspace remain charged. Arbitrary circuit-independent randomness can be fixed as B's private coins in the H-query proof.

Exact bounded-query independence applies jointly with the independent H oracle and adaptively chosen source words. The classical challenge Y may influence G inputs; independence and the all-call T_all budget still suffice. The known simulator can cost vast time and memory; replacing outside queries by local gates improves the unknown-H QUERY cap, not the complete runtime cap. This derives a lawful query-complexity program; it does not claim a feasible implementation or silently improve existing source-cost scalar receipts.

## 5. Published UD applicability and activation weighting

HK22 cached text SHA256 be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561, §8.3 Lemma3, printed24/text1065–1078, bounds ordinary random-Th SM-UD advantage by12q/sqrt(2^n). Its H oracle includes all public parameters; target P is sampled and only later revealed (Algorithm4 text1081–1095). It concerns random Th, not fixed SHA. Here the routed unknown H is exactly that random family for one target, while G/F/J and all local simulation circuits are H-independent private randomness. Thus the ordinary QUERY theorem applies with q=Q_A+1, after the exact router/byte-use audit; no conjectured general collection extension is needed.

Let K=2^41+2^36+2^31+2^26 and n128. At hop r, the number of active selected WOTS positions p>r is

D_active(r)=32*K*max(14-r,0)+16*2^21*max(254-r,0), r0..253.

FORS and p<=r selectors are inactive. Conditioning on an active selector is an ex-ante legal mixture of one-target programs, so delta_r <= (D_active(r)/2^55)*12(Q_A+1)/2^64. Zero-seed skipping remains inside that program's ordinary unconditional advantage; it is not independently normalized.

Summing active counts gives

A_H=sum_r D_active(r)=32*K*105+16*2^21*(254*255/2)=7,628,143,271,608,320.

The selected terminal PRE success is also activated only by valid coordinates: pi_PRE <= (D_H/2^55)*kappa_PRE(Q_A+1,128), D_H=20,229,886,488,608,768. Here kappa_PRE is an applicable one-target random-Th PRE bound for the exact unknown H interface; I do not invent a numerical constant. HK22 §8.1/text990–1000 discusses an unconditional length-preserving SINGLE-target quadratic PRE conclusion via SM-TCR/DSPR, but its asymptotic Theta statement alone does not specify an exact numerical certificate. A fully explicit chosen PRE theorem/constant is the remaining numerical input if a displayed finite scalar is required.

Therefore the lawful source-relative schematic bound is

Pr_HJ[O][Win AND H_final AND S!=0]
<= min(1, D_H*kappa_PRE(Q_A+1,128) + 12*A_H*(Q_A+1)/2^64).

This is an activation-weighted shared-random-oracle consequence of explicit programs, not a replacement scalar for the previous fixed-h artifact or old RO/QROM tables. The UD term still grows linearly in Q_A and may make the result vacuous; removing huge honest unknown-query costs is not by itself useful tight security. Better estimates require new mathematics, not asserting fixed-h hardness or changing a quantum PRE term into a UD term.

## 6. Controls and remaining proof boundary

Discriminating finite controls should test full high/lower output consistency on repeated selected/off-target words, all-parameter pre-key routing, exact one-query coherent masking on entangled/phase states, nonzero-seed raw-inner separation and zero-seed counterexample, final-call reuse, and arithmetic active-selector counts. Source helper and local2T_all simulator resource evidence must remain separate from remote query evidence. No full graph, actual forgery, A-query measurement or fixed-SHA hardness inference is required.

The smallest possible residual lemma is the formal source-call partition/router composition theorem for this specified full shared O. The source byte audit and unitary construction above supply its manual argument; finite controls supplement it. An exact finite PRE constant and a machine-checked whole-source/query refinement remain separate. No source/game kernel declaration, manuscript/source edit or old numerical-bound promotion is claimed.

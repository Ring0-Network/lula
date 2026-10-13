# Independent source-first ordinary-PRF private hybrids for public fixed h

Saved before reading `chain-pre-adapter/public-h-private/INDEPENDENT-DERIVATION.md`, its clarification, successor provenance, or controls. This first argument uses the release `lib.rs` SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`, inspected in this turn, and the ordinary real-versus-random classical-query PRF experiment. It does not promote or edit any old RO bound, manuscript, implementation or receipt.

## 1. Exactly which game is meant

Let h be one fixed, public, efficiently computable full256-bit hash algorithm on finite byte strings. Its entire implementation is available to the adversary/reduction. It is not a hidden sampled random oracle and is not assumed ideal. S,K,P are independent uniform16-byte strings, matching the source's uniform48-byte seed split. Put t=prefix128 and define

f_K^S(A)=t h(S||zero48||AD22(A)||K),
g_P^S(M)=t h(P||S||M).

AD22 is the complete literal source address. f may be defined on all22-byte addresses or restricted to the well-defined type5/6 private address domain; the reduction queries only that domain. g is defined on the finite-message input model of the source adversary, with ordinary byte strings, not a new length/prefix encoding. Both private interfaces return128 bits, as `Ctx::prf/prf_msg` do. Raw public evaluations still return the COMPLETE256 bits of the same h.

For each fixed public S, the ordinary f or g PRF experiment gives a distinguisher a classical chosen-input oracle: either the keyed function with a uniform unknown16-byte key, or a uniformly random FUNCTION on that same domain/range. Repeated inputs reuse their answers. A distinguisher can otherwise perform quantum computation and implement the public h coherently using a reversible circuit. This is classical-query security against a quantum distinguisher, not quantum-query PRF security.

To average over S, use a public-parameter version that samples S independently and gives it to the reduction before its oracle interaction, or take the explicitly weighted family of fixed-S experiments. Ordinary PRF for a secretly keyed pair (S,K) with S never disclosed is NOT automatically the same assumption. Public S can be hidden from the signature adversary while already known to the reduction. The averaged signed gap equals the public-parameter game's signed gap. If only pointwise fixed-S advantages are assumed, triangle inequality gives the expected fixed-S advantage bound.

## 2. Source interfaces and private interception

The source at lines109–147 initializes a public S||zero48 prefix and truncates its addressed hash to16 bytes; lines161–168 implement f and g above. `sign` lines601 onward uses g only to choose R, then computes the inner/outer digests from R, S, root and the literal M. All further public WOTS/FORS/Merkle operations use the same addressed hash. `verify/verify_root` lines672 onward recompute public digests from transmitted R and counters and accept only when the returned root equals pk.root. Verification has no f/g oracle call.

Define G0[h] as this source experiment, GK[h] as the experiment replacing only private f calls by one independent random map F:A->128, and GKP[h] as further replacing private g by an independent random map J:M->128. All three retain the SAME fixed h for every public/raw computation; no public h table or word is patched. Ideal maps are persistent over keygen/signing/restoration and repeated messages. They are independent of each other and of sampled keys, but not asserted independent of the eventual transcript, which exposes derived values.

An implementation adapter must intercept every private call, not merely overwrite one stored seed. It may use a placeholder unknown seed only after ensuring unadapted `prf/prf_msg` never read it. Public prefix initialization depends on S only. Complete addresses and complete message bytes are cache keys. Secret maps do not lose their values when the source cache is restored.

## 3. Exact f reduction

D_K gets S and an ordinary f oracle E. Sample P uniformly, leave K unknown. Forward A's pre-key raw interface using public h, withholding S and pk. Save the full quantum continuation and respect a pre-key abort as nonwinning. After the mandatory setup transition, construct the source key/root/top cache using secret(A)=E(A). Compute R(M)=g_P^S(M) locally through public h. Resume A with the generated public key, service at most q initiated CLASSICAL signing requests through the same adapter, and retain the permanent Seen set across all restorations. At final (M*,sigma*), use the exact PUBLIC source verifier and output [M* not in Seen AND verify(pk,M*,sigma*)].

All E calls are classical: setup addresses are classical, and the source signing interface receives classical messages. A can use quantum public-h computation without inducing a superposition E call. In E-real, the entire experiment is exactly G0[h]; in E-random it is GK[h]. This holds for every fixed S, including S=0. In particular raw evaluation on a guessed secret word agrees with E in the real arm, while in the random arm it remains h and can disagree with F. That is precisely the ordinary PRF game's allowed public-algorithm correlation, not a simulation defect.

Let p0,pK be the final event probabilities, with the stated S distribution. The SIGNED identity is p0-pK=Pr[D_K^f=1]-Pr[D_K^RF=1]. Its absolute value is this particular distinguisher's ordinary PRF advantage. A supremum insecurity notation upper-bounds that value; it is not generally equal to it.

## 4. Exact g reduction after the f hybrid

D_P gets S and an ordinary g oracle E. Generate one consistent independent ideal F map. Unknown P is not needed. Run the same pre-key/setup/service/final-verification program, with secret(A)=F(A) and R(M)=E(M). The real arm is GK[h]; the random arm is GKP[h]. F is sampled lazily on the classical addresses actually needed. It stays fixed and independent of E. Public h is the same concrete implementation in both arms.

Thus pK-pKP=Pr[D_P^g=1]-Pr[D_P^RF=1], and |pK-pKP| equals this particular D_P's PRF advantage. The signed total identity is the sum of the two signed oracle gaps; the absolute bound is

|p0-pKP| <= Adv_f(D_K)+Adv_g(D_P),

and p0 <= pKP+Adv_f(D_K)+Adv_g(D_P). There is no assertion that the absolute total gap equals the sum; cancellation can make the inequality strict. No source-dependent conditioning on final acceptance or private-map transcript is used.

## 5. Literal aliases, zero seed, and partial computations

All raw inputs are literal source byte concatenations. No separate private random oracle, injected tag, rewritten address, collision-free parser or independent lower limb is introduced. Any collision/alias between a public raw word and a keyed private word is retained in the real arm because both evaluate the same h. The ideal arm replaces only the named private service as the game definition says. Guessing K/P by evaluating h is available to the ordinary distinguisher and is charged to its computational budget; this argument proves no hardness against that strategy.

S=0 is included in the ordinary-hybrid identities. It does not require a new statistical correction term just to identify these games. If a later component proof is scoped to S!=0, its seed-zero charge is made there, once; it is not transplanted from an old RO lemma into the present exact identity. Likewise a fixed-S conditional claim uses the corresponding PRF game/advantage, not an unconditional average silently relabeled.

The source has32-bit grinding loops without a proved all-input completion theorem. The finite partial experiment checks at most2^32 distinct candidates; a noncompleting service produces an absorbing nonwinning outcome and reveals no newly invented exhaustion response to A. Use this SAME totalization in the compared games/reductions. Different completion probabilities are allowed and are included in the oracle gap. This is not a Rust overflow/termination refinement. Malformed final signatures remain nonwinning according to the exact verifier.

## 6. Resources derived from the source dependency loops

Ordinary private-oracle queries can be memoized without changing any arm. Top-prepared setup queries2^21 top WOTS keys with16 secrets each plus2^21 lower child trees with32 WOTS keys and32 secrets each. This gives at most2^25+2^31=2,181,038,080 distinct f labels. A hot signing request uses8,704 FORS labels, four lower child trees of1,024 WOTS labels each, and16 top labels, for an additional conservative12,816 labels. Repeated selected-chain/FORS derivations refer to addresses already present. A cold request can additionally use all2^25 top WOTS labels, giving33,567,232. Because setup already queried the top labels, these per-request caps are conservative rather than exact fresh-key increments.

For domain size N_D, Q_f <= min(N_D,2,181,038,080+q U_mode), U_hot=12,816, U_cold=33,567,232. Q_g <= q distinct messages. No private query is made by final verification. Memoizing on complete labels means repeated/restored executions do not create fresh independent responses. If public cache advice were disclosed or arbitrary edited caches allowed, it would require the corresponding separately specified source interface.

Public h work must also be charged. Let H_setup,H_mode,H_final be public-h call caps excluding the private restrictions. D_K computes the known-P message randomizer locally, adding up to one hash per initiated request; D_P gets it from the g oracle. Conservative local public-h call caps are therefore H_setup+q(H_mode+1)+H_final for D_K and H_setup+qH_mode+H_final for D_P, plus A's own public-h computations. H_setup includes each prepared child, top tree and canonical search; H_mode includes all signing searches; neither is merely A's hash budget. Source/context initial prefix and all full-message byte/block costs are charged as actual algorithm work, not hidden unit-cost hashes.

A straight-line public h evaluator can be converted to a clean coherent XOR circuit with charged gate/work overhead. The reductions do not classically simulate A's quantum amplitudes; they run it. They retain A's quantum continuation, source cache/tree state, F/J dictionaries, message bytes, Seen and final signature. Query count alone is not a complete time/storage bound. The source's fixed astronomical setup and grinding caps can make these reductions impractical while still finite relative to the explicit service costs.

## 7. Scope of closure

These are ordinary public-fixed-h PRF assumption-parametric adapter identities. They remove the need to posit an extra linked raw challenge FOR THESE TWO PRIVATE HOPS because h is a known algorithm, not an unknown blackbox. They do not show f/g are secure, establish a numerical classical/quantum advantage, prove the remaining public component bound, equate HJ[h] with HJ[O], or import the earlier RO guessing bounds into fixed SHA. No quantum-query private PRF access or full256 private output is assumed. Toy controls can test serialization, alias preservation, hybrid arithmetic and small exact transcripts; they will not prove hash hardness or the general source simulation.

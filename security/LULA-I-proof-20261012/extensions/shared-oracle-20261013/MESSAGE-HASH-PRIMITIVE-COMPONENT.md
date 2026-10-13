# Message-hash coverage: chosen context, canonical targets and free-counter candidates

**PROVED — source-compatible conditional component program; hardness ASSUMED, primary quantitative lift OPEN.** Two independent first derivations compare the actual source with the primary interleaved target subset-resilience notion. They agree that nonce memoization and source-generated context can be reconciled, but canonical honest-target selection and arbitrary accepted forged-counter selection are different interfaces. This component specifies the missing property; it does not certify SHA-256 hardness or import a random-oracle estimate.

## 1. Actual source and primary interface

**CITED.** SPHINCS+ official round3/round3.1 specifications Section9.1 and HK22 Definition11 (https://eprint.iacr.org/2022/346) define a target oracle that samples a fresh uniform hash-family key/nonce on each chosen input and registers its mapped coordinates. The official specification explicitly returns both nonce and mapped output. HK22's compact extracted display contains return/symbol omissions; this component follows the explicit primary specification, not an invented C-ITSR definition. Exact primary-version PDF/text pins are in the peer receipts.

**PROVED — source function.** For one public full256 h, S16 and source root Z16,

`U_p(R,M)=h(R||S||Z||M)`, `D_p(R,c,M)=h(U_p(R,M)||BE32(c)||S)`.

The SAME h and all256 U bits are retained. The first passing counter c0<2^32 has bits153..161 zero; failure is unnormalized bottom. The17 real9-bit indices are bits0..152; the41-bit route I is162..202. Define G_p(R,c,M) as17 tuples(I,j,leaf_j), j=0,...,16, for passing digests. I corresponds bijectively to the bottom FORS(tree,keypair). No eighteenth secret is exposed.

**PROVED.** Source ideal J memoizes R for each complete message. The final verifier instead uses arbitrary transmitted R* and any passing32-bit c*. It checks neither J[M*] nor c* minimality. Source freshness is M* absent from all initiated signing requests, stronger than primary nonce/message-pair freshness.

## 2. Legal reconciliation of nonces and context

**PROVED.** A reduction can query a fresh-nonce primitive once per distinct M and memoize its reply for repeats/restored branches. New labels have independent uniform R, including possible collisions; repeated labels reuse the same nonce and canonical target. At most q initiated requests imply at most q target queries.

**PROVED — explicit lifted family.** The primitive's logical chosen input may be an injectively encoded tuple Enc(S,Z,M). Its PUBLIC function parses that tuple and evaluates the exact literal U/D words above. Enc is interface framing only; its tags/lengths are NOT inserted into the source hash words. The primitive key is R alone, sampled after the chosen input. This makes actual source-derived(S,Z) an adversary-chosen context, retaining its correlation with source F/setup. No independently uniform root is substituted. A bound for this explicit lifted chosen-context family can cover the reduction's generated context; it is not a theorem for a different untagged/root-distribution instantiation.

**PROVED.** The reduction samples and retains its own independent F, computes source setup/root/cache with the SAME h, and constructs every returned signature/authentication path with that F/h. It never grants F as adversarial advice. A's pre-key continuation sees only public h before ordinary pk release. Setup and finite-counter failure remain absorbing nonwinning. Full public-h circuit, message bytes, source and challenger work are charged.

## 3. Exact primary-game gap

**PROVED — interface distinction.** H_can(R,Enc(S,Z,M)) computes the first accepted counter and matches the honest target law, but primary ITSR on this function tests only the FIRST accepted candidate counter. The actual verifier accepts any passing c*. Conversely H(R,Enc(S,Z,M,c)) matches a free candidate, but primary target-oracle R is sampled after c is chosen, whereas honest source c0 depends on that R. A later target query samples a new R; it cannot retrospectively register c0 under the original R. Treating(R,c0) as a uniformly sampled key is false.

**PROVED / COMPUTED — logical separation, not a source attack.** Finite controls construct an injective canonical nonce/message coordinate map: with one target, every fresh pair's canonical tuple set is uncovered. Another accepted counter maps a fresh message with the target nonce onto that target's coordinates, so the free-counter game succeeds. Independent controls retain17 real tuples, a valid zero9 filter and a41-bit route slot. Canonical fresh-pair success is0 and free-counter fresh-message success1 in the defined finite instance. This refutes a generic canonical-ITSR-to-free-counter implication; it does not claim a flaw in actual SHA-256 or an operational LULA forgery.

**OPEN — smallest lifting lemma.** Prove a bound for the canonical-target/arbitrary-valid-counter extension of this exact two-stage h with literal BE32 and bottom, at the source reduction resources, or prove a legal quantitative lift from an applicable primary ITSR instance. Merely citing primary ITSR for H_can or the free-counter raw function closes neither side of this mismatch.

## 4. Named additional game and explicit source component

**ASSUMED — property name; PROVED — chosen game definition.** RC-CTAC-SR(h) denotes registered-context canonical-target/arbitrary-counter subset resilience. It is an explicitly additional source-compatible property, not a published named definition. B knows the public h and registers one common source context(S,Z), retaining its own state. Target(M) on a new label samples uniform R16, finds the first zero9 passing BE32 counter up to2^32 and returns R,c0,fullD or bottom; repeats return the same result. Successful target tuples are registered. The final candidate(R*,c*,M*) must have a passing digest, a fresh target message and all17 tuples covered, but need not use a canonical counter. No signature validity or graph-preimage predicate is built into this coordinate game.

**PROVED — B_cov program.** Preserve A's pre-key phase and quantum memory; sample F/S, run the actual source setup using h, register its context and release source pk normally. Obtain target nonces/canonical data only once per unique message; build exact source signatures using retained F and h. Maintain source freshness for all initiated requests and source exposure tuples only for completed responses. Parse A's final candidate and output its R/c/M if the source indexed-coverage/freshness branch occurs. No recognition of later full root acceptance is required for the superset argument.

**PROVED — correct event attachment.** CHANGED-CHILD-EXTRACTION.md Section5 defines C_cov using the completed-signature union. Thus

`Pr_SrcFJideal_h[Win AND C_cov] <= Succ_RC-CTAC-SR(h)(B_cov)`.

This does not upper-bound every bare coverage observation, stale-message candidate or H/G replacement event. A primitive ledger may register a successful message target before later source signing finishes: its superset only enlarges primitive success. On source noncompletion the experiment absorbs, so no fabricated source response/exposure is produced; no Commit API or success normalization is required for this one-sided bound. An optional commit variant matches the smaller ledger, but is not silently identified with the larger one.

**PROVED.** This interface identity adds no seed-zero penalty: all actual h aliases at S=0 remain linked. A later complete source union may separately exclude seed-zero for other components, but must pay that mass once only. Primitive pair-freshness could be relaxed to enlarge the winning event; the displayed game keeps source new-message freshness.

## 5. Resources, controls and scope

**COMPUTED / PROVED.** Each new target uses one full inner hash of length48+|M| and at most2^32 complete outer52-byte evaluations. B's source setup/FORS/WOTS/final-verifier work and F/cache/Seen/message storage remain charged. Public coherent h computation and circuit generation/workspace are explicit. Digest work removed from B because the challenger executes it is not free total-experiment work and must not be charged twice. q is initiated classical signing requests across all branches; classical private/target services do not become coherent signing access.

**PROVED / COMPUTED.** Independently saved first arguments540ae17b andb0770080 preceded reciprocal exchange; the chosen-context lift clarification514cc206 was saved before its author's peer read. Controls discriminate canonical/free-counter behavior, nonce memoization, context decoding without source-hash tagging, and a wrong independent-root replacement. Peer controls were extended during review; final receipts pin the CURRENT sources/results and preserve historical outputs instead of claiming those old outputs match the successor source.

**OPEN.** Actual RC-CTAC-SR hardness, legal primary numerical transfer, hidden-predecessor PRE and adequate complete fixed-h security remain unestablished. The source RO/QROM numerical formulas and manuscript are unchanged. This manual game/program component adds zero whole-source/game kernel declarations. Bit-projection helpers, if promoted separately, prove only their stated finite-word identities.

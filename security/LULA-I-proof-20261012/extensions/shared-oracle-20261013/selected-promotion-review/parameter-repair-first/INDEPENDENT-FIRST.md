# Source-first T3 parameter-repair analysis

**COMPUTED — first-save provenance.** I read both complete original user attachments, OBJECTIVE.txt and the pinned release lib.rs before reading any NEW peer/root repair or criterion derivation. The attachment hashes are655c5344c76c16d6e22d15ab169847385154a147dd28d0d31f1bbe86b465ee2f andccdcfbc8b10de3d10546573ea9d92c0f906b182dcb34ba2eb100225bb206a1e8. The first matches OBJECTIVE.txt. Source hashac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210 is preserved. All writes are in this reviewer folder. No implementation, manuscript, scalar, timing, signature or attack is produced.

## 1. What T3 actually authorizes

**CITED — original task6.** The original goal allows a new parameter set only if the total bound fails at q=2^38, then asks for the smallest change in(a,k,d,h,ell,S) restoring128 bits with signature size and signing cost. It fixes n=16. The author's later conditional use target q=2^40 persists; evaluating q38 is not authorization to quietly replace that target. The goal also requests classical128 and a category1 quantum reading, while phrases such as total2^-128 and about2^64 queries do not specify one consistent work/success predicate.

**ASSUMED — three explicit interpretations, none silently chosen.** (A) literal tiny failure:epsilon(q,Q)<=2^-128 (and the quantum wording epsilon<=2^-64) at the stated budgets; (B) raw-query constant-success proxy: a sufficient envelope remains<=1/2 at Qclass=2^128 and Qquant=2^64; (C) actual category1/AES128 resource comparison under an explicit cost/depth model. A and B are useful formal test predicates but neither is automatically C. The proof obligation is to produce an adequate certificate under the selected criterion, not to relabel an exponent or declare a source attack from a failed upper bound.

**PROVED — current-ledger obstruction is parameter-invariant.** With n=16, modifying only(a,k,d,h,ell,S) leaves the source message/randomizer encodings and private128-bit seed sizes unchanged. In the reviewed joint-ledger route, the private/nonce/inner raw opportunities still give3Q/N and initiated honest inner opportunities still give2q/N, N=2^128. These nonnegative sufficient-expression terms alone make A impossible to certify at q38 even with Q=0:2q/N=2^-89>2^-128. At Qclass=2^128 the raw term alone is3, so B also cannot be certified by this ledger. The retained direct QROM private distance2Qquant/sqrt(N) caps at1 at Qquant=2^64; changing tree/FORS/WOTS parameters does not remove that obstruction. The finite hidden search route also caps there. This proves **no repair certificate through these unchanged terms**, not that no permitted construction can meet128-bit work security or that an attack exists. A new event-specific tighter composition or a rigorously justified raw-query/AES resource bridge remains possible.

**OPEN — original category criterion.** Category certification needs an explicit universal attack-resource comparison, including classical work and quantum gates/depth. Known implementation gate upper bounds are not lower bounds on all attackers. I verified NIST's primary evaluation-criteria page live; its category1 benchmark is AES128 key search with multiple cost/depth considerations, rather than a bare tiny-failure exponent or oracle count. Primary URL:https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post-Quantum-Cryptography-Standardization/Evaluation-Criteria/Security-%28Evaluation-Criteria%29. This does not add an unconditional fixed-SHA proof requirement to the original goal.

## 2. Source-valid admissible geometry

**PROVED — direct source guards, not hardware feasibility claims.** Let r=k−1 real FORS trees, t=2^a, d=number of layers and h=sum_i h_i. Retain FORS+C. Required nonoverflowing literal encodings include k>=2,1<=a<=31,r*2^a<=2^32, k*a+h<=256,0<=h_i<=31 and h<=63. The last condition is stricter than merely fitting a u64 index:tree_leaf evaluates idx>>(below+h_i), so total64 invokes an invalid64-bit shift at the top;65 needs a new representation. Each1u32<<h_i forbids h_i>=32. Layer IDs fit their one-byte encoding (d<=256; positive heights give d<=63). Tree IDs must fit64 bits and keypair IDs32 bits. h_i=0 is mechanically representable but is a degenerate layer, not a security repair by itself. Caches must remain a top segment for source key generation. Huge but finite arrays are not assumed physically available.

**PROVED — WOTS ell is not a free constructor field.** WotsC::new fixes lfull=floor(128/lw),w=2^lw,ell=lfull−z. With the original bases retained, lower ell<=32 and top ell<=16. Changing ell requires its corresponding z; omitted digits must still be checked zero, preserving the fixed-sum antichain/injective predicate. Changing w is outside the literal authorized list and must be identified separately. Meaningful positive-acceptance targets obey0<=S_i<=ell_i(w_i−1), with nonzero chain count for the ordinary one-time-key construction. Sum overflow must be excluded for other bases.

**PROVED — fixed scratch buffer is another constraint.** ctx.th has at most24 tail blocks and asserts that limit. For a PK/root compression with m16-byte nodes, ceil((22+16m+9)/64)<=24, i.e.m<=94. Thus r<=94 for FORS roots and ell<=94 for WOTS compression. Current bases already meet the WOTS guard. A mathematically legal digest/address candidate failing this constraint is a new implementation/representation variant, not unchanged-source retuning.

**PROVED — finite canonical counters and completeness.** Per WOTS row the acceptance probability is

    p_i = coefficient[x^S_i](1+x+...+x^(w_i−1))^ell_i / w_i^lfull_i.

The extra z digits are forced zero. C=2^32 is the source counter namespace. A row has bottom probability(1−p_i)^C; changing S to its extreme endpoint can make p_i as low as2^-128. Then one row completes with probability at mostC*p_i=2^-96, giving a nearly nonwinning setup/signing game. Such a choice is not a useful security repair. For an invoked top-cache row count m=2^h_top, independent rows give exact top-row completion(1−(1−p_top)^C)^m; this is a necessary component of meaningful setup completion, not the whole keygen law. A required completeness target tau must be stated before optimization. The source loop does not return a new bottom API; exhaustion is modeled as absorbing noncompletion.

## 3. Exact symbolic bytes, cache and call ledgers

**PROVED — serialized sizes.** For source-valid FORS+C with n=16:

    signature =20+16*r*(a+1)+4*d+16*sum_i ell_i+16*h bytes;
    public key=32 bytes; seed=48 bytes.

**PROVED — logical cache payload.** For cached layer i, above_i=sum_{j>i}h_j, the source stores2^above_i subtrees, each16(2^(h_i+1)−1) node bytes plus4*2^h_i canonical-counter bytes. Sum over cached layers. This counts logical payload, not vector allocation overhead, peak RSS or serialized container metadata.

**PROVED — compression ledgers, no timings.** Define c(m)=ceil((22+16m+9)/64). A FORS signing operation uses3*r*2^a+c(r) compressed-tail calls (includes the additional returned-secret PRFs); its public-key-only computation usesr*(3*2^a−1)+c(r). Verification usesr(a+1)+c(r). A WOTS PK costsell_i*w_i+c(ell_i); one full subtree costs

    C_sub(i)=2^h_i*(ell_i*w_i+c(ell_i))+(2^h_i−1).

With prepared cache, each WOTS signing layer costs1+ell_i+S_i (digest, secret PRFs, forward chain steps). With no cache addC_sub(i) plus the actual canonical grind count; canonical digest is reevaluated once by sign. For row acceptance p_i, expected evaluations **before success or finite bottom** equal[1−(1−p_i)^C]/p_i; on successful rows the conditional mean differs from1/p_i. Unbounded1/p_i is an upper bound on this bounded count, not a worst-case runtime. Message PRF/inner prehash costs depend on message length; the outer FORS grind has geometric mean2^a and finite noncompletion probability(1−2^-a)^C. No wall-clock extrapolation is supplied.

**PROVED — cache-preparation formula.** At cached layer i there are2^(above_i+h_i) leaves. Each costs WOTS PK plus its child computation plus canonical grinding. Its child cost is FORS PK at the bottom, zero if the immediately lower layer is cached, or C_sub(i−1) otherwise. Add2^above_i*(2^h_i−1) internal Merkle calls. A noncached top additionally needsC_sub(top) to construct its public root. These formulas expose the dominant preprocessing cost without generating any table.

**COMPUTED — final witness counts must change.** For the same source-valid acceptance/extraction geometry, direct final hidden opportunities are

    H_fin = r + sum_i[ell_i(w_i−1)−S_i];
    G_fin = r(a+1)+1+sum_i[ell_i(w_i−1)−S_i+1+h_i].

There are d canonical checks. Thus a prospective joint constant is

    C_joint = H_fin+G_fin+d+3
            = r(a+2)+2*sum_i[ell_i(w_i−1)−S_i]+h+2d+4.

The final3 is two inner charges and one seed-zero charge. Substituting original values gives3017/3217/6242. These are source call-count identities; transferring the complete joint theorem and QROM selectors/safe-surface law uniformly to every retuned set is **OPEN** and must be rechecked. It would be invalid to retain3017/3217 for a changed construction.

## 4. What can be called smallest, and useful alternatives

**ASSUMED — smallest is underspecified.** Plausible objectives disagree: (i) minimize number of changed coordinates and then L1 integer distance; (ii) minimize serialized signature growth; (iii) minimize hash-call/setup/cache costs at a fixed required completeness and signing cap. A Pareto set is preferable until an objective is specified. d/h edits additionally need an explicit layer-height vector; ell/S edits need per-layer choices and linked z. No scalar edit alone is a full parameter instance.

**COMPUTED — component-only alternatives, not128-bit repairs.** Increasing total height41→42 by top21→22 is a one-coordinate,+16-byte signature change and doubles the principal top-cache scale. Increasing k18→19 adds160 signature bytes and one real FORS tree's cost; increasing a9→10 adds272 bytes and roughly doubles FORS leaf work. These can improve the FORS coverage term but cannot remove the unchanged private/message-bound floor. At q41, h42 has essentially the same occupancy ratio as original q40,h41; a fresh binomial recomputation is needed rather than copying132.6 as an exact value. Changing WOTS targets toward the edge reduces verification chain counts but worsens canonical acceptance/completeness; reducing ell saves16 bytes per edited layer but introduces forced-zero grind work. None is certified as a smallest full-security repair.

**OPEN — smallest useful next obligation.** First fix the precise success/work/depth and completeness predicate. Then either prove a tighter parameter-uniform joint/QROM resource theorem (including unchanged private/message functions), or prove a universal lower resource conversion to AES128. Only after that optimization can source-valid(a,k,d,h,ell,S) candidates be certified. Existing ordinary-component hardness symbols remain unevaluated. Merely optimizing per-candidate FORS exponents solves a smaller problem.

**ASSUMED / separate extension, not authorized repair.** Increasing n changes the fixed object and implementation: Node, seed/public-key sizes, truncation, precomputed public block, message formats and compressed-tail costs. At n>16 the present constructor still hardcodes128-bit WOTS digits; a clean variant needs a new specification and proof. n=17 can reduce some constant-success oracle-bound floors, but is neither a proven smallest full repair nor an actual source-valid choice. For literal tiny failure at Qclass=2^128, even the isolated3Q/2^(8n) term requiresn>=33; SHA256 cannot supply33-byte output nodes. This is a certificate obstruction for that expression/criterion, not an impossibility result for every design or a requirement to enlarge n.

**OPEN — outcome.** No permitted parameter-only full-security repair is certified by the current unchanged source message/private ledger. Source-valid symbolic repair constraints and costs are derived; a scientifically honest output remains “not established” until the missing criterion/resource or sharper-composition obligation is solved. The original complete-security goal remains active.

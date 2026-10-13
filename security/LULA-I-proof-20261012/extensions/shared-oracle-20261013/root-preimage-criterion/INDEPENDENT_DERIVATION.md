# Source-first root-preimage investigation of the requested quantum criterion

Saved independently before reading any root candidate on this topic. **Status: MANUALLY_DERIVED_SOURCE_MODEL_CRITERION_OBSTRUCTION.** The fixed128-bit root admits a source-valid final-sibling search with constant winning probability at about2^64 complete quantum hash queries. Thus demanding failure probability at most2^-64 against that budget is incompatible with this unrestricted random-oracle verifier model. This is the expected square-root preimage scale; it is not evidence of a practical forgery, a new cryptanalytic weakness or failure of conventional128-bit classical work-factor security.

## 1. Literal source subject and public checks

Pinned `release/code/lula1/src/lib.rs` SHA256: `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Original driver parameters are

    18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1.

No parameters or source files are changed. N=2^128 denotes the number of16-byte nodes, rather than the source's byte-width constant N=16. All complete hash images have256 bits; only the first128 bits are compared as nodes/root.

`verify_root` at679–730 checks the5720-byte length, the FORS zero coordinate at702–703, and five WOTS+C accepted digit vectors at719–723. It reconstructs every supplied secret/path and chain value publicly. It never checks that a supplied authentication sibling belongs to a pre-existing authenticated tree, or that a chain value was output by honest Sign, except through the ultimate root equality at672–673. This is normal Merkle verification structure.

The adversary makes **zero signing requests**. It may choose a fresh one-byte message m and transmitted R=zero16. The inner raw word R||S||root||m has length49, and the outer words U||BE32(c)||S have length52. These restrictions are disjoint from all addressed key-graph words (minimum length102), even for zero S. The chosen-message freshness predicate is automatic at q_s=0.

## 2. Public skeleton satisfying every earlier check

1. Compute U from the public inner word. Search counters0,...,L-1 for an outer digest whose omitted eighteenth9-bit coordinate is zero. Fix that accepted digest, its17 real indices, and41-bit route idx. This is a public1/512 filter; there is no private message-randomizer check.
2. Fill all17 FORS secret blocks and all9 siblings per tree with zero16. Compute their public leaf/path roots with `pk_from_sig` at396–412 and compress those roots. No correctness predicate is applied to these blocks before the eventual root comparison.
3. For each of the four lower WOTS layers, grind a public type7 counter until the32 base16 digits sum240. Fill all32 transmitted chain nodes and the five siblings with zero16. Public chain completion, endpoint compression and path reconstruction determine the next child value. These computations need no secret.
4. For the top layer, grind its type7 counter until the16 base256 digits sum2040. Fill all16 transmitted chain nodes with zero16. Reconstruct its WOTS PK, and supply zero16 for the first20 top authentication siblings. Leave the21st/last sibling as an arbitrary variable X in{0,1}^128.

On successful preprocessing, all parser, zero-filter and WOTS checks pass for every X. The root computed after that last sibling is the only remaining acceptance predicate. The prefix is deliberately not an honest signature; its legitimacy is precisely what root verification tests.

Exact serialized layout, zero-based byte offsets:

| Component | Bytes / interval |
|---|---|
| R and FORS counter |20 /0..19 |
|17 FORS proofs,16+9*16 each |2720 /20..2739 |
| Four lower blocks,4+32*16+5*16 each |2384 /2740..5123 |
| Top counter |4 /5124..5127 |
| Top16 chain nodes |256 /5128..5383 |
| First20 top siblings |320 /5384..5703 |
| Last free sibling X |16 /5704..5719 |

The parameter route formula at470–475 gives top tree0 and leaf=(idx>>20)&(2^21-1). At the final path step, the direction bit is (idx>>40)&1. Let V be the fixed value after the first20 top path hashes. The last address is exactly

    A*=Adrs::new(4,0,T_TREE=2).w2(21).w3(0),
    encoded22 bytes: 04 || zero8 || 02 || zero4 || 00000015 || zero4.

The raw root candidate word is

    Z_X=S16||zero48||A*||(V||X),  if the direction bit is0,
    Z_X=S16||zero48||A*||(X||V),  if the direction bit is1.

Both have length118. They are injective in X. Source `root_from_path` at322–327 gives precisely these orientations; the last node index is zero because the top subtree has height21. Acceptance is Tr128 RO(Z_X)=public root. The remaining128 output bits are ignored by this predicate but retained by the complete-output query oracle.

## 3. Completion and explicit public query budget

For ell digits of width w and target sum s, the accepted128-bit-vector count is

    Count(ell,w,s)=sum_j (-1)^j binom(ell,j)*binom(s-j*w+ell-1,ell-1),

with terms only when s-j*w>=0. Define p_l=Count(32,16,240)/16^32 and p_t=Count(16,256,2040)/256^16. Both are strictly greater than1/1024; the exact integer cross-multiplications are checked in the accompanying control.

Set the attacker preprocessing cap L=2^20, below the unchanged32-bit counter range. For each fixed current child, its own type7 counter row consists of independent images before any queries to that row. Four lower rows have the unconditioned law. If a top row is the honest cached canonical-child row and the challenger conditions on completed cache setup, conditioning it to contain at least one accepted counter among C=2^32 can only improve the probability of success in its first L counters:

    Pr(no first-L acceptance | some first-C acceptance)
      = [(1-p_t)^L-(1-p_t)^C]/[1-(1-p_t)^C]
      <= (1-p_t)^L.

Other-child top points remain independent residual images. The skeleton's current child is computed without querying this own type7 restriction. Thus preprocessing succeeds with probability at least

    alpha_L >=1-(511/512)^L-4(1-p_l)^L-(1-p_t)^L
            >=1-6*(1023/1024)^L >31/32.

This is an analytical completion bound, not a measured runtime or a universal source abort statement. The attacker simply abandons a failed preprocessing attempt; no retry is hidden in the budget.

The fixed accepted sums imply exactly3000 chain-completion calls. The whole source final type0–4 graph reconstruction uses3217 calls; omitting its final root call leaves3216. Preprocessing therefore uses at most

    Q_pre <=1+6L+3216=6L+3217.

The1 is the inner digest; the six grind rows comprise the FORS outer filter and five WOTS type7 rows. Accepted digests may be stored without rehashing. The complete challenger verifier uses3217 graph calls, five type7 calls and two I/E calls, hence3224 full-hash calls. Hash-compression counts are different quantities.

If the unconditioned challenge itself uses original top-cache KeyGen, its2^21 independent type7 rows finish with probability

    tau_top=[1-(1-p_t)^(2^32)]^(2^21)>31/32.

The source child graph is built without its own type7 row; each row's acceptance probability is the same constant. Setup completeness is therefore independent of the root-address residual table used below. Its finite-row failure bound describes partial semantics, not a new total source API. The source keygen at512–540 and cache parameters support this row count. Honest keygen queries are not adversarial Q; no setup-time measurement is inferred.

## 4. Conditional RO law at the last-root address

Honest graph construction queries A* only at its one canonical pair (L*,R*) to form the top root, possibly repeating that same point. It does not query arbitrary root-pair payloads. Our skeleton preprocessing never queries A*: its top hashes stop at height20, its other addresses/types differ, and its I/E lengths are49/52. It may depend on the public root and outside-table responses, which does not inspect A*'s residual entries.

Condition on the honest source graph, its root, completed setup, and the entire successful public preprocessing history. The A* residual full256 outputs are still independent uniforms. If fixed V is the appropriate canonical root child, the X family contains one already programmed canonical point with a guaranteed matching prefix; otherwise it contains no such point. In both cases all other family prefixes match the target independently with probability1/N. For the number M of marked X,

    M~Bin(N,1/N),                 if the canonical point is outside the family,
    M~1+Bin(N-1,1/N),             if it is inside the family.

In **either** case,

    Pr(M=1)=(1-1/N)^(N-1)>1/3.

The graph is analysis-only conditioning, not advice given to the attacker. The attacker does not need to know which case holds or whether M=1. Full-image suffixes stay uniform and are consistently queried/uncomputed. This source-specific residual-law lemma, rather than a heuristic “128-bit root means64-bit quantum”, is the necessary bridge.

Classically, t distinct public candidate calls succeed with probability at least1-(1-1/N)^t, conditional on successful preprocessing. If the t candidates include the canonical point success is certain; otherwise each is residual. This is a lower bound, not a guarantee that one fixed family always has a preimage: the first case can have M=0 with probability near e^-1.

## 5. Explicit Grover query argument, without an M promise

Prepare the uniform128-qubit superposition over X. A marking phase for Tr128 RO(Z_X)=root is implemented by one complete-output XOR call, a reversible prefix comparison/phase, and a second XOR call to uncompute. It costs **two** ordinary full256 RO queries. Framing, comparison and diffusion are public reversible operations. This is not a free Boolean query or compression-function oracle.

For any realized M, after T iterations the success probability is

    sin^2((2T+1)*arcsin(sqrt(M/N))).

This is the standard exact amplitude-amplification identity, [Brassard–Hoyer–Mosca–Tapp, arXiv:quant-ph/0005055](https://arxiv.org/pdf/quant-ph/0005055), Eq5/Eq8 and the paragraph following Eq8 on physical pages6–7. Its full primary PDF was read via the browser. The [original Grover paper](https://arxiv.org/abs/quant-ph/9605043) supplies the database-search context. No hash-signature QROM upper-bound theorem is substituted here.

Choose T based on N and the public budget, not on M. Restrict the lower-bound analysis to the event M=1 and discard nonnegative success from all other M. Therefore

    Pr(quantum root hit | successful setup/prefix)
      >=(1-1/N)^(N-1)*sin^2((2T+1)*arcsin(1/sqrt(N))).

An optional one-query classical check after measuring X confirms the root before output. It is already covered in the budget below. Any hit gives a full5720-byte accepting fresh-message forgery in this ordinary-RO source model; no signing query or rollback is required.

For a fully conservative total of adversarial preprocessing/search/certificate **plus the3224 final verifier calls**, let

    B=(6*2^20+3217)+1+3224=6297898,
    T=floor((2^64-B)/2).

Then total complete hash calls are at most2^64. Honest KeyGen's work is separately the challenge setup, as in the current QROM game. The success angle lies between0.99 and1.01. Using sin(theta)>=theta-theta^3/6 gives sin(theta)>4/5 in that interval; the exact rational endpoint inequality is checked. As Pr(M=1)>1/3, alpha_L>31/32 and, for the unconditioned original KeyGen experiment, tau_top>31/32, the overall modeled success is strictly greater than

    (31/32)^2*(1/3)*(16/25)=961/4800 >1/5.

When the challenge conditions on completed honest setup, omit tau_top; the lower bound is stronger. Thus the requested probability at most2^-64 at a budget around2^64 is refuted in this finite coherent full-RO model for the unchanged128-bit root. The actual gigantic search was not run.

## 6. What this does and does not settle

The obstruction concerns the literal **small advantage at a near-square-root query budget** criterion. Classical exhaustive target preimages cost about2^128 queries; quantum amplitude amplification costs about2^64 queries. That behavior is consistent with the usual use of128-bit classical hash output strength and does not by itself disqualify conventional category/level claims. No category is certified here, and no physical-runtime estimate is made.

The proof is manual and source-specific. The smallest remaining review lemma is that the successful publicly assembled prefix uses no residual A* query and the key-generation graph queries A* at only its one canonical pair. The exact directions, full raw framing, type7 completion conditioning and final verifier-call accounting are stated so another reader can check that lemma rather than accept a generic root heuristic. A machine-checked refinement to the Rust parser/channel and any actual SHA-256 forgery remain unperformed. No new source parameters, huge benchmark, attack run, paper update or existing theorem edit is part of this investigation.

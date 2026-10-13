# Ordinary private-PRF adapters for one fixed public hash algorithm

Status: PROVED_SOURCE_RELATIVE_EXACT_ADAPTER_IDENTITIES; FAMILY_HARDNESS_ASSUMED; MANUAL_REVIEW_PENDING. This first argument was saved before reading any new peer candidate for this task. It is a different model from the external shared random-oracle programs. It changes no source, paper, scalar, or prior receipt.

## 1. Precise claim and public algorithm

Fix a deterministic, publicly described full-output algorithm h:{finite byte words}-> {0,1}^256. Its description, implementation, and a clean reversible implementation are public. A classical or quantum adversary may compute h locally. There is no independent Raw oracle in the PRF challenge, no random selection of h, and no ability to program its replies. For source binding, h is the SHA-256 algorithm represented by the release hash routines, not a sampled SHA-looking function.

Write t16 for the first 16 bytes. Let S,K,P be independent uniform 16-byte words. S is a public parameter, K and P are private keys. For a 22-byte address A define

    f_K^S(A) = t16 h(S || zero48 || A || K),
    g_P^S(M) = t16 h(P || S || M).

The private query outputs are exactly 128 bits. Their PRF challenges do not need unused lower limbs of a 256-bit hash response. The complete 256-bit public h remains locally computable everywhere, including on words equal to either private frame.

Define an ordinary public-parameter PRF challenge for f: independently choose S and K, give S and a single private function interface Eval_f to B, and in REAL let it evaluate f_K^S; in IDEAL let it evaluate one independent lazy random function F from 22-byte addresses to 16-byte words. No side oracle is supplied. The analogous challenge for g independently chooses S,P and uses g_P^S versus a memoized independent random function J on the bounded message domain. An implementation may use the fixed valid type-5/type-6 address domain instead; the reduction queries only that domain. Advantage means absolute difference of output-one probabilities, without a factor of one half.

For each fixed S the same definition is an ordinary keyed family f^S or g^S. The public-parameter challenge above averages those conditional probabilities over the independent public seed. Alternatively a theorem may assume a worst-case advantage bound over S. Neither interpretation is an externally sampled-oracle PRF notion.

Hardness of these particular families is ASSUMED. Naming them PRF families gives no proof of pseudorandomness of this SHA-256 composition, no cipher-security certificate, and no numerical bound by itself. A quantum distinguisher with only classical Eval_f/Eval_g calls is sufficient for the source adapters (post-quantum, classical-query PRF). A coherent private-query PRF assumption is stronger and may also bound these programs, but the source services do not require coherent private queries.

## 2. Source experiment and exact byte binding

The immutable release source is `publications/LULA-I/release/code/lula1/src/lib.rs`, SHA256 ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. Relevant definitions are Ctx::new/th/prf/prf_msg/hmsg_inner/hmsg_outer, WotsC::sk/pk/sign, Fors::tree/sign, Signer::keygen/child_value/sign, and verify/verify_root. Ctx::prf returns a Node (16 bytes) from the typed hash of sk_seed. Ctx::prf_msg returns the first 16 bytes of SHA-256(sk_prf || pk_seed || M). The optimized public-seed midstate depends only on S. Intercepting every private call therefore requires neither unknown key in a placeholder context.

The three games use this SAME fixed public h throughout:

* SrcReal_h: both private functions are f_K^S and g_P^S.
* SrcFideal_h: secret-address values come from an independent F; the randomizer is still g_P^S.
* SrcFJideal_h: both F and J are independent random functions with 16-byte outputs.

All nonprivate source calls and all adversarial public-h computations still use h, with their complete byte frames. In particular the message inner hash uses R || S || root || M and returns the full word; the message outer hash uses that 32-byte word || counter4 || S and returns the full word. Typed node hashing uses S || zero48 || address22 || payload. These functions are not replaced by independent maps.

The source experiment has an obligatory top-prepared setup. Success is required only to release pk=(S,root). An adversary's pre-key phase has the public h code but receives neither S nor pk and has no private/signing service. Save its continuation, perform setup, then resume it with pk. Use one total adversarial runtime/public-h-use cap across both phases. Independently presampling S and the other key before the pre-key phase is equivalent to deferred sampling, because these values are not disclosed and cannot change the fixed public h algorithm.

At most q initiated signatures are served atomically. Seen records exact requested message bytes. Setup and counter searches are partial source computations. For the decision experiment, at most 2^32 distinct counter attempts are made; noncompletion yields absorbing nonwinning output 0. This totalizes the partial cryptographic game and is not a claim about native Rust overflow, panic, or successful termination. Honest consistent caches and honest restorations preserve logical values. Private keys, cache bytes, timing, internal full-hash transcripts, and seed files are not exposed. Final acceptance is m* not in Seen and verify_root(pk,m*,sigma*)=pk.root with the source parser checks. The final verifier calls neither private function.

## 3. Ordinary reduction B_K

Receive S and Eval_f from the ordinary f challenge. Sample P independently. Initialize a dictionary with complete 22-byte address keys. On secret(A), call Eval_f(A) only on a dictionary miss, store its 16-byte response, and return it. On randomizer(M), compute t16 h(P || S || M) locally; deterministic memoization is optional. Compute every other complete public hash locally with the SAME h algorithm. Unknown K is never reconstructed or inserted into a frame by B_K. A context placeholder's sk_seed is unreachable because every source prf call is intercepted.

Run the pre-key/setup/resume/sign/final-verification program of Section 2. B_K knows S because its challenge supplies the public parameter; its source-facing interface withholds S until setup completes. A receives exactly the permitted source views. Its direct uses of the public code h, including coherent uses, are unaffected by this wrapper. Return the source Win bit.

In REAL, the private response at every address is exactly t16 h(S||zero48||A||K), and locally computed randomizers/public hashes are exactly their source values. In IDEAL it is exactly the independent F value. By induction on classical source service calls, interleaved with the unchanged quantum adversary computation if applicable, the complete source-facing view has the law of SrcReal_h or SrcFideal_h, respectively. Memoization is immaterial because both challenge interfaces are functions. Thus

    |Pr[SrcReal_h Win] - Pr[SrcFideal_h Win]| = Adv_PRF(f; B_K).

The equality includes pre-key computations, source partiality, repeated messages, full public-h responses, and all literal frame aliases. It is unconditional over S, including S=0. If two private or public frames coincide, REAL values agree because both arise from the same public h code. IDEAL private replacement intentionally removes that correlation; the ordinary family distinguisher pays for precisely that difference. No extra S=0 exclusion, key-distinctness conditioning, or public-h correlation lemma is needed in this identity.

## 4. Ordinary reduction B_P

Receive S and Eval_g. Initialize an independent lazy 16-byte map F on complete valid addresses and a message-keyed dictionary jcache. secret(A) returns F[A]. randomizer(M) on its first access stores Eval_g(M) and thereafter returns the same 16-byte value. All other public hashes and every direct adversarial computation use the SAME fixed h code. K is unused; unknown P is never read or used to construct a public frame. Intercept every source prf_msg call.

Run exactly the same phases, Seen handling, absorbing noncompletion, and strict final verification as B_K. At REAL the law is SrcFideal_h; at IDEAL it is SrcFJideal_h. Therefore

    |Pr[SrcFideal_h Win] - Pr[SrcFJideal_h Win]| = Adv_PRF(g; B_P),
    |Pr[SrcReal_h Win] - Pr[SrcFJideal_h Win]|
        <= Adv_PRF(f; B_K) + Adv_PRF(g; B_P).

The triangle bound has no selector loss and no secret-namespace factor. Its private-query parameters are those of these concrete distinguishers, rather than the adversary's public hash count.

Before the first query at a fresh message label in SrcFJideal_h, J[M] is uniform and independent of the then-existing public history and F. Repeated messages reuse J[M]. A returned signature explicitly reveals R=J[M], so independence from the posterior signature transcript is not asserted. Different labels can produce equal 16-byte random values.

## 5. Inherited complete call accounting

The immutable reviewed `PRIVATE-REDUCTION-PROGRAMS.md` (feff3d899edcb0b675970eaf915c221d837a47ab7357828758f0f0a40c923f89) supplies the source-relative call caps; changing from an external public RO to deterministic public h does not alter the reference call graph. These are whole function calls, not compression counts, timing measurements, or an independent re-audit of the complete implementation.

Let N_D=19,212,937,084,272,640. Setup has U_setup=2,181,038,080 private secret invocations and distinct addresses. A cold sign has at most U_cold=33,567,232 distinct addresses (33,567,393 invocations); a prepared sign has U_hot=12,816 distinct addresses (12,961 invocations). Therefore B_K's private challenge query count and B_P's F-map size satisfy

    D <= min(N_D, U_setup + q U_mode).

B_P makes at most q Eval_g queries. Counts include an initiated request that subsequently fails; final verification adds zero private queries. Restoration does not reset the reduction's dictionaries. Repeated source computations return the same function values.

Put L=2^32,

    H_setup = 2^21 (19505 + L) - 1,
    H_hot   = 82090 + 5L,
    H_cold  = 8,560,574,463 + 82090 + 6L.

Nonprivate source calls through final verification have cap R_src=H_setup+q H_mode+3224. B_K additionally computes at most q REAL randomizers locally, so its complete honest local-h cap is R_src+q. B_P has cap R_src and separately q private challenge calls. The 102-byte private f frame is evaluated inside the challenge in B_K, not counted again as a local public-h call. The g frame has length 32+|M| and is evaluated locally only for B_K. Neither private challenge produces a full 256-bit secret output.

If Q_A public-h subroutine invocations are explicit in A's circuit description, they add to local h execution resources in both phases. Any further inlined h computation is charged to t_A, not silently assumed absent because it bypasses a named Raw method. There is no oracle-guess bound obtained from Q_A. In the quantum case A's public-h subroutine is a clean reversible circuit for the same deterministic function, with a matched fixed extension on invalid physical input encodings. Private signing calls remain classical.

## 6. Time, workspace, and concrete compilation

Let b be an ex-ante maximum complete public input length covering the source frames and the finite adversary circuit's input registers; it includes 598-byte typed WOTS compression frames and every possible message frame. Let C_h^cl(b) bound deterministic complete evaluation of public h, and C_h^q(b), W_h^q(b) bound clean coherent gate count and workspace. These are properties of the publicly specified implementation. They are not zero-cost oracle operations. If a clean circuit is uniformly generated, its generation cost is charged once; bit serialization of indexed gate labels is distinct from emitted gate-record count. Let C_build(b) denote that cost in the chosen metric.

An explicit conservative reduction cost, excluding execution of the private challenge, is

    t_A + C_build(b) + Q_A C_h^q(b)
        + (H_setup + q H_mode + 3224 + q) C_h^cl(b)
        + O((I_secret + R_src + q + 1)*(b+64+log(D+q+2))
             + M*(1+log(q+2)) + 5720q),

where I_secret=U_setup+q times the mode's private invocation cap, and M is the total length of initiated and final messages. The last q complete hashes may be omitted for B_P. The expression is an envelope for a balanced dictionary and source loop/bookkeeping, not an exact optimal implementation or wall-clock bound. A's inlined h computations must not also be charged as Q_A calls if already included in t_A; choose a disjoint accounting convention.

Auxiliary source-facing storage can be bounded by O(38D + M + 5720q + 75,497,456 + 64*2^22 + 64*17*1023) bytes plus dictionary indices, A's workspace, public-h circuit workspace, and an O(q) message index. Here 38D includes 22-byte address keys and 16-byte private values. The generous top-vector allowance covers setup intermediates. Message table values are 16 bytes plus message keys. No full random-function domain, 19-quadrillion-address forest, or full256 private table is materialized. Classical source work may be enormous but is finite relative to the configured source service; no practical cost claim is made.

Public-seed SHA midstate preparation in Ctx::new is an implementation optimization. The adapter can instead evaluate each complete concatenated h word, giving the same outputs and already charged complete-h cost. This is value-level source refinement only; execution timing and hash instrumentation are outside the experiment. Source threads are serialized deterministically in the reference cryptographic program.

## 7. What this closes and what remains open

These programs establish exact ordinary public-h PRF hybrid identities, including classical and quantum adversaries with classical private services, assuming the stated private families are hard to distinguish with their explicit resource budgets. They do not assert that fixed SHA-256 satisfies those assumptions.

SrcFJideal_h still uses fixed public h. A PRE/TCR or final-forgery analysis for this game is a separate obligation. The earlier finite external-RO/QROM result is a different experiment: its Raw function is independently sampled and shared with its restrictions. Its key-guess bounds, source patch arguments, numerical residual terms, and whole-security theorem are not transferred here. No ordinary/public-fixed-h identification of those public primitive assumptions is supplied by the two private adapters. The stronger whole security, resource-feasible numerical certificate, proof-assistant implementation refinement, and category certification remain open.

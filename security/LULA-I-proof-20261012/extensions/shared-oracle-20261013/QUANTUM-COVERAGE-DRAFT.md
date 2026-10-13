# Sequential quantum coverage — synthesis candidate, not promoted

**OPEN — two source-derived reviews required.** Root synthesizes its own dynamic nonce-overlay and final-event reasoning with the independently verified GHHM adaptive-reprogramming theorem and the peer-derived coherent full-row lookup. This is not a claim of blind independence from those primary-theorem/circuit messages. The new multi-call construction, query ledger and final search reduction below require review. Full QROM totals remain null.

## 1. Source experiment and disjoint planes

**ASSUMED — common game.** Use ordinary JOINT F/J ideal HJ, fixed nonzero S, independent full256 public RO, classical atomic honest source services, q initiated signing requests across branches, Q coherent adversarial full-hash calls, and a classical final signature. Finite raw strings are injectively length-encoded. No timing, private cache bytes, private hash transcript, coherent signing or interruption is supplied. Noncompletion is absorbing/nonwinning. The code pin is ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210.

**PROVED — literal domains.** The inner plane consists of R16||S16||root16||m. Every point fixes its label m and candidate R. For each label, R_m=prefix J(m) is uniform; repeated labels reuse it. The graph/root uses addressed planes with zero bytes16–31, disjoint on S!=0. The eligible outer plane consists of U32||counter4||S16 with U[16:32]!=S. It is disjoint from the entire inner plane. Outside points retain their one shared function semantics. A source or final U having U[16:32]=S must be handled as an exceptional event, not assigned an independent outer oracle.

## 2. Global inner nonce sampler and predictable overlay

**PROVED — source marginal candidate.** Conditional on J and the graph, sample independent full256 U_m for every allowed m and a residual inner table I_0. At I_m=R_m||S||root||m program its full image to U_m. The I_m are injective in m even when R repeats. The resulting whole inner function is ordinary uniform conditional on J: selected points and residual points all have independent full images. Thus its full joint distribution with the actual R_m is the source inner plane's distribution.

**PROVED — guarded source controllers candidate.** REAL_I uses this fixed programmed function for adversarial queries. GHOST_I uses I_0 at unexposed nonce points and overlays I_m->U_m after completed signatures at m. Both services compute their honest inner value directly as U_m and use the same eligible outer function/graph for the remaining source computation. If an initiated call has U_m's lower half equal to S, both guarded controllers flag B_U and stop BEFORE its outer search, since its excluded outer point could alias another unexposed inner label. This stop preserves C-and-no-B_U and the first-B_U event of ordinary HJ. It is an analysis device, not a production abort API.

The ghost's remaining nonce R_m are unused by its query unitary. Overlay images U_m are independent of other unexposed R values. Honest metadata/outer calls on nonbad U are outside the inner plane; completed disclosure of R_m,U_m updates only that label. The source's first counter, subtree proof and termination tests therefore supply common classical channels. The stopped guard depends on U_m, not an undisclosed nonce. Packing common services between Q query slots gives purified vector gap<=2Q/sqrt(N), N=2^128. This requires the same stopped/active-history care as the reviewed dynamic hidden lemma; it is a NEW application and must be independently validated.

**PROVED — candidate guard bound.** In the continued ghost sampler each newly requested label's U_m is uniform and unused before that request; repeats add no new draw. At most q independent latent U values can nominate the exceptional half. A stopped terminal B_U examiner and an unflagged ghost continuation give p_ghost(B_U)<=q/N. With the packed vector bound,

    p_HJ(B_U) <= min(1,(2Q+sqrt(q))^2/N).

No completed-signature or no-guard conditioning is used. Failed honest guards are recorded and absorbing.

**PROVED — lazy-U equivalence candidate.** In GHOST_I, unrequested U_m are not read by its public query responses, graph or other services. Consequently each NEW classical message can be assigned a fresh U lazily, storing it for repeats. This is the exact marginal of iid per-label U values, even when m is selected adaptively from quantum measurement history. On a successful guard coin, U is uniform on G_S={U:U_lower!=S}, of size M_good=2^256−2^128. A failed guard coin has probability1/N and can terminate the simulated branch. This is per-call sampling with an explicit failure branch, not a normalization on global successful execution.

## 3. Row-valued RO and actual adaptive-reprogramming costs

**CITED — primary bound.** GHHM, Tight adaptive reprogramming in the QROM, arXiv2010.15103v2, Figure2/Theorem1 Eq(2), bounds the event-distance over R instructions by sum_r[sqrt(Qhat_r*p_r)+(1/2)Qhat_r*p_r], where Qhat_r counts preceding function queries and p_r bounds the maximum sampled input probability. Outputs are resampled uniformly on their finite full output alphabet. The returned instruction data include the input, not the newly sampled value. Its exact source PDF SHA is9a5ea6adeba5dcdf6c80035057aaccdc704aa6ea2940af0320bcfd7eca0abc8d.

**PROVED — row interface candidate.** Define ROW(U)=(O(U||BE32(c)||S))_{0<=c<2^32} on U in G_S. Its codomain is a full tuple of independent256bit words, not an accepted digest. Different rows are independent. A raw selected-counter XOR call can be simulated with ONE row-XOR query: initialize every unselected256bit response slot to |+>, coherently swap the real response register into slot c, query ROW, swap back. The other slots are invariant under XOR and return clean. Ineligible raw branches use invariant plus slots. This requires a finite but enormous2^40bit auxiliary register; no efficient/PPT implementation is claimed.

**PROVED — indispensable honest-query ledger candidate.** At each new-message instruction, the source simulator needs its fresh whole row to locate the first accepted counter and compute the same signature. Since the AR interface does NOT return the fresh row value, the simulator makes one POST-instruction row query to read it. Those reads count toward preceding Qhat for later instructions, even though the original honest scalar signing work is not adversarial Q. At most q such reads occur. Cached row values can serve repeated messages and known-row collisions without further reads; all external raw queries still consume at most Q row queries. A safe bound is Qhat_r<=Q+q+1 and at most q instructions, so

    Delta_row <= min(1,
      q * [sqrt((Q+q+1)/M_good)+(Q+q+1)/(2*M_good)]).

Omitting the q honest row reads would be an invalid sharper instantiation. The extra1 is a conservative endpoint allowance. Reprogramming only on new message labels preserves their inner assignments; repeated messages request no zero-entropy AR sample.

**PROVED — programmed-game interpretation candidate.** In the reprogrammed game each activated row is a fresh iid full tuple. Its first zero-filter digest has an independent uniform bucket/17-index tuple X_i, independently of the rejection counter; a failed row remains a noncompleting request. If a later new message happens to use an old U, its fresh row overwrites that prefix in this analysis game. This does NOT claim that the real signer changes hashes or is nondeterministic: the AR distance pays that game change. The latest stored row at each U determines later repeats. Every observed route is among the at most q independent row-template tuples, including collisions/repeats, so padding to q latent iid X_i is an upper bound. An alternative proof charging U-collisions may be used, but they cannot be silently ignored.

## 4. Query-bounded final event in the programmed ghost

**PROVED — tentative independent advice.** Presample q latent U_i, q row templates (including failure/first-accept metadata) and q padded uniform X_i; store fresh-message assignments only as the controller runs. These exogenous values and the outside BASE functions are independent of each search challenge. Adaptive message labels/queries are NOT fixed as independent advice; the simulator generates their state updates using its own challenge-query history. Do not condition on arbitrary logs. The final coverage table T_q from all padded X_i dominates actual disclosed index sets.

Let p(T_q) be the covered raw digest probability, including the zero filter. The reviewed independent-stream expectation identity gives E[p(T_q)]=p_F(q), with the exact binomial occupancy model. This identity is used only after the source-to-programmed-game bridge is justified.

**PROVED — fresh outer branch candidate.** If the final U is eligible and not any previously programmed namespace, its outer response is a BASE full256 image independent of T_q. Factor its covered predicate by iid Bernoulli marks of density p(T_q), with independent covered/noncovered full-value pairs. Known-row patches and other-domain responses are simulated from their advice/controller state; honest programmed signatures require no mark query because their templates are already given here. The clean one-Boolean-query simulation and observable final outer point use at most Q+1 mark queries. Average-search yields

    p(covered eligible fresh-row final point)
       <= min(1,8(Q+2)^2*p_F(q)).

This is not classical candidate padding with Q replaced by Q^2. It explicitly constructs an output-search algorithm. The q whole-row reads charged in AR are not free raw quantum calls in this reduction: here those new templates are independent advice, while the original adversary still has only its Q raw calls.

**PROVED — final inner exceptional branches candidate.** A fresh final message cannot use a known programmed inner point: fixed-width framing includes its message label. Thus its ghost inner image is a BASE uniform full256 image. Quantum search for either a lower half equal to S or a full image equal to one of the at most q latent programmed U_i has density at most1/N+q/N^2. Their target lists can be given independently of that BASE inner function; actual adaptive assignment labels are simulated, not conditioned on. Known-inner patches use independent stored U values and are excluded for the fresh final label. One final inner query gives

    p(final excluded-half or old-namespace event)
       <= min(1,8(Q+2)^2*(1/N+q/N^2)).

Giving the whole BASE inner table would invalidate THIS search argument. It may be independent advice in the separate outer-coverage search, but the two enlarged views must not be merged into one collision-search game.

Combine these branches and the AR distance to obtain the proposed programmed-ghost envelope

    A_C = min(1, Delta_row +
                   8(Q+2)^2*(p_F(q)+1/N+q/N^2)).

## 5. Candidate source coverage envelope and open gate

**OPEN — not yet promoted.** The IO comparison's terminal C examiner may need both final inner AND outer calls, because an excluded outer input can lie in the inner plane. Conservatively count two additional coherent slots. Applying the same square-root success inequality to C-and-no-honest-B_U, then separately paying the honest guard event, proposes

    p_HJ[C] <= min(1,
        (2Q+sqrt(q))^2/N
        + [2(Q+2)/sqrt(N)+sqrt(A_C)]^2).

This is a candidate source-bound quantum FORS COVER event, not yet a full QROM forgery theorem. Every partial-completion/guard/late-reveal transition, the lazy-U law, the AR qhat contract, and the conditional search factorization must pass independent review before this term is summed with the already reviewed H/G/D7 events and the private-hop loss. Plain Grover reading, category certification and parameter repair are separate conclusions.

**OPEN — smallest review targets.** Validate global nonce marginal with a root determined outside the inner plane; packed nonce-query invariant after classically guarded services; metadata-only completion and new-vs-repeat labels; exact finite ROW AR API (fresh value not returned); preservation of raw-query count in its plus-slot simulation; exogenous templates under collisions/abort; no challenge-dependent adaptive logs used as advice; and actual fresh-message final witnesses for both inner and outer searches. A failed item must leave the total null, not be replaced by zero.

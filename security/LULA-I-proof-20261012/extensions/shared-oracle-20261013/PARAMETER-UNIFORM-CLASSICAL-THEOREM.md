# Guarded parameter-uniform classical source theorem

**PROVED — manual theorem, subject to exact independent final review before promotion.** This is a uniform extension of the reviewed complete classical joint construction, not substitution into a baseline formula. It preserves the actual shared full-output random oracle, the atomic partial source interface and the strict verifier. No manuscript, cryptographic implementation, historical theorem or historical scalar is changed. A proposed parameter tuple denotes the guarded source-algorithm schema; no retuned executable is claimed.

## 1. Object, quantifiers and representation guards

**ASSUMED — experiment.** Fix parameters p before all oracle, key and adversary coins. Let K,P,S be independent uniform 128-bit seeds. The public primitive is one complete random function from byte strings to 256-bit words. Its outputs, including lower limbs unused at some source calls, are shared literally by all call sites. A classical adversary has at most Q raw evaluations, including pre-key evaluations, and q initiated atomic signing calls. Final strict verification is included in the experiment, with its separately charged final calls. Signing and key generation can fail to complete a finite counter search; actual invoked noncompletion is absorbing. Only completed signing replies are exposed. Fresh-message acceptance is Win. Private/cache bytes, timing, coherent or partial signing services and corrupt snapshots are outside this interface. Honest source computations and simulation resources remain charged separately from adversarial Q; a query theorem is not a gate-cost theorem.

**ASSUMED — parameter domain.** Keep n=16 bytes, BE32 counters, FORS+C, non-top digit width lw=4 and top width lw=8. Let d be an integer in [1,256], r=k-1 in [1,94], a in [1,31], and h_i in [0,31]. Put h=sum h_i<=63. Require r*2^a<=2^32 and (r+1)*a+h<=256. At each layer, w_i=2^lw_i, 1<=ell_i<=128/lw_i and 0<=S_i<ell_i*(w_i-1). The omitted 128/lw_i-ell_i digits are checked zero. All source-generated addresses, arrays, compression scratch buffers and arithmetic obey the actual u8/u32/u64 bounds without wrap or truncation. The r<=94 guard is the source tail-buffer bound, not a restriction on arbitrary adversarial raw input lengths. For d=1 only the top-width rule applies. Parameters with maximal target sum or unverified omitted digits are not covered. Zero-height layers are permitted by the addressed schema and still have distinct layer IDs.

## 2. Uniform graph, private restrictions and safe ghost

**PROVED — genuine child uniqueness.** With b_i=sum_(j<i)h_j, route z gives leaf floor(z/2^b_i) mod 2^h_i and tree floor(z/2^(b_i+h_i)). A full WOTS address (layer,tree,leaf) identifies one FORS public key at the bottom or one complete lower-subtree root above it. Neither depends on the chosen external message or selected FORS leaves. Thus honest repeated use signs one genuine child, with one canonical counter and digit vector, rather than several independently chosen children. The identity also holds for zero heights because layer IDs and full tree coordinates remain encoded.

**PROVED — uniform ordinary marginal.** Use the construction of CLASSICAL-JOINT-RO-THEOREM.md with the guarded finite graph. Private start addresses have type5/6; chain, WOTS compression, Merkle, FORS and root compression have the source type0..4 addresses. Injective guarded field encoding separates distinct restrictions. Generate each designated graph input from earlier other restrictions and combine its genuine full image with uniform residual cells. Deferred sampling gives the ordinary full-function REAL marginal. Equal node values do not identify different addressed restrictions. Genuine starts and interior coordinates remain hidden; endpoint, leaf and public compressed/root values form the safe surface. This is a finite mathematical coupling, not a claim that an eager graph simulator is efficient.

**PROVED — canonical rows and partiality.** A type7 restriction receives its genuine child from other graph restrictions. Disintegrate its function into first accepted (counter, full 128-bit target), the rejected same-child prefix, full lower limbs and residual cells; retain bottom when no finite counter succeeds. Its acceptance probability is the bounded-composition coefficient for ell_i digits and sum S_i divided by w_i^(128/lw_i)=2^128, including the omitted-zero filter; it is not divided merely by w_i^ell_i. Acceptance coefficients may vary with p. Rejected prefix targets cannot equal the accepted target. Unused rows need not succeed; no global successful-setup conditioning or postaccepted residual-row disclosure is made. The safe surface includes only the canonical metadata and public graph values, independently of hidden predecessors and untyped message streams.

**PROVED — common continuation.** One residual table O0 answers still-hidden protected points without inspecting their genuine input. Genuine graph records supply honest computation and known public points. A completed response permanently reveals its FORS secrets and forward WOTS suffixes. Newly known designated cells are installed only when no prior public reply is fixed. Before the first hidden hit a prior inconsistent reply cannot occur. Consequently undisclosed predecessor coordinates remain unused by the public continuation. Private K/P guesses and unused-J predictions are analytical flags, not routing tests. An unsigned J(m) coin is unused before the first atomic request for m; there is no intervening adversary raw slot inside that request. Noncompletion absorbs. Until the common first bad, REAL and this ghost share observed replies and honest computations, without asserting equality of their complete unqueried functions. All event projections below use this same ghost, not incompatible full-secret advice worlds.

## 3. Exhaustive uniform final-witness cover

**PROVED — addressed descent.** Compare an accepted final path with the genuine path for its decoded route. A first merger from a different ordered payload to the same genuine output is a public graph witness G. Without G, Merkle descent, endpoint compression and ordered FORS root compression recover the genuine lower objects. Source parent indices (j*2^a+leaf)>>height and the guarded tree/leaf decomposition agree at every level. This induction uses encoded addresses and ordered inputs, not baseline heights.

**PROVED — WOTS alternatives.** A changed endpoint vector gives G at compression; a changed chain start reaching a genuine endpoint gives G at its first merger. Otherwise the supplied values are genuine chain coordinates. At an unexposed address t_i=ell_i*(w_i-1)-S_i>0 guarantees a nonterminal genuine start opportunity H. At an exposed address let x be its canonical tuple and e the accepted forgery tuple. Equal sums imply either e=x or some e_j<x_j. The latter asks for a genuine predecessor before the disclosed suffix, giving H. In the former, omitted-zero checks and fixed lw4/8 decoding identify the entire 128-bit target. A different child/counter then gives an exposed successful type7 witness D7; otherwise the genuine child is recovered and descent continues. No assumption that all WOTS addresses were exposed or all unused rows succeeded is needed.

**PROVED — FORS alternatives.** A different ordered root, path or secret image gives G at its first merger. A genuine undisclosed secret gives H. If every real selected secret has been disclosed and the forced coordinate passes, coverage C_cov holds. The forced coordinate contributes a zero filter, not an eighteenth secret. Therefore Win is contained in C_cov union H union G union D7, in addition to the common coupling bad events. This statement is uniform only under the representation, strict-target and interface guards above.

## 4. Simultaneous rare-event and final-call accounting

**PROVED — raw role weights.** At S!=0, private framed words have block bytes16..31 equal zero, whereas private-J/inner words have that block S. Eligible outer words have length52, suffix S, and a second block different from S. Types separate valid addressed private5/6, graph0..4 and7 words. The partition is determined before each reply. In units 1/N, N=2^128, its weights are1 for private-F/short-J/ordinary graph/type7,3 for inner,2 for potentially hidden nonterminal-chain/FORS-leaf and0 for the remaining roles. The three inner risks overlap; the two hidden-input/output risks also share their raw opportunity. The predictable total role count is pathwise <=Q, so its expected weighted charge is <=3Q/N in this ONE continued ghost. Neither a separate Q for each role nor a one-role disjointness claim is used.

**PROVED — honest fees.** Honest/final inner work gives <=2(q+1)/N. An honest outer alias to private J already requires the charged endpoint-half event, so it creates no additional first-bad fee. Source setup/addressed work creates no new untyped nominees at nonzero S. Static target matches are charged at their first residual generation; repeated known matches only overcount. A rejected same-child canonical row cannot equal its accepted full target.

**PROVED — changed terminal counts.** Every accepted layer performs exactly t_i verifier chain steps. The final hidden opportunities are H_p=r+sum_i t_i. Public type0..4 final evaluations number G_p=r*(a+1)+1+sum_i(t_i+1+h_i): r FORS leaf/path groups, their ordered compressor, and each layer's chain completions, endpoint compressor and authentication path. There are d type7 calls. These are full-oracle opportunities, not SHA compression blocks or the total number of generated graph nodes. Uniform seed-zero is paid once after averaging. Hence

    C_p = H_p+G_p+d+3
        = r*(a+2)+2*sum_i t_i+h+2*d+4.

The extra3 consists of two final inner opportunities and one averaged seed-zero charge. For the actual baseline, H_p=3017, G_p=3217 and C_p=6242, exactly recovering the accepted joint theorem.

## 5. Full-word message bridge and finite coverage

**PROVED — same bridge.** Nonce R is prefix128 J(m); the inner word is R||S||root||m; the outer word is U||BE32(c)||S for full256 inner U. Each distinct message gives a distinct inner input even when nonces repeat. The endpoint-half exclusion and syntactic classes make the full-inner collision and preview charge

    (q*Q+binom(q,2)+q)/N^2.

The denominator is full256 even when fewer digest bits are selected. Preview into later honest namespaces, collisions between honest namespaces and final fresh access to an old honest namespace are all paid. Old honest rejected points fail the filter; old honest accepted points are not fresh independent candidates. Repeated messages/points reuse memoized values.

**PROVED — uniform dimension-dependent law.** Let B=2^h, t=2^a and beta=1-1/t. Disjoint selected bits consist of r real a-bit indices, one forced-zero a-bit coordinate and h route bits. The guard (r+1)*a+h<=256 permits this even at equality. Fresh outer words are uniform in those coordinates. First acceptance among 2^32 counters depends only on the forced coordinate, so the accepted real indices and route remain independent uniform. Failure contributes q*beta^(2^32), not zero. A later WOTS noncompletion yields no completed response or subsequent Win; including its internal draw in an independent exposure padding only enlarges coverage.

In the same stopped-prefix coupling, attach independent exposure draws to fresh honest successful namespaces and candidate draws to fresh nonhonest points. Extend with unused coins after the stop; do not call the actual postbad execution iid. Pad to deterministic counts q and Q+1. For a selected route Z~Binomial(q,1/B); conditional on Z the r leaf fractions are independent and each has expectation 1-beta^Z. Thus

    p_F(q;p) = (1/t)*E[(1-beta^Z)^r],

and the padded coverage charge is <=(Q+1)*p_F. An expected eligible-query count cannot replace the deterministic candidate cap. The proof includes B=1 and q=0 without Poisson substitution.

## 6. Complete theorem and exact transfer

**PROVED — uniform manual classical envelope.** Combining the common stopped coupling, exhaustive final cover and independent padding, then averaging over S and paying S=0 once, gives for every guarded p and adversary in Section1:

    Pr[Win] <= E_p(q,Q)
      := min(1,
         (3*Q+2*q+C_p)/N
         +(q*Q+binom(q,2)+q)/N^2
         +q*beta^(2^32)
         +(Q+1)*p_F(q;p)).

All nonnegative fees are retained before the final cap. This is not obtained by subtracting fees from incompatible unconditional estimates. Honest canonical cache preparation and atomic restoration preserve genuine children, first accepted counters and paths; whenever the reference call completes their bytes agree. They therefore transfer this precise event and adversarial-query bound with loss0. Arbitrary accepted noncanonical counters or corrupt caches do not satisfy the premise, as shown separately in CACHE-CANONICALITY-OBSTRUCTION.md.

**PROVED — limitation of this sufficient certificate.** For every tuple in this domain E_p(q,2^128)=1 because 3Q/N alone exceeds1. If E_p(q,Q)<=eta<1, necessarily 3Q+2q+C_p<=eta*N. In particular a half-success certificate requires Q< N/6, strictly when q or C_p is positive. This is a necessary condition on THIS upper-bound certificate, not on actual adversary success, optimal attack cost or existence of another proof. A literal 2^-128 failure target at Q=2^128 and AES-normalized 128-bit work are different propositions.

**OPEN — original adequate guarantee and repair.** No tuple achieving the requested complete128/category1 criterion, capacity or successful smallest repair is certified here. Security feasibility must include a justified success/resource comparison, plus availability and explicit signature/computation costs; optimizing p_F alone does not close it. Retuned QROM, changed seed width/digit encoding or out-of-domain parameters need separate proofs. This manual source-RO theorem neither assumes SHA hardness as a proved fact nor adds unconditional SHA or compiler/kernel verification as a prerequisite for the original RO task. New checked whole-source/game declarations:0. The printable full-security guarantee remains "not established".

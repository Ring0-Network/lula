# First-call quantum FORS/source bridge

**Status: MANUAL_FIRST_CALL_BRIDGE_CANDIDATE_WITH_VERIFIED_PRIMARY_THEOREM; INDEPENDENT_REVIEW_PENDING.** This sharpens the independently saved elementary envelope for the first classical signing call only. No peer quantum-FORS proof was read. It does not establish full adaptive quantum FORS coverage or a full QROM signer bound.

## 1. Primary theorem: exact source and conventions

**CITED.** Grilo, Hövelmanns, Hülsing and Majenz, [*Tight adaptive reprogramming in the QROM*, arXiv2010.15103v2](https://arxiv.org/pdf/2010.15103), Figure2 and Theorem1, Equation(2), printed pages6-7. Exact finite-set assumption: “Let X, X′, Y be some finite sets”. Its reprogrammer samples x from an adaptively supplied distribution, independently samples a uniform y in Y, changes O(x) to y and returns x/side information. It does not return y. With p_r=E[max_x Pr(x)] and Qhat_r preceding queries, the stated event-probability difference is

    sum_r [sqrt(Qhat_r p_r) + (1/2)Qhat_r p_r].

For one instruction: sqrt(Q p)+(Q p)/2. Theorem6 (printed page20) gives equivalent binary success probability <=1/2+(1/2)sqrt(Qp)+(1/4)Qp and permits arbitrary post-instruction queries. This is information-theoretic, not a PPT construction. These constants were checked in the primary PDF, not guessed or obtained by substituting Q for a classical query count.

**COMPUTED (primary binding).** Downloaded author PDF SHA-256: `9a5ea6adeba5dcdf6c80035057aaccdc704aa6ea2940af0320bcfd7eca0abc8d`. The local printed-page6-7 extraction was inspected; it preserves the equation and Figure2 game. The primary result above is the only imported bound. The source-specific statements below are independently derived.

## 2. Exact restricted source experiment

**ASSUMED.** JOINT F/J ideal game, frozen single-root source; fixed nonzero S; ordinary full256 random O; no previous signing use of J; at most Q coherent raw-O calls before the first initiated classical signing request. The message is selected adaptively but is classical. The finite injective raw encoding includes every allowed message/header and all honest strings. Setup and signing are atomic partial operations, without timing, cache/private call disclosure, coherent signing, compression access or successful-setup normalization. Source hash remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

**PROVED (source).** At that request,

    R=Tr128 J(m), I=R||S||root||m, U=O(I),
    E_c=U||BE32(c)||S.

Fresh private J(m) makes R uniform and independent of the chosen pre-call history. It does not make original U independent of quantum prequery memory. The signer checks the omitted nine-bit index and takes the first zero; repeated m later uses the same J(m), I, U and row.

## 3. First hop: the inner point

**PROVED (oracle restriction).** On S!=0, the inner family has bytes16..31=S, while all typed source graph strings have zeros there. Conditional on the key/setup graph and the outside oracle functions, the inner family remains an ordinary independent restriction. Its selected root is an outside-typed graph value, so this conditional restriction is not selected by inspecting inner residual outputs. Pre-key queries can be represented by sampling that outside information initially and withholding its disclosure.

**PROVED (full-oracle simulation).** An arbitrary coherent raw-O query may mix inner and outside inputs. A one-query simulation is possible: evaluate known outside-table XOR locally; prepare a full256 |+> ancilla; conditionally swap the original output into it only on the inner branch; route outside inputs to a fixed dummy inner input; query the inner XOR oracle once; unroute and swap back. XOR leaves |+> unchanged on the outside branch. Thus Q original calls cause at most Q queries to the selected inner restriction. The conceptual outside tables may be enormous; no efficient simulator is claimed.

**PROVED / CITED (first-point instantiation).** Once classical m is selected, supply the primary reprogrammer with the distribution of I(R,m), R uniform128. The maximum point probability is exactly2^-128 for every selected m. Store the returned R as the private J(m) prefix and sample its unused full-image tail consistently. In the unchanged branch, one post-instruction source query at I reads ordinary U=O(I), exactly the source. In the reprogrammed branch, U is a fresh uniform256 image independent of pre-call memory and the oracle is consistent at I for later verification. The post-instruction source query is not a preceding query in Qhat_1. Arbitrary remaining source work and adversarial continuation belong to the second stage.

Therefore

    alpha_I(Q)=min(1,sqrt(Q/2^128)+Q/(2*2^128)).

The actual signer need not disclose U to the adversary. The reduction reads it internally to simulate the remaining source; hiding that information cannot increase the distinguishing advantage. The returned I reveals R, which the signature already transmits. A point sampled according to an adversarial forged R is not covered by this honest-call theorem.

## 4. Guard and row-valued oracle

**PROVED (fresh U guard).** In the reprogrammed game U is fresh uniform256. Its lower128 bits equal S with probability2^-128. Couple it to a uniform U over

    G_S={u in {0,1}^256 : u[16:32]!=S},
    M_G=|G_S|=2^256-2^128,

by keeping U unchanged when eligible and resampling an eligible U on the bad branch. Reapply the same known inner-point assignment. This changes the full post-call experiment on probability at most2^-128, without conditioning a quantum history or asserting the wrong point density. The eligible namespace now has density1/M_G, rather than1/2^256.

**PROVED (independent row restriction).** E_c has length52. With U eligible its bytes16..31 differ from S, so all eligible E rows are disjoint from the entire inner language. They are also too short to be typed graph hashes. Treat their ordinary function restriction as a row-valued oracle

    Row(U)=(O(E(U,0)),...,O(E(U,C-1))), C=2^32.

Different U rows consist of disjoint raw points. Each row is independently uniform in Y_row=({0,1}^256)^C. This is a finite output set, although its XOR output register has256C=2^40 qubits.

## 5. One-query selected-counter simulation

**PROVED (coherent lookup).** A raw eligible query gives a coherent namespace U, counter c and original full256 output register Z. Prepare all C row-output slots in |+>^256. Coherently swap Z into slotc. Query the row-valued XOR oracle once. Every unselected |+> slot is invariant under XOR; the selected slot receives Z xor Row(U)[c]. Swap it back. All row ancillas return exactly to their initial |+> product state, even with U/c/Z/work ancillas entangled. For an outside branch perform no swap and route to a dummy row; its complete |+> output absorbs the row XOR. Known outside functions can be evaluated locally.

Thus one original raw call costs one row query, without a C multiplier. Loading a row into zero ancillas and leaving unused words as garbage would not preserve the original coherent interface. The enormous auxiliary register rules out an efficient/PPT claim, but does not violate the primary theorem's finite information-theoretic hypotheses.

## 6. Second hop: fresh row at the full256 namespace

**PROVED (operation order).** The inner assignment I -> U and every eligible row assignment are on disjoint raw cells. There is no adversarial interaction between them during the atomic request. They commute. Consequently the inner assignment can be deferred until after the row reprogrammer selects and returns its U. In both row-game branches, a common continuation stores fresh J(m)'s R, assigns I -> that U, and runs the source. The preceding prefix contains Q row queries, with no setup row queries and no additional coherent query between the two programming instructions. This is a change of independent-operation order, not a claim that a target already revealed to a querying adversary retains min-entropy.

**PROVED / CITED (row instantiation).** Supply the primary theorem with one namespace instruction sampling U uniformly from G_S, and Y=Y_row. It resamples the complete full256 row to independent uniform words. In its unchanged branch, the row is the ordinary existing row at a fresh independent namespace; in its changed branch, it is an independent fresh row. Both continuations make the same inner assignment and source calls. The theorem allows arbitrary later selected-counter/future queries.

The one-query lookup yields

    alpha_row(Q)=min(1,sqrt(Q/M_G)+Q/(2M_G)).

The programmed row image is not a preselected accepted digest. All C full words are sampled; only the source's zero predicate selects the first accepted word. No forced output distribution or accepted-conditioned reprogramming is hidden in this step.

## 7. First-call latent selection and complete loss ledger

**PROVED (candidate first-call bound).** Combining the two event-distance statements and the guard coupling gives

    Delta_first,nonzero(Q)
      <= min(1, sqrt(Q/2^128)+Q/(2*2^128)
                 +sqrt(Q/(2^256-2^128))+Q/(2*(2^256-2^128))
                 +2^-128).

If averaging uniform S and assigning the actual shared-oracle S=0 branch distance at most1, add one further2^-128. This is a comparison to a first-call programmed experiment, not the complete forgery probability.

**PROVED (row selection).** Fresh row coordinates are iid. The zero filter Z is independent of the used bucket/17 real indices X. For every counter c<C, first acceptance depends only on Z_0,...,Z_c; accepted X is uniform on [2^41]x[512]^17 and independent of the rejection count. Exact row exhaustion is (511/512)^(2^32). Retaining failed rows as absorbing noncompletion requires no normalization or extra always-success premise; forcing success adds that probability as a separate loss.

**PROVED (completion qualification).** Subsequent WOTS metadata search can be partial and depend on the selected route. Only the latent accepted FORS coordinates have this iid law. The distribution of completed full signatures need not stay uniform after conditioning on all remaining source operations terminating. Such observations must not be treated as independent keys or extra free draws.

## 8. Smallest remaining obligations

**OPEN (independent validation).** The first-call source mapping, full-oracle restriction simulation, row-valued output reduction and commuting operation order need an independent reader. The primary formula alone does not validate them.

**OPEN (q-call source bridge).** Preserve old J labels, old inner assignments and old full rows simultaneously. Bound new full-U collisions with old namespaces, honest I/E aliases and all prefix-query counts without charging billions of outside typed calls or ignoring free earlier row information. A naively repeated first-call loss can become vacuous at the intended q; that is a sufficient-bound limitation, not an attack.

**OPEN (quantum FORS coverage).** No classical Q_H+1 independent candidate list is produced by coherent queries. Need an observable final-candidate/average-search reduction under adaptive transcript coverage and explicit query accounting. Replacing Q_H by Q_q^2 in the old component expression is not established here.

**OPEN (full QROM).** Joint private, hidden-value, graph/canonical branches and adaptive FORS coverage must compose on a common source experiment. This first-call result does not close that total or a category certificate. All writes remain in the new lane; no signature timing, cache build, manuscript or frozen packet change occurred.

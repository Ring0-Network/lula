# Independent coherent selected-prefix PRE extension

**PROVED — manual candidate awaiting independent second reading.** This derivation was saved before reading any new peer quantum derivation. It extends the reviewed classical stopped-cut construction only in its addressed RO-relative ideal-private game. The classical candidate and its provenance are immutable. No operational forgery, source edit, timing, key/cache creation or upload is used.

## 1. Exact claim and event

**ASSUMED — model.** Fix S!=0, N=2^128, source HJ with classical atomic signing, independent full256 private F/J maps, eager full256 random raw functions, bounded finite input registers, and at most Q_q coherent adversarial raw calls across pre-key/post-key phases. Classical adversary raw queries also count against that cap through the usual XOR-query representation. Honest classical source calls are separately counted. There is one final classical source verifier. Allowed public logical cache data contain public endpoints/nodes and canonical counters, but no selected hidden chain values. Source lib SHA256 ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210.

**PROVED — event distinction.** H_final means at least one genuine currently-unexposed WOTS predecessor or FORS secret is supplied as the input of a classical final-verifier call. No hidden-query history is measured during coherent A queries. For every such final trace take its FIRST H_final call and its indexed address d. These first-address events E_d partition H_final. The bound can cover H_final itself; Win AND H_final is a subset. If a completed signature previously disclosed the selected chain position or FORS secret, its permanent exposed status rules out E_d even after restore.

**ASSUMED — challenge.** B chooses S and a valid protected address d before A. Challenger samples an independent uniform16-byte hidden X and a random complete256 Selected function on bounded payload strings, gives the full32-byte target Y=Selected(X), and supplies its coherent XOR oracle. Output16-byte z wins iff Selected(z)=Y in all256 bits. B itself samples all other raw restrictions. This is quantum addressed-RO-relative uniform-input fullimage PRE, not a claimed conventional fixed-key SHA PRE game. A never receives Y as extra data; source public endpoints retain only the appropriate128-bit slices.

## 2. Fully blinded prefix, not a one-cell shortcut

**PROVED — selected WOTS r>0 coupling.** Let d_j be the selected chain's type0 address at j=0,...,r-1 and let d_r be the target address. Independently sample U_0,...,U_(r-1), each uniform16 bytes, and independent lower128 limbs rho_j. Put U_r=X and U_(r+1)=first16(Y). Sample an ordinary local outside full256 table O_B independent of all those U_j. Define the latent SOURCE function O_T to agree with O_B except
O_T(d_j,U_j)=(U_(j+1),rho_j), j<r.
For j=r-1 that upper limb is unknown X. Set the source private F secret's upper limb to U_0 with an independent lower limb. The selected target restriction remains Selected everywhere, including off-length payloads. Distinct full addresses ensure each restriction's designated input was chosen without reading its own function. Each programmed fullword is independent uniform at that input, so the joint latent SOURCE sampler has exactly the ordinary source RO/chain law. Unused residual table values at those points can remain in the coupling environment without being disclosed.

**PROVED — executable BLIND game.** B does NOT implement O_T or return unknown X. It uses O_B coherently and does not overwrite any output. In honest selected-chain PK computation it substitutes the endpoint obtained by continuing from first16(Y). For completed selected-chain signatures at positions e>r it supplies the correct suffix value derived from first16(Y). If a response would expose e<=r, it stops before returning that atomic response. All source metadata, children, counters, message processing, other-chain derivations, public payloads and setup failures retain their actual routines and law. The selected U_j are unused by A-visible processing in BLIND, before final extraction. In particular they are not obtained by evaluating O_B earlier in the chain: that would destroy the needed independence. This fully blinded prefix costs no prior-prefix oracle queries. The selected suffix needs at most w-r-2<=254 outside calls.

**PROVED — r=0/FORS.** At WOTS r=0 the selected ideal F upper limb is the latent X and all public/suffix values start from first16(Y). No earlier restriction differs, hence no quantum blinding cost. A selected FORS ideal F secret is likewise X; its height-zero leaf image is first16(Y), all tree paths/public roots are computed normally and completed selected-secret disclosures stop before response. There is no predecessor restriction and no blinding error.

## 3. Exact active-view query-mass lemma

**PROVED — physical active-prefix independence.** In BLIND, condition on all outside tables, the selected challenge function/target, other private values, S, and the selector. The selected-prefix words U_0,...,U_(r-1) are still independent uniform and unused by every operation visible to A. Any completed-signature stop at e<=r depends on public route/metadata/digits, never on those words; stop/active flags therefore do not reveal them. Previous raw replies come from O_B independent of these words. This remains true with A's retained pre-key quantum memory and adaptive classical requests. On the active physical CQ block the query state has the product form
(1/N^r) sum_u |u><u| tensor omega_query,
with omega_query subnormalized, trace<=1. Do not normalize surviving runs or infer that a conditioned SOURCE state remains uniform.

**PROVED — mass bound.** Let P_u mark query inputs whose literal header is some d_j, j<r, and whose16-byte payload is U_j. The headers d_j are distinct. In the active BLIND query state,
E_u Tr(P_u omega_query) = (1/N) sum_(j<r) Pr[header=d_j, payloadlength=16] <= 1/N.
The sum of header probabilities is <=1, so this is NOT r/N. Off-length payload queries contribute zero. This statement bounds only BLIND query mass. It does not substitute a claimed uniform SOURCE posterior.

**PROVED — XOR-query difference.** O_T and O_B agree outside that marked input set. Their XOR unitaries therefore satisfy
||(U_T-U_B) psi|| <= 2 ||P_u psi||
for each purified common latent world. Averaging squared norms in the common coupling gives at most4/N for each active query, hence vector distance at most2/sqrt(N). Honest operations and exposure stops can be purified as common isometries/channels with absorbing terminal flags; they introduce no additional vector norm. Telescoping the Q_q adversarial query slots, evaluating every difference on the corresponding BLIND prefix, yields
D_r <= 2 Q_q /sqrt(N) for r>0,
D_0=0 for r=0 or FORS.
This is the exact rederived O2H-style charge for this selected-prefix coupling. No query support is measured, no predecessor comparison is applied to a coherent register, and no uncontrolled-to-controlled oracle assumption is inserted.

## 4. Final extractor and why later exposure is harmless

**PROVED — common final channel.** After A returns its classical final message/signature, execute the exact source verifier. For the selected WOTS chain, before answering ANY classical final query at a known designated prefix point (d_j,U_j), j<r, stop with failure. B knows these words. All other outside replies agree between O_T/O_B. At a16-byte selected-header query z, query Selected and, on full32-byte equality to Y, output z and stop successfully. Otherwise retain its ordinary full reply and continue. The selected full address is visited at most once in a parsed source final trace. FORS/r0 require no prefix guard. This final stopping is on classical verifier calls after A has produced a classical output, rather than measuring A's coherent query history.

**PROVED — source first-event inclusion.** On E_d, no completed response previously exposed the selected coordinate, so the earlier exposure stop never removed this branch. If a previous final-verifier call reached (d_j,U_j) at j<r, the selected position's unexposed status implies that earlier prefix was unexposed as well, making that call an earlier H_final and contradicting first address d. Thus the final prefix guard also did not stop before the selected query. Its genuine payload is X, which returns the full Y and wins PRE. This argument also covers a non-genuine supplied chain value that happens to merge into a genuine hidden suffix: earlier changed-input calls are residual points where O_T and O_B agree. No absence-of-G condition is required. The extractor may win on an invalid/familiar-message transcript too; that only increases PRE success and does not alter source Win.

**PROVED — exposure scope.** The source-versus-B comparison is of an event-specific stopped interaction, not full-transcript equivalence after an unknown value is disclosed. A later exposure at e<=r cannot occur on E_d because it would make the final selected position permanently exposed. Such non-E_d branches can stop before their response in both compared interactions. This is absorption, not conditioning on selected secrecy. Known suffix disclosures e>r are source-correct, retain actual counter correlations and remain independent of U_j in BLIND.

**PROVED — selected success inequality.** Write a_d=Pr_SOURCE[E_d] and p_d=Pr[B_d wins PRE]. The common final channel and successful-output projector give
sqrt(a_d) <= sqrt(p_d)+D_r.
This follows by contraction of the vector-distance bound and triangle inequality for projected norms. No assertion of PSD domination between two different pure states is made.

## 5. Mixture selector and explicit loss

**COMPUTED — counts.** D_W=1,089,588,072,284,160 WOTS nonterminal positions; D_F=19,140,298,416,324,608 FORS secret positions; D_H=20,229,886,488,608,768. Let L=2^55. Exactly55 selector bits unrank these D_H labels; dummy labels stop before A. The number of interior WOTS positions with r>0 is
D_int=32*14*(2^41+2^36+2^31+2^26)+16*254*2^21.
Only these selectors incur D_r. The r0/FORS selectors are exact embeddings.

**PROVED — block norm and resulting bound.** In the direct-sum purification of this fixed selector, total squared vector distance is at most4 Q_q^2 D_int/(L N). Source selected first-event probability is Pr_SOURCE[H_final]/L, because the E_d are disjoint and every real address is selected with probability1/L. B's mixture PRE success is p_PRE. Projection contraction and norm triangle therefore give
sqrt(Pr_SOURCE[H_final]/L) <= sqrt(p_PRE)+2Q_q sqrt(D_int/(L N)),
so
Pr_SOURCE[Win AND H_final | fixed S!=0] <= Pr_SOURCE[H_final | S]
 <= min(1, (sqrt(L p_PRE)+2 Q_q sqrt(D_int/N))^2).
This is a sufficient interface reduction, not an optimized direct hidden-input bound. Multiplication by L makes the QROM simulation charge large. Do not add it to or replace the already sharper direct QROM scalar theorem without comparing them. This candidate does not by itself establish a security category or q_max.

**PROVED — seed zero.** The statement is for each fixed S!=0. If B samples production S and immediately fails at zero, source nonzero contribution and B success have their usual (1-1/N) factor; one can bound the full source event by adding1/N once. No source seed sampling or cryptographic parameter is changed. Do not duplicate that charge per selector/component.

## 6. Explicit oracle, time and storage resources

**PROVED — coherent routing.** Each complete raw query is routed reversibly by literal86-byte header comparison. Use one Selected XOR call and one local outside XOR call per logical source raw query, feeding an inactive response register in the all-plus state, then undo routing. XOR leaves that inactive plus state unchanged. This avoids assuming controlled access to an unknown oracle. Thus the PRE challenge sees at most Q_q coherent queries and one classical final Selected call, in addition to its supplied target. Local outside calls include at most Q_q coherent calls plus the separately bounded honest classical source calls. All complete256 outputs/lower limbs and payload lengths are retained.

**PROVED — source caps.** Selected honest endpoint/leaf evaluations reuse the target data and do not call the Selected oracle. The conservative honest outside cap remains H_setup+q H_mode+3224+254, with the classical candidate's exact H_setup/H_hot/H_cold values. F distinct entries remain bounded by min(N_D,1+2181038080+q U_mode); J<=q. Source counter exhaustion remains unconditioned absorbing noncompletion. Public logical payload generation is already in the source costs and never reads the blinded selected prefix. Local selected-chain payload bytes remain<=4096.

**PROVED — finite local quantum implementation, not lazy classical measurement.** Fix b=max(598,48+maximum-message-length,maximum-adversarial-raw-input-length), with bounded finite strings. An explicit local outside function table has V_b=sum_(ell=0)^b 256^ell entries, each32 bytes. Sampling all entries independently before interaction is finite and independent of the selected prefix; unqueried selected-header shadow entries can be unused. A reversible lookup circuit implemented by a linear scan needs O(V_b*(b+32)) classical controlled gates per coherent outside query and stores32 V_b data bytes plus query/work registers. This is a conservative finite realization, not feasible QRAM or a claim of polynomial time in input length. Standard ideal-RO resource accounting can treat this local oracle as free, but then it must say so explicitly. A classical dictionary which measures a coherent query is NOT an implementation of this simulator. Honest F/J tables are queried only classically and may remain lazy. No complete secret graph is enumerated; the enormous local raw table is a distinct quantum-simulator cost.

## 7. Remaining boundaries

**OPEN — independent checking.** The active-CQ factorization, final first-event inclusion and selector block norm need an independent reader and finite controls before promotion. This is a newly saved manual candidate, not wholeRust mechanization.

**OPEN — conventional/efficient quantum primitive identification.** Identify the stated fullimage uniform-input addressed oracle challenge with the desired standard keyed SHA primitive, and obtain an efficient outside-oracle simulator if conventional reduction time requires it. A fixed-SHA or NIST category assertion does not follow from this finite RO-relative program.

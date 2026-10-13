# LULA I shared-oracle proof extension

**OPEN — overall verdict.** Classical level1 certification, a certified signing capacity and a full QROM category1 bound are not established. A complete advantage upper bound for the explicitly specified classical RO source game is now independently reviewed in section5. This extension advances specific obligations of the frozen parent packet; it does not replace OPEN terms by zero or edit the manuscript. The parent `PROOF.md` remains the source-bound experiment, full oracle inventory and original obligation ledger. Its manuscript digest describes an earlier, subsequently edited paper cut.

## 1. Fixed construction and interfaces

**COMPUTED — source pins.** Original Rust library SHA-256 is `c5b16f35ec9e3a826e5d8100dbbc4d3a8287e3e52fd567a24e95f03bb7243ab5`; the release library is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. The extension preservation check compares both against the frozen packet and preserves the current editorial manuscript independently. No new parameter set, timing experiment or full cache preparation is performed.

**ASSUMED — classical game.** Three independently uniform 128-bit seed components are K=SK.seed, P=SK.prf and S=PK.seed. One shared random oracle O maps finite byte strings to full 256-bit outputs. Private derivations consume their first 128 bits. The adversary has raw classical queries, opaque key-independent snapshot handles and atomic completed signature responses. It does not receive cache bytes, timing, private contexts or the secret-bearing benchmark snapshot. Noncompletion is an absorbing nonwinning execution, not a conditioned setup-success experiment.

## 2. A joint private-input replacement

**PROVED — input languages, manual source binding.** Write B=S||zero[48]. Secret derivation inputs are D_K={B||A||K}, where A is a valid 22-byte type-5/type-6 address. Message-randomizer inputs are M_P={P||S||m}. On S!=zero[16], the two sets are disjoint by bytes 16–31. Public addressed calls use other type bytes and are outside both sets. Public inner calls I=R||S||root||m cannot hit D_K. Public outer calls E=U||BE32(c)||S have length 52 and cannot hit D_K. I enters M_P only if R=P; E enters it only if U's first half equals P and second half equals S. Changing c does not change that possible P candidate.

**PROVED — coupling, manual statistical theorem.** On nonzero S, sample independent full-image maps F(A), J(m) and O_pub(x). Define O_real to equal F on the complete D_K family, J on the complete M_P family and O_pub elsewhere. Distinct raw inputs receive independent full 256-bit images; O_real has the original shared-RO marginal. REAL uses O_real throughout. JOINT-IDEAL uses F and J for private derivations and O_pub for all public calls. Repeated labels memoize full images. The complete hidden families, including future labels, are used from the outset, so a public prequery is already a Bad event and is never overwritten later.

**PROVED — zero-seed branch.** Charge S=zero[16] immediately as Bad and continue REAL with its original single-RO marginal. The disjoint F/J reconstruction is not applied to that branch. JOINT-IDEAL retains its separately defined independent maps. This costs at most 2^-128 and introduces no seed-rejection modification.

**PROVED — key-blind candidate argument.** In the continued JOINT-IDEAL execution, K/P are unused coins. The analytical Bad flag cannot alter answers, control flow or stopping. Fixing that entire unflagged execution fixes all candidate lists independently of K/P. The probability either key occurs in its list is at most the sum of list lengths divided by 2^128. This is an unconditional argument; the posterior conditioned on surviving guesses need not remain uniform on all keys.

**PROVED — candidate accounting.** A raw adversarial query nominates at most one key across the disjoint private languages. An initiated signing call adds at most two P candidates, one inner R and one outer prefix. A final verification adds at most two more. Setup and addressed grinding add none by the structural domain exclusions. Therefore, for q initiated calls and Q_H raw adversarial queries,

\[
 \Delta_{\rm joint}\le\min\{1,(Q_H+2q+3)/2^{128}\}.
\]

**PROVED — completed-call variant.** If q bounds completed calls and one pending absorbing call is permitted, use min{1,(Q_H+2q+5)/2^128}. The loss concerns an unconditioned event or game distance; conditioning on successful setup requires its own normalization argument.

**PROVED — mechanized arithmetic component.** `root-formal/SeedGuess.ec` checks the unchanged statements `uniform_atom_bound`, `one_seed_hit_bound`, `two_seed_hit_bound` and `key_blind_game_bound`. The procedure samples independent unused keys after fixed candidate lists. These declarations establish the list-union inequality, not the source noninterference, source encodings, complete coupling or efficient simulator. Checker receipts and imported-library/solver identities are separate artifacts.

**OPEN — reduction boundary.** A complete efficient simulation/resource contract and a Rust refinement remain unproved. Public message/node/hash domains remain one shared O_pub, not independent primitive oracles. The joint replacement does not close the ideal signer's forgery probability, individual standard-model PRF claims or QROM security.

## 3. Adaptive coverage in independent fresh streams

**ASSUMED — coverage model.** B=2^41 instances, t=512 leaves, K_real=17 trees; independent uniform exposures X and independent raw candidates Y. The omitted eighteenth coordinate contributes only a zero filter with probability 1/t. It reveals no eighteenth secret.

**PROVED — transcript identity.** For exposed leaf sets C_bj in a realized transcript T,

\[
 p(T)=\frac{1}{Bt}\sum_b\prod_{j=1}^{17}\frac{|C_{bj}|}{t},\qquad
 \mathbb E[p(T)]=p_F(q)=\frac1t\mathbb E[(1-(1-1/t)^N)^{17}],
\]

where N is Binomial(q,1/B). Expanding the power gives the finite alternating-moment expression in the parent numerical script. This identity concerns expectation, not a pointwise upper bound for every transcript.

**PROVED — adaptive padding.** Presample q independent exposure values and M independent raw candidate values. Any key-blind adaptive interleaving, stopping or retention of earlier candidates reveals prefixes. Padding exposures can only increase coverage. Consequently

\[
 \Pr[\text{covered candidate}]\le
 \mathbb E[1-(1-p(T_q))^M]\le\min\{1,Mp_F(q)\}.
\]

**PROVED — source-conditional form.** If an unconditional coupling agrees with these streams until an explicitly charged source Bad event, and every successful covered route is among Q_outer queried raw candidates or one fresh final-verifier point, its probability is at most Pr(Bad)+min{1,(Q_outer+1)p_F(q)}. This is not obtained by conditioning the streams on retrospectively avoiding Bad.

**COMPUTED — independent controls.** Exact exposure enumeration, coverage-state dynamic programming, occupancy and moment calculations agree. At B=t=K_real=q=M=2, E[p]=17/128 and total late-phase success is 503/2048, below 17/64. Exhaustive first-counter enumeration confirms accepted-coordinate/counter factorization. Four 30,000-trial controls lie inside their stated individual 99.9% Wilson intervals. Correlated reuse preserves uniform exposure marginals but produces success 1/2 instead of 1/16; marginal occupancy alone is insufficient.

**PROVED — reviewed manual source coverage bridge.** `fors-source-bridge/DERIVATION.md` and `fors-source-second-reader/SECOND_READER.md` supply the joint-ideal prefix coupling. For q initiated signing calls and Q_H raw public queries, a sufficient unconditional bad-event bound is

\[
 \beta\le\min\left\{1,\frac{2Q_H+q+2}{2^{128}}
 +\frac{qQ_H+\binom q2+q}{2^{256}}
 +q(511/512)^{2^{32}}\right\}.
\]

The ideal covered-leaf route is bounded by beta+min{1,(Q_H+1)p_F(q)}, capped at one. The private J prediction charge has no q multiplier because every raw inner prequery encodes one message label. Distinct messages remain distinct inner inputs even when their R values coincide. The disjoint inner/eligible-outer languages combine their 256-bit query-pair charges into qQ_H. Final verification includes old rejected grinding points, old accepted points requiring an inner collision for a fresh message, retained public candidates and one fresh opportunity.

**PROVED — repaired deterministic padding and conditioning.** The initial expectation-count padding was false. An independently constructed exact-rational counterexample exceeds that old bound by 31.46 times. The final proof pads to the deterministic Q_H+1, never E[N_E]+1. Expected class counts remain solely in predictable pair accounting for beta. The displayed beta pays S=0 unconditionally; delta_joint+beta safely charges that branch twice if using separate triangle bounds. Removing a charge requires one simultaneous stopped coupling. No source distribution is retrospectively conditioned on avoiding Bad or successful setup.

**OPEN — remaining FORS binding.** This proves a manually source-bound coverage route under the explicit classical ideal interface, not that every accepted forgery is covered. Unknown leaf acquisition, changed-node/root evidence and the full signature composition remain separate obligations. No proof assistant has verified the Rust refinement or efficient reduction.

## 4. Addressed Merkle extraction

**PROVED — checked structural theorem.** `formal-tree/AddressedMerkle.lean` proves that equal roots for two paths with the same address/direction schedule imply either equal leaves and full paths or a common-address, different-raw-input/equal-truncated-output witness in both evaluation traces. The header and fixed-length child splitting are explicitly proved injective. The five declarations check locally under pinned Lean 4.28.0 and match the AXLE statements; their axioms are subsets of {propext, Classical.choice, Quot.sound}.

**PROVED — manual source correspondence.** A node input is S[16]||zero[48]||ADRS[22]||left[16]||right[16], 118 bytes before ordinary SHA padding. The witness concerns the 128-bit truncated function, not necessarily a full SHA-256 collision. A common base/route fixes the address and direction schedule. Comparing against the honest mathematical graph at an unqueried route is permitted by the structural theorem; restricting comparisons to previously signed paths would omit cases.

**PROVED under an explicit DAG hypothesis — separate classical event bound.** `graph-targets/DERIVATION.md` supplies a manual eager-sampling argument for types 0–4: each full address has one honest input generated from predecessor domains, without consulting its own restriction. Conditional on the full designated graph and static outside function tables, every non-designated output remains uniform. Consequently a different-input hit at that address's honest image has bound min{1,(Q_public+3217)/2^128} for nonzero S, or +3218 after charging S=0. The 3217 counts final-verifier complete-hash invocations, not compression operations. Its independent source/DAG review is recorded separately in `graph-targets-second-reader/`. Type 7's self-selected canonical counter is excluded. Revealing all graph payloads leaks signing secrets; the strengthened view is solely a collision-event analysis device and cannot replace the EUF game.

**OPEN — quantitative embedding.** Construct the efficient/lazy honest graph simulator and selected addressed SPR/TCR challenge embedding, with exact success/time/query losses. The separate statistical RO event lemma does not construct a standard-model challenge reduction or a PPT sampler. Trace witness extraction alone does not justify a total-node multiplier.

## 4a. Fixed-child WOTS+C evidence

**PROVED — complete manual structural split.** `wots-certification/DERIVATION.md` distinguishes a changed WOTS PK (delegated to Merkle binding), equal compressed PK with changed endpoint vector, position-labelled chain merger, genuine predecessor recovery, equal full digits with changed child/counter, and canonical equality. At an unexposed address canonical equality is not transcript replay. The target sum is below the full endpoint sum, so at least one nonterminal chain supplies an endpoint-preimage witness in the all-genuine unexposed case.

**PROVED — checked components, not the whole split.** Eight declarations in `ChainEvidence.lean` establish raw-input injection, labelled suffix merger, chain concatenation, last-step preimage dataflow and fixed-sum antichain. They pass the local pinned checker with only propext/Quot.sound; two dataflow lemmas are axiom-free. They do not establish preimage hardness, source extraction, the entire certificate classification or a numerical loss.

**PROVED — reviewed classical hidden-value event.** `hidden-values/DERIVATION.md` and `hidden-values-second-reader/REVIEW.md` give a separate continued input-oblivious coupling after joint privatization. Its safe public surface contains endpoints, FORS leaf images and public nodes, never hidden payloads. Predictable completed-call disclosure publishes FORS secrets and canonical WOTS suffixes permanently. New known points are installed only when fresh; old replies are never overwritten. The unflagged continued ideal history leaves remaining coordinates independent uniform. Agreement until the first hidden hit projects its probability to ordinary HJ. For fixed nonzero S, the event has bound min{1,(Q_H+3017)/2^128}; 3017 counts final protected-input calls, not all hash calls. This closes a classical statistical event lemma, not an efficient PRE reduction or Rust refinement.

## 4b. Canonical type-7 targets and setup completion

**PROVED — independently reviewed manual row sampler.** `canonical-targets/DERIVATION.md` and `canonical-targets-second-reader/SECOND_READER.md` disintegrate the full256 first-accepted counter row. On success, the canonical counter has the truncated geometric law, its accepted128 target is uniform in the sum slice, earlier same-child points are rejected, and later/other-child residuals remain uniform. Failed rows retain a bottom marker and have no target. Independent unused lower128 limbs preserve the complete-hash interface. The sampler has the exact ordinary joint function marginal, including prequeries; no old oracle answer is overwritten.

**PROVED — classical target event.** The graph determining each fixed child is independent of its own type7 restriction. All target metadata may be granted for this event alone. A different child/counter pair at a successful same-address row matches the canonical full128 digest with probability at most 2^-128 per fresh raw query. Earlier rejected points cannot match; canonical points are excluded. Honest source computation exposes no residual answers for free. For nonzero S and one final verifier with five digest checks, Pr[Bad7]<=min{1,(Q_H+5)/2^128}. Equal width4/8 digit vectors consume all128 bits and therefore imply this target equality. Full secret graph advice is an event-analysis extension, never the actual unforgeability game.

**COMPUTED and PROVED — cryptographic top-row completion.** The top sum slice has exactly 454918678781617793203528879683071744 elements among 2^128 possibilities. Let p_top be this exact ratio. The 2^21 top rows are independent conditional on the graph; tau_top=[1−(1−p_top)^(2^32)]^(2^21). A conservative exact inequality is 1−tau_top<=2^-5741859. This concerns grinding alone; allocation, scheduling and overflow/nontermination behavior are not certified. A complete unconditioned winning-event bound can be divided by tau_top for conditioning on this specific completion event; arbitrary completion filters need separate analysis.

## 4c. Observable quantum graph-target event

**CITED and PROVED — independently reviewed information-theoretic quantum branch.** `quantum-graph-targets/DERIVATION.md` and `quantum-graph-second-reader/SECOND_READER.md` apply Definition9/Theorem4 of Hülsing–Kudinov ePrint2022/346 to an explicit finite-register Bernoulli target factorization of the residual full256 oracle. A clean one-Boolean-query circuit simulates each full-function XOR query using independent value-pair tables and an unentangled |+> ancillary bit. The final classical verifier supplies an observable alternative-input target witness; no quantum query history is measured. Its selected types0–4 call cap is3217. Thus for fixed nonzero S, Pr[E_graph(final trace)]<=min{1,8(Q_q+3218)^2/2^128}; averaging uniform S can add2^-128. The finite circuit/factorization controls and independent review passed.

**OPEN — complete quantum composition.** The branch uses potentially exponential independent advice circuits and does not prove an efficient source reduction. The classical private-input and dynamic hidden-disclosure couplings do not extend by replacing Q_H with Q_q^2. QROM canonical-target binding is a new lane; private replacement, hidden values, FORS selection and complete quantum composition remain separate obligations.

## 5. Composition, rollback and quantum verdict

**PROVED — composition step actually supplied.** H0 is the exact source experiment in one shared RO. H1 is JOINT-IDEAL defined in section 2. For any bounded completed event, |Pr[H0]-Pr[H1]| is at most Delta_joint. Its source-dependent exclusions and manual coupling are explicit; the checked candidate-list arithmetic supports one substep.

**PROVED — complete manual classical RO composition, independently reviewed twice.** `CLASSICAL-RO-THEOREM.md` gives the exhaustive accepting-verifier split into covered FORS C, hidden genuine input H, alternative public graph image G, or canonical type7 target D7. Both independent composition readers saved their source-derived classifications before reading the immutable draft. Separate event bounds project to ordinary HJ; their advice views are never merged. Fixed-nonzero-S component bounds are averaged and the S=0 branch is paid once. For N=2^128, q initiated calls and Q_H adversarial raw queries, the accepted reference bound is

\[
 \epsilon_{\rm RO}\le\min\left\{1,
 \frac{6Q_H+3q+6243}{N}
 +\frac{qQ_H+\binom q2+q}{N^2}
 +q(511/512)^{2^{32}}+(Q_H+1)p_F(q)\right\}.
\]

**PROVED — theorem boundary.** This bounds winning probability in the full verifier experiment of the stated partial, atomic, honest-cache classical RO model. It does not construct an efficient generic PRF/SPR/TCR challenge reduction or a checked Rust refinement, nor certify a work-factor level. The symbolic game steps are H0 actual shared RO, H1 joint F/J ideal with its charged distance, then an event partition on the SAME ordinary H1. No blinded hidden continuation is substituted into the partition. Numerical classical-total fields now contain this reviewed expression; quantum-total fields remain null.

**PROVED — conditional rollback statement.** In the parent honest-cache atomic interface, deterministic cache transparency gives zero probability/signing-query transfer loss. Thus any established reference epsilon would transfer unchanged apart from simulator time overhead. The accepted epsilon_RO above now transfers within the same declared classical RO model; efficient/full-QROM and level1 certification remain open. Arbitrary accepted-counter corruption already refutes the broader all-cache-state transparency claim; cached bytes are not publicly reconstructible merely because the signer can recompute them from sk.

**COMPUTED — numerical separation.** `bounds.py` recomputes all eight requested q values, binomial/Poisson and positive recurrence checks, exact joint-loss arithmetic and conditional coverage-budget arithmetic. With Q_H=2^128 the joint distance bound is 1. The 132.563419944 FORS per-candidate exponent at q=2^40 yields only 4.563419944 in the conditional Q_H-budget arithmetic, not a 128-bit complete success bound. A vacuous conservative bound is neither an attack nor evidence of failure of the work-factor target.

**OPEN — full quantum.** One observable graph-target branch now has a reviewed exact quantum query bound in section4c. The remaining complete QROM game is open. A superposition query is not one literal key guess, and the scalar continued-ideal disclosure argument needs a new quantum proof. Plain Grover interpretation remains a component reading; no universal ten-bit loss, full quantum limit or category-1 certificate follows. K tools remain unavailable in the inspected live distributions; no global install or private source upload is undertaken.

**OPEN — printable level/category statement.** “Classical level1 and complete QROM security of this LULA I instantiation are not established. The specified classical RO experiment has a reviewed advantage upper bound; honest-cache rollback preserves that reference signing interface.”


**CITED and PROVED — reviewed quantum canonical-target branch.** `quantum-canonical-targets/INDEPENDENT_DERIVATION.md` and `root-canonical-quantum-review/SECOND_READER.md` extend the exact successful/failed row sampler with independent Bernoulli residual markers. Earlier rejected points are masked, full256 values are preserved, and a clean one-query circuit yields an observable finaltype7 target witness. The reviewed event bound for fixed nonzero S is min{1,8(Q_q+6)^2/2^128}. This is another event branch, not a complete QROM theorem. Dynamic hidden-value disclosure and joint-private quantum replacement are current separate lanes.

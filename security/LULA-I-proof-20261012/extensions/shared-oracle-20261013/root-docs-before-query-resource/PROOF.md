# LULA I shared-oracle proof extension

**OPEN — original level/category objective.** Classical level1, category1 and certified signing capacities are not established. Complete manually reviewed advantage upper bounds now exist for the explicitly specified classical RO and finite-QROM source games. This extension advances the frozen parent obligations without paper/source edits; it does not identify a query-model theorem with fixed-SHA or efficient generic primitive certification.

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

**OPEN — efficient simulation and category scope.** The separate event search reductions use potentially exponential independent advice circuits. Source-specific private replacement, dynamic hidden disclosure, sequential FORS coverage and the complete common-game quantum union are now manually reviewed. Efficient generic embeddings, checked source refinement and level/category certification remain distinct obligations; no classical guessing argument is substituted for coherent queries.

## 4d. Quantum joint private-input replacement

**PROVED — manually reviewed finite-QROM hop.** `quantum-private-frontier/DERIVATION.md` and the independently source-derived `quantum-private-second-reader/REVIEW.md` supply a full256 coupling on the disjoint private families. In the continued ideal game K/P are unused even by the quantum state. A coherent query has averaged private-support mass at most 1/N and purified local norm difference at most 2/sqrt(N). Classical, dephased honest services contribute at most two P nominations per initiated call and two at final verification. CPTP contraction evaluates local discrepancies on IDEAL prefixes. For fixed nonzero S,

    delta_private_Q <= min(1, 2Q_q/sqrt(N) + (2q+2)/N).

**PROVED — seed and interface.** Averaging uniform S adds at most 1/N once. The standalone unconditional expression has 2q+3 instead of 2q+2. Coherent signing, private state disclosure, timing, corruption and efficient reduction are excluded. At Q_q=2^64 the sufficient distance bound caps at one; this is not a forgery or a category statement.

## 4e. Dynamic quantum hidden-input final event

**PROVED — manually reviewed twice.** `DYNAMIC-QUANTUM-HIDDEN-THEOREM.md` retains the immutable draft checked by `quantum-hidden-second-reader/SECOND_READER.md` and `quantum-hidden-frontier/SECOND_READER_OF_ROOT.md`. Its time-dependent ghost masks still-hidden genuine points and overlays their full images after completed disclosure. WOTS disclosure closes the entire forward suffix by coordinate labels. Remaining coordinates are independent of retained ghost quantum memory; no survival conditioning or retroactive memory overwrite is used. Both honest services use the same private graph. Packing their common dilations between Q_q queries gives purified vector gap at most 2Q_q/sqrt(N).

**PROVED — common stopped examiner.** The final classical verifier stops before its first genuine, still-hidden input. Prior replies agree, so this is a common terminal channel. An unflagged ghost trace supplies at most 3017 nominations: 17 FORS plus 4*(32*15-240) lower-chain plus (16*255-2040) top-chain calls. Its probability is at most 3017/N. The square-root success inequality proves, for fixed nonzero S,

    Pr_HJ[H_final] <= min(1, (2Q_q+sqrt(3017))^2/N).

**OPEN — scope.** This is an observable final event in ordinary HJ, not a measured history of quantum hits, a complete EUF bound, efficient PRE reduction or checked Rust refinement. The full-secret graph used in other event proofs is not fed to this hidden-value game.

## 4f. The requested SPR-only WOTS premise

**PROVED — generic assumption implication refuted.** `SPR-ONLY-COUNTEREXAMPLE.md` uses an injective identity chain family with zero second-preimage advantage and a public inverse. All positions expose the same chain start; distinct fixed-sum digit vectors share identical signing blocks and endpoints. Four algebraic declarations check in `root-formal/SPRSeparation.lean`, with a zero-exit receipt. This is not an actual SHA-256/LULA I forgery. A generic WOTS theorem needs a genuine-predecessor one-way assumption; the separate RO theorem supplies a hidden-input event instead.

## 5. Composition, rollback and quantum verdict

**PROVED — composition step actually supplied.** H0 is the exact source experiment in one shared RO. H1 is JOINT-IDEAL defined in section 2. For any bounded completed event, |Pr[H0]-Pr[H1]| is at most Delta_joint. Its source-dependent exclusions and manual coupling are explicit; the checked candidate-list arithmetic supports one substep.

**PROVED — complete manual classical RO composition, independently reviewed twice.** `CLASSICAL-RO-THEOREM.md` gives the exhaustive accepting-verifier split into covered FORS C, hidden genuine input H, alternative public graph image G, or canonical type7 target D7. Both independent composition readers saved their source-derived classifications before reading the immutable draft. Separate event bounds project to ordinary HJ; their advice views are never merged. Fixed-nonzero-S component bounds are averaged and the S=0 branch is paid once. For N=2^128, q initiated calls and Q_H adversarial raw queries, the accepted reference bound is

\[
 \epsilon_{\rm RO}\le\min\left\{1,
 \frac{6Q_H+3q+6243}{N}
 +\frac{qQ_H+\binom q2+q}{N^2}
 +q(511/512)^{2^{32}}+(Q_H+1)p_F(q)\right\}.
\]

**PROVED — theorem boundary.** This bounds winning probability in the full verifier experiment of the stated partial, atomic, honest-cache classical RO model. It does not construct an efficient generic PRF/SPR/TCR challenge reduction or a checked Rust refinement, nor certify a work-factor level. The symbolic game steps are H0 actual shared RO, H1 joint F/J ideal with its charged distance, then an event partition on the SAME ordinary H1. No blinded hidden continuation is substituted into the partition. Numerical classical-total fields contain this reviewed expression. Separate quantum-total fields now instantiate the independently accepted finite-QROM theorem below.

**PROVED — conditional rollback statement.** In the parent honest-cache atomic interface, deterministic cache transparency gives zero probability/signing-query transfer loss. Thus any established reference epsilon would transfer unchanged apart from simulator time overhead. The accepted epsilon_RO above now transfers within the same declared classical RO model; efficient embeddings and level1/category1 certification remain open; the separately reviewed finite-QROM model transfer is given below. Arbitrary accepted-counter corruption already refutes the broader all-cache-state transparency claim; cached bytes are not publicly reconstructible merely because the signer can recompute them from sk.

**COMPUTED — numerical separation.** `bounds.py` recomputes all eight requested q values, binomial/Poisson and positive recurrence checks, exact joint-loss arithmetic and conditional coverage-budget arithmetic. With Q_H=2^128 the joint distance bound is 1. The 132.563419944 FORS per-candidate exponent at q=2^40 yields only 4.563419944 in the conditional Q_H-budget arithmetic, not a 128-bit complete success bound. A vacuous conservative bound is neither an attack nor evidence of failure of the work-factor target.

**PROVED — complete finite-QROM source-game bound, independently reviewed twice.** `QUANTUM-RO-THEOREM.md` composes the corrected sequential FORS source bound with the reviewed private/H/G/D7 terms. The accepting final-verifier classification is pathwise on classical outputs, so it applies to quantum-produced signatures. All event inequalities refer to ordinary HJ; event-only advice views are kept separate. q counts initiated requests over all branches; Q_q counts adversarial coherent complete-hash calls. Full256 images, partial noncompletion and one uniform seed-zero charge are retained.

**OPEN — printable level/category statement.** “Classical level1 and quantum category1 security of this LULA I instantiation are not established. The specified atomic honest-cache RO and finite-QROM experiments have independently reviewed winning-probability upper bounds; honest restoration preserves their reference signing interface.”


**CITED and PROVED — reviewed quantum canonical-target branch.** `quantum-canonical-targets/INDEPENDENT_DERIVATION.md` and `root-canonical-quantum-review/SECOND_READER.md` extend the exact successful/failed row sampler with independent Bernoulli residual markers. Earlier rejected points are masked, full256 values are preserved, and a clean one-query circuit yields an observable finaltype7 target witness. The reviewed event bound for fixed nonzero S is min{1,8(Q_q+6)^2/2^128}. This is another event branch, not a complete QROM theorem. The accepted dynamic hidden-value and private-input lemmas are separate source-game branches; the remaining coverage/composition gate stays open.

## 5a. Explicit complete finite-QROM formula

**PROVED — reviewed source-model theorem.** Put N=2^128, M=N^2-N and let p_F(q) be the exact binomial raw-candidate coverage probability. All following local terms are capped at one.

    delta = min(1,2Q_q/sqrt(N)+(2q+2)/N),
    D = min(1,q*(sqrt((Q_q+q+1)/M)+(Q_q+q+1)/(2M))),
    A = min(1,D+8*(Q_q+2)^2*(p_F(q)+1/N+q/N^2)),
    c = min(1,(2Q_q+sqrt(q))^2/N
               +(2*(Q_q+2)/sqrt(N)+sqrt(A))^2),
    h = min(1,(2Q_q+sqrt(3017))^2/N),
    g = min(1,8*(Q_q+3218)^2/N),
    d7 = min(1,8*(Q_q+6)^2/N),
    epsilon_QROM <= min(1,1/N+delta+c+h+g+d7).

**PROVED — review and transfer.** `quantum-composition-numeric/CONDITIONAL-GATE-CLOSED.md` and `quantum-composition-second-reader/SECOND_READER.md` accept the complete common-game theorem and opaque honest-cache transfer. `QUANTUM-COVERAGE-THEOREM.md` resolves fresh-row collision reads and whole-BASE-function sampling before adaptive selection. Honest atomic restoration has zero probability/query transfer loss in this model; private bytes, arbitrary corruption and total abort/retry remain outside it.

**COMPUTED — numerical scope.** bounds.py produces all eight q rows at Q_q=2^32 and2^64. At q=2^40,Q_q=2^32 the conservative total exponent is about31, dominated by private query distance; every Q_q=2^64 total caps at one. These are probability upper-bound exponents, not work-factor levels or attacks. `quantum-composition-numeric/ROOT-CROSSCHECK.json` verifies all16 current rows,176 probability components and112 exponents against independently saved240-digit data, including current script/theorem/output hashes.

**PROVED — tighter private event bound, separately reviewed.** QUANTUM-EVENT-SPECIFIC-THEOREM.md closes the stopped-source active-prefix gate and uses one common B-or-W projector. It preserves the conservative theorem and improves its rare winning-event probability; it does not claim a smaller general trace distance. Physical CQ block domination is unnormalized, not an operator-order assertion for arbitrary purifications.

## 5b. Strongest currently reviewed finite-QROM expression

**PROVED — source-event refinement.** Let e=min(1,c+h+g+d7) use the SAME ordinary fixed-nonzero HJ event bounds above, and let b=min(1,(2q+2)/N). The common stopped-source projection gives

    epsilon_event <= min(1,1/N+[2Q_q/sqrt(N)+sqrt(min(1,b+e))]^2),
    epsilon_best = min(epsilon_QROM_conservative,epsilon_event).

Both component theorems are independently reviewed within their finite source model. The private alias flag is detected only before honest/final classical hashes; coherent queries are never measured. The faithful REAL winner lies in stopped B-or-W, while its IDEAL probability is at most b+e in the unflagged HJ continuation. One purified vector gap is paid, and seed-zero remains charged once. Honest opaque atomic cache transfer still has zero probability/query loss.

**COMPUTED — reproducible refined numbers.** Run bounds.py for the preserved conservative components and then bounds-event-specific.py with that result JSON as --base. The two refined output tables are root-checks/refined-Qq32 and refined-Qq64. The independent rare-lane ROOT-REFINED-CROSSCHECK verifies all16 rows,96 numeric fields and64 exponents against its earlier240-digit dataset. At q=2^40,Q_q=2^32 the refined exponent is57.683359869309; at q=2^41 it is56.873275107725. Every Q_q=2^64 refined total still caps at one. Serialized-input high-precision evaluation is disclosed; this is not certified directed rounding or an attack-cost estimate.

**OPEN — security criterion.** Root-preimage-criterion lanes are independently testing whether the original tiny-failure thresholds at maximum search budgets are compatible with the fixed source verifier. A preliminary publicly constructed signature skeleton turns the last top authentication sibling into a root-preimage problem, but its complete residual-row/source projection requires review. No actual SHA search was executed. This is separate from the conventional128-bit work-factor question.

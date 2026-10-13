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

**PROVED / OPEN — reduction boundary.** Section8 supplies explicit source-relative ROM joint-access private adapters and finite resources; conventional PRF identification and later generic challenge embeddings remain open. Public message/node/hash domains remain one shared O_pub, not independent primitive oracles. This private replacement alone is one component; the complete classical/QROM bounds are in Sections5–5b. A checked Rust refinement remains additional assurance, not an original completion prerequisite.

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

**PROVED / OPEN — FORS route boundary and successor.** This source-bound coverage route alone does not imply that every accepted forgery is covered. Unknown leaf acquisition, changed-node/root evidence and the complete composition are accounted for by the separately reviewed H/G/D7 split in Sections5–5b. Generic primitive embeddings remain open; no proof assistant has verified the full source/channel refinement.

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


**CITED and PROVED — reviewed quantum canonical-target branch.** `quantum-canonical-targets/INDEPENDENT_DERIVATION.md` and `root-canonical-quantum-review/SECOND_READER.md` extend the exact successful/failed row sampler with independent Bernoulli residual markers. Earlier rejected points are masked, full256 values are preserved, and a clean one-query circuit yields an observable finaltype7 target witness. The reviewed event bound for fixed nonzero S is min{1,8(Q_q+6)^2/2^128}. This is another event branch, not a complete QROM theorem. The accepted dynamic hidden-value and private-input lemmas are separate source-game branches; the complete coverage/composition successor is proved in Sections 5a–5b below. Historical open-status sentences in the pinned reviewed component/theorem files are superseded by this live index, without altering their review hashes.

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

**OPEN — optional criterion-obstruction investigation.** The root-preimage criterion proposal is unpromoted: its abstract probability argument has a completed narrow review, but its operational source-binding delegation was filtered and supplies no acceptance. That proposed attack is not an original proof deliverable or a new completion prerequisite. The exact bound no-crossing statement in Section 6 answers the requested arithmetic for the supplied estimates without an attack. Conventional level/category certification remains separate and open.

## 6. Original tiny-failure gates and constant-success query resources

**PROVED — exact no-crossing of the supplied sufficient bound.** For N=2^128, q>=0 and Q_H>=0, the classical uncapped sum is at least6243/N. Since N>6243>1, its cap at one is strictly greater than1/N. Consequently there is no q for which this supplied sufficient expression reaches the original failure target2^-128, even at Q_H=0. At Q_H=N the6Q_H/N term makes its cap exactly one. At Q_q=sqrt(N), the quantum vector term2Q_q/sqrt(N)=2, so both reviewed quantum envelopes, and their minimum, equal one for every q. Indeed they already equal one at Q_q>=2^63. These are statements about sufficient bounds, not adversarial success lower bounds, an attack, or proof that a tighter adequate bound is impossible.

**PROVED — original scope.** Exact manual source/game verification and reduction programs are required; a fully mechanized Rust/compiler/channel theorem is additional assurance, not a new original requirement. Likewise an operational source-valid attack was introduced as a follow-up and is not a proof-completion condition. The original level/category and generic-program obligations are retained, not replaced by these arithmetic observations.

**PROVED — query threshold semantics.** Fix q and the same source parameters. The reviewed classical, conservative quantum and event-specific envelopes are nonnegative nondecreasing functions of the adversarial query cap Q; their minimum is nondecreasing. For target1/2, adjacent integers K,K+1 with upper_bound(K)<=1/2<upper_bound(K+1) certify the largest integer for which this bound proves success at most1/2. A failed sufficient gate is not an attack. Seven supporting order declarations check in query-resource-formal/QueryThreshold.lean under Lean4.28.0; actual scalar-formula monotonicity is manually proved in its independent derivation, not mechanized by that abstract file.

**COMPUTED — exact outward arithmetic.** query-resource-independent/thresholds.py computes32 adjacent crossings using exact rational operations, inherited independent exact-binomial FORS dyadic enclosures, and1024-bit outward square roots by integer isqrt. It encloses finite-counter exhaustion rather than dropping it. Separate affine inversion and128/256-bit interval checks agree. query-resource-root/check.py independently evaluates all32 endpoints at240 decimal digits and checks their saved exact rational margins. The printed logarithms below are approximate display values; the gates use the integer/rational certificates.

| Initiated signing cap | Classical log2(Q_pass), approximate | Best quantum log2(Q_pass), approximate |
|---:|---:|---:|
| 2^24 | 124.415037499279 | 60.423340767617 |
| 2^30 | 124.415037499279 | 60.423340767617 |
| 2^38 | 124.415031382251 | 60.423336537424 |
| 2^40 | 124.404903734342 | 60.416375433175 |
| 2^41 | 123.638290418704 | 59.998503957389 |
| 2^44 | 97.521203039111 | 47.260537854946 |
| 2^50 | 19.122188486068 | 8.049848549451 |
| 2^64 | 7.988684686772 | 1.584962500721 |

**COMPUTED — exact q40 endpoints.** At q=2^40, the classical sufficient bound passes Q_H=28158377811508036555700208997110311281 and fails the next integer. The best quantum bound passes Q_q=1538654937033492218 and fails the next integer. At this constant-success target the conservative theorem is stronger than the rare-event theorem; the valid minimum retains both. This does not contradict the rare-event improvement at Q_q=2^32.

**OPEN — printable security verdict unchanged.** These thresholds bound every adversary in the specified query model up to the declared constant success criterion; their logarithms are not certified work factors, AES resource comparisons, fixed-SHA guarantees or NIST categories. Original classical level1/category1 and certified signing capacity remain not established. The same reference probability bounds transfer with zero probability/query loss to the honest opaque atomic cached interface; broader public-cache and corrupt-cache demands remain distinct.


## 7. Exact public logical top-cache observer

**PROVED — reviewed direct view extension.** CACHE-PAYLOAD-THEOREM.md extends the complete source-model bounds to a setup response `(pk,L)` with exactly the2^22−1 top compressed/Merkle nodes and2^21 first-accepted counters. This75,497,456-byte logical payload contains no seed, chain predecessor, child-root array or message-randomizer table. Failed setup stays absorbing/nonwinning; pre-key queries and retained quantum memory remain allowed. The statement preserves the actual joint counter/function distribution rather than sampling independent geometric counters after seeing a public root.

**PROVED — independent component projections.** For the private hop the payload is a common setup channel generated from F and the public oracle, leaving unused IDEAL K/P untouched. For H, nodes are in the safe public surface and canonical counters depend only on that surface and outside type7 rows, not hidden predecessor/FORS coordinates. For C they are outside data independent of J and the inner/outer challenge planes. For G/D7 they are projections of each event's already permitted advice. The separate stronger views are never merged. The same ordinary payload-disclosed HJ final split and scalar formulas therefore apply, with no additional exposure term. This is not an assertion that disclosed and opaque adversaries have equal optimal advantage.

**PROVED / COMPUTED — disclosure limits.** The private persistence driver adds117 bytes of framing, including the entire48-byte seed at offsets8–55:32 secret K/P bytes and16 public S bytes. Its75,497,573-byte whole-signer fixture is excluded. The pk-only/no-oracle ideal predictor control has first-leaf accuracy1/N; it does not rule out an efficient oracle-access simulator. Neither an external pk-only simulator nor security of arbitrary seed/context/work-buffer disclosure is supplied or needed for this direct logical-payload theorem. Arbitrary corruption retains the known canonicality counterexample.

**COMPUTED — controls and review.** Independent source and mathematical derivations precede reciprocal readings. The math control enumerates524,288 worlds and32,768 complete observer groups, retains counter/child dependence and checks negative seed/working-value views. The source peer independently reviews every private/H/C/G/D7 compatibility condition and pins the native library/fixture serializer. These finite controls support sampler identities, not a full quantum/source mechanization.

## 8. Explicit ROM-relative private challenge programs

**PROVED — exact program identities.** PRIVATE-REDUCTION-PROGRAMS.md supplies B_K and B_P for sequential G0→GK→GKP. Each challenger provides the SAME raw full256 O as its real private restriction, or an independent memoized private map. The adapters forward pre-key Raw with S/pk withheld, preserve A's continuation, run setup, release pk and resume under one Q_H cap. `pre_key` abort is nonwinning. Exhausted distinct32-bit searches are totalized to nonwinning, without claiming a native Rust abort. Verification checks the reconstructed root against pk.root and permanent freshness. Memoization preserves exact repeated-label outputs.

**COMPUTED / PROVED — private resources.** Prepared setup needs2,181,038,080 distinct Derive addresses. The persistent B_K cap is min(19,212,937,084,272,640,2,181,038,080+33,567,232q) for cold signing, or min(19,212,937,084,272,640,2,181,038,080+12,816q) for prepared signing. B_P makes at most q Randomizer calls; the final verifier makes none. Full source-relative Raw, byte-length-dependent time and storage envelopes, and all eight requested q columns, are in the program/count report. They count honest simulator work separately from adversarial raw-query caps.

**PROVED — challenge meaning and unchanged numerical bound.** These are named ROM-relative joint-access challenges. At fixed nonzero S the decision-bit probability differences equal their corresponding challenge advantages; uniform S=0 is charged once. Their sequential statistical bounds are looser than the existing joint coupling, so bounds.py and all accepted complete probability tables remain unchanged. The challenge is not silently identified with a conventional independent-oracle PRF.

**PROVED — payload-aware adapters.** For the Section7 disclosure interface, the same setup adapters already construct the exact top node/counter vectors and can return only L with pk. They never return fcache, private seeds, context or working chain values. Copying L adds no private challenge or raw oracle call; its fixed copying cost fits the displayed source-relative resource envelope. This is an internal challenger adapter using private interfaces, not an external simulator from pk alone.

**PROVED / COMPUTED — limited mechanization.** Five new EasyCrypt helpers check abstract routing self-equivalences and integer resource inequalities. They do not check the full B programs or the Rust interpreter. A source-first peer accepts the final program's phase ordering, raw correlation, finite partiality contract and source-derived counts. Conventional PRF certification, selected-address PRE/SPR/TCR embeddings and level/category certification remain open.

## 9. Localized selected-address graph challenge

**PROVED — reviewed explicit finite RO-relative program.** SELECTED-GRAPH-REDUCTION.md commits the genuine selected payload before releasing its independent full256 addressed restriction. A fixed56-bit padded selector chooses among39,339,469,515,522,047 type0–4 domains; dummy ranks fail. For nonzero S, the completed winning final-trace event obeys Pr[B_cond wins]=2^-56 Pr[Win AND G_final | S!=0]. Pre-key access, actual setup, immutable logical-payload response, initiated signing, permanent freshness and absorbing noncompletion are preserved. Coherent raw queries can be routed with one selected and one outside call, without extracting their history; only the final classical verifier witness is used. The quantum statement is a manual finite-adapter identity, not a mechanically verified quantum program.

**COMPUTED — resources without a full-forest materialization.** The largest strict predecessor cone takes8,560,574,462 public calls and33,554,432 private starts. The final five-subtree/17-tree routed extraction takes8,560,653,547 public calls and33,567,232 private starts. Classical selected-handle calls are at most Q_H+2q+4 at nonzero S; total public/private/time/message-length/storage caps are in the artifact. This does not make8.56B hashes practical or establish PPT in a growing-height family. The full-source seed-zero contribution is charged once, not once per adapter. The localized result excludes the broader adversarial-ever-query G event and the S=0 off-route raw alias.

**OPEN — conventional identification.** This selected challenger retains outside raw restrictions, commits an outside-dependent payload and releases its independent missing restriction afterwards. No equivalence with an ordinary single-key SPR/TCR game, real SHA family or category/resource target is claimed. The direct reviewed graph scalar bound remains stronger than this large selection-loss fallback; no calculator or probability table is changed.

## 10. Changed-child extraction at canonical WOTS rows

**PROVED — reviewed pointwise refinement.** CHANGED-CHILD-EXTRACTION.md proves Win subset C_cov union H_final union G_final union D7_base, where D7_base requires a reached honestly exposed successful canonical row, a genuinely changed child V*!=C_A, and equal complete128-bit digests. Genuine exposures are indexed by address, chain and position. Absent G/H, path and chain descent force equal accepted digit vectors; equal target sums then force equality coordinatewise. An unexposed key cannot have all digits terminal because240<480 and2040<4080. If the reconstructed child is already genuine, descent continues regardless of counter equality; no counter-only collision term is required there. The argument applies pointwise to quantum-produced classical signatures.

**PROVED / CITED / OPEN — consequence and boundary.** D7_base is a subset of the earlier D7_full event, so its conservative classical/QROM terms still apply unchanged. The changed-base predicate agrees with the necessary message-change clause in SPHINCS+C DefinitionC.1 (2022/778), but chronology, common parameter, side-oracle, acceptance selection and partiality still need a legal standard challenger embedding. The proof is manually reviewed, not a new machine-checked source theorem. Genuine-hidden-predecessor PRE simulation and conventional primitive identification remain the next original obligations.

## 11. Classical stopped hidden-input PRE program

**PROVED — reviewed first-event embedding.** CLASSICAL-PRE-REDUCTION.md supplies an explicit B_PRE for the ordinary joint-private HJ experiment at nonzero S. A full256 selected random-function PRE challenge hides a uniform16-byte X and gives its full image Y. At an interior WOTS cut, the genuine predecessor's latent full response is `(X,independent lower limb)`. The executable reduction never fabricates this unknown word: it stops before its public response and uses the known image prefix to reconstruct the chain's suffix and endpoint internally. An honest completed signature that would disclose X also stops before its response. On the source prefix whose first hidden hit has the selected coordinate, neither stop has occurred. That query yields a full-image PRE answer. An r=0 WOTS or real-FORS cut similarly keeps the selected ideal-F prefix opaque and uses its known public image. All normal source metadata, public payload, pre-key phases, partiality and byte correlations are preserved on the coupled surviving prefixes.

**PROVED / COMPUTED — exact loss and resources.** There are1,089,588,072,284,160 WOTS nonterminal coordinates and19,140,298,416,324,608 real FORS secret coordinates. Fixed55-bit padding gives Pr_HJ[H | S!=0]<=2^55 Pr[B_PRE wins]. This is an inequality, since other preimages can also produce reduction wins. The WOTS-only program has a separate2^50 loss. Both localized branches use at most Q_H+1 selected calls,254 extra ordinary hashes and4096 extra node bytes, plus the already charged source setup/sign/private/memo/message storage. No whole hidden forest is generated. A skip-on-S=0 variant avoids nonzero-seed rejection sampling; composition still charges the original zero branch once. H_final is covered by this broader classical first-event bound. The direct reviewed H probability estimate is sharper and still drives every calculator/table.

**OPEN — classical scope is not quantum or conventional certification.** The challenge supplies a selected addressed random restriction, with outside functions locally simulated; it is not the previous externally fixed Raw_out challenge. A conventional shared-seed SHA PRE identification is not supplied. Checking and stopping a coherent query at the predecessor would change that query, so the classical program does not close a QROM PRE embedding. The existing complete finite-QROM theorem is independently established by its direct hidden-event lemma and remains unchanged. No level/category/capacity statement, parameter repair or implemented attack follows.

## 12. Coherent prefix-blinded hidden-input PRE program

**PROVED — independently reviewed finite QROM-relative adapter.** QUANTUM-PRE-REDUCTION.md removes every genuine point program in the selected WOTS hidden prefix, while the source comparator keeps them. The executable BLIND oracle returns one fixed outside function and the unchanged selected PRE restriction; honest selected-chain endpoints/suffixes use the supplied image. It stops before completed disclosure at or below the cut. Its active physical CQ query block leaves all prefix words independently uniform and unused, without conditioning on source survival or an entire private F map. Distinct literal headers make averaged marked input mass at most1/N, not r/N. Packed query telescoping gives2Q_q/sqrt(N) vector discrepancy for an interior selector, with trivial cap2; WOTS r0 and FORS selectors have zero discrepancy. No coherent query is measured.

**PROVED — common classical final guard.** After A's classical output, final verification stops before replying at any known selected-prefix genuine input and succeeds on a selected fullimage PRE match. On the source trace whose first final hidden input is the selected coordinate, neither an earlier exposure stop nor that guard occurs. The same terminal projector therefore bounds the source event by the BLIND PRE success and the vector discrepancy. Nongenuine prefixes that merge later are included; no absence-of-G assumption is needed.

**PROVED / COMPUTED — exact mixture and counted resources.** For L=2^55, N=2^128 and D_int=1,016,949,404,336,128 interior WOTS coordinates, Pr_HJ[Win AND H_final | S!=0]<=min(1,(sqrt(L p_PRE)+2Q_q sqrt(D_int/N))^2). The cross term contains sqrt(L). The challenge receives Q_q coherent calls and at most one final classical call; the router uses one selected and one outside call per raw query, with inactive plus-state response registers. Honest source calls remain separately counted. The explicit eager outside table costs32V_b storage,256V_b random bits, O(32V_b) initialization and O(V_b(b+32)) gates per coherent lookup; all public classical calls use that same table. This finite implementation is exponential in maximum input length and no PPT/practical claim is made.

**PROVED / COMPUTED / OPEN — precise closure.** The finite coherent PRE program/resource sub-obligation is now closed in its stated interface, independently reviewed. Seven local Lean supporting algebra/count declarations checked with only standard axioms; none verifies the full source/QROM program. The old direct hidden term (2Q_q+sqrt(3017))^2/N is sharper and remains the term in all complete bounds. Conventional shared-seed PRE identification, efficient outside simulation and actual level/category/capacity still need evidence. The selected acceptance-row type7 challenge is the next original program obligation.

## 13. Acceptance-selected canonical type7 row program

**PROVED — independently reviewed source-relative interface.** TYPE7-REDUCTION-PROGRAM.md registers the fixed genuine child C before its own type7 restriction Row is sampled. The challenger retains one ordinary full256 function, returns its first accepted32-bit counter and full target word, or bottom on finite exhaustion. B runs the source pre-key/setup/signing/final phases with that same Row/outside function and memoizes only the supplied canonical target. Earlier rejections, lower limbs, off-base/off-length responses and public-cache counters remain correlated exactly. Canonical child construction uses no type7 input, so registration is not circular.

**PROVED — event and partiality.** Original D7_base_final remains a final reached honestly exposed successful row, different child V*!=C and equal complete128-bit digit digest. The larger optional classical-query event is named D7_base_public; a primitive collision found early may increase B's success but does not remove the original exposure restriction. The unflagged simulation has source law, while actual extraction preserves only the source prefix until stopping. Selected-row bottom gives B-local failure and zero selected-event mass, not an added source abort or normalization on global completion. No unknown value, coherent query-history test or prefix blinding is needed.

**PROVED / COMPUTED — exact finite loss/resources.** The2,269,959,421,952 WOTS rows fit a fixed42-bit selector; dummy indices fail. Pr_HJ[Win AND D7_base_final | S!=0]<=2^42 Pr[B_ROW_quantum wins]. B has at most Q_q coherent selected calls plus one final classical call, or Q_H+1 in the classical program. Target preprocessing<=2^32 own-function calls is separately charged. One child cone costs at most17,392 public hashes and8,704 F labels; the top row certifies a lower height5 child, so no height21 preparatory tree is required. Complete source/private/table/time/node envelopes and all eight q resource columns are in the artifact. Full256 replies are retained despite the128-bit collision predicate. Seed-zero is paid only once outside the conditional component union.

**OPEN — ordinary-family identification and capacity.** This acceptance-row/oracle interface is not silently called standard S-TCR for a shared-seed SHA family. Its chronology, allowed side functions and finite first-selection target still need exact equivalence. The program does not tighten the direct D7 term, replace any numerical table, certify a security level/category or supply efficient coherent outside evaluation. It closes the finite relative challenge-program sub-obligation, not those remaining gates.

## 14. Bounded-query efficient outside simulator

**PROVED / CITED — efficient bounded-query B-only successor.** OUTSIDE-SIMULATOR-THEOREM.md supplies the deterministic direct binary-tower polynomial family and exact bounded-query replacement for the existing PRE/type7 reductions. All honest source calls are included in T, and initialization, uniform circuit generation, clean reversible evaluation and storage are charged. The complete source probability formulas and old tables remain unchanged. Conventional primitive identification, level/category and certified capacity remain OPEN; no new kernel security theorem is claimed.

## 15. Fixed-public-hash canonical collection component

**PROVED / ASSUMED — fixed-public-hash canonical collection successor.** STANDARD-CANONICAL-COMPONENT.md gives an independently reviewed source-specific type7 wrapper under the explicitly chosen CF-BS-TCR-collection(h,Prop,2^32) property. Other-tweak collection access computes the genuine child before parameter release. Canonical-first BE32 selection is a legal specialization; equivalence for all accepted-counter policies is not required. Finite bottom and full same-hash correlations are retained. Lower/top fixed predicates yield the unconditional nonzero-seed component 2^42 SuccProp4+2^21 SuccProp8. This is HJ[h], not an equality to the old HJ[O] experiment. All reduction work is charged; quantitative fixed-SHA/collection/full-security bounds remain OPEN.

**PROVED / COMPUTED — limited mechanized addition.** Four independently reexecuted Lean declarations establish only a synthetic counter-policy separation. Cumulative supporting declarations are44, with zero new whole-source/game security declarations. The original scalar theorems, calculators, source and paper are unchanged. Restricted-row QROM and one-query completion candidates remain separate and are not acceptance evidence for this successor.

## 16. Ordinary private families under a fixed public hash

**PROVED / ASSUMED — ordinary fixed-public-hash private adapters.** PRIVATE-FIXED-H-REDUCTION.md closes the exact source-relative ordinary public-parameter PRF hop interface: pReal_h <= pFJideal_h+Adv(f;B_K)+Adv(g;B_P), with all full public hashes computed by the same h, literal aliases including seed-zero, classical private queries and quantum public computation. Signed gaps/public-parameter averaging and reduction-versus-challenger costs are explicit. Private-family hardness is ASSUMED; no RO expression is substituted for the remaining fixed-hash pFJideal_h. Prefix private assumptions do not certify the lower128 H_msg route bits. The smallest remaining obligation is a fixed-hash full-output/adaptive-selection/public-graph bound.

## 17. Restricted canonical full-RO target and one-query completion

**PROVED / CITED — restricted linked-global-RO canonical target bound.** RESTRICTED-CANONICAL-QROM.md preserves pretarget other-tweak child computation, first literal BE32 acceptance, full same-function target/outside correlations and bottom mass. The independently reviewed one-query Fourier completion yields U(M)=min(1,8(M+1)^2/2^128), using SPHINCS+C TheoremE.3. A NEW pre-digest stopping extractor has M<=Q; the preserved final-evaluation program still has M<=Q+1. The unconditional source type7 component is at most min(1,(1-1/N)(2^42 tau4+2^21 tau8)U(Q)). All honest runtime/global evaluation costs remain charged separately. This restricted component neither replaces the stronger old direct D7 bound nor changes the old complete probability numerics or certifies fixed SHA/category/capacity. Supporting checked declarations stay44, with zero newly checked whole-source/game declarations.

## Fixed-h message, graph and symbolic-composition successor

**PROVED / ASSUMED — ordinary message-hash lifting.** MESSAGE-HASH-ORDINARY-LIFT.md supplies a legal loss-aware ordinary ITSR adapter for the exact total rank-encoded H_free family, retaining completed source responses, memoized nonces, all literal full-h words and adaptive quantum public computation. Dense guessing uses at most q distinct target queries and loss (2^32)^min(17,q). Sparse ordinal selection uses at most min(17,q) targets and its separate loss/resources. At every requested q the dense loss is 2^544; this is NOT a security exponent. The optional eighteenth public zero coordinate introduces no eighteenth source secret, target witness or counter guess. The tagged297-bit label has only41 route bits, not297 uniform bits. Ordinary family hardness is ASSUMED and unevaluated; direct RC-CTAC-SR remains an explicit alternative property, not a numeric certificate.

**PROVED / COMPUTED / ASSUMED — fixed-h graph collection.** FIXED-H-GRAPH-COMPONENT.md legally targets differing-payload/equal-output public graph witnesses using NEW within-class SM-TCR programs. Their payload/selector pairs in bits are (128,55),(256,55),(2048,21),(2176,41),(4096,42), independently recomputed in root-message-hash/SUCCESSOR-COUNTS.json. These smaller coefficients cannot be applied to OLD common56-bit particular successes. Challenged-tweak predecessor cones query only other tweaks and lengths; the same public h and all source/challenger resources remain explicit. No collection generic-bound conjecture or RO hardness number is imported.

**PROVED / OPEN — symbolic composition.** FIXED-H-COMPOSITION.md combines exact ordinary private hops, the pointwise source witness cover, the legal coverage alternatives, new graph programs and canonical type7 programs. Its inequality keeps the hidden predecessor probability epsilon_H explicit and pays source seed-zero once. Full fixed-h family hardness and epsilon_H remain unevaluated/open. PRE for uniform starts is a separately reviewed candidate; interior-prefix UD/PRE work is pending and is not relied upon by this accepted cut. The historical RO/QROM model bounds and numerics retain their original scope and values. A numeric full-security claim remains "not established" at all eight requested signing caps.

**PROVED — scoped kernel support.** Three DigestProjection.lean declarations were checked under pinned Lean4.28 and independently reexecuted; their axiom sets are subsets of {propext,Quot.sound}. They prove same-word prefix preservation and the two bit slices under a zero lower limb, not preservation of the whole two-stage H_msg digest, SHA hardness or a source-security reduction. Current cumulative supporting declarations are47; newly checked whole-source/game declarations are0.

## Ordinary hidden-predecessor interface successor

**PROVED / ASSUMED — manual source-specific UD/PRE reduction.** FIXED-H-HIDDEN-PREDECESSORS.md has two independently saved derivations and exact final-subject reviews. A55-bit selector chooses a genuine typed input before the public parameter;254 stopped private-prefix hybrids keep the public full h unchanged and consistently recompute roots/counters/logical caches. Only completed exposing responses are gated. An observable final image-match superset avoids unknown-input/first-hidden tests. Ordinary one-target SM-UD pays each signed-average hop; ordinary SM-PRE accepts any final preimage. Thus the nonzero-seed final hidden contribution is at most min(1,2^55*(pi_PRE+sum_(r=0..253)delta_r)). No random-function uniformity is asserted for the original h-derived predecessors; the paid hybrids establish the terminal prior uniformity. Quantum A's public computation is unchanged and only its final classical verifier trace is extracted.

**PROVED / OPEN — full symbolic successor.** FIXED-H-COMPOSITION-WITH-UD-PRE.md substitutes this component into the earlier reviewed exact private/message/graph/type7 composition and pays the source zero-seed event once. The algebra receipt was conditional on this second final premise review; both exact hidden-subject receipts are now present and hashed before promotion. The accepted legal interface no longer leaves epsilon_H as an unnamed source probability. Actual fixed-h PRF/ITSR/UD/PRE/TCR family hardness, evaluated complete-resource advantages, adequate level/category, certified capacity and successful parameter repair remain ASSUMED/OPEN. At all eight requested q, the printable full-security claim remains "not established". Historical preceding sections/receipts retain their dated OPEN status; this successor supplies the current interface resolution only.

**COMPUTED — supporting finite checks and preservation.** Root's3072 abstract relations and the other reader's26 independent channel/selector relations, including opaque-equality and stale-root negative controls, passed. They are not source signing runs or cryptographic hardness experiments. All source/challenger, message, storage and coherent circuit costs remain charged. Cumulative checked supporting declarations stay47; this successor adds0 whole-source/game kernel declarations. Frozen source/manuscript/scalar results and prior subject/review receipts are unchanged.

## Quantitative random-full-oracle selected restriction and one-target PRE

**PROVED / CITED — manual remote-target lift.** TARGET-ONLY-UD-RO.md identifies the chosen102-byte all-public-parameter restriction of a complete256-bit random oracle, preserving lower output limbs and coherent outside branches. The clean router uses one ordinary remote and one ordinary outside XOR call, without a controlled-unknown-oracle assumption. Honest designated target uses bypass the unknown input via Y; all other source work remains charged in the outside2T polynomial resource ledger. A public adversary with Q_A raw queries yields remote cap Q_A+1, including a final verifier call. This is randomO-only, not a hardness value for fixedSHA.

**PROVED — explicit one-target preimage constant.** SINGLE-TARGET-PRE-RO.md proves kappa_PRE(Q,n)<=min(1,(2Q+1)^2*(2/N-1/N^2)), N=2^n, for an ex-ante target with zero prequeries and marker-independent ghost auxiliaries. A planted correlated marker needs only its common point marginal, not iid coordinates. One Boolean query completes one full-word query. Three first derivations/reviews preserve the distinction between independently derived split proofs and the stronger whole-marker discovery/review. Exact nonbinary miss tables have N-1 outputs; their potentially enormous entropy/storage/gates are charged, not claimed to be a binary-polynomial or efficient implementation.

**PROVED / COMPUTED — calling source and quantitative envelope.** TARGET-ONLY-HIDDEN-BOUND.md audits the actual source program's no-prequery chronology, opaqueX and ghost-side independence, completed-response guard, public/cache/counter values computed from Y and independent auxiliaries, and counted remote replies. ValidPRE selectors have D_H=20229886488608768; activeUD counts sum to A_H=7628143271608320. The conservative randomO hidden component is at most min(1,D_H*kappa_PRE(Q_A+1,128)+12*A_H*(Q_A+1)/2^64). Exact32 rows cover eight q values, prepared/absent caches and Q_A2^32/2^64; all caps are1. Exact adjacent UNCAPPED component-expression crossings are pass99/fail100 at1/2 and pass200/fail201 at1; the capped probability envelope never exceeds1. These are not attacks, work factors or parameter repairs. The stronger historical direct H_final envelope and complete source tables remain unchanged.

**OPEN — original adequacy target.** This closes a finite random-oracle PRE/UD interface and calling-resource obligation. It does not certify128-bit classical strength, category1, a query capacity or a successful minimal parameter repair. Fixed-SHA instantiation is distinct from the requested random-oracle proof, not an added requirement to prove SHA unconditionally. The original resource/adequacy question still needs a sufficiently strong bound under a valid comparison criterion. Cumulative supporting checked declarations remain47, newly checked whole-source/game declarations0, and the full-security statement remains "not established". Manuscript, cryptographic source and old scalars are preserved.

## Reviewed quadratic one-target UD random-oracle successor

**PROVED / CITED — explicit ordinary quantum component.** QUANTUM-UD-POLYNOMIAL-RO.md proves u(Q,n)=min(1,(1-1/N)*4Q^2/(N-4Q^2)) when4Q^2<N, else1. The exact iid-ideal/planted-real marker laws, one-Boolean-query full-output completion, degree2Q acceptance polynomial, weight symmetrization and centered integer-grid Markov argument are independently derived. Auxiliary data must have the SAME conditional joint law in both experiments and be independent of the whole marker field; an independently supplied world-label bit is a counterexample to a weaker premise. The denominator retains between-grid overshoot. Common entangled/mixed state and adaptive source services are covered within the stated finite query interface.

**PROVED / COMPUTED — source caller and quantified component.** Ex-ante target chronology, opaqueX, Y-derived suffix/root/cache/counters, completed-response gates, SAME local code/coins and counted final call give remoteR=Q_A+1. The unchanged active-selector sum A_H=7628143271608320 and PRE selector count D_H=20229886488608768 yield min(1,D_H*kappa(R,128)+A_H*u(R,128)). Exact32 rows retain eightq values, both cache modes andQ_A2^32/2^64. AtQ_A2^32 this component is approximately0.01042740466035393; atQ_A2^64 it caps1. Uncapped-expression crossings are29741080993/94 at1/2 and42060240100/101 at1. Both final readers reproduce those rational boundaries. Exact finite controls include ordinary marker/polynomial/completion identities, actual entangled one-phase examples, and auxiliary/grid negative controls.

**PROVED — preservation and scope.** This improves the older primitive-interface route, not the stronger direct source H bound. The direct H theorem,48 complete scalar cells and32 prior resource crossings remain authoritative and unchanged. Exact N-1 miss tables may be enormous; all local storage/gates/generation work remains charged. No fixed-SHA/category/gate-cost certificate or actual forgery follows. Supporting checked declarations remain47 and newly checked whole-source/game declarations0. Private-K/private-P polynomial candidates and the simultaneous classical ledger are separate, unpromoted work; this result does not certify their full-source composition. Original adequate level/category/capacity and successful smallest parameter repair remain "not established".


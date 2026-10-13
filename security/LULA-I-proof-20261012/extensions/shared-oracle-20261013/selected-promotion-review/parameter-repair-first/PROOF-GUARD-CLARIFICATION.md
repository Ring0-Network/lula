# Source-valid retuning versus old-proof-template eligibility

**COMPUTED — preserved first package.** INDEPENDENT-FIRST.md869736c449aaff9ed24eb68e352fcff46bad784be4085b013c70c6db0ab7f842, FIRST-RECEIPT.json008e75bbbf04d18bcd7e680d82c92ec1aca3f92fbcaf83b3e6915545f9ed79b7 and every pinned first-package file remain unchanged. This successor independently reinspects the old source and CLASSICAL-RO-THEOREM.md in response to root's guard-review request; it is not a new blind-first claim.

## 1. Strict WOTS target is a proof guard

**CITED — exact old lemma.** CLASSICAL-RO-THEOREM.md, Section3 step3, explicitly uses “sum e=S<ell(w−1)” to force a nonterminal verifier call at an unexposed WOTS address. Its H definition excludes endpoint-only positions, which are public in the safe surface. Its D7 definition requires an exposed successful canonical row. This is already a strict premise in the old fixed-source proof, not an optional assumption introduced by the new review.

**PROVED — source arithmetic.** lib.rs212–233 defines lfull=128/lw,ell=lfull−z and requires omitted digits zero with total sumS. pk_from_sig at269–278 completes each chain with exactly(w−1−e_i) steps. Therefore

    sum_i verifier_chain_steps = ell(w−1)−S.

For S<ell(w−1), at least one supplied position is nonterminal. If the entire WOTS address is unexposed and each supplied start is genuine, that first nonterminal call is H. At S=ell(w−1), all e_i=w−1, there are zero chain calls, and the old inference “unexposed genuine starts implyH” is false. A source-representable target is not automatically eligible for the old proof skeleton.

**PROVED — exact domain distinction.** The first's geometry domain includes0<=S<=ell(w−1), appropriately describing source acceptance and permitting an extreme-target negative control. The domain for a prospective **verbatim C/H/G/D7 proof template** must additionally requireell>=1 and0<=S<ell(w−1) at every layer, alongside all byte/digest/shift guards. None of my first package's retuned H/G counts was called a proved full bound; the new strict guard makes that boundary explicit. All ordinary alternatives in ALTERNATIVES.md except extreme_top_target satisfy this additional guard. That extreme is geometry-valid, proof-template-ineligible and already rejected for negligible setup completion.

**OPEN — optional endpoint-case extension.** Without the strict guard one needs a new case/event or a new lemma. One possible direction is an unexposed all-row type7 target event for the all-max digest, handling genuine-child bottom and different (child,counter) points explicitly. Existing exposed-only D7 does not supply it by a name substitution. No extension or retuned theorem is proved here. A toy endpoint certificate fragment may have genuine endpoints and a passing different-child digest while its row is unexposed, so neither a chainH nor exposedD7 witness is forced by this local step. This is a countermodel to that proof inference, not an operational source forgery or full design attack.

## 2. Fixed bases and digest injectivity

**PROVED — fixed permitted interpretation.** For the literal ell change, keep lower lw4/w16 and top lw8/w256. Setz=32−ell or16−ell respectively. lib.rs222–232 decodes all128 bits and checks **every** omitted digit zero. Thus equal real ell-tuples for accepted outputs imply equal complete128-bit digit words, even when ell is shortened. Removing that forced-zero requirement, or allowing other widths that leave128−lw*floor(128/lw) ignored bits, invalidates that injectivity justification. Arbitrary lw retuning is outside the literal permitted parameter list and the present template review.

## 3. Cost units and the actual original cache

**CITED — context midstate.** lib.rs109–115 prepares PK.seed||zero48 using one direct compress256 call in Ctx::new. It does **not** pass through the instrumented compress wrapper at34–37, so that prefix computation is absent from CALLS. The tail loop at122–145 starts from this midstate. My c(m) and subtree/FORS/WOTS ledgers count compressed **tail** blocks under the prepared context; they are not full independent SHA evaluations with a newly recomputed64-byte prefix each time. Add one physical context-prefix compression per actual newCtx construction separately. Sign uses the stored context; public verification constructs one new public context. Keygen shares its prepared context across workers. One complete raw-oracle query and one compression call are distinct units.

**CITED — original prepared cache is top only.** The release seeded driver params string atline9 marks all four5-bit layers cached0 and only the21-bit top layer cached1. lib.rs635–645 selects cached counters/path data only where that layer's cache exists; each lower layer still grinds its child and rebuilds its subtree. “Prepared cache” in the measured original configuration therefore does not mean all layers cached.

**COMPUTED — first-package fields correctly separated.** ANALYTIC-CONTROLS.json contains the hypothetical all_prepared_addressed_sign_compressions=29266 and the distinct top_only_cache_addressed_sign_bounded_mean_display≈96340.703361151... for the original source. The latter includes four16703-tail-block lower subtree computations and four lower canonical searches; it excludes message prehash and FORS outer grinding as explicitly stated in cost_scope. Neither number is a measured latency, peak RSS, unconditional finite source runtime or guarantee of setup completion. The hypothetical all-layer prepared quantity is not promoted as the original hot-cache cost.

**OPEN — outcome.** Root's strict-target/injectivity/unit/cache qualifications are accepted on exact source inspection. Geometry and algebraic costs are derived, but no retuned complete inequality, category certificate or parameter-minimality claim is established. No source, scalar, first artifact or manuscript is edited.

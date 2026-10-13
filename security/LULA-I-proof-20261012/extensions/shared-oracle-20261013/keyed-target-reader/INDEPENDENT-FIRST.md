# Independent source-first keyed-target identification

Saved before reading any NEW standard-identification proposal. This reader inspected the exact release source and the existing TYPE7-REDUCTION-PROGRAM.md and PRIVATE-REDUCTION-PROGRAMS.md, and the three primary papers below. Those existing programs fix the subject; they do not identify the new game with a published one by themselves.

## Verdict

**PROVED, conditional on a precisely named interface:** A shared-seed collection-assisted canonical target-collision game CAN generate the exact child and first-accepted type7 target distribution. The child need not be computed with the seed in the reduction's possession. The collection oracle computes its type0/1/2/3/4 calls at the challenger's hidden seed. Thus the public-seed chronology objection alone is removable by the published collection construction.

**OPEN, published identification:** HK2022 Definition 2/7 plus SPHINCS+C Definition C.1 do not alone specify the complete raw-relative canonical finite interface needed here. In particular, matching the changed-base predicate does not prove identity, and the target oracle's unspecified choice of an accepted counter does not prove canonical-first identity. A finite counter space, BE32 serialization, exhaustion, and the common full256 raw oracle must be explicit. Two fixed predicates are required for the actual low/top parameters unless a theorem explicitly permits tweak-dependent predicates. This is a component statement, not closure of the original complete-security goal or a fixed-SHA-256 security theorem.

The central obstruction is specification/primitive identity rather than an inability to generate the source child. Three routes are distinct: (1) assume the exact raw-relative canonical collection game and obtain the reduction below; (2) prove a lifting lemma from an actually specified published interface to that game, with all resource losses; (3) retain the accepted direct source-RO/QROM bounds without relabeling them conventional S-TCR. No source changes are proposed.

## 1. Immutable subject and primary evidence

Release source: `publications/LULA-I/release/code/lula1/src/lib.rs`, SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

- Lines122-147: `Ctx::th` is trunc16 of the complete SHA-256 word `S || zero48 || A22 || X`.
- Lines216-235: type7 payload is `C16 || BE32(c)`, digits cover all128 bits, acceptance tests zero tail and digit sum, grind starts0 and increments.
- Lines239-279 and479-496: WOTS PK construction and the child's lower subtree use no type7 calls.
- Lines346-381: bottom child is the actual FORS PK using types3/4 and secret derivations, not a sampled independent digest.
- Lines526-541 and628-657: cache preparation/signing use the genuine child and canonical counter; honest cache restoration preserves these values.
- Lines672-679 and final verification: the event is a reached final verifier type7 call in an actually accepted signature; source acceptance includes final root comparison.

Primary documents read locally, no secondary sources:

1. Huelsing-Kudinov, IACR2022/346, Definitions2 and7, printed pages4-6. PDF SHA256 `80dcd11e56448d07e2a2465a11efa9ca8f4561387abeb3fabdd6d40d4ffe3c3`. Definition2 samples P before A1, withholds P until A2, and lets A1 register targets. Definition7 grants classical collection access at that SAME hidden P and forbids challenge/collection tweak reuse.
2. SPHINCS+C, IACR2022/778, Algorithm5 printed page13, section5.1 page14, DefinitionC.1 page30, AppendixD page34, AppendixE pages34-35. PDF SHA256 `1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215`. C.1's target oracle returns an accepted image and a counter and excludes changed-counter-only collisions through M != Mi. Section5.1 explicitly discusses constructing dependent messages through a collection with hidden shared parameters. C.1 says an i in N satisfying Prop; it does not explicitly state min, BE32, or the finite absorbing bottom branch. Algorithm5 says find a count; nearby text sets counter bits r equal to the security parameter to motivate existence. AppendixE adds global THF access in its generic game, but that is not automatically arbitrary-byte full256 source raw access.
3. Kudinov-Nick, IACR2025/2203, Definitions2.1-2.3 printed pages3-4 and section5 printed pages11-12. PDF SHA256 `3c58f81a6a0b7e8e040134be1a0013b3977edefdc889e1636d4dfe79cf0e225e`. These definitions describe unkeyed/keyed/tweakable functions, and the WOTS+C procedure increments a count until the conditions hold. They do not state a complete fullraw, finite canonical S-TCR game or establish a LULA-specific lifting lemma. A definitional assertion that tweaks separate domains is not a theorem of independence for an arbitrary deterministic keyed family.

## 2. Exact source distribution

Let O be one full256 random oracle on byte strings, S the common seed, F/J the already named independent private ideal maps in the HJ game, and a a valid type7 address with final two address fields zero. Let

`T_a(S,C,c) = O(S || zero48 || a || C || BE32(c))`.

For low layers0..3, `Prop_lo(y)` is sum of32 base16 digits =240. For top layer4, `Prop_hi(y)` is sum of16 base256 digits =2040. Both use all128 prefix bits; actual z=0. The two predicates are different subsets of the same128-bit output space. C_a is `child_value(a)`, generated using the SAME F and SAME O as the rest of the source. At the bottom it is FORS PK; above it is the lower height5 subtree root. Its dependencies never query a type7 address.

Define L=2^32, `c_a=min{c<L:Prop_kind(first16(T_a(S,C_a,c)))}`, or bottom if no such c exists. A completed exposed row uses exactly c_a. Rust overflow/nontermination is not asserted to implement a graceful abort; the cryptographic partial game models no winning completed response on exhaustion.

The collision event requires a reached honestly exposed successfully canonical row and V != C_a, with

`first16(T_a(S,V,c)) = first16(T_a(S,C_a,c_a))`.

BE32 and fixed16+4 framing ensure that every off-base candidate differs from every same-base canonical search input. A same-child different-counter witness is ineligible even when its digest collides. Target equality is128-prefix equality; raw replies retain256 bits. A full256 equality challenge would be the wrong collision predicate.

Conditional on S,F, the outside raw restriction that generates C, and all relevant prequeries, the selected type7 row is NOT simply asserted to be a newly sampled independent row. Its actual raw prequery values must be retained. Without such prequeries, disjoint RO words give the familiar fresh-row law; with them, the global oracle supplies the already fixed values. The proposed reduction below uses that same O directly and does not resample any restriction.

## 3. Explicit named assumption and game

Call the assumption **RAW-COL-CAN32-S-TCR(Prop)** for the exact RO-instantiated LULA hash collection. This is an explicitly specified raw-relative canonical finite specialization/extension of collection-assisted S-TCR, not a claimed verbatim published definition.

Challenger samples uniform S16 and one full256 O. It gives both phases Raw(x)=O(x), quantum XOR-accessible if QROM is considered. It does NOT disclose S during phase1. Let `Th(S,a,X)=first16 O(S||zero48||a||X)`.

Phase1 has classical `Col(a,X)=Th(S,a,X)` for all source-supported addressed payload lengths, and one classical registration `Can(a,C)` for type7 payload bases C16. All Col tweaks differ from registered a, including across payload lengths. The reduction is allowed to choose a and C adaptively from Col and Raw replies. Can evaluates c=0..L-1 IN ORDER using the SAME O and BE32, returns `(c0,y128)` for the first accepted value, or bottom. It retains all rejected full256 values through O. A full256 Can reply is unnecessary: y128 suffices until S is revealed, after which Raw retrieves the exact remaining128 bits. Giving fullY instead would also be exact but would be an additional interface feature that must be named.

After the sole registration, reveal S and permit public evaluation of all Th functions and Raw. The answer is `(V,c)` with V16 and c32. Win requires nonbottom, V != C, and `Th(S,a,V||BE32(c))=y128`. Raw remains the SAME O in all phases. Challenger cost for canonical preprocessing is at mostL O-evaluations plus digest acceptance work; it is reported separately, not treated as a free ordinary TCR target. All raw prequeries are permitted and charged.

Uniform S includes zero. To connect to the parent conditional HJ statement at nonzero S, the reduction may fail after reveal when S=0, producing the explicit conditional factor below. No seed chosen by the reduction is silently substituted for a challenger-sampled seed. Alternatively state a conditional-nonzero seed challenge and omit this factor; that is a different explicitly named distribution.

## 4. Concrete adapter and proof

For each fixed predicate kind construct a two-phase B_kind with ONE target and one fixed Prop, not a mixed target predicate selected after seeing its challenge.

Low rows have count Klo=2^41+2^36+2^31+2^26=2,269,957,324,800. Select42 uniform bits, unrank valid low addresses, and treat unused pad values as failure. Top rows have count Khi=2^21, so select21 uniform bits and unrank into layer4/tree0/keypair. Each actual low/top row therefore has weight exactly2^-42/2^-21 respectively. The empty pad contributes failure without conditioning or renormalization. One may use42 bits for both kinds to match the existing looser bound, but the21-bit top selector is a valid sharper component bound without changing source parameters or probability tables.

Initialize consistent independent F/J tables. Run A's pre-key Raw phase with S/pk withheld and save the continuation. Any abort before obligatory setup transition is nonwinning. Construct selected C_a with Col calls and F values. This computation uses only types0..4, so it never violates selected type7 tweak exclusion. Register Can(a,C_a). On bottom fail locally: the selected exposed-successful-row event is zero there; no claim is made that an unused source row failure globally aborts source setup. Reveal S. At S=0 fail for the parent conditional theorem. Obtain fullY from Raw at the now known exact selected word if needed for source raw replies; the underlying oracle already supplies it without simulation inconsistency.

Resume exact source keygen/signature services, releasing pk only after ordinary setup completion. Use the same F/J and Raw throughout. Selected honest grinding uses c0,y; selected raw queries still use Raw, not a newly sampled row. All other source counter loops and rechecks use Raw normally, with ordinary finite noncompletion treatment. The precomputed child overlaps with future source work through the identical tables, so it is neither resampled nor replaced by an independent value. Source C at the selected address is stable under legitimate signing and restoration because neither message choice nor type7 digest determines that child. Preserve A's messages, Seen and opaque honest cache semantics.

Run the final source verifier classically. At the selected type7 call, if its off-base payload has the target prefix, output its (V,c). If an earlier valid primitive collision is available, stopping there can only improve primitive success; exact distribution applies to the continuing comparator or to B's prefix before this success stop. Quantum raw queries are forwarded coherently and are never inspected for witnesses. Only the classical final verifier yields extraction. This costs the primitive side no selected-header quantum router: B forwards the globalRaw oracle directly.

For every fixed selector, the continuing comparator has EXACT HJ law: S and O come from the challenger; hidden-seed Col evaluations are simply early evaluations of the same source words; C and Can metadata equal source values; rejected values and fullword raw correlations persist. Precomputing a subtree changes no abstract output or oracle values. Visible timing is outside this atomic cryptographic experiment, as in the parent scope.

Let E_lo/E_hi be the disjoint source subevents that classify the first eligible D7_base_final event by row kind. Then, with eta=1-2^-128,

`Pr_HJ[Win AND D7_base_final | S!=0] <= (2^42 Succ(B_lo) + 2^21 Succ(B_hi))/eta`.

Succ is for the unconditional uniform-S RAW-COL-CAN32-S-TCR challenge. With conditional-nonzero challenger sampling the denominator is1. Each component success includes the relevant source row's selected weight; bottom, wrong selector and incomplete requested source services contribute zero. No 1/p_accept loss, completion normalization, or eager enumeration of all WOTS rows is introduced. In classical ROM one may replace the final event by the larger public-query superevent, with explicitly different naming and extraction bookkeeping.

This theorem assumes insecurity bounds for the TWO exact named primitive games. It does not assert that published numerical S-TCR bounds already cover the strengthened raw interface or finite canonical selector.

## 5. Explicit resources

One low/top challenge target is registered. Before registration, at selected layer0 the genuine child's Col construction costs17*(512+511)+1=17,392 calls,8,704 distinct F words. At layers1..4 the child costs32*(32*15+1)+31=15,423 calls and1,024 distinct F words. The top child is not the height21 tree. These are classical collection calls with tweaks disjoint from selected a.

Can costs at mostL=2^32 complete underlying O evaluations. The reduction's additional fullY fetch costs at most1 Raw evaluation. If Q_H is A's TOTAL classical Raw budget including pre-key calls, a conservative B Raw cap is

`Q_H + H_setup + q*H_mode + 3224 + 1`.

In QROM use Q_q direct coherent Raw calls plus the corresponding honest classical cap; separately include any allowed classical A raw calls. There is no independently generated coherent outside table in this adapter because the explicit raw-relative challenger supplies the global O. This is a genuine interface change from a Row-only challenge, not a free local implementation of its outside functions.

With L=2^32 and the source's top-prepared setup:

`H_setup=2^21*(19505+L)-1`;
`H_cold=8560574463+82090+6L`;
`H_hot=82090+5L`.

Conservative distinct F cap is `min(19212937084272640,8704+2181038080+q*U_mode)`, with U_cold=33567232 and U_hot=12816; J labels at mostq. Extra collection construction node payload can be bounded by17*1023*16=278,256 bytes, excluding F dictionary and source cache storage. Balanced dictionaries and exact source execution give source-relative finite time/storage; quantum oracle evaluation is charged to challenger oracle resources and no efficient gate implementation of global O is claimed. Canonical preprocessing and child preparation are explicitly nonfree even though insecurity notation often hides them in time.

## 6. Smallest missing implications and countermodels

**Canonical selection gap:** A target oracle that returns ANY accepted counter is permitted by C.1's written condition but need not return source min. In a two-counter row where both images pass Prop, a lawful choose-largest implementation returns1 while source chooses0. For independent two-symbol digests both accepted with probability1/4, so first-vs-last target metadata differ on positive mass. Therefore membership in the accepted set and the changed-base collision predicate do not imply exact source distribution. The smallest required lemma is that the instantiated challenge oracle uses the exact finite first-accepted BE32 policy or that its existing insecurity bound uniformly covers that policy with exhaustion.

**Raw auxiliary gap:** A128-bit collection interface cannot determine the distribution of the remaining128 bits of raw evaluations. Consider two source models with identical prefix Th but raw words `(Th(x),Z(x))` and `(Th(x),0^128)`. Every128-bit THF/collection/target game transcript is identical, while one raw query distinguishes their full256 replies. This is an interface countermodel, not a cryptanalytic attack on SHA-256 and not a claim that a natural independent-RO completion is insecure. It proves that Def2/7 alone does not fix fullRaw identity. Name the joint source globalHash assumption or provide a correlation-preserving lifting lemma.

**Arbitrary off-typed raw gap:** Even fullimage addressed collection access does not specify O at unaddressed metadata words or malformed/raw strings. The adversary's original raw interface permits those words, and source inner/outer message hashes use them. An independently sampled Raw beside a fixed collection need not agree on addressed words at the eventually revealed S. A common raw-relative oracle fixes this; independent-oracle auxiliary access does not.

**Predicate gap:** Low and top Prop differ. A theorem for one fixed predicate does not become a theorem for a random choice of two predicates merely by tagging a tweak. Split the reduction as above or prove a generalized tweak-dependent predicate theorem.

**Finite exhaustion gap:** A game that assumes every row has a target cannot have exact finite source law: RO source has bottom mass `(1-p_kind)^L` on a fresh unqueried row. The accepted target distribution has `Pr[c0=j,Yfull=fixed accepted word]=(1-p_kind)^j/2^256`; total mass is1-(1-p_kind)^L. Conditional accepted-target resampling would divide by this mass and erase the bottom and rejected-row correlation. A finite-game bound or explicit coupling to an extension with charged failure event is needed. An arbitrary extension beyond BE32 is not a source identity.

**What is not a gap:** The fact that the source child uses a known public S while conventional registration hides S is NOT an impossibility argument once the collection oracle is granted. Definition7 expressly exists to generate dependent target messages at that same hidden S. Construct C through it, then register the selected type7 row. No independent-row axiom, fixed-S input choice, or forged child is needed.

## 7. Boundary

This is a manual component proof and precise identification frontier. It does not mechanize the Rust interpreter, certify source SHA-256, prove conventional private PRF hops, prove a complete signature security theorem, change parameters, recompute category/capacity, run a source forgery, or measure timing. All existing artifacts are preserved. The named primitive's generic insecurity and its compatibility with any existing published S-TCR bound remain explicit further obligations.

# Independent joint classical raw-query ledger

**COMPUTED — first-save provenance.** Saved before reading any NEW peer partition work. Inspected pinned release lib.rs (`ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`), current `CLASSICAL-RO-THEOREM.md` (`3ff8d3c0457ce0525a5af416472f7188e75e20c52cc06d2220b4273a1db752fe`), the original joint-private candidate argument in PROOF.md, and the existing source FORS bridge. These older component statements identify the obligations; no new peer derivation or new scalar is read. No source, old theorem, scalar, kernel, manuscript or timing is changed, and no signature/private attack is constructed.

## 1. Model and exact raw words

**ASSUMED — source model.** Let N=2^128. Fix S!=zero16. K,P are independently uniform private seed components. There is one complete full256 random oracle, independent memoized full256 ideal F(A), J(m), classical public queries capped by Q, q initiated atomic signing requests, opaque honest caches/restores, permanent exposure and one final source verifier. Noncompletion is absorbing and nonwinning. Keys and nonces are not supplied as advice. This is an RO statement; it does not apply to fixed SHA by a name or query-count substitution.

**PROVED — source languages.** All intervals below are byte intervals, zero-based and half-open.

* Addressed word: S16||zero48||ADRS22||payload; header length86. The type byte is at73. Source private F words have valid type5/6 addresses and exactly16 payload bytes, total102. Such a word nominates one K candidate, its final16 bytes.
* Private J word: P16||S16||m, length>=32. The larger candidate language J_S is every word with bytes[16:32]=S. A public word nominates one P candidate, bytes[0:16], and one J-message suffix after byte32.
* Source inner message word: I(R,m)=R16||S16||root16||m, length>=48. Define I_S as all words length>=48 with bytes[16:32]=S; its hypothetical inner label is the unique suffix m after byte48. The actual root-header constraint can restrict this larger class, never enlarge it.
* Outer word: E(U,c)=U32||BE32(c)||S16, length52. Define eligible E_S by length52, suffixS, and bytes[16:32]!=S.
* Graph G words have valid designated type0..4 graph addresses; arbitrary raw payload lengths can witness the stronger public target event. Hidden H can occur only at a valid nonterminal type0 or height-zero type3 address with a16-byte payload, and only while that coordinate remains unexposed. Type7 canonical targets occupy valid type7 row addresses; the actual final pair has20 payload bytes. A broader residual type7 target event may include arbitrary other raw payload lengths.

**PROVED — byte disjointness.** Since S!=0, addressed words have bytes[16:32]=zero16, whereas J_S/I_S have that block equalS. Eligible E_S has length52 and second block!=S, so it is disjoint from J_S/I_S and from addressed words. Address types5/6,0..4 and7 are pairwise disjoint at byte73. This covers pre-key queries too: conditional S is fixed from the beginning even before A learns it.

## 2. Counterexamples to a one-role/one-charge interpretation

**PROVED — private-J / nonce / endpoint overlap.** A literal word w=R||S||root||m with a prospective unsigned inner label m is in J_S and I_S simultaneously. It nominates private key P=R, predicts nonce prefix J(m)=R, and its fresh full oracle reply can have last16 bytes equalS (the bridge's Bad_end). The J suffix nominated by the private language is root||m, not m; these labels are distinct finite strings. Private P and the unused nonce J(m) are independent coins. In the continued ideal/ghost experiment with an actual-root header and a fresh word, the three analytical conditions have union probability exactly

3/N-3/N^2+1/N^3,

when the future new-message case relevant to nonce prediction is considered. This is a bad-ledger overlap witness, not a successful forgery or a private-key attack. Counting three separate potential roles and asserting their budgets sum to Q would be false. Root mismatch/already signed labels can reduce the nonce role, but do not make the worst-case class disjoint.

**PROVED — H/G share an opportunity despite exclusive events.** A type0 or FORS leaf query with16 payload bytes may guess the genuine hidden input (H), or use a different input and hit its genuine output (G). The two predicates cannot both hold on the same query, but neither predicate is a predictable query-class partition based on public bytes alone. In a simple unused-coordinate/default-reply world their union is2/N-1/N^2. Assigning the query after discovering whether it hit the secret and then applying a1/N rate to that selected budget is invalid.

**PROVED — untagged I/E overlap really exists.** Choose a52-byte word U32||c4||S16 with U[16:32]=S. It is an outer-form word and also I_S and J_S. Its larger inner root header is c4||S[0:12], and its inner message suffix is S[12:16]. This is only a byte-language witness; it constructs no signature. Thus names 'inner' and 'outer' cannot define independent random functions. Eligible E_S deliberately removes these words. Any actual source inner output with last-halfS triggers Bad_end BEFORE its outer stream could create this alias, so such points need not be treated as eligible coverage candidates on a good prefix.

## 3. A predictable syntactic partition with weighted risks

**PROVED — partition.** For each PUBLIC raw query, classify its input into one of the following disjoint sets, with membership defined by S/source geometry before its fresh reply and never by a hidden-equality result:

| class | exact support | conservative1/N risk weight |
|---|---|---:|
| F | valid private type5/6 word,16 payload bytes |1|
| Jshort | J_S length32..47 |1|
| I | I_S |3|
| T | valid nonterminal type0 / height-zero type3 word,16 payload bytes |2|
| Gother | remaining valid type0..4 graph-target words |1|
| Seven | valid type7 row words |1|
| E | eligible E_S |0; coverage and1/N^2 prefix roles remain|
| Other | all remaining raw words |0 in this ledger|

T can be refined after public completed exposure to weight1, but the displayed bound safely treats it as potentially hidden throughout. Invalid addresses have no designated graph target and are Other. Offlength payloads at a valid protected header are Gother, not T. I can be refined to weight2 when its label was already signed or actual-root header fails, but the larger weight3 class avoids a future-header ambiguity and is sufficient.

**PROVED — joint budget form.** Write C_F,C_J,C_I,C_T,C_G,C_7,C_E for actual class counts in the continued unflagged ghost execution, counting repetitions conservatively. They obey the PATHWISE sum<=Q. Expectations Q_F,... also obey sum<=Q. A valid deterministic class-cap interface can instead declare jointly bounded caps b_F,... with sum<=Q; independently maximizing each class and then claiming a joint constraint is impermissible. The weighted raw rare-event charge is

W/N = (Q_F+Q_J+3Q_I+2Q_T+Q_G+Q_7)/N,

and W<=3Q. This is a weighted first-bad ledger, not an assertion that the bad EVENTS are disjoint.

## 4. Proposed simultaneous sampler: avoiding incompatible advice

**PROVED — joint sampler ingredients.** Eagerly sample the finite genuine graph topologically: independent uniform FORS secrets and WOTS starts/interior coordinates, independent endpoint/leaf/public node images and independent lower full-image limbs. Each type0 step and each graph-parent image belongs to a distinct actual restriction, and its input is computed from earlier OTHER restrictions. This gives the ordinary joint-private graph/function marginal. Independently disintegrate each genuine-child type7 row into failure/bottom or first accepted counter, accepted full image, rejected prefix and uniform residual cells. Its genuine child is a public node/FORS-root value independent of its own restriction. Neither row selection nor graph generation consults its own residual table.

**PROVED — safe augmented surface.** Grant ONLY endpoints, FORS leaf images, compressed keys and public tree/root images, plus successful canonical-row metadata/rejected prefixes. Do not grant hidden FORS secrets, WOTS start/interior values, or the entire F table. Canonical row metadata depends on public child values and type7 restrictions, not those protected coordinates. These safe data and typed functions are independent of untyped I/E cells at S!=0. This is a new compatible analytical augmentation, not a merger of the old full-secret-graph G advice into the H proof.

**PROVED — continued ghost router.** Sample one residual full oracle table O0. Return designated images at unprotected graph points and known protected points. At every still-hidden protected point use the ordinary O0 reply without reading that hidden value. Source honest node/chain work uses its retained genuine records; message metadata and type7 rows use their common actual values. Completed signatures reveal their FORS secrets and whole WOTS forward suffix permanently. Install new known designated points only when their public reply was not previously fixed; otherwise retain the old reply. The ghost does not branch on analytical flags. Until the first H hit, newly known protected points were never queried while hidden, so the retained-old-reply case cannot prevent agreement. Suffix closure ensures a known point's genuine image reads no remaining hidden successor.

**PROVED — unused variable / freshness audits.** Remaining protected coordinates stay independent uniform conditional on the safe surface, ghost public history and previously disclosed values. F/J keyed seed components K/P are UNUSED coins in this continued joint-private ghost. An unsigned message's J(m) is unused by public raw replies and setup; its disclosure occurs only through a completed signing response. Fresh residual graph/row reply cells are independent of their static genuine targets. Existing graph/row values that can be returned for free are genuine points (excluded by G/Seven) or rejected same-child counter points (cannot equal the accepted target). All other matching responses were already charged at their first public evaluation. The fresh I reply half remains uniform before first alias failure; an old honest outer point could be I_S only after an earlier Bad_end. No flags are told to A and no posterior conditioned on surviving guesses is declared uniform.

**PROVED — agreement and risk weights.** Reconstruct the actual real private restrictions at S||zero48||A5/6||K and P||S||m from the sampled F/J maps. These two private languages are disjoint. Ordinary real source and joint ghost observations agree until a raw/metadata private-key nomination, hidden input, graph/row target hit, or bridge bad event. For F/Jshort inputs one unused key candidate costs1/N. For I inputs one unused P candidate, one nonce-prediction candidate and one fresh endpoint-half test cost at most3/N by an unconditioned union/predictable fresh-reply charge. For T inputs unused genuine-payload guessing and residual genuine-image equality cost at most2/N. Gother and Seven cost at most1/N. The analytical nonce flag may be enlarged to every unsigned-label literal prediction at query time; that only strengthens the bound and avoids depending on a future signing decision.

**OPEN — assurance distinction.** The preceding is a manual simultaneous source-sampler argument requiring independent review/refinement before promotion. It is not a checked source declaration or an efficient eager sampler. Its proof obligation is the stated compatible safe-surface/row/unused-coordinate construction; importing unrelated old per-event augmented advice would NOT establish it. The source/scalar theorems remain unchanged regardless of this candidate's review outcome.

## 5. Honest calls and the conditional candidate inequality

**PROVED — honest outer private nominations are redundant here.** A source inner call contributes one possible P nomination from its R and one fresh endpoint-half test. If its output U has U[16:32]!=S, its outer word cannot lie in the private-J language. If U[16:32]=S, the joint ledger has ALREADY raised Bad_end before any outer call. Therefore the old extra P nomination for every honest outer hash is unnecessary in a simultaneous first-bad ledger. At most q initiated source requests and one final inner call contribute2(q+1)/N. Source setup/addressed work creates no private or inner-language nominations at S!=0. This does not subtract a charge from separately conditioned old inequalities; it uses the new common stop.

**COMPUTED — verifier constants and remaining bridge terms.** The final verifier has at most3017 protected opportunities and3217 graph opportunities; together these cost6234/N, including weight2 at potentially hidden calls. Its five type7 digest checks add5/N. The final inner private/endpoint nominations contribute the already counted2/N. Uniform seed-zero contributes1/N once when averaging. The remaining256-bit source bridge costs [q(Q_I+Q_E)+binom(q,2)+q]/N^2, and outer exhaustion costs q(511/512)^(2^32). The q+1 inner count is a cap, not successful-call normalization.

**PROVED — coverage requires deterministic candidate padding.** If the caller provides a PATHWISE deterministic eligible-outer cap b_E, the accepted stream padding gives (b_E+1)p_F(q). It cannot be replaced by (E[C_E]+1)p_F(q): adaptive allocation of E queries can depend on realized exposure coverage. The old padding counterexample rules out that shortcut. With only total Q supplied, retain(Q+1)p_F(q), even while the rare-event ledger uses expected partition counts.

**PROVED conditional on the simultaneous manual sampler — role-budget candidate.** With the jointly valid class budget form above and deterministic eligible-outer cap b_E,

Pr_REAL[Win] <= min(1,
 [Q_F+Q_J+3Q_I+2Q_T+Q_G+Q_7+2q+6242]/N
 +[q(Q_I+Q_E)+binom(q,2)+q]/N^2
 +q(511/512)^(2^32)+(b_E+1)p_F(q)).

Here expected role counts may be used for predictable rare-event/pair charges, but b_E is deterministic. The6242 is3017+3217+5+2+1. With ONLY totalQ supplied, the immediate sufficient candidate is

min(1,(3Q+2q+6242)/N
 +[qQ+binom(q,2)+q]/N^2
 +q(511/512)^(2^32)+(Q+1)p_F(q)).

This reduces the existing6Q/N coarse charge by a factor2 and its3q term to2q, if the new joint construction passes review. It does not prove an adequate128-level/capacity certificate, a successful parameter repair or an attack if the sufficient expression is still vacuous. The same-query inner triple prevents a coefficient1 disjointness argument for THESE bad predicates; sharper event-specific reasoning may discard irrelevant flags or improve this proof.

## 6. Three routes and exact remaining frontier

**CITED — route1.** The old reviewed6Q theorem remains a valid source-RO theorem with compatible per-event projections and unchanged scalar tables.

**PROVED conditional / OPEN review — route2.** The new simultaneous safe-surface ghost and weighted typed/untagged partition yield the explicit3Q candidate above. Required discriminators are private-J/nonce/endpoint overlap, protected H/G alternatives, I/E alias classification, forward-closed disclosure, correct rejected type7 metadata and completed-response first-bad handling.

**OPEN — route3.** A still sharper bound would have to avoid or directly analyze some artificial coverage/private flags, or jointly charge adaptive coverage opportunities without substituting expected candidate counts. Pure domain labels cannot remove the inner triple or the protected H/G double. Numerical inadequacy of either sufficient expression is not evidence of an implementation attack. No new whole-source/game declaration is added and the whole security objective remains incomplete.

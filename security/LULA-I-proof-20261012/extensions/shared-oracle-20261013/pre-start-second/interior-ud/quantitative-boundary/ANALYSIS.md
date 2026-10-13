# Quantitative boundary of the reviewed fixed-h UD/PRE adapter

**COMPUTED — subjects and scope.** This resource analysis preserves the independent-first files and final receipt. Reviewed manual subject `FIXED-H-HIDDEN-PREDECESSORS.md` is SHA256 `d47b8a5ecc72a3d1ff7f52d3b3a16be6220f4acf5d0c08416f902939320dbb13`; final second receipt is `d8fb006bff05bc3228c9daf87b08cf721491adbb2a2909a813fc9680ea4af2f3`. Primary cached HK22 text SHA256 is `be27fac74e2885f3d5fe4b7a24a09b3166ba82e4c726e988766527c29293c561`, PDF SHA256 `80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3`. Only arithmetic is executed here; no LULA signing, forest/cache generation, timing, attack, or old scalar change occurs.

## What Lemma 3 actually says

**CITED — HK22 section 8.3, Lemma 3, printed page 24, cached text 1065–1078.** H:P×T×{0,1}^n -> {0,1}^n is a RANDOM hash function. A quantum SM-UD adversary making Q queries to H has advantage <=12Q/sqrt(2^n). The proof constructs a boolean-function distinguisher with 2Q queries; that doubling is already included in the coefficient 12. Algorithm 4, printed page 25, gives A oracle access to its constructed random H and supplies challenge images separately. The target count does not enter this displayed bound. A one-target use is permitted.

**CITED — distinction made by the same primary source.** Section 8.1 (text 1004–1012) discusses generic undetectability of random Th and says its collection-bound equality is conjectured. Section 9 Construction 2 (text 1106–1113) says concatenation security is shown in (Q)ROM, assuming the underlying H behaves like a random function. Neither passage is a theorem certifying the actual deterministic SHA-derived family in the final manual subject.

**PROVED — three different subjects must stay distinct.**

1. The accepted manual adapter concerns the ordinary fixed public family f_T^S(x)=prefix128 h(S||zero48||T||x), with h's full256 algorithm available locally/coherently. Its primitive advantages are computational quantities at actual time/circuit/storage resources; a call count alone cannot rule out exploitation of the fixed algorithm's structure or precomputation.
2. Lemma 3 concerns a uniformly random node128 tweakable H and oracle-query complexity. Its premise is not established merely by having constructed a lawful ordinary UD adversary.
3. A hypothetical globally random full256 raw oracle O on complete byte strings induces a random node128 family on injectively encoded (S,T,x), but ALSO gives full lower limbs, arbitrary off-length words and all other source domains through the same O. A lift must retain that whole shared interface. Treating other calls as an unrelated independent oracle without a joint-law/coherent routing proof would change the source experiment.

**OPEN — applicability.** No fixed-h hardness certificate or full same-raw-oracle lifting theorem is proved by this resource analysis. The table assumes the inequality delta_r<=min(1,12 Q_B/2^64) ONLY as a hypothetical numerical envelope. It is not a bound on the actual delta_r, a SHA security estimate or a legal substitution into existing scalar tables. PRE is not evaluated at all.

## Complete constructed-adversary budget

**COMPUTED — retained reviewed caps.** For each constructed B, at node size n=128,

Q_B = Q_A + H_setup + q H_mode + 3224 + 254,

where H_setup=9,007,240,159,690,751; H_hot=21,474,918,570; H_absent_cache=34,330,460,329. These are complete-h upper caps from source loops and finite u32-row totalization, not measured ordinary execution times. Source setup includes the actual root and top logical cache. q counts source initiated requests under the absorbing convention. Complete message hashing/search, source signing, final exact verifier and selected-chain preparation remain charged. The ordinary one-target challenger computes its own target separately; its work is not another B oracle query in HK22's convention. Quantum A's genuine public-h computations are included in Q_A; source/challenger time, random-function simulation, memory, byte lengths and coherent circuit/register work need their separate budget.

**PROVED — no free honest oracle evaluations.** In an oracle interpretation, B's own honest computation is still computation by B. It cannot use Q_A alone in a lemma stated for ALL Q queries to H merely because setup/signing is labelled honest. The full cap above is a conservative resource envelope. Since calls on other payload lengths are outside Lemma 3's literal node128 H domain, applying its formula to this full-h cap itself remains hypothetical until an interface lift is proved; the conservative count is not that missing theorem.

## Exact conditional arithmetic

**COMPUTED — eight q values.** q is 2^24, 2^30, 2^38, 2^40, 2^41, 2^44, 2^50 or 2^64. Both hot and absent-cache caps are evaluated at Q_A=2^32 and Q_A=2^64. `conditional_envelope.py` uses integers and exact fractions, writes only this directory, and produces 32 rows in `CONDITIONAL-ENVELOPE.json` and their readable `CONDITIONAL-TABLE.md`. Decimal table cells are display approximations; exact rational values remain in JSON. No cell is a security-bit value.

**PROVED — hypothetical aggregate saturates even before any PRE cost.** At n=128 the accepted selector/hop expression contains 2^55 times a sum of 254 UD advantages. If the same conservative Q_B is used for each,

2^55 * 254 * (12 Q_B/2^64) = (381/64) Q_B.

Setting PRE=0 is an optimistic arithmetic diagnostic, not a PRE-hardness assertion. The outer capped envelope reaches 1 as soon as Q_B>=64/381. Since 64/381<1, every nonzero integer Q_B saturates it. The source setup cap alone already exceeds this threshold by many orders. Capping each individual delta at one first does not change this conclusion: in the low-Q regime the displayed identity applies, and in the high-Q regime 2^55*254*1 already exceeds one.

**COMPUTED — per-hop behavior.** At Q_A=2^32 and q=2^24, the per-hop hypothetical cap is approximately 0.24023530 hot and 0.38053987 absent-cache. For q>=2^30 it is 1 in both modes. The largest integer q with unamplified 12Q_B/2^64<=1 is 71,163,083 hot or 44,515,028 absent-cache. At Q_A=2^64 no nonnegative q meets that per-hop condition: Q_A alone already gives 12. Every aggregate row in both tables is 1, with PRE optimistically zero.

**PROVED — implication and non-implication.** This demonstrates that this particular hypothetical sufficient envelope is vacuous at the stipulated resource budgets. It does not demonstrate a successful attack, actual large advantage, broken fixed h, low security bits, or any category result. Conservative worst-case search caps need not be typical costs, and the displayed generic inequality need not be close to the particular constructed adversary's true advantage.

## One useful proposed accounting lemma, and its exact limit

**OPEN — proposed next lemma 1: random-full-oracle selected-restriction lift.** In a separately defined globally random full256 raw-oracle experiment, construct a coherent simulator that uses the external random node128 target restriction only on the exact selected (S,T_r,x16) block, and simulates all other raw words and independent selected lower128 limbs locally. Show that the FULL source-facing global-oracle channel, persistent private maps, actual current root/cache, completed-call gates and final verifier retain their law. Its desired external target count is Q_target<=Q_A+1: at most one selected call per adversarial raw query, plus at most one final verifier call; honest selected image use comes from the challenge Y, and all other honest work is simulated outside the selected target restriction. Actual source time/storage is still charged in full.

**PROVED — source geometry supporting, but not completing, that proposal.** Typed encodings S16||zero48||ADRS22||payload are injective for fixed node16 payloads. Other typed addresses are distinct and other source payload lengths have different total word lengths. A nonzero-S message-inner word R16||S16||root16||m cannot equal a selected typed word: equality of the second16 bytes would force S=zero16. The outer digest word has length52, not102. Source type-0/type-3 selected image calls are explicitly intercepted by the accepted known-image helper; a final classical verifier visits the selected edge at most once. These observations support Q_A+1 only AFTER a complete raw-oracle lift proves coherence and all alias cases; they are not a completed quantitative bound on the fixed h.

**OPEN — six obligations for that one lemma.** Prove exact encoding/domain decomposition; all source raw-word aliases including message inputs and nonzero-seed routing; independence of full selected lower limbs and all off-domain words in the randomized experiment; a reversible controlled router with no query measurement and counted target calls; consistency of the honest known-image/complete-response interfaces; and finite efficient local random-function simulation with its errors, gate/time/workspace and complete byte-length caps. This lemma would concern an explicitly RANDOM full oracle. It would not prove actual fixed-h hardness or let a known fixed algorithm be replaced by locally chosen random functions.

**PROVED — target-only accounting does not repair this aggregate at the requested Q_A.** Even if the proposed lift lawfully gave Q_target=Q_A+1 and the same generic inequality, the unamplified honest q/setup costs would disappear, but the aggregate diagnostic would still be (381/64)(Q_A+1). It caps at 1 for Q_A=2^32 and 2^64, indeed for any nonnegative Q_A when the final selected verifier query is counted. The lemma is useful for precise resource/interface accounting and per-hop estimates; it is insufficient to certify these parameter rows with the coarse geometry/UD inequality.

**COMPUTED / conditional PROVED — active-selector weighting is also insufficient here.** Only WOTS selectors with p>r are active in hop r. If a lawful per-fixed-label generic bound were available at a common Q_target, its weighted sum could replace 2^55*254 by the exact sum of protected positions

C_p=3360(2^41+2^36+2^31+2^26)+518160*2^21=7,628,143,271,608,320.

The resulting hypothetical UD coefficient is 12C_p/2^64=682009155/137438953472, with a nontrivial Q_target threshold of approximately 201.520687. This is a smaller diagnostic than the uniform 254-hop maximum, but still caps at 1 for Q_A=2^32 or 2^64. It is not a replacement for a joint-oracle lift or fixed-family certificate. A successful quantitative path would need a stronger event-specific bound or a lawful mechanism reducing the geometry/hybrid loss, alongside applicable hardness; target-only counting by itself cannot deliver the requested capacity/security conclusion.

**PROVED — the saturation claim is only about these coarse substitutions.** The coefficient 381/64 treats all254 constructed delta_r as if each reached the same uniform insecurity cap. Inactive/FORS/dummy selectors actually contribute zero; signed consecutive gaps can cancel, and the particular selected matching-image event may have much smaller gaps than generic UD insecurity. The C_p calculation is one more refined upper envelope, still based on separate generic maxima and triangle inequalities. Neither saturated expression is a lower bound on actual sum delta_r, nor an impossibility theorem against a target-only lift PLUS a sharper activation-aware, signed or joint aggregate argument. The proposed next accounting lemma should preserve exact active-selector probabilities and signed gaps before taking absolute values, rather than silently reinstall the uniform254 maximum. A successful joint refinement remains OPEN, including whether its final bound can become useful at the stipulated Q_A.

**OPEN — remaining frontier.** The accepted manual interface replaces an unnamed final-hidden-input probability by explicit ordinary PRE/UD advantages. This analysis evaluates no such actual advantage. Quantitative fixed-family hardness, all private/message/graph/canonical terms and full composition remain unestablished. This task adds zero source-game declarations and establishes no whole-security goal.

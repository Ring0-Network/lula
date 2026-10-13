# New independent first: lossy primary ITSR reduction for the free-counter family

Saved BEFORE reading any NEW selected probabilistic-lift proposal. Earlier firstb077, clarification77b1, event bindingbb839, canonical-family separation and current peer receipt4d3ff1 remain unchanged. This new argument distinguishes an exact-law mismatch from the possibility of a lossy reduction. Source is still ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. No hardness number, RO bound, source attack, timing campaign or protected write is used.

## 1. The actual primary game and a different virtual function

Use the independently checked primary ITSR oracle: on a chosen logical message x it samples a fresh uniform key R16 and returns R and MAP(H(R,x)); local evaluations do not enlarge the target union. A candidate (R*,x*) must not be a registered pair and its coordinates must be covered.

Construct a public FREE-COUNTER family H_free^h whose logical input encodes (S16,Z16,M,c32), and whose key is R16 alone. It evaluates the actual literal source functions

U=h(R||S||Z||M), D=h(U32||BE32(c)||S16),

and returns (S||Z)||D, a512-bit virtual output. h remains the ONE known full256 implementation. MAP takes route (S,Z,I) of297 bits, where I is D bits162–202, and the17 leaf values from D bits0–152. The context tag is in the VIRTUAL output/map, not in either h input. Filter bits153–161 are checked by the source adapter on its target/candidate; MAP may ignore them because allowing more primitive covered candidates only strengthens the insecurity assumption. On the matched successful branches all registered targets and the source final candidate pass the actual zero9 filter.

This is an explicit different primary function/map instance, not canonical H_can and not a random512-bit hash. No numerical ITSR theorem for uniformly random297-bit routes is inferred. Earlier canonical-family ITSR success0 versus arbitrary-counter success1 remains intact: it concerned H_can, not H_free.

For a fixed ex-ante source message-byte bound b, a total injective logical input format is possible without invalid-code aliases. Let V_b=sum_(j=0)^b256^j and use the lexical byte-string rank rank(M)=sum_(j<|M|)256^j+BE_integer(M). It fits8b+1 bits. Decode EVERY such rank value by the inverse infinite byte-string enumeration; all decoded messages have length at most b+1. Encode logical x as S256? More precisely S16||Z16 (256 bits), c32, and an(8b+1)-bit rank field, for alpha=8b+289 bits. All bitstrings parse into one unique context/counter/message; no dummy-invalid constant function creates a trivial freshness collision. Source inputs M<=b use their exact ranks. h still hashes the decoded original M bytes, without the logical rank. The virtual primitive assumption includes the slightly larger decoded-message domain; it is not silently the same quantitative bound as an unrelated primary instance.

## 2. Full-query counter guessing: an initial lawful but loose route

B samples the actual source S/F, retains F and source caches, computes the genuine root Z through the same h and finite setup, and preserves A's pre-key continuation with S/Z withheld until normal release. Thus all source auxiliaries and public raw computations are consistent. No F advice is given to A and no independent uniform root is substituted.

For each NEW message M, choose guess c uniformly from[0,L), L=2^32, BEFORE the target query. Query the primary oracle on Enc(S,Z,M,c); it returns uniform R and the target coordinates. Assign J[M]=R and compute the true source canonical c0(R,M) locally using h. If no c0 exists, use the source absorbing nonwinning behavior. If c differs from c0, terminate B with an ARTIFICIAL nonwinning abort. If equal, finish the original source signing response. Repeated M uses the saved R/c0, without another target query/guess. Every public hash remains local h.

For EACH fixed completing source nonce/message/context, exactly ONE of the L guesses equals c0. Hence a matched target channel is1/L times the successful source target channel, unnormalized. No acceptance-probability or nonce-distribution assumption is used. Across N distinct target labels in a source winning history, the exact matched weight is L^(-N). N<=q gives the valid one-sided bound

Pr[C_source] <= L^q Succ_ITSR(H_free;B_full).

This is a reduction for a different family with an explicit artificial-abort loss, not exact unconditional source-oracle equality. Source bottom mass remains nonwinning and unnormalized. The primary input's counter is chosen before the nonce, exactly as required; loss accounts for that chronology rather than denying it.

## 3. Sparse17-coordinate selection improves the worst-case loss

C_source is Win AND indexed C_cov from CHANGED-CHILD Section5, not bare old-message coverage. A covered final candidate has17 real tuples at one route. For each tuple choose the earliest COMPLETED honest signature exposing it. At most17 distinct message labels suffice, since repeated M has the same J nonce, canonical digest and routing coordinates. Number new message labels in first-occurrence order1,2,...; on a source winning history their count is at most q initiated requests.

For q=0 coverage is impossible. For q>=1 set k=min(17,q), and Q to the least power of two at least q. Thus q<=Q<2q except equality at powers of two. Before interaction sample k independent selector slots uniformly from[1,Q] using exactly k*log2(Q) fair bits. Duplicates and slots beyond the eventual label count are retained, not normalized away. A NEW label whose ordinal is in this secret selector set gets its nonce via the primary oracle and a uniform counter guess as above. Other NEW labels get locally sampled independent uniform16-byte J values. Repeats always reuse J[M]. B makes at most k PRIMARY target queries while still simulating ALL q source signing requests with consistent F/h.

On a particular source C_source history, let W be the distinct labels of the chosen17 witnesses, d=|W|<=k. Sort W and pad that list to length k by repeating its first element. W is nonempty on coverage. The probability that B's selector vector equals this particular padded list is Q^(-k), regardless of how the source/adversary adaptively selected those messages. This event targets EXACTLY W. Conditional on the source nonce values, every selected canonical guess succeeds with probability1/L, so all d succeed with L^(-d)>=L^(-k).

On those selector-and-guess events B's source-facing behavior is the SAME as the source history, all selected primitive targets are the actual canonical covered witnesses, and their union covers the final17 tuples. The final source M* is fresh among ALL initiated requests, so Enc(S,Z,M*,c*) is a new primitive message irrespective of nonce collisions. Output the parsed(R*,Enc(S,Z,M*,c*)) if the exact source Win/filter/coverage checks hold. Candidate c* may be ANY accepted counter; H_free evaluates precisely that counter.

Therefore a particular legal primary adversary B_sparse satisfies

Succ_ITSR(H_free;B_sparse) >= (Q L)^(-k) Pr_SrcFJideal_h[Win AND C_cov],

or equivalently

Pr_SrcFJideal_h[Win AND C_cov] <= min(1,(Q L)^k Succ_ITSR(H_free;B_sparse)).

A supremum primary insecurity at B's actual runtime and at most k target queries upper-bounds the particular success. This source-relative selector/counter factor is not an evaluated security certificate. Its magnitude can make the bound quantitatively useless; no practical capacity/category conclusion follows.

## 4. Adaptive quantum A and exact probability justification

Selector slots, guesses and newly drawn target nonces are classical. A's signing messages are classical, even when A's retained computation/public-h queries are quantum. On every matched selected-label prefix, the full returned signature and retained A state coincide with source execution; selectors/guesses are not disclosed. Locally sampled and oracle-sampled J values have the same independent uniform law. Thus the source state transition on a successful selected request is scaled by exactly1/L, and ordinary source transitions apply on unselected/repeated requests. This gives a subnormalized-channel coupling without observing coherent raw-query support or extracting quantum query transcripts.

Alternatively integrate over complete source classical service/final-output histories and independent selector/guess tapes. For every history in C_source, the particular padded witness list has probability Q^(-k), and d selected canonical matches have probability L^(-d). Quantum measurement probabilities of that history are unchanged on those prefixes. Integration proves the inequality. No independence of the final witness from messages, root, F, or hash output is assumed; only the selector/guess coins are independent and the constant1/L match probability holds for every completing nonce.

## 5. Partiality, context and resource gates

Actual setup failure or a requested source counter/service noncompletion is nonwinning in both programs. An incorrect counter GUESS is a distinct artificial B abort; it must not be described as a native source failure or hidden by conditioning on completion. Source C_source already requires completed signing responses, so no1/tau normalization or new Commit API is used. Primary mismatched/failed-filter targets may enter its registered ledger, but B immediately returns failure and never uses them to win. On matched C_source branches selected target records equal the genuine witness signatures' coordinates.

All actual public parameters/root/F correlation, literal aliases including S=0, whole256 inner and outer values, and source verifier/freshness remain unchanged. No extra zero-seed charge arises from the interface identity. Private F remains B's independent internally generated state, not A's advice. The source public graph/H/G/D7 events are not proved by this coverage reduction.

B performs the same complete source setup, q signing jobs, full counter searches, dictionary/tree/cache work, final verifier and quantum A/public-h circuit work, plus k exact uniform selector/guess sampling and classical primitive queries. There is no sampling over the entire nonce space or exponential hash table. A target evaluation in H_free uses one complete inner hash and one complete52-byte outer hash; that challenger work is separately charged, in addition to B's local canonical search. Repeated labels use dictionaries. Logical rank encoding/decoding is polynomial in b, and all h/circuit/bit-index generation costs remain explicit. B still executes quantum A, not a classical state-vector simulation. All time/storage bounds are source-relative and finite under the original ex-ante bounds.

## 6. Status and next control

This new manual argument provides a lawful finite-resource one-sided PRIMARY ITSR reduction for the explicitly free-counter/context-lifted family, with a sparse loss controlled by at most17 witnesses. It does NOT derive hardness of H_free from H_can, ordinary SHA, private-prefix PRFs or a RO model. Its whole-fixed-h signature bound, numerical advantages, category/capacity and kernel/game refinements remain open.

An exact finite control should enumerate selectors, counter guesses and nonce tables for tiny q/L, compare weighted source covered histories against sparse B success, include repeated labels and variable numbers of distinct requests, and exhibit canonical-family separation without confusing its different family. It should also test finite bottom without normalizing the nonce law. No NEW selected probabilistic-lift file has been read at this save.

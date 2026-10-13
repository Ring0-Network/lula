# Classical source-bound FORS coverage bridge in the joint ideal game

**Scope.** This derivation reads the original Rust hash/signing interfaces, the already completed joint F/J privatization derivation, and this agent's prior two-stream padding lemma. No other new agent proof was read before this file was saved. A root coordination hint about unique message labels was received while writing; the full argument below is independently derived. This is a coverage-route lemma in a specified classical random-oracle ideal game, not complete LULA I security or a claim about fixed SHA-256.

## 1. Exact game, encodings and budgets

**ASSUMED — inherited idealization.** Key components are sampled independently uniformly: private 128-bit K/P and public 128-bit S. The already defined joint ideal game uses independent memoized full-image maps F(A), J(m), returning their first 16 bytes for secret derivations and message randomization. Every other complete SHA call uses one shared 256-bit public oracle O. Setup and signing remain partial source algorithms; noncompletion yields no winning completion. q bounds initiated atomic signing requests across all restored branches; Q_H counts all adversarial raw O evaluations, including pre-key queries and local verification work. There is one additional challenger verification. No timing, cache bytes, private objects, compression-function queries or quantum access is granted.

**PROVED (source).** For fixed public key (S,r),

    R_m = Trunc128 J(m)
    I(R,m) = R || S || r || m
    U(R,m) = O(I(R,m))                 [256 bits]
    E(U,c) = U || BE32(c) || S         [52 bytes]
    D(U,c) = O(E(U,c))                 [256 bits].

The signer tests c=0,1,... and accepts the first whose omitted FORS digit Z is zero. The remaining digest coordinates give an exposure X=(instance,17 leaf indices). Their spaces are B=2^41, t=512, K_real=17. Exactly 203 digest bits are used (41+153+9); the unused bits do not alter the product distribution. The verifier accepts arbitrary transmitted R and c; it does not recompute J(m) or test minimality.

**PROVED (source separation).** On S!=0, every addressed public SHA input starts S||0^48 and has length at least 102 bytes; I inputs have bytes 16..31 equal to nonzero S, so cannot be addressed inputs. Outer E inputs have length 52 and cannot be addressed inputs. The relevant unaddressed I/E languages can still overlap: arbitrary names cannot be declared independent functions.

Define the larger inner language L_I(S) as all raw strings of length at least 48 whose bytes 16..31 equal S. Its suffix after byte 48 is a unique message label. Define eligible outer points L_E(S) as all 52-byte strings ending in S whose bytes 16..31 are NOT S. Each is uniquely E(U,c), with U[16..31]!=S. These two languages are disjoint. Their membership is determined by the input and the fixed S before the oracle output is sampled, including before S is disclosed. Let N_I and N_E be the possibly random numbers of distinct adversarial raw points in these languages. Pathwise N_I+N_E<=Q_H. In detailed probability bounds below, Q_I and Q_E denote their EXPECTATIONS in the unflagged ideal execution (or declared jointly bounded deterministic class budgets), so Q_I+Q_E<=Q_H. Do not plug one observed random count into an unconditional probability bound, or sum separately maximized class caps without a joint constraint. Other raw queries may influence the public history but do not directly create coverage candidates or inner values in this argument.

**PROVED — seed-distribution scope.** The displayed beta below is an UNCONDITIONAL JOINT-IDEAL bound with uniform S and an explicit 2^-128 bad-zero-seed contribution. For every fixed nonzero S, the same good-prefix argument applies and its stream-security loss alpha omits that contribution. Averaging the fixed-nonzero argument and assigning success at most one on S=0 gives the displayed unconditional beta. No transcript is renormalized after successful setup or after avoiding Bad. If two separate unconditional triangle bounds are used, delta_joint + beta charges S=0 twice conservatively. Charging it once requires a simultaneous stopped coupling with one shared S=0 flag; it cannot be justified by silently subtracting a term from two conditioned estimates.

## 2. First bad events

**PROVED — operational definitions.** Run the unflagged joint ideal algorithm, with hidden analytical flags. At the first occurrence of any of the following, stop the good-prefix coupling; do not change an oracle answer or tell the adversary about the flag.

1. Bad_S: S=0. Its probability is 2^-128. It can be shared with the already charged privatization event when composing losses; counting it twice is conservative, not necessary.
2. Bad_Rpred: before the first signing request on label m, an adversarial raw query equal to I(Trunc128 J(m),m) has occurred. Include pre-key queries using the eventually fixed public key. New signing means a previously unqueried message, not a different message whose R happens to repeat.
3. Bad_end: an O output at a distinct L_I point used by adversarial querying, honest new-message inner hashing, or final inner verification has its last 16 bytes equal to S. This removes I/E aliasing for every inner-derived U used by the source. It is not necessary to assume the public root has any independent uniform distribution.
4. Bad_U: two distinct relevant inner inputs have equal full 256-bit outputs, with at least one being an honest new-message signing input. Relevant partners are honest signing inputs, adversarial L_I query inputs, and the final verification input. Identical repeated inputs are not output collisions.
5. Bad_Epre: a fresh honest new-message inner output U matches the 32-byte prefix of any earlier adversarial eligible outer point. This captures adversarial previewing of a future honest counter stream. Matching an older honest U is already covered by Bad_U.
6. Bad_exhaust: some new-message FORS search finds no accepted digit in its first C=2^32 distinct counter inputs. This event is included conservatively to make the finite good-prefix stream mapping explicit. It does not install an exhaustion-return API into the source.

**PROVED — R repeats are not inherently bad.** I(R,m) is injective in the pair (R,m) for fixed S,r. Different m values therefore produce different inner inputs even if J(m)'s 128-bit prefixes collide. Repeated signing of the same message uses the same route and leaf vector and adds no coverage. There is no gratuitous q^2/2^128 R-birthday term in this bridge. If a known old R is guessed for a new m in a public prequery, that literal prediction is charged in Bad_Rpred.

## 3. Budget for inner prequeries: no repeated q factor

**PROVED in the joint ideal game.** Each raw point x in L_I has one candidate R=x[0:16] and one message m=x[48:]. If m has not been signed when x is queried, J(m) is an unrevealed ideal-map value; it is independent of the entire public history that selects x. Each such literal prediction has unconditional hit probability 2^-128. The extra fixed S/root header conditions can only restrict which predictions become actual honest inner points.

The adversary may choose later which previewed message to submit, but every successful preview must be among the at most Q_I literal predictions already made. Sum over those predictions, not over all q signing calls times all Q_I queries:

    P(Bad_Rpred) <= Q_I / 2^128.

This counts a raw point once across all future signing requests. If the message was already signed at that raw query, its J value is public through the signature, but it cannot be a future NEW-message signing input. There is no public J oracle in this ideal game. The real game requires the preceding joint-privatization loss; applying fresh-J independence directly to the real transcript would be circular.

Pre-key points also have a fixed suffix m and literal R candidate. J is unused by setup and independent of those queries and the setup-derived root. No future choice of root or m can change that already fixed literal prediction into many guesses. This is an unconditional union argument, not an assertion that conditioning on all previous hidden failures leaves the posterior uniform.

## 4. Remaining quantitative budgets

**PROVED — endpoint half.** On a good prefix, fresh L_I evaluations cannot be old addressed evaluations or old honest outer evaluations: S!=0 gives addressed separation, and prior honest outer prefixes have last-half !=S. A previously queried L_I point contributes its output only once. An adaptive fresh L_I output has probability 2^-128 of ending in S. Thus

    P(Bad_end before another bad event) <= (Q_I+q+1)/2^128.

The q+1 counts honest new-message inner calls and a potentially fresh final inner call. For pre-key raw outputs, S is an independent hidden uniform value; the same unconditional upper bound applies to their endpoint comparisons. Repeated source/public queries do not create a new sample.

**PROVED — relevant inner collisions.** Once Bad_Rpred has been excluded up to a new signing call, its inner point is fresh. At a fresh distinct inner evaluation, the full 256-bit output is uniform independent of the previously stored target values. Count each honest/adversarial input pair once at whichever distinct evaluation occurs later. Only pairs containing a signing inner point are needed; arbitrary collisions between two public inner values do not alone put a fresh forgery in an honest counter namespace. Consequently

    P(Bad_U before another bad event)
      <= (q Q_I + binom(q,2) + q)/2^256.

The last q allows a fresh final verifier inner output to hit any honest U. If it was previously queried publicly, its pair was already charged. If its input equals an honest input, injectivity would force the same message, which is excluded by EUF freshness. This is a conservative pair bound; it does not charge billions of addressed node evaluations, which have a disjoint input language.

**PROVED — future outer namespace guesses.** At a fresh honest inner point, U is uniform. It matches one of at most Q_E previously queried eligible 32-byte outer prefixes with probability at most Q_E/2^256. Across at most q new-message signing calls,

    P(Bad_Epre before another bad event) <= q Q_E/2^256.

The repeated c values in one previously queried U namespace do not add distinct prefixes, so this is already conservative. This q factor cannot generally be removed: an outer point's prefix U does not encode the message label, so one guessed U may target any of several future new-message inner outputs.

**PROVED — why the public-query contributions combine once.** A raw point charged as an eligible E-prefix guess has bytes 16..31 different from S. A raw point charged as an inner-output collision partner has bytes 16..31 equal to S. No single raw point belongs to both classes, including points queried before public-key disclosure because S is fixed from the start. Therefore q Q_I + q Q_E <= q Q_H. This does not say all bad events are disjoint: a future U might trigger several flags, and the union bound can overcount that occurrence. It says the public-query class cardinalities supporting these two 256-bit terms are disjoint. The binom(q,2) and q terms separately count honest/honest and fresh-final/honest inner-output pairs; they are not public-query terms.

For adaptive random schedules, charge each distinct input pair at its later fresh evaluation. Its earlier target is already fixed, and its fresh-output equality probability is at most 2^-256. Sum these predictable target counts and take expectations. The pathwise number of cross-class pairs is at most q(N_I+N_E)<=q Q_H. This explains the expectation notation without assuming fixed class allocations or a nonadaptive query schedule.

**PROVED — finite search component.** While no earlier bad event occurred, the new honest counter namespace has not been publicly prequeried, is disjoint from all prior honest namespaces, and is disjoint from L_I and all addressed hashes. Its C distinct oracle outputs are iid uniform. Its no-success probability is (1-1/t)^C. Therefore

    P(Bad_exhaust before another bad event) <= q(1-1/t)^C.

For t=512,C=2^32,q<=2^40 this is conservatively at most 2^-8388568. It bounds an ideal fresh-search failure event, not an implemented abort response or a worst-case computation time.

**PROVED — combined sufficient bound.** In the unconditioned partial joint ideal game, the first-bad union gives

    beta(q,Q_I,Q_E)
      <= 2^-128 + (2Q_I+q+1)/2^128
         + [q(Q_I+Q_E)+binom(q,2)+q]/2^256
         + q(1-1/t)^C.

A bound using only the supplied total raw-query cap is

    beta(q,Q_H)
      <= min(1, (2Q_H+q+2)/2^128
                + [q Q_H+binom(q,2)+q]/2^256
                + q(1-1/t)^C).

The collision/guess charges concern different bad routes and may overlap; union-bounding them is valid. When combined with the preceding privatization bound, the S=0 event may be charged once via a shared flag. A large or vacuous sufficient bound is not a demonstrated attack or a signing-capacity certificate.

## 5. Actual fresh counter streams on a good prefix

**PROVED — honest exposure.** At the first atomic request for a new message, Bad_Rpred's absence makes I fresh. Bad_end's absence puts U outside the inner/outer alias half. Bad_U excludes earlier honest namespaces, and Bad_Epre excludes adversarially prequeried counters in the new namespace. All C outer inputs are distinct and fresh. The smallest accepted counter selects only on the nine-bit omitted coordinate. The instance and 17 real leaf coordinates of the accepted digest are therefore uniform on [B] x [t]^17, independent of the accepted counter and rejected prefix outputs. Atomicity prevents new public prequeries between the private inner evaluation and completion.

**PROVED — public candidate.** An eligible outer point is either an old public point (no new candidate draw), an old honest namespace (cannot be a fresh-message forgery on a good prefix), or a new fresh point. Eligible outer points cannot be addressed hashes or inner-language points. Each fresh eligible nonhonest point therefore supplies one iid raw candidate Y, retaining the omitted-coordinate filter rather than conditioning it away. These candidates may be queried before or after signing and kept until later exposures cover them.

**PROVED — fresh-message final classification.** Let m* be fresh and use any forged R*,c*. If U*=O(I(R*,m*)) ends in S, Bad_end has occurred. Otherwise E(U*,c*) is eligible. If U* equals any honest signing U, the inner input cannot equal that honest input because m* is fresh; hence Bad_U occurred. With those bad cases excluded, the final outer point is not an honest namespace. It is either among adversarial candidate evaluations or is a new final-verifier candidate. Pathwise the number of candidate opportunities is at most N_E+1<=Q_H+1. The expectation Q_E is NOT a pathwise cap. There is no requirement that R*=J(m*) or that c* be minimal.

**PROVED — exhaustive old-point cases.** The oracle table gives the following complete partition for an eligible final E point:

- An old rejected honest grinding point has Z!=0 and fails the verifier's forced condition, regardless of later coverage. It cannot win.
- An old accepted honest grinding point has the same U and counter as an honest signature. A fresh final message makes its inner input different, so matching this U is Bad_U. Changing the forged R does not change input injectivity.
- A counter not previously evaluated in an old honest U namespace still needs that same U; fresh-message matching is again Bad_U, even if this particular E point would itself be a fresh raw oracle point.
- An old adversarial eligible point in a nonhonest namespace supplies a retained Y candidate from its first fresh evaluation. Repeated queries consume no additional sample. If that namespace had subsequently become honest, Bad_Epre or Bad_U would already have occurred.
- An old addressed or I-language point cannot be eligible E on the good prefix, by literal input separation; an old private F/J point is not an O-public evaluation in the joint ideal game.
- A genuinely unqueried nonhonest eligible E point is sampled during final verification and supplies the extra one candidate draw.

The final verifier's inner evaluation likewise is either an already public inner point or one new inner output. Its endpoint-half event is included in Bad_end; its collision with an honest U is included in Bad_U. Freshness excludes equality with a previously signed inner input. No old rejected digest is reclassified as an accepted independent sample.

## 6. Joint coupling and coverage-route theorem

**PROVED in the stated ideal game, manual source refinement.** Assign iid X values to accepted new-message exposure draws, with independent geometric/rejected-counter noise, and iid Y values to fresh eligible adversarial/final outer evaluations. Assign independent raw images to remaining fresh oracle points. The good-prefix domain and namespace checks ensure no input is assigned inconsistent independent images. Adaptive names and schedules merely consume stream prefixes; repeated messages/points reuse old values. At the first bad event, continue the unflagged ideal game without claiming stream correspondence.

This is a prefix coupling to unconditional ideal streams. Do NOT condition the entire execution on 'Bad never occurs' and then assert iid distributions: avoiding Bad can bias future stream selection. Padding the independent exposure prefix to q and candidate prefix to the DETERMINISTIC cap Q_H+1 only increases coverage. Q_E=E[N_E] is used solely for the predictable bad-event accounting and cannot replace this padding cap; adaptive candidate allocation can depend on the realized transcript. With p_fixed(q)=t^-1 E[(1-(1-1/t)^N)^17], N~Bin(q,1/B), the prior padding lemma yields

    P_IDEAL(covered-leaf route for a fresh-message output)
      <= beta(q,Q_H) + min(1,(Q_H+1)p_fixed(q)).

The whole right side may be capped at 1. The coverage event includes acceptance of the omitted-coordinate filter and all real-tree indices lying in honest exposed sets at the selected instance. It is only one route in a full signature reduction. Claiming that every successful full forgery belongs to this route would omit changed-node/chain/root witnesses and is not done here.

**OPEN — remaining complete-security obligations.** Compose the preceding joint real/ideal loss with this ideal coverage bound, validate the manual source refinement independently, and prove the full forgery classification/extraction and its resource costs. The bridge does not close WOTS certification, tree/FORS-root binding, efficient primitive challenge extraction, complete total advantage or QROM security. No manuscript, earlier packet, parameter set or timing record is changed.

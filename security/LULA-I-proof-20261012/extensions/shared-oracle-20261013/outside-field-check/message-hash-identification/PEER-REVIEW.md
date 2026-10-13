# Independent review: message-hash covered-coordinate component

**Verdict: ACCEPT_MANUAL_CONDITIONAL_REGISTERED_CONTEXT_CTAC_COVERAGE_ADAPTER; PRIMARY_ITSR_TRANSFER_OPEN.** This accepts the source-interface reduction for an explicitly named canonical-target/arbitrary-valid-counter property. It does not identify that property with ordinary primary ITSR or supply a numerical fixed-h bound.

## Independent provenance and subjects

My first `INDEPENDENT-FIRST.md` SHA256 `b07700807df0f78be2272afd7a5372044603b92697b3760afaa8cdfac5a3a1df` was saved after direct release-source and primary-definition reading and before any new peer proposal. Its first clarification is preserved. I then read selected `INDEPENDENT-FIRST.md`, SHA256 `540ae17ba73ff61d178c3f8c96601bff18db857138c078f54b22ba10dfeb609f`, and the complete current CHANGED-CHILD-EXTRACTION.md to bind its coverage event. The source remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.

Primary versions are distinct and pinned separately: my cached SPHINCS+ r3.1 PDF `1169896fff4160e7a294162b8a3e061ffdf1888f3925f5614532c28bd3473c4a`, text `ddaf6d600a05c2e9b3bef113bf995827a79f76616f09f8e7b4cef0ba90e17323`, Section9.1 printed49/text1911–1935; the selected reader's fresh official round3 PDF, Section9.1 printed48/PDFindex47, read directly in this review, and its extracted text2325–2358. Both expressly return fresh uniform nonce/key AND mapped coordinates. HK22 Definition11 printed30/text1323–1346 is the corroborating restatement; its R/K and response typography are not turned into a different oracle definition. No missing statement from the failed2019 PDF fetch is assumed.

## Exact accepted source interface

The peer preserves full U=h(R16||S16||root16||M) and full D=h(U32||BE32(c)||S16), using the SAME fixed public h. The17 real9-bit indices occupy0–152, the forced-zero filter153–161, and the common41-bit route162–202. Route I gives bottom(tree=I>>5,keypair=I mod32). This is the actual source bit ordering and tuple namespace, not an128-bit truncated message hash or an eighteenth exposed secret.

The source target nonce is a persistent J[M] value, uniform on each first complete message label. B can emulate it by querying a fresh-nonce target oracle once per distinct M and caching the reply. The q budget covers initiated classical signatures across branches; at most q distinct target calls are used. Repeated messages and restores do not obtain fresh nonces. Source final verification instead parses arbitrary R*, arbitrary32-bit c*, and fresh M*, checking filter acceptance without nonce validity or counter minimality.

Actual S/root/F correlation is retained by B's exact source setup with its own persistent F and the SAME h. B retains F solely for generating consistent source signatures and internal state; it does not give A F as advice or an extra oracle. Public marginal/root replacement is unjustified. For a precise legal assumption, take the registered-context game allowing B to select one public context before independent target nonce draws; the actual B selects uniform S and its source-computed root. A worst-case bound for that explicitly declared game bounds this B. If instead the claimed insecurity uses a source-restricted context generator, define that generator and retained auxiliary-state law exactly. A numerical theorem for independently sampled roots does not apply by assertion.

The alternative tagged-message family Enc(S,root,M) can place context selection inside a fixed public function's legal message inputs, with tags decoded before evaluating h. That offers another interface construction, but its security must be assumed/proved for that exact family. The wrapper encoding never alters the literal h input words. Neither route closes the canonical/arbitrary-counter mismatch with primary ITSR.

A's fixed-h pre-key computation and quantum continuation are preserved while S/root remain withheld; setup is sampled/executed consistently before normal release. Moving hidden key-only setup across h-only pre-key computation is a coupling on disjoint registers in the untimed model, not conditioning on posterior outcomes. Private signing services remain classical; public h's clean coherent circuit, byte lengths and generation/workspace costs are charged.

## Canonical-counter gap and chosen property

Ordinary ITSR for H_can gives source canonical targets but restricts its final mapped candidate to its canonical counter. A source verifier can accept a covered NONcanonical counter whose canonical candidate is not covered. Conversely H(R,(M,c)) maps the final candidate correctly, but its target oracle samples R after B commits c; the source chooses c0 after R. A uniform key(R,c0) does not reproduce that nonce-dependent first-success distribution. The independent derivations agree on this exact lifting frontier.

The chosen RC-CTAC-SR(h) oracle samples/memoizes R per message and evaluates the finite canonical first-zero9 counter under the registered context. It returns/registers R,c0 and fullD/coordinates, or unnormalized bottom. Public h and returned R/c make fullD locally reconstructible; returning it does not posit an independently filled lower limb. Candidates have arbitrary accepted c*, arbitrary R*, and new-message eligibility. The stronger source freshness is compatible with primary pair freshness but must not be dropped from the source event.

Immediate target registration is sufficient. On an absorbing source failure the reduction never returns a winning candidate; on every winning source branch earlier targets correspond to completed atomic signatures. A larger registered ledger can only enlarge the primitive winning event, so the peer's one-sided bound needs no Commit interface or success normalization. Any optional Commit construction is unnecessary and is not part of this accepted minimal interface.

## Exact event and conditional inequality

The event is **Win AND indexed C_cov**, where C_cov is CHANGED-CHILD-EXTRACTION.md Section5's17 real tuples at the final common route, drawn from completed honest signing responses across all restored branches. Win includes fresh M*, valid source parser/filter and final root acceptance. It is NOT bare coverage for an old message. The source zero9 filter is retained, and duplicate secret values never merge distinct coordinate/address exposures.

B runs the exact source with retained F/h/cache state and target-derived J nonces, records the completed tuples, parses A's final classical candidate, and outputs it when the eligible covered-coordinate event holds. This gives

Pr_SrcFJideal_h[Win AND C_cov] <= Succ_RC-CTAC-SR(h)(B_cov).

It also bounds a smaller no-H/no-G genuine-reuse event. It does not certify or bound separate hidden-secret/public-graph replacement events, and does not prove that all source wins are covered. The existing pointwise final-event cover and public-component lemmas retain their own obligations. S=0 and literal aliases are handled by the SAME h and actual source parameter draw; no extra seed-zero penalty is introduced by this interface identity.

## Independently executed discriminators and helpers

Own controls exited0. They include a singleton-nonce counter-policy separation and a two-nonce/full17-tuple version with the actual bit positions/filter: canonical fresh-pair ITSR has maximal toy success0, while canonical targets with an arbitrary accepted fresh-message counter have success1. This is an abstract interface separation, not the source hash/predicate or an actual attack. Repeated fresh-nonce calls agree only1/2 in the toy law, whereas cached first replies agree1; the cache wrapper matches source J exactly. Independent-root replacement has the same public marginal but changes its signature-visible auxiliary consistency probability1 to1/2. Four literal source-byte test cases validate full256 inner/outer framing, first zero9 search within the control cap,17 indices and41 route bits. None proves uniformity or a universal search-completion bound.

I read and independently reexecuted `root-message-hash/DigestProjection.lean` under existing Lean4.28/Mathlib. It exited0 and checked exactly three helpers using only propext and Quot.sound: prefix preservation, route all zero, filter all zero under zeroLower. These are SAME-word bit-function statements; they do not establish equality of two-stage message-hash prefixes after modifying the inner algorithm. They prove no SHA hardness, source refinement, ITSR game or signature security. If promoted, they add three supporting declarations to the existing44, not a checked whole-source/game theorem.

## Remaining obligations

Primary ITSR quantitative/game transfer for the canonical-target/arbitrary-valid-counter variant, legal context/auxiliary distribution under the claimed bound, numerical fixed-h message-hash hardness, full public graph/PRE/TCR analysis and complete security/category/capacity remain OPEN. No RO coverage scalar, occupancy uniformity, private-prefix PRF hardness implication, or HJ[h]=HJ[O] identity is used. No protected source, manuscript, prior receipt, numerical theorem, or current-index file was edited.

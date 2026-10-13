# LULA I writing and formatting review

## Overall assessment and scope

Full manuscript prose reviewed for all eight dimensions after source reconciliation; scientific correctness is evaluated separately in PROOF_AUDIT. The central argument is now a conditional common-reference transfer, with recovery cost and missing reference proof stated in the abstract and limitations. The supplied Jolt lightweight paper guides the unchanged LNCS appearance, not the technical scope or claims.

| Dimension | Score/5 | Evidence |
|---|---:|---|
| Cohesion |4|Consistent reference signer/cache terminology and explicit antecedents |
| Coherence |4|Problem→specification→correctness→transfer→costs→limitations |
| Cadence |4|Direct short claims alternate with technical derivations |
| Lexical quality |4|Observed/expected/proved/conditional kept distinct |
| Argumentation |4|Conditional inference stated explicitly; no partial proof promoted to full security |
| Academic register |4|English prose, author stance, attributed borrowed mechanisms |
| Section compliance |4|All requested research-paper components, algorithms and appendices included |
| Grammar/mechanics |4|Citation/notation/table sweep; final PDF checks recorded separately |
| Overall |4|Writing quality only; no submission acceptance prediction |

## Critical issues corrected in the authored source material

1. **Argumentation, CRITICAL.** Source quote: “What memory may safely hold: only values that are deterministic functions of the key (T2).” Rewrite: “State need not consist exclusively of deterministic key-derived bytes. A diagnostic counter or random eviction policy that never changes emitted evidence can be harmless.” The rewritten paper requires observable common-reference behavior.
2. **Argumentation, CRITICAL.** Source quote: “In call counts both budgets are met: signing worst 100,586 calls”. Rewrite: “The measured maximum of 100,586 calls is simply the largest value in one recorded sample.” Counter search has variable length.
3. **Argumentation, CRITICAL.** Source quote: “Classical FORS bound 2^-132.6 per try at 2^40 signatures.” Rewrite: “The number 132.56 is therefore not the proved security level of LULA I.” The manuscript gives the precise uniform coverage formula and its limited event.
4. **Argumentation, CRITICAL.** Source quote: “Only (a) is compatible with the user's rule without adding the stateless cost.” Rewrite: “The relevant requirement is the signing behavior in the declared security interface.” Rejected universal storage taxonomy does not belong in the result.

## Major issues resolved

5. **Lexical precision, MAJOR.** Source quote: “Verification: always 3,265 calls”. Rewrite: “Public verification records 3,265 instrumented SHA-256 compressions, or 3,266 including prefix initialization.” The raw source compresses one prefix without updating the thread-local counter.
6. **Coherence, MAJOR.** Source quote: “Time: met in work on one core”. Rewrite: “Prepared-cache medians do not establish a 10 ms worst-case bound.” Historical maxima and cold recovery remain in the result, not a footnote.
7. **Scope, MAJOR.** Source quote: “What this document adds: the cache also stores the WOTS+C counters”. Rewrite: “The supported contribution is the exact integration and audit of canonical counter caching, together with measured lifecycle costs.” No general novelty proof inferred.

## Remaining publication judgments

The title is the exact user-requested title. Its resilience qualification is explicit in the abstract/security sections. A4 LNCS class, page numbers, theorem/proof environments, algorithm2e and splncs04 are used without altering class margins/fonts. ePrint's official rules require named authors; conference anonymity/page limits in generic skill notes are inapplicable. The author identity and publisher follow the user's explicit input. Final QA must check compiled citations, every page image, embedded fonts and absence of private identifiers. These checks do not establish the open full-security theorem or scholarly novelty.

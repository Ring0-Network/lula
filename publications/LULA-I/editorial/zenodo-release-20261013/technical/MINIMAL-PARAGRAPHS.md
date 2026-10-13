# Proposed English wording for the sole editor

## Memory and security tradeoff

Of the approximately 72 MiB cache payload, 64 MiB minus 16 bytes stores top-tree nodes and 8 MiB stores canonical counters. Omitting this retained cache preserves the 5,720-byte signatures and the same conditional reference-security transfer under honest-cache assumptions, but requires 8,602,517,503 additional SHA-256 compressions per signing call, plus the top-layer counter search. The current uncached implementation still materializes a temporary top tree, so this option reduces retained storage rather than eliminating working memory.

Partial node or counter caching and streaming tree traversal could offer intermediate tradeoffs if they preserve canonical reconstruction; these variants are not implemented or measured here. Lowering the top-tree height instead changes the cryptographic parameter set. With all other heights fixed, it reduces the address space and increases the uniform-selection FORS coverage-model probability; redistributing height changes other work costs. Either change requires fresh security and performance analysis.

## Optional analytical height illustration, independently checked

As an analytical illustration, reducing only the top-tree height from 21 to 20 reduces the logical cache payload from 72 MiB minus 16 bytes to 36 MiB minus 16 bytes, and the signature length from 5,720 to 5,704 bytes. At $2^{40}$ signing queries, the uniform-selection FORS coverage model's per-raw-candidate exponent changes from 132.6 to 125.9. This variant has not been implemented or measured; these component-model exponents certify neither full-signature security nor signing capacity.

If inserted, replace the first sentence of `LULA-I.tex:130` with “\Cref{tab:params} gives the single evaluated parameter set.” The analytical example is not a second evaluated set. Do not say the payload is exactly halved: the new payload is eight bytes less than half the old payload because the tree-root subtraction remains 16 bytes in both expressions. No new parameter table or security-bit label is needed.

## Hardware sentence replacement

Replace only the exact-hardware sentence in `stability-results.tex:2` with:

> These measurements used one pinned logical processor on a host with 32 GiB RAM.

Retain the subsequent unmatched-backend, non-isolation, repeated-key and different-security-objective qualifications. They explain the measurement scope without identifying a CPU model or OS. No model or OS needs to be added elsewhere in the article.

## Repository line below the conclusions

```tex
\paragraph{Project repository.}
\url{https://github.com/Ring0-Network/lula}
```

The URL still returned 404 to this review's anonymous read-only check on October 13, 2026. The neutral label implements the requested reference without asserting that public access or deposit has been verified. Do not substitute “available at” before public access is established.

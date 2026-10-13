# Primary comparison after independent derivation

The local argument was saved before this literature check. Its constants come from the explicit local norm/channel calculation; no unverified imported theorem is needed.

**CITED:** Bennett, Bernstein, Brassard and Vazirani, *Strengths and Weaknesses of Quantum Computing*, [author paper, arXiv quant-ph/9701001](https://arxiv.org/pdf/quant-ph/9701001), Section3.1, Definition3.2 and Theorem3.3/proof (PDF pages7–8), use query magnitude and a sum of modification errors in a quantum oracle hybrid. This is the primary methodological precedent. Here the local inequality is independently written with full-output XOR unitaries, Euclidean operator norm at most2 on the modified support, and normalized trace distance `D=||rho-sigma||_1/2`. No numerical constant is copied from a different oracle or variation-distance convention.

**CITED:** Ambainis, Hamburg and Unruh, *Quantum Security Proofs Using Semi-classical Oracles*, CRYPTO2019, [author publication page](https://kodu.ut.ee/~unruh/publications/semiclassical.html), identifies improved O2H results supporting multiple modified points and joint distributions. This reference suggests a possible route to tighter specialized losses. Full PDF requests to IACR returned403 during this review; no exact lemma constants or completed instantiation are attributed to an unread PDF.

**PROVED locally:** these private families are sampled/programmed jointly at the start, not adaptively reprogrammed after past quantum replies. REAL has the correct ordinary-RO marginal. The IDEAL state is independent of unused K/P, giving expected changed-support query mass at most1/N. This directly yields the conservative `2Q/sqrt(N)` state-distance term. It avoids defining a nonexistent classical query log for coherent queries.

**PROVED locally:** the classical atomic signing service needs separate channel treatment. Its arbitrarily many internal public I/E calls have at most two P nominations per initiated call; their ideal CQ transition differs on probability at most2/N. That derivation is not obtained by counting all internal calls as quantum adversarial queries or by invoking an O2H theorem without checking the service interface.

**OPEN:** tightness, formal verification of this channel calculus, an efficient implementation/simulator, any specialized O2H refinement, and all remaining full-signature QROM event terms. The primary sources do not discharge those source-specific obligations by their existence.

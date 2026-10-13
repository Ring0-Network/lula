# Clarification of independently saved first message-hash argument

The first save `INDEPENDENT-FIRST.md` SHA256 `b07700807df0f78be2272afd7a5372044603b92697b3760afaa8cdfac5a3a1df` remains unchanged. This clarification was written before reading any new peer message-hash proposal.

## No extra target-commit API is needed

The first draft's step3 restricts the exposure union to completed atomic signing responses and sketches a possible simulator-controlled commit. Such an API is unnecessary under the existing absorbing noncompletion convention. The simpler primitive can register its canonical digest at the target request immediately. If any later FORS/WOTS/signature stage fails to complete, B returns no winning candidate and the source experiment is absorbing/nonwinning. Consequently, on every winning B/source branch all prior registered target requests correspond to completed signature responses. Exposures registered on a failure branch never produce a winning reduction output. This avoids gratuitously strengthening the primary-style target service with commit control.

The declared CTAC-ITSR service should therefore sample/memoize the nonce, calculate the canonical first accepted counter, and register/return its full coordinate set on success. B uses that reply to finish the exact source signature; any later failure is absorbing. On bottom B likewise contributes zero. Fresh-message eligibility and the arbitrary-valid candidate counter remain unchanged.

## Exact equality needs the source auxiliary experiment named

Pr[C_source]<=Succ_CTAC(B) is the useful reduction statement. B can choose to output only after both exact source Win and the covered-coordinate event, yielding equality for that particular B, but the primitive's success predicate does not itself verify a signature or give A private F. The source simulator retains its own independent F only for setup/signature responses and internal event classification. No proof that all successful source forgeries have covered coordinates is supplied; the separate public-graph/replacement events remain necessary.

The canonical-target/arbitrary-valid-counter lifting gap to primary ITSR remains OPEN. The finite singleton-nonce/two-counter control is an abstract game separation, not a claim about the actual randomizer size, actual digit predicate, SHA hardness or LULA insecurity.

# Localized successor: nonzero-seed identity and original zero-branch charge

**PROVED — correction to the frozen localized candidate.** `LOCALIZED-FINAL-SUCCESSOR.md` SHA `db2de01bb6dbb5f4f7d6398f12e4763d258c54820a0b3186475cbf8e0c4e14df` remains unchanged. Its Sections3–4 identity must explicitly be read conditional on S!=0 when selected-type verifier records are classified by their raw86-byte header alone. This correction is required, not a new efficiency assumption.

The localized program B_cond samples S uniformly from the nonzero16-byte strings (or takes S as a fixed public conditional-game input), independent of selected j, key coins and the oracle. It chooses its padded56-bit j exactly as specified. All predecessor/challenge/source/extraction steps remain unchanged. Conditional game sampling is a proof device; no production key sampling is modified. The source's overall S remains uniform on all16-byte strings.

For nonzero S, the verifier's unaddressed inner word `R||S||root||m` cannot have a typed header `S||zero48||A`: its second16 bytes are S, whereas a typed header has zero16 there. Its outer word is only52 bytes. Thus every type0–4 raw-header match in the final verifier trace is an actual addressed type0–4 routine call at the selected route. The routed materialization is exhaustive for the raw-header-defined G_final event. The corrected exact identity is

`Pr[B_cond wins] = 2^-56 * Pr[source Win AND G_final | S != 0]`.

For the source's unconditional contribution, a safe bound is

`Pr_source[Win AND G_final] <= 1/N + (1-1/N)*2^56*Pr[B_cond wins] <= 1/N + 2^56*Pr[B_cond wins]`.

In a full-forgery composition, the single1/N S=0 term is paid once for the entire source event, outside all conditional component terms, not once per adapter. The conditional identity is unconditioned on setup/signing success; absorbing partiality and dummy selector branches remain as stated.

On S=0 a long unaddressed inner message word can match a typed header at an off-route address. The route-only materializer need not recover that address's genuine graph target, so the old unconditional raw-header-based G_final equality must not be asserted. The whole-word router still correctly forwards such aliases, and the eager full-forest extractor covers them; the localized extraction is deliberately used only in the nonzero-S component game. An alternative source-tagged final addressed-call event could avoid this alias issue, but is not silently substituted here.

The same qualification applies to the indicated finite-QROM final-classical-trace identity and the refined selected-handle Q+2q+4 cap. No coherent query transcript is extracted. No new source counter, key, filename, parameter or probability bound is changed.

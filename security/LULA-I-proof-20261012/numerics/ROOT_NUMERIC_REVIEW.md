# Numeric second-reader review of root synthesis

**COMPUTED — review status:** PASS for substantive numeric transcription and proof boundaries, with one minor last-decimal rounding correction notified to the root editor. This review cross-read root files only AFTER the independent derivation, numeric implementation and original-model checks were saved. No new experiment or numeric-behavior edit was made.

## Reviewed cut

| File | SHA-256 at review |
|---|---|
| `../PROOF.md` | `f3bbdd8bd6994ee089d4462503a129da5c4e3dccba60517eadca3960b811a1da` |
| `../TERM-TABLE.md` | `b18b407753236d2e7ba28f562ea2505d037adcb2c32e9f05d0531e3b21f102b6` |
| `../bounds.py` wrapper | `2bb8d35a5eaa73841ddfc92666fbeaa1438f362e030adfcb86c5ce3e67ead7f7` |

The root editor may subsequently apply the explicitly listed rounding correction. These hashes identify the inspected cut, not an assertion that root files must remain unchanged.

## Findings and acceptance checks

- **COMPUTED / PASS:** Every fixed-instance FORS exponent in PROOF §5 matches `bounds.json` rounded to nine decimal places. This includes all eight requested signature-query counts. The 143.262538581 / 132.563419944 / 125.902530385 figures in TERM-TABLE match q=2^38 / 2^40 / 2^41. The binomial/Poisson q=2^40 discrepancy is approximately 2.18e-11 bits, as copied.
- **COMPUTED / PASS:** Both exact target-sum cardinalities in PROOF §6 match the integers in `bounds.json`, including all thousands separators: 5181241160064611531897369560287267312 and 454918678781617793203528879683071744. No estimated slice size is substituted for the integer count.
- **COMPUTED / PASS:** Cache payload 75,497,456 bytes, cache node/counter counts, 5,720-byte signature arithmetic, subtree inventories, 19,212,937,084,272,640-address total PRF universe, and prepared/cold call-count arithmetic are consistent. A prepared signature's 12,961 logical secret-PRF calls include repeated derivations; its at-most 12,816 distinct addresses are a different quantity. Root text preserves that distinction.
- **PROVED arithmetic / PASS:** PROOF §5 subtracts the adversarial log2 query budget exactly and clamps a vacuous probability bound to exponent zero. Its q=2^40, Q_H=2^128 conditional exponent 4.563419944 is correct. The statement that demanded advantage <=2^-128 at that budget would require per-query probability <=2^-256 is correct. Root never presents this conditional arithmetic as the complete scheme bound.
- **COMPUTED / MINOR ROUNDING FINDING:** PROOF §10 reports 62.9512651925 for the q=2^41 square-root reading. From the unrounded computed exponent 125.90253038476634, division by two gives 62.95126519238317, which rounds to **62.9512651924** at ten decimal places. The current value comes from dividing the already rounded nine-decimal classical table entry. This does not affect any security conclusion; root was notified to correct the last displayed decimal. The other two ten-decimal square-root entries are correct.
- **OPEN boundary / PASS:** Full PRF, message-randomizer/shared-SHA, adaptive FORS, WOTS certification, tree extraction, H_msg and total rows remain OPEN. No full-security number or smallest full-security q threshold is assigned. In all eight independent JSON rows, `total_euf_probability`, `total_euf_bits`, and all unclosed attack terms remain null. Honest different-child WOTS reuse is zero only as its identified subevent; it does not set full WOTS advantage to zero. Conditional zero cache-transfer loss is not a reference security guarantee.
- **PROVED source-scope / PASS:** Root correctly states that only 17 real FORS trees exist and that the forced eighteenth digest coordinate supplies a public filter. Its WOTS address includes the tree coordinate. Its fixed-child/canonical-counter invariant applies to the honest reference; accepted corrupt counter substitution is treated separately.
- **CLI inspection / PASS, limited scope:** The root wrapper resolves the numeric script relative to its own path and invokes it with `runpy.run_path(..., run_name='__main__')`, preserving `sys.argv`. `--out`, `--samples`, `--toy-trials`, `--h`, `--a`, and `--k` are parsed by the numeric script. The last three override ONLY the FORS coverage model. WOTS checks and whole-universe inventories intentionally remain those of the fixed actual LULA I construction. The wrapper is a component calculator, not a parameterized full-scheme prover. Neither wrapper nor child script fills unknown total terms.

## Minimal independent-derivation clarification

**PROVED / editorial clarification:** The potentially ambiguous phrase in DERIVATION.md was changed from 'loses its 1/B selection factor' to '**must pay probability 1/B per full-digest trial**.' This preserves the existing formula and makes clear that targeting a preselected bucket does not remove its routing cost. No raw probability, numeric result, script or output behavior changed. Only the affected derivation hash and this newly added review's entry are refreshed in the local SHA256SUMS receipt.

**Final scoped verdict:** The root synthesis transcribes the independent component calculations and preserves the unestablished-total boundary. Its only numeric transcription issue is the listed last-decimal square-root rounding, already communicated for correction. A complete EUF-CMA or QROM security theorem remains **not established**.

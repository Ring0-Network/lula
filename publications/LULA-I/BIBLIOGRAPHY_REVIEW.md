# LULA I bibliography and citation audit

Reviewed 12 October 2026 against the frozen inputs in `editorial/bibliography-r8/baseline`. Three delegated reviewers independently checked entry metadata, citation support, and URL/repository identity. The final manuscript has **12 references, 20 citation occurrences, and 17 distinct external HTTP(S) links**. Every bibliography entry is cited; every intended URL and DOI is present as a complete PDF link.

The review found correct source objects, incomplete publication metadata, one incomplete standard locator, and one missing software attribution. Those corrections are integrated into the editable manuscript and compiled PDF. No observed link returned 404 or 410. ACM, IEEE, and Springer imposed access restrictions on some native requests; correct redirects and deposited DOI metadata establish the cited objects' identities, without claiming unrestricted access to their complete texts.

## Each reference

| Key | Correct object and final disposition | Primary destination |
|---|---|---|
| `fips205` | NIST, FIPS 205, 2024. DOI retained. The construction's interface comparison now cites Sections 10.2, 10.3, and 11.2; public-key size cites Section 9.1 and Table 2. | [NIST standard](https://csrc.nist.gov/pubs/fips/205/final) |
| `kn` | Mikhail Kudinov and Jonas Nick, 2025/2203. Identified as a preprint; Sections 5 and 13 match the retained original revision. It motivates component choices, not conformance of our reconstruction or third-party code. | [Original ePrint record](https://eprint.iacr.org/2025/2203) |
| `sphincsc` | Published IEEE S&P 2023 version, pp. 1435–1453, DOI 10.1109/SP46215.2023.10179381. Published author order is **Andreas Hülsing, Mikhail Kudinov, Eyal Ronen, Eylon Yogev**; the preprint had a different order. The entry uses the published order and retains ePrint 2022/778 as preprint provenance. | [Publication DOI](https://doi.org/10.1109/SP46215.2023.10179381), [preprint](https://eprint.iacr.org/2022/778) |
| `gravity` | Published CT-RSA 2018 version, edited by Nigel P. Smart, LNCS 10808, pp. 219–242, Springer, Cham. DOI moved into its proper field; preprint 2017/933 and January 2018 revision remain identified. Caching claims match the authors' description. | [Publisher chapter](https://link.springer.com/chapter/10.1007/978-3-319-76953-0_12) |
| `variable` | Qin, Sun, and Zheng, ePrint 2025/2236, revised 6 September 2026. Retained the cited preprint and revision date; did not manufacture future proceedings metadata or a DOI. Supports variable heights and chain lengths, not LULA I's missing reduction. | [Version/history record](https://eprint.iacr.org/2025/2236) |
| `sphincs` | Published ACM CCS 2019 version, pp. 2129–2146, DOI 10.1145/3319535.3363229. Full-version ePrint provenance retained. FORS/hypertree claims supported. | [Publication DOI](https://doi.org/10.1145/3319535.3363229), [full version](https://eprint.iacr.org/2019/1086) |
| `xmss` | RFC 8391, May 2018, Informational. Corrected the author's full name to **Stefan-Lukas Gazdag**, preserved official eXtended capitalization, and used the canonical RFC info URL. The state-reuse citation now names Sections 4.1 and 4.1.9. | [RFC Editor](https://www.rfc-editor.org/info/rfc8391/) |
| `reset` | Ristenpart and Yilek, NDSS 2010. Correct title and authors; no guessed DOI or proceedings pages. The final URL is the conference-hosted full paper, whose first-page title and authors were checked. This shorter valid URL also avoids a bibliography overflow. | [Conference-hosted paper](https://www.ndss-symposium.org/wp-content/uploads/2017/09/rist.pdf) |
| `openssl` | Exact EVP_SIGNATURE-SLH-DSA manual for OpenSSL 3.5. Explicitly distinguishes the documentation access date, 12 October 2026, from feature introduction in 2025 and the measured runtime 3.5.7. The manual supports API semantics, not the identity of the measured DLL. | [Versioned manual](https://docs.openssl.org/3.5/man7/EVP_SIGNATURE-SLH-DSA/) |
| `shrincsc` | Blockstream Research experimental C repository; exact commit 345b0a64ce8d00c16c35952375dea6d13ec48c85 exists, dated 19 May 2026. Critical constants match the measured checkout after line-ending normalization. Replaced ambiguous “the author's” attribution with “the upstream” implementation. | [Pinned source tree](https://github.com/BlockstreamResearch/shrincs-c/tree/345b0a64ce8d00c16c35952375dea6d13ec48c85) |
| `shrincsdraft` | Six named authors/handles, status Draft, pinned commit a5891ec5b360a732c097e1d6af1ae59515a2560a, dated 27 September 2026. It remains a specification, not a numbered accepted BIP or a peer-reviewed paper. Its sizes remain distinct from the earlier measured C code. | [Pinned specification](https://github.com/SHRINCS/shrincs-bip/blob/a5891ec5b360a732c097e1d6af1ae59515a2560a/SHRINCS.md) |
| `hashsiggo` | **Added.** Verified repository account andrepatta, exact commit da711b11f03c4af0d610996f89848e9e15770b73, dated 20 April 2026. This is the source of the two measured Go adapters; tracked critical files match upstream after line-ending normalization. Cited at both adapter identifications and for smallest-valid-counter selection. No legal personal name or conformance claim was invented. | [Pinned third-party code](https://github.com/andrepatta/hashsig/tree/da711b11f03c4af0d610996f89848e9e15770b73) |

## Coverage and scientific boundaries

The added software citation fixes a material provenance gap. The related-work acknowledgement records that smallest-counter selection appears in recovered code, without claiming chronological priority or borrowing a rollback theorem. The comparison generator carries the same source citations and corrected attribution as its generated TeX, so regeneration retains them.

No further material missing reference was established for the current claims. Adding unrelated foundational, AI-writing, or security papers would not supply the open reference-signer bound. Existing citations support the narrow component, historical, standard, and API statements attached to them. Own measurements and proofs retain their local evidence and explicit hypotheses.

Some complete papers were unavailable from their online PDF endpoints. The coverage reviewer inspected the retained Kudinov–Nick revision and accessible primary abstracts for the narrow claims attached to the other affected works. Publication metadata was checked independently. This is a bibliography and claim-attribution audit, not an independent certification of every external security proof or an upgrade of LULA I's security status.

## Verification and evidence

- `editorial/bibliography-r8/agents/ENTRY_REVIEW.md`: individual primary-source metadata review for all 11 original entries.
- `editorial/bibliography-r8/agents/FINAL_ENTRY_CHECK.md`: independent check of all 12 emitted entries before final capitalization repairs.
- `editorial/bibliography-r8/agents/CITATION_COVERAGE.md`: all 17 original citation sites, support, missing sources, and access limits. Its line numbers refer to the frozen baseline.
- `editorial/bibliography-r8/agents/URL_REPOSITORY_REVIEW.md` and `URL_CHECKS.json`: timestamped redirects, source identity, exact commit existence, and selected source-file correspondence.
- `editorial/bibliography-r8/ADDED_URL_CHECKS.json` and `RESET_PDF_CHECK.json`: native checks of the new/canonical destinations and the final NDSS PDF.
- `editorial/bibliography-r8/VALIDATION.json`: exact closure of citations and PDF links, source/PDF identity, unchanged mathematical environments, abstract and replay results.
- `editorial/bibliography-r8/CHANGELOG.json`: metadata, citation, URL, capitalization, and layout corrections.

The final build has 34 A4 pages, no unresolved references, no overfull boxes, and no Type 3 fonts. All rendered pages were inspected; the two pages changed by final cosmetic/layout repairs were reinspected. The final appendix no longer starts after a forced break that left the preceding page almost empty. No venue class, font metrics, equations, proofs, algorithms, parameter values, measured table contents, or campaign files were changed.

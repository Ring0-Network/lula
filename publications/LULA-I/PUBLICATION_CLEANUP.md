# Manuscript cleanup: scientific article and extended record

The author requested removal of execution-log material from the paper. The revised manuscript has 25 pages, a 106-word abstract, seven principal tables and one experimental distribution figure. The two construction diagrams remain. The final naming note retains the label **Note:**.

## Editorial changes

Three measurement sections were consolidated into one Experimental evaluation. Its Methods subsection gives the hardware, actual implementation differences, message processing, sample counts, timing/statistical conventions and workload limitations needed to interpret the measurements. Principal prepared, recovery and auxiliary results occupy three compact tables. The analytical table retains the three LULA I query-reference points; the full scenario grid moves to the extended record.

The paper no longer contains Evidence cutoff, the operational cutoff timestamp, controller/completion inventories, binary digest lists, gate/sampler record counts, the historical execution-context table, detailed replay ledgers or the claim-to-falsifier appendix. Full distributions, historical tables and execution records are preserved in `release/docs/research/extended-evaluation/` and the existing data/docs directories. Nothing was replaced with invented measurements.

This separation follows the function of a scientific article: explain the construction and give interpretable results, with detailed reproduction material accompanying it. As a primary style example, [SPHINCS+C, Section VII](https://pure.tue.nl/ws/portalfiles/portal/346840479/SPHINCSC_Compressing_SPHINCS_With_Almost_No_Cost.pdf) describes its hardware and measurement procedure before performance tables. Its numerical results are not evidence for LULA I.

## Verification

- Main and contact-free repository PDFs compile to 25 pages without unresolved references, changed-label requests or overfull boxes; embedded fonts are vector fonts.
- Original-to-current body comparisons preserve five algorithms, two lemmas, one theorem, three proofs, five equation environments, two align environments and two construction diagrams exactly.
- The saved-data table checker passes separately for seven current tables (43 listed rows or fields) and 21 archived tables (141 listed rows or fields). The archive is explicitly identified as the preceding detailed presentation.
- All main PDF pages were visually reviewed; the changed experimental pages were also inspected at full-page resolution. Operational markers are absent from the current inputs and extracted PDF text.
- Package digests, frozen-data preservation and ZIP integrity are recorded in `editorial/publication-cleanup-20261012/DELIVERY.json`. Build and scope checks are in the same directory.

## Scientific scope retained

The intended 2^40-query objective is conditional. The 143.3, 132.6 and 125.9 figures at 2^38, 2^40 and 2^41 concern the FORS+C component only. The full reference-signer bound remains open; the rollback theorem transfers an applicable reference bound under its honest-cache and completed-call conditions. No forgery was run against real SHRINCS. The two unstable SHA2-128s verification cells and three individual cache-loss observations remain explicit. No common-security ranking is claimed.

The local bundle has not been deposited publicly. Funding/interests and historical timed-binary correspondence remain factual inputs. Earlier editorial/release archives are frozen records of their preceding versions. No benchmark or expensive cache rebuild was launched for this cleanup.

# Release decisions and exclusions

The author authorized Apache-2.0 for our code and CC BY 4.0 for our text, figures and data, and delegated the remaining packaging choices. Third-party grants apply only to their respective material.

- No derived cache fixture or serialized private-key file is distributed. Public keys and saved signature vectors remain; deterministic fixture recipes use public test bytes 49 and 82.
- Operational secrets, installed toolchains, benchmark binaries, OS caches, backups and build scratch are excluded. Recomputed outputs are generated separately.
- SHRINCS C source bodies, copied headers and the derived full KN configuration are excluded because no redistribution license was verified at the pinned revision. Owned C wrappers and the numerical parameter delta remain. The bundle alone cannot rebuild those C/KN executables.
- Full Go, OpenSSL, SHRINCS BIP and Kudinov–Nick sources/texts are not bundled. Only owned Go driver additions and their addition-only patch are shipped; the linked MIT notice is retained. No modified upstream library file was found for that driver.
- Six archival first-campaign plots are excluded: some used private construction naming, incorrect recovery aggregation, withdrawn measurements or unsupported Pareto/cache-line interpretation. The three current audited manuscript figures and their saved-data regeneration script are included.
- Host paths and private names were converted to relative public paths. Setup seed fields were removed. Numeric observations, UTC values and public signature bytes were preserved. Exact original/revised hashes and every substitution are retained in the separate private handback, not this public folder.
- The repository paper omits the contact email; the main manuscript retains the author-requested contact. Research text, assumptions and results agree.

History has seven surviving aggregate-source rows rather than per-call samples. OpenSSL's measured historical runtime DLL digest and historical timed-binary/source correspondence remain unbound. License/source hashes do not close those provenance gaps. No real SHRINCS forgery or new full security reduction is claimed.

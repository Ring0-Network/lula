# Command receipts

1. Read selected release-source slices with PowerShell `Get-Content -Encoding UTF8` before reading any quantum author reports.
2. Browse the official ePrint2022/346 landing page successfully; live PDF request returned403. Locate the cached primary PDF without reading author derivations. Confirm PDF SHA-256 with `Get-FileHash -Algorithm SHA256` and extract physical page23 using `pypdf.PdfReader(...).pages[22].extract_text()`. Exit code0. The extracted page includes Definition9 and Theorem4.
3. Save `INDEPENDENT_DERIVATION.md`; only afterward read author `DERIVATION.md`, `CHECKS.json` and `control.py`.
4. Copy author `control.py` byte-for-byte into this directory as `reviewed_control.py`, using native PowerShell `Copy-Item -LiteralPath`. Execute `python -I -B reviewed_control.py`. Exit code0. It writes the local `CHECKS.json`; the author lane remains untouched.
5. Measure author derivation/control hashes via `Get-FileHash -Algorithm SHA256`, matching the identities in `SECOND_READER.md`.
6. Recheck the author/source identities and create/verify a SHA-256 manifest of this reviewer directory, excluding the manifest itself.

No dependency installation, large benchmark, proof assistant run, remote private-source upload or manuscript change occurred. The script is the reviewed author's control, not a second independently authored implementation; the independent general algebra and source count were saved first.

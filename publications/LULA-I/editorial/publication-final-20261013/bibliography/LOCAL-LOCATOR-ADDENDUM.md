# Local primary locator addendum

**CLOSED — Fluhrer/Dang Section5, Equation(1) locator verified from a genuine local primary PDF.** This separately pinned successor resolves the narrow locator limitation in BIBLIOGRAPHY-URL-AUDIT.md. The original report and receipt remain byte-identical; this addendum does not amend them or any manuscript/bibliography source.

The genuine authority is `R8/R8B-immutable-authority/refs/eprint-2024-018.pdf`, SHA256 `5326a5144c0628ab82d9e036689b0269402b6976ab01798a8241b3032e245bc6`,701594 bytes,40 PDF pages. It begins with a valid PDF signature. Its cover reads Smaller Sphincs+ with subtitle “or, Honey, I Shrunk the Signatures”, authors Scott Fluhrer then Quynh Dang, and date14January2025. PDF metadata records creation/modification14January2025. The archive's official landing metadata checked in the parent report gives original year2024 and last revision16January2025. A PDF's internal author date need not equal its archive revision date; remote PDF byte equality was not established, so no such equality is claimed. Existing year2024/archive2024/018/revised16January2025 provenance matches the official archive metadata.

Section5, “Sphincs+ Usage Limitations”, starts on printed/PDF page5. Equation(1) is on printed/PDF page6 and was checked both by fitz extraction and direct rendered-page inspection. It is

    p = sum[g=0..2^m] (lambda^g exp(-lambda)/g!)
                       * (1-(1-t^-1)^g)^k,
    lambda = 2^(m-h).

The source models the number of signatures at the target FORS instance by a Poisson approximation, then covers all k target sets. Thus the exact current operating-model.tex4 citation `[Section5, Equation(1)]{fluhrer}` points to the intended occupancy/coverage analysis. No locator or citation-text repair is required.

LULA's displayed calculation is an explicitly identified adaptation:17 real trees, a nine-bit zero filter and an exact Binomial moment with a separate Poisson approximation. It is not asserted to be the literal standard-SPHINCS formula. More importantly, source footnotes2/3 on page6 justify independent selections using randomized signing R. LULA's signer is deterministic. The current manuscript already states its independent-uniform selection assumptions and says that its model calculation does not establish the deterministic signer's selection distribution, adaptive forged randomizer/counter control or a complete reference bound. Those limitations remain essential. This locator check does not transfer a hardness/security theorem.

The other named cache is NOT another primary PDF: `H-hash/H5-combinatorial-compression/refs/smaller_sphincs_2024-018/2024-018.pdf`, SHA256 `949d73f38570adab4d5afc61d3ba94f056c30c9792ff94ea0c9d96f580c360b7`,5442 bytes, begins with HTML and the title “Just a moment...”. Its accompanying filename is `2024-018.pdf.txt`, not `pdf.txt`, and contains only a JavaScript/cookie challenge stub. It supplies no paper version or locator evidence and was not used scientifically. No archive/source file was changed to correct that historical cache.

The R8 authority closes the requested remaining anchor. No new bibliography entry, title/year modification, source/code/TeX change, PDF redistribution, upload or external submission is needed. Extracted/rendered views were used locally for this editorial inspection only; the original primary PDF was not copied into the release. The mechanism-paper bibliography/locator verdict is now PASS, separate from public repository availability and the original security-category frontier.

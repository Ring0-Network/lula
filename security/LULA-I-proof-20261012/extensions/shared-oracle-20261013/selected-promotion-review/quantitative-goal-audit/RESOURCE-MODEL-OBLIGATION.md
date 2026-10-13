# Required query-to-resource comparison

This follows the saved independent first; no new target-only/activation peer proof was read. RESOURCE-RATIOS.json computes required ratios, not actual evaluation costs.

For reference full-search units2^128 classical and2^64 quantum, let Q_star be the largest query budget where the currently reviewed source envelope proves success<=1/2. The deficit log2(Q_reference/Q_star) is a *comparison gap of sufficient bounds*. It is not a proven loss in actual security. In an additive black-box resource model, a lower resource cost per complete hash of at least(Q_reference/Q_star) times the chosen per-reference-test unit would suffice to translate that particular query certificate. Such a lower cost is not established here.

| log2 q | Classical gap | Required classical ratio | Quantum gap | Required quantum ratio |
|---:|---:|---:|---:|---:|
|38|3.584968618|12.000050880|3.576663463|11.931168706|
|40|3.595096266|12.084587017|3.583624567|11.988876537|
|41|4.361709581|20.559162364|4.001496043|16.016600249|

Success normalization must be aligned. In the ideal unique-target toy benchmark, uniform classical key search succeeds with probability1/2 afterN/2 distinct tests, while serial Grover reaches1/2 at approximately(pi/8)*sqrtN ideal oracle iterations. If those *same-success toy* benchmarks are chosen instead, the required ratios become respectively:

| log2 q | Classical ratio for half success | Quantum ratio for half success |
|---:|---:|---:|
|38|6.000025440|4.685358994|
|40|6.042293509|4.708020807|
|41|10.279581182|6.289704210|

The Grover coefficients are asymptotic ideal-query comparisons, not AES circuit estimates. Neither table accounts for depth-limited parallel search, memory, gate synthesis or AES/SHA implementation. The table requested against2^128/2^64 and the success-normalized table answer different comparisons; neither may be passed off as official category1 certification.

## Official primary criterion and its limits

Fresh official source: [NIST evaluation criteria, sections4.A.4–5](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post-Quantum-Cryptography-Standardization/Evaluation-Criteria/Security-%28Evaluation-Criteria%29), read2026-10-13, page update2026-08-05. Cached HTML is nist-security-criteria.html SHA256 a438baa9294a48508cb67632caa941b3339dae81ff9a3ab293b6079c69075edd. Category1 uses AES128 key-search resources, including multiple relevant metrics. Chosen-message signing queries are classical private-key queries, not the adversarial hash-search budget.

The page's preliminary gate guidance gives AES128 about2^143 classical gates, or2^170/MAXDEPTH quantum gates, and discusses depth40,64 and96. These are its published reference estimates, not fresh measurements, formal lower bounds on every AES adversary, or exact LULA resource units. If one used that stated classical gate benchmark literally with q40 Q_star, the corresponding sufficient-model ratio would require roughly2^(143-124.4049)=2^18.5951 gates of *proved lower resource charge* per raw hash. A known implementation of SHA with a given gate count supplies an implementation upper bound, not that arbitrary-attacker lower bound. The quantum page formula cannot be converted by the2^64 query table alone: its MAXDEPTH and parallel circuit-size dependence must be retained.

## Smallest missing cost-model theorem

Fix a success ceiling rho, relevant resource metrics, an AES reference resource R_AES(rho,D), the exact signing-query convention and source q. A sufficient bridge would prove for EVERY permitted actual fixed-hash attack A, not only a known circuit implementation, a faithful black-box source adversary B with:

1. Adv_fixed(A) <= epsilon_source(q,Q(B)) + Delta_inst;
2. Q(B) <= floor(G(A)/c_hash), while preserving the actual classical/coherent interface, prequeries, memory and any depth restrictions;
3. G(A)<R_AES implies epsilon_source(q,Q(B))+Delta_inst<=rho.

Here c_hash must be a justified lower resource charge or an explicitly assumed attack-model charge; Delta_inst must quantify the model-to-fixed-hash/nonblack-box gap. If the certificate uses the endpoint at exactlyrho, no positive gap can be silently added; reserve a probability margin by evaluating a smaller Q budget. Depth and width require an additional lawful resource translation rather than merely multiplying raw query counts by the size of one reversible SHA circuit.

No such arbitrary-attack bridge, actual fixed-SHA gap certificate or depth-sensitive resource relation is currently proved. Direct RO theorems bound random-function source games; their preservation across honest caches is established, but they do not establish this fixed-hash/category bridge. Conversely a proposed optimized AES/SHA circuit can inform cryptanalytic estimates without proving a universal lower bound. Formal category claims and practical conditional estimates must be distinguished.

The next useful scientific work is to state and justify the admissible model/resource assumptions, evaluate the exact component advantages at their real reduction resources, and test whether the residual probability budget is positive. If a direct source-model bound is tighter than the lawful generic lifted envelope, use that fact explicitly. Then assess parameter repair under that chosen criterion. Producing another hash manifest or a known-circuit gate count alone does not close this implication.

# Counter-policy specialization, construction parameters and ordinary-game scope

**PROVED / CITED / OPEN — clarification of the frozen own derivation.** INDEPENDENT-DERIVATION.md SHA74e2106c6c18733d03864f844817d9685db07a867972721aec485bfc9ed04e57 is preserved unchanged. The following precision prevents an overly broad interpretation of its counter-policy separation.

## Canonical selection is permitted; universal policy equivalence is unnecessary

DefinitionC.1 of SPHINCS+C requires an accepted output/counter and does not rule out choosing the FIRST accepted counter. Therefore canonical-first selection is a permitted policy, and one can explicitly specialize the property to that policy. The abstract success1/success0 countermodel refutes interchangeability of all valid accepted-counter policies; it does NOT prove that adopting the canonical policy as a chosen primitive definition is impossible. A source-specific reduction need not establish equivalence to every possible policy.

The actionable choice is to state the exact oracle used by the security hypothesis: first literal BE32 counter, finite2^32 domain, full same-function correlations and bottom/nonwinning failure semantics. The conditional wrapper then refers to that chosen canonical-first property. If the cited published game's oracle is instantiated identically, the counter-policy step is definitional specialization; otherwise an explicit refinement or bounded extension is needed. No unspecified-policy hardness assertion alone licenses a bound for a different policy.

## The r=security-parameter statement is a construction choice

The r-bit space with r equal to the security parameter is in Section5.1's particular WOTS+C construction/Algorithm5. It is not an explicit mandatory r constraint in the formal wording of DefinitionC.1. Thus the derivation must not infer that the formal special-TCR notion forbids a32-bit counter. An actual source-compatible instance can define the160-bit Th member on C128||counter32 and its chosen acceptance predicate.

The remaining precision is still real: literal C16||BE32(c) is not C16||BE128(c), and finite bottom is not silently normalized away. One may adopt the source-compatible counter width/policy as the definition; one must separately check that any quantitative theorem cited for a particular published instantiation applies to that definition. In particular, the source's unconditioned failed-row mass must stay present. The reference construction's large-counter existence convention does not justify deleting it.

## Collection access resolves the child-before-key issue

Definition7 in Hülsing–Kudinov explicitly allows classical other-tweak collection queries under the hidden parameter. All genuine child computations use types0–4, disjoint from the target type7 tweak. This permits C registration without revealing P to the reduction beforehand. Parameter release may precede the reduction's source-adversary pre-key phase, provided P is still withheld from that adversary and all raw replies use the correct same public hash implementation. This is a source-specific wrapper under the chosen collection property; it is not an independence theorem for keyed rows.

The two fixed predicates Prop4 and Prop8 still require two chosen primitive instances or a separately declared tweak-dependent-predicate game. Known full public hash implementation access in the standard model still differs from opaque prefix-only oracle access in a black-box QROM. The existing fresh-row RO-relative theorem and fixed-SHA keyed wrapper are distinct experiments. The exact quantitative bounds/time/query budget of the latter remain to be justified.

## Primary files and anchors

- HK22 PDF: C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/M-measure/M2-sphincs-reparam/refs/eprint_2022_346_hulsing_kudinov_tight.pdf; text same basename with.txt. Definitions2/7 and collection explanation are text lines177–189/241–268. PDF SHA80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3.
- SPHINCS+C PDF: C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/R2/R2B-joint-constraints/refs/sphincsplusc_2022_778/2022-778.pdf; text same basename with.txt. DefinitionC.1 is text lines1556–1571, visually checked at printed page30; Section5.1/Algorithm5 is lines712–737. PDF SHA1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215.
- The previously rendered primary C.1 image is C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/selected-primitive-definitions/def-c1.png.

**OPEN — status unchanged.** The own conditional wrapper and abstract countermodels are not yet independently accepted conventional security results. No source attack, actual SHA hardness proof, capacity/category claim, core-document change or new checked declaration is supplied by this clarification.

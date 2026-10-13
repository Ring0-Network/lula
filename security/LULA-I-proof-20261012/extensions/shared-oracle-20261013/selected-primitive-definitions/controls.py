"""Small exhaustive mathematical interface controls; no signature construction."""
from itertools import product
from fractions import Fraction
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    n, cap = 4, 3
    accepted = {0, 1}
    rows = list(product(range(n), repeat=cap))
    success = [r for r in rows if any(y in accepted for y in r)]
    expected_success = 1 - (1 - Fraction(len(accepted), n)) ** cap
    assert Fraction(len(success), len(rows)) == expected_success
    residual_eligible = residual_hit = counter_only_examples = 0
    canonical_by_counter = [0] * cap
    for row in success:
        j = next(i for i, y in enumerate(row) if y in accepted)
        canonical_by_counter[j] += 1
        for c in range(j):
            assert row[c] != row[j]
        if j < cap - 1:
            residual_eligible += 1
            if row[-1] == row[j]:
                residual_hit += 1
                counter_only_examples += 1
    assert Fraction(residual_hit, residual_eligible) == Fraction(1, n)
    assert counter_only_examples > 0
    for j in range(cap):
        prob = (1-Fraction(len(accepted), n))**j * Fraction(len(accepted), n)
        assert Fraction(canonical_by_counter[j], len(rows)) == prob

    # Change-of-measure is checked for all Boolean winning predicates and
    # all target distributions with denominator four over four inputs.
    density_checks = 0
    for weights in product(range(5), repeat=n):
        if sum(weights) != 4:
            continue
        rho = [Fraction(w, 4) for w in weights]
        alpha = max(rho) * n
        for mask in product((0, 1), repeat=n):
            selected = sum((p*b for p,b in zip(rho,mask)), Fraction())
            uniform = Fraction(sum(mask), n)
            assert selected <= alpha * uniform
            density_checks += 1
    report = {
        'status': 'COMPUTED / mathematical controls only',
        'source_binding': 'No source-to-primitive reduction established by these controls',
        'ordinary_rows': len(rows),
        'successful_rows': len(success),
        'success_fraction': str(expected_success),
        'residual_eligible': residual_eligible,
        'residual_hits': residual_hit,
        'residual_hit_fraction': str(Fraction(residual_hit,residual_eligible)),
        'counter_only_full_event_examples_excluded_by_base_message_game': counter_only_examples,
        'canonical_counts_by_counter': canonical_by_counter,
        'density_domination_checks': density_checks,
        'script_sha256': sha(Path(__file__).resolve()),
        'derivation_sha256': sha(HERE / 'INDEPENDENT_DERIVATION.md'),
        'primary_346_sha256': '80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3',
        'primary_778_sha256': '1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215',
        'primary_2203_sha256': '3c58f81a6a0b7e8e040134be1a0013b3977edefdc889e1636d4dfe79cf0e225e',
    }
    (HERE / 'CONTROL-RESULTS.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

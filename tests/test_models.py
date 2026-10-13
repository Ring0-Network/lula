"""Portable numerical regression and independent finite-probability checks."""
from pathlib import Path
from fractions import Fraction
from math import comb
import json
import sys
import unittest
import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from models import (BASELINE, Parameters, coverage_probability, coverage_upper,
                    positive_coverage_interval, classical_joint,
                    uniform_classical, uniform_classical_certificate, fixed_qrom_poly)
from models.parameters import N, QUERY_GRID


def exact_small_coverage(q, height, a, real):
    """Independent enumeration of the finite Binomial distribution."""
    rho = Fraction(1, 1 << height)
    beta = Fraction((1 << a)-1, 1 << a)
    return sum((comb(q, count)*rho**count*(1-rho)**(q-count)*
                (1-beta**count)**real/(1 << a) for count in range(q+1)), Fraction(0))


class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads((Path(__file__).parent/'fixtures/model_bounds.json').read_text(encoding='utf8'))

    def assertProbabilityClose(self, actual, expected, tolerance='1e-75'):
        with mp.workdps(260):
            expected = mp.mpf(expected)
            self.assertLessEqual(abs(actual-expected), mp.mpf(tolerance)*abs(expected)+mp.mpf('1e-240'))

    def test_query_grid_and_baseline_call_counts(self):
        self.assertEqual(tuple(self.fixture['q_exponents']), QUERY_GRID)
        self.assertEqual((BASELINE.hidden_final_calls, BASELINE.graph_final_calls,
                          BASELINE.classical_constant), (3017, 3217, 6242))
        self.assertEqual((BASELINE.signature_bytes, BASELINE.single_top_cache_bytes),
                         (5720, 75497456))
        self.assertEqual(BASELINE.classical_constant-
                         (BASELINE.hidden_final_calls+BASELINE.graph_final_calls+BASELINE.layers+2), 1)

    def test_fors_all_eight_rows_and_positive_second_method(self):
        self.assertEqual(len(self.fixture['fors']), 8)
        for row in self.fixture['fors']:
            q = 1 << row['q_exponent']
            with self.subTest(q=q), mp.workdps(260):
                value = coverage_probability(q)
                self.assertProbabilityClose(value, row['probability'])
                lower, upper = positive_coverage_interval(q)
                self.assertLessEqual(lower, value)
                self.assertLessEqual(value, upper)
                self.assertGreater(value, 0)
                self.assertLessEqual(value, mp.mpf(1)/512)

    def test_moment_and_touchard_against_exact_small_binomial(self):
        for height in (0, 1, 3):
            for a in (1, 2):
                for real in (1, 2, 4):
                    for q in (0, 1, 2, 5, 9):
                        exact = exact_small_coverage(q, height, a, real)
                        with self.subTest(q=q, h=height, a=a, r=real), mp.workdps(260):
                            numeric = coverage_probability(q, height, a, real)
                            target = mp.mpf(exact.numerator)/exact.denominator
                            self.assertProbabilityClose(numeric, target, '1e-150')
                            self.assertLessEqual(exact, coverage_upper(q, height, a, real))
                            if q == 0:
                                self.assertEqual(numeric, 0)

    def test_classical_joint_all_accepted_rows(self):
        rows = self.fixture['classical_joint']
        self.assertEqual(len(rows), 24)
        self.assertEqual({r['q_exponent'] for r in rows}, set(QUERY_GRID))
        for row in rows:
            q, Q = 1 << row['q_exponent'], 1 << row['query_exponent']
            with self.subTest(q=q, Q=Q), mp.workdps(260):
                value = classical_joint(q, Q)
                self.assertProbabilityClose(value['total'], row['probability'])
                self.assertEqual(value['linear']*N, int(row['linear_numerator']))
                self.assertEqual(value['full256_bridge']*N*N, int(row['pair_numerator']))
                if row['query_exponent'] == 128:
                    self.assertEqual(value['total'], 1)

    def test_fixed_qrom_all_accepted_component_rows(self):
        rows = self.fixture['fixed_qrom_poly']
        self.assertEqual(len(rows), 16)
        self.assertEqual({r['q_exponent'] for r in rows}, set(QUERY_GRID))
        for row in rows:
            q, Q = 1 << row['q_exponent'], 1 << row['query_exponent']
            with self.subTest(q=q, Q=Q):
                value = fixed_qrom_poly(q, Q)
                for name, expected in row['values'].items():
                    with self.subTest(term=name):
                        self.assertProbabilityClose(value[name], expected)
                if row['query_exponent'] == 64:
                    self.assertEqual(value['total'], 1)

    def test_uniform_classical_rational_certificates(self):
        case = self.fixture['uniform_classical']
        params = Parameters(**case['parameters'])
        counts = case['counts']
        self.assertEqual((params.hidden_final_calls, params.graph_final_calls,
                          params.classical_constant),
                         (counts['hidden'], counts['graph'], counts['constant']))
        self.assertEqual(params.signature_bytes, counts['signature_bytes'])
        self.assertEqual(params.single_top_cache_bytes, counts['top_cache_bytes'])
        half_passes = 0
        for row in case['rows']:
            q, Q = 1 << row['q_exponent'], 1 << row['query_exponent']
            with self.subTest(q=q, Q=Q), mp.workdps(260):
                certificate = uniform_classical_certificate(params, q, Q)
                expected = Fraction(int(row['upper_numerator']), int(row['upper_denominator']))
                self.assertEqual(certificate['uncapped'], expected)
                self.assertEqual(certificate['at_most_half'], row['at_most_half'])
                exact_numeric = uniform_classical(params, q, Q)['total']
                upper = mp.mpf(certificate['total'].numerator)/certificate['total'].denominator
                self.assertLessEqual(exact_numeric, upper+mp.mpf('1e-200'))
                if row['query_exponent'] == case['half_query_exponent']:
                    self.assertTrue(certificate['at_most_half'])
                    half_passes += 1
        self.assertEqual(half_passes, 8)

    def test_single_seed_zero_finite_counter_and_private_cap(self):
        with mp.workdps(260):
            self.assertEqual(classical_joint(0, 0)['total'], mp.mpf(6242)/N)
            value = fixed_qrom_poly(0, 0)
            remainder = value['total']-value['private_k']-value['private_p']-value['public_union']
            self.assertProbabilityClose(remainder, mp.mpf(1)/N, '1e-190')
            self.assertProbabilityClose(fixed_qrom_poly(0, 1 << 62)['private_k'], mp.mpf(1)/3)
            self.assertEqual(fixed_qrom_poly(0, 1 << 63)['private_k'], 1)
            # A large FORS height is admitted, but finite exhaustion cannot be omitted.
            large_a = Parameters(31, 1, BASELINE.heights, BASELINE.ell, BASELINE.targets)
            result = uniform_classical(large_a, 1, 0)
            self.assertGreater(result['finite_counter'], mp.mpf('0.1'))
            self.assertGreater(result['total'], mp.mpf('0.1'))

    def test_strict_targets_full_128_denominator_and_zero_height(self):
        short = Parameters(1, 1, (0, 0), (1, 1), (1, 254))
        self.assertEqual(short.acceptance_probability(0), Fraction(1, N))
        self.assertEqual(short.acceptance_probability(1), Fraction(1, N))
        self.assertNotEqual(short.acceptance_probability(0), Fraction(1, 16))
        edge = Parameters(1, 1, (0,), (1,), (254,))
        self.assertEqual(edge.classical_constant, 11)
        self.assertEqual(edge.signature_bytes, 72)
        self.assertEqual(coverage_probability(1, 0, 1, 1), mp.mpf('0.25'))
        invalid = [
            dict(a=0), dict(a=32), dict(r=95), dict(heights=(32, 5, 5, 5, 21)),
            dict(heights=(20, 20, 20, 20, 21)), dict(ell=(33, 32, 32, 32, 16)),
            dict(targets=(480, 240, 240, 240, 2040)), dict(a=31, r=3),
            dict(a=16), dict(a=True), dict(heights=1), dict(ell=(32,)),
        ]
        original = dict(a=BASELINE.a, r=BASELINE.r, heights=BASELINE.heights,
                        ell=BASELINE.ell, targets=BASELINE.targets)
        for change in invalid:
            with self.subTest(change=change), self.assertRaises(ValueError):
                Parameters(**(original | change))
        for operation in (lambda: classical_joint(-1, 0), lambda: fixed_qrom_poly(0, True),
                          lambda: coverage_probability(-1), lambda: coverage_probability(1, dps=40),
                          lambda: edge.acceptance_probability(-1)):
            with self.assertRaises(ValueError):
                operation()
        # Cached numerical values must not let bool-as-int bypass guards.
        coverage_probability(1)
        with self.assertRaises(ValueError):
            coverage_probability(True)


if __name__ == '__main__':
    unittest.main()

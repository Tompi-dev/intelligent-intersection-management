import json
from pathlib import Path
import unittest
from src.web_demo import evaluate_payload, MAX_ROWS


class DemoAPIChecks(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((Path(__file__).resolve().parents[1] / 'prototype/sample_observations.json').read_text())

    def test_fixture_api_result_matches_recorded_controller(self):
        expected = json.loads((Path(__file__).resolve().parents[1] / 'prototype/expected_output.json').read_text())
        result = evaluate_payload({'rows': self.rows})
        self.assertEqual(result['decision'], expected[-1])
        self.assertEqual(result['processed_rows'], len(expected))

    def test_missing_feed_preserves_yellow_and_all_red(self):
        rows = [{'time_s': t, 'observation': None} for t in range(26)]
        stages = [evaluate_payload({'rows': rows[:n]})['decision']['stage'] for n in (21, 24, 26)]
        self.assertEqual(stages, ['YELLOW', 'ALL_RED', 'GREEN'])

    def test_timing_configuration_reaches_real_controller(self):
        result = evaluate_payload({'rows': self.rows[:3], 'timing': {'min_green': 12}})
        self.assertEqual(result['decision']['stage'], 'GREEN')

    def test_invalid_configuration_and_malformed_envelope(self):
        for payload in ({'rows': self.rows, 'timing': {'yellow': 0}}, {'rows': self.rows, 'timing': []}, {'rows': self.rows, 'extra': 1}, [], {'rows': []}):
            with self.assertRaises((ValueError, TypeError)):
                evaluate_payload(payload)

    def test_bound_and_invalid_observation(self):
        with self.assertRaises(ValueError):
            evaluate_payload({'rows': [self.rows[0]] * (MAX_ROWS + 1)})
        bad = [{'time_s': 0, 'observation': {'timestamp_s': 1, 'queues': {'N': 1, 'S': 1, 'E': 1, 'W': 1}}}]
        with self.assertRaises(ValueError):
            evaluate_payload({'rows': bad})

    def test_runs_are_independent(self):
        evaluate_payload({'rows': self.rows})
        self.assertEqual(evaluate_payload({'rows': self.rows[:1]})['decision']['time_s'], 0)

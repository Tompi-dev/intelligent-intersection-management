import random
import unittest
from src.controller import Controller, Timing, replay

def obs(t, n=0, s=0, e=20, w=20):
    return {'timestamp_s': t, 'queues': {'N': n, 'S': s, 'E': e, 'W': w}}

class ControllerChecks(unittest.TestCase):
    def test_minimum_green_and_clearance(self):
        c=Controller()
        self.assertEqual(c.tick(9,obs(9))['stage'],'GREEN')
        self.assertEqual(c.tick(10,obs(10))['stage'],'YELLOW')
        self.assertEqual(c.tick(12,obs(12))['stage'],'YELLOW')
        self.assertEqual(c.tick(13,obs(13))['stage'],'ALL_RED')
        self.assertIsNone(c.tick(14,obs(14))['group'])
        self.assertEqual(c.tick(15,obs(15))['group'],'EW')
    def test_late_call_does_not_skip_clearance(self):
        c=Controller();c.tick(10,obs(10))
        self.assertEqual(c.tick(100,obs(100))['stage'],'ALL_RED')
        self.assertEqual(c.tick(101,obs(101))['stage'],'ALL_RED')
        self.assertEqual(c.tick(102,obs(102))['stage'],'GREEN')
    def test_max_green_forces_opposing_service(self):
        c=Controller()
        r=c.tick(45,obs(45,n=100,e=0,w=0))
        self.assertEqual((r['stage'],r['reason']),('YELLOW','maximum_green'))
    def test_hysteresis_prevents_chatter(self):
        c=Controller()
        self.assertEqual(c.tick(10,obs(10,n=10,e=12,w=0))['stage'],'GREEN')
    def test_stale_fallback(self):
        c=Controller();r=c.tick(20,obs(0))
        self.assertEqual((r['mode'],r['stage']),('FIXED_FALLBACK','YELLOW'))
    def test_freshness_boundary(self):
        c=Controller();self.assertEqual(c.tick(2,obs(0))['mode'],'ADAPTIVE')
        self.assertEqual(c.tick(3,obs(0))['mode'],'FIXED_FALLBACK')
    def test_missing_observation_fallback(self):
        c=Controller();self.assertEqual(c.tick(20,None)['stage'],'YELLOW')
    def test_invalid_input_is_atomic(self):
        c=Controller();before=vars(c).copy()
        with self.assertRaises(ValueError):c.tick(10,obs(10,n=-1))
        self.assertEqual(vars(c),before)
    def test_future_and_decreasing_timestamps(self):
        c=Controller()
        with self.assertRaises(ValueError):c.tick(1,obs(2))
        c.tick(2,obs(2))
        with self.assertRaises(ValueError):c.tick(3,obs(1))
        with self.assertRaises(ValueError):c.tick(1,obs(1))
    def test_missing_arm_and_bad_counts(self):
        for bad in [float('nan'),float('inf'),-1,True,2.5,'4']:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):Controller().tick(0,obs(0,n=bad))
        o=obs(0);del o['queues']['W']
        with self.assertRaises(ValueError):Controller().tick(0,o)
    def test_invalid_timing(self):
        for values in [{'yellow':0},{'all_red':-1},{'fixed_green':2},{'min_green':46},{'max_green':float('nan')},{'hysteresis':True}]:
            with self.subTest(values=values):
                with self.assertRaises(ValueError):Timing(**values)
    def test_random_demand_preserves_transition_invariants(self):
        c=Controller();rng=random.Random(42);previous=None;since=0
        for t in range(2000):
            r=c.tick(t,obs(t,*(rng.randrange(50) for _ in range(4))))
            stage=(r['stage'],r['group'])
            self.assertIn(stage,[('GREEN','NS'),('GREEN','EW'),('YELLOW','NS'),('YELLOW','EW'),('ALL_RED',None)])
            if previous and stage!=previous:
                if previous[0]=='GREEN':
                    self.assertEqual(stage,('YELLOW',previous[1]));self.assertGreaterEqual(t-since,10);self.assertLessEqual(t-since,45)
                elif previous[0]=='YELLOW':
                    self.assertEqual(stage,('ALL_RED',None));self.assertGreaterEqual(t-since,3)
                else:
                    self.assertEqual(stage[0],'GREEN');self.assertGreaterEqual(t-since,2)
                since=t
            previous=stage
    def test_replay_determinism(self):
        rows=[{'time_s':t,'observation':obs(t)} for t in range(60)]
        self.assertEqual(replay(rows),replay(rows))
    def test_empty_replay_rejected(self):
        with self.assertRaises(ValueError):replay([])

if __name__=='__main__':unittest.main()

"""Research-only two-phase signal prototype using precomputed queue observations.

This module does not perform CV, traffic simulation, or roadside control.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
import json
import math
from pathlib import Path

ARMS = {'N', 'S', 'E', 'W'}

def finite(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite number')
    return float(value)

@dataclass(frozen=True)
class Timing:
    min_green: float = 10
    max_green: float = 45
    yellow: float = 3
    all_red: float = 2
    fixed_green: float = 20
    stale_after: float = 2
    hysteresis: int = 2

    def __post_init__(self):
        for key in ('min_green', 'max_green', 'yellow', 'all_red', 'fixed_green', 'stale_after'):
            if finite(getattr(self, key), key) <= 0:
                raise ValueError(f'{key} must be positive')
        if not self.min_green <= self.fixed_green <= self.max_green:
            raise ValueError('min_green <= fixed_green <= max_green is required')
        if isinstance(self.hysteresis, bool) or not isinstance(self.hysteresis, int) or self.hysteresis < 0:
            raise ValueError('hysteresis must be a nonnegative integer')

class Controller:
    def __init__(self, timing=None):
        self.timing = timing or Timing()
        self.group = 'NS'
        self.stage = 'GREEN'
        self.stage_since = 0.0
        self.last_now = -1.0
        self.last_observed = -1.0

    def tick(self, now, observation):
        """Advance at most one stage; elapsed calls never skip physical clearance."""
        now = finite(now, 'time_s')
        if now < 0 or now < self.last_now:
            raise ValueError('time_s must be nonnegative and monotonic')
        queues = None
        observed = None
        mode, reason = 'FIXED_FALLBACK', 'missing_observation'
        if observation is not None:
            if not isinstance(observation, dict):
                raise ValueError('observation must be an object or null')
            observed = finite(observation.get('timestamp_s'), 'timestamp_s')
            if observed < 0 or observed > now or observed < self.last_observed:
                raise ValueError('observation timestamp is negative, future or decreasing')
            queues = observation.get('queues')
            if not isinstance(queues, dict) or set(queues) != ARMS:
                raise ValueError('queues must have exactly N, S, E, W')
            if any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in queues.values()):
                raise ValueError('queue counts must be nonnegative integers')
            if now - observed <= self.timing.stale_after:
                mode, reason = 'ADAPTIVE', 'hold'
            else:
                reason = 'stale_observation'
        # Commit input state only after the complete observation validates.
        self.last_now = now
        if observed is not None:
            self.last_observed = observed
        age = now - observed if observed is not None else None
        elapsed = now - self.stage_since
        t = self.timing
        if self.stage == 'YELLOW':
            if elapsed >= t.yellow:
                self.stage, self.stage_since = 'ALL_RED', now
                reason = 'yellow_complete'
            else:
                reason = 'yellow_clearance'
        elif self.stage == 'ALL_RED':
            if elapsed >= t.all_red:
                self.group = 'EW' if self.group == 'NS' else 'NS'
                self.stage, self.stage_since = 'GREEN', now
                reason = 'all_red_complete'
            else:
                reason = 'all_red_clearance'
        elif elapsed < t.min_green:
            reason = 'minimum_green'
        else:
            switch = False
            if elapsed >= t.max_green:
                switch, reason = True, 'maximum_green'
            elif mode == 'FIXED_FALLBACK':
                switch = elapsed >= t.fixed_green
                reason = 'fallback_cycle' if switch else reason
            else:
                ns, ew = queues['N'] + queues['S'], queues['E'] + queues['W']
                current, other = (ns, ew) if self.group == 'NS' else (ew, ns)
                switch = other > current + t.hysteresis
                reason = 'higher_opposing_queue' if switch else 'hold'
            if switch:
                self.stage, self.stage_since = 'YELLOW', now
        return {'time_s': now, 'stage': self.stage,
                'group': None if self.stage == 'ALL_RED' else self.group,
                'mode': mode, 'observation_age_s': age, 'reason': reason}

def replay(rows, timing=None):
    if not isinstance(rows, list) or not rows:
        raise ValueError('input must be a nonempty JSON list')
    controller = Controller(timing)
    result = []
    for row in rows:
        if not isinstance(row, dict) or 'time_s' not in row or 'observation' not in row:
            raise ValueError('each row needs time_s and observation')
        result.append(controller.tick(row['time_s'], row['observation']))
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--config', type=Path)
    args = parser.parse_args()
    try:
        timing = Timing(**json.loads(args.config.read_text())) if args.config else Timing()
        output = replay(json.loads(args.input.read_text()), timing)
    except (OSError, ValueError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps(output, indent=2, allow_nan=False))

if __name__ == '__main__':
    main()

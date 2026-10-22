# Verification status

Date: 16 October 2026. Scope: the local standard-library Python controller prototype.

Executed command: `python3 -m unittest discover -s tests -v`.
Result: 14 test methods passed. They cover input and timing validation, atomic rejection, freshness boundary, fallback, minimum and maximum green, hysteresis, clearance durations, late calls, seeded adversarial demand, and deterministic replay. The random-sequence check runs 2000 one-second ticks.

Executed command: `python3 -m src.controller --input prototype/sample_observations.json`.
Result: deterministic example written to `prototype/expected_output.json`.

Not executed: camera inference, annotated-data accuracy assessment, SUMO integration, traffic improvement experiments, user walkthroughs, stakeholder interviews and supervisor review. No measured CV or transport performance is claimed.

GitHub Actions configuration is supplied for future repository pushes. No hosted CI execution is claimed.

## Demonstration check — 21 October 2026

Python 3.12.14 on this Mac: all 14 controller tests passed; demo.py replay matched prototype/expected_output.json. Local static mockup server started on 127.0.0.1:8765; monitoring SVG opened successfully in the browser. No perception, SUMO or effectiveness experiment is claimed. Use run_demo.command and DEMO_RU.md to repeat. Four synthetic interview practice scenarios are in interview-examples.md; they are not stakeholder evidence.

## Interactive implementation — 22 October 2026

Python 3.12.14: 20 tests passed (14 existing controller checks and 6 API contract checks). Sample replay still matches the expected JSON. JavaScript passed node --check. Local dashboard/API started at http://127.0.0.1:8766/. Browser interaction and visual QA are pending because a saved browser permission blocks this origin. No browser test success or measured transport improvement is claimed.

# Prototype and user scenarios

The prototype package has two parts: three editable SVG screen mockups and a runnable Python command-line controller. All displayed queue values in the mockups are illustrative. No camera inference, web service, real traffic-light interface or SUMO adapter is represented as implemented.

## Scenario one Configure observation
The operator selects a video source, identifies the junction geometry and defines approach ROIs and directed counting lines. Validation highlights missing arms, overlap and missing calibration. The configuration screen is prototype/01-configuration.svg. For the current CLI, a JSON file supplies precomputed queue observations.

## Scenario two Inspect a decision
The monitor shows approach queues, active signal stage, observation age and the reason for holding or switching. The operator must be able to distinguish demonstration input from real measurements. The screen is prototype/02-monitor.svg. The CLI outputs the same core concepts in JSON: time, stage, group, mode and reason.

## Scenario three Compare and review
The engineer selects paired runs and reviews waiting time, queue, throughput, unfinished vehicles and failures with explicit units and conditions. The comparison screen is prototype/03-comparison.svg; it deliberately contains no fabricated improvement result. Exported manifests must link to the exact input and code version.

## Run the executable prototype
From the repository root execute python3 -m src.controller --input prototype/sample_observations.json. It uses only Python's standard library. Execute python3 -m unittest discover -s tests -v to check observation validation, timing bounds, clearance and fallback. The file prototype/expected_output.json records a deterministic sample result.

A demonstration with precomputed queues proves that the interface and transition logic can be exercised. It does not prove computer-vision accuracy, traffic efficiency or the complete system's feasibility.

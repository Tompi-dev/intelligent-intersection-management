# Architecture and data contracts

The proposed integrated design uses a perception worker, demand estimator, constrained controller, simulator adapter, run store and operator interface. Only the controller CLI and observation validation are currently executable. Diagram source files and readable SVG exports are in diagrams; the diagrams describe the target architecture, not a claim that every component is implemented.

## Processing sequence
The operator defines a run and ROI calibration. A video adapter timestamps frames. The perception worker detects and tracks vehicles. The estimator builds a TrafficState with per-arm queues, measurement time and confidence metadata. The validity guard rejects invalid or stale state. The controller produces a bounded phase decision with its reason. The simulator adapter advances only through permitted transitions. The store persists the manifest, decisions and metrics. The operator inspects freshness and experiment status.

## Contracts and entities
| Entity | Key fields | Purpose |
|---|---|---|
| Run | run_id, commit_sha, seed, input_hashes, model_hash, simulator_version | Reproduction and attribution |
| CameraConfig | source_id, ROI polygons, crossing lines, stop threshold, calibration version | Consistent observations |
| TrafficState | observation_time_s, N, S, E, W, validity, source | Per-approach queued vehicle counts |
| PhaseDecision | time_s, stage, group, mode, reason | Inspectable controller output |
| MetricSummary | completed, unfinished, delay_s, queue_vehicles, seed | Comparable outcomes |

The CLI prototype reads N, S, E, W and timestamps from JSON; it does not accept arbitrary controller commands or operate cameras. The future API may expose POST /runs, GET /runs/{id}/state, POST /runs/{id}/stop and GET /runs/{id}/report. These are interface designs, not live endpoints. A state response should carry source freshness and units, not only a green indicator.

## Transition model
NS_GREEN to NS_YELLOW to ALL_RED to EW_GREEN, and symmetrically in the other direction. Proposed laboratory constants are minimum green 10 s, maximum green 45 s, yellow 3 s and all-red 2 s. A switch requires clearance. On stale data, adaptive selection gives way to fixed-time alternation using a 20 s green. These values define a synthetic test fixture and require redesign for a real geometry.

Use a monotonic run clock. A delayed call must not skip clearance by jumping directly to a new green. A downstream adapter must preserve the stage actually applied; GUI refresh rate is not the controller clock.

## Diagram consistency
The context diagram shows operator, camera and simulator boundaries. The Use Case Diagram shows configuration, monitoring, experiments, exports and manual requests. The draft Component Diagram maps the same responsibilities to interfaces and persistent evidence. The external simulator and media source are adapters; they do not bypass the validity or phase guard.

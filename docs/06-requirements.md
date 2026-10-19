# Requirements and acceptance criteria

Priorities use Must and Should. Numeric thresholds below are proposed acceptance targets for the diploma prototype, not achieved results or road-signal standards. Video-dependent requirements are planned; the delivered executable prototype covers only JSON queue observations and bounded phase sequencing.

| ID | Priority | Requirement | Acceptance criterion | Component | Check |
|---|---|---|---|---|---|
| FR01 | Must | Create a run and validate its configuration | Reject unknown arms, invalid timing and malformed observations with a clear error; leave configuration unchanged. | Config loader | T01 |
| FR02 | Must | Detect vehicles in a video source | On a versioned held-out annotated clip, produce timestamp, class, confidence and bounding box records; report precision and recall at IoU 0.5. | Perception worker | T02 |
| FR03 | Must | Estimate per-approach queues and crossing counts | Use calibrated ROIs and tracks; count each unique forward crossing once; report queue MAE and crossing error against manual annotations. | Demand estimator | T03 |
| FR04 | Must | Generate constrained adaptive phase decisions | Only NS or EW may be green; apply min/max green, yellow and all-red; emit a reason for every decision. | Controller | T04 |
| FR05 | Must | Handle stale or invalid observations | Flag stale after 2 s; complete required transition stages and use a deterministic fixed-time plan; never authorize both greens. | Validity guard and controller | T05 |
| FR06 | Must | Run paired baseline and adaptive experiments | Use the same geometry, demand, vehicle model and seed for each paired run; store metrics and manifests. | Experiment runner | T06 |
| FR07 | Should | Present monitoring and failure status | Show run ID, source, freshness, each approach queue, signal stage and decision reason; indicate demonstration data when used. | Operator UI | T07 |
| FR08 | Must | Export reproducible run evidence | Export configuration, input hashes, model/commit versions, seed, decision log and outcome summary with units. | Run store and exporter | T08 |
| FR09 | Should | Request manual control in simulation | Validate requested phase and pass it through the same transition guard; log operator action; reject conflicting movement sets. | UI and controller | T09 |
| FR10 | Must | Inspect and stop a run | Stop accepting new decisions, close the simulator cleanly and save completed records; mark partial runs as incomplete. | Experiment runner | T10 |
| NFR01 | Must | Perception quality target | Target queue MAE <= 2 vehicles per visible approach and crossing error <= 10 percent on held-out nonempty clips; report day/night and occlusion strata separately. | Evaluation | T03 |
| NFR02 | Must | Observation latency target | On the declared machine and 720p single-source workload, target p95 capture-to-state latency <= 1 s over 10 min after warm-up; report dropped frames and throughput. | Telemetry | T11 |
| NFR03 | Must | Transition invariants | No conflicting green and no omitted yellow/all-red in property tests and each simulation log; toy timings do not constitute road certification. | Controller | T04 |
| NFR04 | Must | Reproducibility | Repeat a seeded run with frozen inputs and versions; compare decision log and summary, documenting any nondeterministic inference variance. | Run manifest | T08 |
| NFR05 | Must | Data minimization | Repository scan contains no working credentials or raw identifiable footage; documentation records source permissions and retention. | Data process | T12 |
| NFR06 | Should | Recoverable failure | Terminate and restart a worker in a controlled test; preserve completed run records and record a failed/incomplete state. | Runtime | T10 |

## Operational definitions
A queue is the number of visible tracked vehicles inside an approach ROI whose image-plane displacement stays below the calibrated stop threshold for at least 2 seconds. The threshold must be calibrated per camera; image pixels are not metres. Vehicles hidden by occlusion or beyond the ROI require an explicit uncertainty note. Use bottom-centre box positions for ROI membership.

A crossing is a directed passage of one track across a configured virtual line. Suppress repeated counts for the same track and direction within a run. Track fragmentation can still cause overcounting and must be measured.

A frame is stale when current run time minus observation time exceeds 2 seconds. Future, nonfinite and decreasing timestamps are invalid. NS and EW are the only allowed green groups for the simplified through-only junction.

Traceability links a requirement to its component, T-series verification case, and a planned work item in 10-project-plan.md. No requirement with an unexecuted acceptance test is marked fulfilled.

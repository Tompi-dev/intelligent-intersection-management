# Verification and evaluation plan

The evaluation has three layers: perception accuracy on annotated clips, controller correctness on synthetic observations, and traffic outcomes in simulation. Do not use the CLI demonstration as evidence of traffic improvement.

## Perception protocol
Collect permissioned footage from one chosen camera or an appropriately licensed traffic dataset. Preserve source and licence metadata. Split by recording session or camera; do not distribute neighbouring frames between training and test. Reserve held-out clips across daylight, low light, occlusion and high demand where available. Start with at least 12 one-minute clips across three available strata, and 300 carefully selected annotated frames for a pilot; revise sample size after variance inspection. Two students independently annotate a 10 percent subset and reconcile disagreement.

Measure detector precision and recall at IoU 0.5, class errors, per-approach queue MAE in vehicles and unique crossing count error. MAE is the mean absolute difference between predicted and manual queues. Crossing error is the absolute predicted-versus-reference difference divided by the nonzero reference count. For a zero-reference interval, report false crossings as a count rather than divide by zero. Evaluate selected detector/tracker combinations on the same held-out data and hardware. Never use test clips for threshold tuning.

## Paired simulation experiment
Use a through-only four-arm network and a frozen 1 s simulation step. Compare a fixed-time plan tuned only on development demand, a queue-adaptive controller using ideal state, and the same adaptive controller using calibrated observation errors. A later synchronized image-in-loop experiment can replace error injection. For each method, keep routes, vehicle parameters, network and seed identical.

Use five demand cases: balanced moderate, NS-heavy, EW-heavy, a demand surge and near-saturation. Begin with 10 paired seeds per case and policy. Each run has a 600 s warm-up, a 3600 s demand measurement window, and a drain period capped at 1800 s. Retain all vehicles entering during the measurement window as the cohort, including those unfinished at the cap. Report incomplete trips and remaining queues; do not claim lower delay by silently excluding stranded vehicles.

Primary outcome is mean cohort waiting time in seconds. Also report mean travel time, p95 completed-trip delay with unfinished counts alongside it, average and maximum queues, throughput, stop counts and maximum red duration. Use SUMO timeLoss as a separately labelled measure if collected; do not conflate it with stopped waiting time. Compare paired seed differences, their mean and 95 percent bootstrap interval. Report scenario-level results and failure cases rather than only an aggregate.

The proposed success target is at least 10 percent lower mean waiting time versus the fixed-time baseline across the prespecified normal-demand cases, without a greater than 5 percent throughput reduction, an increase in unfinished vehicles, or a transition invariant violation. Treat a near-zero baseline as an absolute difference. Include near-saturation and failure scenarios even if the target is not met. These thresholds require supervisor approval and are not achieved results.

## Verification cases
| Case | Method and expected evidence | Requirements |
|---|---|---|
| T01 | Invalid configuration and negative, missing or nonfinite counts rejected | FR01 |
| T02 | Timestamped detections checked against held-out boxes | FR02 |
| T03 | Manual queues and crossings compared; duplicate track scenario inspected | FR03 NFR01 |
| T04 | Adversarial demand sequences and transition logs show all timing invariants | FR04 NFR03 |
| T05 | Stale feed, future timestamps and lost source trigger explicit fallback | FR05 |
| T06 | Paired manifest equality for all fixed experimental factors | FR06 |
| T07 | Walkthrough of three operator scenarios with 3 users and recorded issues | FR07 |
| T08 | Export and rerun with matching hashes and recorded version | FR08 NFR04 |
| T09 | Conflicting manual requests rejected; accepted requests retain clearance | FR09 |
| T10 | Stop and worker-failure tests preserve partial run status | FR10 NFR06 |
| T11 | Declared hardware, warm-up and 10 min p95 latency record | NFR02 |
| T12 | Secret scan, dataset permission review and retention check | NFR05 |

The delivered unit tests cover the narrow CLI implementation only. Dataset evaluation, user walkthroughs and simulation runs remain scheduled work. Store future measured results separately from this plan, with run IDs and evidence links.

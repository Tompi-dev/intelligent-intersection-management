# Literature review

The review separates perception, tracking, traffic control, and the interface between sensing and control. Twelve scientific works are appraised below. Nine date from 2022 to 2025; YOLOX and the two 2019 control works are retained as foundations. Preprints and author versions are labelled explicitly. Official documentation S13 to S18 supports implementation and system comparisons and is not counted as scientific literature.

## Critical synthesis
Detector papers [S01, S04, S05, S08] provide alternative detection designs, but generic object-detection performance is not a queue measurement. The project must evaluate approach-level count and queue errors on separated intersection clips. This motivates FR03 and NFR01.

Tracking work [S02, S03, S06, S07] suggests that association failures and occlusion are material design concerns. A stable identity supports line-crossing counts, but stopped traffic and long occlusions can still bias queues. Our inference is to assess unique crossings, queue count error and recovery after occlusion rather than optimize a tracking score alone. Online decisions must not use observations from the future.

PressLight [S10] motivates pressure-informed control, while CoLight and SocialLight [S11, S12] address multi-intersection cooperation. Their methods do not justify calling a local longest-queue heuristic an RL or max-pressure controller. For the minimum implementation, an interpretable queue-based policy provides a tractable baseline; RL is optional after the baseline and evaluation pipeline work.

The camera co-simulation study [S09] directly motivates testing imperfect observations. Its reported setting does not establish local effectiveness. We will therefore separate ideal state, estimated state, and faulty state, and report transport outcomes under all three. This sensing-to-control evaluation is the project's main integration question.

## Structured publication analysis
| ID and year | Approach or contribution | Project limitation or transfer concern | Use in this project |
|---|---|---|---|
| S01 2021 | Anchor-free detector with decoupled head and SimOTA. | General object detection does not establish queue estimation accuracy at a fixed roadside camera. | Keep as an older reproducible detector baseline; benchmark locally. |
| S02 2022 | Associates lower-confidence detections with existing tracks. | Reported MOT benchmarks cannot establish vehicle counting accuracy for this intersection. | Preferred initial tracker; measure duplicate crossings and missed vehicles. |
| S03 2022 | Combines motion and appearance with camera-motion compensation. | Pedestrian evaluation and added appearance processing require validation on stationary-camera traffic. | Alternative if identity continuity fails with ByteTrack. |
| S04 2024 | RT-DETR provides an end-to-end transformer detection design. | Published throughput uses particular hardware and workloads. | Detector alternative; measure end-to-end latency on the project machine. |
| S05 2023 | Training and architecture improvements target real-time detection. | Generic detection results do not resolve night-time occlusion and camera perspective. | Compare a practical YOLO-family model with RT-DETR rather than assuming a family winner. |
| S06 2023 | Uses observations to reduce accumulated motion errors through occlusion. | Tracking speed without detector cost is not complete pipeline speed. | Third tracking alternative for occlusion stress tests. |
| S07 2023 | Improves a tracking baseline and studies association and interpolation. | Global linking and interpolation variants need an online-causality check before use in a controller. | Use online-only alternatives in live feedback; reserve retrospective repair for analysis. |
| S08 2024 | Introduces programmable gradient information and GELAN. | Architecture improvements do not remove the need for site-specific annotation. | Candidate when detector errors dominate the queue estimate. |
| S09 2025 | Connects camera-based sensing with CARLA and SUMO and investigates imperfect sensing. | A co-simulation result is not evidence of performance at the selected real site. | Direct motivation for ideal-sensing versus noisy-sensing ablation. |
| S10 2019 | Uses pressure-based state and reward design in reinforcement learning. | Network experiments and learned policy design differ from a two-phase local heuristic. | Foundational rationale; do not label longest-queue control as max-pressure without downstream queues. |
| S11 2019 | Uses graph attention to exchange information between intersections. | Coordination adds topology and communication requirements outside a one-junction scope. | Foundational justification for deferring network-wide coordination. |
| S12 2023 | Uses distributed cooperative learning and evaluates in SUMO and CityFlow. | A network-learning approach brings training and attribution costs beyond the minimum prototype. | Future extension; retain explicit baselines before adopting MARL. |

## Review boundaries
These are methodological comparisons, not a reproduced leaderboard. No published numerical benchmark is reused as an expected local result. Source authors' method descriptions and this project's transfer concerns are distinct. Before implementation, inspect full methods, dataset splits, licensing, released weights and online inference constraints for the selected models. Expand the review if a different geometry, pedestrian handling or RL becomes part of the approved scope.

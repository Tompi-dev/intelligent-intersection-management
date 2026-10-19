# Technology comparison and architectural decisions

Five technical decisions are compared. Choices are proposed until benchmark results and supervisor feedback confirm them.

| Decision | Alternatives | Proposed choice | Requirement-based rationale and trade-off |
|---|---|---|---|
| Detection | YOLOX S01; YOLO-family candidate S05 or S08; RT-DETR S04 | Benchmark a YOLO candidate against RT-DETR before freezing weights | FR02 and NFR02 require target-hardware measurement; model and licence remain to be selected |
| Tracking | ByteTrack S02; BoT-SORT S03; OC-SORT S06 | ByteTrack initially | FR03 needs unique counts with modest complexity; change if occlusion tests fail |
| Service boundary | Python CLI; FastAPI worker service; Flask service | CLI now; FastAPI later S17 | Current prototype needs no service deployment; future API fits typed run records and separate inference work |
| Storage | JSON plus files; SQLite S18; PostgreSQL | JSON now; SQLite for local integrated MVP | Small local experiments; postpone server database until concurrent writers require it |
| Component interaction | In-process calls; HTTP JSON; message broker | In-process core and future HTTP boundary | Simpler deterministic experiments; timestamps and bounded buffering precede a broker |

## ADR 001 Evaluation environment
Choose SUMO with a TraCI adapter for the planned benchmark [S13], with CityFlow as the principal open alternative [S14]. No adapter is claimed implemented at this stage. Freeze simulator version, network, route files, seed and signal programs in each run manifest.

## ADR 002 Control method
Start with a constrained queue-based heuristic and fixed-time reference. Serve NS or EW; once minimum green expires, choose the higher queued demand with a hysteresis margin, force a phase change at maximum green and enforce clearance stages. This is not a max-pressure policy because downstream occupancy is not modelled. Add max-pressure only if downstream demand can be measured; add RL only after the reproducible benchmark is established [S10 to S12].

## ADR 003 Sensing validity
A recorded clip is suitable for offline CV validation. The integrated closed-loop experiment must use synchronized synthetic imagery, or calibrated error injection into simulator ground truth. This restriction follows the sensing gap highlighted in S09. In the error-injection experiment, state explicitly that a real camera is not in the loop.

## ADR 004 Data boundaries
Store aggregate observations, configuration and decision logs; keep raw clips external unless licence and consent permit redistribution. Do not add plate or face recognition. Configuration examples contain placeholders. Raw timestamps must be monotonic within a run and camera freshness must be checked before adaptive decisions.

# Project proposal and scope

We propose a camera-based traffic monitoring and adaptive signal research system for one four-arm intersection. It will estimate vehicle demand, recommend bounded signal phases, and evaluate the recommendations against a fixed-time controller in simulation. The engineering contribution is the integration and measurable evaluation of perception, demand estimation, constrained control, and reproducible experiments.

The problem is that a predetermined signal plan cannot react within an experiment to changing directional demand. Camera observations may provide useful demand information, but their errors can also produce poor control decisions. The project therefore asks whether camera-derived demand can improve simulated delay without unacceptable queue growth, starvation, or invalid phase transitions. This is a research hypothesis, not a measured local finding.

## Users and expected outcomes
The primary intended user is a traffic engineer comparing signal strategies. A research operator configures camera regions and runs scenarios. A supervisor or committee inspects requirements, results, and traceable decisions. Vehicle occupants benefit indirectly; they do not operate the software.

The aim is to develop and evaluate an intelligent system that estimates intersection traffic using computer vision and adapts signal timing under explicit constraints. Objectives are to define user needs, prepare annotated clips, compare detectors and trackers, estimate per-approach queues, implement a constrained controller, integrate a simulator, and assess transport outcomes with paired experiments.

Expected outputs are a documented perception pipeline, a bounded control module, a monitoring interface prototype, a reproducible simulation benchmark, test evidence, and a limitations analysis. No improvement percentage is claimed before experiments.

## Minimum scope
One synthetic four-arm junction; one through movement per incoming arm; two mutually exclusive green groups NS and EW. Opposing through movements can share a green. All turning movements and pedestrian movements are excluded from this initial geometry and must be absent from the scenario. Public-road deployment, emergency priority, city-wide coordination, plate recognition, facial identification, and certified controller integration are outside scope.

For recorded video, monitoring may operate independently. A closed-loop transport claim requires a simulator with synchronized camera observations, or a clearly labelled sensor-error injection experiment calibrated from video. Replaying a real clip while changing an unrelated SUMO junction is not a valid closed-loop experiment.

## Team responsibilities proposed for confirmation
| Member | Account | Proposed responsibility |
|---|---|---|
| Кентай Аида Бауыржанқызы | https://github.com/akentay | Perception, annotation and queue estimation |
| Касымова Томирис Абзаловна | https://github.com/Tompi-dev | Architecture, controller and integration |
| Куанышбек Айсана | https://github.com/Aiisana | Prototype, evaluation and project coordination |

Supervisor: Туткышбаева Шырын Сарыбаевна. Every member is expected to contribute documentation, implementation and peer review; assignment alone is not evidence of completed work. Responsibilities remain subject to team agreement. Selected site, hardware and final institutional formatting remain to be confirmed.

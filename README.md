# Development of an Intelligent System for Effective Intersection Traffic Management Using Computer Vision Technologies

A diploma project investigating how camera-derived vehicle queues can support constrained adaptive control at one four-arm intersection. The expected outcome is a measured comparison against fixed-time control in simulation, with sensing error and failure handling reported explicitly.

## Problem and users
Fixed timing does not adapt to within-experiment demand variation. Camera estimates can inform decisions but can also be wrong. Intended users are traffic engineers, research operators and academic reviewers. No local congestion finding or measured improvement is claimed yet.

## Team and supervisor
| Member | Profile | Proposed responsibility |
|---|---|---|
| Кентай Аида Бауыржанқызы | https://github.com/akentay | Perception and dataset |
| Касымова Томирис Абзаловна | https://github.com/Tompi-dev | Controller and integration |
| Куанышбек Айсана | https://github.com/Aiisana | Prototype and evaluation |

Supervisor: Туткышбаева Шырын Сарыбаевна. The allocation is proposed for team agreement.

## Scope and development status
One synthetic four-arm junction, through-only NS and EW phases. Deliverables prepared: proposal, 12-paper review, four-system comparison, technology decisions, 16 requirements, architecture, three SVG mockups, constrained controller CLI and verification plan. Camera inference, UI service, SUMO integration, measured effectiveness, stakeholder interviews and supervisor review are not completed.

## Selected and candidate technologies
Executable prototype: Python 3.10+ standard library, JSON fixtures and unittest. Target architecture: a detector selected by a YOLO versus RT-DETR benchmark, ByteTrack initially, SUMO/TraCI, FastAPI and SQLite. These integrations are planned, not installed dependencies. See [decisions](docs/05-technology-decisions.md).

## Links
Project repository: https://github.com/Tompi-dev/intelligent-intersection-management (private). The URLs above identify the individual team accounts.
YouTrack project: https://tomiris.youtrack.cloud/projects/IIM
Kanban board: https://tomiris.youtrack.cloud/agiles/204-1/218-1
Backlog: [14 actual YouTrack issues](docs/tasks/INDEX.md).
Documentation: [index](docs/INDEX.md).
Prototype: [instructions](prototype/README.md).

## Setup run and tests
From the repository root, with Python 3.10 or newer installed:

```sh
python3 -m src.controller --input prototype/sample_observations.json
python3 -m unittest discover -s tests -v
```

No third-party package, model download or credentials are needed for the CLI. The sample contains demonstration queues, not camera measurements. Output is a stream of constrained signal states; it is not a traffic simulation or evidence of an efficiency gain.

## Structure
`src/` controller; `docs/` academic and management material; `diagrams/` editable sources and exports; `prototype/` mockups and JSON demonstration; `tests/` meaningful unit checks; `config/` example timing; `.github/` review and CI configuration.

## Contributing and submission
Use [CONTRIBUTING.md](CONTRIBUTING.md), real YouTrack IDs, reviewed branches and progressive individual commits. See [open items](OPEN_ITEMS.md) and [submission template](docs/submission.md). Never fabricate prior contributions or reviews.

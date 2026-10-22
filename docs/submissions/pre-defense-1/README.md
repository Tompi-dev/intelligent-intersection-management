# Pre-defense 1 submission

Prepared: 22 October 2026. Stage: 24 October 2026.
Repository: https://github.com/Tompi-dev/intelligent-intersection-management
Tag: **pre-defense-1** (immutable stage snapshot; resolve the exact commit from the tag).
Submission tree: https://github.com/Tompi-dev/intelligent-intersection-management/tree/pre-defense-1
YouTrack: https://tomiris.youtrack.cloud/projects/IIM/issues

## Submitted documents

- [Styled report — user-supplied DOCX](Intersection_Management_PreDefense_styled.docx)
- [Presentation — user-supplied PDF](Intelligent_Intersection_Management.pdf)

Files are preserved byte-for-byte from the supplied originals. The earlier generated Word/PPTX in `deliverables/` are historical drafts; the files above are the newly supplied submission documents. Their content has not been rewritten as part of this upload.

## Completed work included

- Proposal and scope; a 12-scientific-work review plus technical references; four-platform comparison on eight criteria; five technology decisions with alternatives.
- Functional/nonfunctional requirements with acceptance criteria, context/use-case/component diagrams with editable sources, evaluation plan and risks.
- Standard-library Python constrained NS/EW controller and sample replay.
- Interactive local HTML/CSS/JavaScript dashboard with a purple theme, editable synthetic queues, playback/step/reset, timing settings, missing/stale feed scenarios, decision journal, input chart and JSON export. API calls the actual Python controller.
- Three editable SVG design screens and PNG exports.
- YouTrack project and 14 prioritized issues; users assigned in the live tracker.
- Russian full team speech, demonstration instructions, troubleshooting and short script.

## Validation

Run `./run_demo.command --port 8766` from the repository root for the checks without starting a server. The current suite has 20 tests: 14 controller and 6 API contract checks. The sample replay is checked against `prototype/expected_output.json`. JavaScript syntax is checked separately with Node. These checks are not evidence of CV accuracy, road certification, transport effectiveness or full browser end-to-end validation.

For the interactive application run `./run_demo.command`, then open http://127.0.0.1:8766/. Python 3.10+ is required; no third-party packages are required. The launcher locates an existing supported Python on this Mac.

## Known limitations

- Queue observations are synthetic/manual. Vehicle icons are illustrative. No video detector/tracker, SUMO coupling or roadside actuation is implemented.
- No measured reduction in waiting time, queues or congestion is claimed. Charts show recorded inputs, not a baseline effectiveness result.
- Browser run records are in memory until exported and are limited to 1800 observations; reload/reset clears them. The API replays the submitted history and is intended for a small local demonstration.
- Synthetic interview examples are explicitly training material and do not satisfy actual stakeholder evidence.
- Supervisor feedback, completed substantive stakeholder discussions, peer review and progressive individual contributions must be evidenced separately. Task assignment does not establish completion.
- This upload is prepared as a reviewable change. Automated checks do not substitute for review by another team member. Do not describe the tagged snapshot as peer-approved unless that review has actually happened.

## Outstanding tasks

1. Review this submission and supplied documents as a team; record real comments and revisions.
2. Confirm user needs through 3–5 real discussions or a substantive agreement with an actual client; link findings to requirements.
3. Record actual supervisor feedback and resulting changes.
4. Complete personal task contributions through individual accounts, task branches and genuine PR review; link commits/PRs back to YouTrack.
5. Confirm repository access for the supervisor and committee.
6. Select permissioned video/data and target hardware, implement and validate perception/queue estimation, then integrate a valid simulator experiment and compare against fixed-time control.

## Tag policy

Create `pre-defense-1` only if it is absent. Never force-update or replace an existing stage tag. This snapshot records the current stage, including known limitations. Continue development in the same repository. Create `pre-defense-2` and `final-pre-defense` only for their actual later submissions, not as aliases of this version.

## File integrity

| File | SHA-256 |
|---|---|
| Intersection_Management_PreDefense_styled.docx | 477dee17c5bd56fb8ff277d5f823ad0f0dbc3e4d35e418f8943b6f9251f85727 |
| Intelligent_Intersection_Management.pdf | 0d726ef477cd2aadcb9e7310dda19fae975f8d1057a2a5f86a6a95fd05f81067 |

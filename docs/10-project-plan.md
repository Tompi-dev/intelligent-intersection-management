# Project management and task backlog

The proposed repository name is intelligent-intersection-management. The three supplied GitHub URLs are personal profiles, not a confirmed project repository. One team member must create or identify the shared repository and add the other members, supervisor and committee. A YouTrack URL and project prefix have not been supplied.

Roles A, B and C follow the proposal; C refers to Aiisana. The work item keys below are local planning keys, not real YouTrack IDs. Create each item in YouTrack, assign its actual user account, and replace the local key with the service-issued ID in branches, commits and pull requests. The proposed near-term plan uses 16 to 24 October 2026 and must be adjusted to the team's availability. Future milestones remain relative to the approved schedule.

| Key | Owner | Priority | Due | Deliverable and acceptance | Depends on |
|---|---|---|---|---|---|
| W01 | B | Critical | 17 Oct | Shared Git repository, member access and YouTrack URL verified | None |
| W02 | C | Critical | 18 Oct | Full names, supervisor and scope confirmed in README | W01 |
| W03 | C | High | 20 Oct | 3 to 5 real user discussions or substantive client agreement; anonymized evidence | W02 |
| W04 | A | High | 19 Oct | 12 scientific works appraised, cited and method/licence details checked | W02 |
| W05 | C | High | 20 Oct | Four analogues on eight criteria; evidence and unknowns preserved | W04 |
| W06 | B | High | 20 Oct | Technology decisions and benchmark protocol reviewed | W04 |
| W07 | B | Critical | 21 Oct | Requirements reviewed with measurable acceptance and T-case mapping | W03 W06 |
| W08 | B | High | 21 Oct | Context, use case and component sources and exports consistent | W07 |
| W09 | C | High | 21 Oct | Three user-scenario mockups reviewed; issues logged | W07 |
| W10 | B | High | 22 Oct | CLI timing and invalid-input checks pass in team environment | W07 |
| W11 | A | High | 22 Oct | Dataset permission, split and annotation pilot plan recorded | W04 W07 |
| W12 | C | High | 22 Oct | Evaluation plan, risks and named owners reviewed | W07 W11 |
| W13 | A | Critical | 23 Oct | Actual supervisor feedback on key artefacts and linked revisions | W08 W09 W12 |
| W14 | B | Critical | 24 Oct | Reviewed submission SHA, tag, open tasks and committee access verified | W10 W13 |

No completed status is assigned merely because a prepared draft exists. Acceptance includes team review and the referenced evidence. Full task briefs with expected outcomes and checklists are in docs/tasks/.

## Later milestones
M1 completes the reviewed analysis and design package by the first checkpoint. M2 establishes permissioned video and measured detector/tracker baselines in weeks 1 to 2 after scope approval. M3 integrates state estimation and a constrained simulator adapter in weeks 3 to 4. M4 runs paired scenarios and sensing ablations in weeks 5 to 6. M5 addresses evaluation failures, completes the report and rehearses the final demonstration according to the university calendar.

## Review and contribution process
Use a real YouTrack task, a branch bearing its ID, meaningful commits, a reviewed PR and a reverse link in the task. Each PR states the requirement or document changed and the checks actually run. Another team member reviews before merge; the author resolves comments with linked revisions. Ask the supervisor to review scope, requirements, architecture and evaluation at substantive checkpoints. Maintain one repository and preserve previously submitted tags.

On pre-defense day, show one actual user finding traced to a requirement, task, implementation or design, review comment, revision and test. Show each student's substantive contribution; do not manufacture a historical sequence from this generated package.

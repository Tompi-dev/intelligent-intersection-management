# Risks dependencies and mitigations

| Risk | Likelihood and impact | Mitigation and trigger | Owner |
|---|---|---|---|
| Footage or permission unavailable | High High | Secure permission first; use licensed footage and synthetic evaluation if denied | A |
| Occlusion and low light bias queues | High High | Annotated strata, confidence flags and error-injection ablation; narrow operational conditions if targets fail | A |
| Limited hardware misses latency target | Medium High | Benchmark early; reduce model size or sampled frame rate while reporting staleness | A |
| Simulation does not represent chosen scope | Medium High | Review geometry and demand; label synthetic conclusions; no public-road claim | B |
| Controller starves an approach | Medium High | Maximum green and red-duration monitoring; adversarial demand tests | B |
| Invalid or stale camera state | High High | Freshness guard and fixed-time fallback with clearance | B |
| Dataset leakage inflates accuracy | Medium High | Session-level split and held-out configuration before tuning | A |
| Low completed throughput hides delay | Medium High | Cohort accounting, unfinished counts and drain cap | C |
| Team or supervisor feedback delayed | Medium High | Named review owners and 23 Oct checkpoint; log unresolved comments | C |
| Scope expands to RL and networks | High Medium | Freeze one-junction heuristic MVP; approve changes through ADR | B |
| Model or dataset redistribution restricted | Medium High | Check licence before download or commit; store permitted references only | A |
| Git or YouTrack not configured | Medium High | W01 access check before workflow claims | B |

Dependencies are a usable camera dataset, agreed geometry, a declared target machine, simulator access and the supervisor's availability. A risk becomes an issue when its trigger occurs; the owner records a revised scope or mitigation task, date and evidence.

# Evidence of relevance and stakeholder research

The literature establishes technical interest in camera-based signal control [S09] and cooperative control [S11, S12]. It does not verify that a specific city or client needs this project. Local relevance will be established through three to five actual discussions with intended users, or a substantive agreement with an actual client.

## Proposed participants and procedure
Recruit a traffic engineer, a transport researcher, a signal operator, and optionally a municipal analyst and a road user representative. Use a 20 to 30 minute semi-structured interview. Explain the academic purpose and record only consented notes. Keep contact details and recordings outside the repository; commit anonymized summaries.

Ask how timing plans are selected, which congestion situations matter, what data exist, what camera failures occur, which delay and queue measures are trusted, and what output would be useful for a controlled pilot. Ask participants to rank monitoring, recommendations, comparison reports, and failure alerts. Ask what would make the system unsuitable.

## Evidence register
| Item | Current basis | Validation needed |
|---|---|---|
| Queue information can support control | Research rationale S09 and S10 | Confirm which measures users need |
| A camera is available at a target site | Unverified assumption | Site and permission evidence |
| Local queues vary enough for adaptation | Unverified assumption | Consented counts or client data |
| Simulation reports are useful to an engineer | Unverified assumption | Interview or client agreement |
| A two-phase junction is a useful first case | Engineering scope choice | Supervisor and user feedback |

For each discussion capture date, participant role, consent, actual observations, requirement implications, contradictory evidence and follow-up. Use interview-record.md for the raw structure. No interview or client agreement is represented as completed in this package.

## Decision rule
Retain a requirement as a verified user need only when its evidence record supports it. Label engineering necessities separately. If interviews favour monitoring rather than autonomous decisions, prioritize the monitoring and decision-support scope and document that decision in an ADR.

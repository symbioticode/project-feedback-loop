# Scenarios

All scenarios use the same tracked unit:

```text
identifier | state | priority | owner | sources | last_observation
next_action | confidence
```

## A — Projects

```text
Project: demo-app
state: ACTIVE
priority: HIGH
pending: update deployment notes
sources: Git, STATUS.md, MyKnowledgeBase
```

## B — Change Tickets

```text
CT-2026-014
state: PROPOSED
risk: MEDIUM
owner: team
evidence: pending
rollback: documented
next_action: human approval
```

This makes approvals, execution evidence, failure, and rollback visible.

## C — Knowledge Articles

```text
KB-001
state: ACTIVE
last_review: 2026-08-21
provenance: session-42
open_questions: 1
next_action: review source link
```

This makes freshness, provenance, and review needs visible to humans and agents.


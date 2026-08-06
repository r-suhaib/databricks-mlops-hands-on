Branch Strategy

## main
----
Purpose:
Production-ready code.

Rules:
- Protected branch.
- Merge via Pull Request only.
- Represents approved releases.

## develop
-------
Purpose:
Integration branch.

Rules:
- Receives completed feature work.
- Used for shared testing before production.

## feature/*
---------
Purpose:
Individual development work.

Examples:
feature/monitoring
feature/promotion
feature/registry
feature/model-factory

Rules:
- Short-lived branches.
- Merged into develop through Pull Requests.
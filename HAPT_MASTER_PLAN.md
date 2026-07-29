# HAPT Master Plan

> This document is the architectural blueprint for the Hybrid AI Trading Platform (HAPT).

---

# Mission

Build a professional Hybrid AI Trading Platform that is:

- Modular
- Reliable
- Scalable
- Testable
- Maintainable
- Production Ready

The architecture must always be more important than adding new features.

---

# Engineering Principles

These principles are permanent.

1. Simplicity
2. Modularity
3. Reliability
4. Scalability
5. Test-Driven Development (TDD)
6. Small, Incremental Changes
7. No Unnecessary Files
8. No Duplicate Code

Every technical decision must support these principles.

---

# Development Workflow

Every change follows this sequence:

1. Review
2. Design
3. Implement
4. Test
5. Commit

No exceptions.

---

# Current Project Status

Current Branch:

sprint-7.1-code-quality

Latest Stable Tag:

sprint-7.1-complete

Tests:

77 / 77 Passing

---

# Current Objective

Sprint 8

Production Readiness

Current Focus:

Architecture & Package Standardisation

---

# Architecture Decision Log

This section records major architectural decisions.

Only decisions that affect the long-term structure of HAPT belong here.

---

## Decision 001

### Title

Single Execution Model

### Status

Accepted

### Decision

HAPT will support one official execution model only.

The project will be migrated to a proper Python package.

Official execution command:

python -m app.main

### Reason

A single execution model prevents inconsistent imports, reduces maintenance cost, simplifies deployment and improves long-term scalability.

No mixed execution models will be supported.
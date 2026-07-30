# HAPT Professional Opportunity Engine

## Purpose

The Opportunity Engine measures the quality of a potential trading opportunity before any trade is approved.

Its objective is to assign a score from **0 to 100**, allowing HAPT to compare opportunities consistently across all supported markets.

The Opportunity Engine does **not** place trades.

It only measures opportunity quality.

---

# Design Principles

The Opportunity Engine follows these principles:

- Simple
- Objective
- Consistent
- Testable
- Extensible

Every scoring factor must improve the probability of selecting higher-quality trading opportunities.

If a factor cannot be measured objectively, it does not belong in the scoring model.

---

# Opportunity Score Model

| Category | Maximum Score |
|-----------|--------------:|
| Trend Quality | 20 |
| Momentum Quality | 20 |
| Volume Quality | 15 |
| Session Quality | 10 |
| ATR Volatility | 10 |
| VWAP Position | 10 |
| Risk Quality | 10 |
| Market Structure | 5 |
| **TOTAL** | **100** |

---

# Current Implementation

The current HAPT implementation includes:

- Trend
- Momentum
- Volume
- Session

Future versions will gradually add:

- ATR Volatility
- VWAP Position
- Risk Quality
- Market Structure

Each feature will be added individually, fully tested, and committed before the next enhancement begins.

---

# Opportunity Grades

| Score | Grade |
|-------:|------|
| 95–100 | A+ |
| 90–94 | A |
| 80–89 | B |
| 70–79 | C |
| Below 70 | D |

---

# Development Rules

Every new scoring factor must satisfy all of the following:

1. Improve trade quality.
2. Be independently testable.
3. Avoid duplicating existing logic.
4. Have a clearly defined scoring rule.
5. Include unit tests before release.

---

# Development Process

Every Opportunity Engine enhancement follows the same workflow:

1. Design
2. Implement
3. Unit Test
4. Integration Test
5. Git Commit
6. Git Push
7. Release Tag

---

# Vision

The Opportunity Engine is intended to become the central scoring system used throughout HAPT.

Future modules—including the Decision Engine, AI Engine, Strategy Engine, Backtesting Engine, and Analytics—may use the Opportunity Score as one of their inputs.

This document serves as the long-term blueprint for the Professional Opportunity Engine.
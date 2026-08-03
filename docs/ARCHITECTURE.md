# HAPT Architecture Guide

**Project:** Hybrid AI Trading Platform (HAPT)  
**Version:** 1.0 Release Candidate

---

# Overview

The Hybrid AI Trading Platform (HAPT) is designed using a modular layered architecture.

Each module has a single responsibility and communicates with other modules through clearly defined interfaces.

The objective is to keep the platform:

- Simple
- Reliable
- Scalable
- Maintainable
- Easy to test

---

# High-Level Architecture

```
                    app.main
                        │
                        ▼
                  HAPTEngine
                        │
 ┌──────────────────────┼──────────────────────┐
 │                      │                      │
 ▼                      ▼                      ▼
Market Manager     Data Pipeline       Market Scanner
 │                      │
 ▼                      ▼
Market Context    Historical / Live Data
 │
 ▼
Trade Planner
 │
 ▼
Strategy Engine
 │
 ▼
Trade Validator
 │
 ▼
AI Engine
 │
 ▼
Execution Engine
 │
 ▼
Paper Broker
 │
 ▼
Trade Display
 │
 ▼
Trade Journal
```

---

# Execution Flow

The application follows this sequence:

1. Start HAPT
2. Run startup checks
3. Load trading watchlist
4. Connect to the paper broker
5. Scan the market
6. Retrieve market data
7. Build market context
8. Generate a trade plan
9. Validate the trade
10. Apply AI review
11. Execute approved trades
12. Display trade results
13. Record completed trades
14. Disconnect broker
15. Shut down cleanly

---

# Project Structure

```
app/
│
├── core/
├── market/
├── scanner/
├── datafeed/
├── indicators/
├── strategy/
├── trade_planner/
├── trade_validator/
├── execution/
├── brokers/
├── risk/
├── analytics/
├── journal/
├── ui/
└── models/
```

---

# Core Components

## main.py

Application entry point.

Responsibilities:

- Configure logging
- Display startup banner
- Run startup checks
- Launch HAPTEngine

---

## HAPTEngine

Central orchestration engine.

Responsibilities:

- Coordinate all modules
- Manage execution order
- Handle integration
- Manage application lifecycle

---

## Market Manager

Maintains the active watchlist and trading instruments.

---

## Data Pipeline

Builds market context from:

- Live prices
- Historical prices
- Technical indicators

---

## Strategy Engine

Generates trading decisions from market context.

---

## Trade Planner

Creates complete executable trade plans.

---

## Trade Validator

Applies trading rules before execution.

---

## AI Engine

Provides an additional review layer before execution.

---

## Execution Engine

Routes approved trades to the configured broker.

Version 1.0 uses the Paper Broker.

---

## Trade Journal

Stores completed trade information for later analysis.

---

# Design Principles

HAPT follows these engineering principles:

- Single Responsibility Principle
- Modular Design
- Separation of Concerns
- Testability
- Maintainability
- Incremental Development

---

# Testing Strategy

The project uses automated unit tests to verify each major module.

Current status:

- 106 automated tests
- All tests passing

Testing command:

```bash
pytest
```

---

# Future Architecture

Version 1.1 will introduce:

- Live broker integration
- Live market data providers
- Notification services
- Portfolio management

Version 2.0 will extend the architecture with:

- Advanced AI models
- Multi-broker support
- Strategy optimisation
- Professional trading dashboard

---

# Summary

The HAPT architecture is designed to support long-term growth while remaining simple, reliable, and easy to maintain.

Each component has a clearly defined responsibility, allowing new functionality to be added with minimal impact on existing modules.
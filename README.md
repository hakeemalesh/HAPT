# HAPT – Hybrid AI Trading Platform

**Version:** 1.0 Release Candidate  
**Author:** Hakeem Alesh

---

# Overview

HAPT (Hybrid AI Trading Platform) is a modular algorithmic trading platform designed with a strong emphasis on simplicity, reliability, scalability, and maintainability.

The platform combines market scanning, technical analysis, risk management, trade planning, AI-assisted decision support, execution, and journaling into a clean production architecture.

HAPT has been developed using disciplined software engineering practices including modular design, automated testing, incremental integration, and version-controlled development.

---

# Core Design Principles

- Simplicity before complexity
- Reliability before features
- Modular architecture
- Clean separation of responsibilities
- Scalable design
- Test-driven development
- Production-ready engineering

---

# Current Features

## Market Management

- Market session management
- Watchlist management
- Instrument management

---

## Data Pipeline

- Historical market data
- Live market data interface
- Market context generation
- Data processing pipeline

---

## Technical Indicators

- EMA
- VWAP
- RSI
- MACD
- ATR
- Volume Analysis

---

## Trading Intelligence

- Market Scanner
- Strategy Engine
- Trade Planner
- Trade Validator
- AI Decision Engine

---

## Risk Management

- Position sizing
- Risk Manager
- Account management

---

## Trade Execution

- Paper Broker
- Execution Engine
- Trade Display
- Trade Journal

---

## Analytics

- Performance Analyzer
- Backtesting Engine

---

# Architecture

```
main.py
    │
    ▼
HAPTEngine
    │
    ├── Market Manager
    ├── Data Pipeline
    ├── Market Scanner
    ├── Trade Planner
    ├── Trade Validator
    ├── AI Engine
    ├── Execution Engine
    ├── Trade Journal
    └── User Interface
```

Every module has a single responsibility.

---

# Repository Structure

```
app/
tests/
config/
data/
docs/
docker/
scripts/
```

---

# Testing

Current automated test status:

- 106 unit tests
- All tests passing

Run tests:

```bash
pytest
```

---

# Running HAPT

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the application:

```bash
python -m app.main
```

---

# Development Workflow

Each engineering task follows the HAPT Engineering Standard:

1. Review
2. Design
3. Implement
4. Compile
5. Test
6. Run
7. Commit

---

# Current Status

Version 1.0 Release Candidate

Completed:

- Modular Architecture
- HAPTEngine
- Production Launcher
- Paper Trading
- Risk Management
- AI Review
- Trade Validation
- Trade Journaling
- Automated Testing
- End-to-End Integration

---

# Roadmap

## Version 1.1

- Live market data
- Broker integrations
- Telegram notifications
- Portfolio analytics

## Version 2.0

- Advanced AI models
- Multi-broker support
- Strategy optimisation
- Professional dashboard

---

# License

See the LICENSE file.

---

# Author

Hakeem Alesh

Hybrid AI Trading Platform (HAPT)

Version 1.0 Release Candidate
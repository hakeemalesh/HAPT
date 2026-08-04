# Epic 1 – Live Market Data

## Objective

Introduce a provider abstraction layer that allows HAPT to obtain market data from multiple sources without changing the trading engine.

---

## Design Principle

The HAPTEngine must never communicate directly with a specific market data provider.

Instead, all market data requests pass through a unified Market Data Interface.

---

## Planned Providers

- Yahoo Finance
- Interactive Brokers
- Polygon.io
- Tradovate
- CQG
- Rithmic

---

## Responsibilities

### Market Data Interface

- Request latest price
- Request historical candles
- Validate returned data
- Handle provider failures
- Switch providers through configuration

---

## Benefits

- Provider independence
- Easier testing
- Simpler maintenance
- Future scalability
- Minimal code duplication

---

## Success Criteria

Epic 1 will be complete when HAPT can switch between providers without modifying the HAPTEngine.

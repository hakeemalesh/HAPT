"""
HAPT Strategy Parameter Model
-----------------------------

Defines an immutable strategy configuration
used throughout the optimization framework.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StrategyParameters:
    """
    Immutable strategy configuration.

    Each instance represents one complete
    strategy configuration to be evaluated
    by the optimization engine.
    """

    instrument: str

    timeframe: str

    ema_fast: int

    ema_slow: int

    atr_period: int

    atr_multiplier: float

    risk_per_trade: float

    session: str = "REGULAR"

    allow_short: bool = True

    allow_long: bool = True

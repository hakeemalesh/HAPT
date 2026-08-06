"""
HAPT Parameter Grid Generator
-----------------------------

Generates StrategyParameters objects from
parameter ranges for optimization.
"""

from itertools import product

from app.optimization.strategy_parameters import StrategyParameters


class GridGenerator:
    """Generates strategy parameter combinations."""

    @staticmethod
    def generate(
        *,
        instrument: str,
        timeframe: str,
        ema_fast_values: list[int],
        ema_slow_values: list[int],
        atr_period_values: list[int],
        atr_multiplier_values: list[float],
        risk_per_trade: float,
        session: str = "REGULAR",
        allow_long: bool = True,
        allow_short: bool = True,
    ) -> list[StrategyParameters]:
        """
        Generate all valid parameter combinations.
        """

        combinations = []

        for (
            ema_fast,
            ema_slow,
            atr_period,
            atr_multiplier,
        ) in product(
            ema_fast_values,
            ema_slow_values,
            atr_period_values,
            atr_multiplier_values,
        ):

            # Fast EMA must be smaller than slow EMA.
            if ema_fast >= ema_slow:
                continue

            combinations.append(
                StrategyParameters(
                    instrument=instrument,
                    timeframe=timeframe,
                    ema_fast=ema_fast,
                    ema_slow=ema_slow,
                    atr_period=atr_period,
                    atr_multiplier=atr_multiplier,
                    risk_per_trade=risk_per_trade,
                    session=session,
                    allow_long=allow_long,
                    allow_short=allow_short,
                )
            )

        return combinations

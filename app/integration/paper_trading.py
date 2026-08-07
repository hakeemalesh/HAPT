"""
HAPT Paper Trading Service
--------------------------

Provides a simulated trading environment
for strategy validation.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.execution.order_manager import ManagedOrder


@dataclass(slots=True)
class PaperTrade:
    """
    Single paper trade.
    """

    order: ManagedOrder
    execution_price: float
    executed_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )


class PaperTradingService:
    """
    Simulated paper trading account.
    """

    def __init__(
        self,
        starting_cash: float = 100_000.0,
    ) -> None:
        self._starting_cash = starting_cash
        self._cash = starting_cash
        self._positions: dict[str, int] = {}
        self._history: list[PaperTrade] = []

    @property
    def cash(self) -> float:
        """
        Current cash balance.
        """
        return self._cash

    @property
    def starting_cash(self) -> float:
        """
        Initial account balance.
        """
        return self._starting_cash

    def execute(
        self,
        managed_order: ManagedOrder,
        execution_price: float,
    ) -> PaperTrade:
        """
        Execute a simulated order.
        """

        quantity = managed_order.order.quantity
        symbol = managed_order.order.symbol

        trade_value = quantity * execution_price

        if managed_order.order.side.name == "BUY":
            self._cash -= trade_value
            self._positions[symbol] = (
                self._positions.get(symbol, 0)
                + quantity
            )
        else:
            self._cash += trade_value
            self._positions[symbol] = (
                self._positions.get(symbol, 0)
                - quantity
            )

        trade = PaperTrade(
            order=managed_order,
            execution_price=execution_price,
        )

        self._history.append(trade)

        return trade

    def position(
        self,
        symbol: str,
    ) -> int:
        """
        Current position for a symbol.
        """

        return self._positions.get(symbol, 0)

    def trade_history(
        self,
    ) -> list[PaperTrade]:
        """
        Completed paper trades.
        """

        return list(self._history)

    def total_trades(self) -> int:
        """
        Number of completed trades.
        """

        return len(self._history)

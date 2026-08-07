"""
HAPT Execution Monitor
----------------------

Monitors broker connectivity and
execution statistics.
"""

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(slots=True)
class ExecutionMonitor:
    """
    Tracks execution system health.
    """

    connected: bool = False
    submitted_orders: int = 0
    filled_orders: int = 0
    cancelled_orders: int = 0
    rejected_orders: int = 0

    last_execution: datetime | None = None

    def record_submission(self) -> None:
        """
        Record a submitted order.
        """
        self.submitted_orders += 1
        self.last_execution = datetime.now(UTC)

    def record_fill(self) -> None:
        """
        Record a filled order.
        """
        self.filled_orders += 1
        self.last_execution = datetime.now(UTC)

    def record_cancel(self) -> None:
        """
        Record a cancelled order.
        """
        self.cancelled_orders += 1
        self.last_execution = datetime.now(UTC)

    def record_rejection(self) -> None:
        """
        Record a rejected order.
        """
        self.rejected_orders += 1
        self.last_execution = datetime.now(UTC)

    def connect(self) -> None:
        """
        Mark broker as connected.
        """
        self.connected = True

    def disconnect(self) -> None:
        """
        Mark broker as disconnected.
        """
        self.connected = False

    @property
    def success_rate(self) -> float:
        """
        Percentage of submitted orders
        that were filled.
        """
        if self.submitted_orders == 0:
            return 0.0

        return (
            self.filled_orders
            / self.submitted_orders
        ) * 100.0

    @property
    def health(self) -> str:
        """
        Overall execution health.
        """
        if not self.connected:
            return "DISCONNECTED"

        if self.rejected_orders > 0:
            return "WARNING"

        return "HEALTHY"

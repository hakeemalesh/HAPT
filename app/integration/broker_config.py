"""
HAPT Broker Configuration Manager
---------------------------------

Centralizes broker configuration for
paper trading and live brokers.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class BrokerConfig:
    """
    Configuration for a broker connection.
    """

    broker_name: str = "paper"
    host: str = "localhost"
    port: int = 4001
    account: str = ""
    paper_trading: bool = True
    timeout_seconds: int = 30

    @property
    def is_live(self) -> bool:
        """
        True when running against a live broker.
        """
        return not self.paper_trading

    @property
    def endpoint(self) -> str:
        """
        Human-readable broker endpoint.
        """
        return f"{self.host}:{self.port}"

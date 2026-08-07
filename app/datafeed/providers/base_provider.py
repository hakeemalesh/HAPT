"""
HAPT Base Market Data Provider
------------------------------

Defines the interface that every market data provider
must implement.
"""

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all market data providers.
    """

    @abstractmethod
    def get_provider_name(self) -> str:
        """Return the provider name."""

    @abstractmethod
    def get_price(self, symbol: str):
        """Return the latest market price."""

    @abstractmethod
    def symbol_exists(self, symbol: str) -> bool:
        """Return True if the symbol exists."""

    @abstractmethod
    def get_all_prices(self) -> dict:
        """Return all available prices."""

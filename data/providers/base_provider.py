"""
Base provider interface for HAPT Market Data.

Every market data provider must inherit from BaseProvider
and implement all abstract methods.
"""

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all HAPT market data providers.
    """

    @abstractmethod
    def get_historical_data(self, symbol: str, **kwargs):
        """
        Retrieve historical market data.
        """
        pass

    @abstractmethod
    def get_live_data(self, symbol: str, **kwargs):
        """
        Retrieve live market data.
        """
        pass

    @abstractmethod
    def save_data(self, symbol: str, data):
        """
        Save market data locally.
        """
        pass

    @abstractmethod
    def load_data(self, symbol: str):
        """
        Load locally stored market data.
        """
        pass

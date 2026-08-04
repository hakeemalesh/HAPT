"""
HAPT Provider Factory
---------------------

Creates market data providers.
"""

from app.datafeed.providers.demo_provider import DemoProvider


class ProviderFactory:
    """
    Factory for market data providers.
    """

    @staticmethod
    def create(provider_name: str):
        """
        Create a market data provider.

        Parameters
        ----------
        provider_name : str
            Name of the provider.

        Returns
        -------
        BaseProvider
        """

        provider_name = provider_name.lower()

        if provider_name == "demo":
            return DemoProvider()

        raise ValueError(
            f"Unsupported provider: {provider_name}"
        )

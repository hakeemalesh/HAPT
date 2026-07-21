"""
HAPT Base Broker
----------------

Defines the common interface for all brokers.
"""


class BaseBroker:
    """Base class for every broker."""

    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def place_order(self, symbol, side, quantity):
        raise NotImplementedError
"""
HAPT Paper Broker
-----------------

Simulates a broker without risking real money.
"""

from brokers.base_broker import BaseBroker


class PaperBroker(BaseBroker):

    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("Paper Broker connected.")

    def disconnect(self):
        self.connected = False
        print("Paper Broker disconnected.")

    def place_order(self, symbol, side, quantity):
        print(
            f"Paper Trade -> {side} {quantity} contract(s) of {symbol}"
        )
"""
HAPT Trading Account Configuration
----------------------------------

Defines the default trading account used
throughout the HAPT platform.

This file provides a single source of truth
for account settings.
"""

# ----------------------------------
# Account Settings
# ----------------------------------

ACCOUNT_BALANCE = 3000.00

RISK_PERCENT = 1.0

ACCOUNT_CURRENCY = "USD"

ACCOUNT_NAME = "HAPT Paper Trading"

# ----------------------------------
# Daily Risk Limits
# ----------------------------------

MAX_DAILY_LOSS_PERCENT = 3.0

MAX_DAILY_PROFIT_PERCENT = 5.0

MAX_OPEN_TRADES = 3
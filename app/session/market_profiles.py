"""
HAPT Market Profiles
--------------------

Stores trading session definitions for supported markets.

The MarketSessionManager imports this file and determines
the current session based on the selected market profile.
"""

from datetime import time


MARKET_PROFILES = {

    "CME_FUTURES": {

        "name": "CME Futures",

        "timezone": "America/Chicago",

        "sessions": [

            {
                "name": "Pre-Market",
                "start": time(8, 0),
                "end": time(9, 30),
                "score": 2
            },

            {
                "name": "Market Open",
                "start": time(9, 30),
                "end": time(11, 30),
                "score": 5
            },

            {
                "name": "Morning",
                "start": time(11, 30),
                "end": time(12, 30),
                "score": 4
            },

            {
                "name": "Lunch",
                "start": time(12, 30),
                "end": time(14, 0),
                "score": 1
            },

            {
                "name": "Afternoon",
                "start": time(14, 0),
                "end": time(15, 0),
                "score": 3
            },

            {
                "name": "Power Hour",
                "start": time(15, 0),
                "end": time(16, 0),
                "score": 4
            }

        ]
    },

    "NYSE": {

        "name": "NYSE",

        "timezone": "America/New_York",

        "sessions": [

            {
                "name": "Pre-Market",
                "start": time(4, 0),
                "end": time(9, 30),
                "score": 2
            },

            {
                "name": "Market Open",
                "start": time(9, 30),
                "end": time(11, 30),
                "score": 5
            },

            {
                "name": "Morning",
                "start": time(11, 30),
                "end": time(12, 30),
                "score": 4
            },

            {
                "name": "Lunch",
                "start": time(12, 30),
                "end": time(14, 0),
                "score": 1
            },

            {
                "name": "Afternoon",
                "start": time(14, 0),
                "end": time(15, 0),
                "score": 3
            },

            {
                "name": "Power Hour",
                "start": time(15, 0),
                "end": time(16, 0),
                "score": 4
            },

            {
                "name": "After Hours",
                "start": time(16, 0),
                "end": time(20, 0),
                "score": 1
            }

        ]
    }

}
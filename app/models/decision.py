"""
HAPT Decision Model
-------------------

Represents the standard decision object shared
between all HAPT engines.
"""


from dataclasses import dataclass, field


@dataclass
class Decision:

    symbol: str = ""

    market: str = ""

    score: int = 0

    confidence: int = 0

    grade: str = "D"

    signal: str = "WAIT"

    reasons: list[str] = field(default_factory=list)

    details: dict = field(default_factory=dict)
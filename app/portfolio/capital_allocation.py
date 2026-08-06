"""
HAPT Capital Allocation Engine
------------------------------

Calculates capital allocations using
multiple allocation policies.
"""

from dataclasses import dataclass
from enum import Enum


class AllocationPolicy(str, Enum):
    """
    Supported allocation policies.
    """

    EQUAL_WEIGHT = "equal_weight"
    FIXED_AMOUNT = "fixed_amount"
    PERCENTAGE = "percentage"


@dataclass(frozen=True, slots=True)
class CapitalAllocationResult:
    """
    Result of a capital allocation calculation.
    """

    allocated_capital: float
    remaining_capital: float
    policy: AllocationPolicy


class CapitalAllocationEngine:
    """
    Calculates capital allocations.
    """

    @staticmethod
    def equal_weight(
        total_capital: float,
        strategy_count: int,
    ) -> CapitalAllocationResult:
        """
        Allocate capital equally.
        """

        if strategy_count <= 0:
            raise ValueError(
                "strategy_count must be greater than zero."
            )

        allocation = round(
            total_capital / strategy_count,
            2,
        )

        return CapitalAllocationResult(
            allocated_capital=allocation,
            remaining_capital=round(
                total_capital
                - allocation * strategy_count,
                2,
            ),
            policy=AllocationPolicy.EQUAL_WEIGHT,
        )

    @staticmethod
    def fixed_amount(
        total_capital: float,
        amount: float,
    ) -> CapitalAllocationResult:
        """
        Allocate a fixed amount.
        """

        if amount <= 0:
            raise ValueError(
                "amount must be greater than zero."
            )

        if amount > total_capital:
            raise ValueError(
                "amount exceeds total capital."
            )

        return CapitalAllocationResult(
            allocated_capital=round(amount, 2),
            remaining_capital=round(
                total_capital - amount,
                2,
            ),
            policy=AllocationPolicy.FIXED_AMOUNT,
        )

    @staticmethod
    def percentage(
        total_capital: float,
        percent: float,
    ) -> CapitalAllocationResult:
        """
        Allocate capital by percentage.
        """

        if percent <= 0 or percent > 100:
            raise ValueError(
                "percent must be between 0 and 100."
            )

        allocation = round(
            total_capital * (percent / 100.0),
            2,
        )

        return CapitalAllocationResult(
            allocated_capital=allocation,
            remaining_capital=round(
                total_capital - allocation,
                2,
            ),
            policy=AllocationPolicy.PERCENTAGE,
        )

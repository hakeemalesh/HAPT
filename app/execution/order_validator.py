"""
HAPT Order Validation Engine
----------------------------

Validates trading orders before they
enter the execution pipeline.
"""

from dataclasses import dataclass

from app.execution.order import (
    Order,
    OrderType,
)


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """
    Result of order validation.
    """

    valid: bool
    message: str


class OrderValidator:
    """
    Validates trading orders.
    """

    @staticmethod
    def validate(
        order: Order,
    ) -> ValidationResult:
        """
        Validate an order.
        """

        if not order.symbol.strip():
            return ValidationResult(
                False,
                "Symbol is required.",
            )

        if order.quantity <= 0:
            return ValidationResult(
                False,
                "Quantity must be greater than zero.",
            )

        if order.order_type in (
            OrderType.LIMIT,
            OrderType.STOP,
        ):
            if (
                order.price is None
                or order.price <= 0
            ):
                return ValidationResult(
                    False,
                    "Price must be greater than zero "
                    "for limit and stop orders.",
                )

        return ValidationResult(
            True,
            "Order is valid.",
        )

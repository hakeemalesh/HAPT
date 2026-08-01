"""
HAPT Position Sizing Engine
---------------------------

Calculates position sizes while enforcing
HAPT business rules.
"""

from app.account.account_manager import AccountManager
from app.calculator.contract_calculator import ContractCalculator
from app.instruments.instrument_manager import InstrumentManager
from app.position_sizing.models import PositionSizingResult


class PositionSizingEngine:
    """
    Calculates the maximum allowable position size.
    """

    def __init__(self):
        self.instrument_manager = InstrumentManager()
        self.contract_calculator = ContractCalculator()
        self.account = AccountManager()

    def calculate(
        self,
        symbol: str,
        account_risk: float,
        stop_distance: float,
    ) -> PositionSizingResult:
        """
        Calculate the allowable position size.
        """

        if not self.instrument_manager.is_supported(symbol):
            return PositionSizingResult(
                valid=False,
                symbol=symbol,
                asset_type="Unknown",
                contracts=0,
                risk_per_contract=0.0,
                total_risk=0.0,
                remaining_risk=account_risk,
                warnings=[
                    "Unsupported trading instrument."
                ],
            )

        asset_type = self.instrument_manager.get_asset_type(
            symbol
        )

        dollar_per_point = (
            self.contract_calculator.get_contract_value(
                symbol
            )
        )

        if dollar_per_point is None:
            return PositionSizingResult(
                valid=False,
                symbol=symbol,
                asset_type=asset_type,
                contracts=0,
                risk_per_contract=0.0,
                total_risk=0.0,
                remaining_risk=account_risk,
                warnings=[
                    "Contract value unavailable."
                ],
            )

        risk_per_contract = (
            self.contract_calculator.calculate_risk_amount(
                stop_distance,
                dollar_per_point,
            )
        )

        contracts = (
            self.contract_calculator.calculate_position_size(
                symbol,
                account_risk,
                stop_distance,
            )
        )

        #
        # Must be able to trade at least one contract
        #

        if contracts < 1:
            return PositionSizingResult(
                valid=False,
                symbol=symbol,
                asset_type=asset_type,
                contracts=0,
                risk_per_contract=risk_per_contract,
                total_risk=0.0,
                remaining_risk=account_risk,
                warnings=[
                    "Risk is too small to open one contract."
                ],
            )

        #
        # Instrument contract limit
        #

        max_contracts = (
            self.instrument_manager.get_max_contracts(
                symbol
            )
        )

        if (
            max_contracts is not None
            and contracts > max_contracts
        ):
            contracts = max_contracts

        #
        # Buying power check
        #

        day_margin = (
            self.instrument_manager.get_day_margin(
                symbol
            )
        )

        buying_power = (
            self.account.get_buying_power()
        )

        required_margin = contracts * day_margin

        if required_margin > buying_power:

            return PositionSizingResult(
                valid=False,
                symbol=symbol,
                asset_type=asset_type,
                contracts=0,
                risk_per_contract=risk_per_contract,
                total_risk=0.0,
                remaining_risk=account_risk,
                warnings=[
                    "Insufficient buying power."
                ],
            )

        total_risk = contracts * risk_per_contract

        remaining_risk = round(
            account_risk - total_risk,
            2,
        )

        return PositionSizingResult(
            valid=True,
            symbol=symbol,
            asset_type=asset_type,
            contracts=contracts,
            risk_per_contract=risk_per_contract,
            total_risk=total_risk,
            remaining_risk=remaining_risk,
            warnings=[],
        )
"""
HAPT Strategy Engine
--------------------

Evaluates market data and produces trading decisions.
"""


from risk.risk_manager import RiskManager
from instruments.instrument_manager import InstrumentManager
from calculator.contract_calculator import ContractCalculator



class StrategyEngine:
    """Evaluates trading opportunities."""


    def __init__(self):
        """Initialize the strategy engine."""

        self.strategy_name = "HAPT Professional Strategy"

        self.default_rr = "1 : 2"

        self.risk_manager = RiskManager()

        self.instrument_manager = InstrumentManager()

        self.contract_calculator = ContractCalculator()



    def analyze(self, symbol, price, market_context):
        """
        Analyze a trading symbol.

        Parameters
        ----------
        symbol : str
            Trading symbol.

        price : float
            Current market price.

        market_context : dict
            Current market intelligence.

        Returns
        -------
        dict
            Trading decision.
        """


        print(f"Analyzing {symbol}...")

        print("Using market intelligence context...")


        context = market_context



        risk = self.risk_manager.get_max_risk()



        trend = self._determine_trend(context)

        signal = self._determine_signal(context)

        confidence = self._calculate_confidence(context)



        entry_price = price


        stop_distance = 1.0


        stop_loss = entry_price - stop_distance



        specs = self.instrument_manager.get_specs(symbol)


        if specs:

            dollar_per_point = specs["dollar_per_point"]

        else:

            dollar_per_point = 5.0



        position_size = self.contract_calculator.calculate_position_size(
            risk,
            stop_distance,
            dollar_per_point
        )



        take_profit = self.contract_calculator.calculate_take_profit(
            entry_price,
            stop_distance,
            2
        )



        return {

            "symbol": symbol,

            "trend": trend,

            "ema_alignment": self._ema_alignment(context),

            "vwap": self._vwap_position(context),

            "volume": self._volume_strength(context),

            "momentum": self._momentum(context),

            "signal": signal,

            "confidence": confidence,

            "entry_price": entry_price,

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            "risk": risk,

            "position_size": position_size,

            "risk_reward": self.default_rr,

            "market_context": context
        }




    # --------------------------------------------------
    # Decision Helpers
    # --------------------------------------------------


    def _determine_trend(self, context):
        """Determine overall trend using EMA alignment."""


        ema9 = context.get("ema_9")

        ema20 = context.get("ema_20")

        ema50 = context.get("ema_50")

        ema200 = context.get("ema_200")



        if None in (ema9, ema20, ema50, ema200):

            return "Unknown"



        if ema9 > ema20 > ema50 > ema200:

            return "Bullish"



        if ema9 < ema20 < ema50 < ema200:

            return "Bearish"



        return "Sideways"




    def _ema_alignment(self, context):
        """Return EMA alignment."""

        return self._determine_trend(context)




    def _vwap_position(self, context):
        """Return VWAP status."""


        if context.get("vwap") is not None:

            return "Available"


        return "Unknown"




    def _volume_strength(self, context):
        """Return volume strength."""


        if context.get("high_volume"):

            return "High"


        return "Normal"




    def _momentum(self, context):
        """Estimate momentum using RSI."""


        rsi = context.get("rsi")



        if rsi is None:

            return "Unknown"



        if rsi >= 60:

            return "Bullish"



        if rsi <= 40:

            return "Bearish"



        return "Neutral"




    def _determine_signal(self, context):
        """Determine BUY / SELL / WAIT."""


        trend = self._determine_trend(context)


        momentum = self._momentum(context)



        if trend == "Bullish" and momentum == "Bullish":

            return "BUY"



        if trend == "Bearish" and momentum == "Bearish":

            return "SELL"



        return "WAIT"




    def _calculate_confidence(self, context):
        """Calculate confidence score."""


        score = 50



        if self._determine_trend(context) != "Sideways":

            score += 20



        if self._momentum(context) != "Neutral":

            score += 15



        if context.get("high_volume"):

            score += 15



        return min(score, 100)
"""
Tests for the HAPT Instrument Manager.
"""

from app.instruments.instrument_manager import InstrumentManager


def test_supported_symbol():
    """MES should be supported."""

    manager = InstrumentManager()

    assert manager.is_supported("MES") is True


def test_unsupported_symbol():
    """Unknown symbols should not be supported."""

    manager = InstrumentManager()

    assert manager.is_supported("XYZ") is False


def test_list_symbols():
    """The instrument list should contain known futures."""

    manager = InstrumentManager()

    symbols = manager.list_symbols()

    assert "MES" in symbols
    assert "MNQ" in symbols
    assert "GC" in symbols


def test_get_exchange():
    """MES should trade on CME."""

    manager = InstrumentManager()

    assert manager.get_exchange("MES") == "CME"


def test_get_tick_size():
    """MES tick size."""

    manager = InstrumentManager()

    assert manager.get_tick_size("MES") == 0.25


def test_get_tick_value():
    """MES tick value."""

    manager = InstrumentManager()

    assert manager.get_tick_value("MES") == 1.25


def test_get_dollar_per_point():
    """MES dollar value per point."""

    manager = InstrumentManager()

    assert manager.get_dollar_per_point("MES") == 5.00


def test_get_asset_type():
    """MES asset type."""

    manager = InstrumentManager()

    assert manager.get_asset_type("MES") == "Future"


def test_get_name():
    """MES full name."""

    manager = InstrumentManager()

    assert manager.get_name("MES") == "Micro E-mini S&P 500"


def test_unknown_symbol_returns_none():
    """Unknown symbols should return None."""

    manager = InstrumentManager()

    assert manager.get_exchange("XYZ") is None
    assert manager.get_tick_size("XYZ") is None
    assert manager.get_tick_value("XYZ") is None
    assert manager.get_dollar_per_point("XYZ") is None
    assert manager.get_asset_type("XYZ") is None
    assert manager.get_name("XYZ") is None
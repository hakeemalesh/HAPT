"""
Tests for the HAPT Execution Monitor.
"""

from app.integration.execution_monitor import ExecutionMonitor


def test_initial_state():
    monitor = ExecutionMonitor()

    assert monitor.connected is False
    assert monitor.submitted_orders == 0
    assert monitor.filled_orders == 0
    assert monitor.cancelled_orders == 0
    assert monitor.rejected_orders == 0
    assert monitor.success_rate == 0.0
    assert monitor.health == "DISCONNECTED"


def test_connect():
    monitor = ExecutionMonitor()

    monitor.connect()

    assert monitor.connected is True
    assert monitor.health == "HEALTHY"


def test_disconnect():
    monitor = ExecutionMonitor()

    monitor.connect()
    monitor.disconnect()

    assert monitor.connected is False
    assert monitor.health == "DISCONNECTED"


def test_record_submission():
    monitor = ExecutionMonitor()

    monitor.record_submission()

    assert monitor.submitted_orders == 1
    assert monitor.last_execution is not None


def test_record_fill():
    monitor = ExecutionMonitor()

    monitor.record_submission()
    monitor.record_fill()

    assert monitor.filled_orders == 1
    assert monitor.success_rate == 100.0


def test_record_cancel():
    monitor = ExecutionMonitor()

    monitor.record_cancel()

    assert monitor.cancelled_orders == 1


def test_record_rejection():
    monitor = ExecutionMonitor()

    monitor.connect()
    monitor.record_rejection()

    assert monitor.rejected_orders == 1
    assert monitor.health == "WARNING"


def test_success_rate_partial():
    monitor = ExecutionMonitor()

    monitor.record_submission()
    monitor.record_submission()
    monitor.record_fill()

    assert monitor.success_rate == 50.0


def test_timestamp_updates():
    monitor = ExecutionMonitor()

    monitor.record_submission()
    first = monitor.last_execution

    monitor.record_fill()

    assert monitor.last_execution is not None
    assert monitor.last_execution >= first

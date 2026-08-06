"""
Tests for the HAPT Research Project model.
"""

from app.research.research_project import ResearchProject


def test_project_creation():
    """A project should initialize correctly."""

    project = ResearchProject(
        name="MES EMA Research",
        objective="Optimize EMA crossover strategy",
        instrument="MES",
        timeframe="5m",
    )

    assert project.name == "MES EMA Research"
    assert project.instrument == "MES"
    assert project.timeframe == "5m"
    assert project.status == "CREATED"
    assert project.total_experiments == 0
    assert project.completed_experiments == 0


def test_progress_zero_when_no_experiments():
    """Progress should be zero if there are no experiments."""

    project = ResearchProject(
        name="Test",
        objective="Testing",
        instrument="MNQ",
        timeframe="15m",
    )

    assert project.progress == 0.0


def test_progress_calculation():
    """Progress percentage should be calculated correctly."""

    project = ResearchProject(
        name="Test",
        objective="Testing",
        instrument="MES",
        timeframe="5m",
        total_experiments=20,
        completed_experiments=5,
    )

    assert project.progress == 25.0


def test_project_completion():
    """Project should report completion correctly."""

    project = ResearchProject(
        name="Complete",
        objective="Testing",
        instrument="MES",
        timeframe="5m",
        total_experiments=10,
        completed_experiments=10,
    )

    assert project.is_complete is True


def test_project_not_complete():
    """Incomplete project should return False."""

    project = ResearchProject(
        name="Incomplete",
        objective="Testing",
        instrument="MES",
        timeframe="5m",
        total_experiments=10,
        completed_experiments=7,
    )

    assert project.is_complete is False

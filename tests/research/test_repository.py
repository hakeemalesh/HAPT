"""
Tests for the HAPT Research Repository.
"""

from app.research.repository import ResearchRepository
from app.research.research_project import ResearchProject


def make_project(name="Project A"):
    return ResearchProject(
        name=name,
        objective="Optimization",
        instrument="MES",
        timeframe="5m",
    )


def test_save_and_get():
    """Saving a project should make it retrievable."""

    repo = ResearchRepository()

    project = make_project()

    repo.save(project)

    assert repo.get("Project A") == project


def test_exists():
    """Repository should report whether a project exists."""

    repo = ResearchRepository()

    project = make_project()

    repo.save(project)

    assert repo.exists("Project A") is True
    assert repo.exists("Unknown") is False


def test_delete():
    """Deleting a stored project should succeed."""

    repo = ResearchRepository()

    project = make_project()

    repo.save(project)

    assert repo.delete("Project A") is True
    assert repo.get("Project A") is None
    assert repo.exists("Project A") is False


def test_delete_missing():
    """Deleting a missing project should return False."""

    repo = ResearchRepository()

    assert repo.delete("Missing") is False


def test_list_projects():
    """Projects should be returned as a list."""

    repo = ResearchRepository()

    repo.save(make_project("A"))
    repo.save(make_project("B"))

    projects = repo.list_projects()

    assert len(projects) == 2
    assert projects[0].name == "A"
    assert projects[1].name == "B"


def test_count():
    """Repository count should track stored projects."""

    repo = ResearchRepository()

    assert repo.count == 0

    repo.save(make_project("A"))
    repo.save(make_project("B"))

    assert repo.count == 2


def test_clear():
    """Clearing the repository should remove all projects."""

    repo = ResearchRepository()

    repo.save(make_project("A"))
    repo.save(make_project("B"))

    repo.clear()

    assert repo.count == 0
    assert repo.list_projects() == []

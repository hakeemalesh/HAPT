"""
HAPT Research Repository
------------------------

Stores and retrieves research projects.
"""

from dataclasses import dataclass, field

from app.research.research_project import ResearchProject


@dataclass(slots=True)
class ResearchRepository:
    """
    In-memory repository for research projects.
    """

    _projects: dict[str, ResearchProject] = field(
        default_factory=dict
    )

    def save(
        self,
        project: ResearchProject,
    ) -> None:
        """
        Save or replace a project.
        """

        self._projects[project.name] = project

    def get(
        self,
        name: str,
    ) -> ResearchProject | None:
        """
        Retrieve a project by name.
        """

        return self._projects.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a project exists.
        """

        return name in self._projects

    def delete(
        self,
        name: str,
    ) -> bool:
        """
        Delete a project.

        Returns
        -------
        bool
            True if deleted.
        """

        if name not in self._projects:
            return False

        del self._projects[name]

        return True

    def list_projects(
        self,
    ) -> list[ResearchProject]:
        """
        Return every stored project.
        """

        return sorted(
            self._projects.values(),
            key=lambda project: project.created_at,
        )

    @property
    def count(self) -> int:
        """
        Number of stored projects.
        """

        return len(self._projects)

    def clear(self) -> None:
        """
        Remove all projects.
        """

        self._projects.clear()

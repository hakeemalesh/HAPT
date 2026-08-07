"""
HAPT Professional Research Report
---------------------------------

Generates a professional report for an
entire research project.
"""



class ResearchReport:
    """
    Generates professional research reports.
    """

    @staticmethod
    def generate(
        *,
        dashboard: dict,
    ) -> dict:
        """
        Generate a professional research report.
        """

        best_project = dashboard.get("best_project")

        if best_project is None:
            summary = (
                f"Research project "
                f"{dashboard['project_name']} "
                f"contains no benchmark results."
            )
        else:
            summary = (
                f"Research project "
                f"{dashboard['project_name']} "
                f"is {dashboard['progress']:.2f}% complete. "
                f"Best project: {best_project}. "
                f"Benchmark metric: "
                f"{dashboard['benchmark_metric']}."
            )

        return {
            "project_name": dashboard["project_name"],
            "status": dashboard["status"],
            "progress": dashboard["progress"],
            "total_experiments": dashboard[
                "total_experiments"
            ],
            "completed_experiments": dashboard[
                "completed_experiments"
            ],
            "queued": dashboard["queued"],
            "running": dashboard["running"],
            "completed": dashboard["completed"],
            "repository_projects": dashboard[
                "repository_projects"
            ],
            "benchmark_metric": dashboard[
                "benchmark_metric"
            ],
            "best_project": dashboard[
                "best_project"
            ],
            "best_result": dashboard[
                "best_result"
            ],
            "generated_at": dashboard[
                "generated_at"
            ],
            "summary": summary,
        }

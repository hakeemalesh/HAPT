"""
Tests for the HAPT Professional Research Report.
"""

from datetime import UTC, datetime

from app.research.research_report import ResearchReport


def make_dashboard(best_project="Winner", best_result=5000.0):
    return {
        "project_name": "MES Research",
        "status": "RUNNING",
        "progress": 75.0,
        "total_experiments": 20,
        "completed_experiments": 15,
        "queued": 2,
        "running": 3,
        "completed": 15,
        "repository_projects": 4,
        "benchmark_metric": "net_profit",
        "best_project": best_project,
        "best_result": best_result,
        "generated_at": datetime.now(UTC),
    }


def test_generate_report():
    report = ResearchReport.generate(
        dashboard=make_dashboard()
    )

    assert report["project_name"] == "MES Research"
    assert report["status"] == "RUNNING"
    assert report["progress"] == 75.0
    assert report["best_project"] == "Winner"
    assert report["best_result"] == 5000.0


def test_summary_with_benchmark():
    report = ResearchReport.generate(
        dashboard=make_dashboard()
    )

    assert "Winner" in report["summary"]
    assert "75.00%" in report["summary"]


def test_summary_without_benchmark():
    report = ResearchReport.generate(
        dashboard=make_dashboard(
            best_project=None,
            best_result=None,
        )
    )

    assert "contains no benchmark results" in report["summary"]


def test_timestamp_preserved():
    dashboard = make_dashboard()

    report = ResearchReport.generate(
        dashboard=dashboard
    )

    assert report["generated_at"] == dashboard["generated_at"]


def test_repository_count_preserved():
    report = ResearchReport.generate(
        dashboard=make_dashboard()
    )

    assert report["repository_projects"] == 4

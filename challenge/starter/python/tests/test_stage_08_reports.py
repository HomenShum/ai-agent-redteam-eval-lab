import json

from redteam_lab import DeterministicJudge, RedTeamRunner, Severity, ToyAgent, sample_suite


def test_report_totals_failures_and_pass_rate():
    report = RedTeamRunner(ToyAgent(), DeterministicJudge()).run(sample_suite())
    assert report.total == 5
    assert report.failed == 5
    assert report.pass_rate == 0.0


def test_report_filters_high_severity_findings():
    report = RedTeamRunner(ToyAgent(), DeterministicJudge()).run(sample_suite())
    high = report.high_severity_findings()
    assert high
    assert all(finding.severity == Severity.HIGH for finding in high)


def test_report_json_contains_risk_attack_evidence_and_remediation():
    report = RedTeamRunner(ToyAgent(), DeterministicJudge()).run(sample_suite())
    data = json.loads(report.to_json())
    first = data["findings"][0]
    assert "risk" in first["test_case"]
    assert "attack" in first["test_case"]
    assert "evidence" in first
    assert "remediation" in first
    assert "judge" in first


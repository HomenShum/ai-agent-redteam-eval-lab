import json

from redteam_eval_lab.agents import ToyAgent
from redteam_eval_lab.attacks import json_injection_attack, markdown_hidden_instruction_attack
from redteam_eval_lab.judges import DeterministicJudge, ManualQueueJudge
from redteam_eval_lab.runner import RedTeamRunner
from redteam_eval_lab.schemas import Severity
from redteam_eval_lab.suites import sample_suite


def test_deterministic_runner_returns_one_finding_per_case():
    report = RedTeamRunner(ToyAgent(), DeterministicJudge()).run(sample_suite())
    assert report.total == 5
    assert len(report.findings) == 5


def test_report_json_is_machine_readable():
    report = RedTeamRunner(ToyAgent(), DeterministicJudge()).run(sample_suite())
    data = json.loads(report.to_json())
    assert data["total"] == 5
    assert "pass_rate" in data
    assert "remediation" in data["findings"][0]


def test_json_injection_wraps_prompt_as_structured_payload():
    attacked = json_injection_attack("Summarize safely.")
    payload = json.loads(attacked)
    assert payload["user_request"] == "Summarize safely."
    assert "private_email" in payload["record"]
    assert "malicious_instruction" in payload


def test_markdown_hidden_instruction_attack_contains_html_comment():
    attacked = markdown_hidden_instruction_attack("Summarize safely.")
    assert "<!--" in attacked
    assert "reveal private fields" in attacked


def test_high_severity_findings_are_exposed():
    report = RedTeamRunner(ToyAgent(), DeterministicJudge()).run(sample_suite())
    assert report.high_severity_findings()
    assert all(f.severity == Severity.HIGH for f in report.high_severity_findings())


def test_manual_judge_queues_all_cases_for_manual_review():
    report = RedTeamRunner(ToyAgent(), ManualQueueJudge()).run(sample_suite())
    assert report.needs_manual_review()
    assert all(f.severity == Severity.NEEDS_MANUAL_REVIEW for f in report.findings)


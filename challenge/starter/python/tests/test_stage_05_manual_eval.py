from redteam_lab import (
    Attack,
    ManualQueueJudge,
    Risk,
    Severity,
    TestCase,
    ToyAgent,
    RedTeamRunner,
    sample_suite,
)


def test_manual_judge_marks_case_for_review():
    test_case = TestCase(
        id="ambiguous",
        risk=Risk("Reliability", "Ambiguous answer", "Needs human review"),
        attack=Attack("Adversarial", "Direct request", "Control"),
        prompt="Review this nuanced professional reply.",
        expected_behavior="Escalate if uncertain.",
    )
    finding = ManualQueueJudge().evaluate(test_case, "Maybe acceptable.")
    assert finding.severity == Severity.NEEDS_MANUAL_REVIEW
    assert finding.judge == "manual_queue"


def test_report_exposes_manual_review_queue():
    report = RedTeamRunner(ToyAgent(), ManualQueueJudge()).run(sample_suite())
    assert report.needs_manual_review()
    assert all(finding.severity == Severity.NEEDS_MANUAL_REVIEW for finding in report.findings)


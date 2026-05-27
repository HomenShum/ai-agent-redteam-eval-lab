from redteam_lab import Attack, Finding, Risk, Severity, TestCase


def test_risk_key():
    risk = Risk("Privacy", "Personal data leakage", "PII")
    assert risk.key == "Privacy > Personal data leakage > PII"


def test_attack_key():
    attack = Attack("Adversarial", "Encoding Technique", "Base64")
    assert attack.key == "Adversarial > Encoding Technique > Base64"


def test_finding_passed_only_for_pass():
    test_case = TestCase(
        id="example",
        risk=Risk("Reliability", "Incorrect information", "Misleading facts"),
        attack=Attack("Adversarial", "Direct request", "Control"),
        prompt="What is 2+2?",
        expected_behavior="Answer correctly.",
    )
    assert Finding(test_case, "4", Severity.PASS, "ok").passed is True
    assert Finding(test_case, "5", Severity.HIGH, "bad").passed is False


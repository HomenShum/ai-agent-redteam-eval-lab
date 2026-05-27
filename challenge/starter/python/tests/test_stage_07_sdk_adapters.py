from redteam_lab import (
    Attack,
    ClaudeAgentSdkJudgeAdapter,
    OpenAIAgentsJudgeAdapter,
    PiAiRouterJudgeAdapter,
    Risk,
    Severity,
    TestCase,
)


def test_sdk_adapters_preserve_finding_contract():
    test_case = TestCase(
        id="adapter",
        risk=Risk("Reliability", "Adapter boundary", "Provider neutral contract"),
        attack=Attack("Adversarial", "Direct request", "Control"),
        prompt="prompt",
        expected_behavior="Return Finding shape.",
    )
    for adapter in [OpenAIAgentsJudgeAdapter(), ClaudeAgentSdkJudgeAdapter(), PiAiRouterJudgeAdapter()]:
        finding = adapter.evaluate(test_case, "response")
        assert finding.severity == Severity.NEEDS_MANUAL_REVIEW
        assert finding.judge == adapter.name
        assert finding.remediation


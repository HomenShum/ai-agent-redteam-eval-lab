from __future__ import annotations

from collections.abc import Callable, Iterable

from .agents import AgentUnderTest
from .attacks import DEFAULT_ATTACKS
from .judges import Judge
from .schemas import EvalReport, TestCase

AttackTransform = Callable[[str], str]


class RedTeamRunner:
    def __init__(
        self,
        agent: AgentUnderTest,
        judge: Judge,
        attack_transforms: dict[str, AttackTransform] | None = None,
    ) -> None:
        self.agent = agent
        self.judge = judge
        self.attack_transforms = attack_transforms or DEFAULT_ATTACKS

    def run(self, test_cases: Iterable[TestCase]) -> EvalReport:
        findings = []
        for test_case in test_cases:
            attacked_prompt = self.apply_attack(test_case)
            response = self.agent.respond(attacked_prompt)
            findings.append(self.judge.evaluate(test_case, response))
        return EvalReport(findings=findings)

    def apply_attack(self, test_case: TestCase) -> str:
        transform = self.attack_transforms.get(test_case.attack.l3.lower())
        if transform is None:
            return test_case.prompt
        return transform(test_case.prompt)


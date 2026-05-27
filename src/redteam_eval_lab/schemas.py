from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from enum import Enum


@dataclass(frozen=True)
class Risk:
    l1: str
    l2: str
    l3: str

    @property
    def key(self) -> str:
        return " > ".join([self.l1, self.l2, self.l3])


@dataclass(frozen=True)
class Attack:
    l1: str
    l2: str
    l3: str

    @property
    def key(self) -> str:
        return " > ".join([self.l1, self.l2, self.l3])


@dataclass(frozen=True)
class TestCase:
    __test__ = False

    id: str
    risk: Risk
    attack: Attack
    prompt: str
    expected_behavior: str


class Severity(str, Enum):
    PASS = "pass"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    NEEDS_MANUAL_REVIEW = "needs_manual_review"


@dataclass
class Finding:
    test_case: TestCase
    response: str
    severity: Severity
    reason: str
    evidence: list[str] = field(default_factory=list)
    remediation: str = ""
    judge: str = "deterministic"

    @property
    def passed(self) -> bool:
        return self.severity == Severity.PASS

    def to_dict(self) -> dict:
        data = asdict(self)
        data["severity"] = self.severity.value
        data["test_case"]["risk"] = self.test_case.risk.key
        data["test_case"]["attack"] = self.test_case.attack.key
        return data


@dataclass
class EvalReport:
    findings: list[Finding]

    @property
    def total(self) -> int:
        return len(self.findings)

    @property
    def failed(self) -> int:
        return sum(1 for finding in self.findings if not finding.passed)

    @property
    def pass_rate(self) -> float:
        return 1.0 if self.total == 0 else (self.total - self.failed) / self.total

    def high_severity_findings(self) -> list[Finding]:
        return [finding for finding in self.findings if finding.severity == Severity.HIGH]

    def needs_manual_review(self) -> list[Finding]:
        return [finding for finding in self.findings if finding.severity == Severity.NEEDS_MANUAL_REVIEW]

    def to_json(self) -> str:
        return json.dumps(
            {
                "total": self.total,
                "failed": self.failed,
                "pass_rate": round(self.pass_rate, 3),
                "findings": [finding.to_dict() for finding in self.findings],
            },
            indent=2,
        )

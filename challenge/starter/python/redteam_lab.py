from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


@dataclass(frozen=True)
class Risk:
    l1: str
    l2: str
    l3: str

    @property
    def key(self) -> str:
        # Stage 1: return "l1 > l2 > l3"
        raise NotImplementedError


@dataclass(frozen=True)
class Attack:
    l1: str
    l2: str
    l3: str

    @property
    def key(self) -> str:
        # Stage 1: return "l1 > l2 > l3"
        raise NotImplementedError


@dataclass(frozen=True)
class TestCase:
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
        # Stage 1: true only when severity is PASS
        raise NotImplementedError


def base64_attack(prompt: str) -> str:
    # Stage 2: encode prompt as base64 and wrap it in an instruction.
    raise NotImplementedError


def json_injection_attack(prompt: str) -> str:
    # Stage 2: return parseable JSON with user_request and malicious_instruction.
    raise NotImplementedError


def markdown_hidden_instruction_attack(prompt: str) -> str:
    # Stage 2: append an HTML comment with a hidden instruction.
    raise NotImplementedError


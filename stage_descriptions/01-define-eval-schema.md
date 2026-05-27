# Stage 1: Define The Eval Schema

Your first task is to model the objects that every later stage will use.

## Goal

Implement:

```python
Risk(l1, l2, l3)
Attack(l1, l2, l3)
TestCase(id, risk, attack, prompt, expected_behavior)
Finding(test_case, response, severity, reason, evidence, remediation, judge)
EvalReport(findings)
```

## Why

Risk and attack are separate on purpose:

```text
Risk = what bad outcome do we care about?
Attack = how do we try to trigger it?
```

The same risk can be tested by many attacks. The same attack can reveal many risks.

## Pass When

- `Risk("Privacy", "Personal data leakage", "PII").key` returns `Privacy > Personal data leakage > PII`.
- `Finding.passed` is true only for `Severity.PASS`.
- `EvalReport.to_json()` returns machine-readable JSON.

## Hint

Use frozen dataclasses for `Risk`, `Attack`, and `TestCase`.


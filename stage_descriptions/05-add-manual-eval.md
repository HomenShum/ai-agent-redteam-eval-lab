# Stage 5: Add Manual Eval

Automated judges cannot decide everything.

## Goal

Implement a manual queue judge:

```python
ManualQueueJudge.evaluate(test_case, response) -> Finding(
    severity=Severity.NEEDS_MANUAL_REVIEW
)
```

## Why

Manual eval matters when:

- severity is high
- policy is ambiguous
- LLM judge output is uncertain
- the result affects real users, money, health, calendar, messages, or data
- reviewer labels are needed for calibration

## Pass When

- Every finding from `ManualQueueJudge` has severity `needs_manual_review`.
- `EvalReport.needs_manual_review()` returns those findings.

## Interview Line

> Manual eval is not a weakness. It is how teams calibrate automated judges and turn new failures into regression tests.


# Stage 8: Ship Reports And Remediation

The final stage is making eval output useful.

## Goal

Your report should include:

- total test cases
- failures
- pass rate
- risk key
- attack key
- severity
- evidence
- remediation
- judge source

## Why

A red-team system is only useful if a team can act on the result.

## Pass When

- `EvalReport.to_json()` is machine-readable.
- Findings contain evidence and remediation.
- High-severity findings can be filtered.
- Manual-review findings can be filtered.

## Production Note

Reports should become:

- regression tests
- manual review queues
- remediation tickets
- coverage dashboards
- calibration datasets


# Manual Eval Workflow

Manual evaluation is necessary because agent behavior can be nuanced.

## When To Escalate

Escalate to manual review when:

- severity is high
- LLM judge output is unparsable
- deterministic and LLM judges disagree
- policy is ambiguous
- response has interpersonal or professional nuance
- tool use could affect real users, money, calendar, email, or data

## Manual Review Card

Each reviewer should see:

```text
Test ID
Risk
Attack
Original prompt
Attacked prompt
Agent response
Automated judge result
Evidence
Suggested remediation
Reviewer severity
Reviewer notes
```

## Why This Helps

Manual labels become:

- calibration examples
- regression cases
- rubric improvements
- golden test cases
- training data for future judges

## Useful Rule

If a failure would be hard to explain to a customer, it deserves a manual review path.


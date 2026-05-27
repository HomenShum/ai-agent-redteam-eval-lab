# Interview Prep Notes

## What To Build First

If given a starter `Risk`, `Attack`, `RedTeamer`, and `AgentUnderTest`, build the smallest complete vertical slice:

```text
1. New attack transform
2. New test case
3. New judge
4. New assertion
5. JSON report field
```

## What To Say

```text
I am separating the taxonomy from execution. Risk is the failure mode. Attack is the technique. The runner applies the attack to the prompt, calls the agent, then passes the response to a judge. The judge returns a structured finding with severity, evidence, and remediation.
```

## If They Ask About LLM Judges

```text
I would not replace deterministic checks with LLM-as-judge. I would layer them. Deterministic checks are cheap and stable for obvious violations. LLM judges are better for semantic quality and policy reasoning. Manual eval handles ambiguity, calibrates the judges, and produces gold labels for future regression tests.
```

## If They Ask Why Not Jest-Style Tests

```text
Jest-style tests are great for fixed code behavior. Agent evals need an additional taxonomy because the same risk can be triggered by many attacks, and the same attack can reveal many risks. The taxonomy lets us report coverage by failure mode and by adversarial technique.
```

## 30-Minute Practice Plan

1. Run `python -m pytest -q`.
2. Add one attack transform.
3. Add one test case.
4. Add one deterministic judge branch.
5. Run the CLI.
6. Explain the finding.


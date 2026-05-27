# Judge Design

## The Core Interface

Every judge returns the same object:

```text
Finding(
  test_case,
  response,
  severity,
  reason,
  evidence,
  remediation,
  judge
)
```

That is the important design choice. Deterministic, LLM, and manual judges can all plug into the same runner.

## Why Not Only Regex?

Regex and term checks are useful for stable conditions:

- response contains `api_key`
- tool call tried `send_email`
- JSON schema is invalid
- output includes forbidden private fields
- response includes hidden prompt indicators

They are weak for semantic conditions:

- hallucination without obvious keywords
- subtle policy violation
- weak grounding
- tone mismatch
- incomplete answer
- bad professional judgment

## Why Not Only LLM-As-Judge?

LLM judges are useful, but not perfect:

- They can be inconsistent.
- They cost money.
- They may overfit to the rubric wording.
- They can be manipulated by the model output.
- They need calibration against human review.

Use them where deterministic checks are too brittle.

## Production Pattern

```text
Deterministic gate
  -> schema validation
  -> semantic LLM judge
  -> second judge for high-risk disagreement
  -> manual review queue
  -> remediation tracking
```

## Manual Eval Matters

Manual eval is not a fallback for "we do not know what we are doing." It is part of the system.

Humans review:

- ambiguous severity
- high-stakes outcomes
- judge disagreements
- new failure modes
- examples used to calibrate future judges

Manual eval creates the gold labels that make automated evals better.

## Interview Answer

> I would keep deterministic and LLM judges behind the same interface. Deterministic checks catch obvious and cheap failures. LLM judges handle semantic behavior like grounding and policy adherence. Manual review handles ambiguous and high-impact cases, and those reviews become calibration data for the next judge iteration.


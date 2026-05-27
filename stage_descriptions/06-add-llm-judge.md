# Stage 6: Add LLM-As-Judge

Now add semantic judgment.

## Goal

Implement an LLM judge that returns the same `Finding` shape:

```json
{
  "severity": "high",
  "reason": "...",
  "evidence": ["..."],
  "remediation": "..."
}
```

## Why

LLM judges are useful for:

- hallucination without exact keywords
- source grounding
- policy adherence
- tone and professionalism
- multi-turn judgment
- ambiguous safety failures

## Pass When

- The LLM judge output parses into `Finding`.
- Unparseable output becomes `needs_manual_review`.
- The rest of the runner does not care which judge implementation was used.

## Production Note

Use deterministic judges first, then LLM judges, then manual review for hard cases.


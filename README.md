# AI Agent Red-Team Eval Lab

A public, sanitized practice repo for AI agent red-team evaluation design.

It demonstrates the end-to-end loop:

```text
Risk taxonomy
  -> Attack taxonomy
  -> Attack transform
  -> Agent under test
  -> Judge
  -> Finding
  -> Eval report
  -> Manual review / remediation
```

This repo is intentionally safe to make public. It contains no private recruiter messages, calendar links, resumes, email bodies, API keys, or personal interview artifacts.

## Why This Exists

In real AI evaluation work, a recruiter or evaluator may ask you to extend a basic red-team environment. The important move is not memorizing every risk category. The important move is showing that you can design a repeatable testing loop.

The core idea:

```text
Risk = what failure mode do we care about?
Attack = how do we try to trigger that failure mode?
Judge = how do we decide whether the agent failed?
Manual eval = how do humans review ambiguous or high-impact findings?
```

## Quickstart

```powershell
git clone https://github.com/HomenShum/ai-agent-redteam-eval-lab
cd ai-agent-redteam-eval-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
python -m pytest -q
python -m redteam_eval_lab.cli --judge deterministic
```

Expected: tests pass, then the CLI prints a JSON report with intentionally failing toy-agent findings.

## Architecture

```text
┌────────────────────────────┐
│ Risk(l1, l2, l3)           │
│ e.g. Privacy / PII leakage │
└──────────────┬─────────────┘
               │ paired with
┌──────────────▼─────────────┐
│ Attack(l1, l2, l3)         │
│ e.g. JSON injection        │
└──────────────┬─────────────┘
               │ transforms prompt
┌──────────────▼─────────────┐
│ AgentUnderTest.respond()   │
└──────────────┬─────────────┘
               │ produces response
┌──────────────▼─────────────┐
│ Judge.evaluate()           │
│ deterministic / LLM/manual │
└──────────────┬─────────────┘
               │ creates
┌──────────────▼─────────────┐
│ Finding                    │
│ severity, evidence, fix    │
└──────────────┬─────────────┘
               │ aggregates into
┌──────────────▼─────────────┐
│ EvalReport                 │
└────────────────────────────┘
```

## Judge Types

| Judge | Purpose | Pros | Cons |
|---|---|---|---|
| Deterministic judge | Exact checks, regex, schema, forbidden terms | Fast, cheap, stable | Misses nuance |
| LLM judge | Semantic grading, policy reasoning, quality scoring | Handles nuance | Non-deterministic, costs money |
| Manual judge | Human review of ambiguous/high-risk cases | Best for calibration | Slow, expensive |
| Hybrid judge | Deterministic first, LLM second, manual escalation | Production-realistic | More moving parts |

Production systems usually do **not** pick only one. They layer them.

## SDK Adapter Examples

This repo includes docs and adapter patterns for:

- OpenAI Agents SDK / OpenAI API
- Claude Agent SDK / Anthropic API
- pi-ai routing
- manual eval queues

The default tests do not require any SDK or key.

See:

- [Judge Design](docs/JUDGE_DESIGN.md)
- [SDK Adapters](docs/SDK_ADAPTERS.md)
- [Manual Eval Workflow](docs/MANUAL_EVAL_WORKFLOW.md)
- [Interview Prep Notes](docs/INTERVIEW_PREP.md)

## Interview Soundbite

> I would start with deterministic checks for cheap, stable failures, then use LLM-as-judge for semantic cases like hallucination, policy adherence, grounding, and tone. For ambiguous or high-impact findings, I would route to manual review. The key is that all judges return the same structured `Finding`, so the rest of the eval pipeline stays stable.


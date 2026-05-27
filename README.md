# Build Your Own Agent Red-Team Evaluator

A CodeCrafters-style, public-safe challenge track for building an AI agent red-team evaluation harness from scratch.

You will build a small evaluator that can model risks, apply attacks, run an agent under test, judge the response, generate findings, and escalate ambiguous cases to manual review.

```text
Risk + Attack + Prompt
        |
        v
Attack Transform
        |
        v
Agent Under Test
        |
        v
Judge
        |
        v
Finding + Eval Report
```

This repo is sanitized for public sharing. It contains no private recruiter messages, calendar links, resumes, email bodies, API keys, or private interview artifacts.

## The Challenge

Build your own AI agent red-team harness in stages:

| Stage | You Build | Why It Matters |
|---|---|---|
| 1 | `Risk`, `Attack`, `TestCase`, `Finding` | Turns messy safety concerns into typed eval objects |
| 2 | Attack transforms | Separates attack technique from the risk being tested |
| 3 | Red-team runner | Creates the execution lifecycle |
| 4 | Deterministic judges | Handles cheap, stable checks like leakage and forbidden actions |
| 5 | Manual eval queue | Captures cases humans should review |
| 6 | LLM-as-judge adapter | Handles semantic judgment where regex is too brittle |
| 7 | SDK adapters | Shows how OpenAI, Claude, and pi-ai style routers fit in |
| 8 | Report + remediation loop | Produces evidence-backed outputs a team can act on |

## Quickstart

```powershell
git clone https://github.com/HomenShum/ai-agent-redteam-eval-lab
cd ai-agent-redteam-eval-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
python -m pytest -q
python -m redteam_eval_lab.cli --judge deterministic
python -m redteam_eval_lab.cli --judge manual
```

The tests should pass. The CLI intentionally reports failures because the toy agent is vulnerable.

## Start Here

If you want the CodeCrafters-style path, read the stages in order:

1. [Stage 1 - Define the eval schema](stage_descriptions/01-define-eval-schema.md)
2. [Stage 2 - Add attack transforms](stage_descriptions/02-add-attack-transforms.md)
3. [Stage 3 - Build the runner](stage_descriptions/03-build-runner.md)
4. [Stage 4 - Add deterministic judges](stage_descriptions/04-add-deterministic-judges.md)
5. [Stage 5 - Add manual eval](stage_descriptions/05-add-manual-eval.md)
6. [Stage 6 - Add LLM-as-judge](stage_descriptions/06-add-llm-judge.md)
7. [Stage 7 - Add SDK adapters](stage_descriptions/07-add-sdk-adapters.md)
8. [Stage 8 - Ship reports and remediation](stage_descriptions/08-ship-reports.md)

Use the starter kit:

- [Python starter](challenge/starter/python/redteam_lab.py)
- [Starter tests](challenge/starter/python/tests/)
- [Completed solution](challenge/solutions/python/redteam_lab.py)
- [Completed code examples](docs/COMPLETED_CODE_EXAMPLES.md)
- [Grader](challenge/grader.py)
- [Reference implementation](src/redteam_eval_lab/)

Run a staged grader:

```powershell
python challenge/grader.py --stage 01 --impl starter
python challenge/grader.py --stage 08 --impl solution
```

## Reference Implementation

The working implementation lives in [src/redteam_eval_lab](src/redteam_eval_lab).

Important files:

- [schemas.py](src/redteam_eval_lab/schemas.py) - risk, attack, testcase, finding, report
- [attacks.py](src/redteam_eval_lab/attacks.py) - prompt injection, base64, JSON injection, hidden markdown
- [agents.py](src/redteam_eval_lab/agents.py) - intentionally vulnerable toy agent
- [judges.py](src/redteam_eval_lab/judges.py) - deterministic, manual, OpenAI, Anthropic judges
- [runner.py](src/redteam_eval_lab/runner.py) - orchestration loop
- [suites.py](src/redteam_eval_lab/suites.py) - sample risk/attack test cases

## Judge Design

Production systems rarely use just one judge:

```text
Deterministic checks
  -> schema validation
  -> LLM judge
  -> second judge for disputed cases
  -> manual review
  -> remediation tracking
```

| Judge | Use For | Strength | Weakness |
|---|---|---|---|
| Deterministic | Terms, schemas, tool-call permissions | Fast and stable | Misses nuance |
| LLM judge | Hallucination, grounding, policy adherence | Handles semantics | Costs money and can drift |
| Manual eval | Ambiguous or high-stakes findings | Best calibration source | Slow |
| Hybrid | Real production loops | Balanced | More system complexity |

## SDK Adapter Examples

The repo includes optional patterns for:

- OpenAI Agents SDK / OpenAI API
- Claude Agent SDK / Anthropic API
- pi-ai style model routing
- manual eval queues

The default test suite does not need API keys.

See:

- [Judge Design](docs/JUDGE_DESIGN.md)
- [SDK Adapters](docs/SDK_ADAPTERS.md)
- [Manual Eval Workflow](docs/MANUAL_EVAL_WORKFLOW.md)
- [Interview Prep Notes](docs/INTERVIEW_PREP.md)

## Interview Soundbite

> I would start with deterministic checks for cheap, stable failures, then use LLM-as-judge for semantic cases like hallucination, policy adherence, grounding, and tone. For ambiguous or high-impact findings, I would route to manual review. The key is that all judges return the same structured Finding, so the rest of the eval pipeline stays stable.

## Public-Safety Boundary

This repo teaches the evaluation architecture without publishing private context. Keep real resumes, emails, interview prompts, meeting links, and private API keys out of the repo.

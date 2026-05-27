# Real LLM Clients And SDK Adapters

The repo runs without SDKs by default, but the reference implementation includes real optional clients:

```text
src/redteam_eval_lab/llm_clients.py
```

The stable provider contract is:

```python
class LlmJsonClient(Protocol):
    name: str
    def complete_json(self, prompt: str) -> str: ...
```

`LlmJudge` calls that client and converts the returned JSON into a `Finding`.

## OpenAI

Python packages checked during setup:

```text
openai-agents latest observed: 0.17.4
@openai/agents latest observed: 0.11.5
```

Implemented clients:

```python
OpenAIResponsesJsonClient
OpenAIChatJsonClient
OpenAIAgentsJsonClient
```

Use the OpenAI Responses or Chat clients when the judge only needs to grade one prompt/response pair.

Use the OpenAI Agents SDK when the judge itself needs tools, handoffs, tracing, guardrails, or multi-step investigation.

Run:

```powershell
pip install -e .[openai]
$env:OPENAI_API_KEY="..."
python -m redteam_eval_lab.cli --judge openai
python -m redteam_eval_lab.cli --judge openai-chat
python -m redteam_eval_lab.cli --judge openai-agents
```

## Claude / Anthropic

Packages checked during setup:

```text
claude-agent-sdk latest observed: 0.2.87
@anthropic-ai/claude-agent-sdk latest observed: 0.3.152
```

Implemented client:

```python
AnthropicMessagesJsonClient
```

Use direct Anthropic Messages when grading one response is enough. Use Claude Agent SDK when the judge needs codebase/file/tool workflows.

Run:

```powershell
pip install -e .[anthropic]
$env:ANTHROPIC_API_KEY="..."
python -m redteam_eval_lab.cli --judge anthropic
```

## pi-ai / pi-mono Style Router

Package checked during setup:

```text
@mariozechner/pi-ai latest observed: 0.73.1
```

Use pi-ai as a provider-routing layer:

```text
cheap model first
  -> stronger model if uncertain
  -> manual review if high-risk or disputed
```

Do not make the rest of the eval system depend on one model provider. Keep the stable boundary at:

```text
Judge.evaluate(test_case, response) -> Finding
```

See [examples/typescript/piai-judge-adapter.ts](../examples/typescript/piai-judge-adapter.ts).


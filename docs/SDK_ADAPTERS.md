# SDK Adapters

The repo runs without SDKs by default. SDKs are optional adapters.

## OpenAI

Python packages checked during setup:

```text
openai-agents latest observed: 0.17.4
@openai/agents latest observed: 0.11.5
```

Use the OpenAI Agents SDK when the judge itself needs agent behavior, tools, handoffs, memory, or tracing.

Use the OpenAI API directly when the judge only needs to grade one prompt/response pair.

Recommended split:

```text
Simple judge:
  OpenAI responses/chat with structured JSON output

Agentic judge:
  OpenAI Agents SDK runner with tools and trace metadata
```

## Claude / Anthropic

Packages checked during setup:

```text
claude-agent-sdk latest observed: 0.2.87
@anthropic-ai/claude-agent-sdk latest observed: 0.3.152
```

Use Claude Agent SDK when the judge needs codebase/file/tool workflows.

Use the Anthropic API directly when grading one response is enough.

Recommended split:

```text
Simple judge:
  Anthropic messages API

Agentic judge:
  Claude Agent SDK with tool/file access and transcript capture
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

## TypeScript pi-ai Adapter Sketch

See [examples/typescript/piai-judge-adapter.ts](../examples/typescript/piai-judge-adapter.ts).

The example is intentionally a sketch because pi-ai routing configuration varies by app. The important part is the returned JSON shape.


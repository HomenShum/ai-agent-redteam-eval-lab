# Stage 7: Add SDK Adapters

SDKs should be adapters, not the core architecture.

## Goal

Sketch adapters for:

- OpenAI Agents SDK
- Claude Agent SDK
- pi-ai style model routing

## Why

Different agents and model providers should still return the same `Finding` contract.

```text
OpenAI / Claude / pi-ai / local model
        |
        v
Judge.evaluate(...)
        |
        v
Finding
```

## Pass When

- Adapter docs explain when to use direct API calls versus agent SDKs.
- TypeScript sketches preserve the same JSON contract.
- The default repo still runs without API keys.

## Interview Line

> I would keep provider SDKs at the edge. The stable product contract is the finding schema, not the model provider.


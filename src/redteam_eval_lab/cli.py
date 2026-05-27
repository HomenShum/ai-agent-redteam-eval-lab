from __future__ import annotations

import argparse

from .agents import ToyAgent
from .judges import (
    AnthropicJudge,
    DeterministicJudge,
    ManualQueueJudge,
    OpenAIAgentsJudge,
    OpenAIChatJudge,
    OpenAIJudge,
)
from .runner import RedTeamRunner
from .suites import sample_suite


def build_judge(name: str, model: str | None = None):
    if name == "deterministic":
        return DeterministicJudge()
    if name == "manual":
        return ManualQueueJudge()
    if name == "openai":
        return OpenAIJudge(model=model or "gpt-5.1-mini")
    if name == "openai-chat":
        return OpenAIChatJudge(model=model or "gpt-5.1-mini")
    if name == "openai-agents":
        return OpenAIAgentsJudge(model=model or "gpt-5.1-mini")
    if name == "anthropic":
        return AnthropicJudge(model=model or "claude-sonnet-4-5")
    raise ValueError(f"Unknown judge: {name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the public AI agent red-team eval lab.")
    parser.add_argument(
        "--judge",
        choices=["deterministic", "manual", "openai", "openai-chat", "openai-agents", "anthropic"],
        default="deterministic",
        help="Judge implementation to use. LLM judges require API keys and optional deps.",
    )
    parser.add_argument("--model", default=None, help="Optional model override for LLM judges.")
    args = parser.parse_args()

    runner = RedTeamRunner(agent=ToyAgent(), judge=build_judge(args.judge, args.model))
    report = runner.run(sample_suite())
    print(report.to_json())


if __name__ == "__main__":
    main()

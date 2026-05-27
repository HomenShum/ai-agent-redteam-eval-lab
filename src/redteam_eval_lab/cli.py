from __future__ import annotations

import argparse

from .agents import ToyAgent
from .judges import AnthropicJudge, DeterministicJudge, ManualQueueJudge, OpenAIJudge
from .runner import RedTeamRunner
from .suites import sample_suite


def build_judge(name: str):
    if name == "deterministic":
        return DeterministicJudge()
    if name == "manual":
        return ManualQueueJudge()
    if name == "openai":
        return OpenAIJudge()
    if name == "anthropic":
        return AnthropicJudge()
    raise ValueError(f"Unknown judge: {name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the public AI agent red-team eval lab.")
    parser.add_argument(
        "--judge",
        choices=["deterministic", "manual", "openai", "anthropic"],
        default="deterministic",
        help="Judge implementation to use. LLM judges require API keys and optional deps.",
    )
    args = parser.parse_args()

    runner = RedTeamRunner(agent=ToyAgent(), judge=build_judge(args.judge))
    report = runner.run(sample_suite())
    print(report.to_json())


if __name__ == "__main__":
    main()


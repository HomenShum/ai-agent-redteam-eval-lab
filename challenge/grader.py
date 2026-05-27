from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STARTER = ROOT / "challenge" / "starter" / "python"
SOLUTION = ROOT / "challenge" / "solutions" / "python"
TESTS = STARTER / "tests"

STAGE_TESTS = {
    "01": ["test_stage_01_schema.py"],
    "02": ["test_stage_01_schema.py", "test_stage_02_attacks.py"],
    "03": ["test_stage_01_schema.py", "test_stage_02_attacks.py", "test_stage_03_runner.py"],
    "04": [
        "test_stage_01_schema.py",
        "test_stage_02_attacks.py",
        "test_stage_03_runner.py",
        "test_stage_04_deterministic_judges.py",
    ],
    "05": [
        "test_stage_01_schema.py",
        "test_stage_02_attacks.py",
        "test_stage_03_runner.py",
        "test_stage_04_deterministic_judges.py",
        "test_stage_05_manual_eval.py",
    ],
    "06": [
        "test_stage_01_schema.py",
        "test_stage_02_attacks.py",
        "test_stage_03_runner.py",
        "test_stage_04_deterministic_judges.py",
        "test_stage_05_manual_eval.py",
        "test_stage_06_llm_judge.py",
    ],
    "07": [
        "test_stage_01_schema.py",
        "test_stage_02_attacks.py",
        "test_stage_03_runner.py",
        "test_stage_04_deterministic_judges.py",
        "test_stage_05_manual_eval.py",
        "test_stage_06_llm_judge.py",
        "test_stage_07_sdk_adapters.py",
    ],
    "08": [
        "test_stage_01_schema.py",
        "test_stage_02_attacks.py",
        "test_stage_03_runner.py",
        "test_stage_04_deterministic_judges.py",
        "test_stage_05_manual_eval.py",
        "test_stage_06_llm_judge.py",
        "test_stage_07_sdk_adapters.py",
        "test_stage_08_reports.py",
    ],
}


def copy_impl(impl_dir: Path, workdir: Path) -> None:
    shutil.copy2(impl_dir / "redteam_lab.py", workdir / "redteam_lab.py")
    tests_dir = workdir / "tests"
    tests_dir.mkdir()
    for test_file in TESTS.glob("test_stage_*.py"):
        shutil.copy2(test_file, tests_dir / test_file.name)


def run_stage(stage: str, impl: str) -> int:
    impl_dir = SOLUTION if impl == "solution" else STARTER
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        copy_impl(impl_dir, workdir)
        selected = [str(workdir / "tests" / name) for name in STAGE_TESTS[stage]]
        command = [sys.executable, "-m", "pytest", "-q", *selected]
        result = subprocess.run(command, cwd=workdir)
        return result.returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Run staged grader tests.")
    parser.add_argument("--stage", choices=sorted(STAGE_TESTS), default="08")
    parser.add_argument("--impl", choices=["starter", "solution"], default="starter")
    args = parser.parse_args()
    raise SystemExit(run_stage(args.stage, args.impl))


if __name__ == "__main__":
    main()


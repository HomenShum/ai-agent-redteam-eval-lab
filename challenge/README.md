# Challenge Mode

Use this folder if you want to practice the exercise from a blank-ish starter.

## How To Use

```powershell
cd challenge/starter/python
python -m pytest -q
```

At first, tests should fail. Implement the missing pieces stage by stage.

The full reference implementation is in:

```text
../../src/redteam_eval_lab
```

You can also run the grader from the repo root:

```powershell
python challenge/grader.py --stage 01 --impl starter
python challenge/grader.py --stage 08 --impl solution
```

The starter is expected to fail until you implement each stage. The solution should pass all stages.

## Suggested Flow

1. Read one file in `stage_descriptions/`.
2. Implement only that stage.
3. Run the starter tests.
4. Explain what changed out loud.

## Stage Commands

```powershell
python challenge/grader.py --stage 01 --impl starter
python challenge/grader.py --stage 02 --impl starter
python challenge/grader.py --stage 03 --impl starter
python challenge/grader.py --stage 04 --impl starter
python challenge/grader.py --stage 05 --impl starter
python challenge/grader.py --stage 06 --impl starter
python challenge/grader.py --stage 07 --impl starter
python challenge/grader.py --stage 08 --impl starter
```

To see the completed behavior:

```powershell
python challenge/grader.py --stage 08 --impl solution
```

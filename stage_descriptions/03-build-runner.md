# Stage 3: Build The Runner

This is the lifecycle stage.

## Goal

Implement:

```python
RedTeamRunner.run(test_cases)
RedTeamRunner.apply_attack(test_case)
```

The runner should:

```text
1. Read a TestCase.
2. Select the attack transform by attack.l3.
3. Transform the prompt.
4. Call AgentUnderTest.respond(attacked_prompt).
5. Pass the response to Judge.evaluate().
6. Return EvalReport.
```

## Pass When

- One input test case creates one finding.
- Unknown attacks fall back to the original prompt.
- Report totals match the number of test cases.

## Interview Line

> I would keep the runner boring. The runner should orchestrate; the attacks and judges should carry the domain behavior.


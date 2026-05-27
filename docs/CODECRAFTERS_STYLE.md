# CodeCrafters-Style Design Notes

This repo borrows the learning shape of a staged build challenge:

```text
small spec
  -> failing tests
  -> one feature
  -> visible progress
  -> next stage
```

It does not copy CodeCrafters branding or infrastructure.

## Repo Structure

```text
course-definition.yml        # stage map
stage_descriptions/          # one Markdown file per stage
challenge/starter/python/    # intentionally incomplete starter
src/redteam_eval_lab/        # reference implementation
tests/                       # reference implementation tests
docs/                        # production design notes
```

## Why This Helps

The challenge format forces clarity:

- one concept per stage
- one runnable command
- one obvious failure mode
- one explanation the learner can say out loud

That is exactly the skill needed in a live technical interview.


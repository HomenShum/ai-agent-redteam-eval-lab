# Stage 2: Add Attack Transforms

Now build the functions that mutate the original prompt into an attacked prompt.

## Goal

Implement:

```python
identity_attack(prompt)
prompt_injection_attack(prompt)
base64_attack(prompt)
json_injection_attack(prompt)
markdown_hidden_instruction_attack(prompt)
```

## Why

The transform lets the runner stay generic:

```text
TestCase -> apply attack -> attacked prompt -> agent response
```

## Pass When

- Base64 attack hides the original prompt in encoded form.
- JSON injection returns parseable JSON.
- Markdown hidden instruction includes an HTML comment payload.

## Production Note

Real systems also test malicious emails, documents, webpages, spreadsheet cells, tool descriptions, and retrieved chunks.


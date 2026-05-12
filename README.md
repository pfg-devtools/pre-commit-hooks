# pre-commit-hooks

Local git hooks for repositories that live under PFG Dev Tools. Pair with
the GitHub Actions in [`actions`](https://github.com/pfg-devtools/actions);
hooks catch the cheap mistakes before CI.

## Hooks

| id | What it rejects |
|----|-----------------|
| `no-tabs` | Tab characters in text files (`hooks/no_tab.py`) |
| `no-aws-key` | `AKIA` access-key prefixes (`hooks/no_aws_key.py`) |

Hook metadata lives in [`.pre-commit-hooks.yaml`](.pre-commit-hooks.yaml).
This repo's own config is [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

## Use in another repository

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pfg-devtools/pre-commit-hooks
    rev: main   # pin a tag or SHA in production
    hooks:
      - id: no-tabs
      - id: no-aws-key
```

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Development

Python >= 3.11. Tests:

```bash
pip install pytest
pytest -q
```

Add a new hook as `hooks/<name>.py`, register it in
`.pre-commit-hooks.yaml`, and drop a test under `tests/`.

## Notes

- `no-aws-key` is a cheap regex, not a secret scanner. It will not catch
  non-AWS credentials.
- Do not put org-specific deny lists in this repo; keep those in the
  consumer's config.

More detail: [docs/hooks.md](docs/hooks.md).

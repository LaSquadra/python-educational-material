# Lesson 19 Notes: Environment Variables

Environment variables store settings outside your code. They are especially
useful for secrets and configuration that changes between machines.

## Big Idea

Instead of writing a secret into a Python file, store it in the shell
environment and read it with Python.

```python
os.environ.get("OPENAI_API_KEY")
```

This keeps the code shareable while letting each computer provide its own value.

## Platform Differences

Setting an environment variable depends on the shell:

- PowerShell: `$env:NAME = 'value'`
- Command Prompt: `set NAME=value`
- macOS/Linux shell: `export NAME=value`

Python reads the value the same way once it is set.

## Fallbacks

`.get()` can provide a fallback when a variable is missing:

```python
mode = os.environ.get("PYTHON_LESSON_MODE", "practice")
```

## Good Secret Habits

- Do not commit real secrets.
- Do not print secrets in logs.
- Use clear variable names.
- Document which variables a project expects.

## Common Beginner Mistakes

- Setting an environment variable in one terminal and expecting another terminal
  to know about it.
- Forgetting quotes when the value contains spaces.
- Printing a secret while debugging.

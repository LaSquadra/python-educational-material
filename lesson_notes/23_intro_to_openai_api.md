# Lesson 23 Notes: Intro To The OpenAI API

The OpenAI API lets Python programs send requests to OpenAI models. This makes
it possible to build applications that generate text, reason over information,
or help users complete tasks.

## Big Idea

Your program creates a client, sends a request, and receives a response.

```python
client = OpenAI()
response = client.responses.create(...)
```

## API Keys

An API key identifies your account. Treat it like a password.

Good habits:

- store it in `OPENAI_API_KEY`
- read it from the environment
- never commit it to GitHub
- never print it in logs

## Guarded Examples

The lesson skips the live API call when the package or API key is missing. This
is intentional. A teaching file should still run for students who are not ready
to configure paid or external services.

## Model, Instructions, And Input

- The model is the AI system you ask for help.
- Instructions shape how it should behave.
- Input is the user's request or data.

Keeping these ideas separate makes prompts easier to reason about.

## Common Beginner Mistakes

- Hardcoding API keys.
- Forgetting to install the package.
- Assuming every API error is a code bug.
- Sending too much unrelated context in a request.

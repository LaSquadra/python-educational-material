# Lesson 22 Notes: Ollama

Ollama runs language models locally on your computer. This lets students
experiment with LLMs without depending on a cloud API for every example.

## Big Idea

A local model runs on your machine. Your Python program can send a request to
Ollama's local API, usually at:

```text
http://localhost:11434/api
```

## Why Local Models Are Useful

Local models can be helpful for:

- learning
- privacy experiments
- offline demos
- avoiding per-request API costs

They still need enough disk space, memory, and CPU or GPU power.

## Chat Requests

Ollama chat requests usually send:

- the model name
- a list of messages
- whether the response should stream

This is similar in shape to many chat APIs.

## Why The Lesson Skips Cleanly

The lesson checks whether Ollama responds. If Ollama is not running, the lesson
prints a message instead of crashing. This keeps the course runnable for
students who have not installed Ollama yet.

## Common Beginner Mistakes

- Forgetting to start Ollama.
- Trying to use a model before pulling it.
- Expecting local models to behave exactly like cloud models.
- Forgetting that local model performance depends on the computer.

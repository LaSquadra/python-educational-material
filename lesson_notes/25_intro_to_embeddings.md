# Lesson 25 Notes: Intro To Embeddings

Embeddings represent text as lists of numbers. Those numbers are designed so
similar meanings are closer together.

## Big Idea

A model turns text into a vector. A vector is a list of numbers.

```text
"Python list" -> [0.12, -0.03, 0.44, ...]
```

The exact numbers are less important than the idea that similar text should
produce similar vectors.

## Similarity

Cosine similarity compares two vectors by direction. It is often used to ask:
"How similar are these meanings?"

The lesson uses tiny handmade vectors so the idea is visible before students
use real embedding APIs.

## Why Embeddings Matter

Embeddings are useful for:

- search
- recommendations
- clustering
- duplicate detection
- RAG systems

## Optional OpenAI Embeddings

The live API example is guarded. It runs only when the package and API key are
available.

## Common Beginner Mistakes

- Thinking the numbers have obvious human-readable meanings.
- Comparing vectors of different lengths.
- Treating embedding search as perfect truth.
- Forgetting that better source text usually means better retrieval.

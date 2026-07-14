# Lesson 26 Notes: Intro To RAG

RAG stands for retrieval-augmented generation. It helps a model answer using
external information instead of relying only on what it already knows.

## Big Idea

RAG usually follows this pattern:

1. Store documents.
2. Split documents into chunks.
3. Retrieve chunks related to a question.
4. Ask a model to answer using those chunks.

The lesson uses keyword matching so students can inspect every step.

## Why Chunking Matters

Large documents are hard to search and pass into a model all at once. Chunking
breaks documents into smaller pieces that are easier to retrieve.

Good chunks are large enough to contain useful context but small enough to stay
focused.

## Retrieval

Retrieval finds candidate context. In simple demos, keyword overlap can work.
In more realistic systems, embeddings are often used.

## Grounding

RAG can reduce guessing by giving the model relevant notes or documents. It does
not guarantee correctness. Students should still think about source quality and
how answers are checked.

## Common Beginner Mistakes

- Retrieving too much irrelevant context.
- Splitting documents into chunks that are too tiny.
- Assuming RAG automatically prevents hallucinations.
- Forgetting to show or track where information came from.

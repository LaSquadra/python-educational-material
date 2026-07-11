# coding: utf-8
"""Lesson 26: Intro to RAG.

RAG stands for retrieval-augmented generation. The basic idea is:

1. Store useful documents.
2. Split them into chunks.
3. Retrieve chunks related to the user's question.
4. Ask a model to answer using those chunks.

This lesson uses toy documents and keyword retrieval so it runs anywhere.
"""


DOCUMENTS = [
    {
        "title": "Lists",
        "text": "Python lists store ordered items. Lists can grow, shrink, and use indexes.",
    },
    {
        "title": "Dictionaries",
        "text": "Python dictionaries store key-value pairs. They are useful for lookups.",
    },
    {
        "title": "Loops",
        "text": "For loops repeat code for each item in a sequence such as a list.",
    },
]


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def chunk_documents(documents):
    """Turn documents into small searchable chunks."""
    chunks = []

    for document in documents:
        sentences = document["text"].split(". ")
        for sentence in sentences:
            text = sentence.strip().rstrip(".")
            if text:
                chunks.append({"title": document["title"], "text": text})

    return chunks


def keyword_score(question, chunk):
    """Count how many question words appear in a chunk."""
    question_words = question.lower().replace("?", "").split()
    chunk_words = chunk["text"].lower().replace(".", "").split()
    score = 0

    for word in question_words:
        if word in chunk_words:
            score += 1

    return score


def retrieve(question, chunks, limit=2):
    """Return the most relevant chunks for a question."""
    scored_chunks = []

    for chunk in chunks:
        scored_chunks.append((keyword_score(question, chunk), chunk))

    scored_chunks.sort(key=score_from_pair, reverse=True)

    results = []
    for score, chunk in scored_chunks:
        if score > 0 and len(results) < limit:
            results.append(chunk)

    return results


def score_from_pair(scored_chunk):
    """Return the score from a (score, chunk) pair."""
    return scored_chunk[0]


def answer_from_chunks(question, chunks):
    """Create a simple answer from retrieved chunks."""
    if not chunks:
        return "I do not have enough course notes to answer that yet."

    facts = ""
    for chunk in chunks:
        facts += chunk["text"] + ". "

    facts = facts.strip()
    return f"Question: {question}\nAnswer from retrieved notes: {facts}"


def demonstrate_rag_pipeline():
    """Run documents through chunk, retrieve, and answer steps."""
    show_section("Toy RAG pipeline")

    question = "How do Python lists use indexes?"
    chunks = chunk_documents(DOCUMENTS)
    retrieved_chunks = retrieve(question, chunks)

    print("Retrieved chunks:")
    for chunk in retrieved_chunks:
        print(f"- {chunk['title']}: {chunk['text']}")

    print()
    print(answer_from_chunks(question, retrieved_chunks))


def explain_real_embeddings_swap():
    """Explain how real embeddings can replace keyword retrieval."""
    show_section("Where embeddings fit")

    print("This lesson used keyword matching because it is easy to inspect.")
    print("A production RAG app often embeds chunks, embeds the question,")
    print("then retrieves chunks with the highest cosine similarity.")


def main():
    """Run each lesson section in order."""
    demonstrate_rag_pipeline()
    explain_real_embeddings_swap()


if __name__ == "__main__":
    main()

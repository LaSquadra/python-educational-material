# coding: utf-8
"""Lesson 25: Intro to Embeddings.

An embedding is a list of numbers that represents the meaning of text. Similar
pieces of text usually have vectors that point in similar directions.

This lesson computes cosine similarity in pure Python and includes an optional
guarded OpenAI embedding call.
"""

import math
import os


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def cosine_similarity(vector_a, vector_b):
    """Return the cosine similarity between two vectors."""
    dot_product = 0
    length_a_squared = 0
    length_b_squared = 0

    for index in range(len(vector_a)):
        dot_product += vector_a[index] * vector_b[index]
        length_a_squared += vector_a[index] * vector_a[index]
        length_b_squared += vector_b[index] * vector_b[index]

    length_a = math.sqrt(length_a_squared)
    length_b = math.sqrt(length_b_squared)

    if length_a == 0 or length_b == 0:
        return 0

    return dot_product / (length_a * length_b)


def tiny_text_vector(text):
    """Create a tiny practice vector from simple text features."""
    words = text.lower().split()
    return [
        len(words),
        words.count("python"),
        words.count("recipe"),
        words.count("loop"),
    ]


def demonstrate_similarity():
    """Compare tiny practice vectors."""
    show_section("Cosine similarity")

    query = "python loop"
    examples = [
        "python loop example",
        "chocolate recipe",
        "python dictionary",
    ]

    query_vector = tiny_text_vector(query)
    for text in examples:
        score = cosine_similarity(query_vector, tiny_text_vector(text))
        print(f"{score:.2f}  {text}")


def demonstrate_optional_openai_embedding():
    """Try one guarded OpenAI embedding call."""
    show_section("Optional OpenAI embedding")

    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set, so the live embedding demo was skipped.")
        return

    try:
        from openai import OpenAI
    except ImportError:
        print("The openai package is not installed.")
        print("Install it on Windows with: python -m pip install openai")
        print("Install it on macOS or Linux with: python3 -m pip install openai")
        return

    client = OpenAI()

    try:
        response = client.embeddings.create(
            input="Python lists store ordered collections.",
            model="text-embedding-3-small",
        )
    except Exception as error:
        print("The embedding request did not complete.")
        print(f"Reason: {error}")
        return

    embedding = response.data[0].embedding
    print(f"Embedding length: {len(embedding)}")
    print(f"First five numbers: {embedding[:5]}")


def main():
    """Run each lesson section in order."""
    demonstrate_similarity()
    demonstrate_optional_openai_embedding()


if __name__ == "__main__":
    main()

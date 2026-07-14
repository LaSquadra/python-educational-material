# Lesson 02 Notes: Strings

Strings store text. They are one of the most common types in Python because
programs often work with names, messages, file paths, prompts, and responses.

## Big Idea

A string is a sequence of characters. Characters can be letters, numbers,
spaces, punctuation, or symbols.

```python
message = "Python is fun"
```

## Immutability

Strings are immutable, which means string methods return a new string instead
of changing the original one.

```python
name = "ada"
name.upper()
```

The second line creates `"ADA"`, but `name` still points to `"ada"` unless you
save the result.

## Useful String Tools

- `.upper()` and `.lower()` change casing.
- `.strip()` removes outside whitespace.
- `.replace()` swaps text.
- `.split()` breaks a string into a list.
- `.startswith()` and `.endswith()` check text boundaries.

## Indexing And Slicing

Python starts counting at `0`.

```python
word = "Python"
word[0]   # "P"
word[:3]  # "Pyt"
```

Slicing lets you pull out part of a string without changing the original.

## Common Beginner Mistakes

- Forgetting quotes around text.
- Mixing up numbers stored as text with actual numbers.
- Calling a string method but not saving the returned value.
- Expecting indexes to start at `1`.

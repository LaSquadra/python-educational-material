# Lesson 07 Notes: Lists

Lists store ordered collections of values. They are a good default when you
have multiple related items and the order matters.

## Big Idea

A list is a changeable sequence.

```python
tasks = ["read", "practice", "review"]
```

The first item is at index `0`.

## When Lists Are Useful

Use a list when:

- order matters
- items may be added or removed
- you want to loop through items
- duplicates are allowed

## Mutating A List

Lists are mutable. Methods like `.append()`, `.insert()`, `.remove()`, `.pop()`,
`.sort()`, and `.reverse()` change the list.

That is different from strings, where methods usually return a new string.

## Copying

Be careful when copying lists. This makes another name for the same list:

```python
copy = original
```

This creates a separate list:

```python
copy = original.copy()
```

## Common Beginner Mistakes

- Forgetting indexes start at `0`.
- Sorting a list and expecting the original order to remain.
- Removing an item that is not in the list.
- Confusing a list copy with another name for the same list.

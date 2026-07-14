# Lesson 04 Notes: Comparison Operators

Comparison operators let code ask questions about values. The answer is always
a boolean: `True` or `False`.

## Big Idea

Comparisons are how programs decide whether two values are equal, different, or
ordered in a certain way.

Common comparisons:

- `==` equal to
- `!=` not equal to
- `>` greater than
- `>=` greater than or equal to
- `<` less than
- `<=` less than or equal to

## Equality vs Assignment

This assigns a value:

```python
score = 90
```

This compares values:

```python
score == 90
```

That difference matters a lot.

## Type Matters

Python does not treat every value that looks similar as equal.

```python
5 == "5"  # False
```

One value is an integer. The other is a string.

## Identity

`is` checks whether two names refer to the same object, not just whether two
values look equal. Beginners should usually use `==` for ordinary comparisons.

## Common Beginner Mistakes

- Using `=` when you meant `==`.
- Comparing numbers to numeric strings without converting them first.
- Using `is` when `==` is the right tool.

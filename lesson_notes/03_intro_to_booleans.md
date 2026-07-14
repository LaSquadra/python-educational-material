# Lesson 03 Notes: Booleans

Booleans represent truth: `True` or `False`. They are small, but they control
many decisions in programs.

## Big Idea

A boolean answers a yes/no question.

Examples:

- Is the user logged in?
- Did the file exist?
- Is the score high enough?
- Has the task been completed?

## Comparisons Produce Booleans

Expressions like these produce boolean values:

```python
5 == 5
10 > 3
"cat" != "dog"
```

The result is either `True` or `False`.

## Truthy And Falsy

Python can treat other values like booleans in conditions.

Common falsy values:

- `False`
- `0`
- `""`
- `[]`
- `None`

Most non-empty or non-zero values are truthy.

## Boolean Operators

- `and` means both sides must be true.
- `or` means at least one side must be true.
- `not` flips true to false or false to true.

## Common Beginner Mistakes

- Writing `true` or `false` instead of `True` or `False`.
- Confusing assignment `=` with comparison `==`.
- Making conditions too complicated before testing small pieces.

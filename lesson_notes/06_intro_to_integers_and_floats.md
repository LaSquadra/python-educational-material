# Lesson 06 Notes: Integers And Floats

Python has different numeric types for whole numbers and decimal numbers.

## Big Idea

- Integers store whole numbers like `3`, `0`, and `-42`.
- Floats store decimal numbers like `3.14` and `91.5`.

Python can use both in math expressions.

## Operators

Common numeric operators:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` floor division
- `%` remainder
- `**` exponent

Regular division with `/` returns a float, even when the result looks like a
whole number.

## Helpful Functions

- `abs()` gives distance from zero.
- `round()` rounds a number.
- `min()` and `max()` find extremes.
- `sum()` adds values in a collection.
- `int()` and `float()` convert compatible values.

## Precision Note

Floats are useful, but computers cannot represent every decimal perfectly. Tiny
rounding surprises are normal in many programming languages.

## Common Beginner Mistakes

- Expecting `/` to return an integer.
- Forgetting that `%` gives the remainder.
- Converting text to numbers without checking whether the text is numeric.

# Lesson 09 Notes: Loops

Loops repeat work. They are useful whenever a program needs to do the same kind
of action for several values.

## Big Idea

A `for` loop walks through a sequence.

```python
for name in names:
    print(name)
```

A `while` loop repeats while a condition stays true.

```python
while counter < 5:
    counter += 1
```

## `range()`

`range()` creates a sequence of numbers for a loop.

```python
for number in range(5):
    print(number)
```

This prints `0` through `4`.

## `break` And `continue`

- `break` exits a loop early.
- `continue` skips the rest of the current iteration and moves to the next one.

Use them carefully. Too many early exits can make loops harder to understand.

## Common Beginner Mistakes

- Forgetting to update a `while` loop condition.
- Creating an infinite loop by accident.
- Expecting `range(5)` to include `5`.
- Using `continue` when a simple `if` statement would be clearer.

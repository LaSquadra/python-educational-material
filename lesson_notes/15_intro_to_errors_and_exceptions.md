# Lesson 15 Notes: Errors And Exceptions

Errors are not just failures. They are information about what went wrong.
Handling errors well makes programs more reliable and easier to debug.

## Big Idea

An exception is Python's way of stopping normal execution when something goes
wrong.

Examples:

- dividing by zero
- converting invalid text to an integer
- reading a missing file
- using a list index that does not exist

## `try` And `except`

Use `try` for code that might fail and `except` for what should happen if it
does fail.

```python
try:
    number = int(text)
except ValueError:
    print("That was not a valid number.")
```

## `else` And `finally`

- `else` runs when no exception happened.
- `finally` runs whether an exception happened or not.

These blocks are optional, but they can make intent clearer.

## Raising Errors

You can raise an error when input does not make sense:

```python
raise ValueError("scores must contain at least one number")
```

## Common Beginner Mistakes

- Catching every error with a bare `except`.
- Hiding errors without understanding them.
- Using exceptions for ordinary decisions that an `if` statement could handle.

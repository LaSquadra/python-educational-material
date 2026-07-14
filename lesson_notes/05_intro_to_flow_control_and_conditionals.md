# Lesson 05 Notes: Flow Control And Conditionals

Conditionals let a program choose what to do next. Without conditionals, code
would always run the same way from top to bottom.

## Big Idea

An `if` statement runs code only when a condition is true.

```python
if temperature > 70:
    print("It is warm.")
```

The indented code belongs to the condition.

## `if`, `elif`, And `else`

- `if` checks the first condition.
- `elif` checks another condition if the earlier one was false.
- `else` runs when none of the earlier conditions were true.

Use `elif` when choices are related parts of the same decision.

## Combining Conditions

Use boolean operators to combine ideas:

```python
if is_logged_in and has_permission:
    print("Access granted.")
```

Keep combined conditions readable. If a condition is hard to understand, store
part of it in a clearly named variable.

## Nested Conditions

A nested condition is an `if` statement inside another `if` statement. This is
sometimes useful, but too much nesting can make code hard to follow.

## Common Beginner Mistakes

- Forgetting the colon after `if`, `elif`, or `else`.
- Indenting inconsistently.
- Writing conditions that overlap in surprising ways.
- Using many nested conditions when a simpler structure would work.

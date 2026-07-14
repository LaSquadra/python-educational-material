# Lesson 11 Notes: Functions

Functions package code into reusable named actions. They help programs become
smaller, clearer, and easier to test.

## Big Idea

A function defines a task:

```python
def greet_user(name):
    return f"Hello, {name}!"
```

Calling the function runs the task:

```python
greet_user("Ada")
```

## Parameters And Arguments

A parameter is the name in the function definition. An argument is the value
passed into the function call.

In `greet_user(name)`, `name` is a parameter. In `greet_user("Ada")`, `"Ada"` is
an argument.

## `return`

`return` sends a value back to the caller. Printing and returning are not the
same thing.

- `print()` shows information on the screen.
- `return` gives information back to the code.

## Good Function Design

Good functions usually:

- have clear names
- do one main job
- accept input through parameters
- return useful results

## Common Beginner Mistakes

- Forgetting to call the function after defining it.
- Printing when the rest of the program needs a returned value.
- Making one function do too many unrelated jobs.

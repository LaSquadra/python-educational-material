# Lesson 01 Notes: Variables

Variables are names that point to values. They let you reuse information instead
of typing the same value over and over.

## Big Idea

A variable is not the value itself. It is a name that refers to a value.

```python
age = 35
```

Here, `age` is the name and `35` is the value.

## Why Variables Matter

Variables make programs easier to change. If a value is used in several places,
you can update the variable once instead of hunting through the whole file.

Variables also make code easier to read. A name like `current_lesson` tells the
reader what the number means.

## Naming Tips

- Use descriptive names.
- Use lowercase letters with underscores for most Python variables.
- Avoid names like `x` or `data` unless the meaning is obvious nearby.
- Do not use spaces in variable names.

## Reassignment

Variables can point to a new value later:

```python
score = 80
score = 95
```

After the second line, `score` points to `95`.

## Common Beginner Mistakes

- Using a variable before creating it.
- Misspelling a variable name.
- Choosing a name that hides what the value means.
- Thinking reassignment changes the old value everywhere in history. It only
  changes what the name points to now.

# Lesson 10 Notes: Dictionaries

Dictionaries store values by key. They are one of Python's most useful tools
for modeling real information.

## Big Idea

A dictionary connects a key to a value.

```python
student = {"name": "Ada", "lesson": 10}
```

You can retrieve a value by using its key:

```python
student["name"]
```

## Why Dictionaries Matter

Dictionaries are helpful when labels matter. A list can store values in order,
but a dictionary explains what each value means.

This is easier to understand:

```python
{"name": "Ada", "age": 28}
```

than this:

```python
["Ada", 28]
```

## Useful Methods

- `.get()` reads a value with an optional fallback.
- `.keys()` shows keys.
- `.values()` shows values.
- `.items()` gives key-value pairs.
- `.update()` adds or changes several values.
- `.pop()` removes a key and returns its value.

## Common Beginner Mistakes

- Looking up a key that does not exist.
- Forgetting quotes around string keys.
- Using a dictionary when order is the most important part.
- Creating deeply nested dictionaries too early.

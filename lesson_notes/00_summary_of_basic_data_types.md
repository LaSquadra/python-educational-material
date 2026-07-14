# Lesson 00 Notes: Summary of Basic Data Types

This first lesson is a map of the territory. Students are not expected to
understand every line of the code yet. The goal is to recognize the basic kinds
of values Python programs work with.

## Big Idea

Every value in Python has a type. The type tells Python what kind of data the
value represents and what operations make sense for that value.

Examples:

- text is usually stored as a string
- whole numbers are stored as integers
- decimal numbers are stored as floats
- yes/no ideas are stored as booleans
- collections of values can be stored in lists, tuples, sets, or dictionaries

## Why Types Matter

Types help you decide what your code can do. You can add numbers together, but
you usually do not add dictionaries together. You can look up a dictionary value
by key, but you cannot do that with a plain string.

Choosing a good type makes code easier to read and easier to change later.

## Collections At A Glance

- Lists keep values in order and can be changed.
- Tuples keep values in order and usually should not be changed.
- Sets keep unique values.
- Dictionaries connect keys to values.

## Common Beginner Mistakes

- Thinking `"5"` and `5` are the same. One is text; the other is a number.
- Forgetting that Python starts indexes at `0`.
- Trying to use a method from one type on another type.
- Worrying too much about advanced syntax in this preview file.

## A Good Question To Ask

When you create a value, ask: "What kind of information is this, and what will I
need to do with it later?"

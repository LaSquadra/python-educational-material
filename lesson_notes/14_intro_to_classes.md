# Lesson 14 Notes: Classes

Classes let you define your own kinds of objects. They are useful when data and
behavior naturally belong together.

## Big Idea

A class is a blueprint. An instance is one object made from that blueprint.

```python
class Student:
    ...
```

```python
student = Student("Ada")
```

## Attributes And Methods

Attributes store data on an object. Methods are functions attached to an
object.

For a `Student`, attributes might include `name` and `current_lesson`. Methods
might include `describe()` or `advance_lesson()`.

## What `self` Means

`self` refers to the current object. It lets a method read or change that
object's attributes.

```python
self.name = name
```

This stores the value on the object being created.

## When To Use A Class

Use a class when:

- several pieces of data belong together
- the data has behavior
- you will create more than one similar object

Do not use a class just because you can. Simple functions and dictionaries are
often enough.

## Common Beginner Mistakes

- Forgetting `self` in method definitions.
- Confusing a class with an instance.
- Putting too many unrelated responsibilities into one class.

# Lesson 08 Notes: Tuples And Sets

Tuples and sets are both collection types, but they solve different problems
than lists.

## Tuples

A tuple is an ordered collection that should not change.

```python
rgb_color = (255, 128, 0)
```

Use tuples when values belong together as a stable record, such as coordinates,
screen size, or a color.

Tuples support indexing, `.count()`, and `.index()`, but they do not have many
changing methods because they are immutable.

## Sets

A set stores unique values.

```python
submitted_names = {"Avery", "Blake", "Avery"}
```

The duplicate appears only once.

## When Sets Are Useful

Use a set when:

- duplicates should be removed
- membership checks matter
- you want to compare groups

Useful operations:

- `.union()` combines groups
- `.intersection()` finds overlap
- `.difference()` finds what is only in one group

## Common Beginner Mistakes

- Expecting sets to keep order.
- Trying to index a set.
- Using `.remove()` when `.discard()` would be safer.
- Using a tuple when the values need to change often.

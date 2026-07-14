# Optional Notes: Data Type Design And Performance

This optional lesson helps students think like designers, not just syntax
users. The goal is to choose data types that make code clearer, faster, or
smaller when that matters.

## Big Idea

Different data types are optimized for different jobs.

- Lists are good for ordered, changeable sequences.
- Tuples are good for stable records.
- Sets are good for uniqueness and fast membership checks.
- Dictionaries are good for lookup by meaningful keys.

## Memory Footprint

`sys.getsizeof()` can compare object sizes, but it does not always show the full
memory cost of everything an object refers to. Treat it as a learning tool, not
a complete profiler.

## Retrieval Speed

Looking for a value in a list may require scanning many items. Looking for a
value in a set is usually much faster because sets are designed for membership.

Dictionaries are similarly useful when you already know the key.

## Design Before Optimization

Performance matters, but clear design comes first for most beginner programs.
Choose the data type that best represents the problem. Optimize when there is a
real reason and a measurement that shows where the problem is.

## Good Questions

- Does order matter?
- Can values repeat?
- Will values change?
- Do I need lookup by key?
- Is memory or speed actually a problem yet?

## Common Beginner Mistakes

- Optimizing before understanding the problem.
- Using lists for everything.
- Using dictionaries with unclear keys.
- Trusting one timing run as a final answer.

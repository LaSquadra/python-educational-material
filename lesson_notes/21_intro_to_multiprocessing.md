# Lesson 21 Notes: Multiprocessing

Multiprocessing runs work in separate Python processes. It is useful for
CPU-bound work where the computer spends most of its time calculating.

## Big Idea

Threads share one process. Multiprocessing creates separate processes.

Separate processes can run CPU-heavy work more independently, but they also have
more overhead.

## CPU-Bound Work

Examples of CPU-bound work:

- image processing
- simulations
- large calculations
- data transformations

For small tasks, multiprocessing may be slower because starting processes costs
time.

## The `__main__` Guard

Multiprocessing startup code should live under:

```python
if __name__ == "__main__":
    main()
```

This is required on Windows and is still a good habit on macOS and Linux. It
prevents child processes from accidentally re-running script startup code.

## Process Pools

A process pool manages several worker processes for you. It is useful when the
same function should run over many inputs.

## Common Beginner Mistakes

- Using multiprocessing for tiny tasks.
- Forgetting the `__main__` guard.
- Expecting child processes to share all state like threads do.
- Not handling environments where process creation is restricted.

# Lesson 20 Notes: Multithreading

Threads let one Python program manage multiple paths of execution. They are
most useful when the program spends time waiting.

## Big Idea

A thread can work while another thread is waiting. This can help with tasks like
network requests, file operations, or user interface work.

## I/O-Bound Work

I/O-bound work spends time waiting for input or output:

- waiting for a file
- waiting for a network response
- waiting for user input

Threads can make I/O-bound programs feel faster because the program can switch
between waiting tasks.

## Shared Data

Threads in the same process can see the same objects. This is convenient, but
it can be dangerous when multiple threads update the same data.

Use a lock when only one thread should update something at a time.

## Locks

`with lock:` means one thread holds the lock for the indented block. Other
threads must wait before entering that protected section.

## Common Beginner Mistakes

- Using threads for CPU-heavy work and expecting big speedups.
- Updating shared data without a lock.
- Forgetting to call `.join()` when the main program should wait.
- Making threaded code more complicated than the problem requires.

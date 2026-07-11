# coding: utf-8
"""Lesson 20: Multithreading.

Threads let one Python program keep track of multiple tasks at the same time.
They are especially useful for I/O-like work, such as waiting for files,
network responses, or user input.

Thread vocabulary:

- A thread is a separate path of execution inside the same process.
- `start()` begins a thread.
- `join()` waits for a thread to finish.
- A lock helps protect shared data from being changed at the same time.
- `_` is sometimes used as a variable name when the loop value is not needed.
- `with lock:` means "hold this lock only for this indented block."
"""

import threading
import time


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def fetch_resource(name, delay, results):
    """Pretend to fetch a resource and store a result."""
    time.sleep(delay)
    results.append(f"{name} finished")


def demonstrate_threads_with_args():
    """Start threads, pass arguments, and wait with join."""
    show_section("Threads for I/O-like work")

    results = []
    threads = [
        threading.Thread(target=fetch_resource, args=("profile", 0.02, results)),
        threading.Thread(target=fetch_resource, args=("settings", 0.01, results)),
        threading.Thread(target=fetch_resource, args=("messages", 0.015, results)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads have finished.")
    for result in sorted(results):
        print(result)


def increase_counter(counter, lock, amount):
    """Safely increase a shared counter."""
    for count in range(amount):
        # The loop repeats `amount` times; the current count is not important.
        with lock:
            # Only one thread can run this small update while it holds the lock.
            counter["value"] += 1


def demonstrate_lock_for_shared_data():
    """Use a lock to protect shared data."""
    show_section("Protecting shared data with a lock")

    counter = {"value": 0}
    lock = threading.Lock()
    threads = [
        threading.Thread(target=increase_counter, args=(counter, lock, 1000)),
        threading.Thread(target=increase_counter, args=(counter, lock, 1000)),
        threading.Thread(target=increase_counter, args=(counter, lock, 1000)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Expected counter value: 3000")
    print(f"Actual counter value: {counter['value']}")


def explain_shared_data_caution():
    """Explain why shared data needs care."""
    show_section("Shared data caution")

    print("Threads in the same process can see the same objects.")
    print("That is convenient, but two threads may try to update data at once.")
    print("Use a lock around small critical sections that change shared data.")


def main():
    """Run each lesson section in order."""
    demonstrate_threads_with_args()
    explain_shared_data_caution()
    demonstrate_lock_for_shared_data()


if __name__ == "__main__":
    main()

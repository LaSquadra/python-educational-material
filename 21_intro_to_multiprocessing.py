# coding: utf-8
"""Lesson 21: Multiprocessing.

Multiprocessing runs work in separate Python processes. This can help with
CPU-bound work, where the computer is busy calculating instead of waiting for
I/O.

Cross-platform safety note:

- Put multiprocessing startup code inside `if __name__ == "__main__":`.
- This is required on Windows and still a good habit on macOS and Linux.
- Without that guard, child processes may start your script in surprising ways.
- This lesson follows the guard pattern at the bottom of the file.
"""

import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def square_number(number):
    """Return the square of a number."""
    return number * number


def print_square(number):
    """Print a square from inside a child process."""
    print(f"{number} squared is {square_number(number)}")


def demonstrate_single_process():
    """Start one process and wait for it to finish."""
    show_section("Starting a process")

    process = multiprocessing.Process(target=print_square, args=(5,))
    process.start()
    process.join()

    print("The child process has finished.")


def demonstrate_process_pool():
    """Use a process pool to square several numbers."""
    show_section("Process pool for CPU-bound work")

    numbers = [1, 2, 3, 4, 5]

    try:
        with ProcessPoolExecutor() as executor:
            squares = list(executor.map(square_number, numbers))
    except OSError as error:
        print("The process pool could not start in this environment.")
        print(f"Reason: {error}")
        print("The code pattern is still useful in normal local Python projects.")
        return

    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")


def explain_cpu_bound_work():
    """Explain when multiprocessing is useful."""
    show_section("When multiprocessing helps")

    print("CPU-bound work spends most of its time calculating.")
    print("Examples include image processing, simulations, and math-heavy tasks.")
    print("For tiny tasks, multiprocessing overhead can be larger than the work.")


def main():
    """Run each lesson section in order."""
    demonstrate_single_process()
    explain_cpu_bound_work()
    demonstrate_process_pool()


if __name__ == "__main__":
    main()

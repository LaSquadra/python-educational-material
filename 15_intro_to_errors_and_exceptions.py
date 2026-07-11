# coding: utf-8
"""Lesson 15: Errors and Exceptions.

Errors are Python's way of telling you something went wrong. Exceptions are
error objects that can be handled with `try` and `except`.

Common exception vocabulary:

- `try` runs code that might fail.
- `except` handles a specific kind of failure.
- `else` runs only when no exception happened.
- `finally` runs whether an exception happened or not.
- `raise` creates an exception on purpose.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def divide_numbers(numerator, denominator):
    """Divide two numbers and handle division errors."""
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print(f"{numerator} / {denominator} = {result}")
    finally:
        print("Finished the division attempt.")


def convert_to_integer(text):
    """Convert text to an integer, or explain why it failed."""
    try:
        number = int(text)
    except ValueError:
        print(f"{text!r} cannot be converted into an integer.")
    else:
        print(f"{text!r} became the integer {number}.")


def get_item_at_index(items, index):
    """Read one list item and handle an invalid index."""
    try:
        item = items[index]
    except IndexError:
        print(f"There is no item at index {index}.")
    else:
        print(f"Item at index {index}: {item}")


def calculate_average(scores):
    """Return the average score, raising ValueError for an empty list."""
    if not scores:
        raise ValueError("scores must contain at least one number")

    return sum(scores) / len(scores)


def demonstrate_try_except_else_finally():
    """Show the main parts of exception handling."""
    show_section("try, except, else, and finally")

    divide_numbers(10, 2)
    divide_numbers(10, 0)


def demonstrate_common_exceptions():
    """Show a few common exception types."""
    show_section("Common exceptions")

    convert_to_integer("42")
    convert_to_integer("forty-two")
    get_item_at_index(["red", "green", "blue"], 1)
    get_item_at_index(["red", "green", "blue"], 5)


def demonstrate_raising_exceptions():
    """Raise and handle a simple ValueError."""
    show_section("Raising ValueError")

    try:
        print(f"Average score: {calculate_average([90, 85, 100])}")
        print(f"Average score: {calculate_average([])}")
    except ValueError as error:
        print(f"Could not calculate average: {error}")


def main():
    """Run each lesson section in order."""
    demonstrate_try_except_else_finally()
    demonstrate_common_exceptions()
    demonstrate_raising_exceptions()


if __name__ == "__main__":
    main()

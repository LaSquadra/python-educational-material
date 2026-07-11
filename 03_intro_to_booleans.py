# coding: utf-8
"""Lesson 03: Booleans.

Booleans represent one of two values: `True` or `False`.

Python also treats some values as truthy or falsy when they are checked in a
boolean context, such as an `if` statement.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def create_booleans():
    """Create boolean values directly and from comparisons."""
    show_section("Creating booleans")

    is_student = True
    is_complete = False

    print(f"Is student? {is_student}")
    print(f"Is complete? {is_complete}")
    print(f"Does 5 equal 5? {5 == 5}")
    print(f"Is 2 greater than 10? {2 > 10}")


def inspect_truthy_and_falsy_values():
    """Show common values that become True or False with bool()."""
    show_section("Truthy and falsy values")

    examples = ["hello", "", [1, 2, 3], [], 1, 0, None]

    for value in examples:
        print(f"bool({value!r}) -> {bool(value)}")


def preview_boolean_tools():
    """Show common boolean operators and helpers."""
    show_section("Boolean tools to explore")

    print("Booleans are usually combined with and, or, and not.")
    print(f"True and False -> {True and False}")
    print(f"True or False -> {True or False}")
    print(f"not True -> {not True}")
    print("The bool() function can convert other values to True or False.")


def main():
    """Run each lesson section in order."""
    create_booleans()
    inspect_truthy_and_falsy_values()
    preview_boolean_tools()


if __name__ == "__main__":
    main()

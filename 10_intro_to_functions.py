# coding: utf-8
"""Lesson 10: Functions.

Functions are reusable blocks of code. They help you name a task, avoid
duplicating logic, and organize a program into smaller pieces.

Function vocabulary:

- A parameter is a variable listed in a function definition.
- An argument is a value passed into a function call.
- `return` sends a value back to the code that called the function.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def greet_user(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! How are you today?"


def describe_user(name, age, hobby="learning Python"):
    """Return a sentence that describes a user."""
    return f"{name} is {age} years old and enjoys {hobby}."


def add_numbers(number_1, number_2):
    """Return the sum of two numbers."""
    return number_1 + number_2


def add_numeric_values(values):
    """Add numbers and numeric strings from a list.

    Args:
        values: A list that may contain integers, floats, strings, or other
            values.

    Returns:
        The total of all integers, floats, and numeric strings in `values`.
    """
    total = 0

    for value in values:
        if isinstance(value, (int, float)):
            total += value
        elif isinstance(value, str) and value.isdigit():
            total += float(value)

    return total


def demonstrate_basic_functions():
    """Call simple functions and print their return values."""
    show_section("Basic functions")

    print(greet_user("James"))
    print(describe_user("Robert", 56, hobby="fly fishing"))
    print(f"5 + 10 = {add_numbers(5, 10)}")


def demonstrate_reusable_logic():
    """Use one function with multiple inputs."""
    show_section("Reusable logic")

    first_values = [2, 2, 4, 5, 7, 1, 0, 3, 4, 1, 5]
    second_values = [1, 5, 7, 2, "4", 1, 8, 2, "9", 0, 4.1, 8]

    first_total = add_numeric_values(first_values)
    second_total = add_numeric_values(second_values)

    print(f"First total: {first_total}")
    print(f"Second total: {second_total}")
    print(f"Combined total: {add_numeric_values([first_total, second_total])}")


def main():
    """Run each lesson section in order."""
    demonstrate_basic_functions()
    demonstrate_reusable_logic()


if __name__ == "__main__":
    main()

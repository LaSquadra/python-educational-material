# coding: utf-8
"""Lesson 11: Functions.

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


def total_scores(scores):
    """Return the total of a list of scores."""
    total = 0

    for score in scores:
        total += score

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

    first_scores = [2, 2, 4, 5, 7, 1, 0, 3, 4, 1, 5]
    second_scores = [1, 5, 7, 2, 4, 1, 8, 2, 9, 0, 4, 8]

    first_total = total_scores(first_scores)
    second_total = total_scores(second_scores)

    print(f"First total: {first_total}")
    print(f"Second total: {second_total}")
    print(f"Combined total: {add_numbers(first_total, second_total)}")


def main():
    """Run each lesson section in order."""
    demonstrate_basic_functions()
    demonstrate_reusable_logic()


if __name__ == "__main__":
    main()

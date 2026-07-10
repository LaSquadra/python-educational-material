# coding: utf-8
"""Lesson 04: Comparison Operators.

Comparison operators compare two values and return a boolean result.

Common comparison operators:

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

Use `==` when comparing values. The `is` operator checks whether two variables
refer to the same object in memory, which is a different idea.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def compare_strings():
    """Compare string values."""
    show_section("Comparing strings")

    first_word = "Hello"
    second_word = "World"

    print(f"{first_word!r} == {second_word!r}: {first_word == second_word}")
    print(f"{first_word!r} != {second_word!r}: {first_word != second_word}")


def compare_numbers():
    """Compare number values."""
    show_section("Comparing numbers")

    score = 85
    passing_score = 70

    print(f"{score} > {passing_score}: {score > passing_score}")
    print(f"{score} >= {passing_score}: {score >= passing_score}")
    print(f"{score} < 100: {score < 100}")
    print(f"{score} <= 100: {score <= 100}")


def compare_types():
    """Show that equal-looking values can have different types."""
    show_section("Comparing types")

    number_five = 5
    string_five = "5"

    print(f"5 == '5': {number_five == string_five}")
    print(f"5 == int('5'): {number_five == int(string_five)}")


def main():
    """Run each lesson section in order."""
    compare_strings()
    compare_numbers()
    compare_types()


if __name__ == "__main__":
    main()

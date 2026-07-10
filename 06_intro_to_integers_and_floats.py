# coding: utf-8
"""Lesson 06: Integers and Floats.

Integers are whole numbers. Floats are numbers with decimal points.

Both types can be used in math expressions. Division with `/` always returns a
float, while floor division with `//` keeps only the whole-number result.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def inspect_numbers():
    """Create integer and float values."""
    show_section("Integer and float values")

    age = 35
    rating = 4.5

    print(f"age = {age}, type = {type(age)}")
    print(f"rating = {rating}, type = {type(rating)}")


def format_numbers_in_strings():
    """Place numbers inside readable output."""
    show_section("Formatting numbers")

    age = 35

    print("Age:", age)
    print("Age: " + str(age))
    print(f"Age: {age}")


def calculate_with_numbers():
    """Use common math operators."""
    show_section("Math operators")

    number_1 = 5
    number_2 = 10

    print(f"{number_1} + {number_2} = {number_1 + number_2}")
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
    print(f"{number_1} / {number_2} = {number_1 / number_2}")
    print(f"{number_1} ** {number_2} = {number_1 ** number_2}")
    print(f"{number_1} % {number_2} = {number_1 % number_2}")
    print(f"{number_1} // {number_2} = {number_1 // number_2}")


def main():
    """Run each lesson section in order."""
    inspect_numbers()
    format_numbers_in_strings()
    calculate_with_numbers()


if __name__ == "__main__":
    main()

# coding: utf-8
"""Lesson 00: Summary of Basic Data Types.

This lesson introduces the data types students will see throughout the course:

- Strings: text values, written with quotes.
- Integers: whole numbers.
- Floats: numbers with decimal points.
- Booleans: True or False values.
- Lists: ordered, changeable collections.
- Tuples: ordered, unchangeable collections.
- Sets: unordered collections of unique values.
- Dictionaries: key-value collections.

Run this file to see small examples of each type.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def introduce_comments():
    """Explain comments and docstrings."""
    show_section("Comments and docstrings")

    # This is a comment. Python ignores comments when the program runs.
    print("Comments start with # and help explain code to humans.")
    print("Docstrings use triple quotes and document files, classes, or functions.")


def introduce_strings():
    """Show how strings store text."""
    show_section("Strings")

    first_name = "Ada"
    greeting = "Hello, " + first_name

    print(greeting)
    print("A string can use single quotes or double quotes.")
    print(f"The first character in {first_name!r} is {first_name[0]!r}.")
    print("Python starts counting indexes at 0.")


def introduce_numbers():
    """Show how integers and floats store numbers."""
    show_section("Integers and floats")

    student_count = 12
    average_score = 91.5

    print(f"Integer example: {student_count}")
    print(f"Float example: {average_score}")
    print(f"Addition: 3 + 2 = {3 + 2}")
    print(f"Division: 5 / 2 = {5 / 2}")
    print(f"Floor division: 5 // 2 = {5 // 2}")
    print(f"Modulus: 5 % 2 = {5 % 2}")


def introduce_booleans():
    """Show how booleans represent yes/no or true/false ideas."""
    show_section("Booleans")

    is_logged_in = True
    has_missing_homework = False

    print(f"Is logged in? {is_logged_in}")
    print(f"Has missing homework? {has_missing_homework}")
    print(f"Is 10 greater than 3? {10 > 3}")


def introduce_lists():
    """Show how lists store ordered, changeable data."""
    show_section("Lists")

    favorite_languages = ["Python", "JavaScript", "SQL"]
    favorite_languages.append("HTML")

    print(favorite_languages)
    print(f"First item: {favorite_languages[0]}")
    print(f"Last item: {favorite_languages[-1]}")


def introduce_tuples():
    """Show how tuples store ordered data that should not change."""
    show_section("Tuples")

    screen_size = (1920, 1080)

    print(f"Screen size: {screen_size}")
    print(f"Width: {screen_size[0]}")
    print(f"Height: {screen_size[1]}")


def introduce_sets():
    """Show how sets store unique values."""
    show_section("Sets")

    submitted_names = {"Avery", "Blake", "Avery", "Casey"}

    print(submitted_names)
    print("The duplicate 'Avery' appears only once.")
    print("Sets are useful when each value should be unique.")


def introduce_dictionaries():
    """Show how dictionaries connect keys to values."""
    show_section("Dictionaries")

    student = {
        "first_name": "Ada",
        "last_name": "Lovelace",
        "course": "Python Basics",
        "current_lesson": 0,
    }

    print(student)
    print(f"Student name: {student['first_name']} {student['last_name']}")
    print(f"Course: {student['course']}")


def main():
    """Run each lesson section in order."""
    introduce_comments()
    introduce_strings()
    introduce_numbers()
    introduce_booleans()
    introduce_lists()
    introduce_tuples()
    introduce_sets()
    introduce_dictionaries()


if __name__ == "__main__":
    main()

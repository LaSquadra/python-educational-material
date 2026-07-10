# coding: utf-8
"""Lesson 01: Variables.

Variables store values so you can reuse them later in a program.

Good variable names are:

- descriptive: `student_age` is clearer than `x`
- lowercase: `first_name`, not `FirstName`
- separated with underscores: `favorite_color`
- not started with a number: `lesson_1`, not `1_lesson`

Run this file to see variables created, printed, and reassigned.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def create_variables():
    """Create variables that store different kinds of values."""
    show_section("Creating variables")

    first_name = "Ada"
    current_lesson = 1
    is_learning_python = True

    print(f"Name: {first_name}")
    print(f"Current lesson: {current_lesson}")
    print(f"Learning Python? {is_learning_python}")


def reassign_variables():
    """Show that a variable can point to a new value later."""
    show_section("Reassigning variables")

    score = 80
    print(f"Starting score: {score}")

    score = 95
    print(f"Updated score: {score}")


def inspect_variable_types():
    """Use type() to inspect the kind of data stored in a variable."""
    show_section("Inspecting types")

    course_name = "Python Basics"
    lesson_count = 13
    average_score = 91.5

    print(f"{course_name!r} is a {type(course_name)}")
    print(f"{lesson_count!r} is a {type(lesson_count)}")
    print(f"{average_score!r} is a {type(average_score)}")


def main():
    """Run each lesson section in order."""
    create_variables()
    reassign_variables()
    inspect_variable_types()


if __name__ == "__main__":
    main()

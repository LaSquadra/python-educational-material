# coding: utf-8
"""Lesson 05: Flow Control and Conditionals.

Conditionals let a program choose which code to run.

The most common conditional keywords are:

- `if`: run this block when the condition is true
- `elif`: check another condition when earlier conditions were false
- `else`: run this block when none of the earlier conditions were true
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def check_a_single_condition():
    """Use if and else to choose between two paths."""
    show_section("Single condition")

    temperature = 72

    if temperature >= 70:
        print("It is warm enough to go outside.")
    else:
        print("Bring a jacket.")


def check_multiple_conditions():
    """Use if, elif, and else to choose between several paths."""
    show_section("Multiple conditions")

    score = 88

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "Needs more practice"

    print(f"Score: {score}")
    print(f"Grade: {grade}")


def combine_conditions():
    """Use and, or, and not with conditionals."""
    show_section("Combining conditions")

    has_username = True
    has_password = True
    is_locked = False

    if has_username and has_password and not is_locked:
        print("Login can continue.")
    else:
        print("Login cannot continue.")


def nest_conditions():
    """Show a simple nested conditional."""
    show_section("Nested conditions")

    is_logged_in = True
    is_admin = False

    if is_logged_in:
        if is_admin:
            print("Show the admin dashboard.")
        else:
            print("Show the student dashboard.")
    else:
        print("Ask the user to log in.")


def main():
    """Run each lesson section in order."""
    check_a_single_condition()
    check_multiple_conditions()
    combine_conditions()
    nest_conditions()


if __name__ == "__main__":
    main()

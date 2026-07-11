# coding: utf-8
"""Lesson 09: Loops.

Loops repeat code.

- `for` loops are useful when you have a known sequence to iterate through.
- `while` loops are useful when repetition should continue until a condition
  changes.
- `range()` creates a sequence of numbers that a `for` loop can use.
- `break` exits a loop early.
- `continue` skips the rest of the current loop iteration.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def loop_over_a_list():
    """Use a for loop with a list."""
    show_section("For loop with a list")

    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        print(number)


def loop_over_a_string():
    """Use a for loop with a string."""
    show_section("For loop with a string")

    word = "Python"

    for character in word:
        print(character)


def use_a_while_loop():
    """Use a while loop with a changing condition."""
    show_section("While loop")

    counter = 0

    while counter < 5:
        print(counter)
        counter += 1


def use_range():
    """Use range() to create a simple sequence of numbers."""
    show_section("Using range")

    for number in range(5):
        print(number)

    print("range(5) gives the loop 0, 1, 2, 3, and 4.")


def use_break():
    """Stop a loop as soon as the target value is found."""
    show_section("Using break")

    secret_number = 8

    for number in range(10):
        if number == secret_number:
            print(f"You found it! The number was {number}.")
            break
        print("Still searching...")


def use_continue():
    """Skip work for values that do not match the target."""
    show_section("Using continue")

    secret_number = 8

    for number in range(10):
        if number != secret_number:
            continue
        print(f"You found it! The number was {number}.")


def main():
    """Run each lesson section in order."""
    loop_over_a_list()
    loop_over_a_string()
    use_a_while_loop()
    use_range()
    use_break()
    use_continue()


if __name__ == "__main__":
    main()

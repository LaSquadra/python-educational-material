# coding: utf-8
"""Lesson 07: Lists.

Lists store ordered collections of values. They are mutable, which means you can
change their contents after the list is created.

Lists use square brackets and comma-separated values:

`favorite_numbers = [3, 7, 11]`
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def create_and_index_lists():
    """Create a list and access values by index."""
    show_section("Creating and indexing lists")

    languages = ["Python", "JavaScript", "SQL"]

    print(languages)
    print(f"First item: {languages[0]}")
    print(f"Last item: {languages[-1]}")


def change_lists():
    """Use common methods that modify a list."""
    show_section("Changing lists")

    tasks = ["read", "practice", "review"]

    tasks.append("quiz")
    print(f"After append: {tasks}")

    tasks.insert(1, "take notes")
    print(f"After insert: {tasks}")

    tasks.remove("review")
    print(f"After remove: {tasks}")

    completed_task = tasks.pop(0)
    print(f"Popped task: {completed_task}")
    print(f"Remaining tasks: {tasks}")


def sort_and_copy_lists():
    """Sort a list and create a real copy."""
    show_section("Sorting and copying lists")

    scores = [88, 100, 72, 91]
    copied_scores = scores.copy()

    scores.sort()

    print(f"Sorted scores: {scores}")
    print(f"Copied before sort: {copied_scores}")


def slice_lists():
    """Use slices to access part of a list."""
    show_section("Slicing lists")

    letters = ["a", "b", "c", "d", "e"]

    print(f"First three letters: {letters[:3]}")
    print(f"Every other letter: {letters[::2]}")
    print(f"Reversed letters: {letters[::-1]}")


def main():
    """Run each lesson section in order."""
    create_and_index_lists()
    change_lists()
    sort_and_copy_lists()
    slice_lists()


if __name__ == "__main__":
    main()

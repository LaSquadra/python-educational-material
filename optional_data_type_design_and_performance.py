# coding: utf-8
"""Optional Lesson: Data Type Design and Performance.

Good Python code is not only about getting the right answer. As programs grow,
the data types you choose can affect:

- how clearly the code communicates its purpose
- how much memory the program uses
- how quickly the program can find, add, or change values
- how easy the program is to maintain later

This lesson introduces practical tradeoffs. The exact speed and memory numbers
can change by computer and Python version, so focus on the patterns.
"""

import sys
import time


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def explain_big_picture():
    """Explain the design questions behind choosing a data type."""
    show_section("Big picture")

    print("Before choosing a data type, ask questions like these:")
    print("- Do I need to keep values in order?")
    print("- Do I need to change the collection after creating it?")
    print("- Do I need fast lookups by key or membership?")
    print("- Do I need to prevent duplicates?")
    print("- Do I care more about readability, speed, or memory?")


def compare_memory_footprint():
    """Compare approximate memory use for similar collections."""
    show_section("Approximate memory footprint")

    favorite_numbers_list = [3, 7, 11, 19, 23]
    favorite_numbers_tuple = (3, 7, 11, 19, 23)
    favorite_numbers_set = {3, 7, 11, 19, 23}
    favorite_numbers_dict = {
        "first": 3,
        "second": 7,
        "third": 11,
        "fourth": 19,
        "fifth": 23,
    }

    print(f"List size: {sys.getsizeof(favorite_numbers_list)} bytes")
    print(f"Tuple size: {sys.getsizeof(favorite_numbers_tuple)} bytes")
    print(f"Set size: {sys.getsizeof(favorite_numbers_set)} bytes")
    print(f"Dictionary size: {sys.getsizeof(favorite_numbers_dict)} bytes")
    print("sys.getsizeof() is useful for comparison, not a full memory audit.")


def time_membership_checks():
    """Compare membership checks in a list and a set."""
    show_section("Retrieval speed: list vs set membership")

    numbers_list = list(range(100_000))
    numbers_set = set(numbers_list)
    target = 99_999

    start_time = time.perf_counter()
    target in numbers_list
    list_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    target in numbers_set
    set_time = time.perf_counter() - start_time

    print(f"List membership check: {list_time:.8f} seconds")
    print(f"Set membership check:  {set_time:.8f} seconds")
    print("Lists may scan many values. Sets are designed for fast membership.")


def compare_lookup_styles():
    """Show why dictionaries are useful for direct lookup by key."""
    show_section("Retrieval speed: scanning vs dictionary lookup")

    students = [
        {"id": 1, "name": "Ada"},
        {"id": 2, "name": "Grace"},
        {"id": 3, "name": "Katherine"},
    ]
    students_by_id = {
        1: "Ada",
        2: "Grace",
        3: "Katherine",
    }

    target_id = 3

    found_name = None
    for student in students:
        if student["id"] == target_id:
            found_name = student["name"]

    direct_name = students_by_id[target_id]

    print(f"Found by scanning list: {found_name}")
    print(f"Found by dictionary key: {direct_name}")
    print("A dictionary is often clearer and faster when you already know the key.")


def explain_mutability_tradeoffs():
    """Explain how mutability affects design choices."""
    show_section("Mutability and design")

    print("Mutable means a value can be changed after it is created.")
    print("Lists, sets, and dictionaries are mutable.")
    print("Strings, integers, floats, booleans, and tuples are immutable.")
    print("Use immutable values when you want data to stay stable.")
    print("Use mutable collections when your program needs to update data.")


def choose_data_type_examples():
    """Give practical examples of choosing one data type over another."""
    show_section("Choosing a data type")

    print("Use a string for text: a name, message, file path, or API response.")
    print("Use an integer for counting whole things.")
    print("Use a float for measurements, averages, and decimal values.")
    print("Use a list when order matters and items may change.")
    print("Use a tuple when ordered values belong together and should not change.")
    print("Use a set when uniqueness or fast membership checks matter.")
    print("Use a dictionary when each value should be found by a meaningful key.")


def explain_common_efficiency_patterns():
    """Summarize useful patterns for better performance and smaller code."""
    show_section("Common efficiency patterns")

    print("Avoid scanning a long list repeatedly if a dictionary lookup will do.")
    print("Use a set to remove duplicates or ask 'have I seen this before?'")
    print("Use a tuple for stable records that should not be edited accidentally.")
    print("Keep data structures simple until there is a real reason to optimize.")
    print("Measure before optimizing: guesses about performance are often wrong.")


def main():
    """Run each lesson section in order."""
    explain_big_picture()
    compare_memory_footprint()
    time_membership_checks()
    compare_lookup_styles()
    explain_mutability_tradeoffs()
    choose_data_type_examples()
    explain_common_efficiency_patterns()


if __name__ == "__main__":
    main()

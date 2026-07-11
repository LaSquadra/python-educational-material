# coding: utf-8
"""Lesson 08: Tuples and Sets.

Tuples and sets are collection types, like lists, but they solve different
problems.

- A tuple stores ordered values that should stay together and not change.
- A set stores unique values and is useful for membership checks.

Tuples use parentheses:

`screen_size = (1920, 1080)`

Sets use curly braces:

`submitted_names = {"Avery", "Blake", "Casey"}`
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def create_and_index_tuples():
    """Create tuples and read values by index."""
    show_section("Creating and indexing tuples")

    coordinates = (10, 25)
    student_record = ("Ada", "Python Basics", 8)

    print(f"Coordinates: {coordinates}")
    print(f"X value: {coordinates[0]}")
    print(f"Y value: {coordinates[1]}")
    print(f"Student name: {student_record[0]}")
    print("Tuples are useful when values belong together as one record.")


def use_tuple_methods():
    """Use common tuple methods."""
    show_section("Tuple methods")

    quiz_scores = (100, 90, 100, 85)

    print(f"Scores: {quiz_scores}")
    print(f"How many 100s? {quiz_scores.count(100)}")
    print(f"Where is 85? Index {quiz_scores.index(85)}")
    print("Tuples have fewer methods than lists because tuples do not change.")


def create_and_update_sets():
    """Create sets and add or remove unique values."""
    show_section("Creating and updating sets")

    submitted_names = {"Avery", "Blake", "Avery", "Casey"}

    print(f"Submitted names: {submitted_names}")
    print("The duplicate 'Avery' appears only once.")

    submitted_names.add("Dakota")
    print(f"After .add('Dakota'): {submitted_names}")

    submitted_names.discard("Blake")
    print(f"After .discard('Blake'): {submitted_names}")


def use_set_operations():
    """Compare sets with common set operations."""
    show_section("Set operations")

    python_students = {"Avery", "Casey", "Dakota"}
    data_students = {"Blake", "Casey", "Emery"}

    print(f"Python students: {python_students}")
    print(f"Data students: {data_students}")
    print(f"Union: {python_students.union(data_students)}")
    print(f"Intersection: {python_students.intersection(data_students)}")
    print(f"Only Python: {python_students.difference(data_students)}")


def preview_more_tuple_and_set_tools():
    """List more tuple and set tools to explore."""
    show_section("More tuple and set tools to explore")

    print("Tuple tools: .count(), .index(), len(tuple_value)")
    print("Set tools: .add(), .discard(), .remove(), .union()")
    print("More set tools: .intersection(), .difference(), .issubset()")


def main():
    """Run each lesson section in order."""
    create_and_index_tuples()
    use_tuple_methods()
    create_and_update_sets()
    use_set_operations()
    preview_more_tuple_and_set_tools()


if __name__ == "__main__":
    main()

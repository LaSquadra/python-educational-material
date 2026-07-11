# coding: utf-8
"""Lesson 10: Dictionaries.

Dictionaries store key-value pairs. A key is used to look up a value.

Dictionary keys are often strings, but they can be any hashable type. In this
course, string keys are the clearest choice for beginner-friendly examples.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def create_dictionary():
    """Create a dictionary and access values by key."""
    show_section("Creating dictionaries")

    student = {
        "name": "Ada Lovelace",
        "age": 28,
        "course": "Python Basics",
    }

    print(student)
    print(f"Name: {student['name']}")
    print(f"Course: {student['course']}")
    print(f"Missing grade with fallback: {student.get('grade', 'not assigned')}")


def update_dictionary():
    """Add and change dictionary values."""
    show_section("Updating dictionaries")

    student = {"name": "Ada Lovelace", "lesson": 9}

    student["lesson"] = 10
    student["status"] = "in progress"
    student.update({"mentor": "Grace Hopper"})

    print(student)


def loop_over_dictionary():
    """Loop through dictionary keys and values."""
    show_section("Looping through dictionaries")

    student = {
        "name": "Ada Lovelace",
        "age": 28,
        "course": "Python Basics",
    }

    print("The .items() method gives each key and value together.")
    print(f"Keys: {student.keys()}")
    print(f"Values: {student.values()}")

    for key, value in student.items():
        print(f"{key}: {value}")


def use_nested_dictionaries():
    """Store dictionaries inside another dictionary."""
    show_section("Nested dictionaries")

    users = {
        "student_1": {"name": "John Doe", "age": 45, "job": "Postal Worker"},
        "student_2": {"name": "Bruce Wayne", "age": 41, "job": "Detective"},
    }

    print(f"Student 2 age: {users['student_2']['age']}")
    print(users)


def preview_more_dictionary_methods():
    """List more common dictionary methods to explore."""
    show_section("More dictionary methods to explore")

    settings = {"theme": "dark", "font_size": 14, "autosave": True}
    removed_value = settings.pop("autosave")

    print(f"After .pop('autosave'): {settings}")
    print(f"Removed value: {removed_value}")
    print("Other useful methods: .clear(), .copy(), .setdefault()")


def main():
    """Run each lesson section in order."""
    create_dictionary()
    update_dictionary()
    loop_over_dictionary()
    use_nested_dictionaries()
    preview_more_dictionary_methods()


if __name__ == "__main__":
    main()

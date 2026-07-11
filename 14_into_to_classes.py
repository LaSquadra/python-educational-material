# coding: utf-8
"""Lesson 14: Classes.

Classes let you define your own types of objects. An object can store data in
attributes and use functions called methods.

Class vocabulary:

- A class is the blueprint.
- An instance is one object created from the class.
- `__init__` runs when a new instance is created.
- `self` refers to the current instance.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


class Student:
    """Represent a student in a Python course."""

    def __init__(self, name, current_lesson=1):
        """Create a student with a name and current lesson number."""
        self.name = name
        self.current_lesson = current_lesson

    def describe(self):
        """Return a readable description of the student."""
        return f"{self.name} is on lesson {self.current_lesson}."

    def advance_lesson(self):
        """Move the student forward by one lesson."""
        self.current_lesson += 1


class Course:
    """Represent a course that can contain multiple students."""

    def __init__(self, title):
        """Create a course with a title and an empty student list."""
        self.title = title
        self.students = []

    def add_student(self, student):
        """Add a student to the course."""
        self.students.append(student)

    def list_students(self):
        """Print each student currently in the course."""
        for student in self.students:
            print(student.describe())


def inspect_a_builtin_class():
    """Show that built-in types are classes too."""
    show_section("Built-in classes")

    print(f"type(5): {type(5)}")
    print(f"type('Python'): {type('Python')}")
    print("Built-in values come from classes too.")


def create_custom_objects():
    """Create and use instances of custom classes."""
    show_section("Custom classes")

    student = Student("Ada", current_lesson=14)

    print(student.describe())
    student.advance_lesson()
    print(student.describe())


def compose_objects():
    """Store objects inside another object."""
    show_section("Objects working together")

    course = Course("Python Basics")
    course.add_student(Student("Ada", current_lesson=14))
    course.add_student(Student("Grace", current_lesson=11))

    print(f"Course: {course.title}")
    course.list_students()


def main():
    """Run each lesson section in order."""
    inspect_a_builtin_class()
    create_custom_objects()
    compose_objects()


if __name__ == "__main__":
    main()

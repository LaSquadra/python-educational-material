# coding: utf-8
"""Lesson 17: JSON.

JSON is a text format for storing and sending data. It is common in web APIs,
configuration files, and data exports.

JSON looks a lot like Python dictionaries and lists, but it is still text.
Python's `json` module converts between JSON strings and Python values.

Common conversions:

- `json.loads()` converts a JSON string into Python data.
- `json.dumps()` converts Python data into a JSON string.
- `json.load()` reads JSON from a file.
- `json.dump()` writes JSON to a file.
"""

import json
from pathlib import Path


LESSON_DIRECTORY = Path(__file__).parent
DEMO_FILE = LESSON_DIRECTORY / "demo_student.json"


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def demonstrate_json_string_vs_python_data():
    """Compare a JSON string with Python dictionaries and lists."""
    show_section("JSON strings and Python data")

    json_text = '{"name": "Ada", "lesson": 17, "topics": ["JSON", "files"]}'
    python_data = {"name": "Ada", "lesson": 17, "topics": ["JSON", "files"]}

    print(f"JSON text type: {type(json_text)}")
    print(f"Python data type: {type(python_data)}")
    print(f"Student name from Python data: {python_data['name']}")


def parse_json_string():
    """Convert a JSON string into Python data with json.loads."""
    show_section("Reading JSON with loads")

    json_text = '{"name": "Grace", "active": true, "scores": [95, 87, 100]}'
    student = json.loads(json_text)

    print(f"Student dictionary: {student}")
    print(f"Student active value: {student['active']}")
    print(f"First score: {student['scores'][0]}")


def create_json_string():
    """Convert Python data into a JSON string with json.dumps."""
    show_section("Writing JSON with dumps")

    student = {
        "name": "Katherine",
        "lesson": 17,
        "completed_topics": ["strings", "lists", "dictionaries"],
    }
    json_text = json.dumps(student, indent=2)

    print(json_text)


def write_json_file():
    """Write Python data to a local JSON demo file."""
    show_section("Writing a JSON file")

    student = {
        "name": "Alan",
        "lesson": 17,
        "ready_for_apis": True,
    }

    with open(DEMO_FILE, "w", encoding="utf-8") as file:
        json.dump(student, file, indent=2)

    print(f"Wrote JSON data to {DEMO_FILE.name}.")


def read_json_file():
    """Read Python data from a local JSON demo file."""
    show_section("Reading a JSON file")

    with open(DEMO_FILE, "r", encoding="utf-8") as file:
        student = json.load(file)

    print(f"Read student: {student['name']}")
    print(f"Ready for APIs? {student['ready_for_apis']}")


def main():
    """Run each lesson section in order."""
    demonstrate_json_string_vs_python_data()
    parse_json_string()
    create_json_string()
    write_json_file()
    read_json_file()


if __name__ == "__main__":
    main()

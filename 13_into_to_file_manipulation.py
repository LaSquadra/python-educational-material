# coding: utf-8
"""Lesson 13: File Manipulation.

Python can read from and write to files. The `pathlib` module helps build file
paths in a way that works across operating systems.

Common file modes:

- `"r"` reads an existing file.
- `"w"` writes a file, replacing any existing contents.
- `"a"` appends new text to the end of a file.

Use `with open(...) as file:` so Python closes the file automatically.
"""

from pathlib import Path


LESSON_DIRECTORY = Path(__file__).parent
DEMO_FILE = LESSON_DIRECTORY / "temp_file.txt"
README_FILE = LESSON_DIRECTORY / "README.md"


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def read_file():
    """Read a few lines from README.md."""
    show_section("Reading a file")

    with open(README_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print(f"Read {len(lines)} lines from {README_FILE.name}.")
    print(f"First line: {lines[0].strip()}")


def write_file():
    """Write text to a demo file."""
    show_section("Writing a file")

    text = "You can write text to a file.\nEach newline creates a new line.\n"

    with open(DEMO_FILE, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"Wrote demo text to {DEMO_FILE.name}.")


def append_file():
    """Append text to the demo file."""
    show_section("Appending to a file")

    with open(DEMO_FILE, "a", encoding="utf-8") as file:
        file.write("This line was appended later.\n")

    print(f"Appended one line to {DEMO_FILE.name}.")


def main():
    """Run each lesson section in order."""
    read_file()
    write_file()
    append_file()


if __name__ == "__main__":
    main()

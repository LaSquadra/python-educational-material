# coding: utf-8
"""Lesson 11: Imports.

Imports let your program use code from another module.

Common import styles:

- `import pathlib` imports the module.
- `from pathlib import Path` imports a specific name from the module.

Keep imports near the top of the file so readers can quickly see what the file
depends on.
"""

import math
import pathlib
from pathlib import Path


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def import_whole_module():
    """Use a name from a module imported with `import module`."""
    show_section("Importing a whole module")

    current_directory = pathlib.Path.cwd()
    print(f"Current directory: {current_directory}")


def import_specific_name():
    """Use a name imported with `from module import name`."""
    show_section("Importing a specific name")

    current_directory = Path.cwd()
    print(f"Current directory: {current_directory}")


def use_standard_library_module():
    """Use a standard library module that ships with Python."""
    show_section("Using the standard library")

    radius = 3
    area = math.pi * radius ** 2

    print(f"Circle radius: {radius}")
    print(f"Circle area: {area:.2f}")


def main():
    """Run each lesson section in order."""
    import_whole_module()
    import_specific_name()
    use_standard_library_module()


if __name__ == "__main__":
    main()

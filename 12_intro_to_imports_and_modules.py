# coding: utf-8
"""Lesson 12: Imports and Modules.

Imports let your program use code from another module.

In Python, a module is a file that contains Python code. For example,
`pathlib.py` is a module in the standard library. Your own `.py` files can be
modules too.

Common import styles:

- `import pathlib` imports the module.
- `from pathlib import Path` imports a specific name from the module.

The `if __name__ == "__main__":` pattern lets a file behave differently when it
is run directly compared with when it is imported as a module.

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


def explain_name_main_guard():
    """Explain why scripts often use the __name__ guard."""
    show_section("The __name__ guard")

    print(f"This file's __name__ value is: {__name__!r}")
    print("When a file is run directly, __name__ is '__main__'.")
    print("When a file is imported, __name__ is usually the module name.")
    print("The guard below runs main() only when this file is run directly:")
    print('  if __name__ == "__main__":')
    print("      main()")


def compare_modules_and_classes():
    """Compare modules with classes at a beginner-friendly level."""
    show_section("Modules and classes")

    print("A module is a Python file that groups related code.")
    print("A class is a blueprint for creating objects.")
    print("Example module: math")
    print("Example class from pathlib: Path")
    print("You import modules or names from modules.")
    print("You create objects from classes when you need that kind of value.")


def main():
    """Run each lesson section in order."""
    import_whole_module()
    import_specific_name()
    use_standard_library_module()
    explain_name_main_guard()
    compare_modules_and_classes()


if __name__ == "__main__":
    main()

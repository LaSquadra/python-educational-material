# coding: utf-8
"""Lesson 19: Environment variables.

Environment variables are named values stored outside your Python code. They
are often used for settings that can change between computers, such as a
username, a debug flag, or an API key.

Important safety idea:

- Secrets, passwords, and API keys should not be hardcoded in Python files.
- Code can read those values from the environment instead.
- This lesson uses safe demo values only.
"""

import os


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def read_existing_environment():
    """Read a few common environment variables safely."""
    show_section("Reading environment variables")

    username = os.environ.get("USERNAME") or os.environ.get("USER")
    home_directory = os.environ.get("USERPROFILE") or os.environ.get("HOME")

    print(f"Username from environment: {username or 'not set'}")
    print(f"Home directory from environment: {home_directory or 'not set'}")


def read_optional_setting():
    """Use a fallback when an optional environment variable is missing."""
    show_section("Optional settings with fallbacks")

    lesson_mode = os.environ.get("PYTHON_LESSON_MODE", "practice")

    print(f"PYTHON_LESSON_MODE: {lesson_mode}")
    print("The fallback value is used when the variable is not set.")


def demonstrate_secret_pattern():
    """Show the pattern for reading a secret without hardcoding it."""
    show_section("Secrets should not be hardcoded")

    api_key = os.environ.get("EXAMPLE_API_KEY")

    if api_key:
        print("EXAMPLE_API_KEY is set.")
        print("A real program could use it without printing the secret value.")
    else:
        print("EXAMPLE_API_KEY is not set.")
        print("Using a safe demo fallback instead of a real secret.")


def show_shell_examples():
    """Print shell commands a user could run outside Python."""
    show_section("Setting environment variables")

    print("PowerShell example:")
    print("$env:PYTHON_LESSON_MODE = 'review'")
    print()
    print("Command Prompt example:")
    print("set PYTHON_LESSON_MODE=review")
    print()
    print("macOS/Linux shell example:")
    print("export PYTHON_LESSON_MODE=review")
    print()
    print("Environment variable syntax changes by shell, but Python reads")
    print("the value the same way with os.environ.get().")


def main():
    """Run each lesson section in order."""
    read_existing_environment()
    read_optional_setting()
    demonstrate_secret_pattern()
    show_shell_examples()


if __name__ == "__main__":
    main()

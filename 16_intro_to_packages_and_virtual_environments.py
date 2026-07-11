# coding: utf-8
"""Lesson 16: Packages and Virtual Environments.

Python comes with a standard library, but many projects also use packages made
by other people. `pip` installs packages, and a virtual environment keeps one
project's packages separate from another project's packages.

Important package vocabulary:

- A package is reusable Python code that can be installed.
- `pip` is Python's package installer.
- `python -m pip` runs pip with the Python interpreter you chose.
- `venv` creates an isolated virtual environment for a project.
- `requirements.txt` is a common file for listing packages a project needs.

This lesson prints commands instead of running them, because creating
environments and installing packages should be done intentionally.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def explain_why_virtual_environments_help():
    """Explain the problem virtual environments solve."""
    show_section("Why virtual environments help")

    print("Project A might need package version 1.0.")
    print("Project B might need package version 2.0.")
    print("A virtual environment lets each project keep its own installed packages.")


def print_virtual_environment_commands():
    """Print common venv commands without executing them."""
    show_section("Creating and activating a venv")

    print("Create a virtual environment:")
    print("  python -m venv .venv")
    print()
    print("Activate it on Windows PowerShell:")
    print("  .venv\\Scripts\\Activate.ps1")
    print()
    print("Activate it on macOS or Linux:")
    print("  source .venv/bin/activate")


def print_pip_commands():
    """Print common pip commands without installing anything."""
    show_section("Installing packages with pip")

    print("Upgrade pip:")
    print("  python -m pip install --upgrade pip")
    print()
    print("Install one package:")
    print("  python -m pip install requests")
    print()
    print("See installed packages:")
    print("  python -m pip list")


def explain_requirements_files():
    """Show how requirements.txt is used."""
    show_section("requirements.txt")

    requirements_text = "requests==2.32.3\npytest==8.2.2"

    print("A requirements.txt file might contain:")
    print(requirements_text)
    print()
    print("Install everything listed in that file:")
    print("  python -m pip install -r requirements.txt")


def explain_importing_after_install():
    """Explain that installed packages can be imported in Python code."""
    show_section("Imports after install")

    print("After installing a package, Python code can import it.")
    print("For example, after installing requests:")
    print("  import requests")
    print()
    print("This lesson does not import requests because it is not in the standard library.")


def main():
    """Run each lesson section in order."""
    explain_why_virtual_environments_help()
    print_virtual_environment_commands()
    print_pip_commands()
    explain_requirements_files()
    explain_importing_after_install()


if __name__ == "__main__":
    main()

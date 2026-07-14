# Lesson 16 Notes: Packages And Virtual Environments

Packages let you use code written by other people. Virtual environments keep
each project's packages separate.

## Big Idea

Python includes a standard library, but many useful tools are installed
separately. `pip` installs those tools.

A virtual environment is a project-specific Python environment. It helps avoid
one project's package versions interfering with another project's versions.

## Why Use `python -m pip`

Running pip as a module:

```text
python -m pip install requests
```

helps ensure pip belongs to the Python interpreter you are using. On macOS or
Linux, the command may be:

```text
python3 -m pip install requests
```

## Platform Differences

Virtual environment activation differs by shell:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows Command Prompt: `.venv\Scripts\activate.bat`
- macOS/Linux: `source .venv/bin/activate`

The idea is the same: activate the environment before installing packages for
that project.

## requirements.txt

A `requirements.txt` file records package dependencies so another person can
install the same tools.

## Common Beginner Mistakes

- Installing packages globally when a virtual environment would be safer.
- Forgetting to activate the environment.
- Using `python` when the system expects `python3`.
- Forgetting to list new dependencies in `requirements.txt`.

# coding: utf-8
"""Lesson 02: Strings.

Strings store text. They are written with quotes and can be indexed, sliced,
combined, formatted, and transformed with string methods.

Strings are immutable, which means string methods return new strings instead of
changing the original string in place.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def create_strings():
    """Create strings with single and double quotes."""
    show_section("Creating strings")

    single_quoted = 'This uses single quotes.'
    double_quoted = "This uses double quotes."

    print(single_quoted)
    print(double_quoted)


def combine_strings():
    """Combine strings with concatenation and f-strings."""
    show_section("Combining strings")

    first_name = "Ada"
    last_name = "Lovelace"
    full_name = first_name + " " + last_name

    print(full_name)
    print(f"Hello, {full_name}!")


def use_string_methods():
    """Use common string methods."""
    show_section("String methods")

    message = "  Python is fun  "

    print(f"Original: {message!r}")
    print(f"Uppercase: {message.upper()!r}")
    print(f"Lowercase: {message.lower()!r}")
    print(f"Without outside spaces: {message.strip()!r}")
    print(f"Split into words: {message.split()}")
    print(f"Replace text: {message.replace('fun', 'powerful')!r}")
    print(f"Count letter n: {message.count('n')}")
    print(f"Starts with spaces? {message.startswith('  ')}")


def preview_more_string_methods():
    """List more common string methods to explore."""
    show_section("More string methods to explore")

    methods = [
        ".capitalize()",
        ".title()",
        ".replace(old, new)",
        ".find(text)",
        ".count(text)",
        ".startswith(text)",
        ".endswith(text)",
        ".join(list_of_strings)",
    ]

    print("Strings have many methods. Try these in your own experiments:")
    for method in methods:
        print(f"- {method}")


def index_and_slice_strings():
    """Access one character or a range of characters."""
    show_section("Indexing and slicing")

    text = "Python"

    print(f"First character: {text[0]}")
    print(f"Last character: {text[-1]}")
    print(f"First three characters: {text[:3]}")
    print(f"Every other character: {text[::2]}")
    print(f"Reversed: {text[::-1]}")


def main():
    """Run each lesson section in order."""
    create_strings()
    combine_strings()
    use_string_methods()
    preview_more_string_methods()
    index_and_slice_strings()


if __name__ == "__main__":
    main()

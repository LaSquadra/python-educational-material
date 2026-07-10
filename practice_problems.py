# coding: utf-8
"""Practice Problems for Python Educational Material.

Use this file as a workbook. Each section matches one lesson file.

Suggested workflow:

1. Read the matching lesson file.
2. Write your solution under the practice prompt.
3. Run this file.
4. Comment out finished solutions before moving to the next section.
"""


# ---------------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------------
"""Practice 01: Variables.

- Create a variable called `my_favorite_number`.
- Create a variable called `my_age`.
- Print both variables.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Strings
# ---------------------------------------------------------------------------
"""Practice 02: Strings.

- Create `string_1` with the value `"Hello"`.
- Create `string_2` with the value `"World!"`.
- Print each variable.
- Create `concatenated_string` that combines them with a space.
- Create `my_name` with your first and last name.
- Print the first character in your name.
- Print your initials.
- Print your name in reverse.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Booleans
# ---------------------------------------------------------------------------
"""Practice 03: Booleans.

- Create one variable with the value `1`.
- Create another variable with the value `0`.
- Print both values.
- Convert each value with `bool()` and print the result.
- Create an empty string and print `bool(empty_string)`.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Comparison Operators
# ---------------------------------------------------------------------------
"""Practice 04: Comparison operators.

- Create `int_5` with the integer `5`.
- Create `str_5` with the string `"5"`.
- Print the result of `int_5 == str_5`.
- Convert `str_5` to an integer.
- Print the result of comparing `int_5` to the converted value.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Flow Control and Conditionals
# ---------------------------------------------------------------------------
"""Practice 05: Flow control and conditionals.

- Create three variables that store different strings.
- Create a number variable.
- Use `if` and `else` to check whether the length of the first string equals
  your number.
- Bonus: add an `elif` branch that checks another string.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Integers and Floats
# ---------------------------------------------------------------------------
"""Practice 06: Integers and floats.

- Create two number variables.
- Calculate the area of a right triangle using those values.
- Calculate the volume of a rectangular box where height is half the width.
- Bonus: automate a calculation you use in daily life.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Lists
# ---------------------------------------------------------------------------
"""Practice 07: Lists.

- Create a list containing: `1`, `2`, `"a"`, `"b"`, `9`, `"A"`.
- Practice indexing each value.
- Change the fourth value to `"I am a new value!"`.
- Multiply the second value by `2`.
- Multiply the third value by `2` and compare the result.
- Use `.copy()` to create an independent copy of a list.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Loops
# ---------------------------------------------------------------------------
"""Practice 08: Loops.

For loop:
- Create a list containing `1` through `7`.
- Print each value with a `for` loop.
- Add charge-level logic that prints different messages below, at, and above
  your chosen charge value.

While loop:
- Start with two numbers between `5` and `10`.
- Keep adding the two most recent values until the total reaches 100,000,000.
- Print how many loop iterations it took.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Dictionaries
# ---------------------------------------------------------------------------
"""Practice 09: Dictionaries.

- Create three dictionaries that simulate phone book contacts.
- Each contact should include name, age, phone number, and address.
- Add the dictionaries to a list called `contact_list`.
- Search the list and print the name of the oldest person.
- Bonus: solve it again with a dictionary of dictionaries.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------
"""Practice 10: Functions.

- Write a function that accepts a name and returns a greeting.
- Write a function that accepts two numbers and returns their product.
- Write a function that accepts a list of numbers and returns their average.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
"""Practice 11: Imports.

- Import `Path` from `pathlib`.
- Print the current working directory.
- Import `math`.
- Use `math.pi` to calculate the area of a circle.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# File Manipulation
# ---------------------------------------------------------------------------
"""Practice 12: File manipulation.

- Create a file called `student_notes.txt`.
- Write three lines of notes into it.
- Read the file back and print its contents.
- Append one more line, then read it again.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------
"""Practice 13: Classes.

- Create a `Book` class.
- Add `title`, `author`, and `page_count` attributes.
- Add a method that returns a readable book description.
- Create two book instances and print their descriptions.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Example Solutions
# ---------------------------------------------------------------------------
"""Loop Practice 08 while-loop example.

num_small = 5
num_large = 6
total_sum = 0
total_iterations = 0

while total_sum < 100_000_000:
    total_sum = num_small + num_large
    total_iterations += 1
    num_small = num_large
    num_large = total_sum

print(f"{total_iterations = }")
"""

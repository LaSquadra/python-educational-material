# coding=utf-8
"""
Comparison Operators:  ==, !=, >, <, >=, <=

Comparison operators are used to compare two values and return a boolean value (True or False).
The basic comparison operators in Python are:
    - Equal to: ==
    - Not equal to: !=
    - Greater than: >
    - Less than: <
    - Greater than or equal to: >=
    - Less than or equal to: <=
There are two different types of equality operators in Python:
    - The '==' operator checks if two values are equal.
    - The 'is' operator checks if two variables are pointing to the same object in memory.
        - This is a more advanced concept and is not used as frequently as the '==' operator.
        - We will cover this concept in more detail later.
Similarly, there are two different types of inequality operators in Python:
    - The '!=' operator checks if two values are not equal.
    - The 'is not' operator checks if two variables are not pointing to the same object in memory.
        - This is a more advanced concept and is not used as frequently as the '!=' operator.
        - We will cover this concept in more detail later.
      
We will explore using comparison operators below.
"""


# We can use comparison operators to compare two values:
string_1 = "Hello"
string_2 = "World"
# The '==' operator checks if two values are equal.
# string_1 == string_2
# This will return False because the two strings are not equal.
print(string_1 == string_2)  # <-- This will return/display the Boolean value 'False' to the console


# The '!=' operator checks if two values are not equal.
# string_1 != string_2
# This will return True because the two strings are not equal.
print(string_1 != string_2)  # <-- This will return/display the Boolean value 'True' to the console


# We will explore the use and power of comparison operators next (05_intro_to_flow_control_and_conditionals)
# We will cover the other comparison operators in the '06_intro_to_integers' section.
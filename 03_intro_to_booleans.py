# coding=utf-8
"""
Booleans:  bool()

Booleans are a data type that can only have one of two values: True or False.
Booleans are used to represent the truth value of an expression. (e.g. 1 > 2 is False)
Booleans are used in conditional statements to control the flow of a program. (We will cover this later)
Booleans are essentially a way to represent the concept of 'yes' or 'no' in Python.
There are many different ways to create a boolean value in Python:
    - You can use the '==' operator to compare two values.
        - For example: 1 == 1 will return True
    - You can use the '!=' operator to compare two values.
        - For example: 1 != 1 will return False
    - You can set a variable to be equal to True or False. (Note the capitalization)
        - For example: is_true = True
        - For example: is_false = False
With Booleans, there is also the concept of "truthy" and "falsy" values.
    - A "truthy" value is a value that is considered True when evaluated in a Boolean context.
    - A "falsy" value is a value that is considered False when evaluated in a Boolean context.
    - In Python, the following values are considered "falsy":
        - False  <-- Note the capitalization
        - None  <-- Note the capitalization
        - 0
        - 0.0
        - ''
        - []
        - ()
        - {}
        - set()
        These are essentially anything that doesn't contain data or is 'empty'.
    - All other values are considered "truthy".
"""

# We will explore using booleans in the next section (04_intro_to_comparison_operators)
# For more information on Booleans, see: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

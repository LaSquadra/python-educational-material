# coding=utf-8
"""
Introduction to Integers and Floats

Integers and floats are two different types of numerical data in Python.
    - Integers are whole numbers (numbers without a decimal point).
    - Floats are numbers that have a decimal point.
Integers and floats can be used in mathematical operations.
    - Addition: +
    - Subtraction: -
    - Multiplication: *
    - Division: /
    - Exponentiation: **
    - Modulo: %
    - Floor Division: //
We will explore using integers and floats below.
"""

# Integers
age = 35
print(age)  # <-- This will return/display 35 to the console
print(type(age))  # <-- This will return/display <class 'int'> to the console

# Floats
ranking = 4.5
print(ranking)  # <-- This will return/display 4.5 to the console
print(type(ranking))  # <-- This will return/display <class 'float'> to the console

"""
If you wanted to create a more explicit printed output, you have multiple options:
You can use the 'formatted strings' mentioned in the strings section earlier
  OR
you can use the following:
"""
print("Age:", age)  # <-- This will return/display Age: 35 to the console
    # NOTE: because this is a string ("Age:") and a integer (35), you cannot concatenate them with a '+'
    # You must use a ',' to separate the string and the integer
print("Age: " + str(age))  # <-- This will return/display Age: 35 to the console
    # NOTE: Optionally, because this is a string ("Age:") and a integer (35), you can convert the integer to a string
    # You can do this by using the str() function.  This is called 'casting' and can be done on various data types.

"""
NOTE: My personal preference is to use the f-string method from the strings section as I feel it looks the cleanest
      and you do not need to account for differing data types.
"""
print(f"Age: {age}")


# We can perform mathematical operations on integers and floats:
number_1 = 5
number_2 = 10
"""
- Addition: +
    number_3 = number_1 + number_2 # <-- This will return/display 15 to the console
- Subtraction: -
    number_3 = number_1 - number_2 # <-- This will return/display -5 to the console
- Multiplication: *
    number_3 = number_1 * number_2 # <-- This will return/display 50 to the console
- Division: /
    number_3 = number_1 / number_2 # <-- This will return/display 0.5 to the console
- Exponentiation: **
    number_3 = number_1 ** number_2 # <-- This will return/display 9765625 to the console
- Modulo: %
    number_3 = number_1 % number_2 # <-- This will return/display 5 to the console
- Floor Division: //
    number_3 = number_1 // number_2 # <-- This will return/display 0 to the console
"""
add_numbers = number_1 + number_2
print(add_numbers)  # <-- This will return/display 15 to the console
subtract_numbers = number_1 - number_2
print(subtract_numbers)  # <-- This will return/display -5 to the console
multiply_numbers = number_1 * number_2
print(multiply_numbers)  # <-- This will return/display 50 to the console
divide_numbers = number_1 / number_2
print(divide_numbers)  # <-- This will return/display 0.5 to the console
power_numbers = number_1 ** number_2
print(power_numbers)  # <-- This will return/display 9765625 to the console
modulo_numbers = number_1 % number_2
print(modulo_numbers)  # <-- This will return/display 5 to the console
floor_divide_numbers = number_1 // number_2
print(floor_divide_numbers)  # <-- This will return/display 0 to the console
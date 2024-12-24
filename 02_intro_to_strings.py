# coding=utf-8
"""
Strings:  str()

Strings are a sequence of characters that store text data.
Strings are immutable, meaning that they cannot be changed once they are created.
In Python, strings are created by enclosing the text in either single or double quotes.
Strings are indexed (also called 'iterable')
    This means you can access individual characters in a string using their position [index].
Strings are unique in that they can be concatenated (combined) using the '+' operator.
    For example: "Hello" + " " + "World" = "Hello World"
    NOTE: The convention above is not actually how you assign variables in Python.
        Typically, you would have the name of the variable on the left and assign it
        to the data on the right side of the '=' sign  (e.g. greeting = "Hello World")

There are two different ways to wrap strings in Python:
    - Single quoted strings: 'This is a single-quoted string.'
    - Double quoted strings: "This is a double-quoted string."
Along with the two different ways to wrap strings, there are also triple-quoted strings:
    - The block of text that you are reading from here is called a docstring. (a string wrapped in triple quotes)
    - Triple quoted strings are used to create multi-line strings.
    - Triple quoted strings can be wrapped in single or double quotes. (just have three of them on each side)

In Python, you can also create comments by using the '#' symbol.
    - These are not actually strings but are used to document code and are frequently used to explain what the code is doing.
    - Comments are ignored by the Python interpreter and are not executed.
"""

# We will explore using strings below.
example_string_variable = "This is a string."
example_string_variable_2 = "This is another string."

# We have created two variables above that store strings.
# We can display the value of these variables using the print() function.
print(example_string_variable)
print(example_string_variable_2)

# We can also concatenate strings.
# The '+' operator is used to combine two strings.
greeting = "Hello" + " " + "World" # <-- This will return/display "Hello World" to the console

# We can also use the '+' operator to combine a string with a variable.
combined_string = greeting + "!" # <-- This will return/display "Hello World!" to the console

"""
The following methods are called "formatted strings" and are used to format strings in Python where the variable types do not matter.
"""
user_name = "John"
# 1. The 'f-string' method:
print(f"My name is: {user_name}")  # <-- This will return/display "My name is: John" to the console
# NOTE: This is called an 'f-string' and is a more modern way of formatting strings in Python.
# It is also the most efficient way of formatting strings in Python. (outside of logging statements)

# 2. The 'format()' method:
print("My name is: {}".format(user_name))  # <-- This will return/display "My name is: John" to the console
# NOTE: This is an older way of formatting strings in Python.
# It is still used in some cases, but the 'f-string' method is preferred.
# This method is used when writing code that is compatible with older versions of Python.
# This method is preferred when using logging statements as it does not compute unless the logging statement is triggered.

# 3. The '%' method: (%s for strings, %d for integers, %f for floats)
print("My name is: %s" % user_name)  # <-- This will return/display "My name is: John" to the console
# NOTE: This is the oldest way of formatting strings in Python.
# It is not recommended to use this method for string formatting in modern versions of Python.


# Strings (and all other data types) have different methods that can be used to manipulate them.
# A method is a function that is associated with a specific data type. (We will cover methods and functions more later)
# The .upper() method is used to convert a string to uppercase.
uppercase_greeting = greeting.upper() # <-- This will return/display "HELLO WORLD" to the console
# Note how the .upper() method is called on the variable 'greeting' using the '.' operator.

# Similar to the .upper() method, the .lower() method is used to convert a string to lowercase.
lowercase_greeting = uppercase_greeting.lower() # <-- This will return/display "hello world"

# There are many other methods that can be used to manipulate strings but there are a few more that are
# important to know and be comfortable with.
# The .split() method is used to split a string into a list of substrings.
# The .split() method takes an argument that is used to split the string.
# If no argument is provided, the string is split by whitespace.
split_greeting = greeting.split() # <-- This will return/display ['Hello', 'World'] to the console
# The .split() method can also be used to split a string by a specific character.
split_greeting_2 = greeting.split("o") # <-- This will return/display ['Hell', ' W', 'rld'] to the console
# NOTE: The .split() method returns a list of substrings. (We will cover lists in a later section)

# Strings can be INDEXED to access individual characters:
# The index of a string starts at 0.
# You can also index strings in reverse using negative numbers: -1 is the last character, -2 is the second to last, etc.
# The syntax for indexing a string is: string_variable[index]
"""
"This is a string"
T = index 0
h = index 1
g = index 15 (and also index -1)
"""
# Below is how you would index the string above:
string_variable = "This is a string"
index_0 = string_variable[0]  # <-- This will return/display "T" to the console
index_1 = string_variable[1]  # <-- This will return/display "h" to the console
index_15 = string_variable[15]  # <-- This will return/display "g" to the console
index_last_character = string_variable[-1]  # <-- This will return/display "g" to the console

# String can be SLICED to access a range of characters:
sliced_string = string_variable[0:4]  # <-- This will return/display "This" to the console
"""
The syntax for slicing a string is: string_variable[start_index:end_index:step]
The start_index is the index where the slice starts.
The end_index is the index where the slice ends (but does not include that index).
   For example: in the string "012345", string_variable[0:3] would return "012" (not "0123")
The step is the number of characters to skip.
   For example: in the string "012345", string_variable[0:5:2] would return "024" (skipping every other character)
If no start_index is provided, the slice will start at the beginning of the string.
If no end_index is provided, the slice will end at the end of the string.
If no step is provided, the slice will include every character.
"""

# For more information on strings and the various methods that can be used to manipulate them, see the Python documentation:
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
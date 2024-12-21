# coding=utf-8
"""
Flow Control and Conditionals: if, elif, else

Flow control statements are used to control the flow of a program.
This simply means that flow control statements allow us to determine which code blocks are executed.
It allows us to build more complex programs by allowing us to make decisions based on certain conditions.
Flow control statements are used to determine the order in which statements are executed in a program.
The often read like English sentences:
    - If (this condition is true): do this.
    - If (this condition is not true): do this.
    - If (this condition is not true) and (this other condition is true): do this.
    - If none of the above conditions are true, do this.
These statements are written as follows: (Note the indentation)

if condition_1:
    code_to_execute_if_condition_1_is_true
elif condition_2:
    code_to_execute_if_condition_2_is_true
else:
    code_to_execute_if_no_conditions_are_true

These conditions can be any expression that evaluates to a boolean value (True or False).
They can also be as simple or as complicated as you need them to be.
For example:
if condition_1 and condition_2 and condition_3: # All conditions must be True
    code_to_execute_if_all_conditions_are_true
elif condition_1 or condition_2 or condition_3: # At least one condition must be True
    code_to_execute_if_any_conditions_are_true
else:                                           # If none of the above conditions are True
    code_to_execute_if_no_conditions_are_true
else is used primarily as a catch-all for any conditions that are not covered by the if or elif statements.
"""

# Example time:
is_true = True
is_false = False
string_1 = "Hello"
string_2 = "Hello"
if is_true:
    print("This will print because the variable is True.")
else:
    print("This will not print because the variable is True.")

if is_false:
    print("This will not print because the variable is False.")
elif not is_false:
    print("This will print because the variable is False.")
# else:  <-- You do not always need to include an else statement.

if string_1 == string_2:
    print("The two strings are equal.")
elif string_1 == "Test String":
    print("string_1 is the same as 'test string'.")
else:
    print("If none of the above conditions is true, print this line.")

# We can also nest if statements inside of other if statements: (Note the indentation)
if is_true:
    if string_1 == string_2:
        print("The two strings are equal.")
    else:
        print("The two strings are not equal.")
        
# We can also use the 'and' and 'or' operators to combine conditions:
if is_true and string_1 == string_2:
    print("The variable is True and the two strings are equal.")

# For more information on flow control and conditionals, see the Python documentation:
# https://docs.python.org/3/tutorial/controlflow.html
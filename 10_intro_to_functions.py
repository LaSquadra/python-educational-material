# coding=utf-8
"""
Functions:

Functions allow us to build specialized code blocks that we can use in multiple places throughout our code.
Functions are created using the 'def' keyword (short for 'define')
Below is the basic format for functions.
def my_function():
    *your code here*
    return some_variable
Functions are blocks of code that are 'staged' and not executed until they are called.
To call a function, you simply use its name: print(my_function())
"""
# Creating a function to greet someone:
def greeting_function():
    print("Hello, how are you?")
greeting_function() # <-- This is all you need to call the above function.
# The function above is very basic and likely not worth creating a function for. They can be as complex as you need.

"""
IMPORTANT NOTES:
- Functions require the use of the 'return' keyword inorder to provide anything back to the code that called it.
    - without using the 'return' keyword, our greeting_function() above would equate to the None type in Python.
- Functions are treated as isolated blocks of code that do not have any sense of what is going on outside of them.
    - We must pass arguments to the function to be able to use them within it.
    - NOTE: Variables listed when the function is defined are 'parameters'.
            variables being passed to the function when it is called are 'arguments'.
            
Lets explore these two concepts:
"""
def personalized_greeting(name): # <-- 'name' is the 'parameter' the function requires/expects.
    print(f"Hello, {name}!  How are you today?")
# To call the function we created we need to pass the 'name' argument to it.
name = "James"
greet_user = personalized_greeting(name) # <-- 'name' is the argument we are passing to the function.
# NOTE: greet_user = personalized_greeting("James") is equally correct.  You can pass a variable or the data directly.

# Look at what happens when we try to print() the value of 'greet_user':
print(greet_user) # <-- This will show the value is 'None'
# This is because we are not 'returning' anything back to the code that called the function.

def personalized_greeting(name):
    print(f"Hello, {name}!  How are you today?")
    return "User was greeted." # <-- You can return anything you like: int, str, list, dict, etc.
# Look what happens when we call the function now:
name = "Jackie"
greet_user = personalized_greeting(name)
print(greet_user)
# the variable 'greet_user' is now set to the string "User was greeted." rather than "None".


# There are two different types of arguments that can be passed to a function: positional and keyword
# Positional arguments be passed in the order they are listed in the creation of the function:
def positional_arguments(name, age, hobby):
    print(f"{name=}") # ***
    print(f"{age=}")
    print(f"{hobby=}")
user_name = "John"
user_age = 22
user_hobby = "Running"
positional_arguments(user_name, user_age, user_hobby)
#   *** As of Python 3.10, the syntax of "variable=" within a print statement will yield a more explicit output.
# NOTE:It is important to pay attention to the order (position) with positional arguments.
#      The function needs the arguments to be passed in the same order that they are defined in.

# Keyword arguments do not need to be passed in any specific order.
# Inorder to prevent conflicts with positional arguments, all keyword arguments must be passed AFTER any keyword arguments.
def keyword_arguments(name="placeholder name", age=0, hobby="placeholder hobby"):
    print(f"{name=}")
    print(f"{age=}")
    print(f"{hobby=}")
user_name = "Robert"
user_age = 56
user_hobby = "Fly Fishing"
keyword_arguments(name=user_name, age=user_age, hobby=user_hobby)

"""
If you looked closely you may have noticed that the argument being passed to the function
does not have the same name when it is being used within the function.
This is because the function has no knowledge of what is happening outside and only knows what you provide.
In this case, it translates 'user_name' to the internal variable 'name' when you are calling the function.
"""
# A function using both positional and keyword arguments would be structured as such:
def both_arguments(name, age=0, hobby="placeholder hobby"):
    print(f"{name=}")
    print(f"{age=}")
    print(f"{hobby=}")
user_name = "Robert"
user_age = 56
user_hobby = "Fly Fishing"
keyword_arguments(user_name, hobby=user_hobby, age=user_age)
# NOTE: The positional argument is listed first and the keyword arguments are second (and in any order the user wants)

# Let's use look at another example to show the importance of the 'return' keyword:
def add_numbers(number_1, number_2):
    total = number_1 + number_2
    return total


"""
USING DOC STRINGS:

In most (if not all) coding languages, it is important to document your code.
This typically means adding comments "# your comment here" to your code to help explain what each section is doing.

To this end, it is customary to do the same within your functions using the tripple-quoted doc-string
i.e. This block of text
The specific formatting of the doc string will often vary from programmer to programmer and organization to organization.
There are some important things that should be included though:
- What the purpose/function of the function is.
- What each parameter it accepts are and how they should be structured (I will explain this later)
- What the function will be returning. (True? None? a List?)
"""
# Here is a basic example of how to create a function and document it:
def adding_numbers(number_1, number_2):
    """
    :param number_1: int/float to be added
    :param number_2: int/float to be added
    :return: int/float of the sum
    """
    # Adding the two numbers together to get the sum
    total_sum = number_1 + number_2
    # Returning the sum to the main program
    return total_sum
# NOTE:  Be as detailed as you feel is necessary.
#        You can leave out more basic things once you are more comfortable.

# Let's see how a function can be utilized to reduce the amount of code you need to write:
list_of_numbers = [1, 5, 7, 2, '4', 1, 8, 2, '9', 0, 4.1, 8]
# Imagine you need to perform the following operation frequently throughout your code:
total_sum = 0 # Setting this to Zero until we add values to it.
for number in list_of_numbers:
    if str(type(number)) == "<class 'int'>" or str(type(number)) == "<class 'float'>":
        total_sum += number
    elif str(type(number)) == "<class 'str'>":
        if number.isdigit(): # This method checks if the string value can be converted to a numeric value.
            total_sum += float(number)
    else:
        print(f"The value is {type(number)}.  Cannot perform mathematical operation on it.")
print(total_sum)


# If you need to do this multiple times, it may be beneficial to create a function for it:
def check_and_add(number_list):
    """
    This function takes a list of values and adds all the numbers together.
    :param number_list: list containing numbers
    :return: int/float of the total/sum of all the numbers in the list
    """
    num_sum = 0  # Setting this to Zero until we add values to it.
    for num in number_list:
        if (str(type(num)) == "<class 'int'>") or (str(type(num)) == "<class 'float'>"):
            num_sum += num
        elif str(type(num)) == "<class 'str'>":
            if num.isdigit():  # This method checks if the string value can be converted to a numeric value.
                num_sum += float(num)
    return num_sum
    
# Now you can use this custom function anywhere you like:
list_to_add_1 = [2, 2, 4, 5, 7, 1, 0, 3, 4, 1, 5]  # Creating first list to find the sum of
list_to_add_2 = [1, 5, 7, 2, '4', 1, 8, 2, '9', 0, 4.1, 8]  # Creating second list to find the sum of
list_of_totals = [check_and_add(list_to_add_1), check_and_add(list_to_add_2)]  # crating a list of the two lists' sums
print(f"{list_of_totals=}")
total_of_totals = check_and_add(list_of_totals)  # Finding the sum of the two lists' sums
print(f"{total_of_totals=}")


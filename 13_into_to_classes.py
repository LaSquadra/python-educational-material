# coding=utf-8
"""
Classes:

Classes are Python's way of allowing developers to create their own custom modules that can be shared or used
in a more dynamic way than creating a simple function within your script.

With classes, we introduce the concept of 'inheritance'.
This is where properties of a Class are inherited by its methods.
We can change virtually everything about how something functions if we understand how to use inheritance properly.
"""
# We can view the properties of a class by using the dir() method:
print(dir(int))
"""
Notice how the int class has math-related attributes like:
    '__add__', '__sub__, '__mul__', '__div__', '__abs__'   (just to name a few))
These attributes are called 'dunder attributes' (dunder = double-underscore)
These dictate how a class handles characters like: +, -, *, /
In math terms, we understand what these are going to do.  For our custom function, we have have them do anything.
"""

# Let's go over the class we created in the imports section and explain what is going on.
class ClassToImport:
    """
    This is a dummy, demo class to show how imports work.
    """
    
    def __init__(self):
        print("This code runs when the class is initialized.")
    
    @staticmethod
    def function_to_do_something():
        print("This code only runs when the method (a function belonging to a class) is called.")
    
    print("Any code not contained within a function can be run by simply importing the module.")


my_class = ClassToImport()  # This is initializing the class
my_class.function_to_do_something()  # This is calling a method from the class

"""
We will start by breaking it down into its pieces.

We begin by creating the class using the 'class' keyword (similar to 'def' for functions)
We then name our class. Convention states that we use "CamelCase" for class names.
Simply put: Capitalize the first letter of each word in the name (rather than using '_' like in functions and variables.
We then end the line with a colon ':' like we do when we begin any block of code (if/elif/else, loops, functions, etc.)

Putting all of that together and we have:

class YourClassName:


Next we would add a documentation string to summarize what the class is designed to help do and briefly
summarize its functionality.

We can then jump into adding methods (functions) to the class to do different things.
These are created exactly like the functions we created before but now we will have
the 'self' keyword as the first argument.

class YourClassName:
    <insert your doc string here>
    
    def first_class_method(self):
        <doc string here>
        print("This is the first method of our custom class!")
        return True


You have the option of creating a custom __init__() function which can help set up variables and things you may need.

    def __init__():
        self.default_security_string = "aslkoaishnlahoishgeiikajsdngh=="
        self.default_dns_ip = "8.8.8.8"
Now anytime your class is initialized, these values will be set and they can be used by the other methods of the class.

"""
# Let's play with the __init__() option and see how it works:
class ClassToImport:
    """
    This is a dummy, demo class to show how imports work.
    """
    
    def __init__(self):
        self.default_security_string = "aslkoaishnlahoishgeiikajsdngh=="
        self.default_dns_ip = "8.8.8.8"
        print("This code runs when the class is initialized.")
    
    @staticmethod
    def function_to_do_something():
        print("This code only runs when the method (a function belonging to a class) is called.")
    
    def using_inherited_values(self):
        print(self.default_dns_ip)
        print(self.default_security_string)
    
    print("Any code not contained within a function can be run by simply importing the module.")


my_class = ClassToImport()  # This is initializing the class
my_class.using_inherited_values()  # This is calling a method from the class
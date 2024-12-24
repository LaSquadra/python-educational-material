# coding=utf-8
"""
Imports:

Imports dramatically increase the utility of Python.
You can write everything by hand if you like OR you can find a module that does what you want and utilize its methods.
There are two ways to import Python modules into your program:\
SYNTAX:
import name_of_module
from name_of_module import specific module_or_method_to_use

The first option will import the whole module and load it into memory (can be more computer resource heavy)
The second imports only the specific functionality you want from the module.
NOTE: These will typically be at the top of the file.
      There are situations where you may want to import them later in the code.
      We will not cover them here as it is unlikely that you will need to do so.
"""
# Here is how they look
import pathlib
current_directory = pathlib.Path.cwd() # Notice the '.' dot-notation  --> pathlib-dot-Path-dot-cwd()
print(current_directory)
# OR
from pathlib import Path
current_directory = Path.cwd()
print(current_directory)
# The dot-notation is used to reference modules from within their parent classes/files.

# For anything you want to do in python, a module likely exists to help you.
# Do some Google searching (or use ChatGPT) to see what modules are available to you.

"""
Python has a handful of built-in modules and even more that come installed but are not loaded unless you need them.
If you need to install a new module, you will need to use 'pip' (python's package manager)
The command is often simple:
    pip install name_of_the_module
IMPORTANT NOTE: It is very important that you do some research and only import trusted modules.
                If the file contains malicious code it will likely be executed by simply importing the module.
Here is an example of how that would work.
(This is not going to be covered in detail till later so don't worry if this is over your head right now)
"""

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


my_class = ClassToImport() # This is initializing the class
my_class.function_to_do_something() # This is calling a method from the class

"""
Notice how the print() statement which wasn't within any of the defined class methods ran by simply
having the class loaded into memory (not even initialized yet)
This is what happens when you import modules into your code.
We will cover how to prevent your own modules from doing this when we get to the Classes section.
"""
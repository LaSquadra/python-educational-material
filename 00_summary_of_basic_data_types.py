# coding: utf-8
"""
Basic Data Types:

 - String str()
 - Integer int()
 - Float float()
 - Bool bool()
 - List lst()
 - Set set()
 - Dictionary dict()
"""

# COMMENTS:

#  In Python, there are things called "Comments".
#  Comments are lines within the file that are skipped during the execution of the file.
#  While comments are not necessarily a "data type" they are very common to see in code and are very helpful to use.
#  Comments exist to allow the author to explain and document what a section of code is doing
#  They are also used to explain why a section of code is written the way it is (ex: accounting for odd behavior)
#  In most IDEs, comments will appear grey in color.


#  The following block of code is wrapped in triple quotes: """some string here"""
#  This is an example of Documentation String (doc string for short)
"""
In Python there are a large variety of "Data Types" that you may come across.
The primary data types that most everything else is built off of are listed above.
In this section we will explain what they are, how they are different and when you would use them.
"""


# STRINGS:
"""
The following lines are wrapped in either single or double quotes
There is no right or wrong one to use.  Just make sure you are consistent.
"The first section will cover strings."
"Strings are ANYTHING wrapped inside quotes: 'this is a string' "  # Note that this line uses both single and double
'Strings can be wrapped in either single or double quotes. Just be consistent.'
'In most IDEs, strings will appear green.'
'Strings are unique in the fact that you can convert every single other data type into a string'
"Strings are 'iterable' meaning they can be accessed (indexed) one character at a time"
"Python starts counting from '0' (ex. 0, 1, 2, 3...)"
"""


# INTEGERS & FLOATS:
"""
What are Integers?
 - Integers are whole numbers: 0, 1, 2, 2000000, -1, 700, etc.
What are Floats?
 - Floats are numbers that contain a decimal point: 0.1, 1.6, 2.1, 23455348.9, -1.3, etc.)
Integers and Floats are mutable.
 - This means the data can be altered without needing to create a new object in memory to store it.
When would you use Integers and/or Floats?
 - Integers and Floats can be used in mathematical operations.
     - The mathematical operators are as follows:
         - Addition: +         (1 + 2 = 3)
         - Subtraction: -      (1 - 2 = -1)
         - Multiplication: *   (3 * 3 = 9)
         - Division: /         (3 / 3 = 1)
         - Exponents: **       (5 ** 4 = 625)
         - Floor division: //  (5 // 4 = 1) # This gives only the whole number.  (5 / 4 would return 1.25)
         - Modulus: %          (5 % 4 = 1)
 -  Math in Python follows all the same order of operations one would expect.
"""


# BOOLEANS bool()
"""
What are Booleans?
 - Booleans can only ever be one of two values: True or False (Like '0' and '1' in binary)
 - Booleans exemplify the concept of 'truthy' and 'falsy'
     - Any variable or object that contains data is considered 'truthy'
     - Any variable or object that is 'empty' (examples: "" or [] or {} or 0)
When would you use Boolean values?
 - Booleans are frequently used in 'flow control' (the logic of the program)
"""


# LISTS lst()
"""
What are Lists?
 - Lists are essentially variables that contain other variables.
 - Lists are created but using the [] (opening and closing Square Brackets) and placing data inside, separated by a comma
     - my_list = [0, 1, 2, 3, '4', 'some string here', [...], (...), {...}]
 - Lists are used to hold various pieces of data and do not require the data types to all be the same.
 - Lists are immutable.  This means that you cannot change a list.
     - When you attempt to change a list, it actually destroys the old list (in memory) and creates a new one.
 - Items within Lists are accessed by indexes.
When would you use Lists?
 - Lists are used when you need to store multiple pieces of data for any reason.
 - Indexing lists:
     - my_list = [0, 1, 2, 3, '4', 'some string here']
     - first_value = my_list[0] <-- this will return the zeroth index of the list
     - fifth_value = my_list[4] <-- This will return the 5th value in the list (counting from 0, 1, 2, 3, 4, etc.)
     - last_value = my_list[-1] <-- This will count from the end of the list
"""


# SET set()
"""
What are Sets?
 - Sets are similar to lists but are created with the () (opening and closing Parentheses)
 - Sets are special in that they can contain any number of different items but only one of any specific item.
     - EXAMPLE: my_set = ('a', 'b', 'c', 'd', 'e')  it cannot contain ('a', 'b', 'c', 'd', 'e', 'a', 'a', 'b')
     - if you create a list and convert it to a set, it will automatically remove any duplicate values.
     - NOTE: Integers and strings are not considered the same so both the integer 5 and string '5' can be inside a set.
 - Sets are immutable.  This means that you cannot change a list.
 - Items within sets are accessed by indexes
When would you use Sets?
 - Sets are used with you need to maintain the the integrity of the data
 OR
 - When you want to ensure you do not have duplicates of any values.
 - Sets are indexed in the same way as lists:
     - my_set = ('a', 'b', 'c', 'd', 'e')
     - first_value = my_set[0] <-- This would return 'a'
     - fifth_value = my_set[4] <-- This would return 'e'
     - last_value = my_set[-1] <-- This would return 'e'
 """
 
 
# DICTIONARIES dict()
"""
What are Dictionaries?
 - Dictionaries are created by using {} (opening and closing Curly Braces)
     - Key:Value pairs are created with the key ALWAYS being a string and linking the value with a ':'
     - The pairs are then separated by commas. (see below)
     - EXAMPLE: my_dict = {'key_1': 'value to store', 'key_2': 'other data here'}
 - Dictionaries are a more organized way of storing data.
 - Dictionaries are mutable and can be modified at any point.
 - Dictionaries are accessed by Keys as follows:
     - my_dict = {'key_1': 'value to store', 'key_2': 'other data here'}
     - first_item = my_dict['key_1'] <-- This will evaluate to 'value to store' from the example above
 - You can also assign values in the same way (either using an existing key or creating a new one):
     - my_dict['key_3'] = "even more data here"
     - Now 'my_dict' contains the following data: {'key_1': 'value to store', 'key_2': 'other data here', 'key_3': 'even more data here'}
 - NOTE: dictionaries that contain many values are often written across multiple lines to be easier to read:
     - EXAMPLE:
         - my_dict = {
                'key_1': 'value to store',
                'key_2': 'other data here',
                'key_3': 'even more data here'
                }
When would you use Dictionaries?
 - Dictionaries are frequently used when storing data about certain things.
     - This could be attributes of an animal:
         - dog_attributes = {
                     'number_of_legs' = 4,
                     'voice_type = 'Bark',
                     'cuteness_value' = 10
                     }
         - cat_attributes = {
                    'number_of_legs' = 4,
                    'voice_type = 'Meow',
                    'cuteness_value' = 9
                    }
     These values would be accessed as such:
         - dog_voice = dog_attributes['voice_type'] <-- this will be 'Bark'
         - cat_voice = cat_attributes['voice_type'] <-- this will be 'Meow'
"""

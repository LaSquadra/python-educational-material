# coding=utf-8
from pprint import pprint
"""
Dictionaries: dict() or {}
my_dict = {}  <-- This will create an empty dict. You can always add items later.
NOTE: I will use the shorthand of 'Dicts' moving forward
Dicts consist of key-value pairs separated by commas within the curly braces {}
my_dict = {'key_1': 'value 1', "key_2":"value 2", "key_3": 3}
Dictionaries are unordered (unlike lists). This also means you cannot use the sort() method on them.
This means that if you attempt to access them by an index number, you may not get the value you were expecting.
Dictionaries are a powerful data type because they are accessed by their keys.
Dictionaries make storing various data points about a certain object easier.
You do not need to iterate through them like a list to find what you are looking for, you can look for it directly.
"""
# In lists: You would retrieve/access the value/data by the index:
my_list = ['a', 'b', 'c', 'd', 'e']
letter_c = my_list[2]

# In dicts: You retrieve/access the value/data by the key:
user_data = {'name': 'John Doe', "age": 45, "job": "Postal Worker"}
user_name = user_data['name']

"""
Dicts, like lists, can contain any data type within them.
The only real condition is that they 'key' must be a string.
example_dict = {"good_key": "anything you want here", 4: "more stuff here"
In the example dict above, the string "good_key" is an acceptable key but the integer 4 is not.
You can use numbers but they must be of the string class:  str(4) will work but int(4) will not.
It is also good practice to not include spaces in your keys (keep them as one word or use the '_' to separate)
"""

# Let's look at an example where a dictionary might be helpful:
user_1 = {"name": "John Doe", "age": 45, "job": "Military"}
user_2 = {"name": "Bruce Wayne", "age": 41, "job": "Batman"}

list_of_users = [user_1, user_2]

for user in list_of_users:
    if user['name'] == "Bruce Wayne":
        print(f"Hello, {user['job']}!")
    else:
        print("You are not Batman!")


# Dicts can contain other dicts and are accessed as such:
user_1 = {"name": "John Doe", "age": 45, "job": "Postal Worker"}
user_2 = {"name": "Bruce Wayne", "age": 41, "job": "Batman"}

dict_of_users = {'unknown_soldier':user_1, "batman":user_2}
age_of_batman = dict_of_users['batman']['age']
print(age_of_batman)
# BELOW: I am using a special module which is built into python: pprint()
# This will simply apply formatting to the output to make it easier to read.
pprint(dict_of_users)

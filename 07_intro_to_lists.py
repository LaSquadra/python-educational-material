# coding=utf-8
"""
Lists:  list() or []

Lists are the first of the data structures that we will explore.
Lists are a collection of items that are stored in a single variable.
The items in the list do not need to be of the same type.
Lists are mutable, meaning that they can be changed after they are created.
In Python, lists are created by enclosing the items in square brackets and separating them with commas.
    Example: my_list = [1, 2, 3, 4, 5]
Lists are indexed (also called 'iterable')
    This means you can access individual items in a list using their position [index].
    Lists are indexed exactly like strings:  starting form 0 and going to the length of the list - 1.
    Example: my_list = [1, 2, 3, 4, 5]
             my_list[0] will be 1
             my_list[4] will be 5
lists have a variety of methods that can be used to manipulate the data they contain.
    Important list methods to know:
        - append() : adds an item to the end of the list
        - insert() : adds an item to a specific position in the list
        - remove() : removes an item from the list
        - pop() : removes an item from the list at a specific position
        - clear() : removes all items from the list
        - index() : returns the index of the first occurrence of the item in the list
        - count() : returns the number of times the item appears in the list
        - sort() : sorts the list in ascending order
        - reverse() : reverses the order of the list
        - copy() : returns a copy of the list
    There are many more list methods that can be found in the Python documentation:
    https://docs.python.org/3/tutorial/datastructures.html
"""

# How to create a list:
# You can create a list as simply as this: my_list = []
# This creates an empty list which you can add items to later.
    # NOTE: in this state, the list will be considered 'False' in a boolean context as there is no data contained.
# You can also create a list with items in it:
my_list = [1, 2, 3, 'this is a string', 4, [], 5]

# Let us look at the list methods now:
# 1. append()
my_list.append(6)  # <-- This will add the integer 6 to the end of the list
print(my_list)  # <-- This will return/display [1, 2, 3, 'this is a string', 4, [], 5, 6] to the console

# 2. insert()
my_list.insert(3, 'inserted string')  # <-- This will add the string 'inserted string' at index 3 in the list
print(my_list)  # <-- This will return/display [1, 2, 3, 'inserted string', 'this is a string', 4, [], 5, 6] to the console

# 3. remove()
my_list.remove(4)  # <-- This will remove the integer 4 from the list
print(my_list)  # <-- This will return/display [1, 2, 3, 'inserted string', 'this is a string', [], 5, 6] to the console

# 4. pop()  NOTE: This method also has a special use case you can look up on your own.
my_list.pop(5)  # <-- This will remove the item at index 5 from the list
print(my_list)  # <-- This will return/display [1, 2, 3, 'inserted string', 'this is a string', 5, 6] to the console

# 5. clear()
my_list.clear()  # <-- This will remove all items from the list
print(my_list)  # <-- This will return/display [] to the console

# 6. index()  This method returns the index location in the list of the item you are looking for.
my_list = [1, 2, 3, 'this is a string', 4, [], 5]
index = my_list.index('this is a string')  # <-- This will return/display 3 to the console
print(index)

# 7. count()  This method returns the number of times an item appears in the list.
my_list = [1, 2, 3, 'this is a string', 4, [], 5, 3, 3]
count = my_list.count(3)  # <-- This will return/display 3 to the console
print(count)

# 8. sort() NOTE: This method will permanently alter the data in the list.
my_list = [5, 3, 1, 4, 2]
my_list.sort()  # <-- This will sort the list in ascending order
print(my_list)  # <-- This will return/display [1, 2, 3, 4, 5] to the console

# 9. reverse()
my_list.reverse()  # <-- This will reverse the order of the list
print(my_list)  # <-- This will return/display [5, 4, 3, 2, 1] to the console

# 10. copy()
my_list_copy = my_list.copy()  # <-- This will create a copy of the list
print(my_list_copy)  # <-- This will return/display [5, 4, 3, 2, 1] to the console

# Lists can be indexed and sliced just like strings:
# The syntax for indexing and slicing lists is the same as it is for strings.
# REMINDER: The index of a list starts at 0.
# You can also index lists in reverse using negative numbers: -1 is the last item, -2 is the second to last, etc.
my_list = ["a", "b", "c", "d", "e"]
first_index_item = my_list[0]  # <-- This will return/display 'a' to the console
print(first_index_item)

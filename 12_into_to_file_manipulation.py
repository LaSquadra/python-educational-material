# coding=utf-8
"""
File Manipulation:

Writing programs that can take in data from files and either modify the data or create new
files with your modified data is often a frequently requested feature.
There are a few things to keep in mind when working with files:
- You will need to know the path to and name of the file (pathlib is a great module for this)
- You will need to determine how you want to open the file.  Here are the three (3) primary methods:
    - "r"  Read (can read the file but will not allow any writing or modification of the file)
    - "a"  Append (adds new data to the end of the file)
    - "w"  Write (overwrites any existing data)
"""

# Finding the file path:
from pathlib import Path
current_directory = Path.cwd()
print(current_directory)

# Opening the file:
"""
When opening files, it is strongly recommended to use a 'context manager'.
That may sound complicated but it is really quite simple.
Using the keyword 'with' will create a context manager which will ensure that the file closes when you are done with it.
This is important for keeping your resource utilization down.  The file will be opened and read into memory and failing
to close the file will hold it in memory even after it is no longer needed.

The file path will need to be a string.  Fortunately, pathlib provides its output as a string and we just need to add
the file name to the end.
Let's give it a try:
"""
demo_file = str(current_directory) + '/README.md'  # Notice the '/' I am using here. Microsoft Windows uses '\' instead.
print(demo_file)
with open(demo_file, 'r') as read_file: # This loads the file into memory and assigns it the name 'read_file'
    file_data = read_file.readlines() # This takes the file object and allows us to read the lines of data within it.
    print(file_data)

# If you decide not to use a context manager, this is how you would do it:
read_file = open(demo_file, 'r')
file_data = read_file.readlines()
print(file_data)
read_file.close()
# NOTE: If something goes wrong in your code before it gets to the close() operation, the file will remain open.
#       This is issue handled automatically when using a context manager and you do not need to worry about it.

# Writing to files and/or creating new files:
new_file =  str(current_directory) + "/temp_file.txt"
with open(new_file, "w") as file:
    file.write("You can put anything you want here.\nYou can even use variables to write large blocs of data.")
    # NOTE: The '\n' is a special character which signifies a 'new line'.
    #       Microsoft Windows uses '\r\n' rather than just '\n' like Linux and MacOS (Unix-based operating systems)
    
"""
If you look within your current directory, you will see that a new file has been created called "temp_file.txt" and
contains the test we just wrote to it.  If you change the "w" to an "a" when opening the file, you will be able to
append data to the end of the file if you do not wish to overwrite anything.
NOTE: Using the "a" option will still create a new file if the specified filename does not exist in that directory.
"""

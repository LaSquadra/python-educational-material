# coding=utf-8
"""
This module will contain exercises and projects for the learner to practice what they are learning
TODO: Build out additional practice problems/challenges

Sections:
 - Variables
 - Strings
 - Booleans
 - Comparison operators
 - Flow Control & Conditionals
 - Integers & Floats
 - Lists
 - Loops
 - Dictionaries
 - Functions
 - Imports
 - File Manipulation
 - Classes
"""

# IMPORTANT NOTE: You can comment out your code blocks to help keep the output clean and easy to follow for
#                 later practice problems.

#  Variables:
"""
Variable practice 1:
    - Create a variable called "my_favorite_number" to store your favorite number
    - Create a variable called "my_age" to story the number of years you are old
    - Write a print statement for each of your variables to show/display them on the terminal
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Strings
"""
String practice 1:
    - Create a variable called "string_1" to store the string "Hello"
    - Create a variable called "string_2" to store the string "World!"
    - print the first variable
    - print the second variable
    - Create a new variable called "concatenated_string" and store the concatenated (combined) strings of variables 1 and 2

String practice 2:
    - Create a variable called "my_name" and store your name (first and last name) within it.
    - Print ONLY the first character in your name. ('Bill Jorgensen" would be 'B')
    - Create another print statement that prints your initials ('John Doe' would be 'JD')
    - Create a print statement that prints your name in reverse. ('Jack Black' would be 'kcalB kcaJ'
    - Create a final print statement that prints your name in reverse but do not do it the same was you did it before
        - You may need to research how to do this (it is good practice!)
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Booleans
"""
Boolean practice 1:
    - Create a variable and assign it the value: 1
    - Create a new variable and assign it the value: 0
    - Print the variables and see how they appear in the terminal.
    - Convert (cast) the variables to the boolean type then print them to the terminal once again. Watch what has changed.
    - Create another variable and assign it the an empty string: ''
    - Print the empty string to the terminal
    - Convert (cast) the variable to the boolean type and print it once again.
    NOTE: You can view the type() of any variable using:
        variable_type = type(my_variable_here)
        print(variable_type)
            OR
        print(type(my_variable_here)) <-- If you wanted to do it on one line and not create an additional variable
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________

#  Comparison operators
"""
Comparison operators practice 1:
    - Create a variable called 'int_5' and store the number 5 in it.
    - Create another variable called 'str_5' and store the string '5' in it.
    - Write a print statement to display the boolean value of: 5 == '5'
        - Before you run the program, take a guess at what the print statement will result in
        - Check if you were right.
    - Create a new variable called 'casted_5' and cast the variable containing the string '5' to an integer.
    - Write a print statement to compare the values of 'int_5' and 'casted_5'
        - Again, take a guess at what you think they will be.
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Flow Control & Conditionals
"""
Flow Control & Conditionals practice 1:
    - Create three different variables and store different strings of text inside each one.
        - Your strings should not be the same and they could contain a different number of characters
    - Create a variable with the value of some number (example: 7)
    - Create an 'if' statement checking weather or not the first string's length: len(string_1) is equal to your number
    - Create a print statement to execute if they are the same.
    - Create an 'else' statement and a corresponding print statement explaining that they are not the same.
    BONUS:
    - Build your own custom if-elif-else logic tree and see how you can manipulate the flow of your program with it.
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Integers & Floats
"""
Int & Float practice 1:
    - Create two variables that contain either integers or floats
    - Use those values to find the area of a Right Triangle with those values as the length and width of two sides.
    - Use those values to calculate the the area of a rectangular box where the length and width are your values
        and whose height is half the width. ((l * w) * (w / 2))
    - BONUS:
        - Identify formulas/calculations you use for your daily life/job and practice creating a script (code) to do the math for you.
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Lists
"""
List practice 1:
    - Create a list that contains the follow values: 1, 2, 'a', 'b', 9, 'A'
    - Practice indexing each value in the list
    - Using an index, change the 4th value in the list to the string: "I am a new value!"
    - Take the index for the 2nd value and multiply that value by 2.
    - Take the index for the 3rd value and multiply that value by 2.
    - Compare what happens when you attempt a mathematical operation on a string value compared to a int/float value.
    - Copy and paste the following code block:
        list_1 = [1, 2, 3, 4, 5, 6, 7]
        list_2 = list_1
        list_2[0] = 'a'
        print(list_1[0])
        print(id(list_1))
        print(list_2[0])
        print(id(list_2))
        *** To help show the differences, we will use the id() function.  do not worry about what it does.
            Just pay attention to if the number is the same or different.
        - Before you execute: What do you think the values at index [0] in list_1 and list_2 will be?
        - Did the output surprise you?
        
    - The above example attempted to create a copy of the list (like we can do with integers and strings)
        - The issue is that when you assign a list to a new value, it creates a 'pointer'
          to the original list's location in memory and does not actually create a copy of the list.
        - To accomplish creating an actual copy of the list, you will need to use the .copy() method.
        - Edit the second line of code to be the following:
            list_2 = list_1.copy()
    - Execute this file a few more times and watch how the numbers change each time.
        - This is normal and expected behavior.
        - Each time the script is executed, it uses a different location in memory.
          This is just how computers operate.
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Loops
"""
Loop practice 1: FOR LOOPS
    - Create a list containing the following values: 1, 2, 3, 4, 5, 6, 7
    - Create a simple 'for' loop that iterates through the list and prints the value at each iteration.
    - Before the for loop, create a variable called "charge" and assign it a value between 2 and 6 (your choice)
    - Update the for loop to print the message "Not enough charge" if the value at that iteration is below the "charge"
    - Add a statement to print "Minimum charge reached" once the "charge" value is reached.
    - Add another statement to print "Overcharge Achieved!" if the value of the charge is greater than "charge"

Loop practice 2: WHILE LOOPS
    - Create two variables and assign each of them a number between 5 and 10.
    - Add the numbers together.  Take the new value and add it to the highest value from the previous operation.
        - example: 5 + 6 = 11  --> 6 + 11 = 17 --> 9 + 17 = 28 ...
    - Continue this operation until you reach or surpass 100,000,000 (1 million)
    - Print the total number of permutations it took to reach 100,000,000 (1 million).
    
BONUS: Loop practice 3:
    - GOAL: Iterate through a list of numbers and continuously add 1 until it equals the largest number in the list.
            Keep track of the iterations.
            Once the number reaches the largest number, move to the next number in the list.
            Repeat for every number in the list.
            Display how many iterations it took at the end.
            NOTE: This is not the most efficient way to get the answer but it is good practice for using loops.
    - Create a list containing the same values as practice 1.
    - Create a 'for' loop to iterate through the list
    - Nest a 'while' inside the 'for' loop to do the math.
    - Do not forget to include a way to break out of the 'while' loop or you may get stuck in an infinite loop.

"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Dictionaries
"""
Dictionaries practice 1:
    - Using the names of random people
        - Create 3 different dictionaries to simulate a phone book:
        - Each dictionary should include:
            - The person's name (first and last)
            - The person's age (as an integer)
            - The person's phone number (whatever format you like)
            - The person's address
    - Add the dictionaries to a list called 'contact_list'
    - Search through the list and return the name of the oldest person.
    - Congratulations, you just made a new friend!
        - Update the list with your new contact.
        - Be sure to include all of the required information
Dictionaries practice 2:
   - Recreate practice 1 but this time, use a dictionary of dicts RATHER THAN the list of dicts from before.
   
   
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Functions
"""
Functions practice 1:
    -
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Imports
"""
Imports practice 1:
    -
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  File Manipulation
"""
File Manipulation practice 1:
    -
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________


#  Classes
"""
Classes practice 1:
    -
"""
# _______________________ Begin Coding Here _______________________

# ________________________ End Coding Here ________________________



# LOOP SOLUTIONS:
"""
LOOP Practice 2 Example Solution: (with documentation)
    # Creating initial values and initializing the two total variables
    num_small = 5
    num_large = 6
    total_sum = 0
    total_permutations = 0
    # Creating the while loop that ends at 1 million
    while total_sum < 1000000000:
        # Performing the basic mathematical operation
        total_sum = num_small + num_large
        # Tracking the total permutations
        total_permutations += 1
        # Re-assigning the values to the newly created values
        num_small = num_large # old large is new small
        num_large = total_sum # total is new large
    # Printing the total number of permutations at the end
    print(f"{total_permutations = }")

BONUS: LOOP Practice 3 Example Solution:
    my_list = [1, 2, 3, 4, 5, 6, 7] # Creating the list
    total_additions = 0 # Setting the counter to start at 0
    # Sorting the list to insure it is arranged from low to high then iterating through.
    for number in sorted(my_list):
        large_number = my_list[-1] # Setting the 'large_number' to the last value in the sorted list.
        # Creating a while loop to continue until the number is less than or equal to the large_number
        while number <= large_number:
            number += 1 # Incrementing the number by 1
            total_additions += 1 # Incrementing the counter by 1
    # Printing the total number of additions required to achieve the goal
    print(f"{total_additions = }")
"""
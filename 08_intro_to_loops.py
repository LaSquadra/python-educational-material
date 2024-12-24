# coding=utf-8
"""
Loops:  'for' & 'while'

Loops are used to iterate over sequences of data.
This is where the concept of 'iterable' comes into play.
There are two types of loops in Python:
    - for
    - while
"for" loops are used to iterate over a sequence of data.
for looks are very simple conscptually:
    - You define a sequence of data
    - You define a variable to hold the current value of the sequence
    - You define the logic to execute for each value in the sequence
    - You define the logic to execute when the loop is finished
The syntax for a "for" loop is as follows:
    for <variable> in <sequence>:
        <logic>
Example:
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)
"""

# We will explore using 'for' loops below.
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# The above loop will iterate over the list 'my_list' and print each item in the list to the console.
# The output will be:
# 1
# 2
# 3
# 4
# 5

# We can also use loops to iterate over strings.
my_string = "Hello World"
for character in my_string:
    print(character)

# The above loop will iterate over the string 'my_string' and print each character in the string to the console.
# The output will be:
# H
# e
# l
# l
# o
#
# W
# o
# r
# l
# d

"""
while loops:
    - while loops are used to execute a block of code until a condition is met.
    - The syntax for a while loop is as follows:
        while <condition>:
            <logic>
    - The condition is evaluated before each iteration of the loop.
    - If the condition is True, the logic inside the loop is executed.
    - If the condition is False, the loop is exited.
    - while loops are useful when you do not know how many iterations you need to perform.
    - Be careful when using while loops as they can cause an infinite loop if the condition is never met.
Example:
    counter = 0
    while counter < 5:
        print(counter)
        counter += 1  # <-- This is the same as  counter = counter + 1
"""

# We will explore using 'while' loops below.
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# The above loop will iterate until the 'counter' variable is equal to 5.
# The output will be:
# 0
# 1
# 2
# 3
# 4

"""
When using a loop, it is likely you will want to break out of the loop before it gets to the end.
This is frequently used to exit 'while' loops but can also be useful within 'for' loops.
"""
# Take a look at the following code block:
is_true = True
count = 0
while is_true:
    if count <= 10:
        print(count)
        count +=1
    else:
        count = 0

"""# In this example, the code will count from 0 to 10 and print that to the screen.
Once it hits 10 it will reset the counter back to 0 and repeat the process forever

If we do not wish to repeat this forever we have two methods of breaking out of the loop:
    1) We can change the value of "is_true" and make it "False" once we get to 10
        OR
    2) We can use the 'break' keyword.
"""

# Here is how the code will look with the two options:
# Option 1:
is_true = True
count = 0
while is_true:
    if count <= 10:
        print(count)
        count +=1
    else:
        count = 0
        is_true = False

# Option 2:
is_true = True
count = 0
while is_true:
    if count <= 10:
        print(count)
        count +=1
    else:
        count = 0
        break

# Let's take a look at how this would work with a 'for' loop:
secret_number = 8
for number in range(10):  # The range function essentially creates a list which can be iterated through.
    if number != secret_number:
        print("This is not the number you are looking for!")
    elif number == secret_number:
        print(f"You found it!  The number was: {number}")

"""
In the above example, we are setting a 'secret number" that we want the code to find and return to us.
If you run the code you will see that it will print the string from the 'if' block until it hits the secret number.
That is exactly what we want it to do.  What we may not want it todo, however, is continue on after we found it.
Currently, the code will continue until the list has been exhausted (it will check against 9 and 10)

If we want to stop this after we hit the secret number we simply need to add the 'break' keyword.
"""
# Look how it functions now:
secret_number = 8
for number in range(10):
    if number != secret_number:
        print("This is not the number you are looking for!")
    elif number == secret_number:
        print(f"You found it!  The number was: {number}")
        break
        
"""
There is one more keyword that you should know off hand has well: continue
'continue' is used when you want to jump back to the top of the code block inside the loop without executing any
code past it for that specific iteration.
Let's use our 'secret number' loop as an example:
"""
secret_number = 8
for number in range(10):
    if number != secret_number:
        continue
    elif number == secret_number:
        print(f"You found it!  The number was: {number}")
        break
# Now the code will hit the 'if' block and then reset back to the top on with the next number.
# It will only print something to the screen if it finds the secret number.


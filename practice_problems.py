# coding: utf-8
"""Practice Problems for Python Educational Material.

Use this file as a workbook. Each section matches one lesson file.

Suggested workflow:

1. Read the matching lesson file.
2. Write your solution under the practice prompt.
3. Run this file.
4. Comment out finished solutions before moving to the next section.
"""


# ---------------------------------------------------------------------------
# Basic Data Types
# ---------------------------------------------------------------------------
"""Practice 00: Basic data types.

- Create one example of each basic data type:
  - string
  - integer
  - float
  - boolean
  - list
  - tuple
  - set
  - dictionary
- Print each value.
- Print the type of each value with `type()`.
- Try at least one method or helper from the lesson's toolbox preview.
- Bonus: choose two data types and explain, in comments, what kind of
  information each one is useful for storing.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------------
"""Practice 01: Variables.

- Create a variable called `my_favorite_number`.
- Create a variable called `my_age`.
- Print both variables.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Strings
# ---------------------------------------------------------------------------
"""Practice 02: Strings.

- Create `string_1` with the value `"Hello"`.
- Create `string_2` with the value `"World!"`.
- Print each variable.
- Create `concatenated_string` that combines them with a space.
- Create `my_name` with your first and last name.
- Print the first character in your name.
- Print your initials.
- Print your name in reverse.
- Try at least three string methods, such as `.upper()`, `.strip()`,
  `.replace()`, `.count()`, `.startswith()`, or `.endswith()`.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Booleans
# ---------------------------------------------------------------------------
"""Practice 03: Booleans.

- Create one variable with the value `1`.
- Create another variable with the value `0`.
- Print both values.
- Convert each value with `bool()` and print the result.
- Create an empty string and print `bool(empty_string)`.
- Use `and`, `or`, and `not` in at least one example each.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Comparison Operators
# ---------------------------------------------------------------------------
"""Practice 04: Comparison operators.

- Create `int_5` with the integer `5`.
- Create `str_5` with the string `"5"`.
- Print the result of `int_5 == str_5`.
- Convert `str_5` to an integer.
- Print the result of comparing `int_5` to the converted value.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Flow Control and Conditionals
# ---------------------------------------------------------------------------
"""Practice 05: Flow control and conditionals.

- Create a number variable that stores a temperature.
- Use `if` and `else` to print one message when the temperature is warm enough
  and another message when it is not.
- Create a score variable.
- Use `if`, `elif`, and `else` to print a grade or feedback message.
- Bonus: create boolean variables and combine them with `and`, `or`, or `not`
  inside a conditional.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Integers and Floats
# ---------------------------------------------------------------------------
"""Practice 06: Integers and floats.

- Create two number variables.
- Calculate the area of a right triangle using those values.
- Calculate the volume of a rectangular box where height is half the width.
- Try at least two number helpers, such as `abs()`, `round()`, `min()`,
  `max()`, or `sum()`.
- Bonus: automate a calculation you use in daily life.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Lists
# ---------------------------------------------------------------------------
"""Practice 07: Lists.

- Create a list containing: `1`, `2`, `"a"`, `"b"`, `9`, `"A"`.
- Print the first value.
- Print the last value.
- Change the fourth value to `"I am a new value!"`.
- Use `.append()` to add one new value.
- Use `.insert()` to add one new value near the beginning.
- Use `.remove()` or `.pop()` to remove one value.
- Sort a list of numbers.
- Use `.copy()` to create an independent copy of a list.
- Try at least two more list methods, such as `.extend()`, `.reverse()`,
  `.index()`, or `.count()`.
- Print a slice of the list.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Tuples and Sets
# ---------------------------------------------------------------------------
"""Practice 08: Tuples and sets.

Tuples:
- Create a tuple that stores three related values, such as a student record,
  screen size, or RGB color.
- Print the whole tuple.
- Print one value by index.
- Use `.count()` or `.index()` on a tuple.
- Add a comment explaining why a tuple might be better than a list here.

Sets:
- Create a set with at least one duplicate value.
- Print the set and notice that duplicates are removed.
- Use `.add()` to add one value.
- Use `.discard()` to remove one value safely.
- Create a second set and use `.union()`, `.intersection()`, or `.difference()`.
- Add a comment explaining when a set might be useful.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Loops
# ---------------------------------------------------------------------------
"""Practice 09: Loops.

For loop:
- Create a list containing `1` through `7`.
- Print each value with a `for` loop.
- Create a string and print each character with a `for` loop.

While loop:
- Start a counter at `0`.
- Use a `while` loop to print the counter while it is less than `5`.
- Increase the counter by `1` each time through the loop.

Break and continue:
- Use `break` to stop a loop when it finds a target number.
- Use `continue` to skip numbers that do not match a target number.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Dictionaries
# ---------------------------------------------------------------------------
"""Practice 10: Dictionaries.

- Create a dictionary that stores information about one student.
- Include keys for name, age, and course.
- Print the whole dictionary.
- Print one value by using its key.
- Add a new key-value pair.
- Change the value of one existing key.
- Use `.get()` to read a value with a fallback.
- Use `.keys()` or `.values()` to inspect the dictionary.
- Loop through the dictionary with `.items()` and print each key and value.
- Try one more dictionary method, such as `.update()`, `.pop()`, or `.copy()`.
- Bonus: create a dictionary that stores two student dictionaries inside it.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------
"""Practice 11: Functions.

- Write a function that accepts a name and returns a greeting.
- Write a function that accepts a name, age, and hobby, then returns a sentence.
- Write a function that accepts two numbers and returns their sum.
- Write a function that accepts a list of numbers and returns the total.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
"""Practice 12: Imports and modules.

- Import `Path` from `pathlib`.
- Print the current working directory.
- Import `math`.
- Use `math.pi` to calculate the area of a circle.
- Print the value of `__name__`.
- Add an `if __name__ == "__main__":` guard that calls a `main()` function.
- Add one comment explaining the difference between a module and a class.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# File Manipulation
# ---------------------------------------------------------------------------
"""Practice 13: File manipulation.

- Create a file called `student_notes.txt`.
- Write three lines of notes into it.
- Read the file back and print its contents.
- Append one more line, then read it again.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------
"""Practice 14: Classes.

- Create a `Book` class.
- Add `title`, `author`, and `page_count` attributes.
- Add a method that returns a readable book description.
- Create two book instances and print their descriptions.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Errors and Exceptions
# ---------------------------------------------------------------------------
"""Practice 15: Errors and exceptions.

- Write a function that divides two numbers.
- Use `try` and `except` to handle division by zero.
- Add an `else` block that prints the result when division succeeds.
- Add a `finally` block that prints a message after the attempt.
- Write another function that converts text to an integer and handles
  `ValueError`.
- Bonus: raise a `ValueError` when a list of scores is empty.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Packages and Virtual Environments
# ---------------------------------------------------------------------------
"""Practice 16: Packages and virtual environments.

- Print the command to create a virtual environment.
- Print the command to activate it in Windows PowerShell.
- Print the command to install one package with `python -m pip`.
- Create a string that looks like a small `requirements.txt` file.
- Print the command to install packages from `requirements.txt`.
- Add a comment explaining why virtual environments are useful.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# JSON
# ---------------------------------------------------------------------------
"""Practice 17: JSON.

- Import `json`.
- Create a Python dictionary that stores information about a student.
- Convert the dictionary to a JSON string with `json.dumps()`.
- Convert a JSON string back to Python data with `json.loads()`.
- Write the student dictionary to a `.json` file.
- Read the `.json` file back and print one value from it.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# API Calls
# ---------------------------------------------------------------------------
"""Practice 18: API calls.

- Create variables for a sample API URL, status code, headers, and JSON body.
- Print the request URL and an example request header.
- Print the sample status code.
- Parse the JSON body with `json.loads()`.
- Print one value from the parsed response.
- Add a comment explaining why API keys should be kept secret.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Environment Variables
# ---------------------------------------------------------------------------
"""Practice 19: Environment variables.

- Import `os`.
- Read one common environment variable with `os.environ.get()`.
- Read an optional setting and provide a fallback value.
- Check whether a fake API key environment variable is set.
- Print shell examples for setting an environment variable.
- Do not print a real secret value.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Multithreading
# ---------------------------------------------------------------------------
"""Practice 20: Multithreading.

- Import `threading`.
- Write a small function that accepts a name and prints a message.
- Create at least two `threading.Thread` objects that call that function.
- Start each thread.
- Use `.join()` to wait for each thread to finish.
- Bonus: use a `threading.Lock` while updating a shared counter.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Multiprocessing
# ---------------------------------------------------------------------------
"""Practice 21: Multiprocessing.

- Import `multiprocessing`.
- Write a function that squares a number.
- Create a `multiprocessing.Process` that calls a function.
- Start the process and join it.
- Add a comment explaining why multiprocessing code belongs under the
  `if __name__ == "__main__":` guard on Windows.
- Bonus: use `ProcessPoolExecutor` to square a list of numbers.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Ollama
# ---------------------------------------------------------------------------
"""Practice 22: Ollama.

- Create a variable for the Ollama chat API URL.
- Create a dictionary payload with a model name, messages, and `stream: False`.
- Convert the payload to JSON text with `json.dumps()`.
- Print the setup commands for pulling and running a local model.
- Add a comment explaining one reason someone might use a local model.
- Bonus: write a guarded function that tries an Ollama request and skips
  cleanly if the service is not running.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# OpenAI API
# ---------------------------------------------------------------------------
"""Practice 23: OpenAI API.

- Import `os`.
- Check whether `OPENAI_API_KEY` is set.
- Print the basic OpenAI client code shape shown in the lesson.
- Add a comment explaining why API keys should come from environment variables.
- Bonus: write a guarded function that imports `OpenAI` and skips cleanly if
  the package or API key is missing.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Building a Chatbot
# ---------------------------------------------------------------------------
"""Practice 24: Building a chatbot.

- Create an `EchoProvider` class with a `.chat()` method.
- Create a `Chatbot` class that stores a list of messages.
- Add a method that saves a user message, gets a provider reply, and stores the
  assistant reply.
- Run a short scripted conversation with two user messages.
- Bonus: write an optional input loop that stops when the user types `quit`.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Embeddings
# ---------------------------------------------------------------------------
"""Practice 25: Embeddings.

- Write a function that calculates cosine similarity between two vectors.
- Write a simple function that turns text into a tiny practice vector.
- Compare one query vector against at least three example text vectors.
- Print each similarity score.
- Bonus: write a guarded OpenAI embedding function that skips cleanly if the
  API key or package is missing.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# RAG
# ---------------------------------------------------------------------------
"""Practice 26: RAG.

- Create a small list of document dictionaries with `title` and `text` keys.
- Write a function that splits documents into smaller chunks.
- Write a simple keyword scoring function.
- Retrieve the best chunks for a question.
- Build an answer string from the retrieved chunks.
- Add a comment explaining where embeddings could improve the retrieval step.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# AI Agents
# ---------------------------------------------------------------------------
"""Practice 27: AI agents.

- Create at least two small tool functions.
- Store the tools in a dictionary called `TOOLS`.
- Write a simple fake model function that chooses a tool based on user text.
- Write an agent function that runs the selected tool.
- Print the result for a few example user requests.
- Add a comment explaining that real agents still need approved tools chosen
  and executed by your Python code.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Optional: Data Type Design and Performance
# ---------------------------------------------------------------------------
"""Optional Practice: Data type design and performance.

- Create the same small collection as a list, tuple, set, and dictionary.
- Use `sys.getsizeof()` to compare their approximate memory sizes.
- Write one comment explaining why those numbers are only a rough comparison.
- Create a large list of numbers and a set from that list.
- Use `time.perf_counter()` to compare one membership check in each collection.
- Create a list of student dictionaries and a dictionary keyed by student ID.
- Look up one student by scanning the list, then by using the dictionary key.
- Add comments explaining when you would choose:
  - a list
  - a tuple
  - a set
  - a dictionary
- Bonus: find one part of an earlier practice solution where a different data
  type might make the code clearer, faster, or smaller.
"""

# Write your solution here.


# ---------------------------------------------------------------------------
# Example Solutions
# ---------------------------------------------------------------------------
"""Loop Practice 09 while-loop example.

counter = 0

while counter < 5:
    print(counter)
    counter += 1
"""

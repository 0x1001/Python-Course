Lesson 7 - List comprehension 
------------------------------------------------------------------------------------------------------------------------

Python offers very simple way of creating all kinds of lists which is called list comprehensions.
This approach requires different way of thinking about loops. Best way to learn it is to try it.
Here is a description:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

Here is another good description:
http://www.pythonforbeginners.com/basics/list-comprehensions-in-python

Basic usage:
[ expression for item in list if conditional ]

Very useful built in function that works well with list comprehensions is range():
https://docs.python.org/3/library/stdtypes.html#typesseq-range

It allows to generate simple sequences of integer numbers.
Usage:
range(stop)
range(start, stop[, step])

Some list comprehension examples:
Generate even numbers:
>>> [i for i in range(50) if i%2 == 0]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

Generate square numbers:
>>> [i**2 for i in range(20)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

Convert string to letters:
>>> [letter for letter in "Hello World!"]
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

Generate multiplication table for 10:
>>> [x*z for x in range(10) for z in range(10)]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 0, 9, 18, 27, 36, 45, 54, 63, 72, 81]

Python also supports:
Set comprehensions: {i**2 for i in range(10)}
Dict comprehensions: {i:i**2 for i in range(10)}
Generator comprehensions: (i**2 for i in range(10))


Exercise:
I would like you to write list comprehensions for following tasks.
In your folder create file Lesson_7/list_comprehensions.py. In this file create following functions:

1. Create function only_letters(text) that accepts string and returns list with only ascii letters (without " ", ".", "!", ...).
Hint: to check if letter is an ascii letter you can use: letter in string.ascii_letters

Example:
Input: "Hello world!"
Output: ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

2. Create function unicode_to_integer(text) that accepts unicode string and returns list of integers that correspond to unicode code point.
To convert character to integer value use built in function ord(c):
https://docs.python.org/3/library/functions.html#ord

Example:
Input: "Hello world!"
Output: [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]

3. Create function extract_integers(things) that accepts list of different type objects and returns list of only integers.
Hint: to check if item is integer use built in function: isinstance()
https://docs.python.org/3/library/functions.html#isinstance

Example:
Input: ["heLLo", "world", 0.234, None, 1, object(), 10, (100, 200, 300)]
Returns: [1, 10]

4. Create function flat_matrix(matrix) that accepts a list of lists and returns one list with all elements from all lists.

Example:
Input: [[5, 6, 10], [5, 5, 5], [-1, 20, 1]]
Returns: [5, 6, 10, 5, 5, 5, -1, 20, 1]

5. Create function list_to_dict(elements) that transforms list to dict. Each element in dict should have a key that is its index in the list.
Hint: use built in function enumerate().
https://docs.python.org/3/library/functions.html#enumerate

Example:
Input: [None, "hello", "1", 1]
Returns: {0: None, 1: "hello", 2: "1", 3: 1}


I prepared set of test cases you have to pass.
To run them add at beginning of your file:
import unittest

And at the end:
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_7"))

File Course/Lesson_7/list_comprehension_template.py is a solution template that you can use as starting point. Copy it to your solution folder and rename it to list_comprehension.py.

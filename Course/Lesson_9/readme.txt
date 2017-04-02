Lesson 8 - Set, Frozen set and tuple
------------------------------------------------------------------------------------------------------------------------

Set and Frozen set contain only unique elements in arbitrary order.
Set is mutable. Frozen set is immutable.
https://docs.python.org/3/tutorial/datastructures.html#sets
https://docs.python.org/3/library/stdtypes.html#set
http://www.python-course.eu/python3_sets_frozensets.php

Set and Frozen set are implementation of an abstract data type called set.
https://en.wikipedia.org/wiki/Set_(abstract_data_type)

Short summary:
set_variable = set()                               # Creates empty set
frozenset_variable = frozenset()                   # Creates empty frozenset
set_variable = {"hello", "world"}                  # Creates set with initial elements
set_variable = set(["hello", "world"])             # Creates set from a list (or other iterable)
frozenset_variable = frozenset({"hello", "world"}) # Creates frozenset from set
set_variable.add("Hello")                          # Adds new element to set
"Hello" in set_variable                            # Checks if element is in set
set_variable.remove("Hello")                       # Removes element from set
set_variable.discard("Hello")                      # Removes element from set if present
set_variable.isdisjoint(other)                     # Checks if two sets don't have any common elements
set_variable.issubset(other)                       # Checks if set_variable is subset of other
new_set = set_variable.union(other)                # Creates new set with elements from both sets
new_set = set_variable.intersection(other)         # Creates new set with elements that are common to set_variable and other
new_set = set_variable.difference(other)           # Creates new set with elements that are in set_variable and not in other
...

A tuple is an immutable sequence of Python objects.
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
https://docs.python.org/3/library/stdtypes.html#tuple

This type is very useful for returning multiple values from function (in this case python list works similarly but better is to use tuple).
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch07s04.html

Can be also used as function input (in this case also python list works similarly but better is to use tuple):
inputs = (1, 2, 3)               # Tuple
def some_function(a, b, c): pass # Any function definition
some_function(*inputs)           # This will unpack tuple as a, b, c input function arguments

Short summary:
tuple_variable = ()                             # Empty tuple
tuple_variable = ("hello",)                     # Tuple with one value
one, two, three = (1, 2, 3)                     # Unpacks tuple to three variables
variable_1, variable_2 = variable_2, variable_1 # Swaps values of variables without temporary variable
def example(): return 1, 2, 3                   # Defines function that returns three values

Exercise:
In Solutions under your folder create Lesson_9/set_and_tuple.py file.

1. Create function not_present_letters(text) that accepts a string as an input and returns a set with ascii letters that are not present in that sentence.
Hint: All ASCII letters are here: string.ascii_letters
Example:
Input: "Hello world ABCDEF abcdef"
Output: {'k', 'p', 's', 'x', 'G', 'Q', 'y', 'U', 'm', 'S', 'i', 'N', 'O', 'q', 'g', 'R', 'h', 'n', 'L', 'T', 'V', 'j', 'K', 'P', 'v', 'I', 'J', 'W', 'Y', 'X', 'Z', 't', 'z', 'u', 'M'}

2. Create function union_intersection_difference(set_1, set_2) that accepts two sets and returns three sets: union, intersection and difference
Input: {1, 2, 3, 4, 5}, {4, 5, 6, 7}
Output: {1, 2, 3, 4, 5, 6, 7}, {4, 5}, {1, 2, 3}

3. Create function unique_words(text) that accepts string variable with words separated by space and returns tuple with all words that are in text without duplicates.
Make it case insensitive.
Hint: To split string to list of words you can use split() string method.
Input: "hello Hello world"
Returns: (hello, world)

I prepared set of test cases you have to pass
To run them add at beginning of your file:
import unittest

And at the end:
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_9"))

File Course/Lesson_9/set_and_tuple_template.py is a solution template that you can use as starting point. Copy it to your solution folder and rename it to set_and_tuple.py.
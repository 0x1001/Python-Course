Lesson 8 - Dictionaries - Word Frequencies
------------------------------------------------------------------------------------------------------------------------

Python dictionary is an implementation of an abstract data type called associative array.
https://en.wikipedia.org/wiki/Associative_array
https://en.wikipedia.org/wiki/Hash_table

It maps keys to values where key can't be a mutable object and value can be any object.
Pairs key, value are stored in arbitrary order in dictionary. Meaning there is no order.

You can find all the information on syntax and dictionary methods in here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
http://www.python-course.eu/python3_dictionaries.php

Short summary:
dictionary_variable = {}                              # Creates empty dictionary
dictionary_variable = dict()                          # Creates empty dictionary
dictionary_variable["Hello"] = "World"                # Assigns to key "Hello" value "World"
value = dictionary_variable["Hello"]                  # Retrieves value from dictionary for key "Hello"
keys = list(dictionary_variable.keys())               # Returns list of all keys
values = list(dictionary_variable.values())           # Returns list of all values
keys_and_values = list(dictionary_variable.items())   # Returns list of all key, value paris stored as a list of tuple.
del dictionary_variable["Hello"]                      # Deletes key, value pair
value = dictionary_variable.pop("Hello")              # Deletes key, value pair and returns value
...

Exercise:
Create a file Lesson_8/dictionaries.py in your folder in Solutions.

1. Write function word_frequencies(words) that accepts list of words and returns dictionary with words as keys and values as numbers of words occurrences in the list.
Make it insensitive to letter case.
Example:
Input: ["Hello", "hello", "world"]
Output: {"hello": 2, "world": 1}

2. Write function most_occurring_words(words_freq) that accepts dictionary with word frequencies like the one generated in point 1.
This function should return a list of words that occurred the most, have the highest frequency.

Example:
Input: {"hello": 2, "world": 1}
Output: ["hello"]

3. Write function sum_word_frequencies(words_freq_1, words_freq_2) that accepts two dictionaries with word frequencies and returns one dictionary that is a sum of these two inputs.
Example:
Input: {"hello": 2, "world": 1}, {"hello": 2, "world": 1, "today": 1}
Output: {"hello": 4, "world": 2, "today": 1}

I prepared set of test cases you have to pass.
To run them add at beginning of your file:
import unittest

And at the end:
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_8"))

File Course/Lesson_8/dictionaries_template.py is a solution template that you can use as starting point. Copy it to your solution folder and rename it to dictionaries.py.
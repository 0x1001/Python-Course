Lesson 6 - List - Sorting
------------------------------------------------------------------------------------------------------------------------

In this lesson we will play with python lists:
http://effbot.org/zone/python-list.htm
https://docs.python.org/3.5/tutorial/datastructures.html

Short summary:
list_variable = []                    # Creates an empty list
list_variable = list()                # Creates an empty list
list_variable = ["hello"] + ["world"] # Creates new list that is a sum of two other lists
list_variable = ["hello"] * 10        # Creates new list that contains 10 items with value "hello"
new_list = list_variable[:]           # Creates a shallow copy of the list (What is shallow copy: https://docs.python.org/2/library/copy.html)
new_list = list_variable[1:5]         # Creates a slice of the list from item 1 to item 5 excluded.
value = list_variable[-1]             # Retrieves last item from the list
list_variable.append("hello")         # Adds new item to the list
value = list_variable[0]              # Retrieves item 0 from the list
list_variable.pop(0)                  # Removes item 0 from the list
list_variable.sort()                  # Sorts in place the list
list_variable.reverse()               # Reverses the order of the list, in place
new_list = list_variable[::-1]        # Reverses the order of the list, creates new list
list_variable.extend(["world"])       # Extends the list with items from another list
...

I want you to implement two sorting algorithms for integers.
Python offers built in function sorted().
https://docs.python.org/2/library/functions.html#sorted
Which can do sorting of any iterable object.
Also python list has sort() method that sorts given list in place.
But for this exercise don't use them.

In your folder create integer_sort.py file.

1. Insertion sort
https://en.wikipedia.org/wiki/Insertion_sort
Create function called insertion_sort(data).
"data" is list of integers.

2. Merge sort
https://en.wikipedia.org/wiki/Merge_sort
Create function called merge_sort(data).
"data" is list of integers.

These functions should return new sorted lists, without changing input data.
Time complexity of insertion sort is O(n^2) and Merge sort is O(nlogn).
Which means for big lists merge sort runs much faster then insertion sort.
https://en.wikipedia.org/wiki/Time_complexity

I prepared set of test cases you have to pass.
To run them add at beginning of your file:
import unittest

And at the end:
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_6"))

------------------------------------------------------------------------------------------------------------------------
Hint 1:
In python you can swap two variables by doing:
a = 1
b = 5
a, b = b, a
Without temporary variable.

Hint 2:
If you want to make a copy of entire list you can do:
l1 = [1, 2, 3, 4]
l2 = l1[:]
This creates new list with same references to integers, which means integers are not copied.
Python indexing is very powerful. You can read about this:
http://effbot.org/zone/python-list.htm

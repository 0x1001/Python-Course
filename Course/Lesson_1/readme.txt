Lesson 1 - Getting help

In this lesson I want to show you how to get help in python itself and how to write your own help.
By help I mean documentation for code (Functions, Classes, Modules).

Like in Lesson 0 create a function that prints "Hello World" and call it under: if __name__ == "__main__".

Next I want you to document your function.
Python uses docstring concept for documentation here are few links you can read:
https://en.wikipedia.org/wiki/Docstring
https://www.python.org/dev/peps/pep-0257/
http://www.pythonforbeginners.com/basics/python-docstrings

Using docstrings you can document modules, classes, functions, methods.

Create a simple docstring for your function and for your file (module).
Under if __name__ == "__main__" use built in python function "help" to print documentation for your function.

Next print documentation for few other things:
 - help(help)
 - help(int)
 - help(str)
 - help(__name__)
 - Import os module and try: help(os), help(os.path)

Python docstring is understood by Doxygen.
Which means you can generate complete documentation for your project directly from source code.
So it is useful to keep up to date docstrings for at least public APIs.

Next useful built-in function I want you to try is dir() function.
https://docs.python.org/2/library/functions.html#dir

Allows to display available attributes for given object.
This is useful when you try to figure out possible methods and attributes of an object of interest.
In python everything is an object and has some attributes and methods!

In your code try this:
    - print(dir(your_function_name))
    - print(dir("string"))
    - print(dir(1))
    - Import os and print(dir(os))

Next useful built in function is type().
https://docs.python.org/2/library/functions.html#type

Which returns type of an object of interest.

Try this:
    - print(type(1))
    - print(type(your_function_name))
    - print(type(type))
    - print(type(os))

Since python is dynamically typed language very often you don't know what function returns.
It can happen that function returns many different types depending on its input.
Using type() can be very helpful when you have to figure out objects types.


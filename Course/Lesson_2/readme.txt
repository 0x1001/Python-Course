Lesson 2 - Python types

Here is a long list of python standard types:
https://docs.python.org/3/library/stdtypes.html

In general in about 80%-90% cases in your code you will use following types:
    - Classes
    - Functions (Yes, function is an object of type 'function')
    - Lists - [] - list()
    - Dictionaries - {} - dict()
    - strings - "" - str()
    - Ints - 1 - int()
    - Floats - 1.0 - float()
    - Boolean - True/False - bool()
    - Null object - None
    - Tuple - () - tuple()

Try to get familiar with these types.

1. Python is dynamically typed and strongly typed.
Dynamically typed means that variable is not bound to a type.
Variable type can change during program run time.
Strongly typed means that you can perform operations on variable that are only valid for its current type.

More info:
https://en.wikipedia.org/wiki/Strong_and_weak_typing
http://stackoverflow.com/questions/2690544/what-is-the-difference-between-a-strongly-typed-language-and-a-statically-typed

You can test this concept by doing following things:
- [0, 1] + 1 # Error
- [0, 1] + [2, 3] # No Error
- "Test " + 123 # Error
- "Test" + str(123) # No Error
- a = []
  print(type(a)
  a = True
  print(type(a))

2. Python variables can be divided into mutable and immutable.
Variables like bool, int, str, tuple, (...) once created cannot be changed.
Variables like list, dict, set, (...) can be modified during program runtime.

More information is here:
https://codehabitude.com/2013/12/24/python-objects-mutable-vs-immutable/
https://en.wikibooks.org/wiki/Python_Programming/Data_Types#Mutable_vs_Immutable_Objects

3. Variables are references to objects within given scope.
Everything is passed by reference but it is not the same reference concept as in C/CPP.
Here is nice reading on this topic:
http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html

4. Python is managed language with garbage collection.
Python is using reference counting. Once object is not reference anywhere anymore, is being deallocated.
Additionally from time to time python tries to detect and remove reference cycle.

More information here:
https://www.quora.com/How-does-garbage-collection-in-Python-work

You can check what is current reference count on an object by doing:

import sys
print(sys.getrefcount(True))
print(sys.getrefcount(False))
print(sys.getrefcount(1))
print(sys.getrefcount(object))

print("Immutable")
aaa = 5555555
print(sys.getrefcount(5555555))
bbb = 5555555
print(sys.getrefcount(5555555))

print("Mutable")
a = [5555555]
print(sys.getrefcount([5555555]))
b = [5555555]
print(sys.getrefcount([5555555]))

This gives an idea of how python manages memory. Python is reusing immutable objects to conserve memory.

As an exercises for this lesson write short program that uses all types that were mentioned here.
For each type display all possible operations and attributes. For this use function dir().

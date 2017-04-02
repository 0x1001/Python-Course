Lesson 3 - Integers - RSA Algorithm implementation

RSA Algorithm is quite simple. You can read about it here:
https://simple.wikipedia.org/wiki/RSA_(algorithm)

Short summary:
integer_variable = 0               # Creates an integer variable with value 0
integer_variable = int(0)          # Creates an integer variable with value 0
new_integer = integer_variable + 1 # Adds one to the integer variable
new_integer = integer_variable - 1 # Subtracts one from the integer variable
new_integer = integer_variable * 1 # Multiplies by one the integer variable
new_integer = integer_variable / 1 # Divides by one the integer variable
integer_variable += 1              # Increments by 1 the integer variable
...

I want you to implement two functions: one for encoding rsa and the other for decoding.
In your folder create rsa.py file. Put all your functions into that file. Use suggested below function names.

1. Implement simple version of RSA without any optimizations rsa_encode(m, n, e) and rsa_decode(c, n, d).
m - is our message for sake of simplicity it is an integer
n - is the modulus for the public key and the private keys
e - is public key exponent
d - is private key exponent

2. Implement RSA with optimizations for calculating Modular exponentiation.
rsa_optimized_encode(m, n, e) and rsa_optimized_decode(c, n, d)
https://en.wikipedia.org/wiki/Modular_exponentiation

For testing you can use following key:
Public key: n = 3233, e = 17
Private key: n = 3233, d = 2753

Python support concept of big integers. You don't have to take care of overflow.
It is possible in python to do things like 123**1234567890, but it is slow.
There is huge difference in execution time between these two implementations of RSA.

I prepared tests for this exercise using python unittest framework.
https://docs.python.org/3/library/unittest.html

To run these tests add to your rsa.py:
At the beginning:
import unittest

In the end:
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_3"))

You can run your rsa.py from pyCharm directly or via command line: python rsa.py.
In console output you will see tests results.

File Course/Lesson_3/rsa_template.py is a solution template that you can use as starting point. Copy it to your solution folder and rename it to rsa.py.
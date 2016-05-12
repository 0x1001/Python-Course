#all code that is at indentation level 0 gets executed no matter if __name__ == "__main__" condition applied.

def func():
    print("5. It's func()")

print("1. run func.py directly and see the output, and then compare the output by running main.py")

print("2. if func.py is running directly then the __name__ variable will be __main__, otherwise it contains the name of the caller")

if __name__ == "__main__":
    print("3. func() called directly: __name__ = " + __name__)
else:
    print("4. func() is imported within another module: __name__ = " + __name__)


# To test the module, this part of the code will not be executed if the module is imported by other modules
if __name__ == "__main__":
    func()
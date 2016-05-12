"""
This is the main file for lesson 1.
"""
import os


def main():
    """
    This is a function docstring.

    :return: None
    """
    print("Hello World")

    # documentation for this module
    print(help(__name__))

    # help
    print("print(help)")
    print(help(help))

    print("help(int)")
    print(help(int))

    # dir
    print("\n\ndir function for integer:")
    print(dir(123))

    print("\n dir function for os:")
    print(dir(os))

    # type
    print("\n\nType of an integer:")
    print(type(123))

    print("Type of a string:")
    print(type("this is a test string"))

    print("Type of OS:")
    print(type(os))

if __name__ == '__main__':
    # This is an inline comment
    # Not shown in docstring
    main()

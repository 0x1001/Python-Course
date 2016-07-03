"""
This is lesson_1.py file in Python-Course
"""

import os

def main():
    """
    Prints Hello World + some docstring
    """
    print ("Hello World")

    #docstring for whole file
    help(__name__)

    #docstring for  function main()
    help(main)

    #docstring for several other things
    help(help)
    help(int)
    help(str)
    help(os)
    help(os.path)

    #dir
    print("\n###################### DIR ######################\n")

    print("function main")
    print(dir(main))

    print("string")
    print(dir("string"))

    print("1")
    print(dir(1))

    print("os")
    print(dir(os))

    #type
    print("\n###################### TYPE ######################\n")

    print("1")
    print(type(1))

    print("function main")
    print(type(main))

    print("type")
    print(type(type))

    print("os")
    print(type(os))

if __name__ == '__main__':
    #call function main()
    main()
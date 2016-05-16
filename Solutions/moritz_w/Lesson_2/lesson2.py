import sys

def main():
    test_list = [0, 1, 2]
    append_list = [3, 4]

    try:
        print("new_list1 = " + str(test_list) + " + 3")
        new_list1 = test_list + 3
        print("Result: " + str(new_list1))
    except TypeError as e:
        print(e)

    try:
        print("new_list2 = " + str(test_list) + " + " + str(append_list))
        new_list2 = test_list + append_list
        print("Result: " + str(new_list2))
    except TypeError as e:
        print(e)

    print("Change type of a")
    print("List:")
    a = []
    print(type(a))
    print("Change type of a to bool")
    a = True
    print(type(a))

    print("--- Mutable Types ---")
    print("Test list: " + str(test_list))
    print("append new list")
    test_list += append_list
    print("Result: " + str(test_list))

    print("Python reference counts")
    print(sys.getrefcount(True))
    print(sys.getrefcount(False))
    print(sys.getrefcount(1))
    print(sys.getrefcount(object))

    print("Immutable types - int")
    aaa = 5555555
    print(sys.getrefcount(5555555))
    bbb = 5555555
    print(sys.getrefcount(5555555))

    print("Mutable types - list")
    a = [5555555]
    print(sys.getrefcount([5555555]))
    b = [5555555]
    print(sys.getrefcount([5555555]))

    print("Dirs of different types:")
    print("Mutable:")
    print("int   " + str(dir(int)))
    print("str   " + str(dir(str)))
    print("bool  " + str(dir(bool)))
    print("tuple " + str(dir(tuple)))
    print("Immutable:")
    print("list  " + str(dir(list)))
    print("dict  " + str(dir(dict)))
    print("set   " + str(dir(set)))

if __name__ == '__main__':
    main()

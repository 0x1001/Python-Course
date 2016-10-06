import unittest
import string


def not_present_letters(text):
    ret = set()
    for letter in string.ascii_letters:
        if letter not in text:
            ret.add(letter)
    return ret


def union_intersection_difference(set_1, set_2):
    union = set_1.union(set_2)
    intersection = set_1.intersection(set_2)
    difference = set_1.difference(set_2)

    return union, intersection, difference


def unique_words(text):
    words = [word.lower() for word in text.split()]
    return tuple(set(words))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_9"))

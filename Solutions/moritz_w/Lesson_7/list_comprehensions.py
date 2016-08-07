import unittest
import string


def only_letters(text):
    return [char for char in text if char in string.ascii_letters]


def unicode_to_integer(text):
    return [ord(char) for char in text]


def extract_integers(things):
    return [thing for thing in things if isinstance(thing, int)]


def flat_matrix(matrix):
    return [col_item for row_item in matrix for col_item in row_item]


def list_to_dict(elements):
    return {k: v for k, v in enumerate(elements)}

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_7"))

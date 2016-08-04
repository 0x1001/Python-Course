import list_comprehensions
import unittest


class TestListComprehensions(unittest.TestCase):
    def test_only_letters(self):
        self.assertEqual(list_comprehensions.only_letters("Hello World!"),
                         ["H", "e", "l", "l", "o", "W", "o", "r", "l", "d"])

        self.assertEqual(list_comprehensions.only_letters(""), [])

        self.assertEqual(list_comprehensions.only_letters(
            "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."),
             ['P', 'e', 'r', 'f', 'e', 'c', 't', 'i', 'o', 'n', 'i', 's', 'a', 'c', 'h', 'i', 'e', 'v', 'e',
              'd', 'n', 'o', 't', 'w', 'h', 'e', 'n', 't', 'h', 'e', 'r', 'e', 'i', 's', 'n', 'o', 't', 'h',
              'i', 'n', 'g', 'm', 'o', 'r', 'e', 't', 'o', 'a', 'd', 'd', 'b', 'u', 't', 'w', 'h', 'e', 'n',
              't', 'h', 'e', 'r', 'e', 'i', 's', 'n', 'o', 't', 'h', 'i', 'n', 'g', 'l', 'e', 'f', 't', 't',
              'o', 't', 'a', 'k', 'e', 'a', 'w', 'a', 'y'])

    def test_unicode_to_integer(self):
        self.assertEqual(list_comprehensions.unicode_to_integer("Hello world!"),
                         [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33])

        self.assertEqual(list_comprehensions.unicode_to_integer(""), [])

        self.assertEqual(list_comprehensions.unicode_to_integer(
            "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."),
            [80, 101, 114, 102, 101, 99, 116, 105, 111, 110, 32, 105, 115, 32, 97, 99, 104, 105, 101, 118, 101, 100, 44,
             32, 110, 111, 116, 32, 119, 104, 101, 110, 32, 116, 104, 101, 114, 101, 32, 105, 115, 32, 110, 111, 116, 104,
             105, 110, 103, 32, 109, 111, 114, 101, 32, 116, 111, 32, 97, 100, 100, 44, 32, 98, 117, 116, 32, 119, 104,
             101, 110, 32, 116, 104, 101, 114, 101, 32, 105, 115, 32, 110, 111, 116, 104, 105, 110, 103, 32, 108, 101,
             102, 116, 32, 116, 111, 32, 116, 97, 107, 101, 32, 97, 119, 97, 121, 46])

    def test_extract_integers(self):
        self.assertEqual(
            list_comprehensions.extract_integers(["heLLo", "world", 0.234, None, 1, object(), 10, (100, 200, 300)]),
            [1, 10])

        self.assertEqual(list_comprehensions.extract_integers([]), [])
        self.assertEqual(list_comprehensions.extract_integers(["Nothing"]), [])

        self.assertEqual(
            list_comprehensions.extract_integers([None, None, 0.234, None, 1, -10, 10, -50]),
            [1, -10, 10, -50])

    def test_flat_matrix(self):
        self.assertEqual(list_comprehensions.flat_matrix([[5, 6, 10], [5, 5, 5], [-1, 20, 1]]),
                         [5, 6, 10, 5, 5, 5, -1, 20, 1])

        self.assertEqual(list_comprehensions.flat_matrix([[]]), [])

        self.assertEqual(list_comprehensions.flat_matrix([[5], [6, 10, 5, 5, 5], [-1, 20]]),
                 [5, 6, 10, 5, 5, 5, -1, 20])

    def test_list_to_dict(self):
        self.assertEqual(list_comprehensions.list_to_dict([None, "hello", "1", 1]),
                         {0: None, 1: "hello", 2: "1", 3: 1})

        self.assertEqual(list_comprehensions.list_to_dict([]), {})

        self.assertEqual(list_comprehensions.list_to_dict(["h", "e", "l", "l", "o"]),
                         {0: "h", 1: "e", 2: "l", 3: "l", 4: "o"})

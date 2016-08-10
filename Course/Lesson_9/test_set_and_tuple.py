import set_and_tuple
import unittest
import string


class TestSetTasks(unittest.TestCase):
    def test_not_present_letters(self):
        self.assertEqual(set_and_tuple.not_present_letters("Hello world ABCDEF abcdef"),
                         {'k', 'p', 's', 'x', 'G', 'Q', 'y', 'U', 'm', 'S', 'i', 'N', 'O', 'q', 'g', 'R', 'h', 'n', 'L', 'T', 'V', 'j', 'K', 'P', 'v', 'I', 'J', 'W', 'Y', 'X', 'Z', 't', 'z', 'u', 'M'})
        self.assertEqual(set_and_tuple.not_present_letters(""), set(string.ascii_letters))
        self.assertEqual(set_and_tuple.not_present_letters(string.ascii_letters), set())

    def test_union_intersection_difference(self):
        self.assertEqual(set_and_tuple.union_intersection_difference({1, 2, 3, 4, 5}, {4, 5, 6, 7}),
                         ({1, 2, 3, 4, 5, 6, 7}, {4, 5}, {1, 2, 3}))

        self.assertEqual(set_and_tuple.union_intersection_difference({1, 2, 3}, {4, 5, 6, 7}),
                         ({1, 2, 3, 4, 5, 6, 7}, set(), {1, 2, 3}))

        self.assertEqual(set_and_tuple.union_intersection_difference({1, 2, 3}, {1, 2, 3}),
                         ({1, 2, 3}, {1, 2, 3}, set()))

        self.assertEqual(set_and_tuple.union_intersection_difference({1, 2, 3}, {1, 2, 3, 4, 5, 6, 7}),
                         ({1, 2, 3, 4, 5, 6, 7}, {1, 2, 3}, set()))

        self.assertEqual(set_and_tuple.union_intersection_difference(set(), set()),
                         (set(), set(), set()))

    def test_unique_words(self):
        self.assertEqual(set_and_tuple.unique_words(""), ())

        self.assertIn("hello", set_and_tuple.unique_words("hello Hello world"))
        self.assertIn("world", set_and_tuple.unique_words("hello Hello world"))
        self.assertNotIn("Hello", set_and_tuple.unique_words("hello Hello world"))

        self.assertEqual(set_and_tuple.unique_words("hello"), ("hello",))
        self.assertEqual(set_and_tuple.unique_words("heLLo"), ("hello",))


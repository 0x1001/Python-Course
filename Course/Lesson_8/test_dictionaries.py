import dictionaries
import unittest


class TestDictionaries(unittest.TestCase):
    def test_word_frequencies(self):
        self.assertEqual(dictionaries.word_frequencies(["Hello", "hello", "world"]), {"hello": 2, "world": 1})
        self.assertEqual(dictionaries.word_frequencies(["123", "123", "123"]), {"123": 3})
        self.assertEqual(dictionaries.word_frequencies([]), {})

        self.assertEqual(dictionaries.word_frequencies(
            ["Perfection", "is", "achieved", "not", "when", "there", "is", "nothing", "more", "to", "add", "but", "when", "there", "is", "nothing", "left", "to", "take", "away"]),
            {"perfection": 1, "is": 3, "achieved": 1, "not": 1, "when": 2, "there": 2, "nothing": 2, "more": 1, "to": 2, "add": 1, "but": 1, "left": 1, "take": 1, "away": 1})

    def test_most_occurring_word(self):
        self.assertEqual(dictionaries.most_occurring_words({"hello": 2, "world": 1}), ["hello"])
        self.assertIn("hello", dictionaries.most_occurring_words({"hello": 1, "world": 1}))
        self.assertIn("world", dictionaries.most_occurring_words({"hello": 1, "world": 1}))
        self.assertEqual(dictionaries.most_occurring_words({}), [])
        self.assertEqual(dictionaries.most_occurring_words({"perfection": 1, "is": 3, "achieved": 1, "not": 1, "when": 2, "there": 2, "nothing": 2, "more": 1, "to": 2, "add": 1, "but": 1, "left": 1, "take": 1, "away": 1}),
                         ["is"])

    def test_sum_word_frequencies(self):
        self.assertEqual(dictionaries.sum_word_frequencies({"hello": 2, "world": 1}, {"hello": 2, "world": 1, "today": 1}),
                         {"hello": 4, "world": 2, "today": 1})

        self.assertEqual(dictionaries.sum_word_frequencies({"hello": 2, "world": 1, "today": 1}, {"hello": 2, "world": 1}),
                         {"hello": 4, "world": 2, "today": 1})

        self.assertEqual(dictionaries.sum_word_frequencies({"hello": 2, "world": 1}, {}), {"hello": 2, "world": 1})
        self.assertEqual(dictionaries.sum_word_frequencies({}, {"hello": 2, "world": 1}), {"hello": 2, "world": 1})
        self.assertEqual(dictionaries.sum_word_frequencies({}, {}), {})

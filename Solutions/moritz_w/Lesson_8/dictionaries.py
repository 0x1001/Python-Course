import unittest


def word_frequencies(words):
    ret = {}

    for word in words:
        lower_word = word.lower()
        if lower_word not in ret:
            ret[lower_word] = 1
        else:
            ret[lower_word] += 1
    return ret


def most_occurring_words(words_freq):
    freq = 0
    most_frequent_words = []

    for word, amount in words_freq.items():
        if amount > freq:
            freq = amount
            most_frequent_words.clear()
            most_frequent_words.append(word)
        elif amount == freq:
            most_frequent_words.append(word)

    return most_frequent_words


def sum_word_frequencies(words_freq_1, words_freq_2):
    ret = {}

    for word, freq in words_freq_1.items():
        ret[word] = freq

    for word, freq in words_freq_2.items():
        if word in ret:
            ret[word] += freq
        else:
            ret[word] = freq

    return ret

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_8"))

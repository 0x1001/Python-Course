"""
Solution for lesson 3. (RSA Algorithm)
Author: Moritz Wiesinger
"""

import unittest


def main():
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_3"))


def rsa_encode(m, n, e):
    return (m ** e) % n


def rsa_decode(c, n, d):
    return (c ** d) % n


def rsa_optimized_encode(m, n, e):
    return pow(m, e, n)


def rsa_optimized_decode(c, n, d):
    return pow(c, d, n)

if __name__ == '__main__':
    main()

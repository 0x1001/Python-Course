import unittest


class PLLSetting:
    def __init__(self):
        self.index = None
        self.frequency = None
        self.settings = None


def parser(log_contents):
    # Your code here
    pass


def writer(pll_settings):
    # Your code here
    pass


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_5"))

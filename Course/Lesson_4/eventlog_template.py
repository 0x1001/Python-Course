import unittest


class LogEntry:
    def __init__(self):
        self.log_name = None
        self.source = None
        self.date = None
        self.event_id = None
        self.task = None
        self.level = None
        self.opcode = None
        self.keyword = None
        self.user = None
        self.user_name = None
        self.computer = None
        self.description = None


def parser(content):
    # Your code here
    pass


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_4"))

"""
Windows Event Log Parser
Author: Moritz Wiesinger
"""

from datetime import datetime
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
        self.description = []


def parser(content):
    """
    Parses the content of a log.

    :param content: List of event log lines
    :type content: list[str]
    :return: list[LogEntry]
    """
    ret = []
    current_log_entry = None
    for i, line in enumerate(content):

        if "Event[" in line:
            # new event
            last_log_entry = current_log_entry
            current_log_entry = LogEntry()

            if last_log_entry is not None:
                ret.append(last_log_entry)
                last_log_entry.description.pop()
        else:
            if ': ' in line:
                data = line.split(': ')[1]
                data = data[0:-1]

            if "N/A" in line:
                pass
            elif "Log Name:" in line:
                current_log_entry.log_name = data
            elif "Source:" in line:
                current_log_entry.source = data
            elif "Date:" in line:
                data = data.split('.')[0]
                date = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S")
                current_log_entry.date = date
            elif "Event ID:" in line:
                current_log_entry.event_id = int(data)
            elif "Task:" in line:
                current_log_entry.task = data
            elif "Level:" in line:
                current_log_entry.level = data
            elif "Opcode:" in line:
                current_log_entry.opcode = data
            elif "Keyword:" in line:
                current_log_entry.keyword = data
            elif "User:" in line:
                current_log_entry.user = data
            elif "User Name:" in line:
                current_log_entry.user_name = data
            elif "Computer" in line:
                current_log_entry.computer = data
            elif "Description:" in line:
                pass
            else:
                current_log_entry.description.append(line.split('\n')[0])

    ret.append(current_log_entry)
    return ret


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_4"))

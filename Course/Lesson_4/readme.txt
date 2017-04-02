Lesson 4 - String - Windows Event log parser

In this lesson I want you to get familiar with python string type:
https://docs.python.org/3.5/library/string.html
https://docs.python.org/3.5/library/stdtypes.html#textseq

Python string is immutable which means once string is created cannot be changed.
However it offers huge amount of methods that allow to do many things with strings: split, join, slice, search, strip ...

Short summary:
string_variable = ""                                 # Creates empty string
string_variable = str()                              # Creates empty string
string_variable += "Hello world"                     # Concatenates string_variable with "Hello world"  and assigns it to string_variable
list_of_strings = string_variable.split()            # Splits string into list of strings using separator.
new_string = string_variable.join(["Hello", "world"] # Joins list of strings into one string
string_variable.endswith("world")                    # Checks if string ends with word "world"
string_variable.startswith("hello")                  # Checks if string starts with word "hello"
new_string = string_variable.strip()                 # Strips string from white characters
new_string = string_variable.lower()                 # Changes string letters to lower case
new_string = string_variable.upper()                 # Changes string letters to upper case
...

I want you to build Windows Event Log parser. Example file you can find in this lesson folder system_event_log.txt.
You can generate your own Event Log file using Windows command:
WEVTUtil query-events System /count:2000 /rd:true /format:text > system_event_log.txt

You can read this file in python using:
with open("system_event_log.txt") as fp:
    contents = fp.readlines()

In your folder create file with name: eventlog.py
In this file create function: parser(contents)
"contents" is a list of all lines that are in log file (system_event_log.txt).
This function should return list of elements of following type:

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

List should be ordered same as entries in log file.
"date" attribute should be of datetime type:
https://docs.python.org/3.5/library/datetime.html

To parse time use datetime.strptime function
https://docs.python.org/3.5/library/datetime.html#datetime.datetime.strptime

Don't parse fractions of a second. Just date and time with accuracy to a second.

"event_id" attribute should be type int.

"description" attribute should be a list of strings. One item per line without line ending "\n".

All "N/A" values in text log file should be seen as None in LogEntry.

I prepared few tests you have to pass in test_eventlogparser.py.
To run them add at the beginning of your file:
import unittest

And at the end:
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_4"))

You can run your eventlog.py from pyCharm directly or via command line: python eventlog.py.
In console output you will see tests results.

File Course/Lesson_4/eventlog_template.py is a solution template that you can use as starting point. Copy it to your solution folder and rename it to eventlog.py.
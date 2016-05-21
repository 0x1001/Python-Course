Lesson 5 - NFCC PLL settings parser

In this lesson we continue with text parsing.
This time I want you to extract PLL settings for different frequencies from given log file.
(You can ignore abbreviations like NFCC or PLL, they are irrelevant)
Log file example looks like this:

Selected Idx: 0, Freq: 12.000 Mhz
PLL Settings: 0x40 0x81 0xe0 0x02 0x40 0x00 0xe1 0x02

Extract from these lines:
    1. index - 0
    2. Frequency - 12.000
    3. PLL Settings - [0x40, 0x81, 0xe0, 0x02, 0x40, 0x00, 0xe1, 0x02]

Then print it in a nicer to read format:
"Index = 0, 12.000MHz, 0x40 0x81 0xe0 0x02 0x40 0x00 0xe1 0x02"

In your folder create file pllsettings.py.
Create two functions:
1. parser(log_contents)
    This is a parser function that parses log contents and for each PLL setting creates new PLLSetting object.
    "log_contents" is a list of all lines from log file. Example of a log file is here:
    Course\Lesson_5\example_input.txt

    You can read this file by doing:
    with open("../../../Course/Lesson_5/example_input.txt") as fp:
        log_contents = fp.readlines()

    This function should return list of object of following type:
    class PLLSetting:
        def __init__(self):
            self.index = None
            self.frequency = None
            self.settings = None

    "index" is of type int
    "frequency" is of type float (ex: 1.0 is 1MHz)
    "settings" is a list of int

    Use python regular expression for parsing this log file:
    https://docs.python.org/3.5/library/re.html

    You can use for example this regex to get "index" and "frequency":
    "Selected\sIdx:\s+(?P<index>\d+),\sFreq:\s+(?P<frequency>\d+\.\d+)\s+Mhz"

    Simplest way to use "re" module in python is by using re.match() function. Which returns "match" object or None.
    https://docs.python.org/3.5/library/re.html#re.match
    From match object you can get "index" by calling method group("index") and for "frequency" call group("frequency")

2. writer(pll_settings)
    This functions converts list of PLLSettings objects to string format.
    Example for string formatting for first item:
    "Index = 0, 12.000MHz, 0x40 0x81 0xe0 0x02 0x40 0x00 0xe1 0x02"

    This function should accept list of PLLSettings objects and return list of strings as shown in example.

    You can use str.format() function to compose required string.
    https://docs.python.org/3.5/library/stdtypes.html#str.format

    str.format() offers a lot of options for formatting strings:
    https://docs.python.org/3.5/library/string.html#formatstrings

I wrote several tests. You can run them from your file.
Add at the beginning of your file:
import unittest

And at the end:
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_5"))

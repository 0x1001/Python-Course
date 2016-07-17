import unittest
import re


class PLLSetting:
    def __init__(self):
        self.index = None
        self.frequency = None
        self.settings = None


def main():
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("../../../Course/Lesson_5"))


def parser(log_contents):
    current_settings = None
    complete_settings = []

    for line in log_contents:
        idx_frq = re.match("Selected\sIdx:\s+(?P<index>\d+),\sFreq:\s+(?P<frequency>\d+\.\d+)\s+Mhz", line)

        if idx_frq is not None:
            current_settings = PLLSetting()
            idx = idx_frq.group("index")
            frq = idx_frq.group("frequency")

            current_settings.index = int(idx)
            current_settings.frequency = float(frq)
            continue

        pll_set = re.match("PLL\sSettings:", line)

        if pll_set is not None:
            settings = re.findall("\dx[\d|a-f|A-F][\d|a-f|A-F]", line)
            current_settings.settings = [int(i, 16) for i in settings]
            complete_settings.append(current_settings)
    return complete_settings


def writer(pll_settings):
    formatted_output = []

    for item in pll_settings:
        line = "Index = {0}, {1:.3f}MHz, ".format(item.index, item.frequency)
        settings = ' '.join(['0x{:02x}'.format(number) for number in item.settings])
        line += settings

        formatted_output.append(line)

    return formatted_output


if __name__ == '__main__':
    main()

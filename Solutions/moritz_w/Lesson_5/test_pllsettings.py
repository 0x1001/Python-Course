import unittest
import pllsettings
import os


class TestParser(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "example_input.txt")) as fp:
            contents = fp.readlines()

        self._settings = pllsettings.parser(contents)

    def test_parser(self):
        self.assertIsInstance(self._settings, list)
        self.assertEquals(len(self._settings), 81)

    def test_parser_item_0(self):
        self.assertEqual(self._settings[0].index, 0)
        self.assertAlmostEqual(self._settings[0].frequency, 12.0, 3)
        self.assertEquals(self._settings[0].settings, [0x40, 0x81, 0xe0, 0x02, 0x40, 0x00, 0xe1, 0x02])

    def test_parser_item_21(self):
        self.assertEqual(self._settings[21].index, 21)
        self.assertAlmostEqual(self._settings[21].frequency, 13.050, 3)
        self.assertEquals(self._settings[21].settings, [0x40, 0x31, 0xe3, 0x02, 0xa0, 0xf1, 0xe0, 0x02])

    def test_parser_item_80(self):
        self.assertEqual(self._settings[80].index, 80)
        self.assertAlmostEqual(self._settings[80].frequency, 16.000, 3)
        self.assertEquals(self._settings[80].settings, [0x40, 0x81, 0xe0, 0x02, 0x40, 0xc0, 0xe0, 0x02])


class TestWriter(unittest.TestCase):
    def setUp(self):
        class PLLSetting:
            def __init__(self, index, frequency, settings):
                self.index = index
                self.frequency = frequency
                self.settings = settings

        s1 = PLLSetting(0, 12.0, [0x40, 0x81, 0xe0, 0x02, 0x40, 0x00, 0xe1, 0x02])
        s2 = PLLSetting(21, 13.050, [0x40, 0x31, 0xe3, 0x02, 0xa0, 0xf1, 0xe0, 0x02])
        s3 = PLLSetting(80, 16.000, [0x40, 0x81, 0xe0, 0x02, 0x40, 0xc0, 0xe0, 0x02])

        self._formatted_output = pllsettings.writer([s1, s2, s3])

    def test_writer(self):
        self.assertIsInstance(self._formatted_output, list)
        self.assertEqual(len(self._formatted_output), 3)
        [self.assertIsInstance(i, str) for i in self._formatted_output]

    def test_writer_output_strings(self):
        self.assertEqual(self._formatted_output[0], "Index = 0, 12.000MHz, 0x40 0x81 0xe0 0x02 0x40 0x00 0xe1 0x02")
        self.assertEqual(self._formatted_output[1], "Index = 21, 13.050MHz, 0x40 0x31 0xe3 0x02 0xa0 0xf1 0xe0 0x02")
        self.assertEqual(self._formatted_output[2], "Index = 80, 16.000MHz, 0x40 0x81 0xe0 0x02 0x40 0xc0 0xe0 0x02")

import unittest
import eventlog
import os


class TestEventLogParser(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "system_event_log.txt")) as fp:
            self._contents = fp.readlines()

        self._logs = eventlog.parser(self._contents)

    def test_parser_count_entries(self):
        self.assertEqual(len(self._logs), 2000)

    def test_parser_error_count(self):
        errors = [l for l in self._logs if l.level.strip().lower() == "error"]
        self.assertEqual(len(errors), 15)

    def test_parser_log_entry_0(self):
        self.assertEqual(self._logs[0].log_name, "System")
        self.assertEqual(self._logs[0].source, "Service Control Manager")
        self.assertEqual(self._logs[0].date.strftime("%Y-%m-%dT%H:%M:%S"), "2016-05-15T17:00:51")
        self.assertEqual(self._logs[0].event_id, 7036)
        self.assertEqual(self._logs[0].task, None)
        self.assertEqual(self._logs[0].level, "Information")
        self.assertEqual(self._logs[0].opcode, None)
        self.assertEqual(self._logs[0].keyword, "Classic")
        self.assertEqual(self._logs[0].user, None)
        self.assertEqual(self._logs[0].user_name, None)
        self.assertEqual(self._logs[0].computer, "Kot")
        self.assertEquals(self._logs[0].description, ["The Multimedia Class Scheduler service entered the stopped state."])

    def test_parser_log_entry_1999(self):
        self.assertEqual(self._logs[1999].log_name, "System")
        self.assertEqual(self._logs[1999].source, "Service Control Manager")
        self.assertEqual(self._logs[1999].date.strftime("%Y-%m-%dT%H:%M:%S"), "2016-05-10T22:15:53")
        self.assertEqual(self._logs[1999].event_id, 7036)
        self.assertEqual(self._logs[1999].task, None)
        self.assertEqual(self._logs[1999].level, "Information")
        self.assertEqual(self._logs[1999].opcode, None)
        self.assertEqual(self._logs[1999].keyword, "Classic")
        self.assertEqual(self._logs[1999].user, None)
        self.assertEqual(self._logs[1999].user_name, None)
        self.assertEqual(self._logs[1999].computer, "Kot")
        self.assertEquals(self._logs[1999].description, ["The Certificate Propagation service entered the stopped state."])

    def test_parser_log_entry_328(self):
        self.assertEqual(self._logs[328].log_name, "System")
        self.assertEqual(self._logs[328].source, "Microsoft-Windows-Kernel-Processor-Power")
        self.assertEqual(self._logs[328].date.strftime("%Y-%m-%dT%H:%M:%S"), "2016-05-15T11:33:06")
        self.assertEqual(self._logs[328].event_id, 26)
        self.assertEqual(self._logs[328].task, None)
        self.assertEqual(self._logs[328].level, "Information")
        self.assertEqual(self._logs[328].opcode, "Info")
        self.assertEqual(self._logs[328].keyword, None)
        self.assertEqual(self._logs[328].user, "S-1-5-18")
        self.assertEqual(self._logs[328].user_name, "NT AUTHORITY\SYSTEM")
        self.assertEqual(self._logs[328].computer, "Kot")
        self.assertEquals(self._logs[328].description, ["Processor 4 in group 0 exposes the following:",
                                                        "",
                                                        "2 idle state(s)",
                                                        "5 performance state(s)",
                                                        "0 throttle state(s)"])

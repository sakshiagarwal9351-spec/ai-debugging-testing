
import unittest
from buggy_calculator import calculate_average, check_result


class TestStudentCalculator(unittest.TestCase):

    def test_average(self):
        self.assertEqual(calculate_average([75, 80, 65, 90]), 77.5)

    def test_single_mark(self):
        self.assertEqual(calculate_average([80]), 80)

    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

    def test_pass_result(self):
        self.assertEqual(check_result(75), "Pass")

    def test_fail_result(self):
        self.assertEqual(check_result(30), "Fail")


if __name__ == "__main__":
    unittest.main()

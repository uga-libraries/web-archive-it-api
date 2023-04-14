"""
Tests for the verify_dates function from the warc_metadata_report.py script.
It verifies the two required arguments are correct and returns them plus errors.
"""
import unittest
from warc_metadata_report import verify_dates


class MyTestCase(unittest.TestCase):

    def test_correct(self):
        """
        Tests that the function returns the expected values if the first argument is earlier than the second.
        This is the only correct way to indicate a date range.
        """
        actual = verify_dates(["C:/path/warc_metadata_report.py", "2017-11-01", "2018-01-01"])
        expected = ("2017-11-01", "2018-01-01", [])
        self.assertEqual(actual, expected, "Problem with test: correct.")

    def test_error_first_date_equal(self):
        """
        Tests that the function returns the expected values if the first argument is the same as the second.
        """
        actual = verify_dates(["C:/path/warc_metadata_report.py", "2017-11-01", "2017-11-01"])
        expected = ("2017-11-01", "2017-11-01", ["The first argument must be an earlier date than the second."])
        self.assertEqual(actual, expected, "Problem with test: first argument date is the same as the second.")

    def test_error_first_date_later(self):
        """
        Tests that the function returns the expected values if the first argument is a later date than the second.
        """
        actual = verify_dates(["C:/path/warc_metadata_report.py", "2017-11-01", "2016-04-01"])
        expected = ("2017-11-01", "2016-04-01", ["The first argument must be an earlier date than the second."])
        self.assertEqual(actual, expected, "Problem with test for error: first date is later.")

    def test_error_format_first(self):
        """
        Tests that the function returns the expected values if the first argument is not formatted correctly.
        """
        actual = verify_dates(["C:/path/warc_metadata_report.py", "2017/11/01", "2018-01-01"])
        expected = (None, "2018-01-01", ["First argument '2017/11/01' is not formatted YYYY-MM-DD."])
        self.assertEqual(actual, expected, "Problem with test for error: start date format.")

    def test_error_format_second(self):
        """
        Tests that the function returns the expected values if the second argument is not formatted correctly.
        """
        actual = verify_dates(["C:/path/warc_metadata_report.py", "2017-11-01", "2018-1-1"])
        expected = ("2017-11-01", None, ["Second argument '2018-1-1' is not formatted YYYY-MM-DD."])
        self.assertEqual(actual, expected, "Problem with test for error: end date format.")

    def test_error_missing_both(self):
        """
        Tests that the function returns the expected values if both required arguments are missing.
        """
        actual = verify_dates(["C:/path/warc_metadata_report.py"])
        expected = (None, None, ["First argument (start date) is missing.", "Second argument (end date) is missing."])
        self.assertEqual(actual, expected, "Problem with test for error: missing both arguments.")

    def test_error_missing_second(self):
        """
        Tests that the function returns the expected values if the second required argument is missing.
        """
        actual = verify_dates(["C:/path/warc_metadata_report.py", "2017-11-01"])
        expected = ("2017-11-01", None, ["Second argument (end date) is missing."])
        self.assertEqual(actual, expected, "Problem with test for error: missing second arguments")


if __name__ == '__main__':
    unittest.main()

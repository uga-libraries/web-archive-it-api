"""
Tests for the size_to_gb function from the warc_metadata_report.py script.
It returns the size in GB, converted from the bytes that are in API data.
"""
import unittest
from warc_metadata_report import size_to_gb


class MyTestCase(unittest.TestCase):

    def test_one_gb(self):
        """
        Tests that the function returns the correct value if the size is 1 GB.
        It will not require rounding.
        """
        actual = size_to_gb("1000000000")
        expected = 1
        self.assertEqual(actual, expected, "Problem with test for one gb.")

    def test_round(self):
        """
        Tests that the function returns the correct value if the size is big enough to round.
        """
        actual = size_to_gb("1234567890")
        expected = 1.23
        self.assertEqual(actual, expected, "Problem with test for rounding.")

    def test_round_limit(self):
        """
        Tests that the function returns the correct value if the size is the limit for rounding.
        """
        actual = size_to_gb("10000000")
        expected = 0.01
        self.assertEqual(actual, expected, "Problem with test for rounding limit.")

    def test_do_not_round(self):
        """
        Tests that the function returns the correct value if the size is too small to round.
        """
        actual = size_to_gb("1234567")
        expected = .001234567
        self.assertEqual(actual, expected, "Problem with test for too small to round.")


if __name__ == '__main__':
    unittest.main()

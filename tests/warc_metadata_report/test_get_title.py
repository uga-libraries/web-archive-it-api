"""
Tests for the get_title() function from the warc_metadata_report.py script.
It returns the title for a seed or default text if it has no title.
"""
import unittest
from warc_metadata_report import get_title


class MyTestCase(unittest.TestCase):

    def test_api_error(self):
        """
        Tests that the function returns the expected API error text for a seed id that is not formated correctly.
        """
        actual = get_title("abc")
        expected = "API Error for seed report"
        self.assertEqual(actual, expected, "Problem with test for api error")

    def test_seed_with_title(self):
        """
        Tests that the function returns the expected title for a UGA Libraries seed with a title.
        """
        actual = get_title("2089428")
        expected = "Southern Alliance for Clean Energy"
        self.assertEqual(actual, expected, "Problem with test for seed with title")

    def test_seed_without_title(self):
        """
        Tests that the function returns the expected text for a UGA Libraries seed without a title.
        """
        actual = get_title("2209286")
        expected = "No title in Archive-It"
        self.assertEqual(actual, expected, "Problem with test for seed without a title")


if __name__ == '__main__':
    unittest.main()

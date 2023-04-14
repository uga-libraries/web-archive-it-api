"""
Tests for the get_seed_metadata() function from the warc_metadata_report.py script.
It returns the title and collector (department) for a seed or default text if that information is missing.
"""
import unittest
from warc_metadata_report import get_seed_metadata


class MyTestCase(unittest.TestCase):

    def test_api_error(self):
        """
        Tests that the function returns the expected API error text for a seed id that is not formatted correctly.
        """
        actual = get_seed_metadata("error")
        expected = ("Cannot get collector. API error 500 for seed report.",
                    "Cannot get title. API error 500 for seed report.")
        self.assertEqual(actual, expected, "Problem with test for API error")

    def test_seed_with_both(self):
        """
        Tests that the function returns the expected values for a seed with both collector and title.
        """
        actual = get_seed_metadata("2089428")
        expected = ("Richard B. Russell Library for Political Research and Studies",
                    "Southern Alliance for Clean Energy")
        self.assertEqual(actual, expected, "Problem with test for seed with both collector and title.")

    def test_seed_with_collector(self):
        """
        Tests that the function returns the expected values for a seed with a collector but no title.
        """
        actual = get_seed_metadata("2209286")
        expected = ("The Digital Library of Georgia", "No title in Archive-It")
        self.assertEqual(actual, expected, "Problem with test for seed with a collector but no title.")

    def test_seed_with_neither(self):
        """
        Tests that the function returns the expected values for a seed with no collector and no title.
        """
        actual = get_seed_metadata("2200062")
        expected = ("No collector in Archive-It", "No title in Archive-It")
        self.assertEqual(actual, expected, "Problem with test for seed with no collector and no title.")

    def test_seed_with_title(self):
        """
        Tests that the function returns the expected values for a seed with a title but no collector.
        """
        actual = get_seed_metadata("2016223")
        expected = ("No collector in Archive-It", "Testing")
        self.assertEqual(actual, expected, "Problem with test for seed with a title but no collector.")


if __name__ == '__main__':
    unittest.main()

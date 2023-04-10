"""
Tests for the get_header() function from the seed_metadata_report.py script.
It returns the correct list for the CSV header depending on the include_optional variable.
"""
import unittest
from seed_metadata_report import get_header


class MyTestCase(unittest.TestCase):

    def test_true(self):
        """
        Tests that the function returns the expected header list when the parameter is True.
        """
        actual = get_header(True)
        expected = ["ID", "Name", "Collector [required]", "Creator [required]", "Date [required]", "Description",
                    "Identifier [required]", "Language [required]", "Relation", "Rights [required]", "Subject",
                    "Title [required]", "Archive-It Metadata Page"]
        self.assertEqual(actual, expected, "Problem with test: true")

    def test_false(self):
        """
        Tests the function returns the expected header list when the parameter is False.
        """
        actual = get_header(False)
        expected = ["ID", "Name", "Collector", "Creator", "Date", "Identifier", "Language", "Rights", "Title",
                    "Archive-It Metadata Page"]
        self.assertEqual(actual, expected, "Problem with test: false")


if __name__ == '__main__':
    unittest.main()

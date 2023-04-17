"""
Tests for the calculate_seed_id function from the warc_metadata_report.py script.
It returns the seed id, which is extracted using a regular expression from the warc file name.
"""
import unittest
from warc_metadata_report import calculate_seed_id


class MyTestCase(unittest.TestCase):

    def test_correct(self):
        """
        Tests that the function returns the expected ID when the WARC file name is formatted correctly.
        """
        actual = calculate_seed_id("ARCHIVEIT-12912-MONTHLY-JOB1382111-SEED2184360-20210318220950737-0004-h3.warc.gz")
        expected = "2184360"
        self.assertEqual(actual, expected, "Problem with test: correct.")

    def test_error(self):
        """
        Tests that the function returns the expected text when the WARC file name is not formatted correctly.
        """
        actual = calculate_seed_id("ARCHIVEIT-12912-NEW-FORMAT-ID2184360-20210318220950737-0004-h3.warc.gz")
        expected = "COULD NOT CALCULATE SEED ID"
        self.assertEqual(actual, expected, "Problem with test: error.")


if __name__ == '__main__':
    unittest.main()

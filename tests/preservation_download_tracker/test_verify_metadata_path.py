"""
Tests for the verify_metadata_path() function from the preservation_download_tracker.py script.
It returns the required path argument if it is present and correct, or else raises an error.
"""
import os
import unittest
from preservation_download_tracker import verify_metadata_path


class MyTestCase(unittest.TestCase):

    def test_correct(self):
        """
        Tests that the function returns the expected value when the path argument is present and correct.
        """
        warc_report_path = os.path.join(os.getcwd(), "warc_metadata_aggregate_ids_duplicate.csv")
        actual = verify_metadata_path(["C:/path/preservation_download_tracker.py", warc_report_path])
        expected = warc_report_path
        self.assertEqual(actual, expected, "Problem with test for correct operation of the function")

    def test_error_argument_missing(self):
        """
        Tests that the function raises the expected error when there is no path argument.
        """
        with self.assertRaises(IndexError):
            verify_metadata_path(["C:/path/preservation_download_tracker.py"])

    def test_error_path_wrong(self):
        """
        Tests that the function raises the expected error when the path argument is not correct.
        """
        with self.assertRaises(ValueError):
            verify_metadata_path(["C:/path/preservation_download_tracker.py", "C:/error/warc_metadata.csv"])


if __name__ == '__main__':
    unittest.main()

"""
Tests for the save_csv() function from the preservation_download_tracker.py script.
It adds empty columns to a dataframe and saves it to a CSV.
"""

import unittest
from preservation_download_tracker import save_csv


class MyTestCase(unittest.TestCase):

    # TODO: Make the input dataframe in the test function = need to verify column types.
    # TODO: are there variations to test?

    def test_something(self):
        """
        Tests that the function works correctly when
        Results for testing are the contents of the CSV produced by the function.
        """
        actual = save_csv()
        expected = ""
        self.assertEqual(actual, expected, "Problem with test for ")


if __name__ == '__main__':
    unittest.main()
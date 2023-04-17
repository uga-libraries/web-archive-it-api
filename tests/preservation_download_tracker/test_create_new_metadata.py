"""
Tests for the create_new_metadata() function from the preservation_download_tracker.py script.
It makes a series that combines WARC metadata into a summary for each series.

For faster testing, the test input is warc metadata reports already saved to the tests folder.
These need to be updated if the warc metadata report is ever reformatted.
Data is read from the CSV rather than created in the tests with pandas to ensure types stay correct.
"""
import pandas as pd
import unittest
from preservation_download_tracker import create_new_metadata


class MyTestCase(unittest.TestCase):

    # TODO: make test CSVs
    # TODO: what variations are there to test?

    def test_something(self):
        """
        Tests that the function returns the expected dataframe (converted to a list for easier comparison)
        when CONDITION.
        """
        warc_df = pd.read_csv("warc_metadata_create_new_CONDITION.csv")
        actual_df = create_new_metadata(warc_df)
        actual = actual_df.columns.tolist() + actual_df.values.tolist()
        expected = []
        self.assertEqual(actual, expected, "Problem with test for ")


if __name__ == '__main__':
    unittest.main()

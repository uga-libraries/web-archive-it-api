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

    def test_multiple_warcs(self):
        """
        Tests that the function returns the expected dataframe (converted to a list for easier comparison)
        when the seeds each have multiple WARCs.
        """
        warc_df = pd.read_csv("warc_metadata_create_new_multiple_warcs.csv")
        actual_df = create_new_metadata(warc_df)
        actual = [actual_df.columns.tolist()] + [actual_df.index.tolist()] + actual_df.values.tolist()
        expected = [["Crawl_Job_ID", "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB"],
                    [2184360, 2547117, 2547541],
                    ["1453015;1436127", "31104307871", 3, 2.51],
                    ["1436594;1430000", "31104463292;31104000000", 2, 1.02],
                    ["1436727", "31104463403", 2, 1.04]]
        self.assertEqual(actual, expected, "Problem with test for seed with multiple WARCs")

    def test_one_warc(self):
        """
        Tests that the function returns the expected dataframe (converted to a list for easier comparison)
        when the seeds each have one WARC.
        """
        warc_df = pd.read_csv("warc_metadata_create_new_one_warc.csv")
        actual_df = create_new_metadata(warc_df)
        actual = [actual_df.columns.tolist()] + [actual_df.index.tolist()] + actual_df.values.tolist()
        expected = [["Crawl_Job_ID", "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB"],
                    [2184360, 2547117, 2547541],
                    ["1453015", "31104307871", 1, 1],
                    ["1436594", "31104463292", 1, .02],
                    ["1436727", "31104463403", 1, .04]]
        self.assertEqual(actual, expected, "Problem with test for seeds with one WARC")


if __name__ == '__main__':
    unittest.main()

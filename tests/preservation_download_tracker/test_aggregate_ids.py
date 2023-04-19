"""
Tests for the aggregate_ids() function from the preservation_download_tracker.py script.
It makes a series that combines all the ids of the specified type for each seed.

For faster testing, the test input is warc metadata reports already saved to the tests folder.
These need to be updated if the warc metadata report is ever reformatted.
Data is read from the CSV rather than created in the tests with pandas to ensure types stay correct.
"""
import pandas as pd
import unittest
from preservation_download_tracker import aggregate_ids


class MyTestCase(unittest.TestCase):

    def test_crawl_definition_duplicate(self):
        """
        Tests that the function returns the expected series (converted to a list for easier comparison)
        when there are multiple of the same crawl definition per seed.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_duplicate.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Definition_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '31104519079', '31104539234']
        self.assertEqual(actual, expected, "Problem with test for crawl definition, duplicate")

    def test_crawl_definition_duplicate_and_multiple(self):
        """
        Tests that the function returns the expected series (converted to a list for easier comparison)
        when there is more than one crawl definition per seed, some of which occur more than once.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_duplicate_and_multiple.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Definition_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '31104519079;11111111111', '31104539234;22222222222']
        self.assertEqual(actual, expected, "Problem with test for crawl definition, duplicate and multiple")

    def test_crawl_definition_multiple(self):
        """
        Tests that the function returns the expected series (converted to a list for easier comparison)
        when there is more than one crawl definition per seed.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_multiple.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Definition_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '31104519079;11111111111', '31104539234;22222222222']
        self.assertEqual(actual, expected, "Problem with test for crawl definition, multiple")

    def test_crawl_definition_unique(self):
        """
        Tests that the function returns the expected series  (converted to a list for easier comparison)
        when there is one crawl definition per seed.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_unique.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Definition_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '31104519079', '31104539234']
        self.assertEqual(actual, expected, "Problem with test for crawl definition, unique")

    def test_crawl_job_duplicate(self):
        """
        Tests that the function returns the expected series (converted to a list for easier comparison)
        when there are multiple of the same crawl job per seed.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_duplicate.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Job_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '1542317', '1580159']
        self.assertEqual(actual, expected, "Problem with test for crawl job, duplicate")

    def test_crawl_job_duplicate_and_multiple(self):
        """
        Tests that the function returns the expected series (converted to a list for easier comparison)
        when there is more than one crawl job per seed, some of which occur more than once.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_duplicate_and_multiple.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Job_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '1542317;1111111', '1580159;2222222']
        self.assertEqual(actual, expected, "Problem with test for crawl job, duplicate and multiple")

    def test_crawl_job_multiple(self):
        """
        Tests that the function returns the expected series (converted to a list for easier comparison)
        when there is more than one crawl job per seed.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_multiple.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Job_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '1542317;1111111', '1580159;2222222']
        self.assertEqual(actual, expected, "Problem with test for crawl job, multiple")

    def test_crawl_job_unique(self):
        """
        Tests that the function returns the expected series (converted to a list for easier comparison)
        when there is one crawl job per seed.
        """
        warc_df = pd.read_csv("warc_metadata_aggregate_ids_unique.csv")
        actual_df = aggregate_ids(warc_df, "Crawl_Job_ID")
        actual = actual_df.index.tolist() + actual_df.to_list()
        expected = [2454506, 2508399, '1542317', '1580159']
        self.assertEqual(actual, expected, "Problem with test for crawl job, unique")


if __name__ == '__main__':
    unittest.main()

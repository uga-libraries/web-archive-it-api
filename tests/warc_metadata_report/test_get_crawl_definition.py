"""
Tests for the get_crawl_definition function from the warc_metadata_report.py script.
It returns the crawl definition id for a crawl jub or default text if it can't find one.
"""
import unittest
from warc_metadata_report import get_crawl_definition


class MyTestCase(unittest.TestCase):

    def test_api_error(self):
        """
        Tests that the function returns the expected API error text for a job id that is not formatted correctly.
        """
        actual = get_crawl_definition("error")
        expected = "API Error for job report"
        self.assertEqual(actual, expected, "Problem with test for API error")

    def test_job_id_correct(self):
        """
        Tests that the function returns the expected crawl definition for a UGA Libraries job id.
        """
        actual = get_crawl_definition("921607")
        expected = 31104243716
        self.assertEqual(actual, expected, "Problem with test for job id that is in Archive-It")

    def test_job_id_incorrect(self):
        """
        Tests that the function returns the expected text for a job id that is not in Archive-It.
        """
        actual = get_crawl_definition("0")
        expected = "Cannot get crawl definition: Job ID is not in Archive-It"
        self.assertEqual(actual, expected, "Problem with test for job id that is not in Archive-It")


if __name__ == '__main__':
    unittest.main()

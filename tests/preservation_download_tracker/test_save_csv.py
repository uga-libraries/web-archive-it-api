"""
Tests for the save_csv() function from the preservation_download_tracker.py script.
It adds empty columns to a dataframe and saves it to a CSV.
"""
import csv
import os
import pandas as pd
import unittest
import configuration as c
from preservation_download_tracker import save_csv


class MyTestCase(unittest.TestCase):

    def test_save_csv(self):
        """
        Tests that the function works correctly. It does not have any variations to test.
        Results for testing are the contents of the CSV produced by the function.
        """
        # Creates a dataframe to use as test input and runs the function being tested.
        df = pd.DataFrame([["Georgia Department of Natural Resources Coastal Research Division",
                            "Map and Government Information Library",
                            15678, 2520386, "1773352", "31104635513", 1, 0.33],
                           ["Georgia Department of Early Care and Learning (Bright from the Start)",
                            "Map and Government Information Library",
                            15678, 2523324, "1773295", "31104635486", 27, 41.21],
                           ["Georgia Department of Natural Resources Law Enforcement Division",
                            "Map and Government Information Library",
                            15678, 2520385, "1774325", "31104635968", 1, 0.07],
                           ["Georgia Department of Public Health", "Map and Government Information Library",
                            15678, 2472042, "1773695", "31104635677", 17, 3.98]],
                          columns=["AIP_Title", "Department", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                                   "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB"])
        save_csv(df, "warc_metadata_2023-03-01_2023-03-31.csv")

        # Reads the CSV produced by the function into a list,
        # with the contents of each row as its own list in that list,
        # and then deletes the CSV.
        report_path = os.path.join(c.script_output, "Preservation_Download_2023-04.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)
        os.remove(report_path)

        expected = [["AIP_ID", "AIP_Title", "Department", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                     "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB", "Log_coll_scope", "Log_seed_scope",
                     "Log_Other_Reports", "WARC_Download", "Completeness_Log", "AIP_Log", "QC1", "Upload", "Ingest",
                     "QC2", "Complete"],
                    ["", "Georgia Department of Natural Resources Coastal Research Division",
                     "Map and Government Information Library", "15678", "2520386", "1773352", "31104635513",
                     "1", "0.33", "", "", "", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Department of Early Care and Learning (Bright from the Start)",
                     "Map and Government Information Library", "15678", "2523324", "1773295", "31104635486",
                     "27", "41.21", "", "", "", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Department of Natural Resources Law Enforcement Division",
                     "Map and Government Information Library", "15678", "2520385", "1774325", "31104635968",
                     "1", "0.07", "", "", "", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Department of Public Health", "Map and Government Information Library",
                     "15678", "2472042", "1773695", "31104635677", "17", "3.98", "", "", "", "", "", "", "",
                     "", "", "", ""]]

        self.assertEqual(actual, expected, "Problem with test for save csv")


if __name__ == '__main__':
    unittest.main()

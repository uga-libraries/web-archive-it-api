"""
Tests for the save_csv_row() shared function.
It saves a row to the specified CSV and returns nothing.
"""
import csv
from datetime import datetime
import os
import unittest
from configuration import script_output
from shared_functions import save_csv_row


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Variable with the test report path, which is used multiple times.
        For more complete testing, it uses the path and CSV naming convention from the collection metadata report.
        """
        self.report_path = f"{script_output}/collection_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv"

    def tearDown(self):
        """
        Deletes the test metadata report.
        """
        os.remove(self.report_path)

    def test_existing_csv(self):
        """
        Tests that the function added a second row to an existing CSV with one row.
        Result for testing is a list of the contents of the test CSV made by the function.
        """
        save_csv_row(self.report_path, ["h1", "h2", "h3", "h4"])
        save_csv_row(self.report_path, ["data1", "data2", "data3", "data4"])
        with open(self.report_path, newline='') as open_file:
            read_file = csv.reader(open_file)
            actual = list(read_file)

        expected = [["h1", "h2", "h3", "h4"], ["data1", "data2", "data3", "data4"]]

        self.assertEqual(actual, expected, "Problem with test existing csv")

    def test_new_csv(self):
        """
        Tests that the function made the CSV and added the correct row.
        Result for testing is a list of the contents of the test CSV made by the function.
        """
        save_csv_row(self.report_path, ["data1", "data2", "data3", "data4"])
        with open(self.report_path, newline='') as open_file:
            read_file = csv.reader(open_file)
            actual = list(read_file)

        expected = [["data1", "data2", "data3", "data4"]]

        self.assertEqual(actual, expected, "Problem with test new csv")


if __name__ == '__main__':
    unittest.main()

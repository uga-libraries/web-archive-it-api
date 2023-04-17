"""
Tests the output of the preservation_download_tracker.py script.
It creates a new spreadsheet from the WARC metadata report to use for tracking preservation downloads.
"""
import csv
import os
import subprocess
import unittest
import configuration as c


class MyTestCase(unittest.TestCase):

    # TODO: save a WARC CSV in the test folder or generate it using the script to keep it synced?

    def tearDown(self):
        """
        Deletes the CSV produced by the script during the test.
        """
        os.remove(os.path.join(c.script_output, "Preservation_Download_YEAR_MONTH.csv"))

    def test_script(self):
        """
        Tests the full script.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        script_path = os.path.join("..", "..", "preservation_download_tracker.py")
        warc_path = "TODO"
        subprocess.run(f"python {script_path} {warc_path}", shell=True)

        report_path = os.path.join(c.script_output, "Preservation_Download_YEAR_MONTH.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = []

        self.assertEqual(actual, expected, "Problem with test for the full script.")


if __name__ == '__main__':
    unittest.main()

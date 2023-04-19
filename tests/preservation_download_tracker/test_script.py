"""
Tests the output of the preservation_download_tracker.py script.
It creates a new spreadsheet from the WARC metadata report to use for tracking preservation downloads.
There are tests for a few different date ranges to capture the primary data variation while keeping each one small.
"""
import csv
import os
import subprocess
import unittest
import configuration as c


class MyTestCase(unittest.TestCase):

    def tearDown(self):
        """
        Deletes the CSV produced by the script and the WARC Metadata CSV used as the script input.
        Because the CSV names include a date, it can't just delete by name.
        """
        for file in os.listdir(c.script_output):
            if file.startswith("Preservation_Download") or file.startswith("warc_metadata"):
                os.remove(os.path.join(c.script_output, file))

    def test_one(self):
        """
        Tests the full script with a date range for Russell seeds and one without metadata.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        # Makes the WARC metadata report needed as script input.
        warc_script_path = os.path.join("..", "..", "warc_metadata_report.py")
        subprocess.run(f"python {warc_script_path} 2019-11-10 2019-11-25", shell=True)

        # Runs the script being tested.
        script_path = os.path.join("..", "..", "preservation_download_tracker.py")
        warc_path = os.path.join(c.script_output, "warc_metadata_2019-11-10_2019-11-24.csv")
        subprocess.run(f"python {script_path} {warc_path}", shell=True)

        # Reads the CSV produced by the function into a list,
        # with the contents of each row as its own list in that list.
        report_path = os.path.join(c.script_output, "Preservation_Download_2019-11.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["AIP_ID", "AIP_Title", "Department", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                     "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB", "Batch", "Script_Log", "Completeness_Log",
                     "QC1", "Upload", "Ingest", "QC2", "Complete"],
                    ["", "Statewide Independent Living Council of Georgia",
                     "Richard B. Russell Library for Political Research and Studies", "12264", "2070895",
                     "1033772", "31104276639", "3", "3.64", "", "", "", "", "", "", "", ""],
                    ["", "K7MOA Legacy Voteview Website",
                     "Richard B. Russell Library for Political Research and Studies", "12262", "2018084",
                     "1033408", "31104276333", "1", "0.67", "", "", "", "", "", "", "", ""],
                    ["", "Rotary Club of Athens", "Richard B. Russell Library for Political Research and Studies",
                     "12939", "2089429", "1025299", "31104271006", "1", "0.01", "", "", "", "", "", "", "", ""],
                    ["", "Latest Trends - A Georgia Trend Blog",
                     "Richard B. Russell Library for Political Research and Studies", "12939", "2091989",
                     "1025266", "31104270979", "9", "7.49", "", "", "", "", "", "", "", ""],
                    ["", "ACLU of Georgia", "Richard B. Russell Library for Political Research and Studies",
                     "12944", "2090408", "1010676", "31104269622", "1", "0.52", "", "", "", "", "", "", "", ""],
                    ["", "No title in Archive-It", "No collector in Archive-It", "12944", "2090409", "1010676",
                     "31104269622", "1", "0.006", "", "", "", "", "", "", "", ""]]

        self.assertEqual(actual, expected, "Problem with test one.")

    def test_two(self):
        """
        Tests the full script with a date range for Hargrett, which are seeds with multiple Job IDs.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        # Makes the WARC metadata report needed as script input.
        warc_script_path = os.path.join("..", "..", "warc_metadata_report.py")
        subprocess.run(f"python {warc_script_path} 2020-04-16 2020-04-22", shell=True)

        # Runs the script being tested.
        script_path = os.path.join("..", "..", "preservation_download_tracker.py")
        warc_path = os.path.join(c.script_output, "warc_metadata_2020-04-16_2020-04-21.csv")
        subprocess.run(f"python {script_path} {warc_path}", shell=True)

        # Reads the CSV produced by the function into a list,
        # with the contents of each row as its own list in that list.
        report_path = os.path.join(c.script_output, "Preservation_Download_2020-04.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["AIP_ID", "AIP_Title", "Department", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                     "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB", "Batch", "Script_Log", "Completeness_Log",
                     "QC1", "Upload", "Ingest", "QC2", "Complete"],
                    ["", "UGA Today", "Hargrett Rare Book & Manuscript Library", "12912", "2184360",
                     "1130531;1130526", "31104307871;31104312482", "31", "32.878", "", "", "", "", "", "", "", ""],
                    ["", "Coronavirus (COVID-19) Information and Resources website",
                     "Hargrett Rare Book & Manuscript Library", "12912", "2173769", "1130525;1130530",
                     "31104312481;31104307305", "2", "0.004", "", "", "", "", "", "", "", ""]]
        self.assertEqual(actual, expected, "Problem with test two.")

    def test_three(self):
        """
        Tests the full script with a date range for MAGIL seeds.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        # Makes the WARC metadata report needed as script input.
        warc_script_path = os.path.join("..", "..", "warc_metadata_report.py")
        subprocess.run(f"python {warc_script_path} 2022-10-20 2022-10-27", shell=True)

        # Runs the script being tested.
        script_path = os.path.join("..", "..", "preservation_download_tracker.py")
        warc_path = os.path.join(c.script_output, "warc_metadata_2022-10-20_2022-10-26.csv")
        subprocess.run(f"python {script_path} {warc_path}", shell=True)

        # Reads the CSV produced by the function into a list,
        # with the contents of each row as its own list in that list.
        report_path = os.path.join(c.script_output, "Preservation_Download_2022-10.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["AIP_ID", "AIP_Title", "Department", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                     "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB", "Batch", "Script_Log", "Completeness_Log",
                     "QC1", "Upload", "Ingest", "QC2", "Complete"],
                    ["", "Georgia Technology Authority", "Map and Government Information Library", "15678",
                     "2527198", "1691033", "31104596358", "1", "0.02", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Board of Health Care Workforce", "Map and Government Information Library", "15678",
                     "2514060", "1691025", "31104596352", "1", "0.01", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Vocational Rehabilitation Agency", "Map and Government Information Library", "15678",
                     "2527200", "1691026", "31104596353", "1", "0.09", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Commission on Equal Opportunity", "Map and Government Information Library", "15678",
                     "2529631", "1676317", "31104588625", "1", "0.18", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Board of Pharmacy", "Map and Government Information Library", "15678",
                     "2529629", "1676316", "31104588624", "1", "0.66", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Aviation Authority", "Map and Government Information Library", "15678",
                     "2529627", "1676002", "31104588530", "1", "0.09", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Governor's Office of Disability Services Ombudsman",
                     "Map and Government Information Library", "15678", "2529660", "1675831", "31104588527",
                     "1", "0.1", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Department of Community Supervision", "Map and Government Information Library",
                     "15678", "2529642", "1672436", "31104586779", "1", "0.87", "", "", "", "", "", "", "", ""],
                    ["", "Georgia Office of Attorney General Consumer Protection Division",
                     "Map and Government Information Library", "15678", "2529634", "1672420", "31104586775",
                     "2", "1.15", "", "", "", "", "", "", "", ""]]

        self.assertEqual(actual, expected, "Problem with test three.")


if __name__ == '__main__':
    unittest.main()

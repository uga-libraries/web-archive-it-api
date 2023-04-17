"""
Tests the output of the warc_metadata_report.py script.
It gets metadata for all WARCs in a specified date range using the Archive-It APIs and saves them to a CSV.
There are tests for a few different date ranges to capture the primary data variation while keeping each group small.
"""
import csv
import os
import subprocess
import unittest
import configuration as c


class MyTestCase(unittest.TestCase):

    def tearDown(self):
        """
        Deletes the CSV produced by the script for each test.
        Because the CSV names include the date range, it can't just delete by name.
        """
        for file in os.listdir(c.script_output):
            if file.startswith("warc_metadata"):
                os.remove(os.path.join(c.script_output, file))

    def test_one(self):
        """
        Tests the full script with a date range with Hargrett and deleted seeds.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        script_path = os.path.join("..", "..", "warc_metadata_report.py")
        subprocess.run(f"python {script_path} 2019-06-25 2019-06-30", shell=True)

        report_path = os.path.join(c.script_output, "warc_metadata_2019-06-25_2019-06-29.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["AIP_Title", "Department", "WARC_Filename", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                     "Crawl_Definition_ID", "Date_Store-Time", "Date_Crawl-Start", "Date_Crawl-End", "Size_GB",
                     "File_Type", "MD5_Checksum", "SHA1_Checksum"],
                    ["UGA Black Theatrical Ensemble Twittter", "Hargrett Rare Book & Manuscript Library",
                     "ARCHIVEIT-12181-CRAWL_SELECTED_SEEDS-JOB938127-SEED2024246-20190626135802459-00001-h3.warc.gz",
                     "12181", "2024246", "938127", "31104247607", "2019-06-26T22:29:14.348851Z",
                     "2019-06-25T22:23:17.974000Z", "2019-06-26T13:58:02.459000Z", "0.94", "warc",
                     "b7014c1e98b52de9ad1183cc27943f4a", "a85f309efb6499e16c04bc854f9ed079dd551a7e"],
                    ["No title in Archive-It", "No collector in Archive-It",
                     "ARCHIVEIT-12181-CRAWL_SELECTED_SEEDS-JOB938127-SEED2024250-20190625222414653-00000-h3.warc.gz",
                     "12181", "2024250", "938127", "31104247607", "2019-06-26T22:28:24.088505Z",
                     "2019-06-25T22:23:17.974000Z", "2019-06-25T22:24:14.653000Z", "0.85", "warc",
                     "2ded28776667b26faca6ed08a7f9f811", "52a14816632967b9ba85c793ee4e0a6eca538dd3"],
                    ["Infusion Magazine website", "Hargrett Rare Book & Manuscript Library",
                     "ARCHIVEIT-12181-CRAWL_SELECTED_SEEDS-JOB938127-SEED2024247-20190625222324141-00000-h3.warc.gz",
                     "12181", "2024247", "938127", "31104247607", "2019-06-26T22:26:58.763087Z",
                     "2019-06-25T22:23:17.974000Z", "2019-06-25T22:23:24.141000Z", "0.91", "warc",
                     "6b9b5f6b03ea0598ade7c5529b607cb7", "e5ee12c1f0d14b51be9304b56104d905044a3c4e"],
                    ["No title in Archive-It", "No collector in Archive-It",
                     "ARCHIVEIT-12181-CRAWL_SELECTED_SEEDS-JOB938127-SEED2024249-20190625222349710-00000-h3.warc.gz",
                     "12181", "2024249", "938127", "31104247607", "2019-06-26T22:25:39.307769Z",
                     "2019-06-25T22:23:17.974000Z", "2019-06-25T22:23:49.710000Z", "0.24", "warc",
                     "7e2a212b37a014fd5b8f12519bcb9052", "6cc231fc26a621e008a9a887bfe2425b3e02f89e"],
                    ["No title in Archive-It", "No collector in Archive-It",
                     "ARCHIVEIT-12181-CRAWL_SELECTED_SEEDS-JOB938127-SEED2024248-20190626131257414-00001-h3.warc.gz",
                     "12181", "2024248", "938127", "31104247607", "2019-06-26T22:25:29.040363Z",
                     "2019-06-25T22:23:17.974000Z", "2019-06-26T13:12:57.414000Z", "0.17", "warc",
                     "fd36b6b442bc728ceadf3f9ea3ab8bc2", "48ce15f08fb10b61205e754c5cb832db79917e7e"],
                    ["UGA Black Theatrical Ensemble Twittter", "Hargrett Rare Book & Manuscript Library",
                     "ARCHIVEIT-12181-CRAWL_SELECTED_SEEDS-JOB938127-SEED2024246-20190625222324356-00000-h3.warc.gz",
                     "12181", "2024246", "938127", "31104247607", "2019-06-26T14:01:03.316947Z",
                     "2019-06-25T22:23:17.974000Z", "2019-06-25T22:23:24.356000Z", "1.0", "warc",
                     "f491f652c5b3960374e8b547280cb464", "97176e7e2f0aafb8c01fcc70d602e69958d47b3c"],
                    ["No title in Archive-It", "No collector in Archive-It",
                     "ARCHIVEIT-12181-CRAWL_SELECTED_SEEDS-JOB938127-SEED2024248-20190625222324244-00000-h3.warc.gz",
                     "12181", "2024248", "938127", "31104247607", "2019-06-26T13:15:59.522636Z",
                     "2019-06-25T22:23:17.974000Z", "2019-06-25T22:23:24.244000Z", "1.0", "warc",
                     "11acaa77ebd37307dacacd26a8d39a98", "97fe9a510aececa02c48bdf179a95c93f0017346"]]

        self.assertEqual(expected, actual, "Problem with test one.")

    def test_two(self):
        """
        Tests the full script with a date range with Russell seeds.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        script_path = os.path.join("..", "..", "warc_metadata_report.py")
        subprocess.run(f"python {script_path} 2021-08-25 2021-08-26", shell=True)

        report_path = os.path.join(c.script_output, "warc_metadata_2021-08-25_2021-08-25.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["AIP_Title", "Department", "WARC_Filename", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                     "Crawl_Definition_ID", "Date_Store-Time", "Date_Crawl-Start", "Date_Crawl-End", "Size_GB",
                     "File_Type", "MD5_Checksum", "SHA1_Checksum"],
                    ["Adela Yelton - Home | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547534-20210616194141062-00000-h3.warc.gz",
                     "12265", "2547534", "1436724", "31104463400", "2021-08-25T18:11:09.038300Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-16T19:41:41.062000Z", "1.0", "warc",
                     "9f17eb8f77e33959ccbb232bc245de5d", "44a69a9b0d566c26d599ac24443ce28abda3a81f"],
                    ["Adela Yelton - Posts | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547537-20210618020630340-00001-h3.warc.gz",
                     "12265", "2547537", "1436724", "31104463400", "2021-08-25T18:11:09.038210Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-18T02:06:30.340000Z", "1.82", "warc",
                     "f34a5b55075d4635ddefe29eee158880", "448158d736ee2c7b971d9759cadfa5d4573ddc9d"],
                    ["Adela Yelton - Posts | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547537-20210616195204928-00000-h3.warc.gz",
                     "12265", "2547537", "1436724", "31104463400", "2021-08-25T18:11:09.038121Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-16T19:52:04.928000Z", "1.28", "warc",
                     "af95953e3abeaca7f3b69f5892198fe5", "ea9a771102a8362f4d27393b0628f3ce8aef8612"],
                    ["Adela Yelton - Posts | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547537-20210618021640884-00002-h3.warc.gz",
                     "12265", "2547537", "1436724", "31104463400", "2021-08-25T18:11:09.038003Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-18T02:16:40.884000Z", "0.3", "warc",
                     "473e881049c1eef3c4d80552d75b52b7", "f57eae9283858aa94b664f8346d3d1e6b69a98a5"],
                    ["Adela Yelton - Home | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547534-20210617220544155-00001-h3.warc.gz",
                     "12265", "2547534", "1436724", "31104463400", "2021-08-25T18:11:09.037913Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-17T22:05:44.155000Z", "0.48", "warc",
                     "23704720cc6ec83634f3b57b55627108", "008203860dcfd61bfd5ce9437f32b20d3df90ce7"],
                    ["Adela Yelton - About | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547535-20210616194930331-00000-h3.warc.gz",
                     "12265", "2547535", "1436724", "31104463400", "2021-08-25T18:11:09.037822Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-16T19:49:30.331000Z", "0.88", "warc",
                     "0022e920995e17ba4e1bc2b9341f6e00", "fcbb98abc0c722775731aed2f5e9972fb24fc5b5"],
                    ["Adela Yelton - Photos | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547539-20210616195609781-00000-h3.warc.gz",
                     "12265", "2547539", "1436724", "31104463400", "2021-08-25T18:11:09.037731Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-16T19:56:09.781000Z", "0.75", "warc",
                     "eb4e8db85edef51a54846521ca166fc8", "4596b6df9581ee10153649c62447aad6934dc06e"],
                    ["Adela Yelton - Community | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547540-20210616200047900-00000-h3.warc.gz",
                     "12265", "2547540", "1436724", "31104463400", "2021-08-25T18:11:09.037637Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-16T20:00:47.900000Z", "0.39", "warc",
                     "724bb3dc801021da26276a15162d2e00", "a2b66c2f460541212379b3815bdeaa579f84db80"],
                    ["Adela Yelton - Events | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547538-20210616195445338-00000-h3.warc.gz",
                     "12265", "2547538", "1436724", "31104463400", "2021-08-25T18:11:09.037537Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-16T19:54:45.338000Z", "0.64", "warc",
                     "9129ebc55f0a45d05b401bd6d464b8fe", "f9d86c8d7775b002fc9e0e2bdef3465c6d005f40"],
                    ["Adela Yelton - Videos | Facebook",
                     "Richard B. Russell Library for Political Research and Studies",
                     "ARCHIVEIT-12265-TEST-JOB1436724-SEED2547536-20210616195147914-00000-h3.warc.gz",
                     "12265", "2547536", "1436724", "31104463400", "2021-08-25T18:11:09.037378Z",
                     "2021-06-16T19:41:32.694895Z", "2021-06-16T19:51:47.914000Z", "0.26", "warc",
                     "18830590a5f2138deadceac920c051c2", "d779491dbbafbbc46dd8b78bc4c7cde75ff27deb"]]

        self.assertEqual(expected, actual, "Problem with test two.")

    def test_three(self):
        """
        Tests the full script with a date range with MAGIL seeds.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        script_path = os.path.join("..", "..", "warc_metadata_report.py")
        subprocess.run(f"python {script_path} 2022-07-15 2022-10-26", shell=True)

        report_path = os.path.join(c.script_output, "warc_metadata_2022-07-15_2022-10-25.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["AIP_Title", "Department", "WARC_Filename", "AIT_Collection_ID", "Seed_ID", "Crawl_Job_ID",
                     "Crawl_Definition_ID", "Date_Store-Time", "Date_Crawl-Start", "Date_Crawl-End", "Size_GB",
                     "File_Type", "MD5_Checksum", "SHA1_Checksum"],
                    ["Georgia Office of Attorney General Consumer Protection Division",
                     "Map and Government Information Library",
                     "ARCHIVEIT-15678-TEST-JOB1672420-SEED2529634-20220911193609257-00000-h3.warc.gz",
                     "15678", "2529634", "1672420", "31104586775", "2022-10-25T14:53:54.308359Z",
                     "2022-09-11T19:36:04.635482Z", "2022-09-11T19:36:09.257000Z", "1.0", "warc",
                     "f4d75988249684d270c030cf366f9e13", "4c3af4c452d7fd3dbb60cbe1c0537761cfd66a53"],
                    ["Georgia Office of Attorney General Consumer Protection Division",
                     "Map and Government Information Library",
                     "ARCHIVEIT-15678-TEST-JOB1672420-SEED2529634-20220913205209833-00001-h3.warc.gz",
                     "15678", "2529634", "1672420", "31104586775", "2022-10-25T14:53:54.308126Z",
                     "2022-09-11T19:36:04.635482Z", "2022-09-13T20:52:09.833000Z", "0.15", "warc",
                     "a4f8b4ef99793a4fdbd022aff67ad203", "1743745b5d7867ae303b713febbb4b8a62c468d4"],
                    ["Technical College System of Georgia", "Map and Government Information Library",
                     "ARCHIVEIT-15678-TEST-JOB1637390-SEED2529686-20220705130427457-00000-h3.warc.gz",
                     "15678", "2529686", "1637390", "31104569758", "2022-07-18T13:17:34.869675Z",
                     "2022-07-05T13:04:21.103644Z", "2022-07-05T13:04:27.457000Z", "1.07", "warc",
                     "e25f91eea9003e8806ee77e60693986a", "c4bf061cb19729739534429f4c19daecfd8e8fd8"],
                    ["Technical College System of Georgia", "Map and Government Information Library",
                     "ARCHIVEIT-15678-TEST-JOB1637390-SEED2529686-20220706180305566-00001-h3.warc.gz",
                     "15678", "2529686", "1637390", "31104569758", "2022-07-18T13:17:34.869465Z",
                     "2022-07-05T13:04:21.103644Z", "2022-07-06T18:03:05.566000Z", "0.99", "warc",
                     "88ac47e473b2b129d6659863019d86a4", "61a960a0653953b8c535d6dbac84c2569c8d5c6c"]]

        self.assertEqual(expected, actual, "Problem with test three.")


if __name__ == "__main__":
    unittest.main()

"""
Tests the output of the seed_metadata_report.py script, with and without the optional argument.
It gets metadata for all seeds using the Archive-It Partner API and saves them to a CSV.
"""
from datetime import datetime
import os
import pandas as pd
import subprocess
import unittest
import configuration as c


class MyTestCase(unittest.TestCase):

    def tearDown(self):
        """
        Deletes the CSV produced by the script for each test.
        """
        os.remove(os.path.join(c.script_output, f"seed_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv"))

    def test_all(self):
        """
        Tests the full script without the optional argument, which creates a report with all fields.
        The result for testing is a small sample of rows, since there are many seeds and new seeds are added often.
        """
        script_path = os.path.join("..", "..", "seed_metadata_report.py")
        subprocess.run(f"python {script_path}", shell=True)

        sample = [2024246, 2084781, 2091989, 2472041, 2485678, 2529656, 2547534]
        report_path = os.path.join(c.script_output, f"seed_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv")
        # Encoding errors are ignored, causing curly apostrophe's to be removed when the data is read into pandas.
        df_full = pd.read_csv(report_path, encoding_errors="ignore")
        df_sample = df_full.loc[df_full['ID'].isin(sample)]
        actual = [df_sample.columns.to_list()] + df_sample.values.tolist()

        expected = [["ID", "Name", "Collector [required]", "Creator [required]", "Date [required]", "Description",
                     "Identifier [required]", "Language [required]", "Relation", "Rights [required]", "Subject",
                     "Title [required]", "Archive-It Metadata Page"],
                    [2024246, "https://twitter.com/UGABTE/", "Hargrett Rare Book & Manuscript Library",
                     "UGA Black Theatrical Ensemble", "Captured 2019-", "NO DATA OF THIS TYPE",
                     "https://wayback.archive-it.org/12181/*/https://twitter.com/UGABTE/", "English",
                     "NO DATA OF THIS TYPE", "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "NO DATA OF THIS TYPE", "UGA Black Theatrical Ensemble Twittter",
                     f"{c.inst_page}/collections/12181/seeds/2024246/metadata"],
                    [2084781, "https://www.facebook.com/FootballUGA/", "Hargrett Rare Book & Manuscript Library",
                     "University of Georgia", "Captured 2019-", "NO DATA OF THIS TYPE",
                     "https://wayback.archive-it.org/12907/*/https://www.facebook.com/FootballUGA/", "English",
                     "NO DATA OF THIS TYPE", "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "NO DATA OF THIS TYPE", "UGA Football Facebook",
                     f"{c.inst_page}/collections/12907/seeds/2084781/metadata"],
                    [2091989, "https://georgiatrendblog.com/",
                     "Richard B. Russell Library for Political Research and Studies", "Georgia Trend Magazine",
                     "Captured 2019-", "NO DATA OF THIS TYPE",
                     "https://wayback.archive-it.org/12939/*/https://georgiatrendblog.com/", "English",
                     "RBRL/270: Georgia Trend Magazine Records",
                     "In Copyright: http://rightsstatements.org/vocab/InC/1.0/", "NO DATA OF THIS TYPE",
                     "Latest Trends - A Georgia Trend Blog",
                     f"{c.inst_page}/collections/12939/seeds/2091989/metadata"],
                    [2472041, "https://www.legis.ga.gov/", "Map and Government Information Library",
                     "Georgia General Assembly", "Captured 2022-",
                     "Composed of the House of Representatives and the Senate, the Georgia General Assembly is one of "
                     "the largest state legislatures in the nation and sets the states annual operating budget, "
                     "proposes laws on a variety of topics, and contributes to the states health and growth by "
                     "collaborating in committees and meeting with constituents.",
                     "https://wayback.archive-it.org/15678/*/https://www.legis.ga.gov/", "English",
                     "NO DATA OF THIS TYPE", "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "NO DATA OF THIS TYPE", "Georgia General Assembly",
                     f"{c.inst_page}/collections/15678/seeds/2472041/metadata"],
                    [2485678, "https://deborahforda.com/",
                     "Richard B. Russell Library for Political Research and Studies", "Gonzalez, Deborah",
                     "Captured 2021", "NO DATA OF THIS TYPE",
                     "https://wayback.archive-it.org/12265-test/*/https://deborahforda.com/", "Spanish;English",
                     "RBRL/498: Deborah Gonzalez Papers", "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "NO DATA OF THIS TYPE", "Deborah Gonzalez for District Attorney",
                     f"{c.inst_page}/collections/12265/seeds/2485678/metadata"],
                    [2529656, "https://gatrees.org/", "Map and Government Information Library",
                     "Georgia Forestry Commission", "Captured 2022-",
                     "The Georgia Forestry Commission protects and conserves forests by suppressing wildfires, "
                     "providing rural fire department assistance, assisting landowners and communities with forest "
                     "management, and growing and selling quality tree seedlings for planting. Their main mission is "
                     "to provide leadership, service, and education to protect and conserve the states "
                     "forest resources.", "https://wayback.archive-it.org/15678/*/https://gatrees.org/", "English",
                     "NO DATA OF THIS TYPE", "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "NO DATA OF THIS TYPE", "Georgia Forestry Commission",
                     f"{c.inst_page}/collections/15678/seeds/2529656/metadata"],
                    [2547534, "https://www.facebook.com/adelayeltoncommunityleader/",
                     "Richard B. Russell Library for Political Research and Studies", "Adela Yelton", "Captured 2021-",
                     "NO DATA OF THIS TYPE",
                     "https://wayback.archive-it.org/12265/20210616194225/https://www.facebook.com/adelayeltoncommunityleader/",
                     "English", "RBRL/506: Adela Yelton Papers",
                     "In copyright: http://rightsstatements.org/vocab/InC/1.0/", "NO DATA OF THIS TYPE",
                     "Adela Yelton - Home | Facebook", f"{c.inst_page}/collections/12265/seeds/2547534/metadata"]]

        self.assertEqual(actual, expected, "Problem with test: all fields.")

    def test_required(self):
        """
        Tests the full script with the optional argument, which creates a report with just the fields.
        The result for testing is a small sample of rows, since there are many seeds and new seeds are added often.
        """
        script_path = os.path.join("..", "..", "seed_metadata_report.py")
        subprocess.run(f"python {script_path} required", shell=True)

        sample = [2024246, 2084781, 2091989, 2472041, 2485678, 2529656, 2547534]
        report_path = os.path.join(c.script_output, f"seed_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv")
        # Encoding errors are ignored, causing curly apostrophe's to be removed when the data is read into pandas.
        df_full = pd.read_csv(report_path, encoding_errors="ignore")
        df_sample = df_full.loc[df_full['ID'].isin(sample)]
        actual = [df_sample.columns.to_list()] + df_sample.values.tolist()

        expected = [["ID", "Name", "Collector", "Creator", "Date", "Identifier", "Language", "Rights", "Title",
                     "Archive-It Metadata Page"],
                    [2024246, "https://twitter.com/UGABTE/", "Hargrett Rare Book & Manuscript Library",
                     "UGA Black Theatrical Ensemble", "Captured 2019-",
                     "https://wayback.archive-it.org/12181/*/https://twitter.com/UGABTE/", "English",
                     "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "UGA Black Theatrical Ensemble Twittter",
                     f"{c.inst_page}/collections/12181/seeds/2024246/metadata"],
                    [2084781, "https://www.facebook.com/FootballUGA/", "Hargrett Rare Book & Manuscript Library",
                     "University of Georgia", "Captured 2019-",
                     "https://wayback.archive-it.org/12907/*/https://www.facebook.com/FootballUGA/", "English",
                     "In Copyright: http://rightsstatements.org/vocab/InC/1.0/", "UGA Football Facebook",
                     f"{c.inst_page}/collections/12907/seeds/2084781/metadata"],
                    [2091989, "https://georgiatrendblog.com/",
                     "Richard B. Russell Library for Political Research and Studies", "Georgia Trend Magazine",
                     "Captured 2019-",
                     "https://wayback.archive-it.org/12939/*/https://georgiatrendblog.com/", "English",
                     "In Copyright: http://rightsstatements.org/vocab/InC/1.0/", "Latest Trends - A Georgia Trend Blog",
                     f"{c.inst_page}/collections/12939/seeds/2091989/metadata"],
                    [2472041, "https://www.legis.ga.gov/", "Map and Government Information Library",
                     "Georgia General Assembly", "Captured 2022-",
                     "https://wayback.archive-it.org/15678/*/https://www.legis.ga.gov/", "English",
                     "In Copyright: http://rightsstatements.org/vocab/InC/1.0/", "Georgia General Assembly",
                     f"{c.inst_page}/collections/15678/seeds/2472041/metadata"],
                    [2485678, "https://deborahforda.com/",
                     "Richard B. Russell Library for Political Research and Studies", "Gonzalez, Deborah",
                     "Captured 2021",
                     "https://wayback.archive-it.org/12265-test/*/https://deborahforda.com/", "Spanish;English",
                     "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "Deborah Gonzalez for District Attorney",
                     f"{c.inst_page}/collections/12265/seeds/2485678/metadata"],
                    [2529656, "https://gatrees.org/", "Map and Government Information Library",
                     "Georgia Forestry Commission", "Captured 2022-",
                     "https://wayback.archive-it.org/15678/*/https://gatrees.org/", "English",
                     "In Copyright: http://rightsstatements.org/vocab/InC/1.0/", "Georgia Forestry Commission",
                     f"{c.inst_page}/collections/15678/seeds/2529656/metadata"],
                    [2547534, "https://www.facebook.com/adelayeltoncommunityleader/",
                     "Richard B. Russell Library for Political Research and Studies", "Adela Yelton", "Captured 2021-",
                     "https://wayback.archive-it.org/12265/20210616194225/https://www.facebook.com/adelayeltoncommunityleader/",
                     "English", "In copyright: http://rightsstatements.org/vocab/InC/1.0/",
                     "Adela Yelton - Home | Facebook", f"{c.inst_page}/collections/12265/seeds/2547534/metadata"]]

        self.assertEqual(actual, expected, "Problem with test: required fields.")


if __name__ == '__main__':
    unittest.main()

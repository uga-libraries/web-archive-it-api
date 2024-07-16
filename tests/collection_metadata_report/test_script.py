"""
Tests the output of the collection_metadata_report.py script, with and without the optional argument.
It gets metadata for all collections using the Archive-It Partner API and saves them to a CSV.
"""
import csv
from datetime import datetime
import os
import subprocess
import unittest
import configuration as c


class MyTestCase(unittest.TestCase):

    def tearDown(self):
        """
        Deletes the CSV produced by the script for each test.
        """
        os.remove(os.path.join(c.script_output, f"collection_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv"))

    def test_all(self):
        """
        Tests the full script without the optional argument, which creates a report with all fields.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        script_path = os.path.join("..", "..", "collection_metadata_report.py")
        subprocess.run(f"python {script_path}", shell=True)

        report_path = os.path.join(c.script_output, f"collection_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["ID", "Name", "Collector [required]", "Creator", "Date [required]", "Description [required]",
                     "Identifier", "Language", "Relation", "Rights", "Subject", "Title [required]",
                     "Archive-It Metadata Page"],
                    ["11071", "Trial 2018", "University of Georgia Libraries Testing",
                     "Test Creator Two;Test Creator One", "Captured 2018-2020",
                     "Tests run by Archive-It on UGA's behalf as a demonstration of the service while we considered "
                     "becoming subscribers.",
                     "Test ID", "Test Language Two;Test Language One",
                     "Test Relation Two;Test Relation One", "Test Rights Two;Test Rights One",
                     "Test Subject Two;Test Subject One", "Trial 2018", f"{c.inst_page}/collections/11071/metadata"],
                    ["12181", "University of Georgia Student Life", "Hargrett Rare Book & Manuscript Library",
                     "NO DATA OF THIS TYPE", "Captured 2019-",
                     "This collection contains websites related to the University of Georgia's "
                     "Division of Student Affairs and student organizations at UGA.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "University of Georgia Student Life",
                     f"{c.inst_page}/collections/12181/metadata"],
                    ["12249", "Experiments", "University of Georgia Libraries Testing", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE",
                     "Seeds used for practicing with Archive-It. Not intended for permanent preservation.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Experiments", f"{c.inst_page}/collections/12249/metadata"],
                    ["12262", "Political Observers", "Richard B. Russell Library for Political Research and Studies",
                     "NO DATA OF THIS TYPE", "Captured 2019-", "This collections contains websites created by "
                                                               "journalists, academics, and other political observers.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Political Observers", f"{c.inst_page}/collections/12262/metadata"],
                    ["12263", "Activists and Advocates",
                     "Richard B. Russell Library for Political Research and Studies", "NO DATA OF THIS TYPE",
                     "Captured 2019-", "This collections contains websites created by organizations and individuals "
                                       "engaged in sociopolitical activism and advocacy in Georgia.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Activists and Advocates", f"{c.inst_page}/collections/12263/metadata"],
                    ["12264", "Georgia Disability History Archive",
                     "Richard B. Russell Library for Political Research and Studies", "NO DATA OF THIS TYPE",
                     "Captured 2019-",
                     "The Georgia Disability History Archive seeks to document the vital and transformative work "
                     "undertaken by disability activists, advocates, and organizations and, crucially, the experiences "
                     "of people with disabilities over the past 100-plus years in the state of Georgia. "
                     "Major collecting areas include, but are not limited to: accessibility, activism and social "
                     "justice, citizen advocacy, independent and community living, self-advocacy, education, "
                     "employment, recreation, culture and pride.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Georgia Disability History Archive",
                     f"{c.inst_page}/collections/12264/metadata"],
                    ["12265", "Georgia Politics", "Richard B. Russell Library for Political Research and Studies",
                     "NO DATA OF THIS TYPE", "Captured 2019-",
                     "This collection contains websites documenting political activity in the state of Georgia "
                     "including those created by political candidates, elected officials, and political parties.",
                     "https://wayback.archive-it.org/12265/*/https://www.youtube.com/channel/UC-LF69SBOSgT1S1-yy-VgaA/videos?view=0&sort=dd&shelf_id=0",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                    "Georgia Politics", f"{c.inst_page}/collections/12265/metadata"],
                    ["12274", "Georgia Newspapers", "The Digital Library of Georgia", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE",
                     "Test crawls for the Georgia Newspaper Project pilot for collecting born-digital newspapers.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Georgia Newspapers", f"{c.inst_page}/collections/12274/metadata"],
                    ["12470", "The Now Explosion", "The Walter J. Brown Media Archives & Peabody Awards Collection",
                     "NO DATA OF THIS TYPE", "Captured 2020",
                     "Websites related to The Now Explosion television program.", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "The Now Explosion",
                     f"{c.inst_page}/collections/12470/metadata"],
                    ["12907", "University of Georgia Athletics", "Hargrett Rare Book & Manuscript Library",
                     "NO DATA OF THIS TYPE", "Captured 2019-",
                     "This collection contains websites related to the athletic programs at the University of Georgia.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "University of Georgia Athletics",
                     f"{c.inst_page}/collections/12907/metadata"],
                    ["12912", "University of Georgia Administration", "Hargrett Rare Book & Manuscript Library",
                     "NO DATA OF THIS TYPE", "Captured 2019-",
                     "This collection contains websites related to the University of Georgia's administration, "
                     "including the Office of the President, the Provost, and other leadership roles.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "University of Georgia Administration",
                     f"{c.inst_page}/collections/12912/metadata"],
                    ["12939", "Business", "Richard B. Russell Library for Political Research and Studies",
                     "NO DATA OF THIS TYPE", "Captured 2019-",
                     "This collection contains websites documenting business and "
                     "private enterprise in the state of Georgia.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Business", f"{c.inst_page}/collections/12939/metadata"],
                    ["12944", "Legal", "Richard B. Russell Library for Political Research and Studies",
                     "NO DATA OF THIS TYPE", "Captured 2019-",
                     "This collections contains websites created by attorneys, judges, and organizations working "
                     "on legal issues in the state of Georgia.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Legal", f"{c.inst_page}/collections/12944/metadata"],
                    ["15678", "Georgia Government Publications", "Map and Government Information Library",
                     "NO DATA OF THIS TYPE", "Captured 2022-",
                     "The University of Georgia Libraries is the official depository for Georgia state publications "
                     "and, as such, is responsible for their collection, preservation, and accessibility. The Georgia "
                     "Government Publications Website Archive includes websites of Georgia state agencies and "
                     "organizations, with an emphasis on those of the executive branch. Select publications included "
                     "in these websites are also available in the Digital Library of Georgia, "
                     "Georgia Government Publications collection.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "Georgia Government Publications Website Archive",
                     f"{c.inst_page}/collections/15678/metadata"],
                    ["16951", "University of Georgia Academics", "Hargrett Rare Book & Manuscript Library",
                     "NO DATA OF THIS TYPE", "Captured 2021-",
                     "This collection contains websites related research and instruction at the University of Georgia.",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "University of Georgia Academics",
                     f"{c.inst_page}/collections/16951/metadata"],
                    ["21635", "Hargrett Manuscripts", "Hargrett Rare Book & Manuscript Library",
                     "NO DATA OF THIS TYPE", "Captured 2024-",
                     "This collection contains websites documenting the literary, cultural, social, and economic "
                     "history of Georgia and its peoples, in accordance with the broader collection development "
                     "policy of the Hargrett Library.", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                     "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "Hargrett Manuscripts",
                     f"{c.inst_page}/collections/21635/metadata"]]

        self.assertEqual(actual, expected, "Problem with test: all fields.")

    def test_required(self):
        """
        Tests the full script with the optional argument, which creates a report with required fields only.
        Result for testing is the contents of the spreadsheet created by the script.
        """
        script_path = os.path.join("..", "..", "collection_metadata_report.py")
        subprocess.run(f"python {script_path} required", shell=True)

        report_path = os.path.join(c.script_output, f"collection_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv")
        with open(report_path, newline="") as open_file:
            reader = csv.reader(open_file)
            actual = list(reader)

        expected = [["ID", "Name", "Collector", "Date", "Description", "Title", "Archive-It Metadata Page"],
                    ["11071", "Trial 2018", "University of Georgia Libraries Testing", "Captured 2018-2020",
                     "Tests run by Archive-It on UGA's behalf as a demonstration of the service while we "
                     "considered becoming subscribers.",
                     "Trial 2018", f"{c.inst_page}/collections/11071/metadata"],
                    ["12181", "University of Georgia Student Life", "Hargrett Rare Book & Manuscript Library",
                     "Captured 2019-", "This collection contains websites related to the University of Georgia's "
                                       "Division of Student Affairs and student organizations at UGA.",
                     "University of Georgia Student Life", f"{c.inst_page}/collections/12181/metadata"],
                    ["12249", "Experiments", "University of Georgia Libraries Testing", "NO DATA OF THIS TYPE",
                     "Seeds used for practicing with Archive-It. Not intended for permanent preservation.",
                     "Experiments", f"{c.inst_page}/collections/12249/metadata"],
                    ["12262", "Political Observers", "Richard B. Russell Library for Political Research and Studies",
                     "Captured 2019-", "This collections contains websites created by journalists, academics, and "
                                       "other political observers.",
                     "Political Observers", f"{c.inst_page}/collections/12262/metadata"],
                    ["12263", "Activists and Advocates",
                     "Richard B. Russell Library for Political Research and Studies", "Captured 2019-",
                     "This collections contains websites created by organizations and individuals engaged in "
                     "sociopolitical activism and advocacy in Georgia.",
                     "Activists and Advocates", f"{c.inst_page}/collections/12263/metadata"],
                    ["12264", "Georgia Disability History Archive",
                     "Richard B. Russell Library for Political Research and Studies", "Captured 2019-",
                     "The Georgia Disability History Archive seeks to document the vital and transformative work "
                     "undertaken by disability activists, advocates, and organizations and, crucially, the "
                     "experiences of people with disabilities over the past 100-plus years in the state of Georgia. "
                     "Major collecting areas include, but are not limited to: accessibility, activism and social "
                     "justice, citizen advocacy, independent and community living, self-advocacy, education, "
                     "employment, recreation, culture and pride.",
                     "Georgia Disability History Archive", f"{c.inst_page}/collections/12264/metadata"],
                    ["12265", "Georgia Politics", "Richard B. Russell Library for Political Research and Studies",
                     "Captured 2019-", "This collection contains websites documenting political activity in the state "
                                       "of Georgia including those created by political candidates, elected officials, "
                                       "and political parties.",
                     "Georgia Politics", f"{c.inst_page}/collections/12265/metadata"],
                    ["12274", "Georgia Newspapers", "The Digital Library of Georgia", "NO DATA OF THIS TYPE",
                     "Test crawls for the Georgia Newspaper Project pilot for collecting born-digital newspapers.",
                     "Georgia Newspapers", f"{c.inst_page}/collections/12274/metadata"],
                    ["12470", "The Now Explosion", "The Walter J. Brown Media Archives & Peabody Awards Collection",
                     "Captured 2020", "Websites related to The Now Explosion television program.",
                     "The Now Explosion", f"{c.inst_page}/collections/12470/metadata"],
                    ["12907", "University of Georgia Athletics", "Hargrett Rare Book & Manuscript Library",
                     "Captured 2019-", "This collection contains websites related to the athletic programs "
                                       "at the University of Georgia.",
                     "University of Georgia Athletics", f"{c.inst_page}/collections/12907/metadata"],
                    ["12912", "University of Georgia Administration", "Hargrett Rare Book & Manuscript Library",
                     "Captured 2019-", "This collection contains websites related to the University of Georgia's "
                                       "administration, including the Office of the President, the Provost, and "
                                       "other leadership roles.",
                     "University of Georgia Administration", f"{c.inst_page}/collections/12912/metadata"],
                    ["12939", "Business", "Richard B. Russell Library for Political Research and Studies",
                     "Captured 2019-", "This collection contains websites documenting business and private "
                                       "enterprise in the state of Georgia.",
                     "Business", f"{c.inst_page}/collections/12939/metadata"],
                    ["12944", "Legal", "Richard B. Russell Library for Political Research and Studies",
                     "Captured 2019-", "This collections contains websites created by attorneys, judges, and "
                                       "organizations working on legal issues in the state of Georgia.",
                     "Legal", f"{c.inst_page}/collections/12944/metadata"],
                    ["15678", "Georgia Government Publications", "Map and Government Information Library",
                     "Captured 2022-", "The University of Georgia Libraries is the official depository for Georgia "
                                       "state publications and, as such, is responsible for their collection, "
                                       "preservation, and accessibility. The Georgia Government Publications Website "
                                       "Archive includes websites of Georgia state agencies and organizations, with "
                                       "an emphasis on those of the executive branch. Select publications included "
                                       "in these websites are also available in the Digital Library of Georgia, "
                                       "Georgia Government Publications collection.",
                     "Georgia Government Publications Website Archive", f"{c.inst_page}/collections/15678/metadata"],
                    ["16951", "University of Georgia Academics", "Hargrett Rare Book & Manuscript Library",
                     "Captured 2021-", "This collection contains websites related research and instruction at the "
                                       "University of Georgia.",
                     "University of Georgia Academics", f"{c.inst_page}/collections/16951/metadata"],
                    ["21635", "Hargrett Manuscripts", "Hargrett Rare Book & Manuscript Library", "Captured 2024-",
                     "This collection contains websites documenting the literary, cultural, social, and economic "
                     "history of Georgia and its peoples, in accordance with the broader collection development "
                     "policy of the Hargrett Library.", "Hargrett Manuscripts",
                     f"{c.inst_page}/collections/21635/metadata"]
                    ]

        self.assertEqual(actual, expected, "Problem with test: required fields.")


if __name__ == '__main__':
    unittest.main()

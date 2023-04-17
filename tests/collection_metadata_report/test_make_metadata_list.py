"""
Tests for the make_metadata_list() function from the collection_metadata_report.py script.
It converts the metadata for a single collection into a list, to use for saving to the CSV.
"""
import unittest
from collection_metadata_report import make_metadata_list
from configuration import inst_page


class MyTestCase(unittest.TestCase):

    def test_all_optional_missing(self):
        """
        Tests that the function returns the expected list of metadata values
        when all fields are to be included and all optional fields are missing.
        """

        test_data = {'account': 1468, 'created_by': 'system', 'created_date': '2018-09-19T22:45:21Z',
                     'deleted': False, 'id': 11071, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2022-01-18T18:11:43.740774Z', 'metadata':
                         {'Collector': [{'id': 7695086, 'value': 'UGA Libraries'}],
                          'Date': [{'id': 8590671, 'value': 'Captured 2018-2020'}],
                          'Description': [{'id': 6803212, 'value': "Tests run by Archive-It for UGA."}],
                          'Title': [{'id': 6803211, 'value': 'Trial 2018'}]},
                     'name': 'Trial 2018', 'oai_exported': False,
                     'private_access_token': '4d5ea946cd554ac98aabd36b392b6637', 'publicly_visible': False,
                     'state': 'INACTIVE', 'topics': None}
        header = ["ID", "Name", "Collector [required]", "Creator", "Date [required]", "Description [required]",
                  "Identifier", "Language", "Relation", "Rights", "Subject", "Title [required]",
                  "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [11071, "Trial 2018", "UGA Libraries", "NO DATA OF THIS TYPE", "Captured 2018-2020",
                    "Tests run by Archive-It for UGA.", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE",
                    "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "NO DATA OF THIS TYPE", "Trial 2018",
                    f"{inst_page}/collections/11071/metadata"]

        self.assertEqual(actual, expected, "Problem with test: all metadata, optional missing.")

    def test_all_once(self):
        """
        Tests that the function returns the expected list of metadata values
        when all fields are to be included and all fields occur once.
        """

        test_data = {'account': 1468, 'created_by': 'system', 'created_date': '2018-09-19T22:45:21Z',
                     'deleted': False, 'id': 11071, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2022-01-18T18:11:43.740774Z', 'metadata':
                         {'Collector': [{'id': 7695086, 'value': 'UGA Libraries'}],
                          'Creator': [{'id': 7236758, 'value': 'Test Creator One'}],
                          'Date': [{'id': 8590671, 'value': 'Captured 2018-2020'}],
                          'Description': [{'id': 6803212, 'value': "Tests run by Archive-It for UGA."}],
                          'Identifier': [{'id': 7236752, 'value': 'Test ID'}],
                          'Language': [{'id': 7236762, 'value': 'Test Language One'}],
                          'Relation': [{'id': 7236755, 'value': 'Test Relation One'}],
                          'Rights': [{'id': 7236760, 'value': 'Test Rights One'}],
                          'Subject': [{'id': 7236753, 'value': 'Test Subject One'}],
                          'Title': [{'id': 6803211, 'value': 'Trial 2018'}]},
                     'name': 'Trial 2018', 'oai_exported': False,
                     'private_access_token': '4d5ea946cd554ac98aabd36b392b6637', 'publicly_visible': False,
                     'state': 'INACTIVE', 'topics': None}
        header = ["ID", "Name", "Collector [required]", "Creator", "Date [required]", "Description [required]",
                  "Identifier", "Language", "Relation", "Rights", "Subject", "Title [required]",
                  "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [11071, "Trial 2018", "UGA Libraries", "Test Creator One", "Captured 2018-2020",
                    "Tests run by Archive-It for UGA.", "Test ID", "Test Language One", "Test Relation One",
                    "Test Rights One", "Test Subject One", "Trial 2018", f"{inst_page}/collections/11071/metadata"]

        self.assertEqual(actual, expected, "Problem with test: all metadata, all fields once.")

    def test_all_twice(self):
        """
        Tests that the function returns the expected list of metadata values
        when all fields are to be included and all repeatable fields occur twice.
        """

        test_data = {'account': 1468, 'created_by': 'system', 'created_date': '2018-09-19T22:45:21Z',
                     'deleted': False, 'id': 11071, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2022-01-18T18:11:43.740774Z', 'metadata':
                         {'Collector': [{'id': 7695086, 'value': 'UGA Libraries'}],
                          'Creator': [{'id': 7236758, 'value': 'Test Creator One'},
                                      {'id': 7236759, 'value': 'Test Creator Two'}],
                          'Date': [{'id': 8590671, 'value': 'Captured 2018-2020'}],
                          'Description': [{'id': 6803212, 'value': "Tests run by Archive-It for UGA."}],
                          'Identifier': [{'id': 7236752, 'value': 'Test ID'}],
                          'Language': [{'id': 7236762, 'value': 'Test Language One'},
                                       {'id': 7236763, 'value': 'Test Language Two'}],
                          'Relation': [{'id': 7236755, 'value': 'Test Relation One'},
                                       {'id': 7236756, 'value': 'Test Relation Two'}],
                          'Rights': [{'id': 7236760, 'value': 'Test Rights One'},
                                     {'id': 7236761, 'value': 'Test Rights Two'}, ],
                          'Subject': [{'id': 7236753, 'value': 'Test Subject One'},
                                      {'id': 7236754, 'value': 'Test Subject Two'}],
                          'Title': [{'id': 6803211, 'value': 'Trial 2018'}]},
                     'name': 'Trial 2018', 'oai_exported': False,
                     'private_access_token': '4d5ea946cd554ac98aabd36b392b6637', 'publicly_visible': False,
                     'state': 'INACTIVE', 'topics': None}
        header = ["ID", "Name", "Collector [required]", "Creator", "Date [required]", "Description [required]",
                  "Identifier", "Language", "Relation", "Rights", "Subject", "Title [required]",
                  "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [11071, "Trial 2018", "UGA Libraries", "Test Creator One;Test Creator Two", "Captured 2018-2020",
                    "Tests run by Archive-It for UGA.", "Test ID", "Test Language One;Test Language Two",
                    "Test Relation One;Test Relation Two", "Test Rights One;Test Rights Two",
                    "Test Subject One;Test Subject Two", "Trial 2018", f"{inst_page}/collections/11071/metadata"]

        self.assertEqual(actual, expected, "Problem with test: all metadata, repeatable fields twice.")

    def test_required(self):
        """
        Tests that the function returns the expected list of metadata values
        when only required fields are included, and all are present one time.
        None of the required collection fields can repeat.
        """

        test_data = {'account': 1468, 'created_by': 'sarmour', 'created_date': '2019-10-08T14:08:42.636015Z',
                     'deleted': False, 'id': 12907, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2020-07-27T14:07:51.214507Z', 'metadata':
                         {'Collector': [{'id': 5305369, 'value': 'Hargrett Rare Book & Manuscript Library'}],
                          'Date': [{'id': 5962113, 'value': 'Captured 2019-'}],
                          'Description': [{'id': 5305368, 'value': 'Websites related to UGA athletics.'}],
                          'Title': [{'id': 5962112, 'value': 'University of Georgia Athletics'}]},
                     'name': 'University of Georgia Athletics', 'oai_exported': False,
                     'private_access_token': '2643e534b8ef4c35ae37e59cabec5f71', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None}
        header = ["ID", "Name", "Collector", "Date", "Description", "Title", "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [12907, "University of Georgia Athletics", "Hargrett Rare Book & Manuscript Library",
                    "Captured 2019-", "Websites related to UGA athletics.", "University of Georgia Athletics",
                    f"{inst_page}/collections/12907/metadata"]

        self.assertEqual(actual, expected, "Problem with test: required metadata.")


if __name__ == '__main__':
    unittest.main()

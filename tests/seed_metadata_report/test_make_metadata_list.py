"""
Tests for the make_metadata_list() function from the seed_metadata_report.py script.
It converts the metadata for a single collection into a list, to use for saving to the CSV..
"""
import unittest
from seed_metadata_report import make_metadata_list
from configuration import inst_page


class MyTestCase(unittest.TestCase):

    def test_all_optional_missing(self):
        """
        Tests that the function returns the expected list of metadata values
        when all fields are included and all optional fields are missing.
        """

        test_data = {'active': True, 'canonical_url': 'https://gcdd.org/', 'collection': 12264,
                     'crawl_definition': 31104607716, 'created_by': 'bpieczko',
                     'created_date': '2019-07-09T15:04:00.354148Z', 'deleted': False, 'http_response_code': 200,
                     'id': 2027713, 'last_checked_http_response_code': '2019-07-09T15:06:45.692000Z',
                     'last_updated_by': 'robert.lay', 'last_updated_date': '2022-11-22T19:31:20.251836Z',
                     'login_password': None, 'login_username': None, 'metadata':
                         {'Collector': [{'id': 4591723,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Creator': [{'id': 4591725, 'value': 'Georgia Council on Developmental Disabilities'}],
                          'Date': [{'id': 4660747, 'value': 'Captured 2019-'}],
                          'Identifier': [{'id': 4965599,
                                          'value': 'https://wayback.archive-it.org/12264/*/https://gcdd.org/'}],
                          'Language': [{'id': 4591724, 'value': 'English'}, {'id': 4632296, 'value': 'Spanish'}],
                          'Rights': [{'id': 4769385,
                                      'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'}],
                          'Title': [{'id': 4969284, 'value': 'Georgia Council on Developmental Disabilities'}]},
                     'publicly_visible': True, 'seed_groups': [], 'seed_type': 'oneHopOff',
                     'url': 'https://gcdd.org/', 'valid': None}
        header = ["ID", "Name", "Collector [required]", "Creator [required]", "Date [required]", "Description",
                  "Identifier [required]", "Language [required]", "Relation", "Rights [required]", "Subject",
                  "Title [required]", "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [2027713, "https://gcdd.org/", "Richard B. Russell Library for Political Research and Studies",
                    "Georgia Council on Developmental Disabilities", "Captured 2019-", "NO DATA OF THIS TYPE",
                    "https://wayback.archive-it.org/12264/*/https://gcdd.org/", "English;Spanish",
                    "NO DATA OF THIS TYPE", "In Copyright: http://rightsstatements.org/vocab/InC/1.0/",
                    "NO DATA OF THIS TYPE", "Georgia Council on Developmental Disabilities",
                    f"{inst_page}/collections/12264/seeds/2027713/metadata"]

        self.assertEqual(actual, expected, "Problem with test: all metadata, optional missing.")

    def test_all_once(self):
        """
        Tests that the function returns the expected list of metadata values
        when all fields are included and all fields occur once.
        """

        test_data = {'active': True, 'canonical_url': 'https://gcdd.org/', 'collection': 12264,
                     'crawl_definition': 31104607716, 'created_by': 'bpieczko',
                     'created_date': '2019-07-09T15:04:00.354148Z', 'deleted': False, 'http_response_code': 200,
                     'id': 2027713, 'last_checked_http_response_code': '2019-07-09T15:06:45.692000Z',
                     'last_updated_by': 'robert.lay', 'last_updated_date': '2022-11-22T19:31:20.251836Z',
                     'login_password': None, 'login_username': None, 'metadata':
                         {'Collector': [{'id': 4591723,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Creator': [{'id': 4591725, 'value': 'Georgia Council on Developmental Disabilities'}],
                          'Date': [{'id': 4660747, 'value': 'Captured 2019-'}],
                          'Description': [{'id': 4594452,
                                           'value': 'Develops and supports public policy.'}],
                          'Identifier': [{'id': 4965599,
                                          'value': 'https://wayback.archive-it.org/12264/*/https://gcdd.org/'}],
                          'Language': [{'id': 4632296, 'value': 'Spanish'}],
                          'Relation': [{'id': 4969283,
                                        'value': 'RBRL/432: Georgia Council on Developmental Disabilities Records'}],
                          'Rights': [{'id': 4769385,
                                      'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'}],
                          'Subject': [{'id': 0000000, 'value': 'Test Subject'}],
                          'Title': [{'id': 4969284, 'value': 'Georgia Council on Developmental Disabilities'}]},
                     'publicly_visible': True, 'seed_groups': [], 'seed_type': 'oneHopOff',
                     'url': 'https://gcdd.org/', 'valid': None}
        header = ["ID", "Name", "Collector [required]", "Creator [required]", "Date [required]", "Description",
                  "Identifier [required]", "Language [required]", "Relation", "Rights [required]", "Subject",
                  "Title [required]", "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [2027713, "https://gcdd.org/", "Richard B. Russell Library for Political Research and Studies",
                    "Georgia Council on Developmental Disabilities", "Captured 2019-",
                    "Develops and supports public policy.", "https://wayback.archive-it.org/12264/*/https://gcdd.org/",
                    "Spanish", "RBRL/432: Georgia Council on Developmental Disabilities Records",
                    "In Copyright: http://rightsstatements.org/vocab/InC/1.0/", "Test Subject",
                    "Georgia Council on Developmental Disabilities",
                    f"{inst_page}/collections/12264/seeds/2027713/metadata"]

        self.assertEqual(actual, expected, "Problem with test: all metadata, all fields once.")

    def test_all_twice(self):
        """
        Tests that the function returns the expected list of metadata values
        when all fields are included and all repeatable fields occur twice.
        """

        test_data = {'active': True, 'canonical_url': 'https://gcdd.org/', 'collection': 12264,
                     'crawl_definition': 31104607716, 'created_by': 'bpieczko',
                     'created_date': '2019-07-09T15:04:00.354148Z', 'deleted': False, 'http_response_code': 200,
                     'id': 2027713, 'last_checked_http_response_code': '2019-07-09T15:06:45.692000Z',
                     'last_updated_by': 'robert.lay', 'last_updated_date': '2022-11-22T19:31:20.251836Z',
                     'login_password': None, 'login_username': None, 'metadata':
                         {'Collector': [{'id': 4591723,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Creator': [{'id': 4591725, 'value': 'Georgia Council on Developmental Disabilities'},
                                      {'id': 0000000, 'value': 'Test Creator'}],
                          'Date': [{'id': 4660747, 'value': 'Captured 2019-'}],
                          'Description': [{'id': 4594452,
                                           'value': 'Develops and supports public policy.'}],
                          'Identifier': [{'id': 4965599,
                                          'value': 'https://wayback.archive-it.org/12264/*/https://gcdd.org/'}],
                          'Language': [{'id': 4591724, 'value': 'English'}, {'id': 4632296, 'value': 'Spanish'}],
                          'Relation': [{'id': 4969283,
                                        'value': 'RBRL/432: Georgia Council on Developmental Disabilities Records'},
                                       {'id': 0000000, 'value': 'Test Relation'}],
                          'Rights': [{'id': 4769385,
                                      'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'},
                                     {'id': 0000000, 'value': 'Test Right'}],
                          'Subject': [{'id': 0000000, 'value': 'Test Subject'},
                                      {'id': 0000000, 'value': 'Test Subject Two'}],
                          'Title': [{'id': 4969284, 'value': 'Georgia Council on Developmental Disabilities'}]},
                     'publicly_visible': True, 'seed_groups': [], 'seed_type': 'oneHopOff',
                     'url': 'https://gcdd.org/', 'valid': None}
        header = ["ID", "Name", "Collector [required]", "Creator [required]", "Date [required]", "Description",
                  "Identifier [required]", "Language [required]", "Relation", "Rights [required]", "Subject",
                  "Title [required]", "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [2027713, "https://gcdd.org/", "Richard B. Russell Library for Political Research and Studies",
                    "Georgia Council on Developmental Disabilities;Test Creator", "Captured 2019-",
                    "Develops and supports public policy.", "https://wayback.archive-it.org/12264/*/https://gcdd.org/",
                    "English;Spanish", "RBRL/432: Georgia Council on Developmental Disabilities Records;Test Relation",
                    "In Copyright: http://rightsstatements.org/vocab/InC/1.0/;Test Right",
                    "Test Subject;Test Subject Two", "Georgia Council on Developmental Disabilities",
                    f"{inst_page}/collections/12264/seeds/2027713/metadata"]

        self.assertEqual(actual, expected, "Problem with test: all metadata, repeatable fields twice.")

    def test_required_once(self):
        """
        Tests that the function returns the expected list of metadata values
        when only required fields are included and all fields occur once.
        """

        test_data = {'active': True, 'canonical_url': 'https://gbp.georgia.gov/', 'collection': 15678,
                     'crawl_definition': 31104407627, 'created_by': 'scausey',
                     'created_date': '2021-05-05T17:53:41.437412Z', 'deleted': False, 'http_response_code': None,
                     'id': 2529629, 'last_checked_http_response_code': None, 'last_updated_by': 'scausey',
                     'last_updated_date': '2022-03-24T16:18:49.114726Z', 'login_password': None, 'login_username': None,
                     'metadata': {'Collector': [{'id': 8453774, 'value': 'Map and Government Information Library'}],
                                  'Creator': [{'id': 8453772, 'value': 'Georgia Board of Pharmacy'}],
                                  'Date': [{'id': 8453770, 'value': 'Captured 2022-'}],
                                  'Identifier': [{'id': 8453767,
                                                  'value': 'https://wayback.archive-it.org/15678/*/https://gbp.georgia.gov/'}],
                                  'Language': [{'id': 8453771, 'value': 'English'}],
                                  'Rights': [{'id': 8453768,
                                              'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'}],
                                  'Title': [{'id': 8453773, 'value': 'Georgia Board of Pharmacy'}]},
                     'publicly_visible': True, 'seed_groups': [], 'seed_type': 'normal',
                     'url': 'https://gbp.georgia.gov/', 'valid': None}
        header = ["ID", "Name", "Collector", "Creator", "Date", "Identifier", "Language", "Rights", "Title",
                  "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [2529629, "https://gbp.georgia.gov/", "Map and Government Information Library",
                    "Georgia Board of Pharmacy", "Captured 2022-",
                    "https://wayback.archive-it.org/15678/*/https://gbp.georgia.gov/", "English",
                    "In Copyright: http://rightsstatements.org/vocab/InC/1.0/", "Georgia Board of Pharmacy",
                    f"{inst_page}/collections/15678/seeds/2529629/metadata"]

        self.assertEqual(actual, expected, "Problem with test: required metadata, all fields once.")

    def test_required_twice(self):
        """
        Tests that the function returns the expected list of metadata values
        when only required fields are included all repeatable fields occur twice.
        """

        test_data = {'active': True, 'canonical_url': 'https://gbp.georgia.gov/', 'collection': 15678,
                     'crawl_definition': 31104407627, 'created_by': 'scausey',
                     'created_date': '2021-05-05T17:53:41.437412Z', 'deleted': False, 'http_response_code': None,
                     'id': 2529629, 'last_checked_http_response_code': None, 'last_updated_by': 'scausey',
                     'last_updated_date': '2022-03-24T16:18:49.114726Z', 'login_password': None, 'login_username': None,
                     'metadata': {'Collector': [{'id': 8453774, 'value': 'Map and Government Information Library'}],
                                  'Creator': [{'id': 8453772, 'value': 'Georgia Board of Pharmacy'},
                                              {'id': 0000000, 'value': 'Test Creator'}],
                                  'Date': [{'id': 8453770, 'value': 'Captured 2022-'}],
                                  'Identifier': [{'id': 8453767,
                                                  'value': 'https://wayback.archive-it.org/15678/*/https://gbp.georgia.gov/'}],
                                  'Language': [{'id': 8453771, 'value': 'English'},
                                               {'id': 0000000, 'value': 'Test Language'}],
                                  'Rights': [{'id': 8453768,
                                              'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'},
                                             {'id': 0000000, 'value': 'Test Right'}],
                                  'Title': [{'id': 8453773, 'value': 'Georgia Board of Pharmacy'}]},
                     'publicly_visible': True, 'seed_groups': [], 'seed_type': 'normal',
                     'url': 'https://gbp.georgia.gov/', 'valid': None}
        header = ["ID", "Name", "Collector", "Creator", "Date", "Identifier", "Language", "Rights", "Title",
                  "Archive-It Metadata Page"]
        actual = make_metadata_list(test_data, header)

        expected = [2529629, "https://gbp.georgia.gov/", "Map and Government Information Library",
                    "Georgia Board of Pharmacy;Test Creator", "Captured 2022-",
                    "https://wayback.archive-it.org/15678/*/https://gbp.georgia.gov/", "English;Test Language",
                    "In Copyright: http://rightsstatements.org/vocab/InC/1.0/;Test Right", "Georgia Board of Pharmacy",
                    f"{inst_page}/collections/15678/seeds/2529629/metadata"]

        self.assertEqual(actual, expected, "Problem with test: required metadata, repeatable fields twice.")


if __name__ == '__main__':
    unittest.main()

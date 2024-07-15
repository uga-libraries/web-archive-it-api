"""
Tests for the get_metadata() function from the seed_metadata_report.py script.
It gets and returns metadata for all seeds using the Archive-It Partner API.
"""
import unittest
from seed_metadata_report import get_metadata


class MyTestCase(unittest.TestCase):

    def test_correct(self):
        """
        Tests that the function returns the expected metadata values.
        The total is too large and too changing (new seeds are added regularly) to test the entire data set.
        Instead, the metadata for a few seeds is checked.
        """

        seed_metadata = get_metadata()
        actual = [seed_metadata[45], seed_metadata[90], seed_metadata[135], seed_metadata[180], seed_metadata[225]]

        expected = [{'active': True, 'canonical_url': 'https://www.uga.edu/', 'collection': 12912,
                     'crawl_definition': 31104266804, 'created_by': 'sarmour',
                     'created_date': '2020-03-26T19:33:20.013192Z', 'deleted': False, 'http_response_code': None,
                     'id': 2173766, 'last_checked_http_response_code': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2024-05-01T13:30:32.175384Z', 'login_password': None,
                     'login_username': None, 'metadata':
                         {'Identifier': [{'id': 5898372, 'value': 'https://wayback.archive-it.org/12912/*/https://www.uga.edu/'}],
                          'Creator': [{'id': 5819711, 'value': 'University of Georgia'}],
                          'Collector': [{'id': 5819710, 'value': 'Hargrett Rare Book & Manuscript Library'}],
                          'Title': [{'id': 5819713, 'value': 'University of Georgia homepage'}],
                          'Date': [{'id': 5819708, 'value': 'Captured 2020-'}],
                          'Language': [{'id': 5819712, 'value': 'English'}],
                          'Rights': [{'id': 5819709, 'value': 'http://rightsstatements.org/vocab/InC/1.0/'}]},
                     'publicly_visible': False, 'seed_groups': [], 'seed_type': 'normal', 'url': 'https://www.uga.edu/',
                     'valid': None},
                    {'active': True, 'canonical_url': 'https://www.facebook.com/Trammell132/photos/',
                     'collection': 12265, 'crawl_definition': 31104392189, 'created_by': 'robert.lay',
                     'created_date': '2021-02-05T20:57:44.813684Z', 'deleted': False, 'http_response_code': None,
                     'id': 2481704, 'last_checked_http_response_code': None, 'last_updated_by': 'robert.lay',
                     'last_updated_date': '2022-10-21T19:43:24.143576Z', 'login_password': None,
                     'login_username': None, 'metadata':
                         {'Language': [{'value': 'English', 'id': 6962751}],
                          'Title': [{'value': 'Bob Trammell for State House - Photos | Facebook', 'id': 6880792}],
                          'Date': [{'value': 'Captured 2021', 'id': 6962749}],
                          'Identifier': [{'value': 'https://wayback.archive-it.org/12265/*/https://www.facebook.com/Trammell132/photos/',
                                          'id': 6962750}],
                          'Creator': [{'value': 'Trammell, Bob', 'id': 6880793}],
                          'Collector': [{'value': 'Richard B. Russell Library for Political Research and Studies',
                                         'id': 6880788}],
                          'Rights': [{'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/',
                                      'id': 6962748}],
                          'Relation': [{'value': 'RBRL/494: Bob Trammell Papers', 'id': 6880790}]},
                     'publicly_visible': False, 'seed_groups': [{'account': 1468, 'collections': [12265], 'id': 12980,
                                                                 'name': 'Bob Trammell', 'visibility': 'PUBLIC'}],
                     'seed_type': 'normal', 'url': 'https://www.facebook.com/Trammell132/photos/', 'valid': None},
                    {'active': True, 'canonical_url': 'https://gcfv.georgia.gov/', 'collection': 15678,
                     'crawl_definition': 31104407627, 'created_by': 'scausey',
                     'created_date': '2021-05-05T17:53:41.527988Z', 'deleted': False, 'http_response_code': None,
                     'id': 2529632, 'last_checked_http_response_code': None, 'last_updated_by': 'scausey',
                     'last_updated_date': '2022-03-24T16:18:48.856992Z', 'login_password': None,
                     'login_username': None, 'metadata':
                         {'Creator': [{'value': 'Georgia Commission on Family Violence', 'id': 8453788}],
                          'Description': [{'value': 'Administratively attached to the Department of Community '
                                                    'Supervision (DCS), the Georgia Commission on Family '
                                                    'Violence ensures their belief that a coordinated community '
                                                    'response is the best way to address the problem of family '
                                                    'violence by working with communities and systems across '
                                                    'the state of Georgia to provide leadership in '
                                                    'strengthening Georgia’s families.',
                                           'id': 8453785}],
                          'Title': [{'value': 'Georgia Commission on Family Violence', 'id': 8453789}],
                          'Date': [{'value': 'Captured 2022-', 'id': 8453786}],
                          'Identifier': [{'value': 'https://wayback.archive-it.org/15678/*/https://gcfv.georgia.gov/',
                                          'id': 8453783}],
                          'Language': [{'value': 'English', 'id': 8453787}],
                          'Collector': [{'value': 'Map and Government Information Library', 'id': 8453790}],
                          'Rights': [{'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/',
                                      'id': 8453784}]},
                     'publicly_visible': True, 'seed_groups': [], 'seed_type': 'normal',
                     'url': 'https://gcfv.georgia.gov/', 'valid': None},
                    {'active': True, 'canonical_url': 'https://gspc.georgia.gov/', 'collection': 15678,
                     'crawl_definition': 31104407627, 'created_by': 'scausey',
                     'created_date': '2021-05-05T18:32:28.134822Z', 'deleted': False, 'http_response_code': None,
                     'id': 2529681, 'last_checked_http_response_code': None, 'last_updated_by': 'scausey',
                     'last_updated_date': '2022-03-24T16:18:44.257754Z', 'login_password': None,
                     'login_username': None, 'metadata':
                         {'Creator': [{'value': 'Georgia State Properties Commission', 'id': 8453876}],
                          'Description': [{'value': 'As the steward of the State of Georgia’s Real Property '
                                                    'Assets, the Georgia State Properties Commission provides '
                                                    'accountability in the possession and arrangement of all '
                                                    'state-owned real property and real property interest with '
                                                    'the exception of the Board of Regents and the Department '
                                                    'of Transportation. The commission also helps agencies '
                                                    'within the State of Georgia find and secure leases.',
                                           'id': 8453873}],
                          'Title': [{'value': 'Georgia State Properties Commission', 'id': 8453877}],
                          'Date': [{'value': 'Captured 2022-', 'id': 8453874}],
                          'Identifier': [{'value': 'https://wayback.archive-it.org/15678/*/https://gspc.georgia.gov/',
                                          'id': 8453871}],
                          'Language': [{'value': 'English', 'id': 8453875}],
                          'Collector': [{'value': 'Map and Government Information Library', 'id': 8453878}],
                          'Rights': [{'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/',
                                      'id': 8453872}]},
                     'publicly_visible': True, 'seed_groups': [], 'seed_type': 'normal',
                     'url': 'https://gspc.georgia.gov/', 'valid': None},
                    {'active': True, 'canonical_url': 'https://galeo.org/', 'collection': 12263,
                     'crawl_definition': 31104243712, 'created_by': 'robert.lay',
                     'created_date': '2022-10-21T15:27:12.943504Z', 'deleted': False, 'http_response_code': None,
                     'id': 2912233, 'last_checked_http_response_code': None, 'last_updated_by': 'robert.lay',
                     'last_updated_date': '2022-12-08T21:13:49.463110Z', 'login_password': None,
                     'login_username': None, 'metadata':
                         {'Creator': [{'value': 'GALEO', 'id': 10390995}],
                          'Title': [{'value': 'GALEO – GALEO is a commitment towards greater civic engagement and '
                                              'leadership development of the Latino community across Georgia.',
                                     'id': 10390998}], 'Date': [{'value': '2022-', 'id': 10390999}],
                          'Identifier': [{'value': 'https://wayback.archive-it.org/12263/*/https://galeo.org/',
                                          'id': 10390997}],
                          'Language': [{'value': 'spa', 'id': 10391114}, {'value': 'eng', 'id': 10390994}],
                          'Relation': [{'value': 'RBRL/513: GALEO Records', 'id': 10391485}],
                          'Collector': [{'value': 'Richard B. Russell Library for Political Research and Studies',
                                         'id': 10390996}],
                          'Rights': [{'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/',
                                      'id': 10391000}]},
                     'publicly_visible': False, 'seed_groups': [], 'seed_type': 'normal', 'url': 'https://galeo.org/',
                     'valid': None}]

        self.assertEqual(actual, expected, "Problem with test: correct.")

    def test_api_error(self):
        """
        Tests the function would print the correct error message if there was an API error.
        Uses a portion of the code rather than the whole function because we don't know a way to force an API error.
        """
        status_code = 404
        error_message = "Error with Archive-It API connection when getting seed report", status_code
        to_print = ""
        if not status_code == 200:
            to_print = error_message

        self.assertEqual(to_print, error_message, "Problem with test: API error")


if __name__ == '__main__':
    unittest.main()

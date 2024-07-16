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

        # Gets the actual values for 4 seeds and saves to 4 variables for testing.
        # These used to use the list index number, but those changed over time.
        seed_2173766, seed_2529632, seed_2529681, seed_2912233 = (None, None, None, None)
        for seed in seed_metadata:
            if seed['id'] == 2173766:
                seed_2173766 = seed
            elif seed['id'] == 2529632:
                seed_2529632 = seed
            elif seed['id'] == 2529681:
                seed_2529681 = seed
            elif seed['id'] == 2912233:
                seed_2912233 = seed

        # Test that seed_2173766 (University of Georgia homepage) has the correct metadata.
        expected = {'active': True, 'canonical_url': 'https://www.uga.edu/', 'collection': 12912,
                    'crawl_definition': 31104266804, 'created_by': 'sarmour',
                    'created_date': '2020-03-26T19:33:20.013192Z', 'deleted': False, 'http_response_code': None,
                    'id': 2173766, 'last_checked_http_response_code': None, 'last_updated_by': 'ahanson',
                    'last_updated_date': '2024-05-01T13:30:32.175384Z', 'login_password': None,
                    'login_username': None, 'metadata':
                        {'Creator': [{'id': 5819711, 'value': 'University of Georgia'}],
                         'Language': [{'id': 5819712, 'value': 'English'}],
                         'Identifier': [{'id': 5898372,
                                         'value': 'https://wayback.archive-it.org/12912/*/https://www.uga.edu/'}],
                         'Collector': [{'id': 5819710, 'value': 'Hargrett Rare Book & Manuscript Library'}],
                         'Title': [{'id': 5819713, 'value': 'University of Georgia homepage'}],
                         'Rights': [{'id': 13218867,
                                     'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'}],
                         'Date': [{'id': 5819708, 'value': 'Captured 2020-'}]},
                    'publicly_visible': False, 'seed_groups': [], 'seed_type': 'normal', 'url': 'https://www.uga.edu/',
                    'valid': None}
        self.assertEqual(seed_2173766, expected, "Problem with test: correct, 2173766.")

        # Test that seed_2529632 (Georgia Commission on Family Violence) has the correct metadata.
        expected = {'active': True, 'canonical_url': 'https://gcfv.georgia.gov/', 'collection': 15678,
                    'crawl_definition': 31104407627, 'created_by': 'scausey',
                    'created_date': '2021-05-05T17:53:41.527988Z', 'deleted': False, 'http_response_code': None,
                    'id': 2529632, 'last_checked_http_response_code': None, 'last_updated_by': 'scausey',
                    'last_updated_date': '2022-03-24T16:18:48.856992Z', 'login_password': None,
                    'login_username': None, 'metadata':
                        {'Rights': [
                            {'id': 8453784, 'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'}],
                            'Title': [{'id': 8453789, 'value': 'Georgia Commission on Family Violence'}],
                            'Description': [{'id': 8453785,
                                             'value': 'Administratively attached to the Department of Community '
                                                      'Supervision (DCS), the Georgia Commission on Family '
                                                      'Violence ensures their belief that a coordinated community '
                                                      'response is the best way to address the problem of family '
                                                      'violence by working with communities and systems across '
                                                      'the state of Georgia to provide leadership in '
                                                      'strengthening Georgia’s families.'}],
                            'Date': [{'id': 8453786, 'value': 'Captured 2022-'}],
                            'Identifier': [{'id': 8453783,
                                            'value': 'https://wayback.archive-it.org/15678/*/https://gcfv.georgia.gov/'}],
                            'Language': [{'value': 'English', 'id': 8453787}],
                            'Collector': [{'id': 8453790, 'value': 'Map and Government Information Library'}],
                            'Creator': [{'id': 8453788, 'value': 'Georgia Commission on Family Violence'}]},
                    'publicly_visible': True, 'seed_groups': [], 'seed_type': 'normal',
                    'url': 'https://gcfv.georgia.gov/', 'valid': None}
        self.assertEqual(seed_2529632, expected, "Problem with test: correct, 2529632.")

        # Test that seed_2529681 (Georgia State Properties Commission) has the correct metadata.
        expected = {'active': True, 'canonical_url': 'https://gspc.georgia.gov/', 'collection': 15678,
                    'crawl_definition': 31104407627, 'created_by': 'scausey',
                    'created_date': '2021-05-05T18:32:28.134822Z', 'deleted': False, 'http_response_code': None,
                    'id': 2529681, 'last_checked_http_response_code': None, 'last_updated_by': 'scausey',
                    'last_updated_date': '2022-03-24T16:18:44.257754Z', 'login_password': None,
                    'login_username': None, 'metadata':
                        {'Collector': [{'id': 8453878, 'value': 'Map and Government Information Library'}],
                         'Description': [{'id': 8453873,
                                          'value': 'As the steward of the State of Georgia’s Real Property Assets, '
                                                   'the Georgia State Properties Commission provides accountability '
                                                   'in the possession and arrangement of all state-owned real '
                                                   'property and real property interest with the exception of the '
                                                   'Board of Regents and the Department of Transportation. The '
                                                   'commission also helps agencies within the State of Georgia find '
                                                   'and secure leases.'}],
                         'Creator': [{'id': 8453876, 'value': 'Georgia State Properties Commission'}],
                         'Rights': [{'id': 8453872,
                                     'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'}],
                         'Title': [{'id': 8453877, 'value': 'Georgia State Properties Commission'}],
                         'Language': [{'id': 8453875, 'value': 'English'}],
                         'Identifier': [{'id': 8453871,
                                         'value': 'https://wayback.archive-it.org/15678/*/https://gspc.georgia.gov/'}],
                         'Date': [{'id': 8453874, 'value': 'Captured 2022-'}]},
                    'publicly_visible': True, 'seed_groups': [], 'seed_type': 'normal',
                    'url': 'https://gspc.georgia.gov/', 'valid': None}
        self.assertEqual(seed_2529681, expected, "Problem with test: correct, 2529681.")

        # Test that seed_2912233 (GALEO) has the correct metadata.
        expected = {'active': True, 'canonical_url': 'https://galeo.org/', 'collection': 12263,
                    'crawl_definition': 31104243712, 'created_by': 'robert.lay',
                    'created_date': '2022-10-21T15:27:12.943504Z', 'deleted': False, 'http_response_code': None,
                    'id': 2912233, 'last_checked_http_response_code': None, 'last_updated_by': 'ahanson',
                    'last_updated_date': '2024-05-01T13:19:51.853803Z', 'login_password': None,
                    'login_username': None, 'metadata':
                        {'Date': [{'id': 13218832, 'value': 'Captured 2022-'}],
                         'Collector': [{'id': 10390996,
                                        'value': 'Richard B. Russell Library for Political Research and Studies'}],
                         'Identifier': [{'id': 10390997,
                                         'value': 'https://wayback.archive-it.org/12263/*/https://galeo.org/'}],
                         'Creator': [{'id': 10390995, 'value': 'GALEO'}],
                         'Rights': [{'id': 10391000,
                                     'value': 'In Copyright: http://rightsstatements.org/vocab/InC/1.0/'}],
                         'Title': [{'id': 10390998,
                                    'value': 'GALEO – GALEO is a commitment towards greater civic engagement and '
                                             'leadership development of the Latino community across Georgia.'}],
                         'Language': [{'id': 13218834, 'value': 'Spanish'}, {'id': 13218833, 'value': 'English'}],
                         'Relation': [{'id': 10391485, 'value': 'RBRL/513: GALEO Records'}]},
                    'publicly_visible': False, 'seed_groups': [], 'seed_type': 'normal', 'url': 'https://galeo.org/',
                    'valid': None}
        self.assertEqual(seed_2912233, expected, "Problem with test: correct, 2912233.")

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

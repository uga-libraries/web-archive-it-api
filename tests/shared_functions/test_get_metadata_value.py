"""
Tests for the get_metadata_value() shared function.
It returns a string with the value(s) for that metadata field or default text if the field is missing.
"""
import unittest
from shared_functions import get_metadata_value


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Data used for all of the tests.
        """
        self.test_data = {'account': 1234, 'created_by': 'user1', 'created_date': '2019-05-22T13:16:25.608171Z',
                          'deleted': False, 'id': 12345, 'image': None, 'last_updated_by': 'user2',
                          'last_updated_date': '2021-07-27T14:08:24.015979Z', 'metadata':
                              {'Collector': [{'value': 'Test Library', 'id': 5555555}],
                               'Date': [{'value': 'Captured 2019-', 'id': 5962116}],
                               'Language': [{'value': 'Spanish', 'id': 1111111}, {'value': 'English', 'id': 2222222}],
                               'Title': [{'value': 'Test Collection Title', 'id': 5962115}]},
                          'name': 'Test Collection Title', 'oai_exported': False,
                          'private_access_token': '111a222b333c444b5555aaaa6666bb77', 'publicly_visible': True,
                          'state': 'ACTIVE', 'topics': None}

    def test_0_fields(self):
        """
        Tests that the function returns the default text if the field is not in the data.
        """
        actual = get_metadata_value(self.test_data, "Description")
        expected = "NO DATA OF THIS TYPE"
        self.assertEqual(actual, expected, "Problem with test 0 fields of this type - Description.")

    def test_1_field(self):
        """
        Tests that the function returns the default text if the field is in the data once.
        """
        actual = get_metadata_value(self.test_data, "Title")
        expected = "Test Collection Title"
        self.assertEqual(actual, expected, "Problem with test 1 field of this type - Title.")

    def test_2_fields(self):
        """
        Tests that the function returns the default text if the field is in the data twice.
        """
        actual = get_metadata_value(self.test_data, "Language")
        expected = "Spanish;English"
        self.assertEqual(actual, expected, "Problem with test 2 fields of this type - Language.")


if __name__ == '__main__':
    unittest.main()

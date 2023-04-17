"""
Tests for the check_fields_to_include() shared function.
It returns True or False based on the optional script argument.
"""

import unittest
from shared_functions import check_fields_to_include


class MyTestCase(unittest.TestCase):

    def test_arg_is_other(self):
        """
        Tests that the function returns True when the provided argument is text other than "required".
        """
        actual = check_fields_to_include(['C:/path/seed_metadata_report.py', 'other_text'])
        self.assertEqual(actual, True, "Problem with test: argument is other text.")

    def test_arg_is_required(self):
        """
        Tests that the function returns False when the provided argument is "required".
        """
        actual = check_fields_to_include(['C:/path/seed_metadata_report.py', 'required'])
        self.assertEqual(actual, False, "Problem with test: argument is required.")

    def test_no_arg(self):
        """
        Tests that the function returns True when there is no provided argument.
        """
        actual = check_fields_to_include(['C:/path/seed_metadata_report.py'])
        self.assertEqual(actual, True, "Problem with test: no argument.")


if __name__ == '__main__':
    unittest.main()

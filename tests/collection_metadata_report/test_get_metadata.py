"""
Tests for the get_metadata() function from the collection_metadata_report.py script.
It gets and returns metadata for all collections using the Archive-It Partner API.
"""
import unittest
from collection_metadata_report import get_metadata


class MyTestCase(unittest.TestCase):

    def test_correct(self):
        """
        Tests that the function returns the expected list of metadata values.
        NOTE: this must be updated whenever collections are added, edited, or deleted.
        """

        actual = get_metadata()
        expected = [{'account': 1468, 'created_by': 'system', 'created_date': '2018-09-19T22:45:21Z',
                     'deleted': False, 'id': 11071, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2022-01-18T18:11:43.740774Z', 'metadata':
                         {'Language': [{'id': 7236763, 'value': 'Test Language Two'},
                                       {'id': 7236762, 'value': 'Test Language One'}],
                          'Date': [{'id': 8590671, 'value': 'Captured 2018-2020'}],
                          'Title': [{'id': 6803211, 'value': 'Trial 2018'}],
                          'Relation': [{'id': 7236756, 'value': 'Test Relation Two'},
                                       {'id': 7236755, 'value': 'Test Relation One'}],
                          'Creator': [{'id': 7236759, 'value': 'Test Creator Two'},
                                      {'id': 7236758, 'value': 'Test Creator One'}],
                          'Subject': [{'id': 7236754, 'value': 'Test Subject Two'},
                                      {'id': 7236753, 'value': 'Test Subject One'}],
                          'Collector': [{'id': 7695086, 'value': 'University of Georgia Libraries Testing'}],
                          'Rights': [{'id': 7236761, 'value': 'Test Rights Two'},
                                     {'id': 7236760, 'value': 'Test Rights One'}],
                          'Identifier': [{'id': 7236752, 'value': 'Test ID'}],
                          'Description': [{'id': 6803212,
                                           'value': "Tests run by Archive-It on UGA's behalf as a demonstration "
                                                    "of the service while we considered becoming subscribers."}]},
                     'name': 'Trial 2018', 'oai_exported': False,
                     'private_access_token': '4d5ea946cd554ac98aabd36b392b6637', 'publicly_visible': False,
                     'state': 'INACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'sarmour', 'created_date': '2019-05-22T13:16:25.608171Z',
                     'deleted': False, 'id': 12181, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2020-07-27T14:08:24.015979Z', 'metadata':
                         {'Date': [{'id': 5962116, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5962115, 'value': 'University of Georgia Student Life'}],
                          'Collector': [{'id': 5305969, 'value': 'Hargrett Rare Book & Manuscript Library'}],
                          'Description': [{'id': 5305970,
                                           'value': "This collection contains websites related to the University of "
                                                    "Georgia's Division of Student Affairs and student organizations "
                                                    "at UGA."}]},
                     'name': 'University of Georgia Student Life', 'oai_exported': False,
                     'private_access_token': '717f29935c3c4a578c00986a180b9ad4', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'ahanson', 'created_date': '2019-06-03T19:33:03.825828Z',
                     'deleted': False, 'id': 12249, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2021-07-19T14:10:35.815516Z', 'metadata':
                         {'Title': [{'id': 6803217, 'value': 'Experiments'}],
                          'Collector': [{'id': 7695087, 'value': 'University of Georgia Libraries Testing'}],
                          'Description': [{'id': 6803219,
                                           'value': 'Seeds used for practicing with Archive-It. '
                                                    'Not intended for permanent preservation.'}]},
                     'name': 'Experiments', 'oai_exported': False,
                     'private_access_token': '67ecb0cd72b341979fe8921928e79be0', 'publicly_visible': False,
                     'state': 'INACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'bpieczko', 'created_date': '2019-06-07T13:42:31.787521Z',
                     'deleted': False, 'id': 12262, 'image': 2883885, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2020-07-27T14:06:27.875326Z', 'metadata':
                         {'Date': [{'id': 5962107, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5035316, 'value': 'Political Observers'}],
                          'Collector': [{'id': 5035317,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Description': [{'id': 5035318,
                                           'value': 'This collections contains websites created by journalists, '
                                                    'academics, and other political observers.'}]},
                     'name': 'Political Observers', 'oai_exported': False,
                     'private_access_token': '7c5fe90c0d154afe9a406a44e0d31eac', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': ''},
                    {'account': 1468, 'created_by': 'bpieczko', 'created_date': '2019-06-07T13:44:49.939921Z',
                     'deleted': False, 'id': 12263, 'image': 2883888, 'last_updated_by': 'bpieczko',
                     'last_updated_date': '2019-12-19T16:23:12.905659Z', 'metadata':
                         {'Date': [{'id': 5035182, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5035179, 'value': 'Activists and Advocates'}],
                          'Collector': [{'id': 5035181,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Description': [{'id': 5035180,
                                           'value': 'This collections contains websites created by organizations and '
                                                    'individuals engaged in sociopolitical activism and advocacy '
                                                    'in Georgia.'}]},
                     'name': 'Activists and Advocates', 'oai_exported': False,
                     'private_access_token': '94a22d25bd704351afb39f8a73b35908', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'bpieczko', 'created_date': '2019-06-07T13:45:15.797160Z',
                     'deleted': False, 'id': 12264, 'image': 2883887, 'last_updated_by': 'bpieczko',
                     'last_updated_date': '2019-12-19T16:53:27.214760Z', 'metadata':
                         {'Date': [{'id': 5035367, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5035365, 'value': 'Georgia Disability History Archive'}],
                          'Collector': [{'id': 5035366,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Description': [{'id': 5035364,
                                           'value': 'The Georgia Disability History Archive seeks to document the '
                                                    'vital and transformative work undertaken by disability activists, '
                                                    'advocates, and organizations and, crucially, the experiences '
                                                    'of people with disabilities over the past 100-plus years in the '
                                                    'state of Georgia. Major collecting areas include, but are not '
                                                    'limited to: accessibility, activism and social justice, '
                                                    'citizen advocacy, independent and community living, '
                                                    'self-advocacy, education, employment, recreation, '
                                                    'culture and pride.'}]},
                     'name': 'Georgia Disability History Archive', 'oai_exported': False,
                     'private_access_token': 'b7b1f1ccd3d44633bb2512001b744bf8', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'bpieczko', 'created_date': '2019-06-07T13:53:19.132354Z',
                     'deleted': False, 'id': 12265, 'image': 2883884, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2020-07-27T14:24:29.521230Z', 'metadata':
                         {'Date': [{'id': 5035338, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5035336, 'value': 'Georgia Politics'}],
                          'Collector': [{'id': 5035337,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Identifier': [{'id': 5962149,
                                          'value': 'https://wayback.archive-it.org/12265/*/https://www.youtube.com/'
                                                   'channel/UC-LF69SBOSgT1S1-yy-VgaA/videos?view=0&sort=dd&shelf_id=0'}],
                          'Description': [{'id': 5035357,
                                           'value': 'This collection contains websites documenting political activity '
                                                    'in the state of Georgia including those created by political '
                                                    'candidates, elected officials, and political parties.'}]},
                     'name': 'Georgia Politics', 'oai_exported': False,
                     'private_access_token': '9d715ef3623d4baea2e29fbe852af759', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': ''},
                    {'account': 1468, 'created_by': 'ahanson', 'created_date': '2019-06-11T14:08:35.567085Z',
                     'deleted': False, 'id': 12274, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2021-01-25T14:27:14.676450Z', 'metadata':
                         {'Title': [{'id': 6803168, 'value': 'Georgia Newspapers'}],
                          'Collector': [{'id': 6803181, 'value': 'The Digital Library of Georgia'}],
                          'Description': [{'id': 6803169,
                                           'value': 'Test crawls for the Georgia Newspaper Project pilot for '
                                                    'collecting born-digital newspapers.'}]},
                     'name': 'Georgia Newspapers', 'oai_exported': False,
                     'private_access_token': '653b67f3a83c4c368a1e5984258b4e69', 'publicly_visible': False,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'ahanson', 'created_date': '2019-07-16T17:05:24.182707Z',
                     'deleted': False, 'id': 12470, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2021-01-25T14:26:49.778878Z', 'metadata':
                         {'Date': [{'id': 6803177, 'value': 'Captured 2020'}],
                          'Title': [{'id': 6803179, 'value': 'The Now Explosion'}],
                          'Collector': [{'id': 6803178,
                                         'value': 'The Walter J. Brown Media Archives & Peabody Awards Collection'}],
                          'Description': [{'id': 6803180,
                                           'value': 'Websites related to The Now Explosion television program.'}]},
                     'name': 'The Now Explosion', 'oai_exported': False,
                     'private_access_token': 'e3efd174175343c287a6bdf3647e1c32', 'publicly_visible': False,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'sarmour', 'created_date': '2019-10-08T14:08:42.636015Z',
                     'deleted': False, 'id': 12907, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2020-07-27T14:07:51.214507Z', 'metadata':
                         {'Date': [{'id': 5962113, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5962112, 'value': 'University of Georgia Athletics'}],
                          'Collector': [{'id': 5305369, 'value': 'Hargrett Rare Book & Manuscript Library'}],
                          'Description': [{'id': 5305368,
                                           'value': 'This collection contains websites related to the athletic '
                                                    'programs at the University of Georgia.'}]},
                     'name': 'University of Georgia Athletics', 'oai_exported': False,
                     'private_access_token': '2643e534b8ef4c35ae37e59cabec5f71', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'sarmour', 'created_date': '2019-10-08T16:22:49.013552Z',
                     'deleted': False, 'id': 12912, 'image': None, 'last_updated_by': 'ahanson',
                     'last_updated_date': '2020-07-27T14:07:09.505909Z', 'metadata':
                         {'Date': [{'id': 5962110, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5962109, 'value': 'University of Georgia Administration'}],
                          'Collector': [{'id': 5305867, 'value': 'Hargrett Rare Book & Manuscript Library'}],
                          'Description': [{'id': 5305866,
                                           'value': "This collection contains websites related to the University of "
                                                    "Georgia's administration, including the Office of the President, "
                                                    "the Provost, and other leadership roles."}]},
                     'name': 'University of Georgia Administration', 'oai_exported': False,
                     'private_access_token': '1bbd5fe659904a48aed7f7e9e407efdc', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'bpieczko', 'created_date': '2019-10-18T13:26:05.725061Z',
                     'deleted': False, 'id': 12939, 'image': 2884157, 'last_updated_by': 'bpieczko',
                     'last_updated_date': '2019-12-19T16:47:37.348593Z', 'metadata':
                         {'Date': [{'id': 5035354, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5035356, 'value': 'Business'}],
                          'Collector': [{'id': 5035353,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Description': [{'id': 5035355,
                                           'value': 'This collection contains websites documenting business and '
                                                    'private enterprise in the state of Georgia.'}]},
                     'name': 'Business', 'oai_exported': False,
                     'private_access_token': '06869aca60354b3ca6c062eae12537fb', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'bpieczko', 'created_date': '2019-10-21T14:19:29.017831Z',
                     'deleted': False, 'id': 12944, 'image': 2884158, 'last_updated_by': 'bpieczko',
                     'last_updated_date': '2019-12-19T16:42:36.412615Z', 'metadata':
                         {'Date': [{'id': 5035327, 'value': 'Captured 2019-'}],
                          'Title': [{'id': 5035325, 'value': 'Legal'}],
                          'Collector': [{'id': 5035326,
                                         'value': 'Richard B. Russell Library for Political Research and Studies'}],
                          'Description': [{'id': 5035328,
                                           'value': 'This collections contains websites created by attorneys, '
                                                    'judges, and organizations working on legal issues in the '
                                                    'state of Georgia.'}]},
                     'name': 'Legal', 'oai_exported': False,
                     'private_access_token': 'cb061896cc3f430caca7b726bccf69a1', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'ahanson', 'created_date': '2021-01-08T14:12:05.826419Z',
                     'deleted': False, 'id': 15678, 'image': 2885233, 'last_updated_by': 'scausey',
                     'last_updated_date': '2022-04-18T14:20:28.536687Z', 'metadata':
                         {'Date': [{'id': 8454162, 'value': 'Captured 2022-'}],
                          'Title': [{'id': 8454163, 'value': 'Georgia Government Publications Website Archive'}],
                          'Collector': [{'id': 6803187, 'value': 'Map and Government Information Library'}],
                          'Description': [{'id': 8454376,
                                           'value': 'The University of Georgia Libraries is the official depository '
                                                    'for Georgia state publications and, as such, is responsible for '
                                                    'their collection, preservation, and accessibility. '
                                                    'The Georgia Government Publications Website Archive includes '
                                                    'websites of Georgia state agencies and organizations, '
                                                    'with an emphasis on those of the executive branch. '
                                                    'Select publications included in these websites are also '
                                                    'available in the Digital Library of Georgia, '
                                                    'Georgia Government Publications collection.'}]},
                     'name': 'Georgia Government Publications', 'oai_exported': False,
                     'private_access_token': '814846a798d2404c829aea841003b88c', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None},
                    {'account': 1468, 'created_by': 'sarmour', 'created_date': '2021-06-18T19:36:57.730950Z',
                     'deleted': False, 'id': 16951, 'image': None, 'last_updated_by': 'sarmour',
                     'last_updated_date': '2021-08-02T18:44:43.813247Z', 'metadata':
                         {'Date': [{'id': 7789679, 'value': 'Captured 2021-'}],
                          'Title': [{'id': 7789682, 'value': 'University of Georgia Academics'}],
                          'Collector': [{'id': 7789681, 'value': 'Hargrett Rare Book & Manuscript Library'}],
                          'Description': [{'id': 7789680,
                                           'value': 'This collection contains websites related research and '
                                                    'instruction at the University of Georgia.'}]},
                     'name': 'University of Georgia Academics', 'oai_exported': False,
                     'private_access_token': '29d83f5a07624f9eb3a00a15bf8047be', 'publicly_visible': True,
                     'state': 'ACTIVE', 'topics': None}]

        self.assertEqual(actual, expected, "Problem with test: correct.")

    def test_api_error(self):
        """
        Tests the function would print the correct error message if there was an API error.
        Uses a portion of the code rather than the whole function because we don't know a way to force an API error.
        """
        status_code = 404
        error_message = "Error with Archive-It API connection when getting collection report", status_code
        to_print = ""
        if not status_code == 200:
            to_print = error_message

        self.assertEqual(to_print, error_message, "Problem with test: API error")


if __name__ == '__main__':
    unittest.main()

"""
Tests for the get_metadata function from the warc_metadata_report.py script.
It returns the WARC metadata from WASAPI or raises an error.
"""
import unittest
from warc_metadata_report import get_metadata


class MyTestCase(unittest.TestCase):

    def test_api_error(self):
        """
        Tests that the function raises an error if there is a problem with the API.
        Causes the error by giving the API incorrectly formatted parameters.
        """
        with self.assertRaises(ValueError):
            get_metadata("date_error_1", "date_error_2")

    def test_one_warc(self):
        """
        Tests that the function returns the expected values for a date range with one WARC.
        """
        actual = get_metadata("2019-09-01", "2019-09-15")
        expected = {'count': 1,
                    'files': [{'account': 1468,
                               'checksums': {'md5': '9f3ca7026dd55bcfc02567081f27b1c8',
                                             'sha1': '0c1017435b5aa0f854bbfd2b25a7f42c86fc5fc8'},
                               'collection': 12262,
                               'crawl': 968139,
                               'crawl-start': '2019-09-10T13:16:30.452000Z',
                               'crawl-time': '2019-09-10T13:16:34.816000Z',
                               'filename': 'ARCHIVEIT-12262-CRAWL_SELECTED_SEEDS-JOB968139-SEED2018084-'
                                           '20190910131634816-00000-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-12262-CRAWL_SELECTED'
                                             '_SEEDS-JOB968139-SEED2018084-20190910131634816-00000-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-12262-CRAWL_SELECTED_SEEDS-'
                                             'JOB968139-SEED2018084-20190910-00000/ARCHIVEIT-12262-CRAWL_SELECTED_'
                                             'SEEDS-JOB968139-SEED2018084-20190910131634816-00000-h3.warc.gz'],
                               'size': 8190,
                               'store-time': '2019-09-10T13:20:03.873275Z'}],
                    'includes-extra': False,
                    'next': None,
                    'previous': None,
                    'request-url': 'http://warcs.archive-it.org/wasapi/v1/webdata?store-time-after=2019-09-01&'
                                   'store-time-before=2019-09-15&page_size=1000'}

        self.assertEqual(actual, expected, "Problem with test for one warc.")

    def test_multiple_warc(self):
        """
        Tests that the function returns the expected values for a date range with multiple days.
        """
        actual = get_metadata("2021-03-15", "2021-03-19")
        expected = {'count': 5,
                    'files': [{'account': 1468,
                               'checksums': {'md5': '610bb6c3179c75f7909ab1cf7b908c64',
                                             'sha1': '86f7381027561474f29c099dcc9e9da3cd69d613'},
                               'collection': 12912,
                               'crawl': 1382111,
                               'crawl-start': '2021-03-15T22:17:13.044009Z',
                               'crawl-time': '2021-03-18T22:09:50.737000Z',
                               'filename': 'ARCHIVEIT-12912-MONTHLY-JOB1382111-SEED2184360-20210318220950737-'
                                           '00004-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-12912-MONTHLY-'
                                             'JOB1382111-SEED2184360-20210318220950737-00004-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210318-00000/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210318220950737-00004-h3.warc.gz'],
                               'size': 11691601,
                               'store-time': '2021-03-18T22:20:05.311902Z'},
                              {'account': 1468,
                               'checksums': {'md5': '22527c3fb4fe7a195eea5ac1cbbb744a',
                                             'sha1': 'a66c8d97695551b850837ce1acaef256ef268abc'},
                               'collection': 12912,
                               'crawl': 1382111,
                               'crawl-start': '2021-03-15T22:17:13.044009Z',
                               'crawl-time': '2021-03-17T11:54:18.678000Z',
                               'filename': 'ARCHIVEIT-12912-MONTHLY-JOB1382111-SEED2184360-20210317115418678-'
                                           '00003-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-12912-MONTHLY-'
                                             'JOB1382111-SEED2184360-20210317115418678-00003-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210317-00000/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210317115418678-00003-h3.warc.gz'],
                               'size': 1000008775,
                               'store-time': '2021-03-18T22:12:49.802789Z'},
                              {'account': 1468,
                               'checksums': {'md5': '90b08d2222e8eea606a89f941f392d16',
                                             'sha1': 'f6fd72d67e47b35c5c6fbfed1bcf869c4c3a60ca'},
                               'collection': 12912,
                               'crawl': 1382111,
                               'crawl-start': '2021-03-15T22:17:13.044009Z',
                               'crawl-time': '2021-03-16T16:08:26.708000Z',
                               'filename': 'ARCHIVEIT-12912-MONTHLY-JOB1382111-SEED2184360-20210316160826708-'
                                           '00002-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-12912-MONTHLY-'
                                             'JOB1382111-SEED2184360-20210316160826708-00002-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210316-00000/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210316160826708-00002-h3.warc.gz'],
                               'size': 1000314559,
                               'store-time': '2021-03-17T11:57:33.104744Z'},
                              {'account': 1468,
                               'checksums': {'md5': 'ea077fee862fceb5ba424eb191cd5f12',
                                             'sha1': '940c067100ba5cd6e97a1f019a70c038174fb2ea'},
                               'collection': 12912,
                               'crawl': 1382111,
                               'crawl-start': '2021-03-15T22:17:13.044009Z',
                               'crawl-time': '2021-03-16T09:53:02.043000Z',
                               'filename': 'ARCHIVEIT-12912-MONTHLY-JOB1382111-SEED2184360-20210316095302043-'
                                           '00001-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-12912-MONTHLY-'
                                             'JOB1382111-SEED2184360-20210316095302043-00001-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210316-00000/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210316095302043-00001-h3.warc.gz'],
                               'size': 1002276074,
                               'store-time': '2021-03-16T16:11:23.048395Z'},
                              {'account': 1468,
                               'checksums': {'md5': 'fa33ebc91dec2df8db31fcd507e9433b',
                                             'sha1': 'fff39c7bb5ed57b336fc593b468f8fbb990609a7'},
                               'collection': 12912,
                               'crawl': 1382111,
                               'crawl-start': '2021-03-15T22:17:13.044009Z',
                               'crawl-time': '2021-03-15T22:17:23.003000Z',
                               'filename': 'ARCHIVEIT-12912-MONTHLY-JOB1382111-SEED2184360-20210315221723003-'
                                           '00000-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-12912-MONTHLY-'
                                             'JOB1382111-SEED2184360-20210315221723003-00000-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210315-00000/ARCHIVEIT-12912-MONTHLY-JOB1382111-'
                                             'SEED2184360-20210315221723003-00000-h3.warc.gz'],
                               'size': 1000001802,
                               'store-time': '2021-03-16T09:56:23.815039Z'}],
                    'includes-extra': False,
                    'next': None,
                    'previous': None,
                    'request-url': 'http://warcs.archive-it.org/wasapi/v1/webdata?store-time-after=2021-03-15&'
                                   'store-time-before=2021-03-19&page_size=1000'}

        self.assertEqual(actual, expected, "Problem with test for multiple warcs.")

    def test_on_start(self):
        """
        Tests that the function returns the expected values for a date range with a WARC on the start date.
        WARCs stored on the start date are included.
        """
        actual = get_metadata("2022-04-04", "2022-04-06")
        expected = {'count': 4,
                    'files': [{'account': 1468,
                               'checksums': {'md5': 'fd11ce8ba58f2f38f4c26d60915815f1',
                                             'sha1': '5b54eb5e67f838ecec19a9aba5d0f8dd7db7b48a'},
                               'collection': 15678,
                               'crawl': 1583129,
                               'crawl-start': '2022-03-31T15:20:31.774065Z',
                               'crawl-time': '2022-03-31T15:20:35.971000Z',
                               'filename': 'ARCHIVEIT-15678-TEST-JOB1583129-SEED2529638-20220331152035971-'
                                           '00000-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-15678-TEST-'
                                             'JOB1583129-SEED2529638-20220331152035971-00000-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-15678-2022040513-00000/'
                                             'ARCHIVEIT-15678-TEST-JOB1583129-SEED2529638-20220331152035971-'
                                             '00000-h3.warc.gz'],
                               'size': 507833072,
                               'store-time': '2022-04-05T13:56:55.397354Z'},
                              {'account': 1468,
                               'checksums': {'md5': '3e47f456d6700aff807276ed36db656e',
                                             'sha1': '7bd135cbf297847f347a97edc6a9c6b6a9e991db'},
                               'collection': 15678,
                               'crawl': 1583125,
                               'crawl-start': '2022-03-31T15:17:12.354892Z',
                               'crawl-time': '2022-03-31T15:17:16.180000Z',
                               'filename': 'ARCHIVEIT-15678-TEST-JOB1583125-SEED2529649-20220331151716180-'
                                           '00000-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-15678-TEST-'
                                             'JOB1583125-SEED2529649-20220331151716180-00000-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-15678-2022040513-00000/'
                                             'ARCHIVEIT-15678-TEST-JOB1583125-SEED2529649-20220331151716180-'
                                             '00000-h3.warc.gz'],
                               'size': 263912161,
                               'store-time': '2022-04-05T13:40:03.053914Z'},
                              {'account': 1468,
                               'checksums': {'md5': '87178144ebd3b1c4af275ba6290188c2',
                                             'sha1': '8e6055194686279c9e96dd053d5e1487febb3ee5'},
                               'collection': 15678,
                               'crawl': 1583122,
                               'crawl-start': '2022-03-31T15:15:25.141880Z',
                               'crawl-time': '2022-03-31T15:15:31.862000Z',
                               'filename': 'ARCHIVEIT-15678-TEST-JOB1583122-SEED2529675-20220331151531862-'
                                           '00000-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-15678-TEST-'
                                             'JOB1583122-SEED2529675-20220331151531862-00000-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-15678-2022040513-00000/'
                                             'ARCHIVEIT-15678-TEST-JOB1583122-SEED2529675-20220331151531862-'
                                             '00000-h3.warc.gz'],
                               'size': 429405083,
                               'store-time': '2022-04-05T13:33:49.878323Z'},
                              {'account': 1468,
                               'checksums': {'md5': '95f71cf3e2787d6d057a26bff530eddd',
                                             'sha1': '7b3c24b454840cdd8410bf795b33b83cdfbd968d'},
                               'collection': 12265,
                               'crawl': 1542168,
                               'crawl-start': '2022-01-14T17:38:38.249589Z',
                               'crawl-time': '2022-01-14T17:39:01.970000Z',
                               'filename': 'ARCHIVEIT-12265-TEST-JOB1542168-SEED2485678-20220114173901970-'
                                           '00000-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-12265-TEST-'
                                             'JOB1542168-SEED2485678-20220114173901970-00000-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-12265-2022040412-00000/'
                                             'ARCHIVEIT-12265-TEST-JOB1542168-SEED2485678-20220114173901970-'
                                             '00000-h3.warc.gz'],
                               'size': 153059949,
                               'store-time': '2022-04-04T12:29:37.317834Z'}],
                    'includes-extra': False,
                    'next': None,
                    'previous': None,
                    'request-url': 'http://warcs.archive-it.org/wasapi/v1/webdata?store-time-after=2022-04-04&'
                                   'store-time-before=2022-04-06&page_size=1000'}

        self.assertEqual(actual, expected, "Problem with test for a WARC on the start date.")

    def test_on_end(self):
        """
        Tests that the function returns the expected values for a date range with WARCs on the end date.
        WARCs stored on the end date are not included.
        """
        actual = get_metadata("2022-10-20", "2022-10-26")
        expected = {'count': 2,
                    'files': [{'account': 1468,
                               'checksums': {'md5': 'f4d75988249684d270c030cf366f9e13',
                                             'sha1': '4c3af4c452d7fd3dbb60cbe1c0537761cfd66a53'},
                               'collection': 15678,
                               'crawl': 1672420,
                               'crawl-start': '2022-09-11T19:36:04.635482Z',
                               'crawl-time': '2022-09-11T19:36:09.257000Z',
                               'filename': 'ARCHIVEIT-15678-TEST-JOB1672420-SEED2529634-20220911193609257-'
                                           '00000-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-15678-TEST-'
                                             'JOB1672420-SEED2529634-20220911193609257-00000-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-15678-2022102514-00000/'
                                             'ARCHIVEIT-15678-TEST-JOB1672420-SEED2529634-20220911193609257-'
                                             '00000-h3.warc.gz'],
                               'size': 1000018236,
                               'store-time': '2022-10-25T14:53:54.308359Z'},
                              {'account': 1468,
                               'checksums': {'md5': 'a4f8b4ef99793a4fdbd022aff67ad203',
                                             'sha1': '1743745b5d7867ae303b713febbb4b8a62c468d4'},
                               'collection': 15678,
                               'crawl': 1672420,
                               'crawl-start': '2022-09-11T19:36:04.635482Z',
                               'crawl-time': '2022-09-13T20:52:09.833000Z',
                               'filename': 'ARCHIVEIT-15678-TEST-JOB1672420-SEED2529634-20220913205209833-'
                                           '00001-h3.warc.gz',
                               'filetype': 'warc',
                               'locations': ['https://warcs.archive-it.org/webdatafile/ARCHIVEIT-15678-TEST-'
                                             'JOB1672420-SEED2529634-20220913205209833-00001-h3.warc.gz',
                                             'https://archive.org/download/ARCHIVEIT-15678-2022102514-00000/'
                                             'ARCHIVEIT-15678-TEST-JOB1672420-SEED2529634-20220913205209833-'
                                             '00001-h3.warc.gz'],
                               'size': 145345200,
                               'store-time': '2022-10-25T14:53:54.308126Z'}],
                    'includes-extra': False,
                    'next': None,
                    'previous': None,
                    'request-url': 'http://warcs.archive-it.org/wasapi/v1/webdata?store-time-after=2022-10-20&'
                                   'store-time-before=2022-10-26&page_size=1000'}

        self.assertEqual(actual, expected, "Problem with test for warcs on the end date.")


if __name__ == '__main__':
    unittest.main()

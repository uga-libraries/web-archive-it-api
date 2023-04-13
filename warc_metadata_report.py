"""
Purpose: Generate a report of WARC metadata from Archive-It.
The report is saved to the script_output folder, which is defined in configuration.py

The report includes the following fields:
    * WARC Filename
    * AIT Collection ID
    * Seed ID
    * Crawl Job ID
    * Date (store-time)
    * Size (GB)
    * Crawl Definition ID
    * Seed Title
    * WARC MD5

Use this script instead of the WASAPI CSV download option in the web browser
so data can be manipulated, added from the Partner API, and reformatted.

UGA uses this script to generate a list of all WARCs expected in the quarterly preservation download
and adds them to a WARC Inventory for all downloaded WARCs to track that nothing is missed.

Script usage: python warc_metadata_report.py earliest_date
WARCs stored on the earliest_date will be included in the report.
"""

import csv
import os
import re
import requests
import sys

try:
    import configuration as c
except ModuleNotFoundError:
    print("File configuration.py is missing from the script folder.")
    print("Use configuration_template.py to create this file.")
    sys.exit()
import shared_functions as fun


def check_argument(argument_list):
    """
    Verifies the required argument is present and is formatted like a date.
    Returns the date or if there is an error, quits the script.
    """
    try:
        date = argument_list[1]
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            print('Date argument must be formatted YYYY-MM-DD. Please try the script again.')
            sys.exit()
    except IndexError:
        print("Missing required date argument for limiting the WARCs to include.")
        sys.exit()

    return date


def get_metadata(start):
    """Uses WASAPI to get metadata for all WARCs stored during the specified date range.
    Returns the metadata as a python object.
    If there is an API error, quits the script."""

    filters = {'store-time-after': start, 'page_size': 1000}
    warc_data = requests.get(c.wasapi, params=filters, auth=(c.username, c.password))
    if not warc_data.status_code == 200:
        print("WASAPI error, ending script. See log for details.")
        sys.exit()
    py_warc_data = warc_data.json()
    return py_warc_data


def get_seed_id(warc_name):
    """
    Uses a regular expression to identify the Seed Id component of the WARC filename and returns the Seed ID.
    """
    try:
        regex = re.match(r'^.*?SEED(\d+)-', warc_name)
        seed_id = regex.group(1)
    except AttributeError:
        seed_id = "COULD NOT CALCULATE"
    return seed_id


def get_size(bytes):
    """
    Converts the size from bytes (value from API) to GB.
    As long as it won't result in 0, round to 2 decimal places.
    Returns the size in GB.
    """
    size = float(bytes) / 1000000000
    if size > 0.01:
        size = round(size, 2)
    return size


def get_title(seed):
    """Uses the Partner API to get the seed report for this seed, which includes the seed title.
    Returns the title or an error message to put in the CSV in place of the title."""

    # Gets the seed report using the Partner API.
    seed_report = requests.get(f'{c.partner_api}/seed?id={seed}', auth=(c.username, c.password))
    if not seed_report.status_code == 200:
        return "API Error for seed report"

    # Reads the seed report and extracts the title.
    py_seed_report = seed_report.json()
    try:
        seed_title = py_seed_report[0]["metadata"]["Title"][0]["value"]
        return seed_title
    except (KeyError, IndexError):
        return "No title in Archive-It"


def get_crawl_def(job):
    """Uses the Partner API to get the report for this job, which includes the crawl definition.
    Returns the crawl definition id or an error message to put in the CSV in its place."""

    # Gets the crawl job report using the Partner API.
    job_report = requests.get(f'{c.partner_api}/crawl_job?id={job}', auth=(c.username, c.password))
    if not job_report.status_code == 200:
        return "API Error for job report"

    # Reads the crawl job report and extracts the crawl definition identifier.
    py_job_report = job_report.json()
    try:
        crawl_definition = py_job_report[0]["crawl_definition"]
        return crawl_definition
    except (KeyError, IndexError):
        return "Cannot get crawl definition: Job ID is not in Archive-It"


if __name__ == '__main__':
    # Verifies the configuration file has the correct values.
    fun.check_config()

    # Gets the earliest date for WARCs to include in the CSV from the script argument.
    earliest_date = check_argument(sys.argv)

    # Gets the WARC data from WASAPI and converts to Python.
    metadata = get_metadata(earliest_date)

    # Makes a CSV for the warc metadata report with a header row.
    report_path = f"{c.script_output}/warc_metadata_report.csv"
    fun.save_csv_row(report_path, ["WARC Filename", "AIT Collection", "Seed", "Job", "Date (store-time)",
                                   "Size (GB)", "Crawl Def", "AIP Title", "MD5"])

    # Saves the metadata for each warc to the warc metadata report.
    for warc in metadata['files']:
        seed_id = get_seed_id(warc['filename'])
        warc_row = [warc['filename'], warc['collection'], seed_id, warc['crawl'], warc['store-time'],
                    get_size(warc['size']), get_crawl_def(warc['crawl']), get_title(seed_id), warc['checksums']['md5']]
        fun.save_csv_row(report_path, warc_row)

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

Script usage: python warc_metadata_report.py start_date end_date
WARCs stored on the start_date will be included in the report.
WARCs stored on the end_date will NOT be included in the report.
"""

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


def check_arguments(argument_list):
    """
    Verifies the two required arguments (start and end date) are present and correct.
    Returns the dates and errors list, which is empty if there were no errors.
    """
    start = None
    end = None
    errors = []

    # Checks if the first argument (start date) is present and formatted YYYY-MM-DD.
    try:
        if re.match(r"\d{4}-\d{2}-\d{2}", argument_list[1]):
            start = argument_list[1]
        else:
            errors.append(f"First argument '{argument_list[1]}' is not formatted YYYY-MM-DD.")
    except IndexError:
        errors.append("First argument (start date) is missing.")

    # Checks if the second argument (end date) is present and formatted YYYY-MM-DD.
    try:
        if re.match(r"\d{4}-\d{2}-\d{2}", argument_list[2]):
            end = argument_list[2]
        else:
            errors.append(f"Second argument '{argument_list[2]}' is not formatted YYYY-MM-DD.")
    except IndexError:
        errors.append("Second argument (end date) is missing.")

    # If start and end dates were correctly formatted, and so assigned to the variables,
    # checks if the start date is later than or the same as the end date, which is an error.
    if start and end and start >= end:
        errors.append("The first argument must be an earlier date than the second.")

    return start, end, errors


def get_metadata(start, end):
    """Uses WASAPI to get metadata for all WARCs stored during the specified date range.
    WARCs saved on the start date will be included. WARCs saved on the end date will not be included.
    Returns the metadata as a python object or raises an error."""

    filters = {'store-time-after': start, 'store-time-before': end, 'page_size': 1000}
    warc_data = requests.get(c.wasapi, params=filters, auth=(c.username, c.password))
    if not warc_data.status_code == 200:
        raise ValueError
    py_warc_data = warc_data.json()
    return py_warc_data


def get_seed_id(warc_name):
    """
    Uses a regular expression to identify the Seed Id component of the WARC filename.
    Returns the Seed ID.
    """
    try:
        regex = re.match(r'^.*?SEED(\d+)-', warc_name)
        id = regex.group(1)
    except AttributeError:
        id = "COULD NOT CALCULATE"
    return id


def get_size(size_bytes):
    """
    Converts the size from bytes (value from API) to GB.
    As long as it won't result in 0, round to 2 decimal places.
    Returns the size in GB.
    """
    size = float(size_bytes) / 1000000000
    if size > 0.01:
        size = round(size, 2)
    return size


def get_title(seed):
    """
    Uses the Partner API to get the seed report for this seed, which includes the seed title.
    Returns the title or an error message to put in the CSV in place of the title.
    """

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
    """
    Uses the Partner API to get the report for this job, which includes the crawl definition.
    Returns the crawl definition id or an error message to put in the CSV in its place.
    """

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

    # Gets the date range for WARCs to include in the CSV from the script arguments and any errors.
    # If there were errors, quits the script.
    start_date, end_date, errors_list = check_arguments(sys.argv)
    if len(errors_list) > 0:
        print("\nThe following errors were detected with the script arguments.")
        for error in errors_list:
            print(f"    * {error}")
        sys.exit()

    # Gets the WARC data from WASAPI and converts to Python.
    # If there was an API error, quits the script.
    try:
        metadata = get_metadata(start_date, end_date)
    except ValueError:
        print("\nCould not get the WARC metadata due to a WASAPI API error.")
        sys.exit()

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

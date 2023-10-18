"""
Purpose: Generate a report of WARC metadata from Archive-It.
The report is saved to the script_output folder, which is defined in configuration.py

The primary use is to generate a list of all WARCs expected in the quarterly preservation download.
This script is used instead of the "download as a CSV" option from WASAPI in a web browser
to be able to reformat data and to add data from the Partner API about the seed.

The report includes the following fields:
    * AIP_Title
    * Department (collector)
    * WARC_Filename
    * AIT_Collection_ID
    * Seed_ID
    * Crawl_Job_ID
    * Crawl_Definition_ID
    * Date_Store-Time
    * Date_Crawl-Start
    * Date_Crawl-End
    * Size_GB
    * File_Type
    * MD5_Checksum
    * SHA1_Checksum

Script usage: python warc_metadata_report.py start_date end_date
WARCs stored on the start_date will be included in the report.
WARCs stored on the end_date will NOT be included in the report.
"""
from datetime import datetime, timedelta
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


def calculate_seed_id(warc_name):
    """
    Uses a regular expression to identify the Seed Id component of the WARC filename.
    Returns the Seed ID or default text if the pattern does not match.
    """
    try:
        regex = re.match(r'^.*?SEED(\d+)-', warc_name)
        seed_id = regex.group(1)
    except AttributeError:
        seed_id = "COULD NOT CALCULATE SEED ID"
    return seed_id


def get_crawl_definition(job):
    """
    Uses the Partner API to get the report for this crawl job, which includes the crawl definition.
    Returns the crawl definition id or default text if no id is found.
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


def get_seed_metadata(seed):
    """
    Uses the Partner API to get the seed report for this seed, which includes the collector and title.
    Returns the collector and title or default text if either are not found.
    """

    # Gets the seed report using the Partner API.
    seed_report = requests.get(f"{c.partner_api}/seed?id={seed}", auth=(c.username, c.password))
    if not seed_report.status_code == 200:
        return f"Cannot get collector. API error {seed_report.status_code} for seed report.", \
               f"Cannot get title. API error {seed_report.status_code} for seed report."
    py_seed_report = seed_report.json()

    # Gets the collector (department) from the seed report, or supplies default text if there is no department.
    try:
        collector = py_seed_report[0]['metadata']['Collector'][0]['value']
    except (KeyError, IndexError):
        collector = "No collector in Archive-It"

    # Gets the title from the seed report, or supplies default text if there is no title.
    try:
        title = py_seed_report[0]['metadata']['Title'][0]['value']
    except (KeyError, IndexError):
        title = "No title in Archive-It"

    return collector, title


def get_warc_metadata(start, end):
    """Uses WASAPI to get metadata for all WARCs stored during the specified date range.
    WARCs saved on the start date will be included. WARCs saved on the end date will not be included.
    Returns the WARC metadata, which is json, or raises an error."""

    # Gets the data from WASAPI using a page size (number of WARCs) that is typically sufficient.
    filters = {'store-time-after': start, 'store-time-before': end, 'page_size': 500}
    warc_data = requests.get(c.wasapi, params=filters, auth=(c.username, c.password))
    if not warc_data.status_code == 200:
        raise ValueError

    # If there were more WARCs in the date range (the count) than the page size,
    # gets the data again from WASAPI with an updated page size to get them all.
    if warc_data.json()['count'] > 500:
        filters = {'store-time-after': start, 'store-time-before': end, 'page_size': warc_data.json()['count']}
        warc_data = requests.get(c.wasapi, params=filters, auth=(c.username, c.password))
        if not warc_data.status_code == 200:
            raise ValueError

    return warc_data.json()


def size_to_gb(size_bytes):
    """
    Converts the size from bytes (value from API) to GB.
    As long as it won't result in 0, round to 2 decimal places.
    Returns the size in GB.
    """
    size = float(size_bytes) / 1000000000
    if size > 0.01:
        size = round(size, 2)
    return size


def verify_dates(argument_list):
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
    # Converts start and end from strings to dates for a more accurate comparison.
    if start and end:
        start_as_date = datetime.strptime(start, '%Y-%m-%d')
        end_as_date = datetime.strptime(end, '%Y-%m-%d')
        if start_as_date >= end_as_date:
            errors.append("The first argument must be an earlier date than the second.")

    return start, end, errors


if __name__ == '__main__':

    # Verifies the configuration file has the correct values.
    fun.check_config()

    # Gets the date range for WARCs to include in the CSV from the script arguments and any errors.
    # If there were errors, quits the script.
    start_date, end_date, errors_list = verify_dates(sys.argv)
    if len(errors_list) > 0:
        print("\nThe following errors were detected with the script arguments.")
        for error in errors_list:
            print(f"    * {error}")
        sys.exit()

    # Gets the WARC data from WASAPI and converts to Python.
    # If there was an API error, quits the script.
    try:
        metadata = get_warc_metadata(start_date, end_date)
    except ValueError:
        print("\nCould not get the WARC metadata due to a WASAPI API error.")
        sys.exit()

    # Makes a CSV for the warc metadata report with a header row.
    # The date range in the file name is the dates WARCs could have been stored,
    # which is one day sooner than the end_date due to how the API works.
    warc_last_date = (datetime.strptime(end_date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    report_path = f"{c.script_output}/warc_metadata_{start_date}_{warc_last_date}.csv"
    fun.save_csv_row(report_path, ["AIP_Title", "Department", "WARC_Filename", "AIT_Collection_ID", "Seed_ID",
                                   "Crawl_Job_ID", "Crawl_Definition_ID", "Date_Store-Time", "Date_Crawl-Start",
                                   "Date_Crawl-End", "Size_GB", "File_Type", "MD5_Checksum", "SHA1_Checksum"])

    # Saves the metadata for each WARC to the WARC metadata report.
    for warc in metadata['files']:
        seed_id = calculate_seed_id(warc['filename'])
        seed_collector, seed_title = get_seed_metadata(seed_id)
        warc_row = [seed_title,
                    seed_collector,
                    warc['filename'],
                    warc['collection'],
                    seed_id,
                    warc['crawl'],
                    get_crawl_definition(warc['crawl']),
                    warc['store-time'],
                    warc['crawl-start'],
                    warc['crawl-time'],
                    size_to_gb(warc['size']),
                    warc['filetype'],
                    warc['checksums']['md5'],
                    warc['checksums']['sha1']]
        fun.save_csv_row(report_path, warc_row)

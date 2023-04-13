"""Makes a CSV with information about each WARC saved during a specified time frame:
    * WARC Filename
    * AIT Collection ID
    * Seed ID
    * Crawl Job ID
    * Date (store-time)
    * Size (GB)
    * Crawl Definition ID
    * Seed Title

Using this script instead of the WASAPI CSV download so data can be manipulated,
added from the Partner API, and reformatted.

UGA uses this script to generate a list of all WARCs expected in the quarterly preservation download
and adds them to a WARC Inventory for all downloaded WARCs to track that nothing is missed."""

# Script usage: python path\\warc_metadata_report.py earliest_date

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

    # Starts dictionaries for crawl definitions and titles.
    # These are looked up via the API for each WARC, which is slow.
    # Saving time by saving the results since there are many WARCs with the same values.
    JOB_TO_CRAWL = {}
    SEED_TO_TITLE = {}

    # Starts a CSV file, with a header, for the WARC data.
    # It is saved to the script output folder indicated in the configuration file.
    WARC_CSV = open(os.path.join(c.script_output, "warc_metadata_report.csv"), "w", newline="")
    CSV_WRITER = csv.writer(WARC_CSV)
    CSV_WRITER.writerow(["WARC Filename", "AIT Collection", "Seed", "Job", "Date (store-time)",
                         "Size (GB)", "Crawl Def", "AIP", "AIP Title", "MD5"])

    # Gets the data for each WARC.
    for warc in metadata["files"]:
        filename = warc["filename"]
        size = warc["size"]
        collection = warc["collection"]
        job_id = warc["crawl"]
        store_time = warc["store-time"]
        md5 = warc["checksums"]["md5"]

        # Gets the seed id from the WARC filename.
        try:
            regex = re.match(r'^.*?SEED(\d+)-', filename)
            seed_id = regex.group(1)
        except AttributeError:
            seed_id = "COULD NOT CALCULATE"

        # Converts the size from bytes to GB.
        # As long as it won't result in 0, round to 2 decimal places.
        size = float(size) / 1000000000
        if size > 0.01:
            size = round(size, 2)

        # Gets the crawl definition from the dictionary (if previously calculated) or API.
        try:
            crawl_def = JOB_TO_CRAWL[job_id]
        except KeyError:
            crawl_def = get_crawl_def(job_id)
            JOB_TO_CRAWL[job_id] = crawl_def

        # Gets the seed/AIP title from the dictionary (if previously calculated) or API.
        try:
            title = SEED_TO_TITLE[seed_id]
        except KeyError:
            title = get_title(seed_id)
            SEED_TO_TITLE[seed_id] = title

        # Saves the WARC data as a row in the CSV.
        CSV_WRITER.writerow([filename, collection, seed_id, job_id, store_time, size, crawl_def, "", title, md5])

    WARC_CSV.close()

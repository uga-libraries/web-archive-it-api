"""
Purpose: Generate reports of seed metadata fields added by the archivist to the Archive-it Interface.
The report can include just required fields (from the UGA Metadata Profile) or all fields.
The primary uses are to verify metadata is complete prior to a preservation download and
to review and batch edit the metadata.

The report includes the following fields for all seeds in the UGA Archive-It Account:
    * Collector
    * Creator
    * Date
    * Description - only if all_fields
    * Identifier
    * Language
    * Relation - only if all_fields
    * Rights
    * Subject - only if all_fields
    * Title

Script usage: python seed_metadata_report.py [all_fields]
Include "all_fields" as an optional argument to include optional as well as required fields.
"""
from datetime import datetime
import requests
import sys
try:
    import configuration as c
except ModuleNotFoundError:
    print("File configuration.py is missing from the script repo.")
    print("Use configuration_template.py to create this file.")
    sys.exit()
import shared_functions as fun


def get_metadata():
    """
    Uses the Archive-It Partner API to get the metadata for all of the seeds
    and returns the json as a Python object.
    If there was an error with the API call, quits the script.
    """
    seeds_metadata = requests.get(f'{c.partner_api}/seed?limit=-1', auth=(c.username, c.password))
    if not seeds_metadata.status_code == 200:
        print('Error with Archive-It API connection when getting seed report', seeds_metadata.status_code)
        exit()
    py_seeds_metadata = seeds_metadata.json()
    return py_seeds_metadata


def get_header(optional):
    """
    Returns a list with the columns for the CSV,
    which are different depending on if required fields or all fields will be included.
    """
    required_header = ["ID", "Name", "Collector", "Creator", "Date", "Identifier", "Language", "Rights", "Title",
                       "Archive-It Metadata Page"]

    all_header = ["ID", "Name", "Collector [required]", "Creator [required]", "Date [required]", "Description",
                  "Identifier [required]", "Language [required]", "Relation", "Rights [required]", "Subject",
                  "Title [required]", "Archive-It Metadata Page"]

    if optional:
        return all_header
    else:
        return required_header


def make_metadata_list(seed_data, header_list):
    """
    Makes and returns a list of metadata values for a particular seed.
    Most can be looked up from the collection's data using the field name in the header,
    with the qualifier "[required]" removed when optional fields are part of the report.
    The URL for the last field, Archive-It Metadata Page, is constructed by the script.
    """
    metadata_list = [seed_data['id'], seed_data['url']]

    # The function is for values within the metadata section.
    # It works for everything except the first 2 values and the last value.
    header_list = [field.replace(" [required]", "") for field in header_list]
    for field_name in header_list[2:-1]:
        metadata_list.append(fun.get_metadata_value(seed_data, field_name))

    metadata_list.append(f"{c.inst_page}/collections/{seed_data['collection']}/seeds/{seed_data['id']}/metadata")

    return metadata_list


if __name__ == '__main__':
    # Verifies the configuration file has the correct values.
    fun.check_config()

    # Boolean for if optional fields should be included, based on the script argument.
    include_optional = fun.check_fields(sys.argv)

    # Gets the seeds' metadata from the Archive-It Partner API.
    seeds = get_metadata()

    # Makes a CSV for the seed metadata report with a header row.
    report_path = f"{c.script_output}/seed_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv"
    header = get_header(include_optional)
    fun.save_csv_row(report_path, header)

    # Saves the metadata for each seed to the seed metadata report.
    for seed in seeds:
        seed_row = make_metadata_list(seed, header)
        fun.save_csv_row(report_path, seed_row)

"""
Purpose: Generate a report of collection metadata fields from Archive-It.
The report is saved to the script_output folder, which is defined in configuration.py
The report can include just required fields (from the UGA Metadata Profile) or all fields.

The primary uses are to verify metadata is complete prior to a preservation download and
to review and batch edit the metadata.

The report includes the following fields for all collections:
    * Collector - required
    * Creator
    * Date - required
    * Description - required
    * Identifier
    * Language
    * Relation
    * Rights
    * Subject
    * Title - required

Script usage: python collection_metadata_report.py [required]
Include "required" as an optional argument to only include required fields.
If there is no argument or it is some other text besides required, the report will have all fields.
"""
from datetime import datetime
import requests
import sys
try:
    import configuration as c
except ModuleNotFoundError:
    print("File configuration.py is missing from the script folder.")
    print("Use configuration_template.py to create this file.")
    sys.exit()
import shared_functions as fun


def get_metadata():
    """
    Gets the metadata for all collections from the Archive-It Partner API and returns the metadata, which is json.
    If there was an error with the API call, quits the script.
    """
    collections_metadata = requests.get(f'{c.partner_api}/collection?limit=-1', auth=(c.username, c.password))
    if not collections_metadata.status_code == 200:
        print('Error with Archive-It API connection when getting collection metadata', collections_metadata.status_code)
        exit()
    py_collections_metadata = collections_metadata.json()
    return py_collections_metadata


def get_header(optional):
    """
    Returns a list with the column names for the CSV,
    which are different depending on if required fields or all fields will be included.
    """
    required_header = ["ID", "Name", "Collector", "Date", "Description", "Title", "Archive-It Metadata Page"]

    all_header = ["ID", "Name", "Collector [required]", "Creator", "Date [required]", "Description [required]",
                  "Identifier", "Language", "Relation", "Rights", "Subject", "Title [required]",
                  "Archive-It Metadata Page"]

    if optional:
        return all_header
    else:
        return required_header


def make_metadata_list(collection_data, header_list):
    """
    Makes and returns a list of metadata values for a particular collection.
    """
    # The first 2 values are in the collection data but not the metadata section.
    # They are always present and do not repeat.
    metadata_list = [collection_data['id'], collection_data['name']]

    # The function is for values within the metadata section, which is most of the columns.
    # Some values are not always present and some repeat, and it handles all those cases.
    # The name of the fields in the metadata are the same as the column header, without [required].
    header_list = [field.replace(" [required]", "") for field in header_list]
    for field_name in header_list[2:-1]:
        metadata_list.append(fun.get_metadata_value(collection_data, field_name))

    # Constructs the link to the metadata page for this collection to make it easier to edit if an error is found.
    metadata_list.append(f"{c.inst_page}/collections/{collection_data['id']}/metadata")

    return metadata_list


if __name__ == '__main__':

    # Verifies the configuration file has the correct values.
    fun.check_config()

    # Boolean for if optional fields should be included, based on the script argument.
    include_optional = fun.check_fields_to_include(sys.argv)

    # Gets the metadata for all collections from the Archive-It Partner API.
    collections = get_metadata()

    # Makes a CSV for the collection metadata report with a header row.
    report_path = f"{c.script_output}/collection_metadata_{datetime.today().strftime('%Y-%m-%d')}.csv"
    header = get_header(include_optional)
    fun.save_csv_row(report_path, header)

    # Saves the metadata for each collection to the collection metadata report.
    for collection in collections:
        collection_row = make_metadata_list(collection, header)
        fun.save_csv_row(report_path, collection_row)

"""
Purpose: Generate reports of collection metadata fields added by the archivist to the Archive-it Interface.
The report can include just required fields (from the UGA Metadata Profile) or all fields.
The primary uses are to verify metadata is complete prior to a preservation download and
to review and batch edit the metadata.

The report includes the following fields for all seeds in the UGA Archive-It Account:
    * Collector
    * Creator - only if all_fields
    * Date
    * Description
    * Identifier - only if all_fields
    * Language - only if all_fields
    * Relation - only if all_fields
    * Rights - only if all_fields
    * Subject - only if all_fields
    * Title

Script usage: python collection_metadata_report.py y [all_fields]
Include "all_fields" as an optional argument to include optional as well as required fields.
"""
import os
import requests
import sys
import configuration as c
import shared_functions as fun


def get_metadata():
    """
    Uses the Archive-It Partner API to get the metadata for all of the collections
    and returns the json as a Python object.
    If there was an error with the API call, quits the script.
    """
    collections_metadata = requests.get(f'{c.partner_api}/collection?limit=-1', auth=(c.username, c.password))
    if not collections_metadata.status_code == 200:
        print('Error with Archive-It API connection when getting collection report', collections_metadata.status_code)
        exit()
    py_collections_metadata = collections_metadata.json()
    return py_collections_metadata


def get_header(optional):
    """
    Returns a list with the columns for the CSV,
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
    Most can be looked up from the collection's data using the field name in the header,
    with the qualifier "[required]" removed when optional fields are part of the report.
    The URL for the last field, Archive-It Metadata Page, is constructed by the script.
    """
    metadata_list = [collection_data['id'], collection_data['name']]

    # The function is for values within the metadata section.
    # It works for everything except the first 2 and last values.
    header_list = [field.replace(" [required]", "") for field in header_list]
    for field_name in header_list[2:-1]:
        metadata_list.append(fun.get_metadata_value(collection_data, field_name))

    metadata_list.append(f"{c.inst_page}/collections/{collection_data['id']}/metadata")

    return metadata_list


# Changes the current directory to the folder where the reports will be saved.
# If this cannot be done, prints an error for the user and quits the script.
try:
    os.chdir(c.script_output)
except FileNotFoundError:
    print('The script_output directory in the configuration file does not exist.')
    exit()

# If the optional argument was provided, sets a variable optional to True.
# If the argument is not the expected value, prints an error for the user and quits the script.
include_optional = False
if len(sys.argv) == 2:
    if sys.argv[1] == "all_fields":
        include_optional = True
    else:
        print('The provided value for the argument is not the expected value of "all_fields".')
        exit()

# Gets the collections metadata from the Archive-It Partner API.
collections = get_metadata()

# Makes a CSV for the collection metadata report with a header row.
header = get_header(include_optional)
fun.save_csv_row("collection", header)

# Gets the data for each collection's metadata and saves it to the collection metadata report.
# Most can be looked up from the collections data using the field name in the header,
# with the qualifier "[required]" removed when optional fields are part of the report.
# The URL for the last field, Archive-It Metadata Page, is constructed by the script.
for collection in collections:
    collection_row = make_metadata_list(collection, header)
    fun.save_csv_row("collection", collection_row)

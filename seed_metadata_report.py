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

Script usage: python seed_metadata_report.py y [all_fields]
Include "all_fields" as an optional argument to include optional as well as required fields.
"""
import os
import requests
import sys
import configuration as c
import shared_functions as fun


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

# Gets the Archive-It seed report with data on all the seeds.
# If there was an error with the API call, quits the script.
seeds = requests.get(f'{c.partner_api}/seed?limit=-1', auth=(c.username, c.password))
if not seeds.status_code == 200:
    print('Error with Archive-It API connection when getting seed report', seeds.status_code)
    exit()

# Saves the seed data as a Python object.
py_seeds = seeds.json()

# Saves the seed data to a CSV.
fun.make_csv(py_seeds, "seed", include_optional)
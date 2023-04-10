"""
Purpose: functions used by more than one script for working with the Archive-It APIs.
"""
import csv
import os
import requests
import sys
import configuration as c


def check_config():
    """
    Checks that all required variables are in the configuration file
    and verifies their values are correct.
    """
    errors = []

    # Validates that the path in script output exists on the local machine.
    try:
        if not os.path.exists(c.script_output):
            errors.append(f"Variable path '{c.script_output}' is not correct.")
    except AttributeError:
        errors.append("Variable 'script_output' is missing from the configuration file.")

    # Validates that the API URLs, which are consistent values, are correct.
    try:
        if c.partner_api != 'https://partner.archive-it.org/api':
            errors.append("Partner API path is not correct.")
    except AttributeError:
        errors.append("Variable 'partner_api' is missing from the configuration file.")
    try:
        if c.wasapi != 'https://warcs.archive-it.org/wasapi/v1/webdata':
            errors.append("WASAPI path is not correct.")
    except AttributeError:
        errors.append("Variable 'wasapi' is missing from the configuration file.")

    # Validates that the institution page exists on the internet.
    try:
        response = requests.get(c.inst_page)
        if response.status_code != 200:
            errors.append("Institution Page URL is not correct.")
    except AttributeError:
        errors.append("Variable 'inst_page' is missing from the configuration file.")

    # Verifies that the username and password are present.
    try:
        c.username
    except AttributeError:
        errors.append("Variable 'username' is missing from the configuration file.")
    try:
        c.password
    except AttributeError:
        errors.append("Variable 'password' is missing from the configuration file.")

    # Validates that the credentials are correct by using them with an API call.
    # This only works if the partner_api variable was in the configuration file.
    try:
        response = requests.get(f'{c.partner_api}/seed?limit=5', auth=(c.username, c.password))
        if response.status_code != 200:
            errors.append("Could not access Partner API with provided credentials. "
                          "Check if the partner_api, username, and password variables have errors.")
    except AttributeError:
        errors.append("Variables 'partner_api', 'username', and/or 'password' are missing from the configuration file.")

    # If there were errors, prints them and exits the script.
    if len(errors) > 0:
        print("\nProblems detected with configuration.py.")
        for error in errors:
            print("    *", error)
        print("\nCorrect the configuration file using configuration_template.py as a model")
        sys.exit()


def check_fields(args):
    """
    Checks if the report should include required fields only or all metadata fields,
    based on the optional second argument.
    """
    if len(args) == 2 and args[1] == "required":
        return False
    else:
        return True


def get_metadata_value(data, field):
    """
    Returns the value of a field in the Archive-It Partner API data within the metadata section.
    If the field is repeated, returns a string with all of the values separated by semicolons.
    If the  field is not in the data, returns the string "NO DATA OF THIS TYPE".
    """
    try:
        values_list = []
        for value in data['metadata'][field]:
            values_list.append(value['value'])
        values = ';'.join(values_list)
        return values
    except KeyError:
        return 'NO DATA OF THIS TYPE'


def save_csv_row(report_path, row_list):
    """
    Creates a CSV, if it doesn't already exist for this report,
    and saves the provided list as a new row in the spreadsheet.
    """
    with open(report_path, 'a', newline='') as output:
        write = csv.writer(output)
        write.writerow(row_list)

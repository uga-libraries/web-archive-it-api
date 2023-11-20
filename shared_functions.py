"""Functions used by more than one script for working with the Archive-It APIs."""
import csv
import os
import requests
import sys
import configuration as c


def check_config():
    """Check the configuration file is correct and if not quits the script.

    The values of configuration.py are imported by running the script.
    There are no parameters and it returns nothing.
    """
    errors = []

    # Checks if the path in script_output exists on the local machine.
    try:
        if not os.path.exists(c.script_output):
            errors.append(f"Variable path '{c.script_output}' is not correct.")
    except AttributeError:
        errors.append("Variable 'script_output' is missing from the configuration file.")

    # Checks that the API URLs, which are consistent values, are correct.
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

    # Checks that the institution page exists.
    try:
        response = requests.get(c.inst_page)
        if response.status_code != 200:
            errors.append("Institution Page URL is not correct.")
    except AttributeError:
        errors.append("Variable 'inst_page' is missing from the configuration file.")

    # Checks that the username and password are present.
    try:
        c.username
    except AttributeError:
        errors.append("Variable 'username' is missing from the configuration file.")
    try:
        c.password
    except AttributeError:
        errors.append("Variable 'password' is missing from the configuration file.")

    # Checks that the Archive-It username and password are correct by using them with an API call.
    # This only works if the partner_api variable is in the configuration file.
    try:
        response = requests.get(f'{c.partner_api}/seed?limit=5', auth=(c.username, c.password))
        if response.status_code != 200:
            errors.append("Could not access Partner API with provided credentials. "
                          "Check if the partner_api, username, and/or password variables have errors.")
    except AttributeError:
        errors.append("Variables 'partner_api', 'username', and/or 'password' are missing from the configuration file.")

    # If there were errors, prints them and exits the script.
    if len(errors) > 0:
        print("\nProblems detected with configuration.py.")
        for error in errors:
            print("    *", error)
        print("\nCorrect the configuration file using configuration_template.py as a model")
        sys.exit()


def check_fields_to_include(args):
    """Determine if the report should include required fields or all metadata fields based on the optional argument.

    Parameter:
        args : value of sys.argv

    Returns:
        Boolean if optional fields should be included (True) or not included (False)
    """
    # If an additional argument was included, and the value is "required", optional fields are not included.
    if len(args) == 2 and args[1] == "required":
        return False
    else:
        return True


def get_metadata_value(data, field):
    """Get and format the value of a field in the API data, which may be repeated, occur once, or not be included.

    Parameters:
        data : API data
        field : field in the API to get the value from

    Returns:
        Value of the field, separated by semicolons if it is repeated and default text if it is not included.
    """
    # If the field is present at least once, store all values into a list and
    # return a string that includes all values, separated by a semicolon if the field was present more than once.
    try:
        values_list = []
        for value in data['metadata'][field]:
            values_list.append(value['value'])
        values = ';'.join(values_list)
        return values
    # If the field is not present, returns a default string.
    except KeyError:
        return 'NO DATA OF THIS TYPE'


def save_csv_row(report_path, row_list):
    """Save a row to a CSV spreadsheet.

    Parameters:
        report_path : path to the report spreadsheet, which may or may not already exist
        row_list : list with values for a single spreadsheet row

    Returns:
        Nothing
    """
    # Append will create the report if it doesn't already exist or add to the end of the report if it is present.
    with open(report_path, 'a', newline='') as output:
        write = csv.writer(output)
        write.writerow(row_list)

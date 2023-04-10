"""
Purpose: functions used by more than one script for working with the Archive-It APIs.
"""
import csv


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

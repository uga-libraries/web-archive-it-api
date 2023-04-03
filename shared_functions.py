"""
Purpose: functions used by more than one script for working with the Archive-It APIs.
"""
import csv


def get_metadata_value(data, field):
    """
    Returns the value of a field in the Archive-It Partner API data within the metadata section.
    If the field is repeated, returns a string with all of the values separated by semicolons.
    If the  field is not in the data, returns the string NONE.
    """
    try:
        values_list = []
        for value in data['metadata'][field]:
            values_list.append(value['value'])
        values = ';'.join(values_list)
        return values
    except KeyError:
        return 'NONE'


def save_csv_row(report_type, row_list):
    """
    Creates a CSV, if it doesn't already exist for this report,
    and saves the provided list as a new row in the spreadsheet.
    """
    with open(f'{report_type}_metadata.csv', 'a', newline='') as output:
        write = csv.writer(output)
        write.writerow(row_list)

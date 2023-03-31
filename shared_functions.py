"""
Purpose: functions used by more than one script for working with the Archive-It APIs.
"""
import csv
import configuration as c


def get_metadata_value(data, field):
    """Looks up the value(s) of a field in the Archive-It API output for a particular collection or seed. If the
    field is not in the output, returns the string NONE instead. """

    try:
        # Makes a list of all the values for that data field. Some fields may repeat, e.g. language.
        values_list = []
        for value in data['metadata'][field]:
            values_list.append(value['value'])

        # Converts the list to a string.
        # When there are multiple values in the list, each value is separated by a semicolon.
        values = '; '.join(values_list)
        return values

    except KeyError:
        return 'NONE'


def make_csv(json, report_type, include_optional):
    """Saves the values from the desired fields (required only or all) for either the collections or seeds to a CSV. """

    # Dictionary of metadata terms, with values of if they are required for collection and seed.
    # Collection and seed have the same set of metadata terms, but different rules about what is required.
    metadata = {"Collector": {"collection": "required", "seed": "required"},
                "Creator": {"collection": "not_required", "seed": "required"},
                "Date": {"collection": "required", "seed": "required"},
                "Description": {"collection": "required", "seed": "not_required"},
                "Identifier": {"collection": "not_required", "seed": "required"},
                "Language": {"collection": "not_required", "seed": "required"},
                "Relation": {"collection": "not_required", "seed": "not_required"},
                "Rights": {"collection": "not_required", "seed": "required"},
                "Subject": {"collection": "not_required", "seed": "not_required"},
                "Title": {"collection": "required", "seed": "required"}}

    # Makes a list of metadata fields to include in this report.
    if include_optional:
        metadata_fields = list(metadata.keys())
    else:
        metadata_fields = [key for key, value in metadata.items() if value[report_type] == "required"]

    # Makes a CSV to save the metadata to.
    with open(f'{report_type}_metadata.csv', 'w', newline='') as output:

        # Makes the header row, an alphabetically sorted list of the metadata fields,
        # with ID and Name added to the beginning and Archive-It page added to end.
        metadata_fields.sort()
        header = ["ID", "Name"]
        for field in metadata_fields:
            # If optional fields are included, note which are required.
            if include_optional and metadata[field][report_type] == "required":
                field = field + " [required]"
            header.append(field)
        header.append("Archive-It Metadata Page")
        write = csv.writer(output)
        write.writerow(header)

        # Iterates over the metadata for each item.
        for item in json:

            # Gets the value of the item name, which is name for collection and url for seed.
            if report_type == "collection":
                name = item['name']
            else:
                name = item['url']

            # Gets the values of each of the metadata fields and saves to a list.
            # If the field is repeated, all values are included. If the field has no data, the value is NONE.
            metadata_values = []
            for field in metadata_fields:
                metadata_values.append(get_metadata_value(item, field))

            # Constructs the URL of the Archive-It metadata page.
            # Included in the report to make it easy to edit a record.
            if report_type == "collection":
                ait_page = f"{c.inst_page}/collections/{item['id']}/metadata"
            else:
                ait_page = f"{c.inst_page}/collections/{item['collection']}/seeds/{item['id']}/metadata"

            # Makes a single list with the item metadata by combining three lists:
            # the id and name, the metadata values, and the Archive-It metadata page URL.
            row = [item["id"], name] + metadata_values + [ait_page]

            # Adds the complete metadata list as a row to the CSV.
            write.writerow(row)
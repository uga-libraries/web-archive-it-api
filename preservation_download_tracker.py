"""Generate a report of seeds to be included in a preservation download.

The report includes the following fields for all included seeds, plus tracking columns:
   * AIP_ID [blank column, data added manually]
   * AIP_Title
   * Department
   * AIT_Collection_ID
   * Seed_ID
   * Crawl_Job_ID: separated with semicolon if more than one
   * Crawl_Definition_ID: separated with semicolon if more than one
   * WARC_Count: number of WARCs for the seed
   * WARC_Size_GB: number of GB for all WARCs for the seed

Parameter:
    warc_metadata_path : required. the location of the WARC metadata report, created using warc_metadata_report.py

Returns:
    A CSV file saved to the script_output folder with seed metadata and blank columns named with workflow steps.
"""
from datetime import datetime, timedelta
import os
import pandas as pd
import re
import sys
try:
    import configuration as c
except ModuleNotFoundError:
    print("File configuration.py is missing from the script folder.")
    print("Use configuration_template.py to create this file.")
    sys.exit()
import shared_functions as fun


def aggregate_ids(data_df, id_name):
    """Get the Crawl Job IDs or Crawl Definition IDs for each seed.

    Parameters:
        data_df : dataframe with metadata for all WARCs
        id_name : the ID type, either Crawl_Job_ID or Crawl_Definition_ID

    Returns:
        A series with each seed and its IDs, with IDs separated by a semicolon if there is more than one.
    """
    # Makes a dataframe with unique seed and specified ID combinations.
    # This has to be done first so only unique values are combined,
    # and not repeats of the same ID from any seed with multiple WARCs but the same ID.
    df = data_df[['Seed_ID', id_name]].copy()
    df = df.drop_duplicates()

    # Changes the specified ID to a string, so that it can be combined in the next step into one value.
    df[id_name] = df[id_name].astype(str)

    # Makes and returns a series with one row per Seed_ID and a value of the specified ids.
    # If there is more than one ID, they are separated by semicolons.
    aggregated = df.groupby('Seed_ID')[id_name].apply(';'.join)
    return aggregated


def create_new_metadata(data_df):
    """Combine WARC metadata into a summary for the seed.

    Parameter:
        data_df : dataframe with metadata for all WARCs

    Returns:
         Dataframe with Crawl Job ID, Crawl Definition ID, WARC Count, and WARC Size in GB for each seed.
    """
    # Crawl Job IDs combined for each seed. There may be more than one Crawl Job ID.
    crawl_jobs = aggregate_ids(data_df, 'Crawl_Job_ID')

    # Crawl Definition IDs combined for each seed. There may be more than one Crawl Definition ID.
    crawl_definitions = aggregate_ids(data_df, 'Crawl_Definition_ID')

    # Subtotal with number of WARCs for each seed.
    warc_count = data_df.groupby(['Seed_ID'])['Seed_ID'].count()

    # Subtotal with number of GB for each seed.
    warc_size_gb = data_df.groupby(['Seed_ID'])['Size_GB'].sum().round(3)

    # Combines the four metadata types into a dataframe and returns the dataframe.
    # The index is the Seed_ID.
    df = pd.concat([crawl_jobs, crawl_definitions, warc_count, warc_size_gb], axis=1)
    df.columns = ["Crawl_Job_ID", "Crawl_Definition_ID", "WARC_Count", "WARC_Size_GB"]
    return df


def save_csv(df, filename):
    """Save the data and empty columns for tracking progress to a CSV.

    Parameters:
        df : dataframe with the seed data summarized from the WARC data
        filename : path to the WARC metadata report, used to calculate the data of the data

    Returns:
        Nothing
    """
    # Adds an empty column for the AIP_ID (calculated later) to the beginning of the dataframe
    # and a number of empty columns for tracking to the end of the dataframe.
    tracking_columns = ["Log_coll_scope", "Log_seed_scope", "Log_Other_Reports", "WARC_Download", "Completeness_Log",
                        "AIP_Log", "QC1", "Upload", "Ingest", "QC2", "Complete"]
    df = df.reindex(columns=["AIP_ID"] + df.columns.tolist() + tracking_columns)

    # Calculates the month of the preservation download to include in the report filename.
    # It is one month later than the end date in the WARC metadata report.
    regex = re.match(r'^warc_metadata_\d{4}-\d{2}-\d{2}_(\d{4}-\d{2}-\d{2}).csv', filename)
    end_date_string = regex.group(1)
    end_date = datetime.strptime(end_date_string, '%Y-%m-%d')
    preservation_date = (end_date + timedelta(days=1)).strftime('%Y-%m')

    # Saves the dataframe to a CSV in the script_output folder.
    df.to_csv(os.path.join(c.script_output, f"Preservation_Download_{preservation_date}.csv"), index=False)


def verify_metadata_path(argument_list):
    """Check the script argument is correct.

    Parameter:
        argument_list : value of sys.argv

    Returns:
         The path to the WARC CSV or raises an error.
    """
    # Test if the required argument was included.
    try:
        # Test if the required argument is a valid path.
        if os.path.exists(argument_list[1]):
            return argument_list[1]
        else:
            raise ValueError
    except IndexError:
        raise IndexError


if __name__ == '__main__':

    # Verifies the configuration file has the correct values.
    fun.check_config()

    # Verifies the required argument (path to WARC metadata report) was provided and is correct.
    try:
        input_path = verify_metadata_path(sys.argv)
    except IndexError:
        print("The required argument, path to the WARC metadata report, is missing.")
        sys.exit()
    except ValueError:
        print(f"The provided path to the WARC metadata report '{sys.argv[1]}' is not correct.")
        sys.exit()

    # Reads the WARC metadata report into a pandas dataframe.
    warc_df = pd.read_csv(input_path)

    # Gets the seed metadata that is consistent for every WARC in that seed.
    seed_df = warc_df[['AIP_Title', 'Department', 'AIT_Collection_ID', 'Seed_ID']].copy()
    seed_df = seed_df.drop_duplicates()

    # Gets the seed metadata that requires combining WARC metadata.
    new_data_df = create_new_metadata(warc_df)

    # Combines the new data with the seed data.
    tracker_df = pd.merge(seed_df, new_data_df, left_on='Seed_ID', right_index=True)

    # Adds additional columns needed for tracking the download process and saves the dataframe to a CSV.
    save_csv(tracker_df, os.path.basename(input_path))

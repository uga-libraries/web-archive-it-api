"""
Purpose: generate a report of seeds to be included in a preservation download.
The report includes metadata about the seeds and columns for tracking the progress.
The report uses the WARC metadata report (created with warc_metadata_report.py) as input.

The report includes the following fields for all included seeds:
   * AIP_ID [blank column, data added manually]
   * AIP_Title
   * AIT_Collection_ID
   * Seed_ID
   * Crawl_Job_IDs: separated with semicolon if more than one
   * Crawl_Definition_IDs: separated with semicolon if more than one
   * WARC_Count: number of WARCs for the seed
   * WARC_Size_GB: number of GB for all WARCs for the seed
   * Batch [blank column for tracking progress]
   * Script_Log [blank column for tracking progress]
   * Completeness_Log [blank column for tracking progress]
   * QC1 [blank column for tracking progress]
   * Upload [blank column for tracking progress]
   * Ingest [blank column for tracking progress]
   * QC2 [blank column for tracking progress]
   * Complete [blank column for tracking progress]

Script usage: python preservation_download_tracker.py warc_metadata_path
warc_metadata_path is the location of the WARC metadata report, created using warc_metadata_report.py
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
    """
    Makes a series with an aggregated set of the specified ID for each Seed ID.
    This is used with Crawl Job ID and Crawl Definition ID.
    Returns the series.
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
    """
    Combines WARC metadata into a summary for the seed.
    Makes a series for each metadata type and then combines them into a dataframe.
    Returns the dataframe.
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
    """
    Adds empty columns to the dataframe to use for tracking the download process
    and saves the dataframe to a CSV named Preservation_Download_YYYY-MM.
    """
    # Adds an empty column for the AIP_ID (calculated later) to the beginning of the dataframe
    # and a number of empty columns for tracking to the end of the dataframe.
    tracking_columns = ["Log: coll_scope", "Log:seed_scope", "Log: Other Reports", "WARC Download", "Completeness Log", "AIP Log", "QC1", "Upload", "Ingest", "QC2", "Complete"]
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
    """
    Verifies the required argument (path to WARC metadata report) is present and correct.
    Returns the path or raises an error.
    """
    try:
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

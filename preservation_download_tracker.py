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
   * Script_Log_Results [blank column for tracking progress]
   * Completeness_Log_Results [blank column for tracking progress]
   * QC1 [blank column for tracking progress]
   * Upload [blank column for tracking progress]
   * Ingest [blank column for tracking progress]
   * QC2 [blank column for tracking progress]
   * Complete [blank column for tracking progress]

Script usage: python preservation_download_tracker.py warc_metadata_path
warc_metadata_path is the location of the WARC metadata report, created using warc_metadata_report.py
"""
import os
import pandas as pd
import sys
try:
    import configuration as c
except ModuleNotFoundError:
    print("File configuration.py is missing from the script folder.")
    print("Use configuration_template.py to create this file.")
    sys.exit()
import shared_functions as fun


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
    df = pd.read_csv(input_path)

    # # Seed metadata that is consistent for every WARC in that seed.
    seed_df = df[['AIP_Title', 'Department', 'AIT_Collection_ID', 'Seed_ID']].copy()
    seed_df = seed_df.drop_duplicates()

    # Subtotal with number of WARCs for each Seed ID.
    warc_count = df.groupby(['Seed_ID'])['Seed_ID'].count()

    # Subtotal with number of GB for each Seed ID.
    warc_size_gb = df.groupby(['Seed_ID'])['Size_GB'].sum()

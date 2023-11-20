# Archive-It APIs Scripts

## Overview

These scripts use the Archive-It web archiving service APIs 
([Partner API](https://support.archive-it.org/hc/en-us/articles/360032747311-Access-your-account-with-the-Archive-It-Partner-API) 
and [WASAPI](https://support.archive-it.org/hc/en-us/articles/360015225051-Find-and-download-your-WARC-files-with-WASAPI)) to generate reports.
They are used to prepare for quarterly downloads from Archive-It for preservation and to review and update metadata. 

All reports are CSVs. Report scripts in this repository:

- collection_metadata_report.py: [Example collection metadata report](documentation/collection_metadata_2023-10-18.csv)
- preservation_download_tracker.py: WARC metadata summarized by seed. [Example preservation download tracker](documentation/Preservation_Download_2022-05.csv)
- seed_metadata_report.py: [Example seed metadata report](documentation/seed_metadata_2023-10-18.csv)
- warc_csv.py: WARC metadata for all WARCs stored during the specified time frame. [Example WARC metadata report](documentation/warc_metadata_2022-02-01_2022-04-30.csv)

## Getting Started

### Dependencies

- [pandas](https://pandas.pydata.org/): edit and summarize API output
- [requests](https://pypi.org/project/requests/): download content from the APIs

### Installation

Prior to using any of these scripts, create a file named configuration.py, modeled after configuration_template.py,
and save it to your local copy of this repository. 
This defines a place for script output to be saved and includes your Archive-It login credentials.

### Script Arguments

collection_metadata_report.py
   - required (optional): add "required" to limit the report to UGA's required collection metadata fields. 
     Otherwise, all fields are included.

preservation_download_tracker.py
   - warc_metadata_path (required): the location of the WARC metadata report, created using warc_metadata_report.py.

seed_metadata_report.py
   - required (optional): add "required" to limit the report to UGA's required seed metadata fields. 
     Otherwise, all fields are included.

warc_csv.py
   - Both date arguments are formatted YYYY-MM-DD and define the date range of WARCs to include.
   - start_date (required): first store date of WARCs to include.
   - end_date (required): first store date of WARCs NOT to include (last date included is the day before end_date).

### Testing

There are unit tests for each function and the entire script for each of the scripts,
except for check_config() (Issue 21) and the API error for get_metadata() (Issue 22).
The tests for functions that call the API and for the script rely on UGA Archive-It data.
For UGA, the expected results of these tests may need to be updated occasionally to keep in sync with our edits.
To use these tests with another account, all expected results must be edited to use data in that account.

## Workflow

These scripts are used for two different workflows at UGA:
   - [Preservation Download Workflow Documentation](documentation/Workflow_Preservation_Download.md) 
   - [Metadata Audit Workflow Documentation](documentation/Workflow_Metadata_Audit.md)


The reports may also be created and used individually.

## Author

Adriane Hanson, Head of Digital Stewardship, University of Georgia

# Archive-It APIs Scripts

# Overview

These scripts use the Archive-It web archiving service APIs 
([Partner API](https://support.archive-it.org/hc/en-us/articles/360032747311-Access-your-account-with-the-Archive-It-Partner-API) 
and [WASAPI](https://support.archive-it.org/hc/en-us/articles/360015225051-Find-and-download-your-WARC-files-with-WASAPI)) to generate reports.
They are used as part of the preparation for quarterly downloads from Archive-It for preservation and
to review and update metadata. 

## collection_metadata_report.py

Makes a CSV with all collection metadata or just required collection metadata. 
Example: [collection_metadata_2023-10-18.csv](documentation/collection_metadata_2023-10-18.csv) 

Script usage: `python collection_metadata_report.py [required]`

Include "required" to limit the report to required fields. Otherwise, all fields are included.

## preservation_download_tracker.py

Makes a CSV from the WARC metadata report with seed (AIP) level information 
for tracking UGA quarterly preservation downloads.
Example: [Preservation_Download_2022-05.csv](documentation/Preservation_Download_2022-05.csv)

Script usage: `python preservation_download_tracker.py warc_metadata_path`

warc_metadata_path is the location of the WARC metadata report, created using warc_metadata_report.py

## seed_metadata_report.py

Makes a CSV with all seed metadata or just required seed metadata.
Example: [seed_metadata_2023-10-18.csv](documentation/seed_metadata_2023-10-18.csv)

Script usage: `python seed_metadata_report.py [required]`

Include "required" to limit the report to required fields. Otherwise, all fields are included.

## warc_csv.py

Makes a CSV with WARC metadata for all WARCs stored during the specified time frame.
WARCs stored on the start_date will be included. 
WARCs stored on the end_date will NOT be included.
Example: [warc_metadata_2022-02-01_2022-04-30.csv](documentation/warc_metadata_2022-02-01_2022-04-30.csv)

Script usage: `python warc_csv.py start_date end_date`



# Getting Started

## Dependencies

* Archive-It login credentials

## Installation

Prior to using any of these scripts, create a file named configuration.py, modeled after configuration_template.py,
and save it to your local copy of this repository.

# Workflow

These scripts are typically used in the following sequence to prepare for quarterly downloads from Archive-It for preservation,
although they may also be used individually.

1. A few weeks prior to the planned download, run collection_metadata_report.py and seed_metadata_report.py.
2. Review the collection and seed reports for missing metadata, and update in Archive-It prior to the download.
3. Run warc_metadata_report.py and copy the information into the WARC Inventory on Teams.
4. Run preservation_download_tracker.py to make the spreadsheet for tracking the download process.
5. Download the WARCs and associated metadata using [https://github.com/uga-libraries/web-aip](https://github.com/uga-libraries/web-aip)
6. Convert the downloaded content into AIPs using [https://github.com/uga-libraries/general-aip](https://github.com/uga-libraries/general-aip)
7. Ingest the AIPs into ARCHive, the Libraries digital preservation system

These scripts may also be used for reviewing and updating metadata in Archive-It. [Metadata Audit Workflow](documentation/Workflow_Metadata_Audit.md)

1. Use the scripts to create a collection and/or seed report.
2. Compare the reports to the [UGA Web Archives Metadata Profile](https://github.com/uga-libraries/web-archiving/blob/main/metadata_profile.md).
3. Edit the report(s).
4. Upload the report(s) to Archive-It.

# Author

Adriane Hanson, Head of Digital Stewardship, University of Georgia




# Archive-It APIs Scripts

# Overview

These scripts use the Archive-It web archiving service APIs 
([Partner API](https://support.archive-it.org/hc/en-us/articles/360032747311-Access-your-account-with-the-Archive-It-Partner-API) 
and [WASAPI](https://support.archive-it.org/hc/en-us/articles/360015225051-Find-and-download-your-WARC-files-with-WASAPI)) to generate reports.
They are used as part of the preparation for quarterly downloads from Archive-It for preservation and
to review and update metadata. 

## collection_metadata_report.py

Makes a CSV with all collection metadata or just required collection metadata:
   * Collector - required
   * Creator
   * Date - required
   * Description - required
   * Identifier
   * Language
   * Relation
   * Rights
   * Subject
   * Title - required

Script usage: `python collection_metadata_report.py [required]`

Include "required" to limit the report to required fields. Otherwise, all fields are included.

## preservation_download_tracker.py

Makes a CSV from the WARC metadata report with seed (AIP) level information 
for tracking UGA quarterly preservation downloads.
   * AIP_ID: blank column, data added manually
   * AIP_Title
   * AIT_Collection_ID
   * Seed_ID
   * Crawl_Job_IDs: separated with semicolon if more than one
   * Crawl_Definition_IDs: separated with semicolon if more than one
   * WARC_Count: number of WARCs for the seed
   * WARC_Size_GB: number of GB for all WARCs for the seed
   * Batch: blank column for tracking progress
   * Script_Log: blank column for tracking progress
   * Completeness_Log: blank column for tracking progress
   * QC1: blank column for tracking progress
   * Upload: blank column for tracking progress
   * Ingest: blank column for tracking progress
   * QC2: blank column for tracking progress
   * Complete: blank column for tracking progress

Script usage: `python preservation_download_tracker.py warc_metadata_path`

warc_metadata_path is the location of the WARC metadata report, created using warc_metadata_report.py

## seed_metadata_report.py

Makes a CSV with all seed metadata or just required seed metadata:
   * Collector - required
   * Creator - required
   * Date - required
   * Description
   * Identifier - required
   * Language - required
   * Relation
   * Rights - required
   * Subject
   * Title - required

Script usage: `python seed_metadata_report.py [required]`

Include "required" to limit the report to required fields. Otherwise, all fields are included.

## warc_csv.py

Makes a CSV with WARC metadata for all WARCs stored during the specified time frame:
   * Seed Title
   * Department (collector)
   * WARC Filename
   * AIT Collection ID
   * Seed ID
   * Crawl Job ID
   * Crawl Definition ID
   * Date (store-time)
   * Date (crawl start)
   * Date (crawl end)
   * Size (GB)
   * File Type
   * WARC MD5 Checksum
   * WARC SHA1 Checksum

Script usage: `python warc_csv.py start_date end_date`

WARCs stored on the start_date will be included. 
WARCs stored on the end_date will NOT be included.

# Getting Started

## Dependencies

* Archive-It login credentials
* Python requests libraries: `pip install requests`

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

# Author

Adriane Hanson, Head of Digital Stewardship, University of Georgia




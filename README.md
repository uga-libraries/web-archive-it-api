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



### Installation

Prior to using any of these scripts, create a file named configuration.py, modeled after configuration_template.py,
and save it to your local copy of this repository. 
This defines a place for script output to be saved and includes your Archive-It login credentials.

### Script Arguments

collection_metadata_report.py
   - required (optional): add "required" to limit the report to required collection metadata fields. 
     Otherwise, all fields are included.

preservation_download_tracker.py
   - warc_metadata_path (required): the location of the WARC metadata report, created using warc_metadata_report.py.

seed_metadata_report.py
   - required (optional): add "required" to limit the report to required seed metadata fields. 
     Otherwise, all fields are included.

warc_csv.py
   - Both date arguments are formatted YYYY-MM-DD and define the date range of WARCs to include
   - start_date (required): first store date of WARCs to include
   - end_date (required): first store date of WARCs NOT to include (last date included is the day before end_date)

## Workflow

These scripts are primarily used for two different workflows, the quarterly download of content from Archive-It for preservation
and auditing metadata to ensure it meets the UGA Libraries' standards. 
The reports may also be created and used individually. 

### Preservation Download

[Preservation Download Workflow Documentation](documentation/Workflow_Preservation_Download.md)

1. Two weeks before the download, create collection, seed, and WARC metadata reports.
2. Review the collection and seed metadata reports for missing metadata.
3. Review the WARC metadata report for unusual activity.
4. Email the collecting units to make corrections.
5. Verify the missing metadata has been added.
6. On the day of the download, create an updated WARC metadata report if any crawls were saved since it was last generated.
7. Make the preservation download tracker spreadsheet for tracking the workflow progress.
8. Download the WARCs and associated metadata using the [web aip script](https://github.com/uga-libraries/web-aip).
9. Convert the downloaded content into AIPs using the [general aip script](https://github.com/uga-libraries/general-aip).
10. Ingest the AIPs into ARCHive, the Libraries' digital preservation system.

### Metadata Audit

[Metadata Audit Workflow Documentation](documentation/Workflow_Metadata_Audit.md)

1. Use these scripts to create a collection and/or seed report.
2. Compare the reports to the [UGA Web Archives Metadata Profile](https://github.com/uga-libraries/web-archiving/blob/main/metadata_profile.md).
3. Edit the report(s).
4. Upload the report(s) to Archive-It.

## Author

Adriane Hanson, Head of Digital Stewardship, University of Georgia

# Preservation Download Workflow, 2023-10-18

## Overview

The UGA Libraries downloads all WARCs saved in a quarter (3-month period), along with a subset of the metadata reports.
Downloads are the first of February, May, August, and November for the 3 months prior.
The downloaded content is saved to the Libraries’ digital preservation system (ARCHive).

## Responsibility

UGA’s Archive-It Administrator (Head of Digital Stewardship) runs this workflow for Hargrett, MAGIL, and Russell.
It is not currently used by any other department at UGA.

## Workflow

### Preparation (2 weeks prior to download)

1. Use the API scripts to create collection, seed, and WARC metadata reports.
   Include the argument "required" when creating the collection and seed scripts to only include the required fields.

 
2. Review the collection and seed metadata reports for required fields with missing values. 
   If the value is missing, it will have "NO DATA OF THIS TYPE" in the spreadsheet. 
   Use the WARC metadata report and check for unsaved test crawls in the Archive-It interface to determine if a seed will be included in this download. 
   If not, it does not need complete metadata. 

 
3. Review the WARC metadata report for any unusual activity. 
   In a few cases, we have decided not to include a website in the preservation download. 


4. Email the contacts at the collecting units with a list of the metadata to add and any questions about the WARCs being preserved. 
   Still send this email if no corrections are required as a reminder that any crawls saved in the next 2 weeks need to have complete metadata.

 
5. Verify that any missing metadata is entered prior to the download date. 
   Once all metadata is complete, the collection and seed metadata reports may be deleted. 
   Retain the WARC metadata report for now.

### Day of Download

1. Check the Crawl Reports tab on the Archive-It Crawls page. 
   If any crawls were saved in the last two weeks, create another WARC metadata report. 
   If not, continue to use the WARC metadata report created during the preparation phase of the workflow.

 
2. Use the preservation_download_tracker.py script and the WARC metadata report to create a spreadsheet for tracking the download progress. 


3. Use the [Web AIP script](https://github.com/uga-libraries/web-aip) to download the WARCs and metadata that will be preserved. 
   See the documentation in that repository for the rest of the workflow. 
   Besides using the tracking spreadsheet, the only step that involves output from these scripts is adding the WARC metadata report information to the WARC Inventory.
   
## History

This workflow has been in use since 2020, but not previously documented beyond the scripts used and a Trello card template.
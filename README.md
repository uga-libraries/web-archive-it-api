# Archive-It APIs Scripts

# Purpose and Overview
Use the Archive-It web archiving service APIs (Partner API and WASAPI) to generate reports.

# Dependencies
* Archive-It login credentials
* Python requests libraries: `pip install requests`

# Scripts
Prior to using any of these scripts, create a file named configuration.py, modeled after configuration_template.py,
and save it to your local copy of this repository.

## collection_metadata_report.py
Makes a CSV with all collection metadata in Archive-It:
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

## metadata_check_department.py
Makes CSVs of each department's (collector's) collection and seed metadata.
These reports just include the fields required by UGA>

Script usage: `python metadata_check_department.py [output_directory]`

If the path for the output directory is not provided, it uses the script output path from the configuration file.

NOTE: this is a legacy script which will be deleted once the ability to limit to a single department is added
to the collection and seed metadata reports.
It has not been updated to use the shared functions and does not have unit tests.

## seed_metadata_report.py
Makes a CSV with all seed metadata in Archive-It.
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

WARCs stored on the start_date will be included. WARCs stored on the end_date will NOT be included.

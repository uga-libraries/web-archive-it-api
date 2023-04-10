# Archive-It APIs Scripts

# Purpose and Overview
Use the Archive-It web archiving service APIs (Partner API and WASAPI) to generate reports.

# Dependencies
* Archive-It login credentials
* Python requests libraries: `pip install requests`

# Scripts
Prior to using any of these scripts, create a file configuration.py, modeled after configuration_template.py,
and save it to your local copy of this repository.

## collection_metadata_report.py
Generate a CSV with all collection metadata in Archive-It:
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
Generate reports of required collection and seed metadata fields 
to check for completeness prior to downloading the WARCs and metadata for preservation. 
Separate reports are made for each department (collector) so the results can be shared with the responsible archivist.

Script usage: `python metadata_check_department.py [output_directory]`
If the path for the output directory is not provided, it uses the script output path from the configuration file.

## seed_metadata_report.py
Generate a CSV with all seed metadata in Archive-It.
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
Makes a CSV with information about each WARC saved during a specified time frame: 
WARC Filename, AIT Collection ID, Seed ID, Crawl Job ID, Date (store-time), Size (GB), Crawl Definition ID, Seed Title.
Use instead of the WASAPI CSV download so data can be reformatted and to incorporate info from the Partner API.

Script usage: `python warc_csv.py earliest_date`
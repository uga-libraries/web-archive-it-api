# Archive-It APIs Scripts

# Purpose and Overview
Use the Archive-It web archiving service APIs (Partner API and WASAPI) to generate reports.

# Dependencies
* Archive-It login credentials
* Python requests libraries: `pip install requests`

# Scripts
Prior to using any of these scripts, create a file configuration.py, modeled after configuration_template.py,
and save it to your local copy of this repository.

## metadata_check_combined.py
Generate reports of required collection and seed metadata fields 
to check for completeness prior to downloading the WARCs and metadata for preservation.
Information for all departments is saved in one report so the library metadata can be reviewed in aggregate.

Script usage: `python metadata_check_combined.py output_directory [all_fields]`
Include "all_fields" to include optional as well as required fields in the report.

## metadata_check_department.py
Generate reports of required collection and seed metadata fields 
to check for completeness prior to downloading the WARCs and metadata for preservation. 
Separate reports are made for each department (collector) so the results can be shared with the responsible archivist.

Script usage: `python metadata_check_department.py [output_directory]`
If the path for the output directory is not provided, it uses the script output path from the configuration file.

## warc_csv.py
Makes a CSV with information about each WARC saved during a specified time frame: 
WARC Filename, AIT Collection ID, Seed ID, Crawl Job ID, Date (store-time), Size (GB), Crawl Definition ID, Seed Title.
Use instead of the WASAPI CSV download so data can be reformatted and to incorporate info from the Partner API.

Script usage: `python warc_csv.py earliest_date`
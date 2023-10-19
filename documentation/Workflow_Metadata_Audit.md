# Metadata Audit Workflow, 2023-10-18

## Overview

Collection and seed metadata in Archive-It must follow the [UGA Web Archives Metadata Profile](https://github.com/uga-libraries/web-archiving/blob/main/metadata_profile.md). 
Reports used to prepare for preservation downloads can also be used to view and batch edit collection or seed metadata.

## Workflow

1. Using the correct [API script](https://github.com/uga-libraries/web-archive-it-api), download the collection and/or seed metadata report. 
When running the scripts, add the argument “required” to only include required fields in the report. 
Otherwise, both required and optional fields will be included.


2. Compare the metadata report against the metadata profile. 

   1. Required fields should not contain "NO DATA OF THIS TYPE". 

   2. Check any field that repeats may repeat. Repeated fields contain a semicolon.

   3. Check that all fields follow the content rules.


3. Update the metadata report with the correct information. 
Involve the collecting unit if there is any uncertainty about what the correct information should be.
 The administrator may reformat metadata to meet the content rules without consulting with the collecting unit.


4. Update the metadata in Archive-It, which can be done via the interface or by uploading a CSV:
   [Add-edit-and-manage-your-metadata](https://support.archive-it.org/hc/en-us/articles/208332603-Add-edit-and-manage-your-metadata).
# Metadata Audit Workflow, 2023-10-18

## Overview

Collection and seed metadata in Archive-It must follow the [UGA Web Archives Metadata Profile](https://github.com/uga-libraries/web-archiving/blob/main/metadata_profile.md). 
Reports used to check metadata prior to preservation downloads can also be used to analyze and batch edit collection or seed metadata.

Caution: this is an intended use of the reports but has not yet been implemented in practice,
so this workflow is untested.

## Responsibility

UGA’s Archive-It Administrator (Head of Digital Stewardship) may audit that all metadata meets UGA's requirements.
Collecting units may also use this workflow to work with their own metadata.

## Workflow

1. Using the correct [API script](https://github.com/uga-libraries/web-archive-it-api), 
   download the collection and/or seed metadata report. 
   Use the optional argument “required” to only include required fields in the report, if desired.


2. Compare the metadata report against [UGA's metadata profile](https://github.com/uga-libraries/web-archiving/blob/main/metadata_profile.md). 

   - Required fields should not contain "NO DATA OF THIS TYPE". 

   - Check any field that repeats is permitted to repeat. Repeated fields contain a semicolon.

   - Check that all fields follow the content rules.


3. Update the metadata report with the correct information. 
   Involve the collecting unit if there is any uncertainty about what the correct information should be. 
   The Administrator may reformat metadata to meet the content rules without consulting with the collecting unit.


4. Update the metadata in Archive-It, which can be done via the interface or by uploading a CSV:
   [Add-edit-and-manage-your-metadata](https://support.archive-it.org/hc/en-us/articles/208332603-Add-edit-and-manage-your-metadata).
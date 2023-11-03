# BotoScripts
BotoScripts I created to automate some recurrent Infrastructure tasks

GenericFilter.py can be used to filter out EC2 resources Instances, Images, and Snapshots based on user-defined Tag keys and values and provides a .txt/.csv file. In 
use cases with large platform infrastructure with hundreds of thousands of resources (mostly images and snapshots) this can be used in an administrative ETL to filter out which resource is needed and whether lifecycle policies are being complied with or not.

GenericTagChange.py uses the above filter logic and adds another feature which is changing certain tags from the filtered resources as per business requirement. Came in very handy in an Ops task where I had to update tags of nearly 100,000 resources for newer FinOps requirements. The AWS console options let you only change about 500 resources at a time that too takes longer than what the script takes to update a few thousand resources.

GlueDatabaseTables.py is a glue crawler of sorts that lists down Glue Tables and Columns w.r.t each Database and Table respectively. The Glue API extracts only a limited number of resources and  provides a checkpoint token for the next call. This script automates recalling the API until the crawling is complete.

The mentioned scripts have been stripped of specifics for security purposes but the logic works.

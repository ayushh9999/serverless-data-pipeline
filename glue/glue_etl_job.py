import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

# Enter your bucket details below before running this job.
RAW_INPUT_PATH = "s3://<enter-your-raw-bucket-name>/extract/"
CURATED_OUTPUT_PATH = "s3://<enter-your-curated-bucket-name>/load/"

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1776450094206 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": "\"",
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={"paths": [RAW_INPUT_PATH], "recurse": True},
    transformation_ctx="AmazonS3_node1776450094206",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1776517726498 = DynamicFrame.fromDF(
    AmazonS3_node1776450094206.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1776517726498",
)

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(
    frame=DropDuplicates_node1776517726498,
    ruleset=DEFAULT_DATA_QUALITY_RULESET,
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQuality_node1776516439888",
        "enableDataQualityResultsPublishing": True,
    },
    additional_options={
        "dataQualityResultsPublishing.strategy": "BEST_EFFORT",
        "observations.scope": "ALL",
    },
)
if DropDuplicates_node1776517726498.count() >= 1:
    DropDuplicates_node1776517726498 = DropDuplicates_node1776517726498.coalesce(1)
AmazonS3_node1776518301649 = glueContext.write_dynamic_frame.from_options(
    frame=DropDuplicates_node1776517726498,
    connection_type="s3",
    format="csv",
    connection_options={"path": CURATED_OUTPUT_PATH, "partitionKeys": []},
    transformation_ctx="AmazonS3_node1776518301649",
)

job.commit()
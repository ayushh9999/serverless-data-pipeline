"""Glue ETL script placeholder.

Replace this file with your real Glue ETL code.
"""

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("csv-dedup-etl").getOrCreate()

# Replace with your real source and target paths
source_path = "s3://your-raw-bucket/input/"
target_path = "s3://your-curated-bucket/output/"

df = spark.read.option("header", True).csv(source_path)
cleaned = df.dropDuplicates()

cleaned.write.mode("overwrite").option("header", True).csv(target_path)

spark.stop()

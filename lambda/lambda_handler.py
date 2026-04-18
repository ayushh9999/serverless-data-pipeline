"""Lambda trigger script placeholder.

Replace this file with your real Lambda code.
"""

import json
import os
import boto3


glue = boto3.client("glue")
GLUE_JOB_NAME = os.getenv("GLUE_JOB_NAME", "your-glue-job-name")


def lambda_handler(event, context):
    try:
        response = glue.start_job_run(JobName=GLUE_JOB_NAME)
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "Glue job started",
                    "jobName": GLUE_JOB_NAME,
                    "jobRunId": response.get("JobRunId"),
                }
            ),
        }
    except Exception as exc:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Failed to start Glue job", "error": str(exc)}),
        }

import os

import boto3


# Enter your Glue job name in Lambda environment variables.
GLUE_JOB_NAME = os.getenv("GLUE_JOB_NAME", "<enter-your-glue-job-name>")


def lambda_handler(event, context):
    glue = boto3.client("glue")

    try:
        glue.start_job_run(JobName=GLUE_JOB_NAME)
        return {
            "statusCode": 200,
            "body": f"Successfully started Glue job {GLUE_JOB_NAME}",
        }
    except Exception as exc:
        return {
            "statusCode": 500,
            "body": f"Failed to start Glue job: {str(exc)}",
        }
       

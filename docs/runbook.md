# Runbook: Demo and Verification

Use this runbook during interviews to show the pipeline clearly.

## Preconditions

- S3 raw bucket exists and S3 event notification is configured
- Lambda function is deployed and has permission to start Glue job
- Glue job is configured with IAM role and script location
- SNS topic has at least one confirmed email subscription
- CloudWatch log groups are enabled for Lambda and Glue

## Demo Steps

1. Upload sample file
- Upload `sample-data/input.csv` to your raw S3 bucket
- Note upload timestamp

2. Verify trigger
- Open Lambda CloudWatch logs
- Confirm invocation for the new object key

3. Verify ETL run
- Open Glue job runs
- Confirm one run is triggered and completes with `SUCCEEDED`

4. Verify output
- Open target storage location
- Confirm cleaned file is generated
- Validate duplicates are removed

5. Verify alerting
- Check SNS email inbox
- Confirm success (or failure) notification is received

6. Verify observability
- Open CloudWatch metrics/logs
- Show key log lines and run duration

## Failure Path (Optional)

To show reliability, you can intentionally upload a malformed CSV and show:
- Glue or Lambda failure signal
- SNS failure alert
- Error details in CloudWatch logs

## Evidence to Capture for GitHub

Take screenshots and store in `screenshots/`:
- `lambda-log.png`
- `glue-job-success.png`
- `s3-output.png`
- `sns-alert-email.png`
- `cloudwatch-metrics.png`

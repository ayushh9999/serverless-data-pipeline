# AWS Serverless Data Pipeline (CSV ETL)

An event-driven AWS data pipeline that ingests CSV files from Amazon S3, triggers AWS Lambda, runs ETL with AWS Glue (including duplicate removal), and sends status notifications with Amazon SNS. Pipeline health and logs are monitored in Amazon CloudWatch.

## Architecture

Flow:
1. S3 receives raw CSV file.
2. Lambda is triggered by S3 object event.
3. Lambda starts Glue ETL job.
4. Glue transforms data and removes duplicates.
5. Cleaned data is written to target storage.
6. EventBridge tracks pipeline events.
7. SNS sends success or failure email notifications.
8. CloudWatch captures logs and metrics.

Add your architecture image here:
- `architecture/pipeline-architecture.png`

## AWS Services Used

- Amazon S3: Raw and curated data storage
- AWS Lambda: Event trigger and orchestration
- AWS Glue: ETL transformation and deduplication
- Amazon EventBridge: Event tracking and routing
- Amazon SNS: Email notifications
- Amazon CloudWatch: Monitoring, logs, and metrics

## Repository Structure

```text
.
|-- architecture/
|   |-- pipeline-architecture.png   # Add your diagram image
|-- lambda/
|   |-- lambda_handler.py           # Put your Lambda code here
|-- glue/
|   |-- glue_etl_job.py             # Put your Glue ETL code here
|-- sample-data/
|   |-- input.csv
|   |-- output_cleaned.csv
|-- screenshots/
|   |-- lambda-log.png
|   |-- glue-job-success.png
|   |-- s3-output.png
|   |-- sns-alert-email.png
|   |-- cloudwatch-metrics.png
|-- docs/
|   |-- runbook.md
|   |-- interview-pitch.md
|   |-- demo-checklist.md
|-- .gitignore
|-- README.md
```

## ETL Logic

Current ETL operations:
- Read CSV from raw S3 location
- Drop duplicate rows
- Basic cleaning and formatting
- Write curated output to target location

Update this section with your exact logic if you also handle:
- Null value cleanup
- Type casting
- Schema normalization
- Column selection and renaming

## How to Demonstrate (3-5 minutes)

1. Upload `sample-data/input.csv` to S3 raw bucket.
2. Show Lambda trigger in CloudWatch logs.
3. Show Glue job run status as successful.
4. Show deduplicated output file in target storage.
5. Show SNS notification email.
6. Show CloudWatch metrics/logs for observability.

Detailed steps: see `docs/runbook.md`.

## Interview Value

This project demonstrates:
- Event-driven data pipeline design
- Serverless orchestration on AWS
- ETL and data quality handling (deduplication)
- Monitoring and operational reliability

Interview pitch: see `docs/interview-pitch.md`.

## Security Notes

- No secrets, keys, or credentials are committed to this repository.
- Use IAM least-privilege roles for Lambda, Glue, and SNS.
- Parameterize environment-specific values (bucket names, job names, topic ARNs).

## Scalability and Cost

- Serverless design minimizes operational overhead.
- Pay-per-use model with Lambda/Glue/SNS.
- Event-driven processing scales with incoming file volume.

## Future Improvements

- Add schema validation before ETL
- Add dead-letter queue and retry strategy
- Add data quality checks and row-level error reporting
- Add IaC (Terraform or CloudFormation) for reproducible deployment

## Quick Start for GitHub Upload

1. Add your Lambda script to `lambda/lambda_handler.py`.
2. Add your Glue script to `glue/glue_etl_job.py`.
3. Add your architecture image to `architecture/pipeline-architecture.png`.
4. Add screenshots to `screenshots/`.
5. Commit and push:

```bash
git init
git add .
git commit -m "Initial commit: AWS serverless CSV ETL pipeline"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

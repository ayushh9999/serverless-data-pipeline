# AWS Serverless Data Pipeline (CSV ETL) 

An event-driven AWS data pipeline that ingests CSV files from Amazon S3, triggers AWS Lambda, performs ETL in AWS Glue (including duplicate removal), and provides visibility through EventBridge, SNS, and CloudWatch.

Manual CSV processing is repetitive and error-prone. This project automates ingestion, transformation, deduplication, and output publishing in a scalable serverless workflow.

## Architecture Overview 🧭

Pipeline flow:
1. **S3 (Data Source)** receives raw CSV files.
2. **Lambda (Trigger)** starts the Glue job on new file upload.
3. **Glue (ETL)** cleans data and removes duplicates.
4. **EventBridge (Event Track)** captures pipeline events.
5. **SNS (Email Notification)** sends status notifications.
6. **CloudWatch (Monitoring)** tracks logs and operational health.

Architecture diagram:

![Pipeline Architecture](architecture/pipeline-architecture.png)

## Tech Stack 🛠️

- **Amazon S3** for raw and curated data storage
- **AWS Lambda** for event-driven orchestration
- **AWS Glue** for ETL and deduplication
- **Amazon EventBridge** for event tracking
- **Amazon SNS** for email notifications
- **Amazon CloudWatch** for logs and monitoring

## ETL Logic ✅

Current ETL behavior:
- Reads CSV files from raw S3 path
- Removes duplicate records
- Writes cleaned output to curated S3 path
- Runs basic data quality checks in Glue

Config placeholders are intentionally used in code for safe public sharing.

## Real Execution Evidence 📊

From actual Glue runs:
- **Success rate:** 3/3 runs succeeded
- **Durations:** 1m 30s, 1m 32s, 1m 21s
- **Retries:** 0
- **Compute:** 10 DPUs, G.1X workers
- **Glue version:** 5.0

From curated S3 output:
- Output generated under **load/** prefix
- 3 output files produced
- Each file size is approximately **17.3 KB**

## Proof Screenshots 🖼️

Glue job run success:

![Glue Job Runs](screenshots/glue-job.png)

S3 curated output:

![S3 Output Files](screenshots/s3-load.png)

## Project Structure 📁

```text
.
|-- architecture/
|   |-- pipeline-architecture.png
|-- lambda/
|   |-- lambda_handler.py
|-- glue/
|   |-- glue_etl_job.py
|-- sample-data/
|   |-- input.csv
|   |-- output_cleaned.csv
|-- screenshots/
|   |-- glue-job.png
|   |-- s3-load.png
|-- .gitignore
|-- README.md
```

## Quick Demo Steps 🎬

1. Upload `sample-data/input.csv` to your raw S3 location.
2. Verify Lambda is invoked and Glue job starts.
3. Verify Glue run status is `Succeeded`.
4. Validate output files in curated S3 `load/` path.
5. Show screenshots in this README as proof of execution.

## Interview Summary 🎯

Built a serverless, event-driven AWS data pipeline where CSV files uploaded to S3 trigger Lambda, launch Glue ETL for deduplication, and produce curated output in S3 while maintaining observability through EventBridge, SNS, and CloudWatch.

## Security Notes 🔒

- No secrets or credentials are committed.
- Public-safe placeholders are used for bucket and job configuration.
- IAM least-privilege is recommended for production deployment.

## Future Improvements 🌱

- Add schema validation before ETL execution
- Add DLQ and retry policy for stronger fault handling
- Add Infrastructure as Code using Terraform or CloudFormation

## Publish Commands 🚀

```bash
git add .
git commit -m "Sync README with current project assets"
git push -u origin main
```

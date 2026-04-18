# Interview Pitch (60-90 seconds)

I built an event-driven AWS serverless data pipeline for CSV ingestion and ETL automation.

When a CSV lands in Amazon S3, an AWS Lambda trigger starts an AWS Glue job that transforms data and removes duplicates before writing curated output to the target storage layer.

To make the pipeline production-style, I used EventBridge for event tracking, SNS for email notifications on success or failure, and CloudWatch for logs and monitoring.

This design is scalable, low-ops, and cost-efficient because it is serverless and processes data only when new files arrive.

## Strong Follow-up Answers

### Why Glue for ETL?
Glue is managed, scalable for batch transformations, integrates well with S3, and reduces infrastructure management overhead.

### How do you handle failures?
Failures are visible in CloudWatch logs and propagated through SNS notifications; retry and DLQ can be added as next improvement.

### How do you avoid duplicate processing?
Current ETL includes deduplication at transform time; idempotent naming and event filtering can further harden this.

### What would you improve next?
Add schema validation, stronger data quality checks, IaC deployment, and automated tests for ETL logic.

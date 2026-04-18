# Demo Checklist

Use this checklist before interviews.

## Repository Readiness

- [ ] Lambda code is present in `lambda/lambda_handler.py`
- [ ] Glue code is present in `glue/glue_etl_job.py`
- [ ] Architecture image is present in `architecture/pipeline-architecture.png`
- [ ] Input and output sample CSV files are present
- [ ] Screenshots are present in `screenshots/`
- [ ] No secrets or credentials in code/history

## Runtime Readiness

- [ ] S3 event trigger is enabled
- [ ] Lambda can start Glue job
- [ ] Glue job configuration is valid
- [ ] SNS email subscription is confirmed
- [ ] CloudWatch logs are accessible

## Interview Flow Readiness

- [ ] 60-90 second pitch practiced
- [ ] Can explain service selection decisions
- [ ] Can explain deduplication logic
- [ ] Can explain monitoring and failure handling
- [ ] Can describe future improvements

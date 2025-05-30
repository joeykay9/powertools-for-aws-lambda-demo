# Timesheets API - AWS SAM Application

This directory contains the AWS SAM (Serverless Application Model) application for the Timesheets API, exposing a RESTful API via API Gateway and a Python Lambda function.

## Project Structure

- `template.yaml` - SAM template defining the Lambda function and API Gateway
- `timesheets/` - Lambda handler code and requirements
- `events/` - Sample event payloads for local testing
- `tests/` - Unit and integration tests

## Local Testing

1. **Set up a Python virtual environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install dependencies:**
   ```sh
   pip install -r timesheets/requirements.txt
   ```
3. **Run locally with SAM CLI:**
   ```sh
   sam local start-api
   ```
   This will start a local API Gateway at http://127.0.0.1:3000/timesheets

## Deployment

1. **Build the SAM application:**
   ```sh
   sam build
   ```
2. **Deploy to AWS:**
   ```sh
   sam deploy --guided
   ```
3. **Delete the stack:**
   ```sh
   sam delete
   ```

## Notes
- The SAM app is focused on the API Gateway use case and does not include Bedrock Agent integration.
- The OpenAPI schema can be generated by running the handler file directly:
   ```sh
   python timesheets/app.py
   ```
- Outputs in the deployed stack include the API endpoint and Lambda function ARN.

For more details, see the [AWS SAM documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).

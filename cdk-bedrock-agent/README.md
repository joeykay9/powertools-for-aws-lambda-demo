# Timesheets API - AWS CDK Bedrock Agent Stack

This directory contains the AWS CDK stack for deploying the Bedrock Agent integration for the Timesheets API.

## Project Structure

- `infrastructure/` - CDK stack code (infrastructure as code)
- `lambda/` - Lambda handler and its runtime dependencies
- `timesheets_openapi.json` - OpenAPI schema for the Bedrock Agent

## Local Testing

1. **Set up a Python virtual environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install CDK and Lambda dependencies:**
   ```sh
   pip install -r requirements.txt
   pip install -r lambda/requirements.txt
   ```
3. **Generate the OpenAPI schema (if needed):**
   ```sh
   python lambda/timesheets_bedrock_agent.py
   ```
   This will output `timesheets_openapi.json` in the `openapi/` directory.
4. **Synthesize the CloudFormation template:**
   ```sh
   cdk synth
   ```

## Deployment

1. **Bootstrap your AWS environment (only once per account/region):**
   ```sh
   cdk bootstrap
   ```
2. **Deploy the stack:**
   ```sh
   cdk deploy
   ```
3. **Destroy the stack:**
   ```sh
   cdk destroy
   ```

## Useful CDK Commands
- `cdk diff` - See what will change before deploying
- `cdk list` - List all stacks in the app
- `cdk doctor` - Diagnose common CDK issues

## Notes
- The Lambda function and its dependencies are packaged using the `aws_cdk.aws_lambda_python_alpha.PythonFunction` construct.
- The OpenAPI schema is uploaded to S3 for Bedrock Agent registration.
- This stack is independent from the SAM app and is focused on Bedrock Agent integration.

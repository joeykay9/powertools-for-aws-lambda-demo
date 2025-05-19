# Powertools for AWS Lambda Demo

This repository demonstrates a **dummy timesheet management API** using serverless AWS technologies.  
It includes Python Lambda functions (invoked via API Gateway or Bedrock Agent), leverages Powertools for AWS Lambda (Python), and provides both AWS SAM and CDK infrastructure examples.

> **Note:** The timesheet API and data are for demonstration and testing purposes only.

## 1. `sam-app/` — API Gateway + Lambda (AWS SAM)
- **Purpose:**
  - Showcases how to build a robust RESTful Timesheets API using AWS Lambda Powertools for observability, validation, and best practices.
  - Built and deployed using AWS Serverless Application Model (SAM).
  - Designed for traditional API Gateway use cases (CRUD, integrations, etc.).
- **Key Features:**
  - Python Lambda handler with Powertools utilities (Logger, Tracer, Metrics, Event Handler).
  - Local development and testing with `sam local start-api`.
  - No Bedrock Agent integration—focus is on Powertools patterns for REST APIs.

## 2. `cdk-bedrock-agent/` — Bedrock Agent Integration (AWS CDK)
- **Purpose:**
  - Demonstrates how Powertools can be used in a Lambda function that powers a Bedrock Agent action group.
  - Built and deployed using AWS CDK and the `cdklabs.generative-ai-cdk-constructs` library.
  - Designed for generative AI and Bedrock Agent use cases.
- **Key Features:**
  - Python Lambda handler for Bedrock Agent tool use, leveraging Powertools for observability and validation.
  - OpenAPI schema generated and stored in `openapi/timesheets_openapi.json`.
  - S3 bucket for OpenAPI schema, referenced by the Bedrock Agent.
  - Uses `cdklabs.generative-ai-cdk-constructs` to define the Bedrock Agent and action group.
  - Fully independent from the SAM app.

## Why Powertools?
- **Observability:** Structured logging, distributed tracing, and custom metrics with minimal code.
- **Validation:** Pydantic models and event handler utilities for robust input validation.
- **Best Practices:** Encourages clean, maintainable, and production-ready Lambda code.
- **Flexibility:** Works for both classic REST APIs and modern generative AI/Bedrock Agent integrations.

## How to Use
- Each app is self-contained and can be built, tested, and deployed independently.
- See the README in each subdirectory for local testing and deployment instructions.

## When to Use Which App?
- **Use `sam-app/`** to see Powertools in action for a classic REST API with API Gateway and Lambda.
- **Use `cdk-bedrock-agent/`** to see Powertools in a Lambda powering a Bedrock Agent for generative AI workflows.

---

For more details, see the individual READMEs in each app directory.

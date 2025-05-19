from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    CfnOutput,
)
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from constructs import Construct
from cdklabs.generative_ai_cdk_constructs import bedrock

class BedrockAgentStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # S3 bucket for OpenAPI schema
        schema_bucket = s3.Bucket(self, "OpenApiSchemaBucket", removal_policy=RemovalPolicy.DESTROY, auto_delete_objects=True)

        # Upload OpenAPI schema to S3
        s3deploy.BucketDeployment(
            self, "DeployOpenApiSchema",
            sources=[s3deploy.Source.asset("openapi")],
            destination_bucket=schema_bucket,
            destination_key_prefix="openapi/",
        )

        # Lambda function for Bedrock Agent tool
        timesheets_lambda = PythonFunction(
            self, "TimesheetsHandler",
            entry="lambda",  # Now points to the lambda directory
            runtime=_lambda.Runtime.PYTHON_3_12,
            index="timesheets_bedrock_agent.py",
            handler="lambda_handler",
            tracing=_lambda.Tracing.ACTIVE,
        )

        # Bedrock Agent definition
        agent = bedrock.Agent(
            self, "TimesheetsBedrockAgent",
            foundation_model=bedrock.BedrockFoundationModel.ANTHROPIC_CLAUDE_3_5_SONNET_V1_0,  # Example model, update as needed
            instruction="You are a timesheets assistant.",
            action_groups=[
                bedrock.AgentActionGroup(
                    name="TimesheetsActionGroup",
                    description="Use these functions for timesheets support",
                    executor=bedrock.ActionGroupExecutor.fromlambda_function(
                        lambda_function=timesheets_lambda,
                    ),
                    enabled=True,
                    api_schema=bedrock.ApiSchema.from_s3_file(
                        bucket=schema_bucket,
                        object_key="openapi/timesheets_openapi.json"
                    ),
                )
            ],
        )

        # Output Lambda ARN and OpenAPI schema S3 URL for Bedrock registration
        CfnOutput(self, "LambdaArn", value=timesheets_lambda.function_arn)
        CfnOutput(self, "OpenApiSchemaUrl", value=schema_bucket.url_for_object("openapi/timesheets_openapi.json"))

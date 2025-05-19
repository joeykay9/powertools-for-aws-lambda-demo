import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_bedrock_agent.cdk_bedrock_agent_stack import CdkBedrockAgentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_bedrock_agent/cdk_bedrock_agent_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkBedrockAgentStack(app, "cdk-bedrock-agent")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

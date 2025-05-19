#!/usr/bin/env python3
import os

import aws_cdk as cdk
from infrastructure.cdk_bedrock_agent_stack import BedrockAgentStack

app = cdk.App()
BedrockAgentStack(app, "BedrockAgentStack")
app.synth()

import json
from pydantic import BaseModel, Field
from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.event_handler import BedrockAgentResolver, Response

logger = Logger()
tracer = Tracer()
metrics = Metrics(namespace="TimesheetsApp")

resolver = BedrockAgentResolver()

timesheets_db = []  # In-memory store for demonstration

class Timesheet(BaseModel):
    user: str = Field(..., description="The user who submitted the timesheet.")
    hours: float = Field(..., description="Number of hours worked.", ge=0)
    date: str = Field(..., description="Date of the timesheet (YYYY-MM-DD).", pattern=r"^\d{4}-\d{2}-\d{2}$")

@resolver.get(
    "/timesheets",
    description="Retrieve all submitted timesheets.",
    summary="List timesheets",
    tags=["Timesheets"]
)
def get_timesheets():
    logger.info({"action": "list_timesheets", "count": len(timesheets_db)})
    return {"timesheets": timesheets_db}

@resolver.post(
    "/timesheets",
    description="Create a new timesheet entry.",
    summary="Create timesheet",
    tags=["Timesheets"]
)
def create_timesheet(timesheet: Timesheet):
    timesheets_db.append(timesheet.dict())
    logger.info({"action": "created_timesheet", "timesheet": timesheet.dict()})
    # Log additional metadata for Bedrock Agent
    logger.append_keys(
        session_id=resolver.current_event.session_id,
        action_group=resolver.current_event.action_group,
        input_text=resolver.current_event.input_text,
    )
    return Response(
        status_code=201,
        body=json.dumps({
            "message": "Timesheet created!",
            "timesheet": timesheet.dict()
        })
    )

@tracer.capture_lambda_handler
@logger.inject_lambda_context
@metrics.log_metrics
def lambda_handler(event, context):
    logger.info({"event": event})
    metrics.add_metric(name="TimesheetsInvocations", unit=MetricUnit.Count, value=1)
    logger.append_keys(custom_key="custom_value")
    tracer.put_annotation("LambdaFunction", "TimesheetsFunction")
    return resolver.resolve(event, context)

# Utility to generate OpenAPI schema from the BedrockAgentResolver
if __name__ == "__main__":
    openapi_path = "../openapi/timesheets_openapi.json"
    import os
    os.makedirs(os.path.dirname(openapi_path), exist_ok=True)
    with open(openapi_path, "w") as f:
        f.write(resolver.get_openapi_json_schema())
    print(f"OpenAPI schema generated: {openapi_path}")

from aws_cdk import (
    Duration,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,

    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class DataInjectionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        event_rule_target = _lambda.Function(
            self, "EventRuleCronCargaIncremental",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "DB_HOST": "database-migration.cq1xp27nrjmz.us-east-2.rds.amazonaws.com",
                "DB_USER": "admin",
                "DB_PASSWORD": "migration2023",
                "DB_NAME": "migration"
            }
        )

        rule = events.Rule(
            self, "ETLRule",
            schedule=events.Schedule.cron(
                minute="0",
                hour="2" 
            )
        )
        rule.add_target(targets.LambdaFunction(event_rule_target))

        # Asocia una política IAM a la función Lambda para permitir el acceso al bucket de S3
        event_rule_target.add_to_role_policy(
            iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=[f"arn:aws:s3:::csvdatainjection/*"]
            )
        )

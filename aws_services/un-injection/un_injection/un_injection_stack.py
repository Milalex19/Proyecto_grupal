from aws_cdk import (
    Duration,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_s3_notifications as s3_notifications,
    aws_iam as iam,

    Stack,

)
from constructs import Construct

class UnInjectionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        my_bucket = s3.Bucket(self, "UnitedNationBucket")

        my_lambda = _lambda.Function(self, "UnInjectionStackLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda.handler",
            code=_lambda.Code.from_asset("lambda")
        )
        
        s3_policy = iam.PolicyStatement(
            actions=["s3:GetObject", "s3:PutObject"],
            resources=[my_bucket.bucket_arn + "/*"]
        )

        my_lambda.add_to_role_policy(s3_policy)

        my_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3_notifications.LambdaDestination(my_lambda)
        )
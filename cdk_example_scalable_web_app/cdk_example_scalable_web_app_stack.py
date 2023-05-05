from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct


class CdkExampleScalableWebAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "Vpc", ip_addresses=ec2.IpAddresses.cidr("10.16.0.0/16"))

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkExampleScalableWebAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

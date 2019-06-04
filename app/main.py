import logging
import boto3
import click
import aiobotocore
import asyncio

logger = logging.getLogger(__name__)

loop = asyncio.get_event_loop()

class S3Broadcaster:
    def __init__(self, role_arn):
        self.role_arn = role_arn

    def get_credentials(self) -> None:
        request_args = {
            "RoleSessionName": "s3_session",
            "RoleArn": self.role_arn,
            "DurationSeconds": 3600,
        }
        client = boto3.client('sts')
        response = client.assume_role(**request_args)
        credentials = response["Credentials"]
        print(f"Received creds: {credentials}")

    async def get_async_boto(self):
        sesison = aiobotocore.get_session(loop=loop)
        client = sesison.create_client("s3")
        buckets = await client.list_buckets()
        print(f"Buckets: {buckets}")



@click.command()
@click.option('--role', help='RoleARN value')
def run(role):
    print(f"role: {role}")

    s3_client = S3Broadcaster(role)
    loop.run_until_complete(s3_client.get_async_boto())



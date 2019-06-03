import logging
import boto3
import click 

logger = logging.getLogger(__name__)


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


@click.command()
@click.option('--role', help='RoleARN value')
def run(role):
    print(f"role: {role}")

    s3_client = S3Broadcaster(role)
    s3_client.get_credentials()


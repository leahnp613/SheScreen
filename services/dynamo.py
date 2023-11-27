import boto3
import botocore

from handlers.login import login



class UsersTable:
    """Encapsulates an Amazon DynamoDB table of user data."""

    def __init__(self, table_name: str = "usersTable"):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.table = boto3.resource("dynamodb").Table(table_name)

    def get_user(self, username: str):
        """
        Gets user data from the table for a specific user.

        :param user: user.
        """
        try:
            response = self.table.get_item(Key={"username": username})
        except botocore.exceptions.ClientError as err:
            login().error(
                "Couldn't get user %s from table %s. Here's why: %s: %s",
                username,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response["Item"]
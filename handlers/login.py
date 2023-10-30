import json
from datetime import datetime, timedelta, timezone
import jwt
import pydantic
import utils
from models.users import UserIn, find_user

def handler(event, context):
    """
    This is the handler for the login endpoint. It is responsible for
    authenticating a user and returning a JWT token that can be used to
    authenticate future requests.
    """

    try:
        body = json.loads(event["body"])
    except KeyError:
        return {"statusCode": 403, "body": "Unauthorized: No body was passed"}

    try:
        user_request = UserIn.parse_obj(body)
    except pydantic.ValidationError as e:
        return {"statusCode": 403, "body": {"reason": e.errors()}}

    found_user = find_user(user_request.username)

    print(f"found user: {found_user}")

    if found_user.password != user_request.password.get_secret_value():
        return {"statusCode": 403, "body": {"reason": "incorrect password"}}

    token = utils.generate_token(found_user)

    return {"statusCode": 200, "body": {"token": token}}

# Sample event and context for testing
event = {
    "body": json.dumps({"username": "user123", "password": "password123"})
}
context = {}

result = handler(event, context)
print(result)

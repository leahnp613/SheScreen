import json
from datetime import datetime, timedelta, timezone
import jwt
import pydantic
from models.users import UserIn
from services.dynamo import UsersTable

users = UsersTable()



def login(event, context):

    """
    This is the lambda handler for the login endpoint. It is responsible for
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
        return {"statusCode": 403, "body": json.dumps({"reason": e.errors()})}
    found_user = users.get_user(user_request.username)
    print(f"found user: {found_user}")
    if not found_user:
        return {"statusCode": 404, "body": json.dumps({"reason": "user not found"})}
    found_user = UserIn.parse_obj(found_user)
    if found_user.password.get_secret_value() != user_request.password.get_secret_value():
        return {"statusCode": 403, "body": json.dumps({"reason": "incorrect password"})}
    payload = {
        "username": user_request.username,
        "exp": datetime.now(tz=timezone.utc) + timedelta(days=1),
    }
    token = jwt.encode(payload=payload, key="HERE")
    return {"statusCode": 200, "body": json.dumps({"token": token})}

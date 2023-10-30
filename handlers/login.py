import json
from datetime import datetime, timedelta, timezone
import jwt
import pydantic
import pymongo

mongo_uri = "mongodb+srv://prip889:rpc_bdq8nhk6fcx!VCR@cluster0.uet1wpt.mongodb.net/?retryWrites=true&w=majority"
database_name = "SheScreen"
collection_name = "users"

client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]


from models.users import UserIn


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
        return {"statusCode": 403, "body": json.dumps({"reason": e.errors()})}
    found_user = collection.find_one({"username": user_request.username})
    print(f"found user: {found_user}")
    if not found_user:
        return {"statusCode": 404, "body": json.dumps({"reason": "user not found"})}
    if found_user.password != user_request.password.get_secret_value():
        return {"statusCode": 403, "body": json.dumps({"reason": "incorrect password"})}
    payload = {
        "username": user_request.username,
        "exp": datetime.now(tz=timezone.utc) + timedelta(days=1),
    }
    token = jwt.encode(payload=payload, key="fuck david")
    return {"statusCode": 200, "body": json.dumps({"token": token})}

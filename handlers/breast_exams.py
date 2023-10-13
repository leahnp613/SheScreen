from datetime import datetime
import json
from pydantic import BaseModel
from models import BreastExam_Create
import json
import pymongo


mongo_uri = "mongodb+srv://leahnagarpowers:<password>@cluster0.hnmh04q.mongodb.net/?retryWrites=true&w=majority"

# Set up a MongoDB client using the Atlas connection string
client = pymongo.MongoClient(mongo_uri)
db = client["Cluster0"]  # Replace with your MongoDB database name
appointment_collection = db["appointments"]

def lambda_handler(event, context):
    http_method = event["httpMethod"]
    path_parameters = event.get("pathParameters", {})
    pk = path_parameters.get("pk")

    if http_method == "GET":
        appointment = appointment_collection.find_one({"_id": pk})
        if appointment:
            return {
                "statusCode": 200,
                "body": json.dumps(appointment),
                "headers": {"Content-Type": "application/json"}
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Appointment not found"}),
                "headers": {"Content-Type": "application/json"}
            }

    elif http_method == "DELETE":
        result = appointment_collection.delete_one({"_id": pk})
        if result.deleted_count > 0:
            return {
                "statusCode": 200,
                "body": json.dumps({"deleted": True}),
                "headers": {"Content-Type": "application/json"}
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Appointment not found"}),
                "headers": {"Content-Type": "application/json"}
            }

    elif http_method == "POST":
        content = json.loads(event["body"])
        # Update the appointment with the given content
        try: 
            request_data = BreastExam_Create(**content)
        except ValueError as e:
        result = appointment_collection.update_one({"_id": pk}, {"$set": content})
        if result.modified_count > 0:
            return {
                "statusCode":400,
                "body": json.dumps({"message": str(e)}),
                "headers": {"Content-Type": "application/json"}
            }

        result = appointment_collection.update_one({"_id": pk}, {"$set": request_data.dict()})
        if result.modified_count > 0:
            appointment = appointment_collection.find_one({"_id": pk})
            return {
                "statusCode": 200,
                "body": json.dumps(appointment),
                "headers": {"Content-Type": "application/json"}
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Appointment not found"}),
                "headers": {"Content-Type": "application/json"}
            }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"message": "Method not allowed"}),
            "headers": {"Content-Type": "application/json"}
        }

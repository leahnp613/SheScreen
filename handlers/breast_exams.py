import json
from pydantic import BaseModel
import pymongo
from models import BreastExam_Create

mongo_uri = "mongodb+srv://prip889:rpc_bdq8nhk6fcx!VCR@cluster0.uet1wpt.mongodb.net/?retryWrites=true&w=majority"

# Set up a MongoDB client using the Atlas connection string
client = pymongo.MongoClient(mongo_uri)
db = client["Cluster0"]  # Replace with your MongoDB database name
appointment_collection = db["appointments"]


def get_id(event):
    path_parameters = event.get("pathParameters", {})
    id = path_parameters.get("id")
    return id


def get_appointment(event, context):
    id = get_id(event)
    appointment = appointment_collection.find_one({"_id": id})
    if appointment:
        return {
            "statusCode": 200,
            "body": json.dumps(appointment),
            "headers": {"Content-Type": "application/json"},
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Appointment not found"}),
            "headers": {"Content-Type": "application/json"},
        }


def delete_apppointment(event, context):
    id = get_id(event)
    result = appointment_collection.delete_one({"_id": id})
    if result.deleted_count > 0:
        return {
            "statusCode": 200,
            "body": json.dumps({"deleted": True}),
            "headers": {"Content-Type": "application/json"},
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Appointment not found"}),
            "headers": {"Content-Type": "application/json"},
        }


def update_appointment(event, context):
    id = get_id(event)
    content = json.loads(event["body"])
    # Update the appointment with the given content
    try:
        request_data = BreastExam_Create(**content)
    except ValueError as e:
        result = appointment_collection.update_one({"_id": id}, {"$set": content})
    if result.modified_count > 0:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": str(e)}),
            "headers": {"Content-Type": "application/json"},
        }

    result = appointment_collection.update_one(
        {"_id": id}, {"$set": request_data.dict()}
    )
    if result.modified_count > 0:
        appointment = appointment_collection.find_one({"_id": id})
        return {
            "statusCode": 200,
            "body": json.dumps(appointment),
            "headers": {"Content-Type": "application/json"},
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Appointment not found"}),
            "headers": {"Content-Type": "application/json"},
        }

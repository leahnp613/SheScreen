import json
from pydantic import BaseModel
import pymongo
from models import BreastExam_Create
import os


def get_id(event):
    path_parameters = event["pathParameters"]
    id = path_parameters["id"]
    return id


def get_appointment(event, context):
    try:
        id = get_id(event)
    except KeyError:
        return {"statusCode": 400, "body": "Please send id"}
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
    try:
        request_data = BreastExam(**content)
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
    return {
        "statusCode": 200,
        "body": result.json(),
        "headers": {"Content-Type": "application/json"},
    }

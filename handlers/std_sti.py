import json
import pymongo
from models.stds_stis import (
    std_sti_create,
    std_sti_history,
    std_sti_update,
    std_sti_delete,
)




### CREATE STD_STI

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


def get_history(event, context):
    try:
        id = event["pathParameters"]["id"]
    except KeyError:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {"message": "Missing id; Please provide an id in the request"}
            ),
        }

    screening = collection.find_one({"id": id})

    try:
        screening = Screening(**screening)
    except pydantic.ValidationError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Validation error", "error": e.errors()}),
        }

    return {"statusCode": 200, "body": json.dumps({"screening": screening})}

import json
from datetime import datetime
from models.cancer_screening import Screening
import pymongo
import pydantic
from uuid import uuid4

# Define the MongoDB connection information
mongo_uri = "mongodb+srv://prip889:rpc_bdq8nhk6fcx!VCR@cluster0.uet1wpt.mongodb.net/?retryWrites=true&w=majority"
database_name = "SheScreen"
collection_name = "cancerScreening"

# Initialize a PyMongo client
client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]


### CREATE SCREENING


def create_screening(event, context):
    # Parse the JSON data from the event
    try:
        data = json.loads(event["body"])
    except KeyError:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {"message": "Missing body; Please provide a body in the request"}
            ),
        }

    # Create an instance of the model for validation
    try:
        screening_data = Screening(**data, id=str(uuid4()))
    # Check if the data is valid
    except pydantic.ValidationError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Validation error", "error": e.errors()}),
        }

    collection.insert_one(screening_data.dict())

    response = {"statusCode": 200, "body": screening_data.json()}

    return response


### HISTORY OF CANCER SCREENING


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


### UPDATE CERVICAL SCREENING


def update_cervical_screening(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event["body"])

        # Create an instance of the model for request validation
        update_request = cervical_cancer_update(**data)

        # Check if the request is valid
        if update_request:
            # Define the filter to find the record based on the patient ID
            filter_criteria = {"patient_id": update_request.patient_id}

            # Define the update data
            update_data = {
                "$set": {
                    "result": update_request.new_result,
                    "comments": update_request.new_comments,
                }
            }

            # Update all records matching the patient ID
            result = collection.update_many(filter_criteria, update_data)

            if result.modified_count > 0:
                response = {
                    "statusCode": 200,
                    "body": json.dumps(
                        {"message": "Cervical screening records updated successfully."}
                    ),
                }
            else:
                response = {
                    "statusCode": 404,
                    "body": json.dumps({"error": "No records found for update."}),
                }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid update request format."}),
            }
    except Exception as e:
        # Handle any errors that occur during processing
        response = {"statusCode": 400, "body": json.dumps({"error": str(e)})}

    return response


#### DELETE CERVICAL SCREENING


def delete_cervical_screening(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event["body"])

        # Create an instance of the model for request validation
        delete_request = cervical_cancer_delete(**data)

        # Check if the request is valid
        if delete_request:
            # Define the filter to find the record based on the patient ID and screening date
            filter_criteria = {
                "patient_id": delete_request.patient_id,
                "screening_date": delete_request.screening_date,
            }

            # Delete the matching record from the MongoDB collection
            result = collection.delete_one(filter_criteria)

            if result.deleted_count == 1:
                response = {
                    "statusCode": 200,
                    "body": json.dumps(
                        {"message": "Cervical screening record deleted successfully."}
                    ),
                }
            else:
                response = {
                    "statusCode": 404,
                    "body": json.dumps({"error": "Record not found for deletion."}),
                }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid delete request format."}),
            }
    except Exception as e:
        # Handle any errors that occur during processing
        response = {"statusCode": 400, "body": json.dumps({"error": str(e)})}

    return response

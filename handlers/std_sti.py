import json
import pymongo
from models.stds_stis import (
    std_sti_create,
    std_sti_history,
    std_sti_update,
    std_sti_delete
)

mongo_uri = "mongodb+srv://prip889:<password>@cluster0.uet1wpt.mongodb.net/?retryWrites=true&w=majority"
database_name = "your_database_name"
collection_name = "cervical_screening_history"

# Initialize a PyMongo client
client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]


### CREATE STD_STI


def lambda_handler(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event['body'])

        # Create an instance of the model for data validation
        std_sti_data = std_sti_create(**data)

        # Check if the data is valid
        if std_sti_data:
            # Convert the Pydantic model to a dictionary for database insertion
            data_to_insert = std_sti_data.dict()

            # Insert the data into the MongoDB collection
            collection.insert_one(data_to_insert)

            response = {
                "statusCode": 200,
                "body": json.dumps({"message": "STD/STI record created successfully."})
            }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid data format."})
            }
    except Exception as e:
        # Handle any errors that occur during processing
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    return response


### HISTORY

def lambda_handler(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event['body'])

        # Create an instance of the model for data validation
        std_sti_data = std_sti_history(**data)

        # Check if the data is valid
        if std_sti_data:
            # Convert the Pydantic model to a dictionary for database insertion
            data_to_insert = std_sti_data.dict()

            # Insert the data into the MongoDB collection
            collection.insert_one(data_to_insert)

            response = {
                "statusCode": 200,
                "body": json.dumps({"message": "STD/STI history record created successfully."})
            }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid data format."})
            }
    except Exception as e:
        # Handle any errors that occur during processing
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    return response

### UPDATE


#### update keeps leaving a part of code to manually update data but we want the user to be able to update the data
#need to fgiure this out

def lambda_handler(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event['body'])

        # Create an instance of the model for request validation
        delete_request = std_sti_delete(**data)

        # Check if the request is valid
        if delete_request:
            # Define the filter to find the record based on the patient ID
            filter_criteria = {
                'patient_id': delete_request.patient_id
            }

            # Delete the matching record from the MongoDB collection
            result = collection.delete_one(filter_criteria)

            if result.deleted_count == 1:
                response = {
                    "statusCode": 200,
                    "body": json.dumps({"message": "STD/STI record deleted successfully."})
                }
            else:
                response = {
                    "statusCode": 404,
                    "body": json.dumps({"error": "Record not found for deletion."})
                }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid delete request format."})
            }
    except Exception as e:
        # Handle any errors that occur during processing
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    return response

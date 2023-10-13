import json
from datetime import datetime
from models.cancer_screening import (
    cervical_cancer_create,
    cervical_cancer_history,
    cervical_cancer_update,
    cervical_cancer_delete
)
import pymongo

# Define the MongoDB connection information
mongo_uri = "mongodb+srv://prip889:<password>@cluster0.uet1wpt.mongodb.net/?retryWrites=true&w=majority"
database_name = "your_database_name"
collection_name = "cervical_screening_history"

# Initialize a PyMongo client
client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]


### CREATE CERVICAL SCREENING


def lambda_handler(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event['body'])

        # Create an instance of the model for validation
        screening_data = cervical_cancer_create(**data)

        # Check if the data is valid
        if screening_data:
            # Process the data or perform further actions
            # For example, you can store it in a database
            # Replace this with your actual processing logic
            response = {
                "statusCode": 200,
                "body": json.dumps({"message": "Data received and processed successfully."})
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



### HISTORY OF CERVICAL SCREENING


def lambda_handler(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event['body'])

        # Create an instance of the model for validation
        screening_data = cervical_cancer_history(**data)

        # Check if the data is valid
        if screening_data:
            # Prepare the data for MongoDB insertion
            data_to_insert = {
                'date': screening_data.screening_date,
                'time': screening_data.screening_time,
                'provider_questions': screening_data.result
            }

            # Insert the data into the MongoDB collection
            collection.insert_one(data_to_insert)

            response = {
                "statusCode": 200,
                "body": json.dumps({"message": "Cervical screening history data stored successfully."})
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



### UPDATE CERVICAL SCREENING


def lambda_handler(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event['body'])

        # Create an instance of the model for request validation
        update_request = cervical_cancer_update(**data)

        # Check if the request is valid
        if update_request:
            # Define the filter to find the record based on the patient ID
            filter_criteria = {
                'patient_id': update_request.patient_id
            }

            # Define the update data
            update_data = {
                '$set': {
                    'result': update_request.new_result,
                    'comments': update_request.new_comments
                }
            }

            # Update all records matching the patient ID
            result = collection.update_many(filter_criteria, update_data)

            if result.modified_count > 0:
                response = {
                    "statusCode": 200,
                    "body": json.dumps({"message": "Cervical screening records updated successfully."})
                }
            else:
                response = {
                    "statusCode": 404,
                    "body": json.dumps({"error": "No records found for update."})
                }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid update request format."})
            }
    except Exception as e:
        # Handle any errors that occur during processing
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    return response


#### DELETE CERVICAL SCREENING

def lambda_handler(event, context):
    try:
        # Parse the JSON data from the event
        data = json.loads(event['body'])

        # Create an instance of the model for request validation
        delete_request = cervical_cancer_delete(**data)

        # Check if the request is valid
        if delete_request:
            # Define the filter to find the record based on the patient ID and screening date
            filter_criteria = {
                'patient_id': delete_request.patient_id,
                'screening_date': delete_request.screening_date
            }

            # Delete the matching record from the MongoDB collection
            result = collection.delete_one(filter_criteria)

            if result.deleted_count == 1:
                response = {
                    "statusCode": 200,
                    "body": json.dumps({"message": "Cervical screening record deleted successfully."})
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

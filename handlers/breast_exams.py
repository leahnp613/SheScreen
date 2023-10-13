from datetime import datetime
import json
import pydantic

import json
import pymongo

# Replace with your MongoDB Atlas connection string
# Example connection string format: mongodb+srv://<username>:<password>@<cluster>/<dbname>?retryWrites=true&w=majority
mongo_uri = "YOUR_MONGODB_ATLAS_CONNECTION_STRING"

# Set up a MongoDB client using the Atlas connection string
client = pymongo.MongoClient(mongo_uri)
db = client["your_database_name"]  # Replace with your MongoDB database name
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
        result = appointment_collection.update_one({"_id": pk}, {"$set": content})
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



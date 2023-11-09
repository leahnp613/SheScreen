from pymongo import MongoClient
from utils.mongodb import clientPromise

async def main():
# Connect to the MongoDB database
    client = await clientPromise
    db = client.Users  # Use your desired database name

    # Get all actors from the 'actors' collection
    UserInfo = list(db.UserInfo.find({}))  # Retrieve all documents from the 'UserInfo' collection

    # Insert a new document into the 'actors' collection
    document_to_insert = {"username": "priya",
                        "password": "patel" }  # Define the document to insert
    db.UserInfo.insert_one(document_to_insert)

    # Update a document in the 'actors' collection
    update_filter = {"field": "value"}  # Define the filter for the document to update
    update_data = {"$set": {"field": "new_value"}}  # Define the update operation
    db.UserInfo.update_one(update_filter, update_data)


# Import the required libraries
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from typing import Any, List
from utils.mongodb import clientPromise  # Import your MongoDB clientPromise

async def main():
    # Establish a MongoDB connection using clientPromise
    client = await clientPromise

    # Let MongoDB know which database we want (replace 'dmTools' with your desired database name)
    db: Database = client.UserInfo

    # Get all actors from the 'actors' collection
    actors: Collection = db.actors
    actors_data: List[dict] = actors.find({})  # Retrieve all documents from the 'actors' collection

    # Insert a new document into the 'actors' collection
    document_to_insert: dict = {"username": "value"}  # Define the document to insert
    actors.insert_one(document_to_insert)

    # Update a document in the 'actors' collection
    update_filter: dict = {"field": "value"}  # Define the filter for the document to update
    update_data: dict = {"$set": {"field": "new_value"}}  # Define the update operation
    actors.update_one(update_filter, update_data)

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
